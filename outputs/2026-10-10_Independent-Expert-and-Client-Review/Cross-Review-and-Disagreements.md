# Cross-Review and Disagreements

The full round-2 texts are in `round2/`. This file records what was asked and answered, where the reviewers converged, and which disputes remain open. Disputes are kept as they stand; no majority vote replaces evidence. Where the coordinator settled a point, it was by checking evidence, and the check is stated.

## How the interaction round ran

After all six first-round reviews were submitted independently, each reviewer was resumed with its own first-round context and given the other files to read. The pairings followed the brief:

- **Finance and methods:** Expert B examined Expert C's findings, and C examined B's.
- **Markets and industry:** Expert A examined Expert D's findings, and D examined A's. The question was how the three layers connect: manufacturing, then U.S. cost and trade, then ERCOT value.
- **Clients:** Clients E and F read all four expert reviews and challenged them from a reader's position. Each expert also answered the client items in its own field.

## Main exchanges and outcomes

### Finance and methods (B and C)

**C-03: settlement points, not distinct sites**

- **B's check:** B recounted from the frozen node file. The 485 settlement points carry 400 distinct three-year receipt series, and the 13 positive 2024 points carry 10.
- **Effect on conclusions:** None. Recounting on distinct series (reviewer arithmetic only) moves the positive shares to 2.5% in 2024 and 0.5% in 2025. Medians move by at most $1.6m, and nothing changes sign.
- **Severity:**
  - B rated it P1.
  - C, its author, lowered it to P2.
  - Clients E and F also rated it P2.
  - **Outcome: P2.** The originator and both clients agree.
- **Coordinator check:** The recount (485 → 400; 13 → 10) is confirmed. The two positive 2025 points are NF_BRP_RN and the storage node RHESS2_ESS1.

**C-05: calendar basis.** B confirmed it. The tail and resampling files use the full 2024 calendar (−91.84 and −81.33), while the matrix uses the common calendar (−92.15 and −81.59). **Outcome: P2 caption note.**

**EB-01: fixed-route LCOE on paid energy**

- C confirmed it from `scenario_metrics.csv`. Both downside cases have 280.7 GWh of potential output and the same potential-energy LCOE of $46.39; the $54.8 versus $66.7 gap comes only from the denominator.
- C added one point: Fixed base equals Node base only because the 15.24% unpaid share was set equal to the node's negative-price energy share.
- **Outcome: P1 consensus**, with C's addition to the note. This also resolves F-07.

**EB-04: IRR wording.** C corrected B's proposed wording. An uncertified root search cannot support "no root ≥4.27%"; the correct phrasing is "no root at or above 4.27% was found; NPV is negative at all three tested rates". **Outcome: P2**, using C's wording.

**EB-05: tail share.** Across the four dispatch and clause settings the tail share is 38.7%–43.6%, not B's "39–43%". **Outcome: P2.** The summary item now carries only the strike range.

**EB-03 and F-02: −$50.59m is not an after-tax NPV**

- B raised EB-03 from P2 to P1 and merged it with F-02.
- Clients E and F objected to putting the $7.08m (6% base-rate) variant into the summary, and B accepted this.
- **Outcome: P1.** The $7.08m figure stays in §10.8.

**F-03: simulated output not calibrated**

- B and C both noted that the 33.4% potential capacity factor is the wrong comparator for observed net generation. The fair comparison is the delivered 28.29%, which sits inside the 25.5–29.7% range of the recent plants.
- F lowered its own finding to P2.
- **Outcome: P2.** A half-sentence goes in the limits box.

### Markets and industry (A and D)

**D-01: the module benchmark is net of the 45X subsidy**

- A re-derived the figures: module items sum to $291.21/kWdc, or $360.09/kWdc without the −$68.88 subsidy line.
- No market-side conclusion changes. As an illustration only, computing the saving gross of the subsidy would make a 10% module cut worth about $4.4m instead of $3.76m. That is still far below the revenue effects.
- Client E warned against writing a derived "the gap to the MIP is only $0.02" conclusion, because readers could take it to mean imports at the MIP cost about the same as U.S. production.
- **Outcome: P1 label fix (consensus).** No "$0.02" conclusion is stated.

**A-04: foreclosure timing**

- D found that the retained Comptroller form (C06) confirms the foreclosure but gives no date. The October 2022 assignment date rests on C09, which is not in the client package.
- A lowered its finding to P2.
- **Outcome: P2.** A sentence without a date is added.

**A-01, A-03 and A-05.** D agreed with all three and found no conflict with the trade or tax framing. D also suggested labelling both break-even rows "pre-tax, no credit", because a $53.51/MWh credit-illustrated break-even exists. **Outcome: adopted in R-02.**

**E-03: what the material-assistance ratio measures.** D corrected the client's framing. The material-assistance cost ratio measures cost not attributable to a prohibited foreign entity, defined by ownership and control, not by China origin. **Outcome: R-07 wording.**

**E-05: China-origin treatment.** D judged "MIP plus 15%" supportable on the face of the proclamation text, but too strong if worded as "therefore", given the onshoring relief and the Commerce Secretary's power to adjust. D also noted that the country arrangements cover only the 15% duty, not the MIP. **Outcome: P2 softened wording.**

### Clients challenging the experts (E and F)

**Overall position.** Both clients support moving existing qualifiers to the places where readers make decisions. Both oppose adding more numbers or method notes to Chapter 1. **Outcome:** each new number appears in Chapter 1 once; the A-03 and C-03 figures and the $80.4 figure stay in the body.

**A-01 and F-01: hub-hedge break-even in the summary.** Merged into one sentence in item 2, plus one Table 1-1 row. B preferred adding no row and rated the item P2; A, E and F rated it P1. **Outcome: P1 with one labelled row** ("separate version; tail-dependent").

**New items from the clients**

| Item | Issue | Status |
|---|---|---|
| R2-E-1 | Proclamation clause (3): inaccurate importer certification leads to a permanent import ban | **P1.** Coordinator verified the clause text and its absence from the report |
| R2-E-2 | The Commerce Secretary may adjust the MIP (clause 1(b)) | P2. Verified |
| R2-E-3 | The 26.1% module share is of the PV-only benchmark; about 22.9% of total CAPEX | P2. Arithmetic checked |
| G-1 | Real LCOE and nominal break-even sit side by side in Table 1-1 | P2 |
| G-2 | The WLPUN capacity mix needs its qualifiers | P2 |
| G-3 | Table 10-3 has no note for construction starting after 4 July 2026 | P2 |

## Disputes that remain open

| # | Topic | Positions | Coordinator handling |
|---|---|---|---|
| 1 | Severity of E-01 / D-11, dated trade facts in the summary | E and D: P1. A: P2 for the stated use | Listed as P1 (two of three, and directly relevant to the manufacturer reader). The author may treat it as P2 |
| 2 | Export-VAT rebate in the summary sentence | D: include, with a retained-filing locator. A and E: exclude, because the cited MOF page was never retrieved | **Settled by evidence.** The coordinator found the claim in the LONGi FY2025 annual report, p.297, a post-balance-sheet note citing MOF/STA announcement 2026 No. 2, effective 1 April 2026. That removes the stated reason to exclude. Included in R-05 with that locator; the author may still drop it for length |
| 3 | Placement of the "not generally uneconomic" sentence | E: the bold lead paragraph of §1.1. B and F: the limits box | Recommended in the bold lead paragraph (one sentence; the limits box is small grey text). Severity P1: E, C and B; F P2 |
| 4 | Whether Table 1-1 gets a hedge row | B: no row. A, E and F: one row | One labelled row |
| 5 | Severity of C-03 | B: P1. C, E and F: P2 | P2 |
| 6 | Severity of C-02 / A-07 / F-08, the 2026 diagnostic sentence | C: P1, because the source is mislabelled. A and F: P2 | P1, because an evidence-label error falls under P1 in the brief |

## Unanimous points

- **No P0.** All six reviewers chose verdict ② in both rounds: handover-ready after the listed minimal edits.
- **No existing number changes.** No new research, model run or data is needed.
- **Boundaries held.** The 485/641/757 samples, the calendar bases, the node/hub/hedge mechanisms, the six frozen scenarios kept separate from the credit, VPPA and CPI versions, and gross versus net receipts are all correctly bounded in the body text. The problems found concern placement of qualifiers and labels in the summary and decision tables.
- **Disclosed limitations stay disclosed limitations.**
