# Findings and Replacement Text (EN) — SOLAR-001 Report Closure Supplement

**Executed:** 2026-10-10 UTC (evening of 2026-10-09, America/New_York), in a cloud container; round 2 (official sources reachable) 2026-10-10 03:15–03:35 UTC.
**Target manuscript:** `project/Deliverables/2026-10-09_Finance-Integrated-Client-Edition/Integrated-Market-Research-Report-EN_Finance-Integrated.md` (the "manuscript"; line numbers refer to that file as uploaded).
**Scope:** The 16 closed items FIN-01 to FIN-11 and B-01 to B-05 only. No model, regression, simulation or financial version was run. No new research line is opened.

## How to use this file

- Each section gives the anchor quote from the manuscript, an action (**REPLACE**, **INSERT** or **RETAIN**), complete client-ready English text, source IDs with page or locator, a number-to-source map, and the qualifications that must stay.
- Source IDs are defined in `Sources.csv`. `PKG:` paths are files in the uploaded handoff package. `LEAD-` IDs are web-search results. They are leads, not evidence: no original page could be opened from this environment.
- Text marked **CONDITIONAL INSERT** may enter the client report only after Codex (or the author) opens the original and confirms the wording. Otherwise leave it out.

## Access conditions (two rounds)

**Round 1** (2026-10-10 ~02:45 UTC): the container's egress policy refused every official host, so only package originals, prior-round extracts and search leads were used.

**Round 2** (2026-10-10 ~03:15–03:30 UTC), after the author changed the environment's network settings, the following were downloaded and saved under `sources/`:

| Source | Saved as |
|---|---|
| SEC XBRL companyfacts and FY2025 annual filings for JinkoSolar, Canadian Solar, Daqo and First Solar | `sources/sec/` |
| FY2025 annual reports of Trina, JA Solar, Tongwei and **LONGi** (cninfo) | `sources/cninfo/` |
| Official Federal Register PDF of Proclamation 11052, **including Annexes I–II** | `sources/trade/` |
| Federal Register records of Commerce's 16 September 2026 AD/CVD final determinations | `sources/trade/` |
| CourtListener RECAP docket and govinfo metadata for D.D.C. 1:25-cv-04400 | `sources/legal/` |
| The ERCOT Batch Zero deck | `sources/other/` |
| The ATB 2025 utility-scale PV page | `sources/other/` |

Still unavailable in round 2:

- usitc.gov, businesswire.com and static.longi.com return HTTP 403 at site level (bot blocking, not the proxy);
- potomaceconomics.com was still refused by the proxy, and nsrdb.nrel.gov returned 502;
- 7xenergy.com, newsroom.firstcitizens.com and nestleusa.com were not in the allowed list.

Search results remain leads only.

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

**Round 2:** businesswire.com returned HTTP 403 (site-level). SEC full-text search (2019 to 2026-10-09) returns no filing naming "Taygete" or "West Texas Solar Project II". The conditional insert therefore stays conditional.

**Remaining fields:** strike, tenor, settlement point, volume basis, negative-price clause, REC ownership, credit support and curtailment allocation for any comparable contract; a dated merchant-tail price.

---

## FIN-04 — Tax timing, litigation status, basis and material assistance (10.8)

**Anchor (line 745):** "A retained District Court opinion dated 6 June 2026 vacates Notice 2025-42 in full and remands it to the IRS. Current appeal, stay and subsequent-guidance status are not established in this edition…"

**Disposition:** partially disclosed. Statute, opinion and Notice wording were verified against the package originals. In round 2, docket status was checked against the CourtListener RECAP docket and govinfo. No appeal entry was found; this is stated with the limits of those sources. No post-remand IRS guidance was found.

**Verified against originals:**

- **P.L. 119-21 §70512(a):** adds 45Y(d)(4)(A), "This section shall not apply with respect to any applicable facility placed in service after December 31, 2027" (139 Stat. 252–253).
- **§70512(l)(4)** and **§70513(g)(5):** the termination applies to facilities "the construction of which begins after the date which is 12 months after the date of enactment" (139 Stat. 270, 273).
- **§70513(a):** adds 48E(e)(4)(A).
- **New §7701(a)(52)(B)(i):** the material-assistance threshold is 40% for construction beginning in 2026 and 45% for 2027 (139 Stat. 260–261).
- **D.D.C. No. 25-4400 (CKK), Doc. 50, filed 06/06/26:** "VACATE Notice 2025-42, and REMAND" (p.57); vacatur "in full" (pp.1, 56); claims of five of seven plaintiffs decided (p.1).
- **Doc. 49 (Order, 06/06/26)**, per the RECAP docket entry text: grants summary judgment to five named plaintiffs, declares Notice 2025-42 arbitrary and capricious under 5 U.S.C. §706(2)(A), and vacates and remands the notice.
- **RECAP docket (retrieved 2026-10-10):** "Date Terminated: June 8, 2026; Date of Last Known Filing: June 6, 2026." No notice-of-appeal entry is listed. A CourtListener search across all courts returns this one docket only, with no appellate docket.
- **govinfo package USCOURTS-dcd-1_25-cv-04400:** one opinion, dated 2026-06-06.
- **IRS credit pages** (48E and 45Y; "Page Last Reviewed or Updated" 05-Jan-2026 and 03-Mar-2026): no guidance after Notice 2025-42 is listed.
- **Notice 2026-15:** interim safe-harbour guidance, with proposed regulations to follow (§1, p.2). It restates §1.48E-4(a)(2): qualified interconnection property is not part of a qualified facility (p.6).

**Action:** REPLACE line 745 with:

> A District Court memorandum opinion and order dated 6 June 2026 (Oregon Environmental Council v. IRS, D.D.C. No. 25-4400) declare Notice 2025-42 arbitrary and capricious under the Administrative Procedure Act, vacate it in full and remand it to the IRS. The court decided the claims of five of the seven plaintiffs. The public RECAP copy of the district-court docket, retrieved on 10 October 2026, shows the case terminated on 8 June 2026 and lists no later filing; no appellate docket was located. RECAP is not a complete PACER record, and the IRS credit pages reviewed list no replacement guidance. The vacated notice is therefore not treated as controlling. Appeal and remand developments should be rechecked before any project-specific conclusion. Whether a given project began construction by 4 July 2026 remains a project-specific legal question, and the hypothetical case supplies no construction-start facts.

**Action:** REPLACE the box at line 751 with:

> **Tax qualifications.** The statutory timing branches (Table 10-3), the 40%/45% material-assistance thresholds for 2026/2027 construction starts, and the exclusion of interconnection property above 5 MWac are taken from the statute and IRS notice text. The hypothetical case has no construction-start date, placed-in-service date, owner, supplier certifications, wage and apprenticeship records, or transfer agreement. The $35.38m OCC-basis credit illustration is therefore a conditional scenario, not an eligibility finding or an after-tax valuation. Its separately versioned variants, all as PV at 4.27%, are: receipt one year later $33.10m; transfer at 0.90 per credit dollar $31.84m; and the 6% base rate $7.08m.

**Sources:**
- F07 (pages above), F08 pp.1, 56, 57;
- LEGAL-RECAP (`sources/legal/CourtListener_RECAP_docket_dcd_1-25-cv-04400_retrieved_2026-10-10.html`);
- LEGAL-CL-SEARCH;
- LEGAL-GOVINFO-MODS;
- IRS-CREDIT-PAGES (status checked; page not saved);
- F09 pp.2, 6;
- SV-CREDIT.

**Remaining fields:**
- a PACER-complete docket (not consulted; account required);
- any later IRS guidance after the pages reviewed;
- project-specific construction-start, placed-in-service, MACR, PWA, owner and transfer-price facts. These are not facts of the hypothetical case.

---

## FIN-05 — Cost vintage, scope crosswalk and delivered-price references (5.6, 10.7, B.2)

**Anchor (line 346):** "Procurement research pending — FIN-05. Obtain specification-matched U.S. delivered module and EPC quotations…"

**Anchor (line 727):** "Cost research partly addressed — FIN-05. … Reconcile the exact ATB/PVSCM vintage…"

**Disposition:** partially disclosed.

**Action:** REPLACE the box at line 346 with:

> **Procurement evidence boundary.** No free public source located for this edition gives a specification-matched, dated U.S. delivered module or EPC quotation. Such a quotation would state technology, wattage class, DC basis, currency, freight, duty and origin, delivery point and warranty. Published market price surveys report median module prices without confirming delivery terms or tariff treatment, so they are not used as project quotations. The module sensitivities in Table 5-1 therefore remain benchmark-input sensitivities. A module saving reduces an investment-credit basis only if the saved cost would have been eligible energy property. This is why the credit-adjusted gain in Section 5.6 is $2.71m rather than $3.76m.

**Action:** REPLACE the box at line 727 with the box and table below.

> **Cost scope and vintage.** The scenario CAPEX uses ATB 2025 overnight capital cost (OCC) plus grid-connection cost (GCC), 2026 values, converted from 2023 to 2025 dollars. ATB 2025 states that its 2024 overnight cost is based on modeled pricing for a 100-MWdc one-axis tracking system quoted in Q1 2024 (DOE, 2024), adjusted by an ILR of 1.32, and that 2024 fixed O&M of $24.66/kWac-yr splits into system ($10.88), property ($11.41) and administration ($2.38) expenses. The component analysis in Chapter 5 instead uses PVSCM 2025Q1. The two are therefore related but not identical cost vintages, and the module share from PVSCM 2025Q1 is applied to ATB OCC only as an illustration.
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
- ATB-PAGE (`sources/other/ATB2025_utility-scale_pv.html`, Base Year and FOM sections; retrieved round 2);
- LEAD-ANZA-Q1-2026 (secondary report of a median US module price; delivery terms not confirmed; not used).

**Remaining fields:** delivered quotations; the ATB Components-of-CAPEX table (Tableau, not exported); site property tax, insurance and land; generator versus TSP interconnection scope; owner, EPC and financing costs.

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

**Disposition:** partially disclosed (evidence integrated for most fields).

Round 2 extracted the balance-sheet and note values for all eight panel companies from their FY2025 annual filings. The filings are saved under `sources/`, and every value was checked to appear verbatim in the saved text (`tables/FIN-09_Supplier-Liquidity.csv`, 145 rows).

Not compiled:
- covenant headroom, which is not disclosed in a comparable form;
- A-share government-grant detail;
- full maturity ladders, except for Canadian Solar and First Solar.

**Action:** REPLACE the box at line 276 with the paragraph and table below.

> **Liquidity and obligations (FY2025 year-end).** Table 4-3 sets out each company's cash, borrowings, product-warranty provisions and net working capital, in its reporting currency. Two accounting differences matter when reading it. Under Chinese accounting standards, 货币资金 ("cash and bank balances") includes restricted deposits, which are shown separately here. "Non-current liabilities due within one year" can include items other than borrowings, such as lease liabilities. US-GAAP filers report cash excluding restricted cash.
>
> The table is not a solvency ranking and supports no default probability, for four reasons: currencies and accounting standards differ, the reporting dates are single points, covenant headroom is not disclosed comparably, and off-balance-sheet obligations are not captured.
>
> Three observations are relevant to procurement:
> - Several Chinese producers carry large current borrowing obligations alongside their cash. The current portion of Tongwei's non-current liabilities rose to CNY14.85bn from CNY10.73bn, and LONGi's rose to CNY10.33bn from CNY1.90bn.
> - Daqo reports no bank borrowings.
> - First Solar recognised about $1.6bn of section 45X manufacturing credits as a reduction in FY2025 cost of sales. Its margin profile is therefore not comparable with producers outside the United States without adjustment.
>
> Warranty provisions are company estimates, which depend on warranty terms and failure assumptions. JinkoSolar, for example, reversed CNY1.13bn of accrued warranty cost in FY2025 after updating replacement-cost estimates. These provisions measure the accounting reserve, not the value of warranty protection.

**Table 4-3 (INSERT after Table 4-2). FY2025 year-end liquidity and obligations; billions of reporting currency.**

| Company | CCY | Cash & bank | of which / plus restricted | Short-term borrowings and current portion | Long-term borrowings | Bonds / convertibles | Warranty provision | Net working capital |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| JinkoSolar | CNY | 20.01 | +2.93 restricted cash | 10.66¹ | 18.21 | 10.59 | 1.83 | 13.77 |
| Trina Solar | CNY | 22.55 | of which 5.48 | 7.38 + 9.51² | 19.43 | 6.09 | 2.04 | 11.70 |
| JA Solar | CNY | 25.24 | of which 8.89 | 9.06 + 5.75² | 17.52 | 8.88 | 1.99 | 9.40 |
| Tongwei | CNY | 17.48 | of which 2.20 | 7.70 + 14.85² | 51.82 | 15.88 | 1.12 | 10.47 |
| LONGi | CNY | 55.47 | of which 2.12 | 0.30 + 10.33² | 6.83 | 9.51 | 1.89³ | 20.51 |
| Canadian Solar | USD | 1.37 | +0.57 restricted cash | 2.39 | 3.62 | 0.35⁴ | 0.14 | 0.13 |
| Daqo New Energy | USD | 0.86 | +0.12 restricted cash | none⁵ | none⁵ | — | n/d | 2.19 |
| First Solar | USD | 2.80 | +0.004 restricted cash | 0.22 | 0.28 | — | 0.08 | 3.77 |

*Sources: FY2025 annual reports (cninfo) and Form 20-F/10-K (SEC), consolidated statements and notes; page or locator per row in `tables/FIN-09_Supplier-Liquidity.csv`. FY2024 comparatives are in the same file.*

*Notes:*
1. *JinkoSolar's line includes the current portion of long-term borrowings and failed sale-leaseback financing.*
2. *First figure: short-term borrowings. Second: non-current liabilities due within one year, which may include non-debt items.*
3. *LONGi: warranty provision expected to be paid after one year.*
4. *Canadian Solar: green bonds 0.15 plus convertible notes 0.20.*
5. *Daqo states it had no bank borrowings at 31 December 2025, and holds fixed-term deposits of $1,035.6m.*

*Net working capital is current assets minus current liabilities. n/d = not disclosed as a separate line. Currencies are not converted.*

**Remaining fields:**
- covenant headroom;
- full debt maturity ladders for the A-share companies and JinkoSolar;
- A-share government grants or manufacturing incentives;
- First Solar's FY2024 45X amount (not extracted).

---

## FIN-10 — Debt and tax-equity terms (Appendix C box at line 1262)

**Anchor (line 1262):** "Financing research pending — FIN-10 / FIN-11. Public records identify a $256m Taygete I financing and the Taygete II foreclosure, but do not disclose coupons, tenor, sizing, reserves or a tax-equity waterfall."

**Disposition:** not publicly disclosed / inaccessible in this pass.

**Action:** REPLACE the FIN-10 part of the box with:

> **Financing terms.** For Taygete I, the lead arranger's release reports a $256m financing arranged by CIT with five other lenders. For Taygete II, the Comptroller filing reports a foreclosure purchase initiated by the senior lender after the previous owner failed to repay its loan. Neither public record discloses the debt size relative to project cost, coupon or spread, tenor, amortisation, sizing ratios (DSCR), reserve accounts, fees or a tax-equity allocation. The $256m is a financing amount, not a construction cost or a return. No levered or equity return is estimated.

**CONDITIONAL INSERT (after confirming the original Business Wire release):**

> A developer release names the five co-lenders and a single corporate tax-equity investor for Taygete I; it does not disclose flip date, target yield or allocation terms.

**Sources:** F05 CIT release (Contract-Terms CT-01/02; Debt-and-Waterfall-Inputs.csv); C06 Form 772 p.1 §2 item 7. Lead: LEAD-BW-2020.

**Round 2:** Business Wire still returned 403. SEC full-text search found no Taygete filings; "Emerald Grove" appears only in Vistra guarantor exhibits, with no financing terms.

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

**Disposition:** evidence integrated. The LONGi Green Energy 2025 annual report (601012) was downloaded from cninfo and saved as `sources/cninfo/LONGi_2025_AR.pdf` (314 pages).

**Action:** INSERT two rows in Table 4-2 after the LONGi 2024 rows:

| LONGi | Modules/cells | 2025 | 0.19% | -6.42 | 4.36 | 5.89 | CNY | Segment margin; LLA cash |
| LONGi | Wafers/ingots | 2025 | −5.30% | -6.42 | 4.36 | 5.89 | CNY | Segment margin; group result and cash |

**Action:** REPLACE the sentence at line 272 with:

> LONGi's FY2025 annual report shows revenue of CNY70.35bn, down 14.82%. It reports an attributable net loss of CNY6.42bn, against a restated FY2024 loss of CNY8.59bn, and operating cash flow of CNY4.36bn, against an outflow of CNY4.72bn in FY2024. The gross margin of its module-and-cell segment fell to 0.19%, down 6.08 percentage points. The wafer-and-ingot margin improved to −5.30%, up 9.01 points. Cash paid for long-lived assets fell to CNY5.89bn from CNY8.01bn. Segment and group measures are shown separately, and a harmonized segment panel across companies remains incomplete.

**Sources (LONGi 2025 AR):**
- p.13: key indicators (revenue 70,347,049,950.42; attributable net profit −6,419,556,843.85; FY2024 restated −8,592,102,400.42; OCF 4,359,382,755.77 and −4,724,978,931.84);
- p.25: segment table (组件及电池 0.19%, −6.08 pp; 硅片及硅棒 −5.30%, +9.01 pp);
- p.129: cash-flow statement (购建… 5,893,972,740.27 and 8,013,068,271.53).

**Consistency check:** the manuscript's FY2024 segment margins (6.27% and −14.31%) plus the report's stated year-on-year changes reproduce the FY2025 values exactly (6.27 − 6.08 = 0.19; −14.31 + 9.01 = −5.30).

**Remaining fields:** none for the existing panel definition.

---

## B-02 — Trade rules cited in Chapter 5

**Anchor (line 350):** "Proclamation 11052, published August 11, 2026, specifies a $0.38/W minimum import price for solar modules. Its operative provisions apply from December 4, 2026 to covered entries and include documentation rules, pre-existing-contract treatment, additional duties, and exceptions… The annex-level HTS mapping remains unresolved in this report."

**Disposition:** evidence integrated. Round 2 retained the official Federal Register PDF, 91 FR 51975–51987, at `sources/trade/FR-2026-16400.pdf`. Clauses (1)–(16) and Annexes I–II were read, with the annex pages read as page images.

**Correction to round 1:** round 1 used only a truncated extract and wrongly treated secondary "shortfall tariff" descriptions as conflicting with the official text. The full text contains clause 2(c), which provides exactly that shortfall tariff for documented entries. The round-1 B-02 wording is withdrawn and replaced below.

**Action:** REPLACE the first paragraph of 5.7 (line 350) with:

> Proclamation 11052 of 6 August 2026 (91 FR 51975, published 11 August 2026), issued under section 232, sets minimum import prices (MIPs) of $0.22/W for solar cells and $0.38/W for solar modules, alongside per-kilogram prices for polysilicon, ingots and wafers. It applies to goods entered on or after 12:01 a.m. ET on 4 December 2026. Covered modules are those classified under HTSUS 8541.43.0010 and 8541.43.0080, and covered cells under 8541.42.0010 and 8541.42.0080 (Annex I).
>
> The MIP is enforced through entry documentation:
> - An importer may certify either that the first arm's-length U.S. sale will be at or above the MIP, or that the sale follows fixed terms in a contract entered into before the proclamation was signed. Annex II describes this as a time-limited contract entered into prior to 6 August 2026.
> - Without that documentation, the goods bear a specific tariff equal to the full MIP.
> - With documentation but an entered value below the MIP, they bear a specific tariff equal to the shortfall.
>
> Ingots, wafers, cells and modules also bear an additional 15% ad valorem duty. Different arrangements apply to products of Japan, Korea, Taiwan, Switzerland, Liechtenstein and EU members (a combined 15% with the ordinary duty) and to the United Kingdom (10%). These duties apply in addition to other duties, and antidumping and countervailing duties continue to be imposed. The headline $0.38/W is therefore a compliance threshold and potential duty for covered imports, not a delivered project price. [P01, clauses 1–5; Annex I; Annex II, U.S. note 42 and headings 9903.45.30–9903.45.36]

**Action:** INSERT after the second paragraph of 5.7:

> Separately, on 16 September 2026 Commerce published final affirmative antidumping and countervailing duty determinations on crystalline silicon photovoltaic cells, whether or not assembled into modules, from India, Indonesia and Laos (for example 91 FR 58633, 58643, 58651 and 58658). Duty orders require an affirmative final injury determination by the U.S. International Trade Commission, and none had been published in the Federal Register by 10 October 2026. Indonesia and Laos feature prominently in the 2025–2026 import mix (Section 5.8), so any resulting orders would further separate customs value from delivered project cost.

**Action:** in 5.7 (line 350), DELETE "The annex-level HTS mapping remains unresolved in this report."

**Not changed:** the $0.29/Wdc versus $0.38/W paragraph (line 354) remains valid.

**Sources:**
- P01-PDF (`sources/trade/FR-2026-16400.pdf`; printed pp.51977–51979 clauses 1–8; pp.51982–51983 Annex I; pp.51984–51987 Annex II);
- FR-ADCVD (`sources/trade/FR-2026-189xx.json`, FR-search-cspv-2026.json);
- FR-ITC-SEARCH (`FR-search-usitc.json`: no final injury notice since June 2026);
- LEAD-USITC-VOTE (vote listed for 2026-10-14; usitc.gov returned 403).

**Remaining fields:** the USITC final injury outcome (pending); IEEPA and other stacking beyond the clause 5(a) "in addition" rule is not quantified.

---

## B-03 — Batch Zero figure and narrative (Chapter 6)

**Anchor (line 409):** "The deck also uses 127.9 GW in its narrative. That source inconsistency remains unresolved; 125.4 GW is the only as the chart-labeled quantity, with the alternative explicitly disclosed."

**Disposition:** partially disclosed.

In round 2 the deck was re-downloaded from ercot.com (`sources/other/ERCOT_2026-09_Board14_Batch-Zero-Update.pdf`, 8 pages). The figures confirm the inconsistency: 127.9 GW on p.1, and 125.4 GW, 66.4 GW and 302.2 GW on p.6. ERCOT's Large Load Integration page, checked 10 October 2026, describes the Batch Zero verification step that precedes final classifications. No revised figure or later update was found there.

**Action:** REPLACE line 409 with:

> September 2026 Batch Zero materials classify 204 projects and 66.4 GW as conditional base load, and 158 projects as conditional studied load. For studied load the deck gives two totals: 125.4 GW in the chart legend (physical page 6) and 127.9 GW in the summary text (physical page 1). The category values in the chart sum to 125.4 GW, so this report uses 125.4 GW and discloses 127.9 GW as the deck's alternative figure. No official correction had been published as of this edition. Final classifications follow ERCOT's verification process. Requests excluded from Batch Zero (373 projects, 302.2 GW) form a separate category. None of these September quantities is added to March's process total, because different dates, population definitions and conditional treatment prevent a defensible additive estimate. [R-C: Batch Zero deck, physical pages 1 and 5–8]

**Sources:** ERCOT-BZ-DECK; ERCOT-LLI-PAGE (status checked; not saved); `tables/B-03_Batch-Zero-Figure-vs-Narrative.csv`.

**Remaining fields:** an official reconciliation of 125.4 versus 127.9 GW; the final post-verification classification.

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
> | Tax (FIN-04) | Construction start, placed-in-service date, material-assistance ratio, PWA, transfer price; PACER-complete appeal status | Credit cash and timing | Statute verified; public docket shows no appeal entry; case facts absent |
> | Costs (FIN-05) | Delivered module and EPC quotations; ATB component table; site property tax and interconnection scope | Capital and operating cost | Scope crosswalk only |
> | Location (FIN-06) | Official ERCOT–EIA crosswalk; historical mapping versions; original node-selection rationale | Applicability of the reference node | Attribute match; no settlement agreement exists for the hypothetical case |
> | Currency (FIN-07) | — | — | CPI-restated version reported (Section 10.9) |
> | Market regime (FIN-08) | Row-level 2026 price finality; 2026 site generation | Post-launch merchant value | Price coverage documented; no 2026 return |
> | Suppliers (FIN-09) | Covenant headroom; full maturity ladders (A-shares, JinkoSolar); A-share grants | Supplier resilience | Cash, borrowings, warranties and working capital compiled (Table 4-3) |
> | Financing (FIN-10) | Coupon, tenor, sizing, reserves, tax-equity terms | Levered returns | Not publicly disclosed |
> | Net receipts (FIN-11) | Loss factor, QSE fees, imbalance, REC price | Net cash receipts | Gross energy value only |
>
> **Outside the scope of this edition.** The following are possible future work, not unresolved parts of the present analysis: expanding the overseas-factory sample; estimating industry inventory; local gas prices; attributing congestion with interval constraint data; storage design and economics; and new causal or forecasting methods. Three weather and price years provide neither validated P50/P90 output nor a long-run regime probability.

---

## Items not changed

- The six baseline scenarios, Tables 10-2, 10-4 and 10-5, all empirical estimates, and the 4.27% convention are unchanged.
- Executive-summary figures are unchanged.
- No new figure is required.
