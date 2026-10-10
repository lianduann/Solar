"""Separately versioned finance scenarios (2026-10-09), placed beside - never replacing - the frozen panel-edition results.

  A. Credit-base scenarios: original panel illustration (OCC+GCC) kept for tracking; OCC-only base (author-approved analytical
     assumption, not a qualification finding); scope check removing PVSCM substation/transmission/network-upgrade shares; timing,
     PWA and transfer-price variants. Pre-tax unlevered convention of the frozen model (credit as a cash receipt; no depreciation).
  B. Hub-settled VPPA route: physical sale at TAYGETE2_ALL, financial swap at HB_WEST, contract volume H = metered output G
     (as-generated), strike K nominal flat, tenor 10 or 15 years, then merchant node tail. Fees and RECs are missing inputs -> 0
     and labelled. Dispatch and negative-hub-price clauses are explicit switches.
  C. CPI-harmonised scenario: 2023 and 2024 price paths restated to 2025 USD with BLS CPI-U annual averages, beside the frozen
     outputs that reused nominal prices as real.

Cost side (capex, FOM, year-16 replacement, year-30 decommissioning), degradation, discounting and calendar are taken unchanged
from the frozen node_base annual cash flows and reproduced before use (assertions). No regression, resampling or weather simulation.
Usage: 09_finance_scenarios.py <project_root> <out_dir>
"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
PAN = ROOT / "Deliverables/2026-10-09_Panel-Revision-Client-Edition/data"
INFL = 0.025; D = 0.007; YEARS = np.arange(1, 31); RATES = (0.0427, 0.06, 0.08)
CPI = {2023: 304.702, 2024: 313.689, 2025: 321.943}
log = {}

# ---------- frozen cost side, reproduced ----------
cf = pd.read_csv(PAN / "scenario_annual_cash_flows.csv"); nb = cf[cf.scenario_id == "node_base"].sort_values("t")
cost = -(nb.fom_real + nb.major_replacement_real + nb.decommissioning_real + nb.capex_real).to_numpy()  # positive costs by t=0..30
tt = nb.t.to_numpy()
def kcost(r): return float((cost / (1 + r) ** tt).sum())
met = pd.read_csv(PAN / "scenario_metrics.csv").set_index("scenario_id")
pc = json.load(open(PAN / "panel/Panel-Calculations.json"))
assert abs(kcost(0.0427) - pc["K"]) < 1.0, (kcost(0.0427), pc["K"])
deg = (1 - D) ** (YEARS - 1)
rev_frozen = nb[nb.t >= 1].revenue_real.to_numpy()
iv = pd.read_csv(ROOT / "Deliverables/2026-10-09_Finance-Scenario-Versions/data/Node-Hub-Intervals-2023-2025.csv.gz")
def node_rev1(y, f=1.0):
    d = iv[(iv.year == y) & iv.p_node.notna()]; on = d.p_node >= 0
    return float((d.energy_mwh[on] * d.p_node[on]).sum() * f)
r1 = node_rev1(2025)
assert np.allclose(rev_frozen, r1 * deg, rtol=1e-9), "degradation/revenue path differs from frozen"
for r in RATES:
    npv = float(((r1 * deg) / (1 + r) ** YEARS).sum() - kcost(r)); col = f"npv_real_at_{r:.4f}"
    assert abs(npv - met.loc["node_base", col]) < 1.0, (r, npv, met.loc["node_base", col])
log["frozen_reproduction"] = dict(K_cost_4p27=kcost(0.0427), node_rev_yr1=r1, node_base_npv_4p27=float(met.loc["node_base", "npv_real_at_0.0427"]), status="reproduced within 1 USD")

# ---------- A. credit-base scenarios ----------
capex, occ, gcc = pc["capex"], pc["occ"], pc["gcc"]
assert abs(0.30 * capex * (1 + INFL) - pc["credit_nominal_2027"]) < 1 and abs(pc["credit_nominal_2027"] / (1 + INFL) ** 2 / 1.0427 - pc["credit_pv"]) < 1
items = pd.read_csv(PAN / "supplement/A/A_pvscm_item_level_pv_only.csv")
tot = pd.read_csv(PAN / "supplement/A/A_cost_components_pvscm_2025Q1_pv_only.csv")
total_mmp = float(tot[(tot.category == "TOTAL") & (tot.price_basis == "MMP")].usd_per_kwdc.iloc[0])
gi = items[(items.category == "EBOS") & items.item.isin(["Substation", "Transmission", "Network Upgrade"])]
grid_share = float(gi.mmp_per_kwdc.sum() / total_mmp) if "mmp_per_kwdc" in gi else float(gi.mmp_usd_per_kwdc.sum() / total_mmp)
soft = tot[(tot.price_basis == "MMP") & tot.category.isin(["Fieldwork", "Officework", "Other"])].share_of_total.sum()
rowsA = []
def credit(base_real, rate=0.30, recv_t=1, price=1.0, r=0.0427):
    nominal = base_real * (1 + INFL) * rate * price           # 2026 nominal base (construction year), fixed nominal receipt
    real = nominal / (1 + INFL) ** (recv_t + 1)               # 2025 USD: receipt calendar year 2026+recv_t
    return nominal, real, real / (1 + r) ** recv_t
bases = [("A0_original_panel_OCC+GCC", capex, "Original panel illustration kept for tracking; includes grid connection, which 48E(b)(1)(B) excludes above 5 MWac"),
         ("A1_OCC_only", occ, "Author-approved analytical assumption: OCC as the credit base; does not establish that every OCC item qualifies"),
         ("A2_OCC_less_PVSCM_grid_items", occ * (1 - grid_share), f"Scope check: removes the PVSCM 2025Q1 share of substation, generator transmission line and network upgrade ({grid_share:.2%} of PVSCM total) in case ATB OCC still embeds them; may double-exclude if ATB already moved them to GCC")]
for bid, b, note in bases:
    for (vid, rate, t, price, vnote) in [("base", 0.30, 1, 1.0, "30% (PWA met), cash at end-2027, full value"),
                                          ("recv_end2028", 0.30, 2, 1.0, "30%, cash one year later (end-2028)"),
                                          ("transfer_0.95", 0.30, 1, 0.95, "30%, transferred at 0.95 per credit dollar (assumed; no market price retained)"),
                                          ("transfer_0.90", 0.30, 1, 0.90, "30%, transferred at 0.90 (assumed)"),
                                          ("pwa_not_met_6pct", 0.06, 1, 1.0, "6% base rate if prevailing wage/apprenticeship not met")]:
        for r in RATES:
            n, re_, pv = credit(b, rate, t, price, r)
            rowsA.append(dict(scenario=bid, variant=vid, discount_rate=r, credit_base_real_2025usd=b, credit_base_nominal_2026usd=b * (1 + INFL), credit_rate=rate, transfer_price=price,
                              receipt_year=2026 + t, credit_cash_nominal=n, credit_cash_real_2025usd=re_, credit_pv=pv,
                              node_npv_frozen=float(met.loc["node_base", f"npv_real_at_{r:.4f}"]), node_npv_with_credit=float(met.loc["node_base", f"npv_real_at_{r:.4f}"]) + pv,
                              fixed_npv_frozen=float(met.loc["fixed_base", f"npv_real_at_{r:.4f}"]), fixed_npv_with_credit=float(met.loc["fixed_base", f"npv_real_at_{r:.4f}"]) + pv,
                              status="eligibility unproven (placed in service by 2027-12-31, MACR >= 40/45%, PWA, item-level basis)", note=f"{note}; {vnote}"))
A = pd.DataFrame(rowsA); A.to_csv(OUT / "Credit-Base-Scenarios.csv", index=False, float_format="%.6f")
chk = A[(A.scenario == "A0_original_panel_OCC+GCC") & (A.variant == "base") & (A.discount_rate == 0.0427)].iloc[0]
assert abs(chk.credit_pv - pc["credit_pv"]) < 1 and abs(chk.node_npv_with_credit - pc["node_npv_with_credit"]) < 1
log["credit"] = dict(grid_item_share_pvscm=grid_share, soft_cost_share_pvscm=float(soft), original_reproduced=True)

# ---------- B. VPPA route ----------
def vppa(year, K_nom, tenor, dispatch, clause, r, cpi=True, esc=0.0, details=False):
    d = iv[(iv.year == year) & iv.p_node.notna() & iv.p_hub.notna()]
    f = CPI[2025] / CPI[year] if cpi else 1.0
    G = d.energy_mwh.to_numpy(); pn = d.p_node.to_numpy() * f; ph = d.p_hub.to_numpy() * f
    settle = np.ones_like(ph, bool) if clause == "settle_through" else (ph >= 0)
    rev = np.zeros(30); hedge_y = np.zeros(30); mwh = np.zeros(30)
    for i, t in enumerate(YEARS):
        if t <= tenor:
            Kr = K_nom * (1 + esc) ** (t - 1) / (1 + INFL) ** (t + 1)
            h = np.where(settle, Kr - ph, 0.0)
            on = (pn >= 0) if dispatch == "stop_if_node_negative" else (pn + h >= 0)
            hedge_y[i] = (G[on] * h[on]).sum() * deg[i]
        else:
            on = pn >= 0
        rev[i] = (G[on] * pn[on]).sum() * deg[i] + hedge_y[i]; mwh[i] = G[on].sum() * deg[i]
    disc = (1 + r) ** -YEARS
    out = dict(npv=float((rev * disc).sum() - kcost(r)), pv_revenue_contract_years=float((rev * disc)[:tenor].sum()), pv_revenue_tail_years=float((rev * disc)[tenor:].sum()),
               pv_hedge_settlement=float((hedge_y * disc).sum()), yr1_revenue=float(rev[0]), yr1_mwh=float(mwh[0]), yr1_realised_usd_mwh=float(rev[0] / mwh[0]), yr1_hedge_net=float(hedge_y[0]))
    return out
def breakeven(year, tenor, dispatch, clause, r, cpi=True):
    lo, hi = 0.0, 400.0
    if vppa(year, hi, tenor, dispatch, clause, r, cpi)["npv"] < 0: return np.nan
    for _ in range(60):
        mid = (lo + hi) / 2
        if vppa(year, mid, tenor, dispatch, clause, r, cpi)["npv"] >= 0: hi = mid
        else: lo = mid
    return hi
z = vppa(2025, 40, 0, "stop_if_node_negative", "settle_through", 0.0427)
assert abs(z["npv"] - met.loc["node_base", "npv_real_at_0.0427"]) < 20, z["npv"]   # tenor 0 == frozen node route (unpriced-hub intervals excluded)
log["vppa_tenor0_check"] = dict(npv=z["npv"], frozen=float(met.loc["node_base", "npv_real_at_0.0427"]))
rowsB, rowsBE = [], []
paths = [(2025, True, "2025 prices (frozen base path)"), (2024, True, "2024 prices restated to 2025 USD (CPI)"), (2023, True, "2023 prices restated to 2025 USD (CPI)"),
         (2024, False, "2024 nominal reused as real (frozen convention)"), (2023, False, "2023 nominal reused as real (frozen convention)")]
for (y, cpi, plab) in paths:
    for tenor in (10, 15):
        for dispatch in ("stop_if_node_negative", "run_if_node_plus_hedge_nonnegative"):
            for clause in ("settle_through", "suspend_if_hub_negative"):
                for r in RATES:
                    for K in (40.0, 49.0):
                        o = vppa(y, K, tenor, dispatch, clause, r, cpi)
                        rowsB.append(dict(price_path=plab, price_year=y, cpi_restated=cpi, tenor_years=tenor, strike_nominal_flat=K,
                                          strike_source="40 = frozen hypothetical fixed price; 49 = LevelTen ERCOT solar P25 offer Q4 2025 (secondary; tenor not visible) - both assumptions",
                                          dispatch=dispatch, negative_hub_clause=clause, discount_rate=r, volume_rule="H = G (as-generated)", fees_usd=0, rec_usd=0,
                                          tail="merchant at TAYGETE2_ALL using the same historical path (scenario, not a forecast)", **o))
                    rowsBE.append(dict(price_path=plab, price_year=y, cpi_restated=cpi, tenor_years=tenor, dispatch=dispatch, negative_hub_clause=clause, discount_rate=r,
                                       breakeven_strike_nominal_flat=breakeven(y, tenor, dispatch, clause, r, cpi)))
B = pd.DataFrame(rowsB); B.to_csv(OUT / "VPPA-Route-Scenarios.csv", index=False, float_format="%.4f")
BE = pd.DataFrame(rowsBE); BE.to_csv(OUT / "VPPA-Breakeven-Strikes.csv", index=False, float_format="%.4f")

# ---------- C. CPI-harmonised scenario ----------
a = float(((1 - D) ** (YEARS - 1) / 1.0427 ** YEARS).sum()); assert abs(a - pc["a"]) < 1e-9
nhc = pd.read_csv(PAN / "panel/Node-Hub-Comparisons.csv")
rowsC = []
for _, x in nhc.iterrows():
    f = CPI[2025] / CPI[int(x.price_year)]
    npv_rep = a * x.rev_stop_negative_usd - pc["K"]
    rowsC.append(dict(scope="reference points (panel table)", point=x.node, price_year=int(x.price_year), cpi_factor_to_2025=f, revenue_yr1_frozen=x.rev_stop_negative_usd,
                      revenue_yr1_cpi=x.rev_stop_negative_usd * f, npv_4p27_frozen=x.npv_4p27, npv_4p27_reproduced=npv_rep, npv_4p27_cpi=a * x.rev_stop_negative_usd * f - pc["K"],
                      difference=a * x.rev_stop_negative_usd * (f - 1)))
C1 = pd.DataFrame(rowsC)
assert (abs(C1.npv_4p27_frozen - C1.npv_4p27_reproduced) < 5).all()
tail = pd.read_csv(PAN / "empirical/C_tail_results_by_node_year.csv")
tail = tail[tail.tier == "strict"].drop_duplicates(["node", "year"])
tail["f"] = tail.year.map(lambda y: CPI[2025] / CPI[int(y)]); tail["npv_cpi"] = a * tail.rev_raw * tail.f - pc["K"]
assert (abs(a * tail.rev_raw - pc["K"] - tail.npv_raw) < 5).all()
rowsC2 = []
for y, g in tail.groupby("year"):
    rowsC2.append(dict(scope="strict node sample (frozen empirical)", point=f"{g.node.nunique()} nodes", price_year=int(y), cpi_factor_to_2025=CPI[2025] / CPI[int(y)],
                       npv_4p27_frozen_median=g.npv_raw.median(), npv_4p27_cpi_median=g.npv_cpi.median(), share_positive_frozen=(g.npv_raw > 0).mean(), share_positive_cpi=(g.npv_cpi > 0).mean(),
                       difference_median=g.npv_cpi.median() - g.npv_raw.median()))
C2 = pd.DataFrame(rowsC2)
pd.concat([C1, C2], ignore_index=True).to_csv(OUT / "CPI-Harmonised-Scenario.csv", index=False, float_format="%.4f")
log["cpi"] = dict(factors={y: CPI[2025] / CPI[y] for y in (2023, 2024)}, a=a, node_sample_rows=len(tail))
json.dump(log, open(OUT / "scenario_build_log.json", "w"), indent=1, default=float)
print(json.dumps(log, indent=1, default=float))
print(A[(A.variant == "base") & (A.discount_rate == 0.0427)][["scenario", "credit_base_real_2025usd", "credit_cash_nominal", "credit_pv", "node_npv_with_credit", "fixed_npv_with_credit"]].round(0).to_string())
print(BE[(BE.discount_rate == 0.0427)].round(2).to_string())
print(C2.round(3).to_string())
