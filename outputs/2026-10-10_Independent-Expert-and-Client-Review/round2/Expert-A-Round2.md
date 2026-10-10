# Expert A: Round 2 (Interaction)

**Reviewer:** Expert A (energy economics / ERCOT).

**Material read for this round:**
- Expert D: `Expert-D-Industry-Trade-Review-EN.md`
- Client E: `Client-E-Manufacturer-Review-ZH.md`
- Client F: `Client-F-Developer-Buyer-Review-ZH.md`

**Rules:** Same as round 1. No models were rerun and no web was used. Any number I computed myself is labelled "reviewer arithmetic". If I could not check something, I say "could not verify".

---

## 1. Cross-examining Expert D on the three-layer chain (manufacturing → U.S. delivered cost / trade → ERCOT value)

### D-01: the $0.29/Wdc module benchmark already has a −$0.069/Wdc 45X subsidy subtracted

**My position:** Agree, P1, as a labelling fix only. The market-side conclusions do not change.

**What I checked.** `data/supplement/A/A_pvscm_item_level_pv_only.csv` lists the module items. They add up to $291.21/kWdc. That total includes the line `Subsidy … -68.88`. Without that line, the module cost is $360.09/kWdc. `A_module_passthrough_parameters.csv` describes the 26.111% share as "US-assembled benchmark module cost element incl. 45X subsidy". Both of D's facts are correct. D is also right that the gap to the $0.38/W MIP is about $0.02/W on a gross basis, not about $0.09/W. That comparison still ignores the differences in dollar year and in the Wdc versus W denominator, as D notes.

**Does it change a market-side conclusion?** No. The report's numbers are internally consistent with their own label ("U.S. module input"). The issue is that the label does not say the input is net of the subsidy.

As an illustration only (reviewer arithmetic; not proposed for insertion), suppose the share were computed gross of the subsidy:
- Total module-system cost would be about 1,115.3 + 68.9 = 1,184.2 $/kWdc.
- The module share would be about 30.4%, and the effective pass-through share about 34.8%.
- A 10% module change would then move NPV by about $4.4m instead of $3.76m.
- A zero-priced module would leave NPV at about −$42m instead of −$48.3m.

The ordering in Table 11-3 and §13.1 survives either way. Module-side effects stay one to two orders of magnitude smaller than the revenue-side effects:
- the 2023→2024 price-year change: −$179.31m;
- a +10% change in exported volume: +$10.14m;
- the nodal break-even, which needs CAPEX to fall by about 60%.

The H1 conclusion and "Lower equipment prices help, but … leave a large capital-recovery gap" are therefore unaffected.

**One addition from the market side.** The net-of-45X basis matters for which way a price change can go. A covered imported module faces the $0.38/W floor from 4 Dec 2026, plus the additional 15% duty. So for covered imports, the report's −10% and −30% module scenarios are less likely in practice than the reverse direction. The report already says "signals a possible limit to factory-price transmission" (l.411). The Table 11-3 rows should carry the same qualifier.

**Fix:**
- Adopt D's wording at l.411, the Figure 5-1 caption and l.1103.
- Add to the Table 11-3 rows "U.S. module input −10% / −30%" (l.979–980): "net-of-45X U.S.-assembled benchmark input; covered imports subject to the section 232 MIP from 4 Dec 2026 (5.7)".
- No number changes.

### D-05: shares of the import mix

**My position:** Agree, P2. This has no effect on the ERCOT-value layer.

**What I checked.** In `data/r2/A/A_census_hs854143_by_country.csv`, January–August shares are:

| Country | 2025 | 2026 |
|---|---|---|
| Indonesia | 0.2704 | 0.1155 |
| Laos | 0.1932 | 0.0105 |
| India | 0.1517 | 0.0007 |

That is about 61.5% combined in 2025 and 12.6% in 2026 (reviewer arithmetic). D's figures and wording are correct.

**Effect on the chain.** This only changes how the trade layer is described. It does not touch the delivered-cost bridge, which uses no customs data, or any ERCOT figure. D's replacement sentence is descriptive and keeps "modules only, cells not shown". I support it as written.

### D-11 / E-01: dated trade facts in the executive summary

**My position:** Partly agree. The severity should be P2 for the stated use; I note E's P1 below. The wording should be narrower than E's version.

**Why it matters for the chain.** Item 3 of the summary (l.30) is the one place where manufacturing meets project value. It already says the sensitivity "estimates no actual China-to-U.S. price transmission". Adding the MIP date gives the reader the main reason transmission is limited. That is a real improvement in how the three layers connect.

**Severity.** For the stated product use (screening and mechanism), the facts are already present, verified and dated in §5.7, which the manufacturer navigation row points to. So the omission does not block use, and P2 fits. E's P1 is understandable from the exporter-audience view. I would not argue strongly against the coordinator choosing P1.

**Wording.** Use D's sentence, which covers only the MIP and the 15% duty. Do not adopt E's addition "China's export VAT rebate for listed PV products ended on 1 April 2026" in the summary, for two reasons:
- **D-10.** The cited MOF page (P08) was not retrieved. The retained Daqo 20-F describes a phased reduction (9% → 6% from 1 Apr 2026, abolished 1 Jan 2027). Until the product scope is reconciled, this fact is weaker than the MIP fact.
- **E's citation of P07** is the January 2025 pricing reform, which has nothing to do with trade.

**Merged wording (append to item 3, l.30):**

> "From 4 December 2026, covered imported cells and modules face section 232 minimum import prices ($0.22/W; $0.38/W) and an additional 15% duty, alongside continuing AD/CVD (Section 5.7). These are compliance thresholds, not delivered prices, and the module benchmark above is a net-of-45X U.S.-assembled input. [P01]"

---

## 2. Responses to client items in my area

### F-01 + A-01: hub-hedge break-even missing from the summary — one merged wording

**My position:** Agree, P1. F-01 and A-01 are the same issue.

F adds a fair point that I had only touched on. The last sentence of summary item 5, "A hub contract therefore needs its own settlement calculation", reads as if that calculation was never done, when §10.3 contains it.

**Single merged fix:**

1. **Item 2 (l.29), replace with:**
   > "Payment terms matter. A **30-year node-level fixed-price route** breaks even near $66/MWh with the assumed 15.24% unpaid-energy stress ($80.4/MWh at 30.48%; $55.9/MWh if all potential generation is paid). A separately versioned **10–15-year HB_WEST-settled hedge** with a node merchant tail breaks even at $60.6–$84.8/MWh on the 2025 price path at 4.27% real, depending mainly on tenor, dispatch, negative-price clause and the unsourced tail. None of these is an observed contract offer. [S08; F04; 10.3]"
   - This also absorbs F-06 and A-08 (see below).
2. **Item 5 (l.32), last sentence, replace with:**
   > "Under a hub-settled hedge the seller keeps node-minus-hub basis (+$0.67/MWh output-weighted in 2025); the hedge itself is costed separately in Section 10.3."
   - This also absorbs A-06.
3. **Table 1-1:**
   - Relabel l.47 to "Flat nominal break-even, 30-yr node-level fixed-price route (15.24% unpaid) | $66.0/MWh | 10.3, 11.3".
   - Add a row: "Hub-settled hedge break-even strike, 10/15-yr + node tail (separate version) | $60.6–$84.8/MWh | 2025 path, 4.27%; 10.3".
4. **§13.2 (l.1124) and Table 13-1 (l.1152):** add "(30-year node-level route; hub-hedge range in 10.3)".

**Changes a number?** N. **Confidence:** High.

### F-05 + A-02 + E-06: "Realized sales price", and $26.4 versus $22.13

**My position:** Agree. F-05/A-02 is P1. E-06 is P2 and is covered by the same fix.

E-06 adds that a non-specialist sees $26.4 and $22.13 as conflicting figures. E's proposed label ("Delivered-energy-weighted market price") resolves that conflict, but it drops "gross/modelled", which is the point of F-05 and A-02. The merged version keeps both:

1. **Table 1-1, l.45:**
   > "Modelled gross energy value, delivered-energy-weighted | $26.4/MWh | Reference-node RT prices × simulated output after stopping exports below $0; before fees, imbalance and losses to settlement ($22.13 on potential output before that response); 8.2"
2. **Item 1 (l.28):**
   > "…is modelled to receive a gross $26.4/MWh on delivered electricity (after stopping exports at negative prices)…"
3. **Item 5 (l.32):**
   > "…its potential-generation-weighted price is $22.13/MWh (before stopping exports at negative prices; $26.4/MWh on the energy actually delivered)."
4. **Optional, l.776:** "first-year real contract price" in place of "first-year realized price".

**Related point (F-07, which I checked).** In `data/scenario_metrics.csv`, `delivered_mwh_yr1` for the fixed scenarios equals simulated energy × (1 − the assumed unpaid share). For Fixed downside: 280,735.5 × (1 − 0.3048) = 195.2 GWh (reviewer arithmetic). That column is therefore **paid** volume, not physical delivery. The data column for the deducted energy is named `curtailed_mwh_yr1`, which is a misleading name in the frozen file. I agree with F-07 (P2): add "paid (fixed)" to the Table 10-2 header.

### F-04: navigation for electricity buyers, and a question table for §13.4

**My position:** In scope. The navigation row is P1. The question table is P2, and optional.

**Navigation row.** The readership line names "electricity buyers", but the navigation table (l.15–20) has no buyer entry. That is a navigation fault that one row fixes, so P1 under §6 is appropriate. Use F's row, adding §8.1:

> "Buying electricity or hedges (e.g., data-center operator) | 1, 6.2, 6.6, 8.1, 10.3, 11.3, 13.4, B.2 contract table, Appendix C"

**Question table in §13.4.** This is in scope only if every row restates a field the report already defines, with no indicative market terms or recommendations. F's list meets that test: each row maps to l.710–724, B.2 l.1325–1331 or Table C-1 FIN-03/FIN-11. Recommended rows:

| Question | Where defined |
|---|---|
| Settlement point / hub, and who bears node-to-hub basis? | 10.3, B.2 |
| Volume rule (as-generated, fixed shape, block)? | 10.3 |
| Negative-price clause (settle-through vs suspend) and the seller's dispatch right? | 8.2, 10.3 |
| Tenor and what follows (merchant tail sensitivity)? | 10.3 |
| Are RECs contracted separately from energy, and for what term? | 10.3 (Taygete I example) |
| Who bears QSE fees, imbalance/uplift, losses to the settlement point? | Appendix C |
| Credit support / collateral? | B.2, Table C-1 |

Severity is P2 because §6.2, §10.3 and B.2 already contain the substance. Placing a cross-reference to the B.2 table in §13.4 is the minimum. The new table is the fuller version of the fix.

### F-09: the 5.8 GW is part of the 238.6 GW

**My position:** Agree, P2. Verified.

**What I checked.** In `data/supplement/C/C_ercot_large_load_queue_status_by_year_2026-03.csv`, the 2030 column is 130,303 + 79,825 + 19,482 + 3,252 + 5,768 = 238,630 MW, which matches the "TOTAL printed" row (reviewer arithmetic). §6.5 (l.458) phrases it correctly. The summary (l.33) and Table 13-1 (l.1150) say "against" or "versus", which makes the two figures sound like separate quantities.

**A caveat on the fix.** ERCOT's printed total itself mixes requested MW with an observed, historical noncoincident measure. The 5,768 MW is also repeated unchanged in every column from 2025 to 2030. The fix should therefore stay arithmetic and must not invite a "conversion rate" reading.

**Fix (l.33 and l.1150):**
> "ERCOT's March table prints a 238.6 GW 2030 total across all process statuses, which includes about 5.8 GW observed energized on a historical noncoincident basis; the remaining categories are requests, studies or approvals."

**Changes a number?** N.

### Other overlaps with my round-1 findings (merged; nothing new)

- **F-06 = A-08** ("severe"). F's wording is better because it gives the $80.4/MWh downside. It is adopted inside the merged item 2 under F-01 + A-01. Merge them and keep F's severity (P2).
- **F-08 = A-07** (location of the 2026 negative-price share). F could not verify the 2025 figure of 7.7%. I can confirm it: the Jan–Sep 2025 HB_WEST row has `negative_interval_share` = 0.0766. **Merged wording:**
  > "At the West hub, negative prices occur in 14.1% of January–September 2026 intervals, against 7.7% in the same months of 2025, covering 23.6% and 13.7% of the fixed 2025 output profile's energy (reference-node full-year 2025: 6.2% of intervals, Section 8.2)."
  - P2.

---

## 3. Re-checking A-04 (timing of the foreclosure)

**New evidence.** The Comptroller Form 50-772-A (C06) is in the package at `sources/finance/comparables/C06_ch313_1377_772_2025.pdf`. I opened page 1:
- It is for tax year 2024.
- Section 2, item 7, says: "West Texas Solar Project II LLC purchased the project in a foreclosure auction initiated by the project's senior lender when the project's previous owner (Taygete Energy Project II, LLC) failed to repay its loan."
- It gives **no date** for the auction.

This confirms the report's wording at l.533. The **October 2022 assignment date** that my round-1 fix relied on comes from C09 (`finance-supplement/Entity-Node-Mapping.csv` L10). C09 is **not** retained in the client package; only the supplement's record of it is. D's materials and the client reviews add no independent dating.

**Also relevant.** An earlier supplement draft (`finance-supplement/Findings-and-Replacement-Text-EN.md` l.127) worded this as "a reminder that operating plants at this location have faced financing stress". That is exactly the misreading I flagged. The current report text has dropped it, which is correct.

**Re-grade: A-04 goes from P1 to P2.** The risk of misreading is real but moderate. The report already says the event supplies "neither an IRR nor the cause". The dated version of the fix depends on an original that is not retained.

**Revised fix (no date needed; uses only the retained C06):**

> "The filing does not date the auction or the default, so the event cannot be attributed to post-2023 operating prices at this node."

Optionally, if C09 is added to the retained sources, add: "The Comptroller received the assignment to the current owner on 6 October 2022, before the July 2023 in-service date."

**Withdrawals:** None. A-04 is downgraded. A-06, A-07 and A-08 are merged into F-01/A-01, F-08 and F-06 respectively.

---

## 4. Effect on my verdict

No change: **② handover-ready after the listed minimal edits.**

Nothing in D, E or F reveals a P0 in the market layer. D-01 corrects the trade/cost layer's labelling without changing any ERCOT-side conclusion. The merged P1s affecting the market layer:
- F-01/A-01: hub-hedge break-even missing from the summary;
- F-05/A-02: "realized" used for a modelled gross value;
- A-03: RTC+B and 2026 context missing from the base case;
- A-05: the capture-ratio heuristic;
- F-04: the buyer navigation row;
- D-01: the net-of-45X label, carried into Table 11-3.

All can be fixed with existing figures and wording.
