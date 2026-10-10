# Expert C — Round 2: Cross-Examination and Responses on Interpretation

**Role:** Expert C (econometrics and research methods).
**Files read in this round:**
- `Expert-B-Project-Finance-Review-EN.md`
- `Client-E-Manufacturer-Review-ZH.md`
- `Client-F-Developer-Buyer-Review-ZH.md`
- the A-07 and A-08 entries in `Expert-A-Energy-Markets-Review-EN.md` (for the 2026 item only)

**Rules:** Same as round 1. I reran no model and added no data. Checks are lookups in frozen files or simple arithmetic labelled "reviewer arithmetic".

**Frozen files consulted** (paths are relative to the evidence-package root):
- `data/scenario_metrics.csv`
- `scenario-versions/data/VPPA-Breakeven-Strikes.csv`
- `scenario-versions/data/VPPA-Route-Scenarios.csv`
- `scenario-versions/data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv`
- `closure-evidence/Numbers-and-Claims.csv` (N19–N21)
- `data/empirical/C_three_year_mixture_scenario_by_node.csv`

## 1. Cross-examination of Expert B

### EB-01 — Fixed-route LCOE and "delivered GWh" are on a paid-energy denominator. **Agree; P1 (borderline P1/P2).**

**Verification.**
- `scenario_metrics.csv` gives `fixed_downside` delivered/simulated = 195,157.6 / 280,735.5 = 0.6952 = 1 − 0.3048.
- `node_downside` has the same simulated energy (280,735.5 MWh) and delivered share 0.8466.
- The two cases share a cost stream: their potential-energy LCOE is identical at $46.39/MWh.
- The $54.8 versus $66.7 delivered-basis LCOE gap therefore comes only from the denominator. This confirms B, and resolves the "could not verify" in Client F's F-07.

**Methods addition.** Fixed base and Node base show identical delivered GWh (247.8) and LCOE ($48.85). That is a coincidence of construction: the 15.24% unpaid share was set equal to the node's negative-price energy share. It does not show that the two mechanisms deliver the same volume. Without this note, readers may treat Fixed base = Node base as a validation.

**Severity.** I accept P1. Table 2-1 promises "the stated … energy denominator", and that promise is not met for three rows. The $66.7 figure is not in the summary, however, so P2 would also be defensible.

**Fix change.** Keep B's relabel and note. Append one clause to B's note: "Fixed base and Node base coincide only because the base unpaid share was set equal to the node's negative-price energy share."

### EB-04 — IRR labels ("Single rate not certified" versus "no numerical root"). **Agree; P2, with one wording correction.**

**Verification.**
- `fixed_downside` `irr_status` = `no_numerical_root_completeness_not_certified`, with empty `irr_roots`. So "Single rate not certified" in Table 10-2 misdescribes the status: no rate was found.
- B's statements about the other cases match `irr_roots`: Node base, Node downside and Fixed base have only negative roots; Fixed upside has −86.48% and +1.41%.

**Wording correction.** B's proposed note says "no scenario has a root at or above the 4.27% convention". A root search whose completeness is not certified cannot support a universal "no root" claim. The claim can be supported by the NPV signs instead: all six NPVs are negative at 4.27%, 6% and 8%.

**Fix change.** Write: "no root at or above 4.27% was found, and NPV is negative at all three tested rates". Keep B's "No root found (search not certified complete)" label.

### EB-05 — VPPA range and tail-share case. **Partly agree; P2. Correct the range B proposes.**

**Range.** Confirmed. The 2025-path, 4.27% rows span $60.57–$84.77/MWh, and the 6% and 8% rows span $68.38–$107.12/MWh (claims N19–N20). The traceability point (the notes table shows six rows, the CSV holds eight) is valid.

**Tail share.** Reviewer arithmetic from `VPPA-Route-Scenarios.csv` (10-year tenor, K = $40, 4.27%), as tail PV / (contract-years revenue PV + tail PV):

| Dispatch | Hub clause | Tail share |
|---|---|---|
| stop | settle-through | 42.7% (matches N21) |
| stop | suspend | 43.6% |
| run | settle-through | 38.7% |
| run | suspend | 42.8% |

B's proposed "39%–43%" therefore understates the upper end. The correct range is **39%–44%**.

**Denominator check.** I checked that "contract-years revenue" includes the hedge leg. Year-1 revenue of $9.598m equals node receipts of $6.55m plus a hedge net of $3.05m. So B's denominator is the right one.

**Fix change.** Write "(about 39%–44% across dispatch and clause settings; 43% in the stop/settle-through case)".

### B's claim that the frozen NPV identity and Table 10-5 reproduce. **Agree.**

**Reviewer arithmetic.** I applied B's annuity factors to the frozen median receipts (18.5562 / 6.83358 / 6.85495):
- 6%: annuity factor 12.8205, cost PV $179.29m. Results: +58.61, −91.68, −91.40.
- 8%: annuity factor 10.569, cost PV $172.57m. Results: +23.55, −100.34, −100.12.

All six match Table 10-5.

**Methods condition.** Reporting a "median NPV" equal to the NPV of median receipts is valid only because NPV is an increasing affine function of receipts within one rate. The median therefore commutes with the transformation. The same reasoning validates Table 10-4.

The identity does **not** hold for:
- the flat nominal route, which the report states at line 846;
- any summary that mixes discount rates;
- a mean of nonlinear stresses.

The report's use stays within these limits. No change needed.

## 2. Responses to client items on interpretation

### E-02 / F-10 — "Generally uneconomic" inferred from 485 / 13 / 2. **Agree that a summary sentence is needed; P1.**

Methodologically, the 485 / 13 / 2 counts cannot support any population claim about ERCOT solar economics. Five reasons:

1. One hypothetical profile and one cost stack are priced at every settlement point. This is a price-location sensitivity, not a sample of projects.
2. The settlement points are rule-screened survivors, not a random draw (§8.4, B.1).
3. The results are pre-tax, pre-credit and unlevered.
4. The price-year shape is repeated for 30 years, which is a stress setting.
5. Only three regime years are observed.

Line 31 already says the shares are "not profitability probabilities", but nothing in Chapter 1 blocks the separate inference that solar is generally uneconomic. The correct sentence exists only at §14.4 (line 1194) and §10.5 (line 770). E-02 and F-10 should be merged into one fix.

**Fix.** Add to the end of the §1.1 bold lead (line 26) or to the §1.3 limits box:

> "These are conditional results for one hypothetical system priced at screened settlement points under pre-tax, pre-credit, unlevered assumptions; they do not show that ERCOT solar projects are generally uneconomic and are not a forecast of module demand."

**Is my C-03 relevant?** Yes, but only as a qualifier, and it does not change the direction of the message.

| Year | Settlement points positive | Distinct receipt series positive | Note |
|---|---|---|---|
| 2025 | 2 | 2 | The two series are distinct, so the count is unchanged. One of them, RHESS2_ESS1, is a storage resource node. |
| 2024 | 13 | 10 | — |

About 400 of the 485 points carry distinct receipt series. The 2025 share therefore moves only from 0.41% to roughly 0.5% (reviewer arithmetic: 2/400).

The client-relevant point is that "positive nodes" are price locations, not solar sites or projects. The merged sentence above already says "settlement points", which covers this. No further change to the summary is needed beyond that word.

### F-03 — Simulated 33.4% capacity factor versus observed ~25%: is "not conservative on output" correct, and is it already disclosed? **Partly agree; keep P1 for the summary qualifier only, with softer wording.**

**Disclosure.** §9.5 already discloses this clearly:
- "exceeds every observed plant in these screened cohorts" (line 674);
- "the simulated output is therefore not calibrated" (line 682).

So the body text needs no change.

**Why "not conservative on volume" is too strong as a statement of fact.** The comparison is confounded, and the report itself lists the confounders:
- **Different boundaries.** The 33.38% figure is potential, pre-curtailment output. The ~25% medians are net generation after curtailment, availability losses and other losses. System curtailment alone was about 6–7% (lines 679–680).
- **Different capacity denominator.** The EIA medians use each plant's 2025 recorded MWac for both years.
- **Not weather-normalised.** The observed values are not adjusted for weather.
- **Overlap at the delivered level.** The simulated delivered factor of 28.29% lies inside the 25.5%–29.7% range of the three recent-COD plants.

The evidence shows that output is **uncalibrated and above screened operating medians on a potential basis**. It does not show that output is biased high by a known amount.

**The inverse-proportion claim** (break-even price scales with 1 / paid volume) holds exactly only for the flat nominal fixed route with costs held fixed: the paid-volume stress in B.5 divides by 1 − u. It does not apply to the nodal break-even CAPEX or the price multiplier in that simple form.

**Fix.** Add item (4) to the §1.3 limits box:

> "(4) Simulated output is not calibrated: its 33.4% potential AC capacity factor exceeds the screened Pecos operating medians (about 25%, on a different net-generation basis), so break-even thresholds are not shown to be conservative on volume; on the fixed-price route, the break-even price rises roughly in inverse proportion to paid volume (Sections 9.5, 10.3)."

**Severity.** P1, because the break-even thresholds are headline numbers. If the coordinator treats §9.5 disclosure as sufficient, P2 is acceptable.

### F-08 / A-07 / C-02 — The 2026 West-hub negative-price shares. **Consensus on the location label. My source-attribution point stands. Proposed merged severity: P1.**

**What all three agree on.**
- The 14.1% / 7.7% figures are HB_WEST interval shares for January–September. I re-checked `HB_WEST-2026-JanSep-Post-RTCB-Context.csv`: 0.1412 and 0.0766.
- The energy shares A cites are also correct: 0.2361 and 0.1367.

**The two points in my C-02 that A-07 and F-08 do not cover.**
- **Source of the 2026 series.** The 2026 hub series comes from the NP6-785-ER year-to-date file (script `10_hb_west_2026_context.py`). The bullets above the diagnostic describe a different product, the API data with 125 missing intervals, and the two series differ in 423 intervals.
- **Basis of the 2025 comparator.** The 2025 comparator comes from the 2023–2025 archive.

Without this note, a reader assumes the diagnostic inherits the API coverage caveats, when it actually rests on the comparator file.

**Methods caution on A-07 and A-08.**
- **Labelling the energy share.** Adding the 23.6% energy share is acceptable only if it is labelled "share of the fixed 2025 output profile's energy at West-hub prices". It is not a 2026 plant outcome.
- **A-08's argument.** A-08 uses this 2026 hub figure to argue that the 15.24% base share "is not" near the top of the range. That compares a hub with a node, one partial post-reform year with a full pre-reform year, and an interval share with an energy share. It should not be cited as evidence about the severity of the node-based assumption. A-08's wording fix ("a stress parameter, not an observed contract clause") is fine on its own.

**Merged fix:**

> "As context only, using ERCOT's NP6-785-ER year-to-date hub file (which differs from the API series in 423 West-hub intervals): weighting January–September 2026 West hub prices with the 2025 simulated output profile gives $18.24/MWh, against $21.36/MWh for the same months of 2025 from the 2023–2025 archive. At the West hub, negative prices occur in 14.1% of January–September 2026 intervals (7.7% in the same 2025 months), covering 23.6% (13.7%) of the fixed 2025 profile's energy; the reference node's full-year 2025 interval share is 6.2% (Section 8.2)."

**Severity.** I would keep this at P1 because it attaches a data-provenance label to a post-reform claim. If the coordinator prefers to merge it as P2 alongside A-07 and F-08, the fix text is the same.

## 3. Changes to my own round-1 findings

| ID | Change | Reason |
|---|---|---|
| C-01 | Unchanged, P1 | The panels of Fig 11-3 remain unidentified. EB-09 shows the same pattern in Fig 10-2, so both could be fixed together. |
| C-02 | Unchanged, P1; merged with A-07 and F-08 | Section 2 above. |
| C-03 | **Re-graded P1 → P2** | Deduplication leaves the 2025 count unchanged (2) and the 2024 count at 10 distinct series. The message does not move, and the summary need is met by the word "settlement points" in the merged E-02 / F-10 sentence. The §8.4 qualifier stays as a P2 edit. |
| C-04 to C-09 | Unchanged, P2 | — |
| Withdrawn | None | — |

**Verdict unchanged: ② handover-ready after the listed minimal edits.**
