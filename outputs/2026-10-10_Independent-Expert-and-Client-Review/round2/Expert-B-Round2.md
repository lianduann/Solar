# Expert B: Round 2 (interaction): cross-review of Expert C and responses to client misreadings

**Reviewer:** Expert B (project finance and financial modelling).
**Date:** 10 October 2026.

**Rules followed:**
- Evidence only, with no reruns.
- Counts and medians below are "reviewer arithmetic" on frozen files.
- "Could not verify" is stated where it applies.
- Agreement is given only where my own check supports it.

**Files read in this round:**
- `Expert-C-Methods-Review-EN.md`
- `Client-E-Manufacturer-Review-ZH.md`
- `Client-F-Developer-Buyer-Review-ZH.md`
- `data/empirical/C_three_year_mixture_scenario_by_node.csv`
- `data/empirical/C_block_bootstrap_within_year.csv`
- `data/empirical/tables/T_C1_tail_summary_strict_nodes.csv`

The `data/` paths are relative to the package root.

---

## 1. Cross-review of Expert C (findings that touch financial conclusions)

### C-03: "485 nodes" are settlement points with duplicated price outcomes

**Position: Agree. Severity P1.**

**My check (reviewer arithmetic)** uses `C_three_year_mixture_scenario_by_node.csv`, tier = strict, 485 rows, matching on the exact (rev_2023, rev_2024, rev_2025) receipt triplet. It confirms C's counts:

| Year | Positive settlement points | Distinct receipt series |
|---|---|---|
| All years (sample) | 485 | 400 |
| 2024 | 13 | 10 |
| 2025 | 2 | 2 (NF_BRP_RN, RHESS2_ESS1) |

Two of the 13 positive 2024 points sit in duplicate groups: FAL_FALCONG1/2/3 and BRP_ZPT1/2_RN.

**Financial materiality.** The issue is a labelling problem, not a change in any financial conclusion. Recounting on the 400 distinct series (reviewer arithmetic, for materiality only, not for insertion):

| Measure | Reported (485 points) | Distinct series (400) |
|---|---|---|
| 2024 positive share | 2.68% | 2.5% |
| 2025 positive share | 0.41% | 0.5% |
| Same-year median NPV, 2023 | +99.8 | +101.4 |
| Same-year median NPV, 2024 | −81.6 | −81.5 |
| Same-year median NPV, 2025 | −81.3 | −81.0 |
| Equal-weight mixture positive share | 12.2% | 11.75% |

No sign changes and no qualitative statement changes.

**Financial sentences affected.** These sentences count points as if they were locations:
- §1.1 item 4 (MD line 31): "all 485 rule-screened nodes, versus 13 in 2024 and two in 2025";
- Table 1-1 (line 52): "485 / 13 / 2 out of 485";
- Table 10-4 share column (lines 850–854);
- line 883: "South 13";
- §11.8: 99.4% (line 994);
- §11.9: 12.2% (line 1020).

The NPV medians in Tables 10-4 and 10-5 and the $12.1m threshold are unaffected in substance.

**Fix.** I endorse C's §8.4 sentence and propose two small additions:
- Table 1-1 row label: "Same-year positive settlement points (rule-screened resource nodes), 2023 / 2024 / 2025".
- Line 883: "South 13 (10 distinct price series)", since C found that 13 points collapse to 10.

The de-duplicated shares above should **not** be inserted as new results. If the author wants them, they belong in optional future scope (C-11).

On the "about 400" figure in C's sentence: it is a simple count from a frozen file and is acceptable, provided the author re-confirms it.

**Wind and storage resource nodes in the sample.** Pricing one solar profile at a storage or wind resource node is still a valid historical price location. The risk is only that readers take "nodes" to mean solar sites. C's wording ("not … solar sites") covers this. No further change is needed.

**Confidence:** High on the counts. I relied on exact receipt matches as C did and did not open the price panel.

### C-04: medians of node-level ratios described as the ratio for a median node

**Position: Agree. Severity P2.**

I confirmed the source: `T_C1` `share_Rcurt_median` = 0.547353 is a median of node-level shares.

The same imprecision applies to line 1020's "median node needs 44.9%". This is a financial-reading point: a median of required discount weights is not the requirement of a node with median receipts.

**Fix:** keep C's wording unchanged.

### C-05: tail-stress and resampling outputs use the full calendar

**Position: Agree. Severity P2.**

I confirmed two values:
- `C_block_bootstrap_within_year.csv`, TAYGETE2_ALL 2024: `npv_point` = −91.84m. This is the full-year value in B.1; the common-calendar value is −92.15m.
- `T_C1` 2024: `npv_raw_median` = −81.33m. The common-calendar value is −81.59m.

The 2023 values used in the text (99.78; 54.7%; −56.6m; 99.4%) are identical on both bases. No financial sentence is wrong.

This is the same calendar issue the report already labels for the CPI file at line 881. A consistent caption note is therefore sufficient.

**Fix:** keep C's caption wording. Optionally, extend line 881's sentence into a general rule in B.1: "Tail-stress, resampling and CPI files use each year's full calendar; the matrix, Tables 10-4/10-5 and the mixture use the common calendar."

---

## 2. Responses to client misreading claims (finance)

### E-02: the summary invites "U.S./ERCOT solar is generally uneconomic"

**Text change needed: Y. Severity P1 (agree).**

The brief §4 explicitly excludes this inference. The report blocks it only on p. 63 (line 1194). The summary's "Limits of this chapter" box (line 66) lists pre-tax, single-reference and stress caveats, but not this one.

E's wording is supported by existing text (lines 770 and 1194). One edit: drop "U.S. module demand forecast" in favour of the report's own phrase, to avoid introducing a new topic.

> These pre-tax, pre-credit, unlevered results for one hypothetical system do not show that solar projects in ERCOT are generally uneconomic; they are conditional screening calculations, not a market-wide finding or a demand forecast.

**Placement:** add it as item (4) in the line-66 limits box rather than in the bold lead, to keep the lead short. Either location is acceptable.

### E-03: the $35.38m credit read as supplier or product value (Table 13-1, row 2)

**Text change needed: Y. Severity P1 (agree).**

The row answers a supplier-eligibility question with a project-level, eligibility-assumed credit. The material-assistance cost-ratio test (40% / 45%, line 838) and the ownership/control tests are exactly the supplier-relevant facts, and the illustration does not test them.

I endorse E's replacement cell and the navigation additions ("10.8" in the manufacturer route; "see Section 10.8" in Table 13.1).

**Merge with EB-03 / F-02:** any place that repeats $35.38m should also carry "30% rate and eligibility assumed; not an after-tax value". For Table 13-1, E's "assumes eligibility and is not a supplier- or product-level finding" is sufficient.

### E-04: "U.S. module input" read as an exporter's own price

**Text change needed: Y. Severity: I would grade P2. I do not object if the coordinator keeps P1.**

The definition exists only at line 411 ("a U.S.-assembled module input including its stated subsidy treatment"; the module line is about $0.29/Wdc). Item 3 already says "estimates no actual China-to-U.S. price transmission", which partly blocks the misreading. That is why I grade it lower.

The $3.76m arithmetic is correct for a 10% change in that benchmark input. It does not represent a 10% cut in an exporter's FOB price, because freight, duties and the MIP sit between the two.

**Fix:** E's parenthesis at first use (lines 30 and 371), worded from line 411:

> (the DOE/NLR benchmark's U.S.-assembled module input, about $0.29/Wdc including its stated subsidy treatment; not an imported-module or exporter price)

### F-01: hub-hedge (VPPA) break-even missing from the summary

**Text change needed: Y. Severity: P2. Partly agree.**

F correctly reports $60.6–$84.8 at 4.27% (confirmed in round 1 against `VPPA-Breakeven-Strikes.csv`). The risk that a buyer uses the $66 fixed-route figure as a VPPA break-even is plausible.

I grade it P2 rather than P1 for two reasons:
- Item 5 is not wrong; it is an omission.
- The VPPA range depends heavily on an unsourced merchant tail. About 43% of revenue PV in the 10-year stop / settle-through case (39–43% across cases; EB-05) comes from the tail. Promoting the range into Table 1-1 would give an unsourced-tail figure the same prominence as baseline outputs.

**Fix:** use F's sentence (a) in item 5, merged with EB-05:

> A hub-settled contract needs its own settlement calculation: in a separately versioned HB_WEST hedge setting (Section 10.3), break-even flat nominal strikes are $60.6–$84.8/MWh at 4.27% real across tenor, dispatch and negative-price clauses, and depend heavily on the assumed post-contract merchant tail. Neither figure is an observed offer.

I recommend **not** adding a Table 1-1 row, or, if one is added, labelling it "separate version; tail-dependent".

### F-02: −$50.59m is not an after-tax NPV

**Text change needed: Y. Severity P1. Agree, and this merges with my EB-03, which I upgrade to P1.**

Merged wording for line 35, combining F-02 and EB-03:

> Assuming a 30% rate, eligibility and cash at end-2027, the credit's present value at 4.27% is $35.38m ($7.08m at the 6% base rate). Adding it to the pre-tax reference NPV gives −$50.59m. This is a pre-tax NPV plus one illustrative credit, not an after-tax NPV: income tax, depreciation and the section 50(c) basis reduction are not modelled, and eligibility remains unproven.

### F-03: simulated output exceeds all observed plants, so the $66 and $577 thresholds are not conservative on volume

**Text change needed: Y. Severity: P2 (F graded P1). Partly agree.**

**The direction is right.** Both thresholds depend on volume:
- The fixed break-even scales inversely with paid volume (line 712; reviewer arithmetic 55.91 / (1 − u)).
- The nodal break-even CAPEX falls with receipts, through the NPV identity at line 846.

**F's comparison mixes measurement bases.** The 33.38% is *potential* AC output. The observed cohort figures are *net* generation, which already excludes curtailment (about 6–7% system-level, lines 679–680). The economically relevant volume for both thresholds is delivered or paid energy: **28.29%** (line 674). That is:
- above the screened cohort medians (24.6–25.0%);
- inside the 25.5–29.7% range of the three newer (2023–2024 COD) plants.

So "exceeds every observed plant" overstates the gap for break-even purposes. The correct statement is "upper end of the observed range".

**Severity.** §9.5 already discloses that output is uncalibrated, with no P50/P90 (line 682). The fix is to surface this in the summary, so P2 (a disclosed limitation that needs a pointer) rather than P1.

**Fix:** item (5) in the line-66 limits box:

> (5) Simulated output is uncalibrated. The delivered capacity factor (28.3%) is at the upper end of screened Pecos operating plants (cohort medians about 25%; Section 9.5), so the break-even price and CAPEX thresholds are not conservative on volume.

Add F's Table 11-1 footnote:

> Lower paid volume raises the fixed-price break-even approximately in inverse proportion (Section 10.3 paid-volume stress).

**No numbers should be inserted.** F's illustrative $73 and my own scaling (28.29 / 25 × 66 ≈ $75, reviewer arithmetic) should stay out of the report. Net-versus-potential boundaries make any such substitution unsupported.

---

## 3. Changes to my round-1 findings

| ID | Change |
|---|---|
| EB-03 | **Upgraded P2 → P1**, merged with F-02 using the wording in §2 above. |
| EB-05 | Kept at P2. Merged into the F-01 summary sentence; the in-body fix in §10.3 still applies. |
| EB-02 | Kept at P2. If F-01's item-5 rewrite and an item-2 rewrite are made together, EB-02's wording for item 2 stands unchanged. |
| EB-06 | Kept at P2, confidence Medium. No change. |
| EB-01, EB-04, EB-07 to EB-10 | No change. |
| — | No findings withdrawn. |

**Verdict unchanged:** ② handover-ready after the listed minimal edits.

The financial P1s are now:
- EB-01 (fixed-route denominator labels);
- EB-03 / F-02 (after-tax label);
- E-02 (no "generally uneconomic" inference);
- E-03 (supplier row in Table 13-1);
- C-03 (settlement-point counts).

No item changes an existing number.

## 4. Summary table

| Item | Position | Severity (B) | Fix change |
|---|---|---|---|
| C-03 settlement points / ~400 distinct series | Agree (counts verified: 400; 13 → 10; 2 → 2) | P1 | C's §8.4 sentence, plus "settlement points" in the Table 1-1 label and "(10 distinct price series)" at line 883. De-duplicated shares (2.5%, 0.5%, 11.75%) stay out of the report; financial conclusions are unaffected |
| C-04 median of ratios | Agree | P2 | None; C's wording, also covering 44.9% |
| C-05 full vs common calendar | Agree (−91.84 and −81.33 verified) | P2 | C's captions; optionally generalise line 881 into B.1 |
| E-02 "generally uneconomic" | Agree | P1 | Add as limits item (4); avoid introducing "module demand" |
| E-03 $35.38m in supplier row | Agree | P1 | E's cell and navigation edits, plus "30% rate and eligibility assumed" |
| E-04 "U.S. module input" | Agree on text; lower severity | P2 (P1 acceptable) | Parenthesis from line 411, adding "not an exporter price" |
| F-01 VPPA range in summary | Partly agree | P2 | Item 5 sentence with tail-dependence; no Table 1-1 row, or a labelled one |
| F-02 −$50.59m not after-tax | Agree (= EB-03) | P1 | Merged EB-03/F-02 wording |
| F-03 output not conservative | Partly agree: compare delivered 28.3%, not potential 33.4% | P2 | Limits item (5) with "upper end of observed range"; F's Table 11-1 footnote; no new numbers |
| EB-03 (own) | Re-graded | P2 → P1 | Merged with F-02 |
| Withdrawn | None | — | — |
