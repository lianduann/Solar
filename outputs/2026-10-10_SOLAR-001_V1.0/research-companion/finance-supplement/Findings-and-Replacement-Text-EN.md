# Findings and Replacement Text (EN), keyed to FIN-01 to FIN-11

**Prepared:** 2026-10-09 (America/New_York) for integration into `Deliverables/2026-10-09_Panel-Revision-Client-Edition/`. The frozen report and data are not modified.

**How to read this file:**

- Each block gives report-ready paragraphs, then the evidence for each sentence in square brackets.
- Paths are relative to this supplement unless they start with `Data/`.
- "Scenario" marks text that must stay labelled as an analytical setting.

**Scope statement for the "is the project worth it" question:** the evidence below narrows the conditions under which a 100 MWac standalone PV plant at the reference location could recover its cost. It does not support an industry-wide profitability conclusion. It also does not report any comparable project's realised return, because none is public.

---

## FIN-01 — Comparable returns and discount-rate inputs (Sections 10.9, Appendix C)

**Replacement text.**

> We assembled nine named ERCOT solar plants with primary public records. Seven are standalone PV, one is a solar plant with co-located storage, and one is a 2021 plant kept for reference. The records are Texas Comptroller Chapter 313 filings, ERCOT resource lists, EIA-860/923 and lender releases [Comparable-Projects.csv]. None of them discloses a project IRR, an equity IRR or project-level cash flows [Return-Metric-Comparability.csv RM-01–RM-04]. We therefore report no comparable return range.
>
> The discount-rate references that are public are model inputs, not observed returns:
>
> - NREL ATB's nominal 6.5% debt and 8.0% equity assumptions, which are 3.90% and 5.37% real at 2.5% inflation;
> - Berkeley Lab's 3.26% real after-tax WACC for 2024-COD projects [RM-05–RM-08].
>
> The 4.27% real pre-tax rate used here remains an analytical setting derived from the ATB inputs; we recompute it as 4.275% [data/Finance-Arithmetic-Checks.csv R-WACC]. It should not be read as a market hurdle rate. An equity hurdle cannot be applied to unlevered project cash flows.

**Do not insert:** any "typical solar IRR" range. No retained source supports one with a matched definition.

## FIN-02 — Operating generation (Chapter 9)

**Replacement text.**

> EIA-923 net generation for Pecos County standalone single-axis PV plants gives the following full-year AC capacity factors (net of curtailment and station use, divided by in-service AC nameplate × calendar hours) [data/EIA-Operating-Generation-Comparables.csv]:
>
> | Year | Plants | Range | Median |
> |---|---:|---|---:|
> | 2024 (8,784 h) | 10 | 7.5%–29.4% | 24.8% |
> | 2025 | 11 | 18.3%–29.7% | 24.6% |
>
> Among plants that entered service in 2023–2024 (Taygete II, Emerald Grove and Greasewood II), full-year factors were 25.5%–29.7%.
>
> The simulated case produces 33.4% potential AC output in 2025 and 28.3% after the negative-price stop rule. It therefore sits above every observed Pecos plant before curtailment, but within the recent-plant band after it.
>
> These comparisons are a sanity check, not a calibration. The plants differ in DC/AC ratio (1.21–1.37), module and tracker technology, outages and curtailment, and none of the figures is weather-normalised.
>
> Plants with storage at site, multi-unit aggregates, partial years and annual EIA respondents (whose monthly values EIA allocates) are listed separately and excluded from the ranges above.

[EIA-860 2025 final and EIA-923 2023/2024/2025 final: `Data/raw/2026-10-09_Finance-Deepening/EIA/`, `Data/raw/2026-08-25/US/EIA/2024_EIA-923_final.zip`; script `02_eia_operating_generation.py`.]

## FIN-03 — Contracts, hub settlement and tails (Section 10.3, Appendix B)

**Replacement text.**

> ERCOT solar is commonly hedged financially at a hub while the plant is paid the price at its own resource node. With metered output *G*, contract volume *H*, strike *K* and fees, interval revenue is *G·P_node + H·(K − P_hub) + REC − fees*. When *H = G*, this becomes *G·(K + P_node − P_hub)* [Contract-and-Tax-Decision-Tree.md §A.1].
>
> At the reference node, the output-weighted node-minus-HB_WEST basis was −0.05, +0.25 and +0.67 USD/MWh in 2023, 2024 and 2025. The output-weighted HB_WEST price was 64.94, 20.60 and 21.46 USD/MWh, which is a capture ratio of 1.30, 0.75 and 0.65 [frozen `data/panel/Node-Hub-Comparisons.csv`, independently reproduced in data/Node-Hub-Solar-Capture-2023-2025.csv].
>
> Hub settlement therefore removes little average basis at this location. What it changes is who bears the hub price level and the shape. It does not raise the value of midday solar output. Basis risk remains material interval by interval [data/Node-Hub-Basis-2023-2025.csv p05/p95 columns].

> Public evidence on contract terms for comparable plants is thin:
>
> - Taygete I sold part of its output under a long-term hedge with J. Aron & Company, and its other purchaser was an S&P A- rated entity [F01].
> - The Taygete project's two corporate offtakes were described in 2019 as a fixed-shape product [F03, secondary].
> - Tenor, strike, settlement point, negative-price treatment and REC ownership are not disclosed for any comparable.

> LevelTen's ERCOT solar P25 offer price was USD 49/MWh in Q4 2025, as reported in the trade press [PPA/PVMagazine_2026-01-30_…]. This is a first-year offer price for contracts of unstated tenor; Berkeley Lab treats LevelTen data as 12-year flat nominal contracts for its own analysis. It is not comparable with the 30-year flat break-even price of this report without matching tenor and tail assumptions.
>
> The 10- and 15-year contract cases are therefore scenario settings. The merchant tail after expiry remains unspecified until a dated price scenario is sourced [Contract-Terms.csv CT-04, CT-07, CT-08].

**Replacement for the 30-year fixed-route caveat.**

> The 30-year physical fixed-price route is a simplification. Its break-even price depends heavily on the unpaid-energy assumption: 55.91 USD/MWh with no unpaid energy, 65.97 at the 15.24% base and 80.43 at 30.48% (nominal flat, 4.27%) [data/Finance-Arithmetic-Checks.csv M-01, M-02; the 80.43 value is arithmetic scaling of the frozen break-even, not a new model run].

## FIN-04 — Tax credits (Section 10.8)

**Replacement text (law as retrieved 2026-10-09; not tax advice).**

> Public Law 119-21 ends the 45Y and 48E credits for wind and solar facilities placed in service after 31 December 2027. That cut-off applies only to facilities whose construction began after 4 July 2026. A facility that began construction on or before 4 July 2026 is outside the cut-off, so the two conditions are alternatives, not cumulative tests [Data/raw/…/tax/PLAW-119publ21.pdf §70512(a), (l)(4); §70513(a), (g)(5)].
>
> IRS Notice 2025-42, which had narrowed the beginning-of-construction methods, was vacated in full by the U.S. District Court for the District of Columbia on 6 June 2026 and remanded to the IRS [USCOURTS-dcd-1_25-cv-04400-0.pdf p.1, p.57]. We found no replacement guidance.
>
> For this report's timeline, with capital paid at end-2026, the early-construction window has already closed. A credit would therefore require the plant to be placed in service by 31 December 2027.
>
> Because construction would begin after 2025, the plant would also need to meet the material-assistance cost-ratio threshold for prohibited foreign entities: 40% if construction begins in 2026, 45% in 2027 [7701(a)(52)(B)(i); Notice 2026-15 interim safe harbours]. This is the most direct link between Chinese-supply procurement and U.S. project value in this study.
>
> For facilities above 5 MWac, the investment credit base excludes interconnection property [48E(b)(1)(B)]. The 30% illustration should therefore not be applied to grid-connection cost. Removing that cost alone reduces the illustrative credit present value from 40.33m to 35.38m USD, before any wage, sourcing, timing or transfer-discount test [data/Finance-Arithmetic-Checks.csv M-06].
>
> The depreciable basis would also fall by half the credit [50(c)(3)].

## FIN-05 — Cost coverage and interconnection (Sections 5.6, 10.7)

**Replacement text.**

> The ATB fixed O&M used here (USD 24.66/kWac-yr in 2024) is split into system, property and administration costs. The DOE/NLR cost model it cites itemises land lease, property tax (0.2% of system price per year), insurance (0.25%), asset management, security and administration, and annualised inverter and component replacement [ATB 2025 page; PVSCM UPV 2024Q1/2025Q1 parameter files]. The link from ATB to that model is inferred from the ATB citation.
>
> Land, insurance and routine replacement are therefore not missing costs, and adding them again would double count. The explicit year-16 inverter reserve overlaps the FOM replacement line, so its base value should be zero when FOM is used unchanged [Cost-Coverage-Crosswalk.csv].
>
> Texas property tax may exceed the 0.2% embedded in FOM. In the Taygete II filing, the Pecos County levy before abatement was estimated at about USD 4.6/kWac-yr. The school-district Chapter 313 limitation, which is no longer available to new projects according to secondary sources, was worth about USD 3.7/kWac-yr on average [Comptroller #1377, Schedule D; amended certificate Table 1]. A Texas-specific property-tax increment is therefore a sensitivity, not an addition to an unchanged FOM.

> ERCOT interconnection costs follow 16 TAC §25.195, not other markets' upgrade-charge rules:
>
> - The generator pays for its own step-up transformers and protective devices.
> - For interconnection agreements signed after 31 December 2025, the transmission provider funds interconnection facilities up to an allowance (2024 base USD 14 million at or below 138 kV, USD 20 million above, CPI-indexed) and bills the generator for any excess.
> - Transmission system upgrades remain the transmission provider's responsibility [PUCT_16TAC_25.195_current.pdf (f)(1), (f)(3)].
>
> The generator's main exposure to shared-network limits is congestion and curtailment, which nodal prices already capture.
>
> National benchmark capital costs carry a generic network-upgrade line (USD 51–66/kWac in the PVSCM parameter files). For an ERCOT case this may overstate generator capex, and should be tested as a sensitivity.

> Texas Comptroller filings give observed but limited cost evidence: self-reported "qualified investment" for five ERCOT plants with COD 2021–2023. The amounts imply USD 0.92–1.10 per Wac nominal (USD 0.74–0.85 per Wdc), against Berkeley Lab's ERCOT 2024-COD average of USD 1.38/Wac.
>
> Qualified investment excludes land and transmission-provider-owned facilities and may exclude some soft and financing costs. These figures therefore bound only part of the all-in cost. They do not replace the ATB-based CAPEX [data/Finance-Arithmetic-Checks.csv C-*; Comparable-Projects.csv].

## FIN-06 — Reference node identity (Section 8.1)

**Replacement text (replaces "not documented").**

> The reference price point TAYGETE2_ALL is the resource node of ERCOT units TAYGETE2_UNIT1 and TAYGETE2_UNIT2 at substation TAYGETE2 [NP4-160 mapping, Sep and Oct 2026]. ERCOT lists these as "TAYGETE SOLAR 2 U1/U2" in Pecos County, West zone, in service 2023, 101.9 MW each [ERCOT MORA December 2026, Resource Details]. That is 203.8 MW in total, the capacity of "Taygete II Solar" (INR 21INR0233) in ERCOT's 2021 planning list.
>
> EIA reports plant 64075, "Taygete II Energy Project", as 203.8 MWac / 258.4 MWdc single-axis PV in Pecos County, in service since July 2023 and operated by West Texas Solar Project II LLC [EIA-860 2025]. The same legal entity holds Texas Comptroller Chapter 313 agreement #1377, originally filed in 2019 by Taygete Energy Project II LLC (7X Energy) [Comptroller #1377 Forms 773/772].
>
> The ERCOT-to-EIA link rests on matching name, county, capacity and year. No official crosswalk links them. The EIA-to-Comptroller link rests on the shared legal entity.
>
> We use the node because it is the settlement point of an operating solar plant in the same county as the hypothetical site. The hypothetical plant is not Taygete II and would not necessarily settle at this node.

> The owner's 2025 Comptroller filing states that the current owner "purchased the project in a foreclosure auction initiated by the project's senior lender" after the previous owner failed to repay its loan [C06 p.1]. This is a reminder that operating plants at this location have faced financing stress. It is not evidence of the project's returns.

## FIN-07 — Currency and timing (Section 10.9)

> The frozen scenarios reuse 2023 and 2024 nominal prices as real 2025-dollar paths. A separately labelled CPI-harmonised scenario would multiply 2023 prices by 1.0566 and 2024 prices by 1.0263, using BLS CPI-U annual averages. The frozen outputs remain as published [Currency-Timing-Crosswalk.csv].

## FIN-08 — Market regime (Section 11.8)

> ERCOT's real-time co-optimisation with batteries (RTC+B) began on operating day 5 December 2025 [ERCOT release]. The 2025 price year therefore spans two market designs: 27 winter days fall after the change.
>
> ERCOT's operating battery fleet, counted from EIA-860 by operating year, grew from about 4.0 GW at end-2023 to 8.1 GW at end-2024 and 13.7 GW at end-2025 [data/ERCOT-Battery-Capacity-by-Vintage-EIA860-2025.csv].
>
> 2023 included an all-time demand record of 85,464 MW on 10 August, preliminary per ERCOT. It also included an Energy Emergency Alert Level 2 on 6 September at 19:25 that ended without controlled outages [ERCOT Board item 7.2, October 2023].
>
> These facts describe a changing market and support labelling 2023 as a scarcity year. They do not establish how much of 2023's price tail would recur. Finalised 2026 prices are needed before a post-RTC+B merchant scenario is chosen.

## FIN-09 — Supplier liquidity (Chapter 4)

Not addressed in this round. The placeholder should remain [Supplier-Liquidity.csv].

## FIN-10 — Debt and waterfall (Appendix C)

> Public financing evidence for comparable plants is limited to amounts and events:
>
> - a USD 256 million financing for Taygete I, arranged by CIT with five other lenders;
> - a senior-lender foreclosure on Taygete II.
>
> No coupon, tenor, sizing ratio, reserve or tax-equity term was found [Debt-and-Waterfall-Inputs.csv]. No levered equity return is estimated.

## FIN-11 — Settlement and net receipts (Appendix C)

> Revenue in this report is gross energy value: the 15-minute node price times simulated output. To reach net cash receipts, several items still have to be reconciled or added:
>
> - meter-point losses;
> - QSE and settlement charges;
> - imbalance;
> - renewable certificates;
> - any hedge settlement.
>
> None is yet supported by a retained source. ERCOT's protocols set real-time prices final at 16:00 on the second business day, but the retained archives carry no row-level version field [Settlement-and-Net-Receipts.csv; Data/2026-09-08 finality record].
