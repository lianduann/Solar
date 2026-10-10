# Expert C — Econometrics and Research Methods: Independent First-Round Review

**Report reviewed:** SOLAR-001, *From China's Solar Supply Chain to U.S. Power Markets*, closure-integrated candidate edition, 9 October 2026 (73 physical PDF pages).
**Reviewer role:** Expert C (econometrics and research methods). Independent first round; no other reviewer output was opened.
**Review date:** 10 October 2026.
**Standard applied:** Review brief §4 (product boundary) and §6 (severity and verdict criteria), as summarised in the common fact pack.

## 1. Scope and method

I reviewed how the frozen results are interpreted. I did not re-estimate any regression, simulation, decomposition or resampling. Where I checked a number against a frozen table, the check was a lookup or simple arithmetic, labelled "reviewer arithmetic".

Focus areas:
- the boundaries between conditional association, causal language and forecasting;
- sample definitions (485 / 641 / 757);
- calendars (common vs full, leap day, DST);
- Shapley and LMDI accounting;
- tail stresses;
- block resampling and the equal-weight mixture;
- the three-year repetition;
- the regression and out-of-sample statements.

**Files actually read:**
- **Report text.** The Markdown with line numbers, Ch. 1–2, 7–12 and 14 plus App. B–C in full, and the matching PDF text by page. I viewed PDF p. 52 as an image.
- **Figures** (in `figures/` of the evidence package): F2, F4, F5, F6, F7, F8, Panel_Mean_Decomposition and S07_node_prices.
- **Frozen tables** (in `data/empirical/` and `data/empirical/tables/`):
  - `T_A1_weather_by_price_matrix_summary.csv`, `T_A2_decomposition_strict_nodes.csv`, `T_C1_tail_summary_strict_nodes.csv`;
  - `B3_basis_persistence.csv`, `B3_basis_summary.json`;
  - `B_out_of_sample_2025.csv`, `B_solar_effect_sizes.csv`;
  - `Common-Sample-Counts.csv`, `Sample-Flow-By-Year.csv`, `R2-757-By-Type-And-Identity.csv`;
  - `C_block_bootstrap_within_year.csv`, `C_three_year_mixture_scenario_by_node.csv`.
- **Panel tables** (in `data/panel/`): `Mean-Decomposition.csv`, `Required-High-Year-Share.csv`, `Tail-Stress-Summary.csv`, `Positive-Node-Zones.csv`, `Coverage-Cohort-Comparison-2025.csv`.
- **2025 cross-section facts:** `data/supplement/B/B_distribution_facts_2025.json`.
- **Scenario versions:** `scenario-versions/data/CPI-Harmonised-Scenario.csv`, `HB_WEST-2026-JanSep-Post-RTCB-Context.csv` and `scenario-versions/scripts/10_hb_west_2026_context.py`.
- **Closure evidence:** `closure-evidence/tables/FIN-08_2026-Price-Coverage-Summary.csv` and `closure-evidence/Numbers-and-Claims.csv` (rows N27–N28).

All paths above are relative to the extracted evidence package root, `.../scratchpad/review/2026-10-09_Closure-Integrated-Client-Edition/`.

## 2. Spot checks that passed (no change needed)

These checks found no problem; they are recorded so that the coordinator does not re-open them.

| Area | Check | Result |
|---|---|---|
| Affine NPV identity (10.9, B.2) | 15.47 × receipts − 187.3 against Table 10-4: 18.56 → +99.8; 6.83 → −81.6; 6.85 → −81.3; threshold 187.3/15.47 = 12.1 (reviewer arithmetic) | Consistent |
| Same-year positive shares | 13/485 = 2.68%; 2/485 = 0.41%; `T_A1` and `C_three_year_mixture...` give 13 and 2 | Consistent |
| Top-1% tail stress | `T_C1`: 2023 median share 0.547, stress-positive share 0.00619 (3 nodes), so 482 negative (99.4%); stress median −56.6m; p99 cap −10.6m; p99.9 cap +98.25m; ≥$1,000 dates −82.5m; 2024/2025 shares 13.6% / 4.9% | Consistent |
| Shapley 2023→2024 (11.7) | `Mean-Decomposition.csv`: price −174.68m, weather −4.63m, total −179.31m; 97% / 3% | Consistent |
| LMDI Table 11-2 | Rows add to totals (2024→2025: 0.42 + 17.74 − 18.13 + 1.21 = 1.24 vs 1.23, rounding); the transitions chain (−179.31 + 1.23 = −178.08) | Consistent |
| Mixture (11.9) | 485 strict nodes: median mixture NPV −21.39m, 12.16% positive. The median of node-level required 2023 weight is 0.449; TAYGETE2_ALL is 0.477 | Consistent |
| Block resampling (11.9) | TAYGETE2_ALL 2023 5th percentile: +24.6m (1-day blocks), −1.4m (7-day), −72.0m (28-day). "Change materially with block length" is supported. The share of positive draws is not reported in the text, which is correct | Consistent |
| Regression range (8.6) | HB_BUSAVG S1/S2/S3 = −3.83 / −2.66 / −3.30 → "−2.7 to −3.8"; 2023 −8.39 ("stronger"); winsorised −2.53 and ≥$1,000-excluded −2.38 ("weaker") | Consistent |
| Out-of-sample (8.7) | RMSE 65.99 / 44.86 / 38.76 → "$66 / $45 / $39" | Consistent (see C-06 on labelling) |
| Basis persistence (8.8) | Spearman 0.767 / 0.822 / 0.882; variance shares 83.4 / 0.4 / 16.2; n = 485 | Consistent |
| Reference-node percentiles (1.3, 8.5) | 641-node file: weighted-price percentile 0.374; capture-ratio percentile 0.034 | Consistent |
| 485 / 641 / 757 separation | 641 is used only for the 2025 cross-section (8.5, Fig 8-3, Table B-1: 156 + 485 = 641). 757 does not appear in the report text. `R2-757-By-Type-And-Identity.csv` shows that 757 counts all non-benchmark points (LCCRN/PCCRN/PUN included), so it is not mixed with the RN samples | No mixing found |
| Calendar disclosure (B.1, 10.9 l. 881) | Full- vs common-calendar reference NPV (2024: −91.84 vs −92.15) and the CPI file's full-calendar 2024 median are disclosed | Adequate |
| CPI non-harmonisation | Stated in Table 8-1 note, 10.9 "Currency qualification", B.2, plus a separately versioned CPI restatement | Adequate |
| Causal boundaries | 7.4, 8.3, 8.6–8.8, 11.7, 11.8 (RTC+B), 12.2/12.4, 14.4 and B.3 consistently describe results as association or accounting, not cause | Adequate |
| Three-year repetition | Box 1, 1.3, 10.9, 11.5, 14.4 and C state that it is a stress or condition setting, not a forecast or an expected return | Adequate |

## 3. Findings

### Summary table

| ID | Severity | PDF p. | MD line(s) | Problem | Changes a number? |
|---|---|---|---|---|---|
| C-01 | P1 | 52 | 946–948 | Fig 11-3 has three unlabelled panels (485-node median, reference node, positive share); the caption does not identify them | N |
| C-02 | P1 | 55, 72 | 1000–1006, 1394 | The 2026 West-hub diagnostic comes from the NP6-785-ER hub file, not the API product the bullets describe; the 14.1% / 7.7% negative share does not name its location | N |
| C-03 | P1 | 3, 4, 32, 47–48, 67 | 31, 52, 579, 848–856, 883, 1293 | The "485 nodes" are settlement points, not 485 distinct price locations: 144 points fall in 58 groups with identical three-year receipts, leaving 400 distinct patterns | N |
| C-04 | P2 | 3, 54, 56 | 31, 988, 1020 | "54.7% of median modeled receipts" and "the median node needs 44.9%" are medians of node-level ratios, not ratios for a median node | N |
| C-05 | P2 | 54–56, 67 | 990–996, 1014–1018, 1295 | Tail-stress and resampling outputs appear to use per-year (full) calendars while the matrix and mixture use the common calendar; 11.8–11.9 and Figs 11-5/11-6 carry no calendar label | N |
| C-06 | P2 | 32–33 | 591, 595 | The 8.6 range is for HB_BUSAVG only, but the text says "benchmark prices"; the 8.7 "prediction error" metric (RMSE) is not named | N |
| C-07 | P2 | 52, 54 | 942, 952, 976 | The headings "reveal the source" and "The change comes mainly from the price setting", and the Table 11-3 column header "Controlled comparison", read more strongly than the accounting allows | N |
| C-08 | P2 | 59 | 1088 | "Node basis persists in the corrected panel": "corrected" is unexplained in the client text | N |
| C-09 | P2 | 33 | 597–599 | Fig 8-4 left panel shows unlabelled dotted "×" series; the hour axis does not state which clock it uses | N |
| C-10 | Disclosed limitation | 47, 67, 69 | 858, 1293, 1339, 1379 | Unharmonised historical price levels, survivorship in the coverage screen, no causal design and only three regime years are all disclosed | N |
| C-11 | Optional future scope | — | — | A de-duplicated (distinct price series) robustness count for the node shares; storage-only resource nodes flagged separately | N |

### C-01 — Figure 11-3 panels are not identified (P1)

- **Location:** PDF p. 52; MD §11.6, lines 946–948.
- **Quote:** "*Figure 11-3. Weather-year and price-year scenario matrix* … The common-calendar matrix is not a probability distribution or a price forecast."
- **Problem:** The figure shows three 3×3 panels with no panel titles:
  - left: the median NPV across 485 nodes (100 / −82 / −81 diagonal);
  - middle: the TAYGETE2_ALL reference node (98 / −92 / −86);
  - right: the share of the 485 nodes with positive NPV.
  
  The NPV colour bar sits between the middle panel and the share panel, as if it belonged to the share panel. Neither the caption nor the text says which panel is which. The text below the figure discusses only the "median".
- **Evidence:** PDF p. 52 viewed as an image. Panel values match `data/empirical/tables/T_A1_weather_by_price_matrix_summary.csv` rows "strict resource nodes (median)" and "TAYGETE2_ALL (single node)".
- **Client consequence:** A developer can read the middle panel as a second median, or the right panel's percentages as NPV-scaled or probability-like. This mixes a single-reference-node result with a sample statistic, which the report elsewhere keeps separate (for example, the Fig 11-5 caption).
- **Minimal fix:** Add panel titles to the figure, or append to the caption: "Left: median NPV across 485 screened nodes, $m. Centre: reference node TAYGETE2_ALL, $m. Right: share of the 485 nodes with positive NPV (a sample share, not a probability); the colour bar applies to the two NPV panels."
- **Changes number:** N. **Confidence:** High. **In scope:** Y.

### C-02 — The 2026 post-RTC+B diagnostic is attributed to the wrong data product, and its location is unnamed (P1)

- **Location:** PDF p. 55 (also p. 72); MD §11.8, lines 1000–1006 and 1394.
- **Quote:** "Real-time settlement-point prices for 2026 were obtained from ERCOT's public API … Negative prices occur in 14.1% of 2026 intervals, against 7.7% in the 2025 months."
- **Problem 1 (data product):** The paragraph describes the API product, including 125 system-wide missing intervals on 11 days, unverified finality, and 423 West-hub differences from "ERCOT's separate year-to-date hub file". It then gives the West-hub diagnostic ($18.24 vs $21.36; 14.1% vs 7.7%) as if it came from that API product. It did not: the script states that the diagnostic is computed from the **NP6-785-ER 2026 year-to-date hub file**, which is the comparator in the 423-interval cross-check. Consistent with this:
  - the context file has 26,204 Jan–Sep 2026 intervals;
  - 26,208 − 26,204 = 4 missing (reviewer arithmetic);
  - but FIN-08 places all 11 system-wide gap days, 125 intervals in total, between January and 7 September.
- **Problem 2 (location):** The 14.1% / 7.7% sentence does not name its settlement point (HB_WEST). The nearest comparable figure in the report is the reference node's 2025 full-year 6.2% (§8.2).
- **Evidence:**
  - `scenario-versions/scripts/10_hb_west_2026_context.py`, docstring: "HB_WEST 15-minute RTM prices January-September 2026 (ERCOT NP6-785-ER 2026 year-to-date file …)";
  - `scenario-versions/data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv`, row Jan-Sep 2026: intervals 26,204, negative share 0.1412;
  - `closure-evidence/tables/FIN-08_2026-Price-Coverage-Summary.csv`, the 11 dates;
  - `closure-evidence/Numbers-and-Claims.csv`, N27–N28 ("HB_WEST").
- **Client consequence:** The reader cannot tell that the diagnostic rests on the file whose differences from the API remain unexplained. The reader may also compare the 14.1% hub share with the 6.2% node share.
- **Minimal fix:** Replace the sentences after "As context only:" with: "As context only, using ERCOT's NP6-785-ER year-to-date hub file (which differs from the API series in 423 West-hub intervals; see above): weighting January–September 2026 West hub prices with the 2025 simulated output profile gives $18.24/MWh, against $21.36/MWh for the same months of 2025 from the 2023–2025 archive. West hub prices are negative in 14.1% of those 2026 intervals, against 7.7% in the same 2025 months."
- **Changes number:** N. **Confidence:** High for the source; I could not verify the exact gap-handling of the hub file. **In scope:** Y.

### C-03 — "485 nodes" are settlement points, many with identical price outcomes (P1)

- **Location:** PDF pp. 3, 4, 32, 47–48, 67; MD lines 31, 52, 579, 848–856, 883, 1293.
- **Quote:** "Repeating 2023 conditions yields positive NPV at all 485 rule-screened nodes, versus 13 in 2024 and two in 2025."
- **Problem:** All sample shares count settlement points. These include the headline 13/485 and 2/485, the 12.2% mixture share, the 99.4% tail result and the persistence statistics. Many points in the 485 are not distinct price outcomes. In the frozen mixture file, only 400 distinct first-year receipt triplets (2023, 2024, 2025) exist among the 485 strict nodes (reviewer arithmetic: exact match on all three years). Examples:
  - TAYGETE2_ALL equals TAYGETE_ALL;
  - FAL_FALCONG1/2/3 are identical;
  - BRP_ZPT1_RN and BRP_ZPT2_RN are identical.
  
  The 13 positive 2024 points form **10 distinct** receipt series. Separately, the sample is "RN-type", so it includes wind and storage resource nodes; for example, RHESS2_ESS1 (an ESS resource node) is one of the two positive 2025 points. §8.4 states that one solar profile is priced at every node, but nowhere says that points can duplicate one another's prices.
- **Evidence:** `data/empirical/C_three_year_mixture_scenario_by_node.csv` (tier = strict, n = 485); `data/panel/Required-High-Year-Share.csv` (TAYGETE_ALL and TAYGETE2_ALL identical).
- **Client consequence:** A reader may treat "13 of 485" or "12.2%" as the share of independent ERCOT locations, or of solar sites. That overstates the effective sample breadth and the geographic spread of positive cases. All 13 positive points are in LZ_SOUTH, and they reduce to 10 distinct series. This remains a non-probability description in any case.
- **Minimal fix:** Add to §8.4 after "One simulated output profile is valued against all nodes.": "Counts refer to settlement points. Some points share identical price series (about 400 distinct three-year receipt patterns among the 485), and the RN list includes non-solar resources such as wind and storage. Shares therefore describe screened settlement points, not independent locations or solar sites." Optionally add "(10 distinct price series)" after "South 13" at line 883.
- **Changes number:** N. **Confidence:** Medium-High. The receipts match to the cent; I infer identical prices but did not open the price panel. **In scope:** Y.

### C-04 — Medians of node-level ratios are described as ratios of a median (P2)

- **Location:** PDF pp. 3, 54, 56; MD lines 31, 988, 1020.
- **Quotes:**
  - line 31: "contribute 54.7% of median modeled receipts";
  - line 988: "generate 54.7% of the median node's modeled receipts";
  - line 1020: "the median node needs approximately 44.9%".
- **Problem:** 0.547 is the median, across 485 nodes, of each node's own top-1% share. It is not the share for the median-receipt node, and not a share of the median receipts. Likewise, 0.449 is the median of node-level required weights, which range from −0.59 to 0.93.
- **Evidence:** `T_C1_tail_summary_strict_nodes.csv`, column `share_Rcurt_median` (0.547353); `Required-High-Year-Share.csv`, median 0.449 (reviewer arithmetic).
- **Client consequence:** A small imprecision. A careful reader cannot reproduce the statistic from the described definition.
- **Minimal fix:**
  - Line 31: "…contribute a median node-level share of 54.7% of modeled receipts…".
  - Line 988: "…generate a median of 54.7% of each node's modeled receipts…".
  - Line 1020: "the median of node-level required weights is approximately 44.9%; the reference node requires 47.7%".
- **Changes number:** N. **Confidence:** High. **In scope:** Y.

### C-05 — Calendar basis of the tail-stress and resampling outputs is unlabelled (P2)

- **Location:** PDF pp. 54–56, 67; MD lines 990–996, 1014–1018 and 1295.
- **Quote (B.1, line 1295):** "Common-calendar results are labeled throughout the comparison tables."
- **Problem:** The frozen tail and bootstrap outputs reproduce the full-year NPVs, not the common-calendar NPVs:
  - TAYGETE2_ALL 2024 bootstrap point = −91.84m, the full-year value in B.1; the common-calendar value is −92.15m;
  - `T_C1` 2024 raw median = −81.33m, against −81.59m common.
  
  The matrix, Table 10-4 and the mixture use the common calendar. Sections 11.8–11.9 and Figs 11-5/11-6 do not state their calendar. The quoted 2023 values are identical on both bases, so no reported number is wrong.
- **Evidence:**
  - `C_block_bootstrap_within_year.csv`, row TAYGETE2_ALL 2024, `npv_point`;
  - `T_C1_tail_summary_strict_nodes.csv`, 2024 `npv_raw_median`;
  - `C_three_year_mixture_scenario_by_node.csv`, strict 2024 median −81.59m (reviewer arithmetic);
  - report B.1, line 1295.
- **Client consequence:** Minor. A methods reader comparing Fig 11-5 or 11-6 bars with Table 10-4 sees small unexplained differences.
- **Minimal fix:** Add to the Fig 11-5 and Fig 11-6 captions: "Tail-stress and resampling outputs use each year's own full calendar; the matrix and mixture use the common calendar (Appendix B.1). The 2023 values are identical on both bases." I could not verify the calendar basis beyond these matching values.
- **Changes number:** N. **Confidence:** Medium. **In scope:** Y.

### C-06 — Regression benchmark and error metric not named in the main text (P2)

- **Location:** PDF pp. 32–33; MD lines 591 and 595.
- **Quotes:** "higher system solar output is associated with lower benchmark prices … approximately −$2.7 to −$3.8/MWh per additional GW" and "approximately $66/MWh prediction error".
- **Problem:** The range applies to HB_BUSAVG only. For the same specifications, HB_WEST and TAYGETE2_ALL coefficients are larger in magnitude (S1: −4.13 and −4.72). The 8.7 error metric is RMSE; MAE gives 46 / 22 / 19, with the same ranking.
- **Evidence:** `B_solar_effect_sizes.csv`; `B_out_of_sample_2025.csv`; Fig B-1 subtitle "Hourly HB_BUSAVG price".
- **Client consequence:** A reader may apply the HB_BUSAVG range to the reference node or the West hub. It may also be unclear what the "$66" error measures.
- **Minimal fix:**
  - Line 591: "…lower **HB_BUSAVG hub** prices… (other benchmarks in the technical tables show larger magnitudes)".
  - Line 595: "…approximately $66/MWh **root-mean-square** prediction error…".
- **Changes number:** N. **Confidence:** High. **In scope:** Y.

### C-07 — Headings and one table header read more strongly than the accounting allows (P2)

- **Location:** PDF pp. 52 and 54; MD lines 942, 952 and 976.
- **Quotes:** "Crossed weather and price years reveal the source of model sensitivity"; "The change comes mainly from the price setting"; Table 11-3 column "Controlled comparison".
- **Problem:** The body text correctly calls the Shapley and LMDI splits "model accounting, not an explanation". The headings, however, use source and attribution language. Row 1 of Table 11-3 also changes both weather and prices and is a mean across 485 nodes, so the column label "Controlled comparison" does not fit it.
- **Client consequence:** A skimming reader may take the headings as a causal finding about why prices changed.
- **Minimal fix:**
  - 11.6 heading: "Crossed weather and price years locate the model's sensitivity".
  - 11.7 heading: "Model accounting assigns most of the change to the price setting".
  - Table 11-3 header: "Comparison (baselines differ)".
- **Changes number:** N. **Confidence:** Medium. **In scope:** Y.

### C-08 — "Corrected panel" is unexplained (P2)

- **Location:** PDF p. 59; MD line 1088 (Table 12-1).
- **Quote:** "Node basis persists in the corrected panel".
- **Problem:** The client text never says what was corrected; the earlier 757-sample correction does not appear in this report. The phrase invites a question about a previously erroneous sample without giving the answer.
- **Minimal fix:** "Node basis persists in the 485-node common-calendar panel".
- **Changes number:** N. **Confidence:** High. **In scope:** Y.

### C-09 — Figure 8-4 legend is incomplete (P2)

- **Location:** PDF p. 33; MD lines 597–599.
- **Problem:** The left panel draws a second set of dotted "×" series per year with no legend entry; they are presumably medians, but I could not verify this. The right panel's "Local hour of day" does not state whether it uses the civil clock or the fixed UTC−6 key; §7 and B.1 use both conventions.
- **Minimal fix:** Add to the caption: "Dotted × markers: [statistic, e.g. bin medians]. Hours are on the [America/Chicago civil / fixed UTC−6] clock."
- **Changes number:** N. **Confidence:** Medium. **In scope:** Y.

### C-10 — Disclosed limitations (no action required)

Each of the following is already stated and sits within the brief's §4 boundary. None should be escalated.
- **Unharmonised price levels:** 2023 and 2024 nominal price levels are reused as constant-real 2025 values; a separately versioned CPI restatement is provided (10.9, lines 858 and 874–881).
- **Coverage-screen survivorship:** the coverage screen favours continuously observed points (B.1, line 1293; Table B-1).
- **No causal design:** there is no instrument or natural experiment; simultaneity and omitted variables remain (B.3, lines 1335 and 1339).
- **Three years of regimes:** three years give no recurrence probability or P50/P90 (lines 1008 and 1379).
- **2026 data:** finality is not verified row by row, and the 2026 figures are a diagnostic, not a capture price (lines 1003 and 1006).

### C-11 — Optional future scope

Not required for this edition: a robustness line reporting the node shares on distinct price series, and the RN sample restricted to solar-type resources. This would strengthen C-03 but is not needed for the stated screening use.

## 4. Overall assessment

The report is careful about methods. Its main inferential boundaries are stated consistently in Box 1, the chapter limit boxes, Appendix B and the headline text:
- association vs cause;
- accounting vs explanation;
- stress vs forecast;
- sample shares vs probabilities.

Every quantitative statement I spot-checked against the frozen tables reproduced (Section 2). I found no supported factual, arithmetic or unit error and no core misleading claim. The 485 / 641 / 757 samples are not mixed.

The remaining issues are label and navigation problems that existing materials can fix:
- one unlabelled multi-panel figure (C-01);
- one diagnostic attributed to the wrong data product (C-02);
- one missing sample qualifier (C-03);
- several P2 wording fixes.

None changes a number.

**Verdict: ② Handover-ready for the stated use after the listed minimal edits (C-01 to C-03 as P1; C-04 to C-09 optional P2).**

This verdict is not a publication authorisation and not Version 1.0 acceptance.
