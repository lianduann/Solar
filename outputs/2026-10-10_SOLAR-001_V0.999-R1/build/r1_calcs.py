"""SOLAR-001 V0.999-R1 - the three R1 additions, as transparent arithmetic on existing report outputs and public inputs.

  1. Production-credit (PTC) illustration: present value of a 10-year credit on the base paid/delivered volume, added to
     the report's existing pre-tax NPVs, and the implied fixed-route break-even. Uses only V0.999 report figures plus the
     2025 section 45Y applicable amount. Not an after-tax valuation and not an eligibility finding.
  2. Storage screen: perfect-foresight upper bound on daily 4-hour energy arbitrage for 1 MW / 4 MWh, from the report's own
     2025 reference-node interval prices and 2023-2025 HB_BUSAVG hourly means, set against Lazard LCOS v11.0 cost inputs.
  3. Market reference table: public ERCOT offer indices and market-monitor observations, copied with their sources.

No model in build/upstream is rerun; the six baseline scenarios and every V0.999 estimate are unchanged.
Outputs: data/r1/PTC-Illustration.csv, data/r1/Storage-Screen.csv, data/r1/Storage-Cost.csv, data/r1/R1-Calcs.json
Usage: python3 build/r1_calcs.py
"""
import json
from pathlib import Path
import pandas as pd

PKG = Path(__file__).resolve().parents[1]
OUT = PKG / "data" / "r1"; OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- inputs taken from the V0.999 report (sections cited)
R = 0.0427                 # real discount rate (10.1)
GWH_Y1 = 247.8195          # first-year delivered (node) / paid (fixed) energy, GWh (10.3, 10.4)
DEG = 0.007                # annual degradation from operating year 2 (Table 9-1)
NPV_NODE = -85.97          # node base NPV, $m (8.2; -86.0 rounded)
NPV_FIXED = -38.36 - 35.38 # fixed base NPV, $m, recovered from 10.8 (credit case minus credit PV) = -73.74
BE_FIXED = 65.97           # fixed-route flat nominal break-even, 15.24% unpaid (10.3)
ITC_PV = 35.38             # illustrative 30% ITC on OCC, PV $m (10.8)
SLOPE = -NPV_FIXED / (BE_FIXED - 40.0)  # $m NPV per $1/MWh of flat nominal price on the fixed route (linear)
# check: the slope reproduces the report's ITC break-even of $53.51/MWh
assert abs((BE_FIXED - ITC_PV / SLOPE) - 53.51) < 0.01

# ---------------------------------------------------------------- 1. PTC illustration
# 2025 section 45Y applicable amounts (IRS, FR Doc. 2025-16249, 25 Aug 2025): 3.0 cents/kWh if prevailing-wage and
# apprenticeship (PWA) rules are met, 0.6 cents otherwise; inflation-indexed, so held constant in real 2025 dollars here.
rows = []
for label, rate, price in [("Full rate (PWA met), retained by owner", 30.0, 1.00),
                           ("Full rate, transferred at $0.90 per credit dollar", 30.0, 0.90),
                           ("Base rate (PWA not met)", 6.0, 1.00)]:
    pv = sum(GWH_Y1 * 1000 * (1 - DEG) ** (t - 1) * rate * price / (1 + R) ** t for t in range(1, 11)) / 1e6
    rows.append(dict(variant=label, credit_usd_per_mwh_2025=rate, value_per_credit_dollar=price, credit_years=10,
                     pv_usd_m=round(pv, 2), node_base_npv_plus_credit_usd_m=round(NPV_NODE + pv, 2),
                     fixed_base_npv_plus_credit_usd_m=round(NPV_FIXED + pv, 2),
                     fixed_route_breakeven_usd_mwh=round(BE_FIXED - pv / SLOPE, 2)))
ptc = pd.DataFrame(rows); ptc.to_csv(OUT / "PTC-Illustration.csv", index=False)

# ---------------------------------------------------------------- 2. storage screen
def daily_upper_bound(df, date_col, price_col, eta):
    """Per day: discharge in the 4 highest-price hours, charge in the 4 lowest; order within the day ignored (upper bound)."""
    g = df.groupby(date_col)[price_col]
    v = g.apply(lambda s: max(0.0, eta * s.nlargest(4).sum() - s.nsmallest(4).sum()))
    return v.sum() / 1000.0, int(v.size)   # $/kW-yr for 1 MW / 4 MWh, days

series = []
node = pd.read_csv(PKG / "data/interval_energy_price_2025.csv", usecols=["DeliveryDate", "DeliveryHour", "price_usd_mwh", "price_available"])
node = node[node.price_available].groupby(["DeliveryDate", "DeliveryHour"], as_index=False).price_usd_mwh.mean()
series.append(("TAYGETE2_ALL reference node", 2025, node, "DeliveryDate", "price_usd_mwh"))
hub = pd.read_csv(PKG / "data/empirical/plot_inputs/F6_hourly_HB_BUSAVG_and_system_solar.csv")
hub["day"] = (pd.to_datetime(hub.utc, utc=True) - pd.Timedelta(hours=6)).dt.date   # fixed UTC-6 key, as in Appendix B.1
for y in (2023, 2024, 2025):
    series.append(("HB_BUSAVG hub", y, hub[hub.year == y], "day", "HB_BUSAVG_hourly_mean_usd_mwh"))
srows = []
for name, y, df, dc, pc in series:
    lo, n = daily_upper_bound(df, dc, pc, 0.86); hi, _ = daily_upper_bound(df, dc, pc, 0.92)
    srows.append(dict(price_series=name, year=y, days=n, upper_bound_usd_kw_yr_eta86=round(lo, 1), upper_bound_usd_kw_yr_eta92=round(hi, 1)))
scr = pd.DataFrame(srows); scr.to_csv(OUT / "Storage-Screen.csv", index=False)

# Lazard LCOS v11.0 (July 2026), utility-scale standalone 4-hour: capital $270-365/kWh, storage O&M $3.75-7.75/kWh-yr,
# 20-year life. Annualized with a capital-recovery factor; warranty expense, augmentation and charging losses beyond the
# round-trip efficiency are excluded, so the cost is understated rather than overstated.
def crf(r, n=20): return r / (1 - (1 + r) ** -n)
crows = []
for r in (0.0427, 0.06, 0.08):
    lo = 4 * 270 * crf(r) + 4 * 3.75; hi = 4 * 365 * crf(r) + 4 * 7.75
    crows.append(dict(real_discount_rate=r, capital_recovery_factor=round(crf(r), 4), annual_cost_low_usd_kw_yr=round(lo, 1), annual_cost_high_usd_kw_yr=round(hi, 1)))
cost = pd.DataFrame(crows); cost.to_csv(OUT / "Storage-Cost.csv", index=False)

summary = dict(slope_usd_m_per_usd_mwh=round(SLOPE, 4), fixed_base_npv_usd_m=round(NPV_FIXED, 2),
               ptc=ptc.to_dict("records"), storage_screen=scr.to_dict("records"), storage_cost=cost.to_dict("records"))
(OUT / "R1-Calcs.json").write_text(json.dumps(summary, indent=1))
print(ptc.to_string(index=False)); print(scr.to_string(index=False)); print(cost.to_string(index=False))
