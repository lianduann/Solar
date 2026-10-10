"""Independent finance arithmetic for the 2026-10-09 finance-deepening supplement.

Reads only frozen/retained inputs and this supplement's own extracts; no model run, no regression, no weather simulation.
  --panel   Deliverables/2026-10-09_Panel-Revision-Client-Edition   (frozen panel edition; read-only)
  --supp    Deliverables/2026-10-09_Finance-Deepening-Supplement   (this supplement; reads data/*.csv, writes data/Finance-Arithmetic-Checks.csv)
Every row states inputs, formula and result so a reviewer can recompute by hand.
"""
import argparse, json
from pathlib import Path
import pandas as pd

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--panel", required=True); ap.add_argument("--supp", required=True); a = ap.parse_args()
    P, S = Path(a.panel), Path(a.supp); rows = []
    add = lambda cid, topic, inputs, formula, value, unit, note="": rows.append(dict(check_id=cid, topic=topic, inputs=inputs, formula=formula, result=value, unit=unit, note=note))

    # 1. Comparable observable cost metrics: Ch313 Form 773 (2023) self-reported qualified investment / EIA-860 2025 capacity
    f773 = pd.read_csv(S / "data/Ch313-Form773-2023-Extract.csv")
    v = f773.pivot_table(index="local_file", columns="field", values="value", aggfunc="first").set_index("Application ID")
    eia = pd.read_csv(S / "data/EIA-860-2025_WestTX_PV_generators.csv")
    cap = {  # Ch313 application id -> EIA plant code(s) matched in Entity-Node-Mapping.csv
        "1377": [64075], "1519": [63233], "1761": [67006], "1463": [64325]}
    # plants outside the West-Texas county list of script 02 (Concho, Tom Green, Runnels) taken from EIA-860 2025 3_3_Solar rows quoted in Comparable-Projects.csv
    extra = {"1431": (110.0, 146.6), "1451": (172.8, 214.6), "1764": (195.0, 263.0), "1679": (125.0, 159.3)}
    for app, r in v.iterrows():
        made = float(r["The Amount The Agreement Holder Had Made to Date"])
        if str(app) in cap:
            g = eia[eia["Plant Code"].isin(cap[str(app)])]; mwac, mwdc = g.cap.sum(), g.dc.sum()
        else:
            mwac, mwdc = extra[str(app)]
        cod = str(r["Date Of Commmencement of Commercial Operations"]); committed = float(r["Amount of Qualified Investment the Applicant Committed"])
        flag = "INCOMPLETE - project under construction at the 2023 report (self-reported COD " + cod + "); not a cost metric" if cod.endswith(("2024", "2025")) else \
               "Ch313 qualified investment as self-reported in a mid-2023 filing; excludes land and property not owned by applicant; not all-in funded cost; not CPI-adjusted; may be incomplete if spending continued after the filing"
        if made > 0:
            add(f"C-{app}-ac", "comparable cost", f"Form 773 2023 'amount made to date' {made:,.0f} USD (committed {committed:,.0f}); EIA-860 2025 {mwac} MWac", "USD / (MWac*1000)", round(made / (mwac * 1000), 1), "USD/kWac (nominal, as reported 2023)", flag)
            add(f"C-{app}-dc", "comparable cost", f"same; EIA-860 2025 {mwdc} MWdc", "USD / (MWdc*1000)", round(made / (mwdc * 1000), 1), "USD/kWdc (nominal, as reported 2023)", "")
        else:
            add(f"C-{app}-ac", "comparable cost", f"Form 773 2023 'amount made to date' {made:,.0f}", "n/a", None, "USD/kWac", "No investment reported by 2023; not computable")

    # 2. Frozen-model cross-checks (panel edition)
    pc = json.load(open(P / "data/panel/Panel-Calculations.json")); be = json.load(open(P / "data/breakevens.json"))
    k = be["fixed_breakeven_price_nominal_flat_at_0.0427"]; s = be["negative_price_energy_anchor"]
    add("M-01", "fixed-route unpaid-energy stress", f"break-even {k:.6f} with unpaid share {s:.6f}", "K*(1-s)", round(k * (1 - s), 4), "USD/MWh nominal flat",
        f"Panel no_unpaid_breakeven = {pc['no_unpaid_breakeven']:.4f}; identity holds because unpaid share scales paid MWh uniformly")
    add("M-02", "fixed-route unpaid-energy stress", f"unpaid share 2x anchor = {2*s:.6f}", "K_no_unpaid/(1-2s)", round(pc["no_unpaid_breakeven"] / (1 - 2 * s), 4), "USD/MWh nominal flat",
        "Break-even under the 30.48% downside unpaid share, all else as the 4.27% base; arithmetic implication only")
    capex = pc["capex"]; occ = pc["occ"]; gcc = pc["gcc"]
    add("M-03", "basis split", f"capex {capex:,.0f}; occ {occ:,.0f}; gcc {gcc:,.0f}", "occ+gcc-capex", round(occ + gcc - capex, 2), "USD 2025", "Zero confirms the frozen split used by the basis crosswalk")
    add("M-04", "illustrative ITC base if GCC excluded", f"occ {occ:,.0f}", "0.30*occ", round(0.30 * occ, 0), "USD 2025 real (not nominal)",
        "Shows scale only: 48E(b)(1)(B) admits interconnection property only for <=5 MWac facilities; eligibility of each OCC item, PWA, MACR and timing remain unproven")
    add("M-06", "panel credit illustration rescaled to OCC-only base", f"panel credit_pv {pc['credit_pv']:,.0f}; occ/capex {occ/capex:.6f}", "credit_pv*occ/capex", round(pc["credit_pv"] * occ / capex, 0), "USD PV at 4.27% (same timing as panel)",
        f"Removes GCC ({gcc/capex:.2%} of capex) from the illustrative base only; node NPV with this credit would be {pc['node_npv_with_credit'] - pc['credit_pv'] + pc['credit_pv']*occ/capex:,.0f} - still an eligibility-unproven scenario")
    add("M-05", "ITC basis reduction", "credit 0.30*occ", "0.5*0.30*occ", round(0.15 * occ, 0), "USD 2025 real", "50(c)(3): depreciable basis reduced by 50% of the credit")

    # 3. ATB nominal->real (Fisher) with the frozen register's inputs
    for nm, r in [("ATB debt 6.5% nominal", 0.065), ("ATB equity 8.0% nominal", 0.08)]:
        add(f"R-{nm[:8]}", "nominal to real", f"{nm}; inflation 2.5%", "(1+r)/(1.025)-1", round((1 + r) / 1.025 - 1, 5), "real rate", "")
    w = (0.065 * 0.7457 + 0.08 * 0.2543 + 1) / 1.025 - 1
    add("R-WACC", "frozen discount rate", "debt 6.5% x 0.7457 + equity 8.0% x 0.2543; inflation 2.5%", "(1+wacc_nom)/1.025-1", round(w, 5), "real pre-tax", "Equals the frozen 4.27% analytical rate; no tax shield")

    # 4. CPI-U annual averages (retained BLS file) for FIN-07
    cpi = {2022: 292.655, 2023: 304.702, 2024: 313.689, 2025: 321.943}
    for y in (2023, 2024):
        add(f"CPI-{y}", "price-year restatement", f"CPI-U {y} {cpi[y]}; 2025 {cpi[2025]}", "CPI2025/CPIy", round(cpi[2025] / cpi[y], 6), "multiplier to 2025 USD", "For a separately labelled CPI-harmonised scenario only")

    # 5. Hub-settled VPPA identity with H=G (as-generated), no fees/REC, all intervals, frozen panel comparison table
    nh = pd.read_csv(P / "data/panel/Node-Hub-Comparisons.csv")
    for y in (2023, 2024, 2025):
        d = nh[(nh.price_year == y)].set_index("node")
        b = d.loc["TAYGETE2_ALL", "generation_weighted_node_minus_west_basis"]
        add(f"V-{y}", "VPPA identity", f"{y}: gen-weighted (P_node - P_HB_WEST) = {b:.4f}", "realised USD/MWh = K + basis (H=G, no curtailment, no fees)", round(b, 4), "USD/MWh added to strike K",
            f"Node capture {d.loc['TAYGETE2_ALL','capture_price']:.3f} vs HB_WEST capture {d.loc['HB_WEST','capture_price']:.3f}; shape risk sits in the hub capture, not the basis")

    # 6. PUCT 25.195(f)(3) allowance scale for a 100 MWac case
    add("I-01", "interconnection allowance", "16 TAC 25.195(f)(3)(A)(i): 2024 base 14,000,000 (<=138 kV); 100 MWac", "14e6/(100*1000)", 140.0, "USD/kWac (2024 base, CPI-indexed annually)",
        "TSP bears interconnection-facility costs up to the allowance for SGIAs executed after 2025-12-31; excess billed to the generator; upgrades remain TSP")
    add("I-02", "interconnection allowance", "2024 base 20,000,000 (>138 kV)", "20e6/(100*1000)", 200.0, "USD/kWac (2024 base)", "")
    add("I-03", "frozen GCC scale", f"gcc {gcc:,.0f}", "gcc/(100*1000)", round(gcc / 1e5, 1), "USD/kWac 2025", "ATB national grid-connection cost; its split between generator and TSP under the ERCOT rule is unknown")

    # 7. Property tax evidence scale (Taygete II Ch313 #1377 application, Schedule D; Comptroller certificate)
    add("T-01", "county abatement scale", "Schedule D: Pecos County Ch.312, levy without incentive 1,169,058/yr; net levy 1,000/MW; 255 MW", "1169058/255000", round(1169058 / 255000, 2), "USD/kWac-yr county levy before abatement (2019 estimate)", "")
    add("T-02", "school M&O limitation scale", "Comptroller amended certificate: 15-yr M&O levy without limit 20,566,659; with limit 6,609,943; 255 MW", "(20566659-6609943)/15/255000", round((20566659 - 6609943) / 15 / 255000, 2), "USD/kWac-yr average gross M&O benefit (2019-era estimate)",
        "Chapter 313 no longer accepts new agreements per secondary sources; JETI FAQ lists dispatchable generation, so the benefit cannot be assumed for a 2026-27 standalone PV case")
    out = pd.DataFrame(rows); out.to_csv(S / "data/Finance-Arithmetic-Checks.csv", index=False); print(out[["check_id", "result", "unit"]].to_string())

if __name__ == "__main__":
    main()
