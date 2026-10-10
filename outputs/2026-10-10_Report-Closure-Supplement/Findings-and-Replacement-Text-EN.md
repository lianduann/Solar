# Findings and Replacement Text (EN) — SOLAR-001 Report Closure Supplement

**Executed:** 2026-10-10 UTC (evening of 2026-10-09, America/New_York), in a cloud container.
**Target manuscript:** `project/Deliverables/2026-10-09_Finance-Integrated-Client-Edition/Integrated-Market-Research-Report-EN_Finance-Integrated.md` (the "manuscript"; line numbers refer to that file as uploaded).
**Scope:** The 16 closed items FIN-01 to FIN-11 and B-01 to B-05 only. No model, regression, simulation or financial version was run. No new research line is opened.

## How to use this file

- Each section gives the anchor quote from the manuscript, an action (**REPLACE**, **INSERT** or **RETAIN**), complete client-ready English text, source IDs with page or locator, a number-to-source map, and the qualifications that must stay.
- Source IDs are defined in `Sources.csv`. `PKG:` paths are files in the uploaded handoff package. `LEAD-` IDs are web-search results. They are leads, not evidence: no original page could be opened from this environment.
- Text marked **CONDITIONAL INSERT** may enter the client report only after Codex (or the author) opens the original and confirms the wording. Otherwise leave it out.

## Access conditions in this pass (affects every disposition)

The container's egress policy refused connections (proxy HTTP 403 on CONNECT) to every official host attempted: sec.gov, data.sec.gov, federalregister.gov, govinfo.gov, irs.gov, ercot.com, comptroller.texas.gov, static.longi.com, static.cninfo.com.cn, courtlistener.com and atb.nlr.gov. The page-fetch tool also failed (DNS not resolved). Only a web-search tool worked, and it returns search summaries, not documents.

New evidence in this pass therefore comes from three places:

1. a fresh reading of the original PDFs and data files already in the package, such as P.L. 119-21, the D.D.C. opinion, Notice 2026-15, 16 TAC §25.195, the 2026 API QA files and the scenario-version CSVs;
2. the rendered official-page extracts saved by the previous round, such as the Federal Register text of Proclamation 11052 in `support/Policy-and-Cost-Web-Checks.json`;
3. search leads, which are labelled as leads.

"Inaccessible in this pass" below means exactly this access condition. It does not mean that a source is not public.

---

## FIN-01 — Comparable returns and discount-rate basis (10.9; Appendix C)

**Anchor (line 779):** "Comparable returns remain undisclosed. None of the nine named projects in the retained panel reports a comparable project or equity IRR or project-level cash-flow series."

**Disposition:** not publicly disclosed / inaccessible in this pass.

**Action:** RETAIN paragraph 10.9 "Comparable returns remain undisclosed". REPLACE the FIN-01 half of the box at line 781 (combined with FIN-07; see FIN-07 for the full box).

**Replacement wording (FIN-01 sentences inside the new box):**

> **Comparable returns.** Public records for the nine named ERCOT plants contain three kinds of financial observation: a financing amount (Taygete I), a lender-initiated foreclosure (Taygete II), and self-reported qualified investment (Comptroller Form 773). None reports a project or equity IRR, a cash-flow series, or the return definition needed for comparison. Those definitions are: levered or unlevered, pre- or post-tax, target or realised, and development or acquisition. A comparable return range therefore cannot be formed for this edition. The 4.27% real rate is a pre-tax analytical convention derived from ATB financing inputs. It is not a market hurdle rate. NPV results at 6% and 8% show the effect of higher required returns.

**Sources:** PKG Comparable-Projects.csv (CMP-01 to CMP-09); Return-Metric-Comparability.csv (RM-01 to RM-10); C06 Form 772 p.1 §2 item 7; F01 CIT release.

**Numbers:** none new.

**Remaining fields:** project or equity IRR, cash-flow series, return definition and investor hurdle for any of CMP-01 to CMP-09.

**Search record:** S-01, S-02, S-11, S-12. SEC full-text search could not be opened (blocked). Two search-tool queries found no disclosed IRR for Taygete I/II or Emerald Grove.

---

## FIN-02 — Operating benchmark and output reconciliation (Chapter 9, box at line 617)

**Anchor (line 617):** "Performance research partly addressed — FIN-02. Actual generation now supplies a benchmark. Reconcile same-year capacity, technology, losses, availability, forced and economic curtailment…"

**Disposition:** partially disclosed.

**Action:** REPLACE the box at line 617 with the box below.

> **Operating-benchmark boundary.** The EIA comparison uses each plant's 2025 recorded AC nameplate capacity as the denominator for both 2024 and 2025 generation. A capacity change between years would therefore bias the 2024 factor, and the full-year screen does not independently verify every historical nameplate. Emerald Grove is recorded in Pecos County by EIA but in Crane County by ERCOT and the Comptroller. Results are shown with and without it.
>
> Plant-level availability, forced outage and curtailment are not publicly disclosed for the screened plants. Only system-level indicators are available, and they come from different sources and years:
> - Berkeley Lab reports 7.1% solar curtailment in ERCOT for 2024.
> - The ERCOT Independent Market Monitor reports that roughly 6% of ERCOT solar generation was curtailed in 2025.
>
> These indicators show that net operating generation already excludes material curtailed energy. They do not apportion the gap between the simulated 33.38% potential factor and the 24.6%–25.0% screened medians among weather, design, availability and curtailment. The simulated output is therefore not calibrated, and no P50/P90 is available. The 10% export sensitivity, which adds about $10.14m to NPV with costs unchanged, is a sensitivity and not a calibrated forecast.

**Sources:** PKG `data/finance/EIA-Cohort-Reconciliation.csv`; manuscript Table 9-2; Regime-Evidence.csv RG-07 (LBNL USS 2025 slides, curtailment slide); IMM-SOM-2025 p.40 (inherited from the scenario package `Followup-Evidence-No-Login.md` §2; original PDF hash recorded in `Followup-Sources.csv`, not re-opened in this pass).

**Numbers:** 7.1% (LBNL, ERCOT 2024); ~6% (IMM, ERCOT 2025); 33.38%, 24.6%, 25.0%, $10.14m (all unchanged from the manuscript).

**Remaining fields:**
- plant-level availability, forced outage, economic or manual curtailment, and metered delivery for Taygete II, Emerald Grove and Greasewood II;
- same-year (2024) nameplate;
- weather normalisation.

---

## FIN-03 — Contract terms and the VPPA calculation version (10.3, box at line 655)

**Anchor (line 653):** "A lender release identifies a long-term J. Aron hedge for part of Taygete I output and another rated purchaser… Price, tenor, settlement point, negative-price clauses and REC ownership remain not disclosed in this edition."

**Anchor (line 655):** "Proposed 10-/15-year VPPA routes require a separately labeled calculation version."

**Disposition:** partially disclosed. Contract terms are not publicly disclosed. The VPPA calculation version already exists and is integrated by reference, not recomputed.

**Action:** RETAIN line 653. REPLACE the box at line 655 with the text below. The VPPA results come from the existing, separately versioned calculation and must be labelled as such.

> **Separately versioned hub-hedge calculation.** A separately labelled calculation version models the hypothetical plant selling metered output at the reference node, with a financial swap at HB_WEST. The swap pays contract quantity × (strike − hub price) with quantity equal to generation, over a 10- or 15-year tenor followed by a merchant tail at the node. The tail repeats the 2025 price path and is a scenario, not a forecast. Fees, RECs and imbalance are set to zero only because they are not disclosed; they are not assumed costless.
>
> On the 2025 price path at 4.27% real, the break-even flat nominal strike ranges from **$60.6/MWh** to **$84.8/MWh** across the eight tenor, dispatch and negative-hub-clause combinations. With a 10-year tenor and a $40/MWh strike, the merchant tail supplies about 43% of revenue present value. The break-even therefore depends heavily on the unsourced tail price. At 6% and 8% the break-even strikes rise to about $68–$107/MWh.
>
> These are hypothetical contract settings. No comparable project in the public record discloses a strike, tenor, settlement hub, volume rule, negative-price clause, REC allocation or credit support. The only public structure for Taygete I is a long-term hedge with J. Aron & Company for part of output, plus an unnamed S&P A– rated purchaser. The original six scenarios are unchanged.

**CONDITIONAL INSERT (only after the original Business Wire release of 9 December 2020 is opened and confirmed):**

> A developer release reports that a corporate tax-equity investor also purchases the project's renewable attributes under a 15-year agreement; this is the only publicly reported tenor associated with the Taygete projects and concerns attributes, not energy price.

**Sources:**
- PKG Finance-Scenario-Versions `Scenario-Notes-EN.md` §2;
- `data/VPPA-Breakeven-Strikes.csv` (rows: price_year 2025, discount_rate 0.0427 → 81.64, 84.77, 69.06, 81.54, 71.63, 74.41, 60.57, 71.65; rows at 0.06 and 0.08: min 68.38, max 107.12);
- `data/VPPA-Route-Scenarios.csv` (tail share: pv_revenue_tail_years 50.43m / [67.72m + 50.43m] = 42.7%);
- Contract-Terms.csv CT-01, CT-02, CT-03.
- Lead: LEAD-BW-2020 (search summary of the Business Wire release naming Nestlé as sole tax-equity investor and a 15-year renewable-attribute purchase). Not verified.

**Remaining fields:** strike, tenor, settlement point, volume basis, negative-price clause, REC ownership, credit support and curtailment allocation for any comparable contract; a dated merchant-tail price.

---

## FIN-04 — Tax timing, litigation status, basis and material assistance (10.8)

**Anchor (line 745):** "A retained District Court opinion dated 6 June 2026 vacates Notice 2025-42 in full and remands it to the IRS. Current appeal, stay and subsequent-guidance status are not established in this edition…"

**Disposition:** partially disclosed. Statute, opinion and Notice 2026-15 wording were verified against the retained originals in this pass. Appeal and stay status is inaccessible in this pass, because no primary docket could be opened.

**Verified against originals (this pass):**
- **P.L. 119-21 §70512(a)** adds 45Y(d)(4)(A): "This section shall not apply with respect to any applicable facility placed in service after December 31, 2027." Source: PLAW-119publ21.pdf, 139 Stat. 252–253.
- **§70512(l)(4):** the termination applies "to facilities the construction of which begins after the date which is 12 months after the date of enactment of this Act" (enactment 4 July 2025). Source: 139 Stat. 270.
- **§70513(a):** adds 48E(e)(4)(A) for qualified property placed in service after 31 December 2027 that is part of an applicable facility.
- **§70513(g)(5):** the same 12-month construction-start rule. Source: 139 Stat. 270 and 273.
- **New §7701(a)(52)(B)(i):** material-assistance threshold percentages for qualified facilities of 40% (construction beginning in 2026) and 45% (2027), rising to 60% after 2029. Source: P.L. 119-21, text at 139 Stat. 260–261.
- **D.D.C. No. 25-4400 (CKK), Document 50, filed 06/06/26, Memorandum Opinion:** "VACATE Notice 2025-42, and REMAND this matter to the IRS for further administrative action" (p.57). The remedy is vacatur "in full" (pp.1, 56).
- **Notice 2026-15** describes itself as interim safe-harbour guidance. Treasury and the IRS "intend to issue more comprehensive proposed regulations" (§1, p.2). It restates that §1.48E-4(a)(2) provides that qualified interconnection property is not part of a qualified facility (p.6).

**Action:** REPLACE line 745 with:

> A District Court memorandum opinion dated 6 June 2026 (Oregon Environmental Council v. IRS, D.D.C. No. 25-4400) vacates Notice 2025-42 in full and remands it to the IRS. The court decided the claims of five of the seven plaintiffs. As of 10 October 2026, this research could not consult the court docket or IRS releases directly. Secondary legal commentary reviewed through early August 2026 described an appeal or stay as expected but not filed. No replacement beginning-of-construction notice was identified. Appeal, stay and remand status therefore remain unconfirmed from primary sources, and the vacated notice is not treated as controlling guidance. Whether a given project began construction by 4 July 2026, under whichever standard ultimately governs, is a project-specific legal question. The hypothetical case supplies no construction-start facts.

**Action:** REPLACE the box at line 751 with:

> **Tax qualifications.** The statutory timing branches (Table 10-3), the 40%/45% material-assistance thresholds for 2026/2027 construction starts, and the exclusion of interconnection property above 5 MWac are taken from the statute and IRS notice text. The hypothetical case has no construction-start date, placed-in-service date, owner, supplier certifications, wage and apprenticeship records, or transfer agreement. The $35.38m OCC-basis credit illustration is therefore a conditional scenario. It is not an eligibility finding or an after-tax valuation. Its variants are in the separately versioned credit-base calculation: receipt one year later gives $33.10m; transfer at 0.90 per credit dollar gives $31.84m; the 6% base rate gives $7.08m, all as PV at 4.27%.

**Sources:**
- F07 PLAW-119publ21.pdf (pages as above);
- F08 USCOURTS-dcd-1_25-cv-04400-0.pdf pp.1, 56, 57;
- F09 n-26-15.pdf pp.2, 6;
- Finance-Scenario-Versions `Credit-Base-Scenarios.csv` rows A1_OCC_only at 0.0427: recv_end2028 → credit_pv 33,103,126; transfer_0.90 → 31,841,591; pwa_not_met_6pct → 7,075,909.
- Leads: LEAD-LAW-1 to LEAD-LAW-3 (law-firm alerts June–August 2026).

**Remaining fields:**
- appeal, notice-of-appeal or stay status from a primary docket (PACER/CourtListener; account-based);
- any post-remand IRS guidance;
- project-specific construction-start, placed-in-service, MACR, PWA, owner and transfer-price facts. These are not facts of the hypothetical case.

---

## FIN-05 — Cost vintage, scope crosswalk and delivered-price references (5.6, 10.7, B.2)

**Anchor (line 346):** "Procurement research pending — FIN-05. Obtain specification-matched U.S. delivered module and EPC quotations…"

**Anchor (line 727):** "Cost research partly addressed — FIN-05. … Reconcile the exact ATB/PVSCM vintage…"

**Disposition:** partially disclosed.

**Action:** REPLACE the box at line 346 with:

> **Procurement evidence boundary.** No free public source located for this edition gives a specification-matched, dated U.S. delivered module or EPC quotation. Such a quotation would state technology, wattage class, DC basis, currency, freight, duty and origin, delivery point and warranty. Published market price surveys report median module prices without confirming delivery terms or tariff treatment, so they are not used as project quotations. The module sensitivities in Table 5-1 therefore remain benchmark-input sensitivities. A module saving reduces an investment-credit basis only if the saved cost would have been eligible energy property. This is why the credit-adjusted gain in Section 5.6 is $2.71m rather than $3.76m.

**Action:** REPLACE the box at line 727 with the box and table below.

> **Cost scope and vintage.** The scenario CAPEX uses ATB 2025 overnight capital cost (OCC) plus grid-connection cost (GCC), 2026 values, converted from 2023 to 2025 dollars. ATB's utility PV cost is benchmarked on the DOE/NLR PV System Cost Model (PVSCM) of an earlier vintage. The component analysis in Chapter 5 instead uses PVSCM 2025Q1. The two are therefore related but not identical cost vintages, and the module share from PVSCM 2025Q1 is applied to ATB OCC only as an illustration.
>
> PVSCM itemises a network-upgrade line inside electrical balance of system: $66/kWac in the 2024Q1 inputs and $51.26/kWac in 2025Q1. It also itemises annualised inverter and component replacement inside O&M. In ERCOT, 16 TAC §25.195(f) assigns step-up transformers and protective devices to the generator. It assigns transmission system upgrades to the transmission service provider, and for SGIAs executed after 31 December 2025 it bills the generator for interconnection-facility costs above a CPI-indexed allowance. A generic network-upgrade allowance and a separate year-16 replacement reserve may therefore overlap with costs already embedded in the benchmarks. The overlap cannot be quantified without the ATB component table.
>
> Texas property-tax relief for a new standalone PV plant is narrower than for earlier projects. Tax Code Chapter 313 no longer provides new appraised-value limitations, and Government Code §403.602(8)(B) excludes non-dispatchable generation from the JETI programme. The PVSCM property-tax allowance of 0.2% of system price per year is therefore not a verified Texas liability.

**Table (INSERT after the box) — Cost-scope crosswalk, summary**

| Item | In ATB OCC | In ATB GCC | In FOM / PVSCM O&M | Scenario line | Status |
|---|---|---|---|---|---|
| Modules, inverters, trackers, BOS | Yes | No | Replacement lines in PVSCM O&M | OCC | Included; replacement overlap possible |
| Generator step-up and protection | No | Yes (national row) | No | GCC | Included; site value unknown |
| TSP interconnection above allowance | No | Possibly | No | GCC | Rule-dependent; site study absent |
| Network upgrades | Possibly (PVSCM line) | Possibly | No | OCC and/or GCC | Possible overstatement in ERCOT |
| Land lease, insurance, management | No | No | Yes | FOM | Included; do not add again |
| Texas property tax | No | No | 0.2%/yr of price | FOM | Gap risk; site tax needed |
| QSE fees, imbalance, RECs | No | No | No | None | Not modelled; not zero-cost |
| Construction financing | Excluded | Excluded | — | Excluded | Correct for unlevered overnight cost |
| Year-16 replacement reserve | — | — | Possible overlap | $35/kWac | Zero-reserve variant +$1.79m |

*Sources: ATB 2025 utility PV page and workbook rows in the scenario register; PVSCM 2024Q1/2025Q1 parameter files as itemised in the finance supplement; 16 TAC §25.195(f)(1)–(3) (retained PDF, pp.2–3); Texas statute excerpts (browser-rendered, prior round).*

**Sources:**
- Cost-Coverage-Crosswalk.csv;
- scenario_input_register.csv rows occ_2023usd, gcc_2023usd, fom_2023usd;
- PUCT_16TAC_25.195_current.pdf (f)(1)–(3), pages "§25.195-2/3";
- Followup-Evidence-No-Login.md §1 (TX statutes, browser-rendered; FOLLOWUP TX-STATUTES-BROWSER);
- LEAD-ANZA-Q1-2026 (secondary report of a median US module price; delivery terms not confirmed; not used).

**Remaining fields:** delivered quotations; the ATB Components-of-CAPEX table; site property tax, insurance and land; generator versus TSP interconnection scope; owner, EPC and financing costs.

---

## FIN-06 — Reference-node identity and settlement (8.1, box at line 490)

**Anchor (line 490):** "Location research partly addressed — FIN-06. … An official ERCOT–EIA crosswalk, historical identity/version chain and the hypothetical site's actual settlement agreement remain missing."

**Disposition:** not an existing fact of the hypothetical case (settlement agreement); partially disclosed (identity chain).

**Action:** REPLACE the box at line 490 with:

> **Reference-node status.** Official ERCOT and Comptroller documents link TAYGETE2_ALL to the TAYGETE2 units and to West Texas Solar Project II LLC, which also holds Comptroller agreement #1377. The link from ERCOT to EIA plant 64075 is an attribute match on name, county, capacity and in-service year, because no official crosswalk was identified. The mapping files used are current (September/October 2026) versions; 2023–2025 versions were not examined.
>
> The hypothetical 100 MWac system is a scenario and has no interconnection or settlement agreement. TAYGETE2_ALL is therefore used only as a historical price reference, and settlement rights at that node are not an established fact of the case. The research records available for this edition do not document why this node was originally chosen as the reference. Section 8.5 shows where it sits in the 2025 cross-section, and hub prices remain comparison benchmarks.

**Sources:** Entity-Node-Mapping.csv L01–L12; C06, C07, C09; E02, E03.

**Remaining fields:** official ERCOT–EIA crosswalk; historical NP4-160 versions (2023–2025); the original node-selection rationale, which was not in the packaged records.

---

## FIN-07 — CPI-consistent historical price years (10.9, box at line 781; B.2)

**Anchor (line 781):** "A separate CPI-consistent price-year version would scale the 2023 and 2024 nominal price levels by 1.056583 and 1.026313 to 2025 dollars. That version is not implemented here…"

**Disposition:** evidence integrated. The CPI version already exists in Finance-Scenario-Versions and is cited, not recomputed.

**Action:** REPLACE the box at line 781 with:

> **Comparable returns and currency basis.** [Insert FIN-01 "Comparable returns" paragraph.]
>
> **CPI-restated price years (separately versioned).** A separately labelled version restates the 2023 and 2024 nominal price levels in 2025 dollars using CPI-U annual-average ratios of 1.0566 and 1.0263. All other inputs are unchanged. The restatement raises the value of the older price years without changing any sign:
> - reference node 2023: NPV moves from +$97.76m to +$113.89m;
> - reference node 2024: NPV moves from −$92.15m to −$89.64m;
> - 485-node median 2023: NPV moves from +$99.78m to +$116.02m.
>
> The share of nodes with positive NPV is unchanged in every year: 100% in 2023, 2.7% in 2024 and 0.4% in 2025. The frozen same-year results in Tables 10-4 and 10-5 remain the primary presentation, and the CPI version is a purchasing-power check on them.

**Action:** RETAIN the "Currency qualification" paragraph (line 767). Append one sentence:

> "A CPI-restated version is reported in the box below."

**Basis warning for Codex (do not put in client text):** the CPI file's 485-node 2024 median (frozen −$81.33m → CPI −$78.55m) is computed from `C_tail_results_by_node_year.csv`, which uses the full 2024 calendar. Table 10-4 and 10-5 use the common-calendar matrix (−$81.59m). Do not place the CPI 2024 median beside Table 10-4 without that label. The text above therefore quotes the reference-node 2024 values, which are on the common-calendar basis (−$92.15m matches B.1), and the 2023 median, which is identical on both bases (+$99.78m).

**Sources:** Finance-Scenario-Versions `data/CPI-Harmonised-Scenario.csv` (rows TAYGETE2_ALL 2023/2024; strict 485 nodes 2023/2024/2025); `Scenario-Notes-EN.md` §3; `data/scenario_build_log.json` (factors 1.0565831533760854, 1.0263126854942315; a = 15.471935).

**Remaining fields:** none for the CPI restatement. Matched investor risk definitions remain undisclosed (see FIN-01).

---

## FIN-08 — Post-RTC+B market regime and 2026 prices (11.8, box at line 900)

**Anchor (line 900):** "Market-regime research pending — FIN-08. Obtain finalized post-launch prices, outages, available capacity, imports, constraints and battery dispatch…"

**Disposition:** partially disclosed.

**Action:** REPLACE the box at line 900 with:

> **Post-launch price evidence and its limits.** Real-time settlement-point prices for 2026 were obtained from ERCOT's public API for product NP6-905-CD, covering 1 January to 9 October 2026 and all 1,133 published settlement points. All 485 screened nodes and seven benchmarks are present.
>
> - **Coverage.** Through 8 October, the range covers 281 calendar days. Only 270 of them have every interval published: 125 intervals on 11 days are absent for every settlement point and are not filled. 9 October was partial when retrieved.
> - **Finality.** Under the Nodal Protocols, prices become final at 16:00 on the second business day after the operating day. Data through 7 October had passed that time at retrieval, but the API supplies no version field. Row-level finality is therefore not verified.
> - **Cross-product differences.** A cross-check of West hub prices against ERCOT's separate year-to-date hub file found 423 interval differences above $0.005/MWh, up to $4.01/MWh, mostly in January 2026. Their cause is not established.
>
> No 2026 generation series exists for the hypothetical site, so no 2026 capture price, revenue or NPV is reported. As context only: weighting January–September 2026 West hub prices with the 2025 simulated output profile gives $18.24/MWh, against $21.36/MWh for the same months of 2025 with that year's profile. Negative prices occur in 14.1% of 2026 intervals, against 7.7% in the 2025 months. These figures describe the first months after real-time co-optimisation began on 5 December 2025. They do not isolate its effect, because weather, load, fuel prices and new solar and storage capacity also changed.
>
> The ERCOT Independent Market Monitor reports for 2025 that the ORDC shortage adder was active for only 57 hours and that energy-storage capacity exceeded 17 GW. Three historical years provide no recurrence probability for 2023-type scarcity receipts.

**Sources:**
- PKG 2026 API: `qa_summary.json`, `coverage_by_day_all_points.csv`, `Gap-Table-System-Wide-Missing-Intervals.csv`;
- this supplement `tables/FIN-08_2026-Price-Coverage-Summary.csv`;
- Finance-Scenario-Versions `data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv` (rows Jan-Sep 2026: 18.2449 / 0.1412; Jan-Sep 2025: 21.3637 / 0.0766);
- P06 ERCOT RTC+B release (`support/Official-Web-Extracts.json`);
- IMM-SOM-2025 pp.30, 35.

**Remaining fields:** row-level price finality or version; plant-level outages, constraints, imports and battery dispatch. The last group is outside the scope of this edition; no mechanism panel is opened.

---

## FIN-09 — Supplier liquidity and balance-sheet resilience (Chapter 4, box at line 276)

**Anchor (line 276):** "Supplier-finance research pending — FIN-09. Reconcile cash balances, restricted cash, working-capital movements, debt maturities, covenant headroom, warranty provisions and manufacturing incentives…"

**Disposition:** inaccessible in this pass. The SEC and cninfo originals could not be opened from this environment. The package holds only income, OCF and capex extracts, not balance-sheet notes.

**Action:** REPLACE the box at line 276 with:

> **Supplier-resilience boundary.** Table 4-2 reports margins, operating cash flow and long-lived-asset cash outlays. It does not report the following: cash and restricted cash, short-term debt and debt maturing within a year, longer-term maturity profiles, covenant headroom, product-warranty provisions, or manufacturing incentives recorded in cost of sales (for U.S. production, section 45X credits). These items are needed before conclusions are drawn about a supplier's ability to deliver and to honour warranties. Positive operating cash flow alongside an accounting loss does not establish sustainable free cash generation. First Solar's thin-film technology, U.S. manufacturing footprint and 45X exposure require a separate reading before any comparison with Chinese-listed producers. The report assigns no credit score or default probability.

**Fields and filings for any later integration (not client text):**
- For each company: the FY2025 annual filing already cited in Appendix A (R-D SEC accession URLs; R-F cninfo URLs).
- Fields: cash and cash equivalents; restricted cash (current and non-current); OCF; working-capital lines in the cash-flow statement; short-term borrowings and current portion of long-term debt; long-term debt maturity table; product-warranty provision (opening, accrual, utilisation, closing); 45X or government-grant amounts in cost of sales.
- Units: original currency only.

**Remaining fields:** all of the above for the seven panel companies and LONGi.

---

## FIN-10 — Debt and tax-equity terms (Appendix C box at line 1262)

**Anchor (line 1262):** "Financing research pending — FIN-10 / FIN-11. Public records identify a $256m Taygete I financing and the Taygete II foreclosure, but do not disclose coupons, tenor, sizing, reserves or a tax-equity waterfall."

**Disposition:** not publicly disclosed / inaccessible in this pass.

**Action:** REPLACE the FIN-10 part of the box with:

> **Financing terms.** For Taygete I, the lead arranger's release reports a $256m financing arranged by CIT with five other lenders. For Taygete II, the Comptroller filing reports a foreclosure purchase initiated by the senior lender after the previous owner failed to repay its loan. Neither public record discloses the debt size relative to project cost, coupon or spread, tenor, amortisation, sizing ratios (DSCR), reserve accounts, fees or a tax-equity allocation. The $256m is a financing amount, not a construction cost or a return. No levered or equity return is estimated.

**CONDITIONAL INSERT (after confirming the original Business Wire release):**

> A developer release names the five co-lenders and a single corporate tax-equity investor for Taygete I; it does not disclose flip date, target yield or allocation terms.

**Sources:** F05 CIT release (Contract-Terms CT-01/02; Debt-and-Waterfall-Inputs.csv); C06 Form 772 p.1 §2 item 7. Lead: LEAD-BW-2020.

**Remaining fields:** coupon or spread, tenor, amortisation, DSCR/LLCR, DSRA/MRA, fees, sweep, flip date and target, and lender and auction price for Taygete II.

---

## FIN-11 — Price finality and net-receipts bridge (Appendix C; 7.1)

**Anchor (Appendix C row, line 1258):** "FIN-11 | Final-price versions, fees, RECs, losses and imbalance settlement | Net cash receipts and price-data finality".

**Disposition:** partially disclosed.

**Action:** REPLACE the FIN-11 part of the box at line 1262 with:

> **Gross energy value versus net receipts.** Modelled revenue is gross energy value: metered-equivalent output multiplied by the 15-minute real-time settlement-point price. Net cash receipts would also reflect several items:
> - losses between inverter and settlement meter, which sit inside the simulation's loss stack and are not separated to the settlement point;
> - scheduling-entity fees;
> - real-time deviation and uplift allocations;
> - REC sales and registration costs;
> - any hedge settlement.
>
> None of these is disclosed for the comparable plants, and none is assumed to be zero-cost.
>
> On price finality, the 2023–2025 archive prices follow the protocol rule that real-time prices are final at 16:00 on the second business day. The 2026 API data carry no version field. For the West hub, 423 intervals differ by more than $0.005/MWh from ERCOT's separate hub file, and the cause is not established. Successful download, or passage of the finality time, is therefore not treated as row-level proof of final prices.

**Sources:** Settlement-and-Net-Receipts.csv steps 1–10; 2026 API `qa_summary.json` (`finality_rule`, `hb_west_vs_np6_785_er`); this supplement `tables/FIN-08_2026-Price-Coverage-Summary.csv`.

**Remaining fields:** loss factor to settlement meter, QSE fee, imbalance and uplift charges, dated Texas REC price, and row-level price version.

---

## B-01 — LONGi FY2025 (Chapter 4)

**Anchor (line 272):** "LONGi's full FY2025 annual report remains unavailable in the research, and a harmonized segment panel remains incomplete."

**Disposition:** inaccessible in this pass. A new official lead was located: the FY2025 annual report listed on cninfo (LEAD-LONGI-AR2025). It could not be downloaded.

**Action:** REPLACE that sentence with:

> LONGi's rows remain FY2024 segment margins; its FY2025 annual report has not been incorporated into this edition, so LONGi is not compared with the FY2025 observations above. A harmonized segment panel remains incomplete.

**Note for Codex:** the search summary gives FY2025 revenue (CNY70.347bn) and an attributable net loss (CNY6.420bn) for the report at `https://static.cninfo.com.cn/finalpage/2026-04-29/1225251647.PDF`. These are unverified leads. Integrate them only after opening the PDF. Keep segment and group boundaries separate, and do not add LONGi to any ranking.

**Remaining fields:** LONGi FY2025 revenue, attributable result, OCF, LLA cash, segment margins (modules/cells; wafers), and the FIN-09 fields.

---

## B-02 — Trade rules cited in Chapter 5

**Anchor (line 350):** "Proclamation 11052, published August 11, 2026, specifies a $0.38/W minimum import price for solar modules. Its operative provisions apply from December 4, 2026 to covered entries and include documentation rules, pre-existing-contract treatment, additional duties, and exceptions… The annex-level HTS mapping remains unresolved in this report."

**Disposition:** partially disclosed (evidence integrated for the clauses checked; annex HTS unresolved). Clause text was re-read from the rendered official Federal Register extract saved in the previous round (`support/Policy-and-Cost-Web-Checks.json`). The original PDF is not in the package, and the extract ends at clause (2)(b).

**Correction needed:** "minimum import price" is enforced through entry documentation, not as a fixed floor price on every module. The manuscript should state the mechanism.

**Action:** REPLACE the first paragraph of 5.7 (line 350) with:

> Proclamation 11052 of 6 August 2026 (91 FR 51975, published 11 August 2026) acts under section 232. It sets minimum import prices of $0.22/W for solar cells and $0.38/W for solar modules, alongside per-kilogram prices for polysilicon, ingots and wafers. For goods entered on or after 12:01 a.m. ET on 4 December 2026, importers may document at entry either of two things: that the first arm's-length U.S. sale will occur at or above the applicable minimum price, or that the sale follows fixed terms in a contract signed before the proclamation. Without that documentation, the goods are subject to a specific tariff equal to the applicable minimum price. The proclamation also describes a 15% ad valorem duty on polysilicon derivatives. It states that these measures replace the safeguard tariff on solar cells and modules, which expired in February 2026. The Secretary of Commerce may adjust the minimum prices. Covered products are defined in Annexes I and II, whose tariff-line mapping has not been verified for this report. Stacking with other duties is not quantified. The headline $0.38/W is therefore a compliance threshold for covered imports, not a delivered project price. [P01, clauses 1(a)–(b), 2(a)–(b); recitals 10–11]

**Action:** INSERT after the second paragraph of 5.7:

> Separately, Commerce issued final affirmative antidumping and countervailing duty determinations on crystalline silicon cells and modules from India, Indonesia and Laos (91 FR 58633, 16 September 2026). Orders follow only after an affirmative final injury determination by the U.S. International Trade Commission, which was pending at this edition's date. Because Indonesia and Laos feature prominently in the 2025–2026 import mix (Section 5.8), any resulting orders would further separate customs value from delivered project cost.

**Sources:** P01 (rendered FR extract, prior round: `support/Policy-and-Cost-Web-Checks.json`, lines L83–L132); `data/supplement/A/A_rules_evidence.csv` R05, R06; LEAD-USITC-VOTE (USITC calendar lists a final-phase vote on 14 October 2026; lead only).

**Remaining fields:** Annex I/II HTS lines; the operative clause text for the 15% duty and the country arrangements; stacking order with section 301, AD/CVD and any other duties; USITC final injury outcome.

**Not changed:** the $0.29/Wdc versus $0.38/W comparison paragraph (line 354) remains valid as written.

---

## B-03 — Batch Zero figure and narrative (Chapter 6)

**Anchor (line 409):** "The deck also uses 127.9 GW in its narrative. That source inconsistency remains unresolved; 125.4 GW is the only as the chart-labeled quantity, with the alternative explicitly disclosed."

**Disposition:** partially disclosed. The inconsistency is confirmed in the retained transcription. No official revision was identified (one search; ercot.com not reachable). The sentence is also ungrammatical.

**Action:** REPLACE line 409 with:

> September 2026 Batch Zero materials classify 204 projects and 66.4 GW as conditional base load, and 158 projects as conditional studied load. For studied load the deck gives two totals: 125.4 GW in the chart legend (physical page 6) and 127.9 GW in the summary text (physical page 1). The category values transcribed from the chart sum to 125.4 GW, so this report uses 125.4 GW and discloses 127.9 GW as the deck's alternative figure. No official correction was identified as of this edition. Requests excluded from Batch Zero (373 projects, 302.2 GW) form a separate category. All classifications are conditional pending verification. None of these September quantities is added to March's process total, because different dates, population definitions and conditional treatment prevent a defensible additive estimate. [R-C: Batch Zero deck, physical pages 1 and 5–8]

**Sources:** this supplement `tables/B-03_Batch-Zero-Figure-vs-Narrative.csv` (studied 2032 category sum 125,391 MW; base 66,359 MW); `C_transcription_arithmetic_checks.csv`; LEAD-BZ-SEARCH.

**Remaining fields:** official reconciliation of 125.4 versus 127.9 GW; final (post-verification) Batch Zero classification.

---

## B-04 — Weather quality flags, time mapping and loss provenance (9.1, Appendix B)

**Anchor (line 560):** "Variables include irradiance, temperature, wind speed and surface albedo; source quality flags remain part of the generation-input qualifications."

**Anchor (line 592):** "(3) Weather-quality flags and performance uncertainties remain open…"

**Disposition:** partially disclosed. Flag counts were integrated from retained QA files. The raw weather files are not in the package, and the flag-code meanings were not verified from NSRDB documentation.

**Action:** REPLACE the second sentence of line 560 onward with:

> Variables include irradiance, temperature, wind speed and surface albedo. The NSRDB fill flag is non-zero for 4.1% of 2025 five-minute records: codes 1, 5 and 7 account for 1.25%, 1.24% and 1.62% of records. The non-zero share is 2.8% for 2023 and 2.5% for 2024. Flagged records are used as published, with no record removed or replaced. Their effect on simulated output has not been quantified.

**Action:** INSERT in B.2, after the PVWatts sentence:

> The aggregate loss of 14.0757% is the PVWatts v8 default stack in PySAM 7.1.1: soiling 2%, shading 3%, mismatch 2%, wiring 2%, connections 0.5%, light-induced degradation 1.5%, nameplate 1% and availability 3%. It is not derived from site measurements. NSRDB timestamps are in UTC. The simulation aligns five-minute weather to 15-minute price intervals, and the multi-year matrix uses the fixed UTC−6 calendar key described in B.1.

**Action:** REPLACE limit (3) at line 592 with:

> (3) Weather fill flags are counted and disclosed but not used to filter or adjust output; leap-day approximation and time mapping are described in Appendix B.

**Sources:**
- `data/weather_qa.json` (fill_flag_counts 0:100,801; 1:1,310; 5:1,303; 7:1,706; n = 105,120; pysam_version 7.1.1.post1);
- `data/empirical/site_energy_qa.csv` (fill_flag_nonzero_share 2023 0.02846, 2024 0.02455, 2025 0.04109);
- `data/scenario_input_register.csv` row losses_pct;
- this supplement `tables/B-04_Weather-Fill-Flag-Counts.csv`.

**Remaining fields:** decoded meaning of fill-flag codes 1, 5 and 7 (NSRDB PSM v4 documentation not opened); raw weather files (not supplied in this package).

---

## B-05 — Appendix C: separate undisclosed fields from future work

**Anchor (lines 1242–1262):** Appendix C table "Evidence still required" plus "Broader research remains open…" and the FIN-10/FIN-11 box.

**Disposition:** evidence integrated (editorial restructuring; no new evidence needed).

**Action:** REPLACE Appendix C with the text below.

> # Appendix C. Evidence Boundaries and Undisclosed Fields
>
> The report supports procurement screening, contract comparison and tests of capital-recovery conditions. A verified asset valuation would require documented location, generation, settlement, contracts, all-in costs, tax eligibility and financing. The scenario results do not supply these.
>
> **Table C-1. Specific fields not disclosed or not established in this edition.**
>
> | Area | Field not available | Result it would affect | Status in this edition |
> |---|---|---|---|
> | Returns (FIN-01) | Definition-matched project or equity IRR for the nine named plants | Return comparison, hurdle rates | Not publicly disclosed |
> | Operating output (FIN-02) | Plant availability, curtailment, same-year nameplate, metered delivery | Output calibration | System-level curtailment only |
> | Contracts (FIN-03) | Strike, tenor, hub, volume rule, negative-price clause, RECs, credit support | Paid revenue and basis | Structures only; hub-hedge version is hypothetical |
> | Tax (FIN-04) | Construction start, placed-in-service date, material-assistance ratio, PWA, transfer price; appeal or stay status of the June 2026 vacatur | Credit cash and timing | Statute verified; case facts absent; litigation status unconfirmed |
> | Costs (FIN-05) | Delivered module and EPC quotations; ATB component table; site property tax and interconnection scope | Capital and operating cost | Scope crosswalk only |
> | Location (FIN-06) | Official ERCOT–EIA crosswalk; historical mapping versions; original node-selection rationale | Applicability of the reference node | Attribute match; no settlement agreement exists for the hypothetical case |
> | Currency (FIN-07) | — | — | CPI-restated version reported (Section 10.9) |
> | Market regime (FIN-08) | Row-level 2026 price finality; 2026 site generation | Post-launch merchant value | Price coverage documented; no 2026 return |
> | Suppliers (FIN-09) | Cash, restricted cash, debt maturities, warranty provisions, 45X amounts | Supplier resilience | Not compiled |
> | Financing (FIN-10) | Coupon, tenor, sizing, reserves, tax-equity terms | Levered returns | Not publicly disclosed |
> | Net receipts (FIN-11) | Loss factor, QSE fees, imbalance, REC price | Net cash receipts | Gross energy value only |
>
> **Outside the scope of this edition.** The following are possible future work, not unresolved parts of the present analysis: expanding the overseas-factory sample; estimating industry inventory; local gas prices; attributing congestion with interval constraint data; storage design and economics; and new causal or forecasting methods. Three weather and price years provide neither validated P50/P90 output nor a long-run regime probability.

---

## Items not changed

- The six baseline scenarios, Tables 10-2, 10-4 and 10-5, all empirical estimates, and the 4.27% convention are unchanged.
- Executive-summary figures are unchanged.
- No new figure is required.
