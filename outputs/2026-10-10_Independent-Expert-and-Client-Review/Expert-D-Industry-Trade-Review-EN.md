# Expert D — Industry, Trade Policy and Evidence Presentation: Independent First-Round Review

**Report reviewed:** SOLAR-001, *From China's Solar Supply Chain to U.S. Power Markets*, closure-integrated candidate edition, 9 October 2026 (73-page PDF + Markdown).
**Reviewer role:** Expert D (solar industry, trade policy, evidence presentation). Independent first round. I have not read any other reviewer's output.
**Review date:** 10 October 2026.
**Standard applied:** Review brief §4 (product boundary) and §6 (severity/verdict). This is not legal or tax advice. Where the latest docket or agency status is not in a retained original, I say so and do not treat it as known.

## 1. Scope and method

I judged statements only against retained originals and clearly cited sources in the package:

- **Trade:** `closure-evidence/sources/trade/FR-2026-16400.pdf` (Proclamation 11052, text and Annex I/II page images, pp. 51975–51987), plus `FR-2026-18939/18941/18945/18947.json`, `FR-search-cspv-2026.json` and `FR-search-usitc.json`.
- **Census import data:** `data/r2/A/A_census_hs854143_by_country.csv` and `A_census_hs8541430010_*.csv`.
- **Tax:** `sources/finance/tax/PLAW-119publ21.pdf`, `USCOURTS-dcd-1_25-cv-04400-0.pdf` and `n-26-15.pdf`, plus `closure-evidence/sources/legal/CourtListener_RECAP_docket_…_retrieved_2026-10-10.html`.
- **Companies:** `closure-evidence/sources/cninfo/*_2025_AR.txt/pdf`, `closure-evidence/sources/sec/*.txt`, `closure-evidence/tables/FIN-09_Supplier-Liquidity.csv` and `Numbers-and-Claims.csv`.
- **Cost model:** `data/supplement/A/A_pvscm_item_level_pv_only.csv`, `A_cost_components_pvscm_2025Q1_pv_only.csv`, `A_module_passthrough_parameters.csv` and `A_cost_basis_crosswalk.csv`.
- **Capacity and output:** `data/irena_pv.csv` and `data/miit_2024_observations.csv`.
- **Contract evidence:** `closure-evidence/sources/other/BusinessWire_2020-12-09_7X-Nestle-Taygete-I_author-screenshot.jpg` and `closure-evidence/Sources.csv`.

I reran no models and fetched nothing from the web. All derived figures below are labelled "reviewer arithmetic".

## 2. Areas checked and found correct (no change needed)

| Area | Report location | Check against retained original | Result |
|---|---|---|---|
| Proclamation 11052 core terms | §5.7, L398–405, p.21 | FR 91 FR 51975. Signed 6 Aug 2026, published 11 Aug 2026. Clause 1(a): $21/kg, $100/kg, $0.22/W, $0.38/W. Clause 2: 12:01 a.m. ET, 4 Dec 2026. Clause 2(a): certification of the first arm's-length sale at or above the MIP, or fixed terms in a pre-signing contract. 2(b): specific tariff equal to the full MIP. 2(c): specific tariff equal to the shortfall between entered value and MIP. Clause 4: +15% ad valorem. 5(a): duties are additional. 5(b): combined 15% for JP/KR/TW/CH/LI/EU. 5(c): UK 10% | Correct |
| Annex HTS and Annex II wording | L398, L401 | Annex I (p.51982–83): modules 8541.43.0010/.0080, cells 8541.42.0010/.0080. Annex II note 42(a)(3): "time-limited contract entered into prior to August 6, 2026". Note 42(b) (p.51985): "antidumping, countervailing or other duties … shall continue to be imposed". Headings 9903.45.30–.36 | Correct. The note in `Sources.csv` (LEAD-232-SECONDARY) that withdrew an earlier round's error about the shortfall tariff is borne out by clause 2(c) |
| AD/CVD India/Indonesia/Laos | L409, p.21 | Four FR JSONs dated 16 Sep 2026 (91 FR 58633, 58643, 58651, 58658). Search file lists six AD/CVD finals. USITC FR search finds no final injury notice | Correct and properly hedged. "Duty orders require … ITC" is stated as a condition, not a status |
| P.L. 119-21 timing branches | Table 10-3, L830–834, p.46 | §§70512(e)(4), 70513(e)(5): amendments apply to facilities "the construction of which begins after the date which is 12 months after the date of enactment" (enacted 4 Jul 2025). Applicable facilities lose the credit if placed in service after 31 Dec 2027 | Correct |
| Material-assistance thresholds | L838, L842 | §7701(a)(52)(B)(i): 40% for a 2026 construction start, 45% for 2027 (qualified facilities) | Correct. The wording "not percentages of module origin" is appropriately careful |
| Notice 2025-42 vacatur | L836, p.46 | Opinion p.1: "may decide the claims of five of the seven Plaintiffs … vacate the Notice in full and remand". RECAP: Date Terminated 8 Jun 2026; last known filing 6 Jun 2026 | Correct. Appeal status is properly *not* asserted as known (see D-09 for a small precision point) |
| Business Wire release content | L718, L724, L726, L1383, pp.39–40, 63 | Screenshot: J. Aron long-term hedge for "a portion of the energy". Other purchaser is S&P A– rated. Nestlé is sole tax-equity investor and buys 100% of renewable electricity attributes, about 750,000 MWh/yr, for 15 years. Lenders and Marathon Capital match | Correct. The report keeps the 15-year attribute tenor separate from energy-hedge terms and calls the source a developer statement (see D-07 for labelling) |
| Manufacturing vs installation | §3.2–3.3, §4.1, L141–165, L182 | IRENA: 1,872.813 − 1,415.161 = 457.65 GW (2024). 2,383.162 − 1,872.813 = 510.35 GW (2025). China 314.24 GW = 61.6%. MIIT 588 GW − 457.7 = 130.3 GW (reviewer arithmetic) | Correct. The report explicitly refuses an inventory or overcapacity reading. This is exemplary |
| LONGi FY2025 rows | L220–221, L274, Table 4-3A/B | LONGi AR: revenue 70,347,049,950 (−14.82%), OCF 4,359,382,756 (FY2024 −4,724,978,932), LLA cash 5,893,972,740 (8,013,068,272), module & cell 0.19% (−6.08pp), wafer & ingot −5.30% (+9.01pp) (p.25). Loss CNY6.42bn, with the FY2024 loss reduced by 2.173bn, giving 8.59bn | Correct |
| Tables 4-3A/B values | L289–311 | FIN-09 rows for all eight companies. NWC recomputed: LONGi 91.058 − 70.544 = 20.51; Trina 70.599 − 58.902 = 11.70. CSIQ restricted cash 0.542 + 0.028 = 0.57 | Correct |
| First Solar 45X; JinkoSolar warranty reversal | L283, L285 | fslr 10-K: "$1.6 billion of Section 45X credits as a reduction to 'Cost of sales'". jks 20-F warranty roll-forward: reversal (1,132,838) thousand, giving CNY1.13bn | Correct (the 20-F narrative elsewhere says RMB1,141m; the report uses the note table) |
| Table 5-1 arithmetic | L381–392 | 0.26111 × 1.144 = 0.2987. 126.04 × 0.02987 = 3.765. Zero-module case 126.04 × 0.2987 = 37.65. −48.32 − 37.65 ≈ −85.97, consistent with −86.0 base. Credit interaction: 3.765 × (1 − 0.30 × 35.38/37.81) ≈ 2.71 (reviewer arithmetic) | Consistent |
| Census import values | L415–419 | Totals implied by country value ÷ share: 2024 FY 14.415; Jan–Aug 11.642 / 4.435 / 2.817 $bn | Consistent |

## 3. Findings

### D-01 — P1 — The $0.29/Wdc benchmark module line is net of a 45X subsidy deduction, but the report does not say so plainly

- **PDF pages:** 19, 21; also 49–50 (Table 13-1 / §13.1 reuse). **MD:** §5.5 L363–371; §5.7 L411; §13.1 L1103.
- **Quote:** "the benchmark uses a U.S.-assembled module input including its stated subsidy treatment, while the rule applies to covered imported products." (L411)
- **Problem:** The PVSCM 2025Q1 module line ($291.21/kWdc MMP, 2024$) is a bottom-up cost for U.S.-assembled modules. It includes a **Subsidy item of −$68.88/kWdc** and module profit of $89.89/kWdc. Gross of the subsidy, the module line is about **$360.09/kWdc ($0.360/Wdc)** (reviewer arithmetic, summing the module items). Neither Figure 5-1 ("Module $0.291") nor §5.5 says this. §5.7 says only "including its stated subsidy treatment". The headline contrast "$0.29/Wdc vs $0.38/W" therefore compares a net-of-45X domestic cost (2024$) with a nominal 2026 import price floor. On a gross-of-subsidy basis the gap is about $0.02/W, not about $0.09/W, before any dollar-year or denominator adjustment.
- **Evidence:**
  - `data/supplement/A/A_pvscm_item_level_pv_only.csv` row "Module,Subsidy,I,0,kWdc,0,-68.88,0,-68.88". The module items sum to 291.214 net and 360.094 without the subsidy row.
  - `A_module_passthrough_parameters.csv`: "US-assembled benchmark module cost element incl. 45X subsidy; not a Chinese-origin delivered module".
  - `A_cost_basis_crosswalk.csv`: "benchmark system US-assembled modules".
- **Client consequence:** A manufacturer or exporter could read the MIP as sitting about 30% above U.S. benchmark module cost and infer a large compliance-price penalty or opportunity. A developer could read the 26.1% module share and the 10% sensitivity as describing an imported delivered module. Both readings misstate the mechanism the report is trying to bound.
- **Minimal fix:**
  - L411: replace "including its stated subsidy treatment" with "net of a modeled −$0.069/Wdc section 45X subsidy (about $0.36/Wdc before that subsidy, 2024 dollars)".
  - Figure 5-1 caption: add "Module line is a U.S.-assembled bottom-up cost net of the model's 45X subsidy item."
  - L1103: add "(net of 45X; 2024 dollars)" after "$0.29/Wdc".
- **Changes an existing number?** N (adds a disclosed component from existing data). **Confidence:** High. **In scope?** Y.

### D-02 — P1 — Table 4-2 mixes A-share "industry" margins with LONGi "product" margins under one "Segment margin" label

- **PDF page:** 12. **MD:** §4.2 Table 4-2 L215–221; note L223.
- **Quote:** "Trina | Integrated PV | 2025 | 4.6% … Segment margin" / "LONGi | Modules/cells | 2025 | 0.19% …"
- **Problem:** The A-share rows use the broad *by-industry* (分行业) line. The LONGi rows use *by-product* (分产品) lines. These are different levels of aggregation:
  - **Trina 4.60%** is 光伏行业 (CNY64.5bn). It includes storage at 14.69%, system solutions at 11.66% and digital-energy services at 55.69%. Trina's own **PV products** line is **−1.42%** (Trina AR p.45).
  - **JA −2.10%** is 新能源行业, i.e. essentially all revenue (CNY49.13bn). JA **PV modules** are **−4.03%** (JA AR p.21).
  - **Tongwei −1.12%** is 光伏业务. Its **cells, modules and related** line is **−0.38%** and polysilicon is **−5.38%** (Tongwei AR p.21).
  - LONGi's comparable *industry* line is **0.81%**, while the table shows the product lines 0.19% and −5.30% (LONGi AR p.25).
  - The two LONGi rows also carry different basis labels for identical group figures ("Segment margin; LLA cash" vs "Segment margin; group result and cash").
- **Evidence:** `closure-evidence/sources/cninfo/Trina_2025_AR.txt` (分行业/分产品 table, PDF p.45), `JASolar_2025_AR.txt` (p.21), `Tongwei_2025_AR.txt` (p.21) and `LONGi_2025_AR.txt` (p.25). Page numbers are from form-feed counts; for LONGi this matches `Numbers-and-Claims.csv` N46 "p.25".
- **Client consequence:** The text says this is not a ranking, but a procurement reader scanning the margin column sees Trina (4.6%) as the healthiest module maker and LONGi's module business (0.19%) as weaker. On a like-for-like module-product basis the order is LONGi 0.19% > Tongwei −0.38% > Trina −1.42% > JA −4.03%. This is exactly the cross-company basis conflation the brief (§4) prohibits.
- **Minimal fix (choose one):**
  - (a) Relabel the A-share Basis cells "Industry-line margin (分行业), includes non-module businesses" and the LONGi cells "Product-line margin (分产品)". Add to L223: "LONGi's industry-line margin is 0.81%; product-line module margins are Trina −1.42%, JA −4.03%, Tongwei cells/modules −0.38% (FY2025 AR pp.45, 21, 21)."
  - (b) Show product-line margins for all four companies.
  - In either case, harmonize the LONGi basis label to "Segment margin; group result, OCF and LLA cash (not additive)".
- **Changes an existing number?** N under (a). Y under (b): substitutes product-line values already in the retained filings. **Confidence:** High. **In scope?** Y.

### D-03 — P1 — Table 4-3A's "Cash & bank" column understates U.S.-listed filers' liquid resources (Daqo fixed-term deposits exceed its cash)

- **PDF pages:** 16–17. **MD:** §4.7 L276, Table 4-3A L291–298, note 5 L320.
- **Quote:** "US-GAAP filers report cash excluding restricted cash." / "Daqo New Energy | USD | 0.86 | +0.12 restricted cash"
- **Problem:** For the US-GAAP filers the column is "cash and cash equivalents", which also excludes fixed-term deposits and short-term investments. Daqo holds **fixed-term deposits of $1,035.6m**, more than its $0.86bn cash. This appears only in footnote 5 of the *borrowing* table (4-3B). JinkoSolar's **restricted short-term investments of CNY3.30bn** are extracted in FIN-09 but not shown. The A-share "货币资金" column is a different construct. The L276 caveat lists only restricted cash.
- **Evidence:**
  - `closure-evidence/tables/FIN-09_Supplier-Liquidity.csv`: Daqo "fixed-term deposits of $1,035.6 million"; JinkoSolar "restricted_short_term_investments, 3,302,036".
  - `sources/sec/dq-20251231x20f.txt`: "cash, cash equivalents and restricted cash of $980.3 million and fixed-term deposits of $1,035.6 million. We did not have any bank borrowings".
- **Client consequence:** A buyer screening supplier resilience reads Daqo as having less than half its disclosed near-cash resources. The table's own warning (not a solvency ranking) is weakened by an unflagged definitional gap that affects the most net-cash company in the panel.
- **Minimal fix:** Extend L276: "US-GAAP filers report cash and cash equivalents excluding restricted cash, fixed-term deposits and short-term investments." Add a 4-3A note: "Daqo also holds $1.04bn fixed-term deposits; JinkoSolar CNY3.30bn restricted short-term investments (FIN-09)." Optionally move footnote 5's deposit clause to 4-3A.
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### D-04 — P2 — "Current borrowing obligations" applied to a line the table says may include non-debt items

- **PDF page:** 16. **MD:** L281 vs note 2 L317.
- **Quote:** "Several Chinese producers carry large current borrowing obligations alongside their cash. The current portion of Tongwei's non-current liabilities rose to CNY14.85bn…"
- **Problem:** Note 2 says "non-current liabilities due within one year … may include non-debt items" (e.g. lease liabilities). The bullet calls the same line "borrowing obligations".
- **Evidence:** Report L276, L317. FIN-09 rows "non_current_liabilities_due_within_1y (一年内到期的非流动负债)".
- **Client consequence:** It slightly overstates the debt-maturity signal. The figures themselves are correct.
- **Minimal fix:** "Several Chinese producers carry large short-term borrowings and current maturities of non-current liabilities (which may include leases) alongside their cash."
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### D-05 — P2 — "Indonesia and Laos feature prominently in the 2025–2026 import mix" overstates 2026 and omits India

- **PDF page:** 21. **MD:** §5.7 L409 (cross-ref §5.8 L417).
- **Quote:** "Indonesia and Laos feature prominently in the 2025–2026 import mix (Section 5.8)"
- **Problem:** Shares of HS 854143 module customs value, January–August:
  - 2025: Indonesia 27.0%, Laos 19.3%, India 15.2%.
  - 2026: Indonesia 11.5%, **Laos 1.0%**, **India 0.07%**.

  Laos is therefore prominent in 2025 only, and India (also subject to the determinations) is not mentioned. The series covers modules only. Cells (HS 854142), which are in scope of the AD/CVD cases, are not shown.
- **Evidence:** `data/r2/A/A_census_hs854143_by_country.csv` rows INDONESIA/LAOS/INDIA, Jan–Aug, `share_of_total`.
- **Client consequence:** It slightly mis-describes current exposure. The data instead suggest that sourcing had already shifted away from Laos and India before the final determinations. That is a more useful (descriptive, not causal) point for exporters.
- **Minimal fix:** "India, Indonesia and Laos together supplied about 62% of January–August 2025 module customs value but about 13% in January–August 2026, mainly Indonesia (Section 5.8; modules only, cells not shown), so any resulting orders would further separate customs value from delivered project cost." (Reviewer arithmetic: 15.2 + 27.0 + 19.3 = 61.5%; 0.07 + 11.5 + 1.0 = 12.6%.)
- **Changes an existing number?** N (adds derived shares from frozen data). **Confidence:** High. **In scope?** Y.

### D-06 — P2 — Bibliography lists vacated Notice 2025-42 (P02) without a status flag; Figure 4-2 cites P01–P03

- **PDF pages:** 65 (Appendix A), 14 (Figure 4-2 source). **MD:** L1248; L248.
- **Quote:** "**P02.** Notice 2025-42 (beginning of construction, wind and solar) (2025-08-15)"
- **Problem:** §10.8 correctly says the notice was vacated in full on 6 June 2026 and is "not treated as controlling". The bibliography entry and the Figure 4-2 source line give no such flag. P02 also has no retained original in the package (only the URL).
- **Evidence:** Report L836. `sources/finance/tax/USCOURTS-dcd-1_25-cv-04400-0.pdf` p.1 and p.57.
- **Client consequence:** A reader using the bibliography as a regulatory checklist could treat P02 as current guidance.
- **Minimal fix:** Append to P02: "— vacated in full and remanded, D.D.C. No. 25-4400, 6 June 2026 (F08; Section 10.8); listed for history only; not retained."
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### D-07 — P2 — The Business Wire evidence label should state its date and form (pre-COD developer statement; author-supplied screenshot)

- **PDF page:** 40 (also 63). **MD:** §10.3 L726; L1383.
- **Quote:** "The developer's release for Taygete I (250 MWac) states that the project's sole tax-equity investor, Nestlé, will also purchase 100% …"
- **Problem:** The substance is correct, and the separation of attribute tenor from hedge terms is exactly right. Two evidence-label points are missing:
  - The release is dated 9 Dec 2020, before commercial operation ("full commercial operation expected in early 2021"), so its terms are prospective statements.
  - The retained copy is an author-supplied browser screenshot. Direct retrieval was blocked (`Sources.csv` LEAD-BW-2020: "HTTP 403 / Access Denied"; BW-2020-SCREENSHOT: "author-supplied browser screenshot of developer press release").
- **Evidence:** `closure-evidence/sources/other/BusinessWire_2020-12-09_7X-Nestle-Taygete-I_author-screenshot.jpg` (paragraphs 2 and 4); `closure-evidence/Sources.csv`.
- **Client consequence:** Low. It slightly overstates the evidentiary weight of a marketing release relative to an executed contract.
- **Minimal fix:** After "The developer's release" insert "(7X Energy, 9 December 2020, before commercial operation; retained as an author-supplied screenshot)". Add: "It is a developer statement, not an executed agreement."
- **Changes an existing number?** N. **Confidence:** Medium-High. **In scope?** Y.

### D-08 — P2 — AD/CVD sentence omits the affirmative critical-circumstances findings

- **PDF page:** 21. **MD:** §5.7 L409.
- **Quote:** "Commerce published final affirmative antidumping and countervailing duty determinations … from India, Indonesia and Laos"
- **Problem:** The retained FR titles also record **final affirmative critical-circumstances determinations**: Indonesia AD (full), Laos AD (in part), India AD and CVD (in part). Critical circumstances can extend any eventual duty liability to entries before the preliminary determination. For importers and buyers holding contracts that is a material diligence point, and it is directly supported by the retained titles.
- **Evidence:** `closure-evidence/sources/trade/FR-2026-18939.json` ("…Final Affirmative Determination of Critical Circumstances"), `FR-2026-18941.json` ("…Critical Circumstances, in Part"), `FR-2026-18945.json` and `FR-2026-18947.json` (same, "In Part"). The `FR-search-cspv-2026.json` list shows six final determinations; four are retained as JSON.
- **Client consequence:** Procurement readers may underestimate retroactive exposure on entries already in the pipeline.
- **Minimal fix:** Add after the citation: "Several determinations also include affirmative critical-circumstances findings (in full or in part), which can extend any eventual duties to certain earlier entries; the effect depends on the ITC outcome and the specific entries."
- **Changes an existing number?** N. **Confidence:** High on the FR titles; the legal effect is stated conditionally. **In scope?** Y.

### D-09 — P2 — Docket currency: the RECAP copy's own record date is 16 September 2026, not the retrieval date

- **PDF page:** 46 (also 65, 72). **MD:** L836; F08 L1277; Table C-1 L1370.
- **Quote:** "The public RECAP copy of the district-court docket, retrieved on 10 October 2026, shows the case terminated on 8 June 2026 and lists no later filing"
- **Problem:** The retained HTML header reads "Last Updated: Sept. 16, 2026". The statement is accurate, but a reader may take "retrieved 10 October" as the currency of the docket record. The report already (correctly) says RECAP is not complete PACER. Adding the record date makes the limit concrete. I do not infer any appeal status either way.
- **Evidence:** `closure-evidence/sources/legal/CourtListener_RECAP_docket_dcd_1-25-cv-04400_retrieved_2026-10-10.html` (header: "Last Updated … Sept. 16, 2026"; "Date Terminated: June 8, 2026"; "Date of Last Known Filing: June 6, 2026").
- **Client consequence:** Low. It slightly overstates how current the "no later filing" observation is.
- **Minimal fix:** "…retrieved on 10 October 2026 (RECAP record last refreshed 16 September 2026), shows…"
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

### D-10 — P2 — The China export-VAT-rebate statement cites an unretrieved page; two retained filings support it and one describes it differently

- **PDF page:** 13. **MD:** §4.4 L237; P08 L1260.
- **Quote:** "From 1 April 2026, the listed photovoltaic products lose their export VAT rebate under the January 2026 notice."
- **Problem:** The only citation is P08 (MOF web page). Retrieval of that page failed: `support/Source-Acquisition.json` X05_China_Export_Tax shows a DNS error, and the `support/Official-Web-Extracts.json` entry shows "Internal Error". Two retained originals support the report's wording:
  - LONGi FY2025 AR p.297, subsequent events: Announcement 2026 No.2 of 8 Jan 2026, which cancels export VAT rebates for photovoltaic and other products from 1 Apr 2026.
  - The JinkoSolar 20-F: "eliminating export VAT rebates for photovoltaic products, effective April 1, 2026".

  The Daqo 20-F gives a different description: "lowered from 9% to 6% starting April 1, 2026 and will be abolished from January 1, 2027". I could not verify which product category Daqo's phrasing refers to.
- **Client consequence:** Low for accuracy. The current sourcing is weaker than it needs to be for a dated trade fact aimed at exporters.
- **Minimal fix:** Add "[LONGi FY2025 AR p.297; JinkoSolar FY2025 20-F]" to L237. Optionally add: "Daqo's 20-F describes a phased reduction; the announcement text itself was not retrieved for this edition."
- **Changes an existing number?** N. **Confidence:** High that the retained filings say this; whether Daqo's description is correct could not be verified. **In scope?** Y.

### D-11 — P2 — The executive summary carries no dated trade fact, though manufacturers and exporters are told to read Chapter 1 first

- **PDF pages:** 3–4. **MD:** §1.1 L28–35; navigation L17.
- **Quote:** "This cross-benchmark sensitivity estimates no actual China-to-U.S. price transmission." (L30)
- **Problem:** The most time-critical item for the manufacturer and exporter audience is that Proclamation 11052 MIPs and the +15% duty apply to entries from 4 Dec 2026, eight weeks after the report date. This appears only in §5.7. Key findings item 3 discusses module transmission without it.
- **Client consequence:** First readers in the manufacturer or exporter group may miss the governing trade constraint on the very transmission channel item 3 discusses.
- **Minimal fix:** Append to item 3: "From 4 December 2026, covered imported cells and modules face section 232 minimum import prices ($0.22/W; $0.38/W) and an additional 15% duty (Section 5.7); these are compliance thresholds, not delivered prices. [P01]"
- **Changes an existing number?** N. **Confidence:** Medium (this is an editorial-priority judgment). **In scope?** Y.

### D-12 — Disclosed limitation (no change required)

- **PDF pages:** 21, 46, 72. **MD:** L409, L836, Table C-1 L1370, Appendix C.
- **Quote:** "…none was located in the Federal Register search performed on 10 October 2026." / "Appeal and remand developments should be rechecked before any project-specific conclusion."
- **Assessment:**
  - **USITC final injury:** status is unknown in the retained originals. `Sources.csv` LEAD-USITC-VOTE, a notational vote scheduled for 14 Oct 2026, is an *unopened search lead*, and the report rightly does not use it.
  - **Notice 2025-42:** appeal and remand status is unknown beyond the RECAP copy.
  - **Market-wide delivered prices:** delivered module and EPC quotes are absent. The secondary module-price median (LEAD-ANZA) is correctly excluded.
  - **Overseas capacity and ownership:** no panel exists for these.

  All four gaps are disclosed and within the brief's boundary. They should not become new research tasks for this round.
- **Changes an existing number?** N. **Confidence:** High. **In scope?** Y.

## 4. Items I could not verify (未能核查)

- P07 (NDRC January 2025 pricing reform): no retained original was found in the package. I did not judge it.
- Notice 2026-15 content beyond its title. The 40%/45% thresholds were verified from the statute, not from the notice.
- Any post-16-September-2026 docket activity, and any USITC vote or outcome. These are not in the retained originals.
- Daqo's alternative description of the VAT rebate schedule (see D-10).
- The PVSCM workbook itself. I relied on the frozen item-level CSV for D-01.

## 5. Overall verdict

**② Handover-ready after the listed minimal edits.**

No P0 was found:

- The trade-mechanism statements check out against the retained originals: Proclamation 11052 clauses, annex HTS lines, the full-MIP versus documented-shortfall tariff, and AD/CVD status.
- So do the tax statements: P.L. 119-21 dates, the 40%/45% thresholds, the vacatur holding, and the docket hedging.
- Manufacturing output, capacity change and installation are carefully kept apart.
- The Business Wire release is correctly treated as a developer statement, with its 15-year attribute tenor separate from energy-hedge terms.

The three P1 items should be fixed before handover, because each concerns a cross-basis comparison that a client is likely to act on:

- **D-01:** the net-of-45X benchmark module line against the $0.38/W MIP.
- **D-02:** A-share industry-line margins set beside LONGi product-line margins.
- **D-03:** a cash definition that hides Daqo's fixed-term deposits.

All three can be fixed with wording or labels using materials already in the package, and none requires a change to the frozen model results. The P2 items are optional polish. This verdict is not a publication authorization or Version 1.0 acceptance.
