"""Redraw every exhibit of the Integrated Research Release Candidate v0.4 from packaged, frozen tables, under one visual theme (scripts/chart_theme.py).
RENDERING ONLY: no regression, simulation, decomposition, bootstrap or research pipeline is run. Permitted display operations: selecting documented rows, sorting, unit scaling,
hourly/monthly grouping of retained interval tables exactly as the original figure code did, and cumulative sums of already-ranked plot inputs (data/empirical/plot_inputs).
Usage (from the package root or anywhere):  python3 -P scripts/render_all_figures.py [--out DIR]   Output: figures/*.png (original names), figures/empirical/F*.png, figures/vector/*.pdf, support/Figure-Rendering-Lineage.csv"""
import argparse, csv, hashlib, json, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parent)); import chart_theme as T
T.apply(); import matplotlib.pyplot as plt
PK = Path(__file__).resolve().parents[1]; D = PK / "data"; SUP = D / "supplement"; EMP = D / "empirical"; TAB = EMP / "tables"
OUT = PK / "figures"; LIN = []
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

def rec(png, vec, original, inputs, cols, func, ops, pop):
    LIN.append(dict(figure=str(Path(png).relative_to(PK)), original_exhibit=original, input_tables="; ".join(str(Path(i).relative_to(PK)) for i in inputs), input_sha256="; ".join(sha(i)[:16] for i in inputs), columns_used=cols,
                    render_function=func, display_only_operations=ops, units_and_population=pop, png_sha256=sha(png), vector_master=str(Path(vec).relative_to(PK)), vector_sha256=sha(vec)))
def labbar(ax, y, v, text, pad, color=T.INK, **kw): ax.text(v + pad, y, text, va="center", ha="left" if pad > 0 else "right", fontsize=7.2, color=color, **kw)

# ---------------------------------------------------------------- 01 MIIT
def f01():
    m = pd.read_csv(D / "miit_2024_observations.csv").set_index("metric_name"); poly, mod = m.loc["polysilicon_price_change", "value"], m.loc["module_price_change", "value"]
    fig, ax = T.newfig(2.45); y = [1, 0]; v = [mod, poly]; ax.barh(y, v, 0.55, color=T.NAVY); ax.set_yticks(y); ax.set_yticklabels(["PV modules", "Polysilicon"]); ax.axvline(0, color=T.INK, lw=0.8); ax.set_xlim(-46, 3); T.hgrid(ax, "x")
    for yy, vv in zip(y, v): ax.text(vv + 0.8, yy, T.fmt(vv, 1, pct=True), va="center", ha="left", color="white", fontsize=8, fontweight="bold")
    ax.set_xlabel("Reported year-over-year price change (%)")
    png, vec = T.finish(fig, OUT / "01_miit_prices.png", "China PV manufacturing-stage price direction, 2024", None, "Source: MIIT 2024 bulletin (original 2025-02-27; Fujian official republication 2025-04-18, retained 2026-10-07). Extracted from the retained republication; the MIIT-origin page remains inaccessible. Annual changes only; not U.S. delivered cost or a product price index.")
    rec(png, vec, "support/original-figures/01_miit_prices.png", [D / "miit_2024_observations.csv"], "metric_name, value (polysilicon_price_change, module_price_change)", "f01", "none", "Percent year-over-year, China, 2024; two reported observations")

# ---------------------------------------------------------------- 03 LONGi
def f03():
    a = pd.read_csv(D / "longi_product_margins.csv").set_index("segment"); order = ["Modules and cells", "Wafers and ingots"]; v = [a.loc[s, "gross_margin_percent"] for s in order]
    fig, ax = T.newfig(2.45); ax.barh([1, 0], v, 0.55, color=[T.NAVY if x >= 0 else T.BRICK for x in v]); ax.set_yticks([1, 0]); ax.set_yticklabels(order); ax.axvline(0, color=T.INK, lw=0.8); ax.set_xlim(-18, 10); T.hgrid(ax, "x")
    for yy, vv in zip([1, 0], v): ax.text(vv + (0.5 if vv >= 0 else -0.5), yy, T.fmt(vv, 2, pct=True), va="center", ha="left" if vv >= 0 else "right", fontsize=8, fontweight="bold")
    ax.set_xlabel("Reported segment gross margin (%)")
    png, vec = T.finish(fig, OUT / "03_longi_margins.png", "LONGi: different segment margin outcomes, FY2024", None, "Source: LONGi 2024 Annual Report, PDF p.30 (retained 2026-10-07; revenue/cost reconciliation). Same company, different business scopes; no peer ranking, price causality or U.S. project-cost inference.")
    rec(png, vec, "support/original-figures/03_longi_margins.png", [D / "longi_product_margins.csv"], "segment, gross_margin_percent", "f03", "none", "Percent of segment revenue, FY2024, RMB nominal as reported")

# ---------------------------------------------------------------- 04 IRENA
def f04():
    a = pd.read_csv(D / "irena_pv.csv"); fig, ax = T.newfig(3.1)
    for g, st in (("World", dict(color=T.NAVY, marker="o", ls="-")), ("China", dict(color=T.TEAL, marker="s", ls="--"))):
        b = a[a.geography == g].sort_values("year"); ax.plot(b.year, b.capacity_mw / 1000, ms=3.8, **st); ax.text(b.year.iloc[-1] + 0.15, b.capacity_mw.iloc[-1] / 1000, f"{g}\n{b.capacity_mw.iloc[-1] / 1000:,.0f} GW", color=st["color"], fontsize=7.4, va="center", fontweight="bold")
    ax.set_xlim(2015.6, 2026.5); ax.set_ylim(0, 2600); ax.set_xticks([2016, 2018, 2020, 2022, 2024, 2025]); ax.set_ylabel("Solar PV capacity (GW)")
    png, vec = T.finish(fig, OUT / "04_irena_capacity.png", "Global and Chinese solar PV deployment, 2016–2025", None, "Source: IRENA Renewable Capacity Statistics 2026, physical PDF pp.37–38 (printed pp.25–26), retrieved 2026-08-25. Maximum net generating capacity; China carries source flag u (unofficial upstream) and is included in World. Not manufacturing capacity.")
    rec(png, vec, "support/original-figures/04_irena_capacity.png", [D / "irena_pv.csv"], "geography, year, capacity_mw", "f04", "MW to GW", "Cumulative capacity stock, GW; World includes China")

# ---------------------------------------------------------------- 05 ERCOT hourly
def f05():
    a = pd.read_csv(D / "hourly_profile.csv"); fig, ax = T.newfig(3.7, nrows=2, sharex=True, gridspec_kw={"height_ratios": [1, 1]})
    ax[0].plot(a.hour_ending_local, a.mean_load_mw / 1000, color=T.NAVY); ax[0].set_ylim(0, 75); ax[0].set_ylabel("Load (GW)"); h = a.loc[a.mean_load_mw.idxmax()]; ax[0].plot([h.hour_ending_local], [h.mean_load_mw / 1000], "o", color=T.NAVY, ms=4); ax[0].annotate(f"Peak: hour ending {int(h.hour_ending_local)}", (h.hour_ending_local, h.mean_load_mw / 1000), xytext=(h.hour_ending_local - 5.2, 66), fontsize=7.2, arrowprops=dict(arrowstyle="-", color=T.SLATE, lw=0.6))
    ax[1].plot(a.hour_ending_local, a.mean_solar_mwh_per_hour / 1000, color=T.AMBER); ax[1].set_ylim(0, 24); ax[1].set_ylabel("Solar (GWh/h)"); s = a.loc[a.mean_solar_mwh_per_hour.idxmax()]; ax[1].plot([s.hour_ending_local], [s.mean_solar_mwh_per_hour / 1000], "o", color=T.AMBER, ms=4)
    ax[1].annotate(f"Peak: hour ending {int(s.hour_ending_local)}", (s.hour_ending_local, s.mean_solar_mwh_per_hour / 1000), xytext=(s.hour_ending_local + 3.2, 20.5), fontsize=7.2, arrowprops=dict(arrowstyle="-", color=T.SLATE, lw=0.6))
    ax[1].set_xlabel("Local hour ending"); ax[1].set_xticks([1, 4, 8, 12, 16, 20, 24]); ax[1].set_xlim(0.5, 24.5)
    png, vec = T.finish(fig, OUT / "05_ercot_hourly.png", "ERCOT system intraday shapes, 2025 non-DST dates", "Separate panels and scales: system load (top), system solar (bottom)", "Source: ERCOT Native Load and Solar/FINAL fuel mix, retrieved 2026-08-26; 363 dates, 8,712 matched hours. System-level timing only; no project energy, price, capture-price or causal join. Load in MW and solar in MWh per hour are shown in GW and GWh/hour.")
    rec(png, vec, "support/original-figures/05_ercot_hourly.png", [D / "hourly_profile.csv"], "hour_ending_local, mean_load_mw, mean_solar_mwh_per_hour", "f05", "MW to GW; MWh/hour to GWh/hour (original figure used MW and MWh/hour)", "363 non-DST 2025 dates, ERCOT system; separate scales")

# ---------------------------------------------------------------- 06 ERCOT seasonal
def f06():
    a = pd.read_csv(D / "seasonal.csv"); mo = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]; fig, ax = T.newfig(3.7, nrows=2, sharex=True)
    ax[0].plot(a.month, a.weighted_mean_load_mw / 1000, color=T.NAVY, marker="o", ms=3.8); ax[0].set_ylim(0, 75); ax[0].set_ylabel("Load (GW)")
    ax[1].bar(a.month, a.solar_mwh_total / 1e6, 0.68, color=T.AMBER); ax[1].set_ylabel("Solar output (TWh)"); ax[1].set_xticks(a.month); ax[1].set_xticklabels(mo); T.hgrid(ax[1], "y")
    for r in a.itertuples(): ax[1].text(r.month, r.solar_mwh_total / 1e6 + 0.12, f"{r.solar_mwh_total / 1e6:.1f}", ha="center", fontsize=6.4, color=T.MUTED)
    png, vec = T.finish(fig, OUT / "06_ercot_seasonal.png", "ERCOT seasonal system demand and solar output, 2025", "Separate panels: monthly mean load (top), monthly solar total (bottom)", "Source: ERCOT 2025 Native Load and Solar/FINAL fuel mix, retrieved 2026-08-26; all 365 source-aligned dates. Load weighted by source hours; solar summed. DST days retained at daily grain. No asset or AI attribution.")
    rec(png, vec, "support/original-figures/06_ercot_seasonal.png", [D / "seasonal.csv"], "month, weighted_mean_load_mw, solar_mwh_total", "f06", "MW to GW; MWh to TWh", "ERCOT system, 2025, 12 months, source-hour weighted load; solar summed")

# ---------------------------------------------------------------- 08 LBNL
def f08():
    a = pd.read_csv(D / "lbnl_2030_scenarios.csv"); fig, ax = T.newfig(3.1); n = len(a); y = np.arange(n)[::-1]
    cols = [T.NAVY if s == "Reference Case" else (T.SLATE if "Compounded" in s else T.AMBER) for s in a.scenario]; ax.barh(y, a.electricity_twh, 0.62, color=cols); ax.set_yticks(y); ax.set_yticklabels([s.replace("Compounded Uncertainty—", "Compounded: ") for s in a.scenario]); T.hgrid(ax, "x")
    ref = float(a.loc[a.scenario == "Reference Case", "electricity_twh"].iloc[0]); ax.axvline(ref, color=T.INK, lw=0.8, ls=":"); ax.text(ref + 6, n - 0.35, f"Reference {ref:.0f}", fontsize=7, color=T.MUTED, va="bottom")
    for yy, v in zip(y, a.electricity_twh): ax.text(v + 8, yy, f"{v:.0f}", va="center", fontsize=7.6)
    ax.set_xlim(0, 940); ax.set_xlabel("Modeled electricity demand, 2030 (TWh)")
    png, vec = T.finish(fig, OUT / "08_lbnl_scenarios.png", "U.S. data-center demand scenarios, 2030", "Navy: reference case; amber: single-assumption cases; slate: compounded-uncertainty cases", "Source: Berkeley Lab 2025 Update (June 2026), Table 2, physical p.11 / printed p.9 (DOE original retained 2026-10-07). National modeled scenarios, not confidence bounds, AI-only demand, ERCOT allocation or solar offtake.")
    rec(png, vec, "support/original-figures/08_lbnl_scenarios.png", [D / "lbnl_2030_scenarios.csv"], "scenario, electricity_twh", "f08", "none", "TWh, U.S. all data centers, 2030, seven modeled scenarios")

# ---------------------------------------------------------------- S01
def s01():
    a = pd.read_csv(SUP / "D/D_irena_pv_top12_net_change_2025.csv").sort_values("net_change_mw"); fig, ax = T.newfig(3.7); y = np.arange(len(a)); ax.barh(y, a.net_change_mw / 1000, 0.66, color=[T.NAVY if n == "China" else T.NAVY_L for n in a.name]); ax.set_yticks(y); ax.set_yticklabels(a.name); T.hgrid(ax, "x")
    for yy, v in zip(y, a.net_change_mw / 1000): ax.text(v + 3, yy, f"{v:.1f}", va="center", fontsize=7)
    ax.set_xlim(0, 360); ax.set_xlabel("Net PV capacity change in 2025 (GW)"); share = a.set_index("name").loc["China", "share_of_world_net_change_2025"] * 100
    png, vec = T.finish(fig, OUT / "S01_country_net_change.png", f"China accounted for {share:.1f}% of global net PV growth", "Twelve largest net capacity increases, 2025 minus 2024", "Source: retained IRENA country series (R-D). Net stock change, not shipments, gross installations or procurement; small differences reflect source rounding.")
    rec(png, vec, "support/original-figures/S01_country_net_change.png", [SUP / "D/D_irena_pv_top12_net_change_2025.csv"], "name, net_change_mw, share_of_world_net_change_2025", "s01", "sorted ascending; MW to GW", "GW, net change 2025 vs 2024, 12 countries")

# ---------------------------------------------------------------- S02
def s02():
    a = pd.read_csv(SUP / "D/D_company_xbrl_wide.csv"); a = a[a.fiscal_period.isin(["FY2024", "FY2025"])].pivot(index="company", columns="fiscal_period", values="gross_margin"); names = [n.replace(" Holding", "").replace(" New Energy", "") for n in a.index]
    fig, ax = T.newfig(3.1); x = np.arange(len(a)); b1 = ax.bar(x - .19, a.FY2024 * 100, .36, label="FY2024", color=T.NAVY_L); b2 = ax.bar(x + .19, a.FY2025 * 100, .36, label="FY2025", color=T.NAVY); ax.axhline(0, color=T.INK, lw=0.8)
    for xs, col in ((x - .19, a.FY2024), (x + .19, a.FY2025)):
        for xx, v in zip(xs, col * 100): ax.text(xx, v + (1.2 if v >= 0 else -1.2), T.fmt(v, 1), ha="center", va="bottom" if v >= 0 else "top", fontsize=7)
    ax.set_xticks(x); ax.set_xticklabels(names); ax.set_ylabel("Consolidated gross margin (%)"); ax.set_ylim(-28, 52); ax.legend(loc="upper right", ncol=2); T.hgrid(ax, "y")
    png, vec = T.finish(fig, OUT / "S02_company_margins.png", "Company outcomes differ across technologies and business models", "Consolidated reported gross margin, FY2024 and FY2025 (companies in alphabetical order)", "Source: retained SEC filings and extracted annual XBRL contexts. Percent of revenue. Within-company changes; not a ranking of operating efficiency or product-matched margins.")
    rec(png, vec, "support/original-figures/S02_company_margins.png", [SUP / "D/D_company_xbrl_wide.csv"], "company, fiscal_period, gross_margin", "s02", "fraction to percent; FY2024/FY2025 rows only", "Percent, consolidated, four companies, FY2024–FY2025; currencies not combined")

# ---------------------------------------------------------------- S03
def s03():
    a = pd.read_csv(SUP / "A/A_cost_components_pvscm_2025Q1_pv_only.csv"); a = a[(a.price_basis == "MMP") & (a.category != "TOTAL")]; fact = json.loads((SUP / "A/A_summary_facts.json").read_text()); fig, ax = T.newfig(3.1); y = np.arange(len(a))[::-1]
    ax.barh(y, a.usd_per_wdc, 0.62, color=[T.TEAL if c == "Module" else T.NAVY for c in a.category]); ax.set_yticks(y); ax.set_yticklabels(a.category); T.hgrid(ax, "x")
    for yy, v in zip(y, a.usd_per_wdc): ax.text(v + 0.005, yy, f"${v:.3f}", va="center", fontsize=7.4)
    ax.set_xlim(0, 0.35); ax.set_xlabel("2024 USD per Wdc (market-price basis)")
    png, vec = T.finish(fig, OUT / "S03_cost_components.png", f"Modules represent {fact['module_share_mmp'] * 100:.1f}% of modeled PV-only market-price cost", "Component costs, DOE/NLR PVSCM 2025Q1 reimplementation (PV-only; storage excluded); module highlighted", "Source: reimplementation of DOE/NLR PVSCM 2025Q1 inputs; 2024 dollars per Wdc, DC denominator throughout. Shares derived from the unrounded total. National model, not a project quotation.")
    rec(png, vec, "support/original-figures/S03_cost_components.png", [SUP / "A/A_cost_components_pvscm_2025Q1_pv_only.csv", SUP / "A/A_summary_facts.json"], "category, price_basis, usd_per_wdc; module_share_mmp", "s03", "rows with price_basis == MMP and category != TOTAL", "2024 USD per Wdc, national model")

# ---------------------------------------------------------------- S04
def s04():
    a = pd.read_csv(SUP / "A/Integrated_passthrough_chart.csv"); fact = json.loads((SUP / "A/A_summary_facts.json").read_text()); x0 = -29.7; y0 = x0 * fact["module_share_mmp"] * fact["pass_through_k"]; fig, ax = T.newfig(3.1)
    ax.plot(a.module_input_change_pct, a.total_cost_change_pct, color=T.NAVY, lw=1.9); ax.plot([x0], [y0], "o", color=T.AMBER, ms=6, zorder=5); ax.axhline(0, color=T.AXIS, lw=0.8); ax.axvline(0, color=T.AXIS, lw=0.8)
    ax.annotate(f"Illustration: {T.fmt(x0, 1, pct=True)} module input\n→ {T.fmt(y0, 1, pct=True)} modeled total cost", (x0, y0), xytext=(-48, 3.6), fontsize=7.4, arrowprops=dict(arrowstyle="-", color=T.SLATE, lw=0.7))
    ax.set_xlabel("Assumed module-input change (%)"); ax.set_ylabel("Modeled total PV-only cost change (%)"); ax.set_xlim(-52, 32); ax.set_ylim(-17, 10)
    png, vec = T.finish(fig, OUT / "S04_passthrough.png", "Component pass-through is conditional on unchanged other inputs", "Hypothetical comparative statics: module share × modeled marginal factor", "Source: baseline module share × modeled marginal factor, all other inputs fixed. Hypothetical comparative static; neither a historical regression nor a forecast, and not observed U.S. delivered-cost transmission.")
    rec(png, vec, "support/original-figures/S04_passthrough.png", [SUP / "A/Integrated_passthrough_chart.csv", SUP / "A/A_summary_facts.json"], "module_input_change_pct, total_cost_change_pct; module_share_mmp, pass_through_k (marked point)", "s04", "none (marker value recomputed from the same two retained parameters)", "Percent change, PV-only modeled cost")

# ---------------------------------------------------------------- S05
def s05():
    a = pd.read_csv(SUP / "C/C_ercot_large_load_queue_status_by_year_2026-03.csv"); a = a[(a.expected_in_service_year == 2030) & (a.status != "TOTAL printed")]; labels = ["No studies submitted", "Under ERCOT review", "Planning studies approved", "Approved, not operational", "Observed energized (noncoincident)"]
    fig, ax = T.newfig(2.9); y = np.arange(len(a))[::-1]; ax.barh(y, a.mw.to_numpy() / 1000, 0.62, color=T.SEQ_NAVY); ax.set_yticks(y); ax.set_yticklabels(labels); T.hgrid(ax, "x")
    for yy, v in zip(y, a.mw.to_numpy() / 1000): ax.text(v + 2, yy, f"{v:,.1f}", va="center", fontsize=7.4)
    ax.set_xlim(0, 150); ax.set_xlabel("GW in the source process-status table (2030 column)")
    png, vec = T.finish(fig, OUT / "S05_load_status.png", "Requested and operating large-load quantities have different meanings", "ERCOT large-load process categories, March 2026 snapshot", "Source: ERCOT March 2026 large-load status table, 2030 column. Process snapshot, not a probability-weighted load forecast; observed energized is a noncoincident historical measure. Batch Zero quantities are not added.")
    rec(png, vec, "support/original-figures/S05_load_status.png", [SUP / "C/C_ercot_large_load_queue_status_by_year_2026-03.csv"], "status, expected_in_service_year == 2030, mw", "s05", "MW to GW; rows excluding 'TOTAL printed'", "GW requested by process status, ERCOT, 2030 column")

# ---------------------------------------------------------------- S06
def s06():
    a = pd.read_csv(SUP / "C/C_batch_zero_wlpun_byog_2026-09.csv"); a = a[a.component.isin(["Gas", "Solar", "Wind", "Battery"])]; tot = a.mw.sum(); fig, ax = T.newfig(2.3); y = np.arange(len(a))[::-1]
    ax.barh(y, a.mw.to_numpy() / 1000, 0.6, color=[T.NAVY if c == "Gas" else T.NAVY_L for c in a.component]); ax.set_yticks(y); ax.set_yticklabels(a.component); T.hgrid(ax, "x")
    for yy, v, c in zip(y, a.mw.to_numpy() / 1000, a.component): ax.text(v + 0.2, yy, f"{v:.2f} GW ({v * 1000 / tot * 100:.1f}% of listed power capacity)", va="center", fontsize=7.2)
    ax.set_xlim(0, 20); ax.set_xlabel("Reported resource power capacity (GW)")
    png, vec = T.finish(fig, OUT / "S06_wlpun_capacity.png", "Gas dominates the reported mix associated with 11 WLPUN projects", "Resource power capacity by type; shares of the four listed categories", "Source: ERCOT September 2026 Batch Zero deck. Power ratings, not generated-energy shares; battery capacity is a power rating. Does not describe all data centers or establish procurement mix.")
    rec(png, vec, "support/original-figures/S06_wlpun_capacity.png", [SUP / "C/C_batch_zero_wlpun_byog_2026-09.csv"], "component, mw (Gas, Solar, Wind, Battery)", "s06", "MW to GW; shares computed over the four listed categories for labels", "GW, 11 WLPUN projects, September 2026 deck")

# ---------------------------------------------------------------- S07
def s07():
    a = pd.read_csv(SUP / "B/B_all_resource_nodes_screen_2025.csv"); a = a[a.screen == "eligible"]; ref = 22.131927; fig, ax = T.newfig(3.1)
    ax.hist(a.gw_price_ref, bins=40, color=T.NAVY_L, edgecolor="white", linewidth=0.5); ax.axvline(ref, color=T.AMBER, lw=1.8); ax.annotate(f"Reference node TAYGETE2_ALL: ${ref:.2f}/MWh", (ref, 90), xytext=(33, 105), color=T.AMBER, fontsize=7.6, fontweight="bold", va="center", arrowprops=dict(arrowstyle="-", color=T.AMBER, lw=0.8))
    ax.set_xlabel("Generation-weighted price (USD/MWh), potential generation before shutdown response"); ax.set_ylabel("Resource nodes"); T.hgrid(ax, "y")
    png, vec = T.finish(fig, OUT / "S07_node_prices.png", "Reference absolute capture price is near the 37th percentile", f"2025 cross-section: {len(a)} eligible resource nodes under one common hypothetical output curve", "Source: first-round retained 641-node screen (2025 only), potential-generation weighting before the modeled export response. Historical cross-section; separate from the 485-node three-year common panel.")
    rec(png, vec, "support/original-figures/S07_node_prices.png", [SUP / "B/B_all_resource_nodes_screen_2025.csv"], "screen == 'eligible', gw_price_ref", "s07", "histogram, 40 bins (as original); reference value 22.131927 as in original code", "USD/MWh, 641 nodes, 2025, common hypothetical output")

# ---------------------------------------------------------------- S1 / S2
def _ivl():
    ivl = pd.read_csv(D / "interval_energy_price_2025.csv", parse_dates=["interval_start_utc"]); loc = ivl.interval_start_utc.dt.tz_convert("Etc/GMT+6"); ivl["hour_cst"] = loc.dt.hour; return ivl
def s1():
    ivl = _ivl(); pr = ivl[ivl.price_available]; g = ivl.groupby("hour_cst").energy_mwh_base.mean() * 4; p = pr.groupby("hour_cst").price_usd_mwh.mean(); neg = pr.assign(neg=pr.price_usd_mwh < 0).groupby("hour_cst").neg.mean() * 100
    fig, ax = T.newfig(3.2, ncols=2); ax[0].bar(g.index, g.values, 0.78, color=T.NAVY); ax[0].set_title("Mean simulated AC output"); ax[0].set_xlabel("Hour beginning, CST (UTC−6)"); ax[0].set_ylabel("MW"); T.hgrid(ax[0], "y")
    ax2 = ax[1].twinx(); ax2.bar(neg.index, neg.values, 0.78, color=T.BRICK_L, label="% intervals below $0 (right)"); ax2.set_ylabel("% of priced intervals below $0", color=T.MUTED); ax2.spines["top"].set_visible(False); ax2.grid(False); ax2.set_ylim(0, 40)
    ax[1].set_zorder(ax2.get_zorder() + 1); ax[1].patch.set_visible(False); ax[1].plot(p.index, p.values, color=T.AMBER, marker="o", ms=3.2, label="Mean node price (left)"); ax[1].axhline(0, color=T.AXIS, lw=0.7); ax[1].set_ylabel("USD/MWh"); ax[1].set_xlabel("Hour beginning, CST (UTC−6)"); ax[1].set_title("2025 node price: mean and negative share", fontsize=8)
    h1, l1 = ax[1].get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax[1].set_ylim(-5, 118); ax[1].legend(h1 + h2, l1 + l2, loc="upper left", fontsize=6.6)
    png, vec = T.finish(fig, OUT / "S1_intraday_output_and_price.png", "Simulated solar output peaks in the hours with the lowest and most often negative 2025 node prices", None, "Hypothetical 100 MWac/132 MWdc single-axis case at an NSRDB cell in Pecos County, TX; PVWatts v8 (PySAM 7.1.1), NSRDB GOES CONUS v4 2025 5-minute weather. Node price: ERCOT NP6-905-CD real-time SPP, TAYGETE2_ALL, 2025 (price reference only; plant not settled there; finality not verified). 15-minute intervals; 35,038 priced 2025 intervals; two missing night intervals excluded.")
    rec(png, vec, "support/original-figures/S1_intraday_output_and_price.png", [D / "interval_energy_price_2025.csv"], "interval_start_utc, energy_mwh_base, price_usd_mwh, price_available", "s1", "hourly means in UTC−6 (as original); output ×4 MW; negative share by hour", "MW; USD/MWh; percent of priced 15-minute intervals; 2025; hypothetical system, reference node")
def s2():
    mo = pd.read_csv(D / "monthly_energy_price_summary.csv"); fig, ax = T.newfig(3.2, ncols=2); ax[0].bar(mo.month, mo.energy_gwh, 0.7, color=T.NAVY); ax[0].set_xticks(range(1, 13)); ax[0].set_title("Simulated AC energy by month"); ax[0].set_xlabel("Month, 2025"); ax[0].set_ylabel("GWh"); T.hgrid(ax[0], "y")
    ax[1].plot(mo.month, mo.tw, color=T.SLATE, marker="s", ms=3.2, ls="--", label="Time-weighted price"); ax[1].plot(mo.month, mo.gw, color=T.AMBER, marker="o", ms=3.2, label="Generation-weighted, as available"); ax[1].plot(mo.month, mo.gw_curt, color=T.TEAL, marker="^", ms=3.2, ls=":", label="Generation-weighted, shutdown if below $0")
    ax[1].axhline(0, color=T.AXIS, lw=0.7); ax[1].set_xticks(range(1, 13)); ax[1].set_title("Monthly node price measures"); ax[1].set_xlabel("Month, 2025"); ax[1].set_ylabel("USD/MWh"); ax[1].set_ylim(-3, 82); ax[1].legend(fontsize=6.4, loc="upper right", ncol=1); nb = int((mo.gw < mo.tw).sum())
    png, vec = T.finish(fig, OUT / "S2_monthly_energy_and_capture.png", f"The generation-weighted node price is below the time-weighted average in {nb} of 12 months", None, "Hypothetical 100 MWac/132 MWdc single-axis case, Pecos County NSRDB cell; PVWatts v8; ERCOT NP6-905-CD real-time SPP, TAYGETE2_ALL, 2025 (price reference only; plant not settled there; finality not verified). energy_gwh is potential simulated energy; gw_curt is the delivered-energy-weighted price after the assumed negative-price shutdown.")
    rec(png, vec, "support/original-figures/S2_monthly_energy_and_capture.png", [D / "monthly_energy_price_summary.csv"], "month, energy_gwh, tw, gw, gw_curt", "s2", "none", "GWh and USD/MWh by month, 2025; hypothetical system, reference node")

# ---------------------------------------------------------------- S3
def s3():
    m = pd.read_csv(D / "scenario_metrics.csv"); order = ["node_downside", "node_base", "node_upside", "fixed_downside", "fixed_base", "fixed_upside"]; m = m.set_index("scenario_id").loc[order]; fig, ax = T.newfig(3.5, ncols=2, gridspec_kw={"width_ratios": [1, 1.25]}); y = np.arange(6)[::-1]; v = m.npv_real_selected / 1e6
    ax[0].barh(y, v, 0.6, color=[T.BRICK if x < 0 else T.TEAL for x in v]); ax[0].set_yticks(y); ax[0].set_yticklabels(order); ax[0].axvline(0, color=T.INK, lw=0.8); ax[0].set_xlim(-150, 25); ax[0].set_title("NPV at 4.27% real ($ million)", fontsize=8); T.hgrid(ax[0], "x")
    for yy, x in zip(y, v): ax[0].text(x - 3, yy, T.fmt(x, 0), va="center", ha="right", fontsize=7.4, color=T.INK)
    lc = m.lcoe_real_selected.to_numpy(); pz = m.realized_price_real_yr1.to_numpy(); ax[1].scatter(lc, y, marker="|", s=170, color=T.BRICK, zorder=3, label="LCOE at 4.27% (real 2025 $/MWh)"); ax[1].scatter(pz, y, color=T.NAVY, s=26, zorder=3, label="Year-1 realized price (real 2025 $/MWh)")
    for i, (sid, r) in enumerate(m.iterrows()):
        st = str(r.irr_status); tag = f"IRR {r.irr_real * 100:.1f}%".replace("-", "−") if st == "unique" else ("IRR: multiple roots" if st.startswith("multiple") else "IRR: no certified single root"); ax[1].text(max(lc[i], pz[i]) + 3.2, y[i], tag, fontsize=6.6, va="center")
    ax[1].set_yticks(y); ax[1].set_yticklabels([]); ax[1].set_xlim(15, 95); ax[1].set_xlabel("USD/MWh, real 2025"); ax[1].set_title("Year-1 realized price vs LCOE; IRR status", fontsize=8); T.hgrid(ax[1], "x"); ax[1].set_ylim(-1.8, 5.6); ax[0].set_ylim(-1.8, 5.6); ax[1].legend(loc="lower center", bbox_to_anchor=(0.5, -0.02), ncol=2, fontsize=6.3, columnspacing=1.0, handletextpad=0.2)
    nneg = int((m.npv_real_selected < 0).sum()); nuni = int((m.irr_status == "unique").sum())
    png, vec = T.finish(fig, OUT / "S3_scenario_outcomes.png", f"{nneg} of 6 scenario groups have negative NPV at 4.27% real; IRR has a unique root in {nuni} of 6", None, "Scenario groups are not probabilities. Downside/upside move CAPEX/FOM (ATB Conservative/Advanced), losses, degradation, price path or fixed price together. Hypothetical 100 MWac/132 MWdc case, Pecos County NSRDB cell; PVWatts v8; node price ERCOT NP6-905-CD TAYGETE2_ALL 2025 (price reference only). Pre-tax, unlevered.", top_pad=0.0)
    rec(png, vec, "support/original-figures/S3_scenario_outcomes.png", [D / "scenario_metrics.csv"], "scenario_id, npv_real_selected, lcoe_real_selected, realized_price_real_yr1, irr_status, irr_real", "s3", "fixed row order; NPV to $ million", "Real 2025 USD; six scenario groups; pre-tax unlevered")

# ---------------------------------------------------------------- S4
def s4():
    cf = pd.read_csv(D / "scenario_annual_cash_flows.csv"); fig, ax = T.newfig(3.4, ncols=2, sharey=True)
    for k, sid in enumerate(["node_base", "fixed_base"]):
        x = cf[cf.scenario_id == sid]; yrs = x.year; ax[k].bar(yrs, x.revenue_real / 1e6, 0.78, color=T.NAVY, label="Revenue"); neg = x.fom_real + x.major_replacement_real + x.decommissioning_real; ax[k].bar(yrs, neg / 1e6, 0.78, color=T.AMBER, label="FOM, replacement, decommissioning"); ax[k].bar(yrs, x.capex_real / 1e6, 0.78, color=T.BRICK, label="Capex (2026)")
        a2 = ax[k].twinx(); a2.plot(yrs, x.cumulative_real / 1e6, color=T.INK, lw=1.2); a2.axhline(0, color=T.AXIS, lw=0.5); a2.set_ylim(-160, 160); a2.spines["top"].set_visible(False); a2.grid(False); a2.text(2043, -128, "cumulative net (right axis)", fontsize=6.6, ha="left")
        if k == 1: a2.set_ylabel("Cumulative net, $ million")
        else: a2.set_yticklabels([])
        ax[k].set_title(f"{sid}: annual real cash flow", fontsize=8); ax[k].set_ylim(-20, 20); T.hgrid(ax[k], "y")
    ax[0].set_ylabel("$ million per year (clipped at ±20)"); ax[0].text(2026.6, -19.4, "capex −144 (off scale)", fontsize=6.8, color=T.BRICK, va="bottom", ha="left", bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9)); ax[1].text(2026.6, -19.4, "capex −144 (off scale)", fontsize=6.8, color=T.BRICK, va="bottom", ha="left", bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9)); ax[0].legend(fontsize=6.4, loc="upper right")
    png, vec = T.finish(fig, OUT / "S4_annual_cash_flows.png", "Base-case revenue covers annual fixed costs, but cumulative cash never recovers the 2026 capital outlay", None, "Pre-tax, unlevered, real 2025 USD; no taxes, credits, debt or market fees. Bars clipped at ±$20 million; the capex bar extends off scale. Hypothetical 100 MWac/132 MWdc case, Pecos County NSRDB cell; PVWatts v8; node price ERCOT NP6-905-CD TAYGETE2_ALL 2025 (price reference only).")
    rec(png, vec, "support/original-figures/S4_annual_cash_flows.png", [D / "scenario_annual_cash_flows.csv"], "scenario_id, year, revenue_real, fom_real, major_replacement_real, decommissioning_real, capex_real, cumulative_real", "s4", "$ million scaling; clipping at ±20 as original (disclosed on chart)", "Real 2025 USD; node_base and fixed_base; 2026–2056")

# ---------------------------------------------------------------- S5
def s5():
    s = pd.read_csv(D / "sensitivity_one_way.csv"); fig, ax = T.newfig(6.3, nrows=2, gridspec_kw={"height_ratios": [1, 0.93]})
    for k, route in enumerate(["node", "fixed"]):
        x = s[s.route == route]; rng = x.groupby("sensitivity").delta_npv_vs_base.agg(lambda v: v.abs().max()).sort_values()
        for i, lab in enumerate(rng.index):
            for _, r in x[x.sensitivity == lab].iterrows(): ax[k].barh(i, r.delta_npv_vs_base / 1e6, 0.66, color=T.TEAL if r.side == "low" else T.AMBER)
        ax[k].set_yticks(range(len(rng))); ax[k].set_yticklabels(rng.index, fontsize=6.8); ax[k].axvline(0, color=T.INK, lw=0.8); ax[k].set_title(f"{route}_base", fontsize=8.4); ax[k].set_xlabel("NPV change at 4.27% ($ million)"); T.hgrid(ax[k], "x"); ax[k].set_xlim(-34, 34)
    top = s[s.route == "node"].groupby("sensitivity").delta_npv_vs_base.agg(lambda v: v.abs().max()).sort_values(ascending=False).index[:3]
    from matplotlib.patches import Patch
    ax[0].legend(handles=[Patch(color=T.TEAL, label="Low end of listed range"), Patch(color=T.AMBER, label="High end of listed range")], loc="lower right", fontsize=6.6)
    png, vec = T.finish(fig, OUT / "S5_one_way_sensitivity.png", "Within the tested ranges, the largest node-case NPV swings come from: " + "; ".join(t.split(":")[0] for t in top), None, "Teal = low value of the listed range, amber = high value. Ranking holds only for these specified perturbations; it is not a general ranking of return drivers or causal evidence. Hypothetical 100 MWac/132 MWdc case, Pecos County NSRDB cell; PVWatts v8; node price ERCOT NP6-905-CD TAYGETE2_ALL 2025 (price reference only).")
    rec(png, vec, "support/original-figures/S5_one_way_sensitivity.png", [D / "sensitivity_one_way.csv"], "route, sensitivity, side, delta_npv_vs_base", "s5", "sorted by maximum absolute NPV change; $ million scaling; panels stacked vertically (original: side by side) with a common x range of ±34", "NPV change, $ million, 4.27% real; 49 sensitivity rows")

# ---------------------------------------------------------------- S6
def s6():
    t = pd.read_csv(D / "sensitivity_two_way.csv"); be = json.load(open(D / "breakevens.json")); fig, ax = T.newfig(6.0, nrows=2)
    for k, (route, key, lab) in enumerate([("fixed", "fixed_price", "Fixed price, nominal flat ($/MWh)"), ("node", "node_scale", "Node price multiplier on 2025 profile")]):
        x = t[t.route == route].pivot(index="capex_usd_per_kwac", columns=key, values="npv_real_selected") / 1e6; im = ax[k].imshow(x.values, origin="lower", aspect="auto", cmap=T.DIVERGING, vmin=-120, vmax=120)
        ax[k].set_xticks(range(len(x.columns))); ax[k].set_xticklabels([f"{c:g}" for c in x.columns], fontsize=7); ax[k].set_yticks(range(len(x.index))); ax[k].set_yticklabels([f"{v:,.0f}" for v in x.index], fontsize=7); ax[k].grid(False)
        ax[k].contour(x.values, levels=[0], colors=T.INK, linewidths=1.1)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]): ax[k].text(j, i, T.fmt(x.values[i, j], 0), ha="center", va="center", fontsize=6.6, color=T.INK)
        ax[k].set_xlabel(lab); ax[k].set_ylabel("CAPEX, OCC+GCC ($/kWac, 2025 USD)"); ax[k].set_title(f"{route}: NPV at 4.27% ($ million); black line = 0", fontsize=8)
    cax = fig.add_axes([0.915, 0.28, 0.014, 0.5]); fig.colorbar(im, cax=cax, label="NPV, $ million")
    png, vec = T.finish(fig, OUT / "S6_two_way_breakeven.png", f"Break-even: about ${be['fixed_breakeven_price_nominal_flat_at_0.0427']:.0f}/MWh flat nominal at base CAPEX; node case needs CAPEX near ${be['node_breakeven_capex_usd_per_kwac_at_0.0427']:,.0f}/kWac", None, "Each cell re-runs the full base cash flow. CAPEX rows are 70%–130% of ATB 2026 Moderate OCC+GCC converted with CPI-U. Hypothetical 100 MWac/132 MWdc case, Pecos County NSRDB cell; PVWatts v8; node price ERCOT NP6-905-CD TAYGETE2_ALL 2025 (price reference only).", manual=dict(left=0.1, right=0.865, hspace=0.55, bottom_in=0.62))
    rec(png, vec, "support/original-figures/S6_two_way_breakeven.png", [D / "sensitivity_two_way.csv", D / "breakevens.json"], "route, capex_usd_per_kwac, fixed_price / node_scale, npv_real_selected; breakevens", "s6", "pivot to grid; $ million scaling; zero contour of the retained grid; panels stacked vertically (original: side by side)", "NPV $ million, 4.27% real, per grid cell")

# ======================================================== empirical exhibits
def F1():
    flow = pd.read_csv(TAB / "Sample-Flow-By-Year.csv"); mk = pd.read_csv(TAB / "Market-Wide-Missing-Intervals.csv"); aud = pd.read_csv(TAB / "Node-Year-Sample-Table.csv")
    steps = ["all settlement points in NP6-905-CD", "type RN", "type RN and in official list", "  ... of which strictly complete (0 missing)"]; lab = ["All published\npoints", "Type RN", "Type RN,\nin official\nlist", "...complete on\nmarket-wide\ngrid"]; fig, ax = T.newfig(3.2, ncols=2, gridspec_kw={"width_ratios": [1.35, 1]}); w = 0.26
    for i, y in enumerate(T.YEAR):
        v = [int(flow[(flow.year == y) & (flow.step == s)].n.iloc[0]) for s in steps]; xs = np.arange(4) + (i - 1) * w; ax[0].bar(xs, v, w * 0.94, color=T.YEAR[y]["color"], label=str(y))
        for x, vv in zip(xs, v): ax[0].text(x, vv + 12, str(vv), ha="center", fontsize=6.2)
    ax[0].set_xticks(range(4)); ax[0].set_xticklabels(lab, fontsize=6.8); ax[0].set_ylabel("Settlement points"); ax[0].legend(ncol=3, loc="upper right"); ax[0].set_title("Node sample flow by price year", fontsize=8); ax[0].set_ylim(0, 1450); T.hgrid(ax[0], "y")
    c = aud[(aud.year == 2025) & ~aud.is_hub_lz_dc_name]; ax[1].hist(c.coverage * 100, bins=np.linspace(0, 100, 51), color=T.SLATE); ax[1].set_yscale("log"); import matplotlib.ticker as mt; ax[1].yaxis.set_major_formatter(mt.FuncFormatter(lambda v, _: f"{v:g}")); ax[1].yaxis.set_minor_formatter(mt.NullFormatter()); ax[1].set_xlabel("2025 intervals priced (%)"); ax[1].set_ylabel("Settlement points (log scale)"); ax[1].set_title("2025 coverage by point", fontsize=8); T.hgrid(ax[1], "y")
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F1_sample_flow_and_coverage.png", "Sample reconciliation and coverage", "641 = type RN, in official list, complete in 2025 only; 485 = complete in all three years", "Source: empirical candidate sample tables. Market-wide gap intervals (no price for any point), dropped from every series alike: " + "; ".join(f"{y}: {int((mk.year == y).sum())}" for y in T.YEAR) + ". Identity: published type RN and membership of the 2026-09-10 official list (a current snapshot).")
    rec(png, vec, "support/original-figures/empirical/F1_sample_flow_and_coverage.png", [TAB / "Sample-Flow-By-Year.csv", TAB / "Market-Wide-Missing-Intervals.csv", TAB / "Node-Year-Sample-Table.csv"], "year, step, n; year, year==2025 & ~is_hub_lz_dc_name, coverage", "F1", "none (histogram of retained coverage column, 50 bins)", "Settlement points per year; 2025 coverage share")

def _diverging_matrix(ax, M, vmin, vmax, title, fmtf, cmap=None):
    im = ax.imshow(M.values, cmap=cmap or T.DIVERGING, vmin=vmin, vmax=vmax); ax.set_xticks(range(3)); ax.set_xticklabels(M.columns); ax.set_yticks(range(3)); ax.set_yticklabels(M.index); ax.set_xlabel("Price year"); ax.set_ylabel("Weather year"); ax.set_title(title, fontsize=7.8); ax.grid(False)
    for i in range(3):
        for j in range(3): ax.text(j, i, fmtf(M.values[i, j]), ha="center", va="center", fontsize=8.2, fontweight="bold" if i == j else "normal", color=T.INK)
    return im
def F2():
    sm = pd.read_csv(EMP / "A_3x3_summary.csv"); cells = pd.read_csv(EMP / "A_3x3_cells_by_node.csv"); g = sm[sm.grp == "strict resource nodes (median)"]; r = cells[cells.node == "TAYGETE2_ALL"]
    fig, ax = T.newfig(3.0, ncols=4, gridspec_kw={"width_ratios": [1, 1, 0.06, 1], "wspace": 0.55})
    m1 = g.pivot(index="weather_year", columns="price_year", values="npv_4p27_median"); im = _diverging_matrix(ax[0], m1 / 1e6, -120, 120, f"Median NPV, {int(g.n.iloc[0])} nodes", lambda v: T.fmt(v, 0))
    m2 = r.pivot(index="weather_year", columns="price_year", values="npv_4p27"); _diverging_matrix(ax[1], m2 / 1e6, -120, 120, "NPV, reference node", lambda v: T.fmt(v, 0)); ax[1].set_ylabel(""); fig.colorbar(im, cax=ax[2]); ax[2].set_title("$ million", fontsize=6.8)
    m3 = g.pivot(index="weather_year", columns="price_year", values="npv_positive_share"); cm = plt.get_cmap("Blues"); ax[3].imshow(m3.values, cmap=cm, vmin=0, vmax=1.35); ax[3].set_xticks(range(3)); ax[3].set_xticklabels(m3.columns); ax[3].set_yticks(range(3)); ax[3].set_yticklabels(m3.index); ax[3].set_xlabel("Price year"); ax[3].set_title("Nodes with NPV > 0", fontsize=7.8); ax[3].grid(False)
    for i in range(3):
        for j in range(3): ax[3].text(j, i, ("100%" if m3.values[i, j] >= 0.9995 else f"{m3.values[i, j] * 100:.1f}%"), ha="center", va="center", fontsize=7, fontweight="bold" if i == j else "normal", color="white" if m3.values[i, j] > 0.6 else T.INK)
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F2_weather_by_price_matrix.png", "Weather-year and price-year scenario matrix", "Common 365-day calendar (29 February excluded); bold diagonal = same-year pairing, off-diagonal = counterfactual pairing", "Source: empirical candidate 3×3 tables. NPV at 4.27% real with a 30-year repetition of first-year price conditions, pre-tax, unlevered. Not a probability distribution or a price forecast. Hypothetical 100 MWac/132 MWdc profile priced at each node.", manual=dict(left=0.07, right=0.985, wspace=0.7, bottom_in=0.55))
    rec(png, vec, "support/original-figures/empirical/F2_weather_by_price_matrix.png", [EMP / "A_3x3_summary.csv", EMP / "A_3x3_cells_by_node.csv"], "grp, weather_year, price_year, npv_4p27_median, npv_positive_share; node == TAYGETE2_ALL, npv_4p27", "F2", "pivot; $ million scaling; share panel uses a single-hue scale without colour bar (values printed in cells)", "485 strict resource nodes (median) and the reference node; common calendar")

def F3():
    dec = pd.read_csv(EMP / "A_decomposition_by_node.csv"); st = dec[dec.tier == "strict"]; med = st.groupby(["from_year", "to_year", "component"]).npv_change_usd.median().unstack() / 1e6; trs = [(2023, 2024), (2023, 2025), (2024, 2025)]; fig, ax = T.newfig(3.7, ncols=2)
    def stack(a, comps, cols, title):
        xs = np.arange(3); pos = np.zeros(3); neg = np.zeros(3)
        for c, col in zip(comps, cols):
            v = np.array([med.loc[(x, y), c] for x, y in trs]); b = np.where(v >= 0, pos, neg); a.bar(xs, v, 0.55, bottom=b, color=col, label=c.replace("_lmdi", "").replace("_", " ")); pos += np.where(v >= 0, v, 0); neg += np.where(v < 0, v, 0)
        a.plot(xs, [med.loc[(x, y), "total_change"] for x, y in trs], "D", color=T.INK, ms=4.5, label="total change", zorder=5); a.set_xticks(xs); a.set_xticklabels([f"{x}→{y}" for x, y in trs]); a.axhline(0, color=T.INK, lw=0.8); a.set_title(title, fontsize=7.6); a.legend(fontsize=6.3, loc="lower right"); T.hgrid(a, "y")
    stack(ax[0], ["weather_pure", "price_pure", "interaction"], [T.AMBER, T.NAVY, T.SLATE_L], "Weather vs price (pure effects + interaction)")
    stack(ax[1], ["volume_lmdi", "price_level_lmdi", "match_lmdi", "rule_effect"], [T.AMBER, T.NAVY, T.TEAL, T.SLATE_L], "Volume, level, timing match, rule (LMDI)"); ax[0].set_ylabel("Change in NPV, $ million (median)")
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F3_npv_change_decomposition.png", "Alternative decompositions of the year-to-year NPV change", "Two separate accounting identities; each bar stack is a set of component medians, which need not add to the median total", "Source: empirical candidate decomposition tables, 485 strict resource nodes. Shapley allocation of the interaction is reported in the text; here the pure effects and the interaction are shown. Model-internal accounting, not causal effects of capacity additions, AI demand or network constraints.")
    rec(png, vec, "support/original-figures/empirical/F3_npv_change_decomposition.png", [EMP / "A_decomposition_by_node.csv"], "tier == strict, from_year, to_year, component, npv_change_usd", "F3", "median over nodes per component; $ million scaling", "485 strict resource nodes; NPV change at 4.27%")

def F4():
    cum = pd.read_csv(EMP / "plot_inputs/F4_cumulative_revenue_share_TAYGETE2_ALL.csv"); tail = pd.read_csv(EMP / "C_tail_results_by_node_year.csv", low_memory=False); REF = "TAYGETE2_ALL"; fig, ax = T.newfig(3.4, ncols=2)
    for y, st in T.YEAR.items():
        d = cum[cum.year == y]; ax[0].plot(d.top_share_of_intervals_pct, d.cumulative_share_of_revenue_pct, color=st["color"], ls=st["ls"], label=st["lab"])
    ax[0].set_xscale("log"); ax[0].set_xlim(0.01, 100); ax[0].set_xticks([0.01, 0.1, 1, 10, 100]); ax[0].set_xticklabels(["0.01", "0.1", "1", "10", "100"]); ax[0].set_ylim(0, 102); ax[0].set_xlabel("Top x% of 15-minute intervals ranked by price (log scale)"); ax[0].set_ylabel("Share of year's revenue (%)"); ax[0].legend(loc="upper left"); ax[0].set_title(f"Revenue concentration, {REF}", fontsize=7.8); T.hgrid(ax[0], "y")
    t = tail[tail.node == REF].assign(top_pct=lambda d: d.top_pct.astype(str)); cases = [("raw", None), ("drop\ntop 0.1%", "0.1"), ("drop\ntop 1%", "1"), ("cap at\np99", "cap_p99.0"), ("drop days\n≥ $1,000", "scarcity_days_ge1000")]; w = 0.26; xs = np.arange(len(cases))
    for i, (y, st) in enumerate(T.YEAR.items()):
        v = []
        for lab, k in cases: v.append(t[t.year == y].npv_raw.iloc[0] / 1e6 if k is None else t[(t.year == y) & (t.top_pct == k)].npv_drop_top_price_intervals.iloc[0] / 1e6)
        ax[1].bar(xs + (i - 1) * w, v, w * 0.94, color=st["color"], label=st["lab"])
    ax[1].axhline(0, color=T.INK, lw=0.8); ax[1].set_xticks(xs); ax[1].set_xticklabels([c[0] for c in cases], fontsize=6.6); ax[1].set_ylabel("NPV at 4.27%, $ million"); ax[1].legend(fontsize=6.6, loc="upper right"); ax[1].set_title("Stress cases beside the raw result", fontsize=7.8); T.hgrid(ax[1], "y")
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F4_tail_concentration_and_stress.png", "Revenue concentration and tail stresses (reference node)", "Single node TAYGETE2_ALL, stop-below-zero rule; cross-node medians are reported in the text", "Source: empirical candidate. Left: sorted interval revenue from frozen plot inputs; right: tail table. Tail deletion and caps are stress scenarios shown beside the unmodified prices, not corrections to history. Hypothetical output profile priced at the node.")
    rec(png, vec, "support/original-figures/empirical/F4_tail_concentration_and_stress.png", [EMP / "plot_inputs/F4_cumulative_revenue_share_TAYGETE2_ALL.csv", EMP / "C_tail_results_by_node_year.csv"], "year, top_share_of_intervals_pct, cumulative_share_of_revenue_pct; node == TAYGETE2_ALL: top_pct, npv_raw, npv_drop_top_price_intervals", "F4", "left panel: ranked cumulative curve read from plot input (sorted/cumulated by extract_empirical_plot_inputs.py)", "Reference node, three price years; NPV at 4.27%")

def F5():
    co = pd.read_csv(EMP / "tables/B_regression_coefficients_long.csv"); bb = pd.read_csv(EMP / "tables/B_solar_coef_block_bootstrap.csv"); k = co[(co.term == "solar_gw") & (co.dep == "HB_BUSAVG") & ~co.spec.str.startswith(("LPM", "S1_median"))].copy()
    names = {"S1": "S1 baseline (pooled)", "S2": "S2 load spline", "S3": "S3 date fixed effects", "S4": "S4 nonlinear solar", "S5_2023": "S5 by year: 2023", "S5_2024": "S5 by year: 2024", "S5_2025": "S5 by year: 2025", "S6": "S6 midday hours (11:00–16:59)", "S1_wins": "S1, price winsorized 0.5/99.5", "S1_ex1000": "S1, hours ≥ $1,000 excluded"}
    k["label"] = k.spec.map(names); k = k.iloc[::-1]; y = np.arange(len(k)); fig, ax = T.newfig(3.6); colr = [T.YEAR[int(s[-4:])]["color"] if s.startswith("S5_") else T.NAVY for s in k.spec]
    for yy, (c, lo, hi, col) in enumerate(zip(k.coef, k.coef - 1.96 * k.se_hac168, k.coef + 1.96 * k.se_hac168, colr)): ax.plot([lo, hi], [yy, yy], color=col, lw=1.4); ax.plot([lo, lo], [yy - .12, yy + .12], color=col, lw=1.1); ax.plot([hi, hi], [yy - .12, yy + .12], color=col, lw=1.1); ax.plot([c], [yy], "o", color=col, ms=4.8)
    for yy, c in zip(y, k.coef): ax.text(max(0.2, 0) + 0.15, yy, T.fmt(c, 2), va="center", fontsize=6.8, color=T.MUTED)
    ax.set_yticks(y); ax.set_yticklabels(k.label); ax.axvline(0, color=T.INK, lw=0.8); ax.set_xlim(-13.5, 2.2); ax.set_xlabel("Coefficient on system solar, USD/MWh per +1 GW (point; 95% HAC-168-hour interval)"); T.hgrid(ax, "x")
    ax.text(0.01, 1.01, "  ".join(f"{r.spec} moving-block bootstrap 95%: [{T.fmt(r.ci95_lo, 2)}, {T.fmt(r.ci95_hi, 2)}]" for _, r in bb.iterrows()), transform=ax.transAxes, fontsize=6.6, color=T.MUTED, va="bottom")
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F5_solar_price_association_forest.png", "Solar-price associations across specifications", "Hourly HB_BUSAVG price on system solar output, conditional on load, wind, gas, temperature and calendar effects; association only", "Source: empirical candidate regression tables (26,298 hourly observations in pooled specifications). Coefficients are conditional associations, not causal effects or project revenue forecasts; the held-out 2025 prediction check does not outperform simple benchmarks.", top_pad=0.12)
    rec(png, vec, "support/original-figures/empirical/F5_solar_price_association_forest.png", [EMP / "tables/B_regression_coefficients_long.csv", EMP / "tables/B_solar_coef_block_bootstrap.csv"], "dep == HB_BUSAVG, term == solar_gw, spec, coef, se_hac168; bootstrap ci95_lo/hi", "F5", "95% interval = coef ± 1.96 × se_hac168 (as original)", "USD/MWh per GW; hourly benchmark price; 2023–2025")

def F6():
    h = pd.read_csv(EMP / "plot_inputs/F6_hourly_HB_BUSAVG_and_system_solar.csv"); h["g"] = h.solar_mw / 1000; h["sb"] = pd.cut(h.g, [-.01, 0.01, 2, 5, 8, 11, 14, 17, 20, 23, 30]); fig, ax = T.newfig(3.4, ncols=2)
    for y, st in T.YEAR.items():
        d = h[h.year == y].groupby("sb", observed=True).HB_BUSAVG_hourly_mean_usd_mwh.agg(["mean", "median", "count"]); xs = np.arange(len(d)); ax[0].plot(xs, d["mean"], color=st["color"], marker=st["marker"], ms=3.4, ls=st["ls"], label=f"{y} mean"); ax[0].plot(xs, d["median"], color=st["color"], marker="x", ms=3.2, ls=(0, (1, 2)), alpha=.75, lw=0.9)
    ax[0].set_xticks(range(len(d))); ax[0].set_xticklabels(["0"] + [f"{i.left:g}–{i.right:g}" for i in d.index[1:]], rotation=45, fontsize=6.4, ha="right"); ax[0].set_xlabel("System solar output bin (GW)"); ax[0].set_ylabel("HB_BUSAVG hourly price (USD/MWh)"); ax[0].legend(fontsize=6.4, loc="upper right", ncol=1); ax[0].set_title("Price by solar bin (means; medians dotted, ×)", fontsize=7.8)
    ng = h.assign(neg=h.HB_BUSAVG_hourly_mean_usd_mwh < 0).groupby(["year", "local_hour"]).neg.mean().unstack(0) * 100
    for y, st in T.YEAR.items(): ax[1].plot(ng.index, ng[y], color=st["color"], ls=st["ls"], label=st["lab"])
    ax[1].set_xlabel("Local hour of day"); ax[1].set_ylabel("Hours with negative HB_BUSAVG price (%)"); ax[1].legend(); ax[1].set_title("Negative-price share by hour", fontsize=7.8); ax[1].set_xticks([0, 4, 8, 12, 16, 20])
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F6_price_vs_solar_and_negative_hours.png", "Price patterns and negative-hour incidence", "Descriptive binned patterns, hourly mean of HB_BUSAVG; no controls", "Source: empirical candidate frozen plot input (hourly mean of four 15-minute HB_BUSAVG prices joined to ERCOT system solar). Binned patterns are descriptive; regression interpretation requires the stated controls, sample and inference method.")
    rec(png, vec, "support/original-figures/empirical/F6_price_vs_solar_and_negative_hours.png", [EMP / "plot_inputs/F6_hourly_HB_BUSAVG_and_system_solar.csv"], "solar_mw, local_hour, year, HB_BUSAVG_hourly_mean_usd_mwh", "F6", "binning in the original bin edges; mean/median by bin; share of hours below zero by local hour", "Hourly, 26,304 hours, 2023–2025; USD/MWh and percent of hours")

def F7():
    bs = pd.read_csv(EMP / "tables/B3_node_basis_stats.csv"); W = bs.pivot(index="node", columns="year", values="mean_basis"); zc = bs.drop_duplicates("node").set_index("node").zone.reindex(W.index); fig, ax = T.newfig(3.4, ncols=2)
    for z, (c, mk) in T.ZONE.items():
        m = zc == z; ax[0].scatter(W.loc[m, 2023], W.loc[m, 2025], s=9, color=c, marker=mk, alpha=.75, label=z, linewidths=0)
    lim = [min(W.min().min(), -22), max(W.max().max(), 62)]; ax[0].plot(lim, lim, color=T.INK, lw=0.7, ls=":"); ax[0].set_xlabel("Mean basis to HB_BUSAVG, 2023 (USD/MWh)"); ax[0].set_ylabel("Mean basis, 2025 (USD/MWh)"); ax[0].legend(fontsize=6.3, loc="upper left"); ax[0].set_title("Node mean basis, 2023 vs 2025", fontsize=7.8)
    bins = np.linspace(0, 200, 41)
    for y, st in T.YEAR.items(): ax[1].hist(bs[bs.year == y].sd_basis.clip(upper=199.9), bins=bins, histtype="step", lw=1.5, color=st["color"], ls=st["ls"], label=st["lab"])
    ax[1].set_xlabel("Std. dev. of hourly basis (USD/MWh; ≥200 pooled)"); ax[1].set_ylabel("Resource nodes"); ax[1].legend(); ax[1].set_title("Dispersion of hourly basis, by year", fontsize=7.8); T.hgrid(ax[1], "y")
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F7_node_basis_persistence.png", "Cross-year persistence of node basis", "485 resource nodes; basis = node hourly price − HB_BUSAVG hourly price; coloured by official load zone", "Source: empirical candidate basis tables. Basis is a price difference, not a direct measure of congestion cost; one current classification snapshot. Dotted line: equal basis in both years. The right panel truncates the display range at 200 USD/MWh (a few nodes exceed it).")
    rec(png, vec, "support/original-figures/empirical/F7_node_basis_persistence.png", [EMP / "tables/B3_node_basis_stats.csv"], "node, year, mean_basis, sd_basis, zone", "F7", "right panel drawn as step histograms (original: filled) with display clipping at 200 (disclosed on chart)", "485 resource nodes; hourly basis, 2023–2025")

def F8():
    boot = pd.read_csv(EMP / "C_block_bootstrap_within_year.csv"); mix = pd.read_csv(EMP / "C_three_year_mixture_scenario_by_node.csv"); REF = "TAYGETE2_ALL"; bt = boot[boot.node == REF]; fig, ax = T.newfig(3.4, ncols=2)
    cols = {1: T.SLATE, 7: T.NAVY, 28: T.AMBER}
    for i, y in enumerate(T.YEAR):
        for j, L in enumerate((1, 7, 28)):
            r = bt[(bt.year == y) & (bt.block_days == L)].iloc[0]; x = i + (j - 1) * 0.22; ax[0].errorbar(x, r.npv_p50 / 1e6, yerr=[[(r.npv_p50 - r.npv_p05) / 1e6], [(r.npv_p95 - r.npv_p50) / 1e6]], fmt="o", color=cols[L], capsize=3, ms=4.5, label=f"{L}-day blocks" if i == 0 else None)
    ax[0].axhline(0, color=T.INK, lw=0.8); ax[0].set_xticks(range(3)); ax[0].set_xticklabels(list(T.YEAR)); ax[0].set_ylabel("NPV, $ million (median; 5th–95th pct.)"); ax[0].set_title(f"Within-year day-block bootstrap, {REF}", fontsize=7.8); ax[0].legend(fontsize=6.6, loc="upper right"); T.hgrid(ax[0], "y")
    mm = mix[mix.tier == "strict"]; ax[1].hist(mm.npv_mixture / 1e6, bins=40, color=T.SLATE, edgecolor="white", linewidth=0.4); ax[1].axvline(0, color=T.INK, lw=0.8); ax[1].set_xlabel("Equal-weight mixture NPV, $ million"); ax[1].set_ylabel("Resource nodes"); ax[1].set_title("Mixture setting (not a forecast)", fontsize=7.8); T.hgrid(ax[1], "y")
    png, vec = T.finish(fig, T.Path(OUT) / "empirical" / "F8_bootstrap_and_mixture_scenario.png", "Within-year resampling and a three-year mixture setting", "Resampling conditions on each historical year; the mixture is an equal-weight analytical setting", "Source: empirical candidate. Resampling uncertainty is conditional on a particular year and is not a long-run probability; the mixture weights are an assumption, not an estimated expectation. Hypothetical output profile priced at each node; pre-tax, unlevered.")
    rec(png, vec, "support/original-figures/empirical/F8_bootstrap_and_mixture_scenario.png", [EMP / "C_block_bootstrap_within_year.csv", EMP / "C_three_year_mixture_scenario_by_node.csv"], "node == TAYGETE2_ALL: year, block_days, npv_p05, npv_p50, npv_p95; tier == strict: npv_mixture", "F8", "$ million scaling; histogram 40 bins", "Reference node bootstrap (2,000 draws per cell); 485 nodes' mixture NPV")

REG = [f01, f03, f04, f05, f06, f08, s01, s02, s03, s04, s05, s06, s07, s1, s2, s3, s4, s5, s6, F1, F2, F3, F4, F5, F6, F7, F8]
def main():
    global OUT
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=str(PK / "figures")); ap.add_argument("--only", nargs="*"); a = ap.parse_args(); OUT = Path(a.out)
    for f in REG:
        if a.only and f.__name__ not in a.only: continue
        f(); print("rendered", f.__name__)
    with open(PK / "support/Figure-Rendering-Lineage.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(LIN[0].keys())); w.writeheader(); w.writerows(LIN)
    json.dump(T.SNAP, open(PK / "support/Figure-Plot-Data-Snapshot.json", "w"))
    print(len(LIN), "exhibits rendered")

if __name__ == "__main__": main()
