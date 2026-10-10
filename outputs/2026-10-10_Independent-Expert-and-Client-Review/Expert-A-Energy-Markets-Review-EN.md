# Expert A — Energy Economics and Power Markets (ERCOT): Independent First-Round Review

**Object reviewed:** SOLAR-001, *From China's Solar Supply Chain to U.S. Power Markets*, closure-integrated candidate edition, 9 October 2026 (73-page PDF and Markdown).
**Reviewer role:** Expert A, energy economics and ERCOT power markets. This is an independent first round: I did not open any other reviewer's output.
**Standard applied:** The review brief's §4 (scope of use) and §6 (severity and verdict rules). I did not rerun any models and did not use the web. Every number I recomputed is labelled "reviewer arithmetic".

---

## 1. Scope and spot checks

I concentrated on the material that a developer, power buyer or market-entry reader would use to make a commercial decision:

- Chapter 1: the headline figures.
- Chapters 7–8: node versus hub prices, capture prices and the negative-price rule.
- Section 10.3: the revenue mechanisms (node sale, simplified fixed price, hub-settled hedge).
- Sections 11.3 and 11.8: break-evens, RTC+B timing and the 2026 update.
- Chapter 13: the commercial decision matrix.
- Appendices B.2 and C: contract risk allocation, gross versus net receipts, and price finality.

**Numbers I checked against the frozen tables (all matched unless a finding says otherwise):**

| Report claim | Frozen source | Result |
|---|---|---|
| 35,038 of 35,040 intervals; time-weighted price $46.37; potential-output-weighted price $22.13; 2,189 negative intervals (6.2%); 15.24% of energy in negative intervals; 247.8 GWh delivered; delivered-weighted price $26.43; receipts $6.551m | `data/interval_energy_price_2025.csv` (reviewer arithmetic) | Reproduced: 35,038; 46.370; 22.132; 2,189 (6.25%); 15.24%; 247,819.5 MWh; 26.434; $6.551m |
| Average price over negative-price energy ≈ −$1.79/MWh; stop-rule value about $80k | `data/panel/Node-Hub-Comparisons.csv` (rule_effect 79,934 / 44,564 MWh) | Matches |
| Table 8-1 values for node, West hub and Bus Average hub; node-minus-West basis −0.05 / +0.25 / +0.67; West hub capture ratios 1.30 / 0.75 / 0.65 | `data/panel/Node-Hub-Comparisons.csv` | Matches |
| Hub-hedge break-even strike $60.6–$84.8 (4.27%); about $68–$107 at 6% and 8%; tail ≈ 43% of revenue present value (10-year tenor, $40 strike) | `scenario-versions/data/VPPA-Breakeven-Strikes.csv`; `VPPA-Route-Scenarios.csv`; `Scenario-Notes-EN.md` l.96 | Matches (60.57–84.77; 68.38–107.12; 50.4 / 118.1 = 42.7%) |
| 2026 diagnostic: $18.24 vs $21.36; negative intervals 14.1% vs 7.7% | `scenario-versions/data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv` | Matches. These are **West hub** figures. |
| 2026 coverage: 281 days, 270 complete, 125 missing intervals, 423 hub differences up to $4.01, 485 + 7 points | `closure-evidence/tables/FIN-08_2026-Price-Coverage-Summary.csv` | Matches |
| RTC+B launch on 5 Dec 2025; ORDC active 57 hours; storage above 17 GW | `closure-evidence/sources/other/IMM_2025_State-of-the-Market_ERCOT.txt` l.1312–1315, 1611, 8000 | Matches |
| 485 / 13 / 2 positive nodes; 54.7%; 482 nodes negative | Table 10-4 shares (reviewer arithmetic: 2.68% × 485 = 13; 0.41% × 485 = 2; 99.4% × 485 = 482) | Consistent |

**What I could not check:** "HB_BUSAVG … introduced under NPRR817" (l.545). The cited market notice [P09] is not in the package, and I did not use the web. I raise no finding on it.

**Overall impression:** The market chapters handle the main distinctions with care:

- the node is a price reference, not a settlement right;
- the TAYGETE2_ALL ↔ EIA 64075 link is an attribute match, not a crosswalk;
- potential-output weighting versus delivered-output weighting;
- the two legs of a hub-settled contract and the basis it leaves with the seller;
- gross energy value versus net receipts;
- 2025 straddles RTC+B;
- the fixed-2025-profile weighting of 2026 prices is a diagnostic, not a capture price.

I found **no P0**. The remaining risks are about **where** the qualifiers appear. The most-read places (Chapter 1, Table 1-1, Section 13.2 and Table 13-1) carry some figures with fewer qualifiers than Chapters 8, 10 and 11. That gap could lead a reader to the wrong commercial comparison.

---

## 2. Findings

### A-01 — P1 — The $66/MWh headline break-even is shown without its tenor, settlement point and volume rule, and the hub-hedge break-even is missing from the summary and decision sections

- **Location:**
  - PDF p.3, MD §1.1 l.29: "A flat nominal contract breaks even near $66/MWh with the severe assumed 15.24% unpaid-energy deduction".
  - PDF p.4, Table 1-1 l.47: "Flat nominal break-even contract price | $66.0/MWh | Fixed-price route".
  - PDF p.60, §13.2 l.1124: "the fixed route needs about $66/MWh flat nominal".
  - PDF p.61, Table 13-1 l.1152: "About $66/MWh flat nominal, or $577/kWac on the nodal route".
- **Problem:** $66/MWh is the break-even for a specific contract:
  - a **30-year** flat nominal price;
  - paid at the **node**, with no hub leg;
  - with **15.24% of potential energy unpaid**.

  Section 10.3 (l.706) says this clearly. The headline, Section 13.2 and the decision matrix say only "flat nominal contract". Market solar offers in ERCOT are usually hub-settled and have 10–15-year tenors. The report already contains the like-for-like result: a $60.6–$84.8/MWh break-even strike across eight tenor, dispatch and clause combinations, with the merchant tail supplying about 43% of revenue present value (l.722). That result appears in none of the summary or decision places.
- **Evidence:**
  - MD l.706: "holds $40/MWh constant in nominal terms for the full 30-year life".
  - MD l.720–722.
  - `scenario-versions/data/VPPA-Breakeven-Strikes.csv`: 2025 path, 4.27%, min 60.57 and max 84.77.
  - `Scenario-Notes-EN.md` l.96–99.
- **Client consequence:** A developer or buyer could compare "$66" with a 10–15-year hub-settled offer and decide the gap is about $X/MWh. That is the wrong comparison:
  - The tenor differs (30 years versus 10–15 years plus a merchant tail).
  - The settlement point differs (node versus hub plus basis).
  - The paid-volume rule differs.

  The hub-hedge break-evens are higher than $66 in most combinations, because of the weak repeated-2025 merchant tail.
- **Minimal fix:** Qualify every summary appearance and add one line pointing to the hub-hedge result.
  - **l.29:** "A **30-year, node-delivered** flat nominal contract breaks even near $66/MWh with the assumed 15.24% unpaid-energy deduction; paying for all potential generation lowers the threshold to $55.9/MWh. A separately versioned **10–15-year HB_WEST-settled hedge** with a merchant tail at the node breaks even at $60.6–$84.8/MWh on the 2025 price path, depending mainly on the unsourced tail. Neither is an observed contract offer."
  - **Table 1-1, label:** "Flat nominal break-even price, 30-yr node-level fixed-price route (15.24% unpaid)".
  - **Table 1-1, new row:** "Hub-settled hedge break-even strike, 10/15-yr + node tail | $60.6–$84.8/MWh | Separately versioned; 10.3".
  - **§13.2 and Table 13-1:** add "(30-year node-level route; see 10.3 for the 10–15-year hub-hedge range)".
- **Changes an existing number?** N (it only adds existing figures) · **Confidence:** High · **In scope:** Y

### A-02 — P1 — "Realized sales price" and "earns" label a modelled gross energy value

- **Location:**
  - PDF p.4, Table 1-1 l.45: "Realized sales price | $26.4/MWh | Reference node, stop exports below zero".
  - PDF p.3, §1.1 l.28: "The hypothetical 2025 reference system earns $26.4/MWh on delivered electricity".
- **Problem:** $26.4/MWh is a modelled gross energy value: simulated output × the 15-minute real-time price at a reference node, with no documented settlement relationship. It does not deduct:
  - losses to the meter;
  - QSE fees;
  - imbalance or uplift;
  - REC effects;
  - hedges.

  The report itself makes this point in §7.1 l.486 and Appendix C l.1385–1392. Brief §4 requires gross energy value to be kept separate from net receipts. "Realized" and "earns" are the two words most likely to blur that difference, and they sit in the most-read table.
- **Evidence:**
  - MD l.486: "The modeled nodal revenue is gross energy value under the specified reference-price rule".
  - Table C-1 l.1377: "Net receipts (FIN-11) … Gross energy value only".
  - `finance-supplement/Settlement-and-Net-Receipts.csv`, step 10: "cannot be completed".
- **Client consequence:** A reader could treat $26.4 as achievable cash per MWh and compare it directly with net PPA prices or with LCOE as if it were net revenue.
- **Minimal fix:**
  - **Table 1-1:** "Modelled gross energy value per delivered MWh | $26.4/MWh | Reference-node price, stop exports below zero, before fees/losses/imbalance; 8.2".
  - **l.28:** "…is assigned a modelled gross energy value of $26.4/MWh on delivered electricity…"
  - **Optional, l.776:** "first-year real contract price" in place of "first-year realized price".
- **Changes an existing number?** N · **Confidence:** High · **In scope:** Y

### A-03 — P1 — The 2025 base regime is almost entirely before RTC+B, but this and the 2026 diagnostic appear only in §11.8

- **Location:**
  - PDF p.4, §1.3 l.58–62.
  - PDF p.39, §10.3 l.704: "The nodal route uses the 2025 reference-price and output shapes, holds the base price profile constant in real terms".
  - Contrast with PDF p.55, §11.8 l.998 and l.1006.
- **Problem:** The base case repeats the 2025 node price shape for 30 years. Reviewer arithmetic on `data/interval_energy_price_2025.csv`: the post-launch period (5–31 Dec 2025) covers only **7.4% of 2025 intervals, 5.1% of potential output and 4.3% of modelled receipts**. The base case is therefore, in substance, a pre-RTC+B price shape.

  The report states correctly that "2025 straddles" the launch, and it gives a properly labelled diagnostic for Jan–Sep 2026 (fixed 2025 profile). But both appear only on p.55. Chapter 1, §8.1–8.2 and §10.3 present "2025" as the reference without this context.

  The diagnostic is directionally relevant to screening, though not to valuation:
  - West hub profile-weighted price: $18.24 versus $21.36 (−14.6%, reviewer arithmetic).
  - Share of profile energy in negative West-hub intervals: **23.6% versus 13.7%**.
- **Evidence:**
  - `scenario-versions/data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv`, Jan–Sep rows: profile_energy_share_negative 0.2361 versus 0.1367.
  - IMM source l.1312 ("before RTC went live on December 5, 2025").
- **Client consequence:** A reader of Chapters 1, 8 or 10 could assume the 2025 repetition reflects the latest market design. In fact it is mostly pre-launch. The only post-launch price evidence in the report points to lower solar-weighted hub prices and much more negative-price energy. That matters for the stop rule and for the paid-volume stress.
- **Minimal fix:** Add one sentence at the end of §1.3 l.62 and after §10.3 l.704. It must not be presented as a forecast:

  > "About 93% of 2025 intervals predate ERCOT's 5 December 2025 real-time co-optimisation launch. A Jan–Sep 2026 West-hub diagnostic using the fixed 2025 output profile is lower ($18.24 vs $21.36/MWh) with more negative-price energy (23.6% vs 13.7%); it is a price diagnostic, not a 2026 capture price or forecast (Section 11.8)."
- **Changes an existing number?** N (the figures already exist in frozen tables; the energy share is not yet in the text) · **Confidence:** High · **In scope:** Y. This keeps the brief's boundary: no 2026 capture price or return.

### A-04 — P1 — The foreclosure at the matched plant carries no timing context and could be read as evidence about 2024–2025 merchant prices

- **Location:**
  - PDF p.29, §8.1 l.533: "The current owner's 2025 filing reports a senior-lender-initiated foreclosure purchase after the previous owner failed to repay its loan."
  - Repeated at PDF p.71, Appendix C l.1381.
- **Problem:** The sentence sits right next to the 2025 node prices in Chapter 8. The package's own entity-mapping record shows:
  - the Comptroller received the assignment of agreement #1377 to the current owner on **6 October 2022**;
  - Taygete II first entered service in **July 2023**;
  - the auction date is undisclosed.

  The ownership change therefore appears to have happened during development or construction, not after a period of operating at TAYGETE2_ALL prices. The report rightly says the event supplies "neither an IRR nor the cause". It omits this timing context, which matters more to a market reader.
- **Evidence:**
  - `finance-supplement/Entity-Node-Mapping.csv` L09 ("Date of auction lender identity and price not disclosed") and L10 ("On October 6, 2022, the Comptroller received an amendment … to assign the project to West Texas Solar Project II LLC").
  - L05 (COD 2023-07).
  - **Could not verify** against the original C06/C09 PDFs, which are not in this package. That the assignment and the foreclosure are the same event is likely but not proven, hence Medium confidence.
- **Client consequence:** A reader could take the foreclosure as corroborating the weak 2024–2025 merchant economics at the reference node. That would be a causal and timing inference the evidence does not support.
- **Minimal fix (append to l.533):** "The retained Comptroller record shows the agreement was assigned to the current owner in October 2022, before the July 2023 in-service date; the auction date is not disclosed. The event should not be read as evidence about post-2023 prices at this node."
- **Changes an existing number?** N · **Confidence:** Med · **In scope:** Y

### A-05 — P1 — The decision matrix offers the reference node's 48% capture ratio as the evidence for challenging average-price claims, without saying it is near the bottom of the distribution

- **Location:** PDF p.61, Table 13-1 l.1149: "Challenge a claim based on average power prices … 2025 reference capture ratio about 48%, before export response". The same pairing ($46.37 versus $22.13) appears at PDF p.3, l.32.
- **Problem:** The node's low ratio partly reflects its own high non-solar-hour price level, not only the solar timing discount:
  - node time-weighted price is $46.37, versus $32.92 at HB_WEST;
  - yet the output-weighted prices are almost identical ($22.13 versus $21.46);
  - the West hub ratio is 0.65.

  The report states that the ratio is near the **3rd percentile** (l.60, l.583). The decision-matrix row, which is the one a reader would lift as a rule of thumb, does not.
- **Evidence:**
  - `data/panel/Node-Hub-Comparisons.csv`, 2025 rows: mean_price 46.37 (node) and 32.92 (HB_WEST); capture_ratio 0.477 and 0.652.
  - MD l.716 (West hub ratio 0.65); l.583.
- **Client consequence:** A buyer or developer applying "about 48%" to a hub or zone average-price forward would understate solar value by about a quarter compared with the West-hub ratio (reviewer arithmetic: 0.48 / 0.65 ≈ 0.73). They would draw the wrong screening conclusion.
- **Minimal fix (Table 13-1 cell):** "2025 reference-node capture ratio about 48% (near the 3rd percentile of the 2025 cross-section); West hub about 65%. Ratios are location-specific; before export response."
- **Changes an existing number?** N · **Confidence:** High · **In scope:** Y

### A-06 — P2 — Node-versus-hub wording frames the hub as an alternative price rather than as a basis exposure

- **Location:**
  - PDF p.29, §8.1 l.545: "The West hub does not improve this particular 2025 weighted-price comparison."
  - PDF p.3, l.32: "switching benchmarks is not automatically an improvement".
- **Problem:** A generator at this location cannot "switch" to being paid the hub price. Under a hub-settled hedge with H = G, the seller keeps G × (K + node − hub), as §10.3 l.714 says correctly. The useful reading of Table 8-1 is therefore the output-weighted basis: +$0.67/MWh in 2025, mildly favourable to a hub-hedged seller on an annual basis. The current framing invites the reader to compare $22.13 with $21.46 as alternative revenues.
- **Evidence:** MD l.714–716; `data/panel/Node-Hub-Comparisons.csv`, generation_weighted_node_minus_west_basis.
- **Client consequence:** Low. A reader may misread a hub contract as "worse" than the node.
- **Minimal fix (l.545):** "Measured as output-weighted basis, the reference node was $0.67/MWh above the West hub in 2025 (−$0.05 and +$0.25 in 2023–2024). Under a hub-settled hedge this basis stays with the seller; small annual basis does not establish small interval basis (10.3)."
- **Changes an existing number?** N · **Confidence:** High · **In scope:** Y

### A-07 — P2 — The location of the 2026 negative-price share is not stated, and the more relevant energy share is omitted

- **Location:** PDF p.55, §11.8 l.1006: "Negative prices occur in 14.1% of 2026 intervals, against 7.7% in the 2025 months."
- **Problem:** These are **HB_WEST** interval shares. The sentence does not say so, and it sits in a section that otherwise discusses the reference node and 485 nodes. The reference node's own 2025 full-year share (6.2%, §8.2) is a different metric at a different location, which invites confusion. The stop rule and the unpaid-volume stress depend on the **energy** share (23.6% versus 13.7%), which is not given.
- **Evidence:** `scenario-versions/data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv`, Jan–Sep rows.
- **Minimal fix:** "At the West hub, negative prices occur in 14.1% of Jan–Sep 2026 intervals (7.7% in the same 2025 months), covering 23.6% (13.7%) of the fixed 2025 output profile's energy."
- **Changes an existing number?** N · **Confidence:** High · **In scope:** Y

### A-08 — P2 — "Severe" is not a defined severity level

- **Location:** PDF p.3, l.29: "the severe assumed 15.24% unpaid-energy deduction".
- **Problem:** 15.24% equals the same-year negative-price energy share observed at the node. §10.3 calls it a stress assumption, and the 30.48% downside "doubles the stress". "Severe" implies the base share is near the top of the plausible range. The West-hub 2026 diagnostic (23.6%; see A-07) shows it is not. The deduction is severe only in the sense that energy which would earn about −$1.79/MWh in the merchant market forgoes $40/MWh under the contract assumption. That distinction belongs in §10.3, not in an adjective.
- **Minimal fix:** "…with the assumed 15.24% unpaid-energy deduction (a stress parameter, not an observed contract clause)…"
- **Changes an existing number?** N · **Confidence:** Med · **In scope:** Y

### A-09 — P2 — The fixed-price route has several names

- **Location:**
  - l.29: "flat nominal contract".
  - l.47: "Fixed-price route".
  - l.706: "simplified node-level paid-volume arrangement".
  - l.1325 (PDF p.68): "Simplified node PPA".
  - Tables 10-1 and 10-2: "Fixed base".
- **Problem:** Brief §4 requires node sale, simplified fixed-price payment and hub-settled VPPA to be kept visibly distinct. Five labels for one mechanism weaken that distinction. "PPA" in Appendix B in particular suggests an observed contract form.
- **Minimal fix:** Use "simplified node-level fixed-price route" at first mention in each chapter and as the Appendix B column header. Keep "Fixed base / downside / upside" as the scenario names.
- **Changes an existing number?** N · **Confidence:** High · **In scope:** Y

### A-10 — Disclosed limitation (no change needed): reference-node identity and settlement rights

- **Location:** PDF p.29–30, l.529–531, l.547–549; Table C-1 l.1372.
- **Assessment:** The wording is correct and well bounded:
  - ERCOT documents establish TAYGETE2_ALL → TAYGETE2 units → West Texas Solar Project II LLC.
  - The ERCOT → EIA 64075 step is labelled an attribute match.
  - The mapping files are dated September/October 2026, and the 2023–2025 versions are not examined.
  - The hypothetical 100 MWac case has no settlement agreement.
  - The node-selection rationale is undisclosed.

  This meets the brief's boundary that the attribute match cannot prove settlement rights. No further research is needed for this edition.

### A-11 — Disclosed limitation: the negative-price stop rule assumes perfect response to the 15-minute settlement price

- **Location:** PDF p.30, §8.2 l.561–565.
- **Assessment:** In practice, a resource reduces output through SCED offers against 5-minute prices. It does not see the 15-minute settlement-point price in advance. The report states "complete responsiveness to interval prices" and that "dispatch feasibility … [has] not been verified". It also shows that the rule is worth only about $80k a year in the merchant case ($6.551m versus $6.471m), so the modelling simplification has little effect on the merchant results.

  Under a hub hedge the rule matters more. The separately versioned calculation already distinguishes "stop if node negative" from "run if node plus hedge is non-negative" (break-even $60.6 versus $71.6 at 15 years). §8.2 l.565 already flags contract dependence. No change needed.

### A-12 — Disclosed limitation: gross versus net receipts and 2026 price finality

- **Location:** PDF p.72, Appendix C l.1385–1394; PDF p.55, l.1002–1004.
- **Assessment:** The gross-to-net bridge (losses, QSE fees, imbalance and uplift, RECs, hedge) is listed, and the omitted items are explicitly "not established as zero-cost". The 2026 coverage gaps, the missing version field, and the 423 HB_WEST cross-product differences are described accurately against `FIN-08_2026-Price-Coverage-Summary.csv`. These are within the boundary. Only A-02's labelling issue remains.

---

## 3. Summary table

| ID | Severity | PDF page | MD line | Problem | Minimal fix |
|---|---|---|---|---|---|
| A-01 | P1 | 3, 4, 60, 61 | 29, 47, 1124, 1152 | $66 break-even shown without its 30-year / node / unpaid-volume basis; hub-hedge $60.6–$84.8 absent from the summary and decision sections | Qualify the label; add the hub-hedge row and line |
| A-02 | P1 | 3, 4 | 28, 45 | "Realized sales price" / "earns" for modelled gross energy value | Relabel as modelled gross energy value |
| A-03 | P1 | 4, 39 (vs 55) | 58–62, 704 (vs 998, 1006) | 2025 base is about 93% pre-RTC+B; 2026 diagnostic shown only in §11.8 | One cross-reference sentence, labelled as a diagnostic |
| A-04 | P1 | 29, 71 | 533, 1381 | Foreclosure stated without its October 2022 / pre-COD timing | Add timing sentence; warn against post-2023 inference |
| A-05 | P1 | 61 (3) | 1149 (32) | 48% capture ratio offered as a heuristic without its 3rd-percentile / hub 65% context | Add percentile and West hub ratio |
| A-06 | P2 | 29, 3 | 545, 32 | Hub framed as an alternative price, not a basis | Restate as output-weighted basis |
| A-07 | P2 | 55 | 1006 | 2026 negative share not located at the hub; energy share missing | Add "West hub" and 23.6% / 13.7% |
| A-08 | P2 | 3 | 29 | "Severe" adjective for the base unpaid share | Replace with "assumed (stress parameter)" |
| A-09 | P2 | 3, 39, 68 | 29, 47, 706, 1325 | Five labels for the fixed-price route | One consistent label |
| A-10 | Disclosed | 29–30 | 529–549, 1372 | Node identity and settlement rights | No change |
| A-11 | Disclosed | 30 | 561–565 | Perfect-foresight stop rule | No change |
| A-12 | Disclosed | 55, 72 | 1002–1004, 1385–1394 | Gross vs net; 2026 finality | No change |

## 4. Overall verdict

**② Handover-ready after the listed minimal edits.**

I found no P0. Every number I spot-checked reproduces from the frozen tables. The market mechanics (node versus hub, the two-leg hedge identity, basis, the tail, gross versus net, RTC+B timing, and the 2026 diagnostic boundary) are stated correctly in the body. The four P1 items concern qualifiers that are missing where the reader decides: Chapter 1, Table 1-1, §13.2 and Table 13-1. Each can be fixed with wording and numbers that already exist in the package. None requires new research, and none changes a frozen result.

This verdict covers the stated market-research and screening use only. It is not a publication authorisation or acceptance of the original Version 1.0.
