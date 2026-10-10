# Expert B: Project Finance and Financial Modelling Review (independent first round)

**Report reviewed:** SOLAR-001, *From China's Solar Supply Chain to U.S. Power Markets*, closure-integrated candidate edition, 9 October 2026 (73-page PDF and Markdown).
**Reviewer role:** Expert B, project finance and financial modelling.
**Review date:** 10 October 2026.
**Standard applied:** review brief §4 (scope of use) and §6 (severity and verdict criteria). The edition is a candidate research edition, not the original Version 1.0. I did not rerun any model, fetch any web source or add any data. All checks below are either "reviewer arithmetic" on numbers printed in the report or comparisons with the frozen files in the evidence package.

---

## 1. Scope and method

**Chapters read in full:** 1 (summary, Table 1-1), 2.2–2.4, 5.5–5.6, 8.1–8.2, 9.5, 10 (all), 11.1–11.4, 11.7 (Table 11-3), 13.2, 13.5, Appendix A.1–A.2, B.2, B.5 and C.

**Files spot-checked** (package root `2026-10-09_Closure-Integrated-Client-Edition/`):

| Area | Files |
|---|---|
| Frozen baseline | `data/scenario_metrics.csv`, `data/scenario_annual_cash_flows.csv`, `data/breakevens.json`, `data/sensitivity_one_way.csv`, `data/scenario_input_register.csv` |
| Panel and finance arithmetic | `data/panel/Node-Hub-Comparisons.csv`, `data/finance/Unpaid-Energy-Stress.csv`, `data/finance/Qualified-Investment-Comparisons.csv`, `data/finance/Finance-Integration-Calculations.json` |
| Node and hub capture | `finance-supplement/data/Node-Hub-Solar-Capture-2023-2025.csv` |
| Separately versioned scenarios | `scenario-versions/Scenario-Notes-EN.md`; `scenario-versions/data/` files `Credit-Base-Scenarios.csv`, `VPPA-Breakeven-Strikes.csv`, `VPPA-Route-Scenarios.csv`, `CPI-Harmonised-Scenario.csv`, `scenario_build_log.json` |
| Closure records | `closure-evidence/Closure-Disposition.csv`, `closure-evidence/Numbers-and-Claims.csv` |

**Figures viewed:** Figure 10-1 (`Panel_Scenario_NPV.png`) and Figure 10-2 (`S4_annual_cash_flows.png`, also as PDF physical page 42).

### 1.1 Arithmetic spot checks (reviewer arithmetic): all reproduce

Every number below reproduces to the printed precision.

**Discount rate**
- The 4.27% convention: [(0.065 × 0.7457 + 0.080 × 0.2543) + 1] / 1.025 − 1 = 4.275%.
- ATB debt and equity in real terms: 1.065/1.025 − 1 = 3.90%; 1.08/1.025 − 1 = 5.37%.

**Revenue, cost conversion and LCOE**
- Fixed-base year-1 revenue: 247.8195 GWh × $40 = $9.9128m nominal; ÷ 1.025² = $9.4351m in 2025 dollars.
- CPI factor: 321.943 / 304.702 = 1.0566.
- LCOE on potential output ($41.41) versus delivered output ($48.85): both match `scenario_metrics.csv`.

**NPV identity and Tables 10-4 and 10-5**
- Node base: 15.471935 × 6.550953 − 187.321206 = −85.97.
- Zero-NPV revenue threshold: 187.32 / 15.47 = $12.1m.
- Using the annual cash flows, I recomputed the receipts annuity and cost PV at 6% (12.8205; $179.29m) and 8% (10.569; $172.57m). Table 10-5 then reproduces: 2023 +58.61 / +23.55; 2024 −91.68 / −100.34.

**Break-evens**
- CAPEX: 143.67 − 85.97 = $57.7m, which is $577/kWac (40.2% of $1,437).
- Fixed contract at $40: $699/kWac.

**Paid-volume stress:** 55.91 / (1 − 0.1524) = 65.97; 55.91 / (1 − 0.3048) = 80.43.

**Credit illustration**
- OCC-only credit: 0.30 × 126.04 / 1.025 / 1.0427 = $35.38m.
- Original OCC+GCC version: $40.33m. Difference: $4.95m.
- NPV with credit: −85.97 + 35.38 = −50.59 (node); −73.74 + 35.38 = −38.36 (fixed).
- Break-even with credit: 65.97 − 35.38 / 2.8375 = $53.51/MWh, where 2.8375 = $22.70m per $8/MWh, the one-way sensitivity slope.
- Variants: receipt one year later $33.10m; transfer at 0.90 gives $31.84m; 6% statutory rate gives $7.08m. All match `Credit-Base-Scenarios.csv`.

**Replacement reserve:** 3.5 / 1.0427¹⁶ = $1.79m. This gives −84.17 (node) and −71.95 (fixed), matching `sensitivity_one_way.csv`.

**Module sensitivity**
- 126.04 × 26.111% × 1.144 × 10% = $3.76m.
- If the credit applies: 3.76 × (1 − 0.30/1.025/1.0427) = $2.71m.
- Zero module input: $37.65m saving, giving −$48.32m.

**CPI-restated version**
- Reference node 2023: (97.76 + 187.32) / 15.472 × 1.0566 × 15.472 − 187.32 = +113.89.
- 2024: −89.64.
- 485-node median 2023: about +116.0.

**One-way sensitivities:** ±$8/MWh gives ±$22.7m; the unpaid-energy range gives ±$20.4m; ±20% CAPEX gives ±$28.7m; ±20% price gives ±$20.3m; +10% export gives +$10.14m.

**Hub basis (Table 8-1):** −0.05 / +0.25 / +0.67 $/MWh. West hub capture ratios of 1.30, 0.75 and 0.65 match `Node-Hub-Solar-Capture-2023-2025.csv`.

**VPPA break-evens:** the eight 2025 combinations at 4.27% span $60.57–$84.77/MWh, and the 6%/8% rows span $68.38–$107.12/MWh. Both match `VPPA-Breakeven-Strikes.csv`.

**IRR roots:** the roots printed in §10.6 and B.2 match the `irr_roots` field in `scenario_metrics.csv`. Sign changes in the annual cash flows:

| Scenario | Negative years | Sign changes | Undiscounted sum |
|---|---|---|---|
| Node base | t = 0, 16, 30 | 4 | −$45.8m |
| Fixed upside | t = 0, 30 | 2 | +$23.5m |
| Node upside | t = 0 only | 1 | −$8.4m |

**Comptroller qualified investment:** $918.8–$1,103.3/kWac, which is the printed $0.92–$1.10/Wac.

**No arithmetic, unit or currency error was found in the financial chapters.**

### 1.2 Conceptual areas checked: no change needed

- **Cash-flow definitions and timing (§10.1, B.2).** These are coherent:
  - CAPEX is paid at end-2026, which is t = 0.
  - Thirty end-of-year operating flows run from 2027 to 2056.
  - All values are real 2025 dollars, valued at 2026.
  - Nominal series are built consistently with 2.5% inflation.
- **Real versus nominal handling.**
  - The flat nominal contract is correctly deflated, and §10.6 correctly explains why a first-year price above real LCOE ($45.69 versus $43.69, Fixed upside) still gives a negative NPV.
  - The problem that 2023 and 2024 nominal prices are reused as 2025-dollar real prices is disclosed (§10.9, B.2). A CPI-restated version is reported separately.
  - The calendar difference between full-year and common-calendar figures (−81.33 versus −81.59) is labelled at line 881.
- **IRR treatment.** It follows brief §4(4): no single IRR is reported where there are multiple roots, roots are disclosed, and NPV is the primary measure. Some wording refinements are listed in EB-04.
- **Cost scope.** OCC, GCC and FOM; the overlap between the replacement reserve and FOM; the PVSCM network-upgrade line; Texas property tax; and the fact that Comptroller qualified investment is not all-in cost are all explicitly bounded (§10.2, §10.7, Table 10-6, Figure 10-3 note). No overlap is silently netted or added.
- **Separation of the three revenue mechanisms.** The fixed-price route, the nodal route and the hub hedge are kept apart (§10.3, B.2 risk table). The two-leg identity G·P_node + H·(K − P_hub) is correctly stated. The merchant-tail dependence is disclosed, and so is the absence of fees, RECs and imbalance (not zero-cost).
- **Tax-credit illustration.** It is kept separate from the six frozen scenarios (lines 35, 822, 842, 1285). Its basis, timing, transfer, 6%-rate variants and the §50(c)(3) omission are disclosed.

---

## 2. Findings

### EB-01: LCOE and "delivered GWh" for the fixed-price route are on a paid-energy basis, but labelled as delivered energy (P1)

- **Location:** PDF p.41; MD §10.4 Table 10-2, lines 747–754. Also §10.6, line 774, and Table 1-1, line 44 ("Delivered-energy LCOE").
- **Quote:** "First-year delivered GWh … Fixed downside | 195.2 | … | 66.7".
- **Problem:** In the frozen model, the fixed-route "unpaid" share is removed from the energy denominator.
  - `scenario_metrics.csv`, `fixed_downside`: delivered 195.16 GWh = 280.74 × (1 − 0.3048); curtailed 85.58 GWh.
  - So the fixed-route "delivered GWh" and LCOE are really **paid-energy** quantities.
  - Fixed downside LCOE ($66.7) and Node downside LCOE ($54.8) share the same cost stream. The 1.218× ratio comes entirely from the denominator (237.7 / 195.2 = 1.218, reviewer arithmetic).
  - Meanwhile §10.3 (lines 706–708) describes the 15.24% / 30.48% as energy "deducted from payment". It even discusses a buyer who pays through negative-price intervals, which implies the energy may still be physically produced.
  - Table 2-1 (line 91) says LCOE uses "the stated … energy denominator". For the fixed rows, the stated denominator ("delivered") is not the one used.
- **Evidence:** `data/scenario_metrics.csv`, columns `delivered_mwh_yr1`, `curtailed_mwh_yr1`, `lcoe_real_at_0.0427`. `data/scenario_input_register.csv`, row `curtailment_fixed_pct` ("Unpaid curtailment … Seller bears curtailment by assumption").
- **Client consequence:** A developer comparing LCOE across routes may read the fixed-price structure as raising the plant's cost per MWh, or treat $66.7 as a physical-cost benchmark. In fact it is the same cost spread over fewer paid MWh.
- **Minimal fix:**
  - Rename the Table 10-2 column "First-year delivered (node) / paid (fixed) GWh".
  - Add to the table note: "For fixed-price rows, the unpaid share is treated as unsold energy, so delivered GWh and LCOE use paid energy. Fixed and node LCOEs with the same cost case differ only through this denominator."
  - In Table 1-1, keep "Delivered-energy LCOE" (node base and fixed base coincide at 247.8 GWh).
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### EB-02: The summary calls the base-case 15.24% unpaid share "severe" (P2)

- **Location:** PDF p.3; MD §1.1 item 2, line 29.
- **Quote:** "breaks even near $66/MWh with the severe assumed 15.24% unpaid-energy deduction".
- **Problem:** Elsewhere 15.24% is the **base** share and 30.48% is the doubled stress: line 706 ("doubles the stress"), line 712 ("15.24% base share"), and the register ("anchor"). The downside break-even is $80.43/MWh. Calling the base "severe" suggests that $66 is a conservative upper bound, which it is not under the report's own stress.
- **Evidence:** MD lines 706, 712; `data/finance/Unpaid-Energy-Stress.csv`.
- **Client consequence:** A buyer or seller could anchor on $66/MWh as the top of the range.
- **Minimal fix:** Replace with: "breaks even near $66/MWh (4.27% real) under the base assumption that 15.24% of potential energy is unpaid, a stress setting rather than a contract term ($80.4/MWh if that share doubles)."
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### EB-03: The credit result in the summary lacks its rate, timing and "not after-tax" qualifiers (P2)

- **Location:** PDF p.4; MD §1.1, line 35.
- **Quote:** "Its present value is **$35.38m**, leaving reference-node NPV at **−$50.59m**."
- **Problem:** The paragraph says eligibility is unproven and the six scenarios are unchanged, which is good. However, it omits three conditions that §10.8 states:
  - a 30% rate (the 6% rate gives $7.08m);
  - cash at end-2027, discounted at 4.27%;
  - the −$50.59m is a pre-tax NPV plus a credit, not an after-tax NPV. It omits the §50(c)(3) basis reduction, depreciation and income tax (lines 840, 842).
- **Evidence:** MD lines 822, 840, 842; `scenario-versions/data/Credit-Base-Scenarios.csv` (row A1_OCC_only, pwa_not_met_6pct: 7.08).
- **Client consequence:** An investor reading only the summary may take −$50.59m as the "with-ITC" project value, and as the high case rather than the 30%-rate case.
- **Minimal fix:** Rewrite as: "Assuming a 30% rate, eligibility and cash at end-2027, its present value at 4.27% is $35.38m ($7.08m at the 6% base rate). Adding it to the pre-tax NPV gives −$50.59m; this is not an after-tax valuation."
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### EB-04: IRR labels in Table 10-2 could be more informative and consistent with Appendix B.2 (P2)

- **Location:** PDF p.41 (Table 10-2), p.42 (§10.6), p.68 (B.2); MD lines 749–754, 778, 1319.
- **Quote:** "Not a single rate: multiple roots" / "Single rate not certified".
- **Problem:** The treatment is correct under brief §4(4). Two wording issues remain:
  - **Fixed downside.** "Single rate not certified" suggests a rate exists but is uncertified. B.2 says no numerical root was found, and the search is not certified complete (`irr_status = no_numerical_root_completeness_not_certified`).
  - **"Multiple roots" can be over-read.** A reader may infer that an attractive return is hidden behind root ambiguity. In fact:
    - Node base, Node downside and Fixed base have only negative real roots.
    - Fixed upside's only non-negative root is +1.41% real.
    - All six scenarios have negative NPV at every tested rate of 4.27% or more.
- **Evidence:** `data/scenario_metrics.csv` (`irr_status`, `irr_roots`); MD line 1319.
- **Client consequence:** Minor misreading risk. No numbers are wrong.
- **Minimal fix:**
  - Change the Fixed downside cell to "No root found (search not certified complete)".
  - Add to the table note: "Where multiple roots exist, all are below 0% real except Fixed upside (−86.5% and +1.4%); no scenario has a root at or above the 4.27% convention. NPV is the decision measure."
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### EB-05: Hub-hedge figures are not fully traceable to the scenario notes, and the 43% tail share lacks its case label (P2)

- **Location:** PDF p.40; MD §10.3, line 722.
- **Quote:** "ranges from **$60.6/MWh** to **$84.8/MWh** across the eight … combinations. With a 10-year tenor and a $40/MWh strike, the merchant tail supplies about 43%".
- **Problem:**
  - **Range.** The $84.8 upper bound (10-year, stop-if-node-negative, suspend-if-hub-negative: 84.77) and the 15-year stop/suspend value (74.41) appear only in `VPPA-Breakeven-Strikes.csv`. They are absent from the six-row results table in `Scenario-Notes-EN.md` §2, the document Appendix A.2 points readers to, whose maximum is 81.6. The report is correct, but a reader checking it against the notes will see a mismatch.
  - **Tail share.** The 43% applies to the stop / settle-through case only (50.43 / (67.72 + 50.43) = 42.7%; claims register N21). Under run / settle-through it is 38.7% (50.43 / 130.42, reviewer arithmetic from `VPPA-Route-Scenarios.csv`).
- **Evidence:** `scenario-versions/data/VPPA-Breakeven-Strikes.csv`; `scenario-versions/data/VPPA-Route-Scenarios.csv`; `closure-evidence/Numbers-and-Claims.csv` N19–N21.
- **Client consequence:** It may cast doubt on traceability, and slightly overstates precision on tail dependence.
- **Minimal fix:**
  - Change the sentence to "…with a 10-year tenor, a $40/MWh strike, stop-if-node-negative dispatch and settle-through, the merchant tail supplies about 43% (39%–43% across dispatch and clause settings)…".
  - Add "(all eight combinations are in `VPPA-Breakeven-Strikes.csv`; the scenario-notes table shows six)".
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### EB-06: Table 10-6 calls the exclusion of construction financing "Correct" (P2)

- **Location:** PDF p.45; MD Table 10-6, line 815.
- **Quote:** "Construction financing | Excluded | Excluded | — | Excluded | Correct for unlevered overnight cost".
- **Problem:** Excluding interest during construction is consistent with an unlevered overnight-cost convention. However, because CAPEX is placed at end-2026, which is also the valuation point, the time value of spending during construction is also absent. The register itself cautions "discounting alone is not a double-count proof" (`scenario_input_register.csv`, row `construction`). "Correct" overstates the point; it is a stated convention.
- **Evidence:** MD line 688; `data/scenario_input_register.csv`, row `construction`.
- **Client consequence:** It implies a complete capital-cost treatment. Reviewer arithmetic for scale only: an average half-year of spending at 4.27% is about 2% of CAPEX, roughly $3m. This is not a new result.
- **Minimal fix:** Replace the Status cell with "Excluded by convention; capital timing within the construction year not modelled".
- **Changes an existing number?** N. **Confidence:** Medium. **In scope?** Y.

### EB-07: The cost year and dollar year of the ATB FOM figures quoted in §10.7 are unstated (P2)

- **Location:** PDF p.44; MD §10.7, line 798 (compare line 696 and Table 10-1).
- **Quote:** "2024 fixed O&M of $24.66/kWac-yr splits into system ($10.88), property ($11.41) and administration ($2.38)".
- **Problem:** The scenario's FOM is $24.49/kWac-yr in 2025 dollars. That is the ATB **2026 cost-year** value of $23.18 in 2023 dollars × 1.0566 (`scenario_input_register.csv`, `fom_2023usd`). The $24.66 quoted next to it is a **2024 cost-year** figure with no stated dollar year. Placed side by side, readers may think the scenario FOM is about $0.17 below ATB, or that the two share a basis.
- **Dollar-year check:** could not verify the dollar year of $24.66 from the retained claim row (N43).
- **Evidence:** `data/scenario_input_register.csv`; `closure-evidence/Numbers-and-Claims.csv` N43.
- **Client consequence:** Small risk of mis-benchmarking the FOM.
- **Minimal fix:** Add: "(ATB 2024 cost year, ATB dollar basis; the scenario instead uses the ATB 2026 cost-year FOM of $23.18 in 2023 dollars, which is $24.49 in 2025 dollars)."
- **Changes an existing number?** N. **Confidence:** Medium. **In scope?** Y.

### EB-08: The credit-eligibility status in the linked scenario files is framed more narrowly than Table 10-3 (P2)

- **Location:** PDF p.46; MD Table 10-3, lines 826–834, and Appendix A.2, line 1285. The linked notes are `scenario-versions/Scenario-Notes-EN.md` §1 and `Credit-Base-Scenarios.csv` (column `status`).
- **Quote (notes):** "placed in service by 2027-12-31, because the early-construction window has closed".
- **Quote (report, line 834):** "The early-start branch remains available for evaluation if supported by qualifying contemporaneous records."
- **Problem:** The two statements are compatible only if the notes are read as applying to a project with no construction start by 4 July 2026. The report does not say this. A reader following the A.2 link would find that the supporting file treats the early-start branch as closed, while the report keeps it open.
- **Evidence:** as cited; claims register N02.
- **Client consequence:** Inconsistent tax-timing message between the report and its own evidence file.
- **Minimal fix:** Add one sentence to A.2 or after Table 10-3: "The status field in the credit scenario file assumes a project that had not begun construction by 4 July 2026; projects with qualifying earlier start evidence fall under the first branch of Table 10-3." The frozen file does not need to change.
- **Changes an existing number?** N. **Confidence:** Medium. **In scope?** Y.

### EB-09: Figure 10-2 panels are not labelled (P2)

- **Location:** PDF p.42; MD §10.5, line 764.
- **Quote:** "Figure 10-2. Annual real cash flows".
- **Problem:**
  - The two panels carry no titles saying which is Node base and which is Fixed base. The reader can infer it only from the bar shape (the declining revenue is the flat nominal contract).
  - The left panel's right-hand cumulative axis has unlabelled tick marks.
- **Evidence:** `figures/S4_annual_cash_flows.png`; PDF p.42.
- **Client consequence:** A first-time reader cannot tell which route fails by how much (the end-points are −$45.8m and about −$38m).
- **Minimal fix:** Add panel titles "Node base (constant-real price profile)" and "Fixed base ($40/MWh flat nominal)", or name the panels left to right in the caption.
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### EB-10: Contract and cost passages in §10.3 and §10.7 repeat themselves (P2)

- **Location:** PDF pp.39–40 and 43–45; MD lines 710 / 714, 718 / 724 / 726, and 794 / 800.
- **Quote:** "interval receipts would be **node energy receipts + contracted quantity × (strike price − hub price)**" (line 710), restated at line 714.
- **Problem:** Three passages repeat content within a page or two:
  - the two-leg hedge identity (lines 710 and 714);
  - the J. Aron hedge and the A– purchaser (lines 718, 724 and 726);
  - the 16 TAC §25.195(f) allocation (lines 794 and 800).

  This lengthens the core finance chapter without adding content.
- **Client consequence:** Reading burden, and a risk of skimming over the two-leg distinction.
- **Minimal fix:**
  - Delete line 710's formula sentence and keep line 714.
  - Merge line 718 into line 726.
  - In line 800, replace the repeated §25.195 sentences with "(see the connection-cost allocation above)".
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### EB-11: Disclosed limitations (no change needed, not to be upgraded)

These are clearly disclosed, within the brief §4 boundary, and must not become new research tasks:

| Topic | Where disclosed | Notes |
|---|---|---|
| (a) No definition-matched comparable IRR or cash flows for the nine named plants; no market return range | lines 35, 870–872; Table C-1 FIN-01 | Correctly not converted into a "typical IRR". |
| (b) Energy-contract strike, tenor, hub, volume rule, negative-price clause and credit support undisclosed; hub-hedge version is hypothetical, with the tail unsourced | lines 718–726; FIN-03 | — |
| (c) Comptroller qualified investment ($0.92–$1.10/Wac) is mid-2023 nominal, narrow in scope, not all-in cost and not a replacement for the $1.437/Wac input | line 786; Figure 10-3 note | Matches `Qualified-Investment-Comparisons.csv`. |
| (d) Possible overlap of the replacement reserve and network upgrades with ATB/PVSCM benchmark lines is unquantifiable without the ATB component table | lines 698, 792, 800; FIN-05 | The zero-reserve variant (+$1.79m) is a sensitivity only. |
| (e) Gross energy value versus net receipts: QSE fees, imbalance, losses to meter and REC price | lines 1385–1392; FIN-11 | Not zero-cost. |
| (f) Credit eligibility, PWA, MACR, transfer price, after-tax layer and §50(c)(3) | lines 836–842; FIN-04 | — |
| (g) Financing terms: coupon, tenor, DSCR, tax-equity terms | lines 1381–1383; FIN-10 | No levered valuation is required in this round. |
| (h) Historical nominal price levels reused as real 2025 dollars | lines 858, 874–881 | Resolved by a separately versioned CPI restatement that changes no sign or positive share; the full-calendar versus common-calendar difference in the CPI file is labelled. |

**Severity:** Disclosed limitation. **Changes an existing number?** N. **In scope?** Y.

### EB-12: Optional future scope (not part of the required edits)

Possible future extensions, outside this edition:
- an after-tax layer (MACRS, basis reduction, tax-equity or transfer economics);
- an explicit construction-period draw schedule;
- a dated forward curve for any merchant tail;
- a levered case.

None is needed for the stated market-screening use.

---

## 3. Summary of findings

| ID | Severity | PDF page | MD line | Problem (one line) | Minimal fix |
|---|---|---|---|---|---|
| EB-01 | P1 | 41 (also 4, 42) | 747–754, 774, 44 | Fixed-route "delivered GWh" and LCOE are on a paid-energy basis but labelled delivered; the fixed and node downside LCOE gap comes only from the denominator | Relabel the column; add a note explaining the paid-energy denominator |
| EB-02 | P2 | 3 | 29 | Base 15.24% unpaid share called "severe" | Call it the "base stress assumption"; cite $80.4 at the doubled share |
| EB-03 | P2 | 4 | 35 | Summary credit result lacks the 30% rate, end-2027 timing and "not after-tax" | Add the qualifiers and the $7.08m figure at the 6% rate |
| EB-04 | P2 | 41–42, 68 | 749–754, 778, 1319 | "Single rate not certified" is inconsistent with B.2; "multiple roots" can be over-read | Use "No root found…"; note that all roots are below 4.27% |
| EB-05 | P2 | 40 | 722 | $84.8 is absent from the scenario-notes table; the 43% tail share is case-specific | Name the case; give the 39–43% range; point to the CSV |
| EB-06 | P2 | 45 | 815 | Construction financing exclusion called "Correct" | Call it "Excluded by convention; timing within the construction year not modelled" |
| EB-07 | P2 | 44 | 798 | ATB FOM $24.66 has no cost-year or dollar-year label next to the scenario's $24.49 | Add the cost-year and dollar-year note |
| EB-08 | P2 | 46 | 826–834, 1285 | Linked credit notes say the early-start window has closed; Table 10-3 keeps it open | Add one bridging sentence |
| EB-09 | P2 | 42 | 764 | Figure 10-2 panels have no titles | Add Node base / Fixed base titles |
| EB-10 | P2 | 39–40, 43–45 | 710/714, 718/724/726, 794/800 | Repeated passages in §10.3 and §10.7 | Delete the duplicates |
| EB-11 | Disclosed limitation | various | various | IRR comparables, contracts, qualified investment, overlaps, net receipts, tax, financing, CPI | No change |
| EB-12 | Optional future scope | — | — | After-tax layer, levered case, forward tail | Not required |

**P0 findings: none.** All headline financial numbers I checked reproduce from the frozen files. Real and nominal treatments, the discount convention, the IRR policy, the cost-scope boundaries and the separation of the tax-credit, VPPA and CPI versions from the six baseline scenarios are all handled within the brief §4 boundary.

## 4. Overall verdict

**② Handover-ready after the listed minimal edits** for the stated market-screening use.

The single P1 (EB-01, a denominator label on LCOE and GWh for the fixed-price route) and the P2 items are wording, label or traceability edits using existing materials. None changes a number. This verdict is not a publication authorisation and not acceptance of the original Version 1.0.

## 5. Items I could not verify

- The dollar year of the ATB 2024 FOM figure of $24.66/kWac-yr (EB-07).
- Whether ATB FOM explicitly includes "component-failure allowances" (stated at lines 698 and 1321). I did not open the ATB source; the statement is accepted as written.
- Legal accuracy of the P.L. 119-21 timing branches and the court-docket status. This is outside my finance remit and left to Expert D.
