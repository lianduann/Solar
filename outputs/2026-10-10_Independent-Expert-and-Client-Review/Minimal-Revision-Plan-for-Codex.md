# Minimal Revision Plan for Codex

**Input:** `Integrated-Market-Research-Report-EN_Closure-Integrated.md`, repository commit `569a45c3f61c478c9996030afc1ee97174139b77`. Line numbers below refer to that file; PDF pages are physical page numbers of the 73-page PDF.

**Rules for this plan**

- No P0 was found. No existing number changes.
- No new data, model run or research workflow is required. Every addition below restates figures already present in the report, its frozen tables or retained originals.
- Apply the edits to a **new** manuscript version; do not overwrite the input.
- Keep the "candidate" label. This plan is not Version 1.0 acceptance.
- Chapter 1 discipline: the summary gains about 150 words in total. Each new number appears in Chapter 1 once. Diagnostics and method qualifiers stay in the body.

## Order of work

1. P1 edits R-01 to R-16, in the order given (summary first, then body tables).
2. P2 edits R-17 to R-27.
3. Rebuild the PDF. Re-check pages 3–5, 12, 16–17, 21, 41, 52, 55 and 60–61 visually.

---

## P1 edits (complete before handover)

### R-01 · §1.1 bold lead paragraph (line 26) — CF-04

Append:

> These are conditional results for one hypothetical system priced at screened settlement points, pre-tax and unlevered; they do not show that solar projects in ERCOT are generally uneconomic and are not a forecast of module demand.

### R-02 · §1.1 item 2 (line 29), Table 1-1 (line 47) and item 5 (line 32) — CF-01

Replace item 2 with:

> 2. Payment terms matter. A 30-year, node-delivered flat nominal contract breaks even near $66/MWh when 15.24% of potential energy is assumed unpaid (a stress setting, not a contract term); paying for all potential generation lowers this to $55.9/MWh. A separately versioned 10–15-year West-hub-settled hedge with a node merchant tail breaks even at $60.6–$84.8/MWh, depending mainly on the unsourced tail (Section 10.3). None of these is an observed contract offer.

Table 1-1:
- Row "Flat nominal break-even contract price" becomes: "Break-even, 30-yr node-level fixed-price route (15.24% unpaid; pre-tax, no credit)".
- Insert a new row: "HB_WEST hedge break-even strike, 10–15 yr | $60.6–84.8/MWh | Separate version; tail-dependent; 10.3".

Item 5: replace the last sentence with:

> A hub-settled contract leaves the seller with node-to-hub basis and needs its own settlement calculation (item 2; Section 10.3); switching benchmarks is not automatically an improvement.

Elsewhere: use the single label "simplified node-level fixed-price route" at lines 706 and 1325. Add "(see Section 10.3 for the hub-hedge range)" in §13.2 (line 1124) and in the Table 13-1 break-even row (line 1152).

*Sources:* `scenario-versions/data/VPPA-Breakeven-Strikes.csv`, 2025 path at 4.27%, minimum 60.57 and maximum 84.77.

### R-03 · Item 1 (line 28), Table 1-1 (line 45) and item 5 (line 32) — CF-02

- Item 1: change "earns $26.4/MWh on delivered electricity" to "is modelled to receive a gross $26.4/MWh on delivered electricity".
- Table 1-1 row label: change to "Modelled gross energy value per delivered MWh (before fees, losses, imbalance)".
- Item 5: after "$22.13/MWh", insert "(all potential output; $26.4 on exported output after the negative-price stop rule)".

### R-04 · Line 35 — CF-03

After "−$50.59m", insert:

> This is a pre-tax NPV plus one illustrative 30% credit received at end-2027, assuming eligibility; it is not an after-tax valuation.

### R-05 · §1.1 item 3 (line 30) — CF-05, CF-06

Append:

> From 4 December 2026, covered imported cells and modules face Proclamation 11052 minimum import prices ($0.22/W and $0.38/W) and, for most origins, an additional 15% ad valorem duty on top of continuing antidumping and countervailing duties; Commerce's 16 September 2026 final AD/CVD determinations for India, Indonesia and Laos await the ITC injury decision, and China ended export VAT rebates for listed PV products from 1 April 2026. These are compliance thresholds and potential duties, not delivered prices or any supplier's tariff outcome. [P01; Section 5.7; LONGi FY2025 annual report p.297]

At line 237, replace the citation of the unretrieved MOF page with the LONGi annual report p.297 locator. That page carries a post-balance-sheet note citing MOF/STA announcement 2026 No. 2.

### R-06 · "U.S. module input": lines 30, 371, 411, 979–980 and 1103 — CF-06

At first use (line 30, bold term), and replacing "including its stated subsidy treatment" at line 411:

> U.S. module input (DOE/NLR bottom-up U.S.-assembled module cost: about $0.29/Wdc (2024$) after the model's −$0.07/Wdc 45X subsidy, about $0.36/Wdc before it; not an imported-module or export price)

Use a short back-reference at lines 371, 979–980 and 1103. Do not state a derived "gap of $0.02 to the MIP".

*Sources:* `data/supplement/A/A_pvscm_item_level_pv_only.csv` (module items sum to 291.214 $/kWdc including the Subsidy line of −68.88).

### R-07 · Table 13-1 supplier-eligibility row (line 1148); reading path (line 17) — CF-07

Replace the "What this report shows" cell with:

> 40%/45% material-assistance cost ratio for 2026/2027 construction starts (share of manufactured-product cost not attributable to a prohibited foreign entity) plus ownership/control rules (10.8); the $35.38m illustration assumes eligibility and is not a supplier or product finding.

Then:
- Manufacturer reading path (line 17): "1, 4, 5, 10.8, 13.1".
- 13.1 question table, eligibility row: add "(see 10.8)".

### R-08 · Table 4-2 basis labels (lines 205–223) — CF-08

Do not change the values. Relabel the "Basis" column:
- Trina 4.6%: "industry line (光伏行业, incl. storage/systems)".
- JA −2.1%: "industry line (新能源行业)".
- Tongwei −1.12%: "PV business line".
- LONGi rows: "product line".

Add to the note:

> Module/cell product-line margins FY2025: Trina −1.42% (光伏产品), JA −4.03% (光伏组件), Tongwei −0.38% (cells, modules and related), LONGi 0.19%; LONGi industry line 0.81%.

*Sources:* retained 2025 annual reports in `closure-evidence/sources/cninfo/`.

### R-09 · Table 10-2 (lines 747–754, 774) — CF-09

- Column header: change to "First-year delivered (node) / paid (fixed) GWh".
- Note:

> Fixed-route LCOE uses paid energy as its denominator; Fixed base equals Node base because the 15.24% unpaid share was set equal to the node's negative-price energy share; the Fixed downside vs Node downside LCOE gap arises only from the denominator.

### R-10 · 2026 diagnostic sentence (line 1006) — CF-10

Replace the two context sentences with:

> As context only, from ERCOT's separate year-to-date West hub file (NP6-785-ER; it differs from the API series in 423 intervals): weighting January–September 2026 HB_WEST prices with the fixed 2025 simulated profile gives $18.24/MWh, against $21.36/MWh for January–September 2025 with that year's profile. West hub prices were negative in 14.1% of 2026 intervals versus 7.7% (23.6% vs 13.7% of the profile's energy); compare the reference node's full-year 2025 share of 6.2% (Section 8.2).

### R-11 · §1.3 (after line 62) — CF-11

Add (no numbers):

> Most 2025 intervals predate ERCOT's December 2025 real-time co-optimisation launch; a 2026 price diagnostic, not a forecast, is in Sections 10.3 and 11.8.

### R-12 · Table 13-1 capture-ratio cell (line 1149) — CF-12

Append:

> (near the 3rd percentile of the 2025 cross-section; HB_WEST about 65%)

### R-13 · Figure 11-3 caption (lines 946–948) — CF-13

Add:

> Left: median NPV across 485 settlement points; centre: TAYGETE2_ALL; right: share of points with positive NPV (not a probability). The colour bar applies to the NPV panels.

### R-14 · Reading navigation (lines 15–20) and §13.4 — CF-14

- New navigation row: "Buying electricity or hedges | 1, 6.2, 6.6, 8.1, 10.3, 11.3, 13.4, B.2, Appendix C".
- §13.4: add one sentence cross-referencing §10.3, the B.2 contract risk-allocation table and Appendix C. The question table is optional (see R-27).

### R-15 · Supplier cash caveat (line 276) and Table 4-3A note — CF-15

Add:

> For U.S.-listed filers the cash column excludes fixed-term deposits and short-term investments: Daqo also reports fixed-term deposits of $1,035.6m, and JinkoSolar restricted short-term investments of CNY3.30bn.

### R-16 · §5.7 after line 403; 13.1 question table — CF-16

Add:

> If CBP finds an importer's documentation materially inaccurate, the importer and its affiliates are permanently prohibited from importing polysilicon and derivatives (clause 3).

In the 13.1 question table, row "Who is responsible for customs entry and duties?", add "accuracy of MIP certification (clause 3 penalty)".

---

## P2 edits (apply in the same pass if convenient)

| ID | Location | Edit |
|---|---|---|
| R-17 (CF-17) | §1.3 limits box, line 66 | Add "(4) Output is simulated and not calibrated to operating plants (Section 9.5)." |
| R-18 (CF-18) | §8.4; Table 1-1 line 52; line 883 | §8.4: "Counts refer to settlement points; some share identical price series (about 400 distinct three-year receipt series among 485) and some are wind or storage resources; shares are not independent solar sites." Use "settlement points" in the Table 1-1 label. Line 883: "South 13 (10 distinct price series)". |
| R-19 (CF-19) | Line 533 | Add "The filing does not date the default or auction, so the event cannot be attributed to post-2023 operating prices at this node." |
| R-20 (CF-20) | Table 10-2, line 778, B.2 line 1319 | Fixed downside: "No root found (search not certified complete)". Note: "No root at or above 4.27% was found; NPV is negative at all three tested rates." |
| R-21 (CF-21) | Lines 798, 815, Table 10-3 | Line 815: "Excluded by convention (capital timing within the construction year not modelled)". Add a cost-year/dollar-year note to $24.66 vs $24.49. Under Table 10-3: "For construction starting after 4 July 2026 only the placed-in-service-by-2027 branch can apply." |
| R-22 (CF-22) | Figs 8-4, 10-2; §10.3/10.7 | Add the missing legend/clock and panel titles. Delete the duplicated hedge formula, J. Aron description and §25.195 passages (keep the first occurrence). |
| R-23 (CF-23) | Lines 31, 591, 595, 942–1020, 1088 | "Median node-level share", "median of node-level required weights"; calendar note in Fig 11-5/11-6 captions (tail and resampling use full calendars); "HB_BUSAVG hub prices"; "root-mean-square prediction error"; retitle 11.6 "…locate the model's sensitivity" and 11.7 "Model accounting assigns most of the change to the price setting"; Table 11-3 header "Comparison (baselines differ)"; line 1088 "the 485-point common-calendar panel". |
| R-24 (CF-24) | Lines 281/317, 405, 409, 726, 836, 1248 | Line 281: "short-term borrowings and current maturities of non-current liabilities (may include leases)". Line 405: the country arrangements concern the 15% duty only, not the MIP; the Secretary may adjust the MIP (clause 1(b)); on the face of the text China-origin covered goods are subject to the MIP program and the 15% duty (not a customs ruling). Line 409: "India, Indonesia and Laos supplied about 61.5% of January–August 2025 module import value versus about 12.6% in 2026 (modules only)"; add that Commerce made affirmative critical-circumstances findings in part. Line 726: "developer press release, 9 Dec 2020 (author-supplied screenshot); not an executed agreement". Line 836: "(RECAP record last refreshed 16 September 2026)". P02 bibliography: "vacated in full 6 June 2026 (F08; §10.8); history only". |
| R-25 (CF-25) | Lines 5, 33, 50, 254–256, 1150, Table 1-1 note, Table 13-1 | Footer and title line: "Candidate research edition" instead of "Closure-integrated candidate". Replace internal terms ("frozen", "panel calculations") in client text. Line 33 and Table 13-1: "a 238.6 GW total across all statuses, of which about 5.8 GW is observed energized". Fig 4-3 caption: "First Solar's margin includes about $1.6bn of Section 45X credits recognised in FY2025 cost of sales; not directly comparable". Table 1-1 note: "LCOE is real; the break-even price is flat nominal; the two are not directly comparable". Table 13-1 WLPUN cell: "11 WLPUN projects; power capacity, not energy; not a census". Table 1-1 module-share row: "of the PV-only benchmark (about 23% of total scenario CAPEX)". |
| R-26 | §1.3, F-03 | No separate edit (covered by R-17). |
| R-27 (optional) | §13.4 | A PPA/VPPA question table restating only fields already defined in §10.3, B.2 and Appendix C, with no indicative market terms. |

## Not to be changed

- **Disclosed limitations:** the CF-26 items stay as written and are not to be converted into research tasks.
- **Optional future scope:** the CF-27 items are not part of this round.
- **Fixed inputs:** the six baseline scenarios, Tables 10-4 and 10-5 values, the empirical estimates, the 4.27% convention, Appendix C's undisclosed-fields table, and the candidate status.
