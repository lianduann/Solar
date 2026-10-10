# Research Log: Finance Deepening

**Date:** 2026-10-09 (America/New_York).

**Basis:** the compilation-day brief and its updated version with the "追加" section, received the same evening. The updated version targets the panel-revision edition. Execution took place on the brief's compilation date; nothing here is backdated.

**What this log records:** operations and results only. It records no hours. It does not update the weekly work log or any frozen report, data set, register or quality status.

## Operations and results

1. **Workspace rules and project documents.** I read `AGENTS.md`, `README.md`, `PROJECT_STATUS.md`, `Project-Brief.md`, `Methods-and-Data.md`, the client-readable and panel-revision editions, and the expert and panel reviews. I did not access `90-Private-Documents/`.

2. **Node and hub price check against the frozen panel table.**
   - I extracted TAYGETE2_ALL, HB_WEST, HB_BUSAVG, HB_HUBAVG and LZ_WEST from the retained NP6-905-CD archives for 2023–2025. I weighted them with the existing same-year 15-minute site-energy series, copied unchanged into `Data/raw/2026-10-09_Finance-Deepening/solar-weights-reused/`. Their annual totals match the frozen `site_energy_qa.csv`.
   - Results: TAYGETE2_ALL generation-weighted price of 22.13 USD/MWh in 2025, HB_WEST 21.46, and node-minus-HB_WEST basis of −0.05 / +0.25 / +0.67 USD/MWh.
   - These agree with the frozen panel `Node-Hub-Comparisons.csv` within 0.004 USD/MWh (`Verification.json`).
   - After the updated brief arrived, I treat the frozen table as primary and mine as an independent reproduction. A later re-run with extra columns was interrupted before producing output, and I restored the script (Access-Blockers AB-11).

3. **EIA operating-generation comparables.**
   - I downloaded EIA-923 2023 (final revision) and 2025 (final), and EIA-860 2025 (final), from eia.gov.
   - I built monthly and annual AC capacity factors for 36 PV plants in Pecos, adjacent and nearby West Texas counties, plus three other ERCOT counties that hold Chapter 313 comparables.
   - Results: Pecos clean full-year medians of 24.8% (2024) and 24.6% (2025). Taygete II ran 28.1% / 25.5% and Emerald Grove 29.4% / 27.1%.

4. **Tax law.**
   - I retained P.L. 119-21, the enrolled bill, IRS Notices 2025-42, 2026-15 and 2026-11, EO 14315, the 45Y 2026 inflation notice, LII renderings of 26 U.S.C. 45Y, 48E, 50 and 168, and the D.D.C. opinion vacating Notice 2025-42.
   - I personally verified the statute's termination text and effective-date clause (§70512(a), (l)(4); §70513(g)(5)), the vacatur order (opinion pp.1 and 57) and 48E(b)(1)(B).

5. **ERCOT, PUCT and market sources.**
   - I retained the RTC+B go-live release (5 December 2025), the December 2025 board update, the October 2023 board system-operations update (85,464 MW record; 6 September 2023 EEA2 timeline) and the current 16 TAC §25.195 rule PDF.
   - I computed ERCOT battery capacity by operating year from EIA-860 2025: 4.0 GW (end-2023), 8.1 GW (end-2024) and 13.7 GW (end-2025).

6. **O&M and capex scope.** From previously retained files I read the ATB 2025 page and the PVSCM 2024Q1 and 2025Q1 parameter files. They itemise land lease, property tax, insurance, management, inverter replacement and the network-upgrade line.

7. **Comparables.**
   - I retained Texas Comptroller Chapter 313 applications, amendments, agreements, Form 773 (2023) and Form 772 (2025) for eight projects.
   - I also retained the ERCOT CDR (December 2021), MORA (December 2026) and NP4-160 (October 2026) files.
   - I extracted all Form 773 fields (`data/Ch313-Form773-2023-Extract.csv`) and read the Taygete II Form 772 pages as images: a 2024 CAD market value of 166.05m, and the foreclosure-auction ownership statement.
   - I closed the TAYGETE2_ALL → Taygete II → West Texas Solar Project II LLC chain (`Entity-Node-Mapping.csv`).
   - I retained the CIT December 2020 Taygete I financing release and two 2019 trade-press articles.

8. **PPA references.** I retained the LevelTen Q2 2026 public post and two pv magazine articles: ERCOT solar P25 of 49 USD/MWh for Q4 2025, and the continental solar P25 of 52.65 USD/MWh for Q2 2026.

9. **Property tax.** I retained the Comptroller JETI FAQ ("dispatchable electric generation facilities are eligible") and the Chapter 313 landing page.

10. **Finance arithmetic.** I computed comparable cost per kW, the fixed-route break-even under 0% / 15.24% / 30.48% unpaid energy, Fisher conversions, CPI factors, the VPPA basis terms, the interconnection-allowance scale, property-tax scale and the OCC-only credit illustration (`data/Finance-Arithmetic-Checks.csv`).
   - Independent hand check: Taygete II 212,584,851 / 203,800 kW = 1,043.1 USD/kWac.
   - Panel no-unpaid break-even reproduced: 65.9692 × (1 − 0.152417) = 55.9143.

11. **Verification.** I ran a clean-directory re-run of scripts 02–05. All six regenerated tables are identical to the delivered ones (`Verification.json`). No regression, bootstrap or weather simulation was run.

## Problem and resolution status

| Problem or risk | Status | How I handled it today | Evidence or file | Next step if unresolved |
|---|---|---|---|---|
| No comparable discloses an IRR | Unresolved | Reported "not disclosed"; no estimated IRR | Return-Metric-Comparability.csv | Search owner filings for asset-level cash flows (Research-Disposition FIN-01) |
| ERCOT-to-EIA link for the reference node is attribute-based | Partially resolved | Documented every link and its evidence type | Entity-Node-Mapping.csv | Historical NP4-160 versions; any official crosswalk |
| Panel credit illustration includes grid-connection cost in the base | Partially resolved | Showed the statutory exclusion and its arithmetic effect; did not change the frozen output | Basis-Crosswalk.csv; Finance-Arithmetic-Checks M-06 | Author decision on the replacement text |
| Possible double count of inverter replacement and the network-upgrade allowance | Partially resolved | Identified it from the parameter files; recommended a sensitivity | Cost-Coverage-Crosswalk.csv | ATB Components-of-CAPEX export (AB-05) |
| Post-RTC+B prices not retained | Unresolved | Reported the 27-day window as a cross-check only | Regime-Evidence.csv | ERCOT 2026 NP6-905-CD archives (AB-06) |
| Supplier liquidity not researched | Unresolved | Kept the placeholder | Supplier-Liquidity.csv | Company filings listed there |
