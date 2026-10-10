---
title: From China's Solar Supply Chain to U.S. Power Markets
subtitle: Industry Restructuring, Value Capture in ERCOT, and Utility-Scale Solar Economics
tagline: Market opportunities and commercial constraints in the context of data-center electricity demand
organization: Lucid Direction Insights LLC
project: SOLAR-001
version: V1.0
date: 10 October 2026
running: SOLAR-001 · Version 1.0 · 10 October 2026
---

# About This Report {.front}

**Edition.** Version 1.0, dated 10 October 2026, the delivery edition of this report for the uses listed below. Its estimates, model inputs, samples and evidence boundaries are those of the reviewed research edition. Three calculations complete the commercial picture: public market reference points (Section 10.10), a production-credit illustration (Section 10.8) and a storage screen (Section 12.4). They are arithmetic on existing outputs and public sources, not new model runs; methods and sources are in Appendix B.9 and Appendix A.3.

**Coverage.** Manufacturing evidence covers 2024 and selected FY2025 disclosures. Weather and nodal-price scenarios cover 2023–2025, with a separately qualified 2026 year-to-date price diagnostic. Regional load evidence uses March and September 2026 snapshots, and national demand scenarios extend to 2030. Policy context is dated to 9 October 2026.

**Intended readership.** Solar manufacturers and exporters, utility-scale developers, electricity buyers, and research teams.

::: uses
**Designed for**
- Industry and market screening
- Procurement diligence and commercial discussion
- Comparing contract structures and risk allocation
- Conditional capital-recovery analysis

**Not designed for**
- Valuing an actual asset or giving investment advice
- Judging whether ERCOT solar projects are generally profitable or unprofitable
- Typical project IRRs or equity-return ranges
- Financing commitments or bankability opinions
- Determining a project's tax-credit eligibility
- Price forecasts, causal estimates or long-run profit probabilities
:::

The analysis centers on a hypothetical 100 MWac solar system in Pecos County, Texas. Its results are conditional scenarios for that system, not observations of an operating asset. Project-specific costs, contracts, taxes, financing and settlement terms that are not publicly disclosed are listed in Appendix C.

**Table 0-1. Reading navigation.**

| If you are… | Read first |
|---|---|
| A manufacturer or exporter | 1, 4, 5, 10.8, 13.1 |
| A developer or investor | 1 (Table 1-2), 8.1–8.2, 10.3, 10.8, 10.10, 11.3, 13.2 |
| Selling electricity to large loads | 1, 6, 8.1–8.2, 13.3 |
| Buying electricity or hedges | 1 (Table 1-2), 6.2, 6.5, 8.1, 10.3, 10.10, 11.7, 13.3, B.2 |
| Considering storage | 12.4, B.9 |
| A research or consulting team | 2, 8.6–8.8, Appendix B (including B.6–B.9), Appendix C |

**Conventions.** Dollar amounts are U.S. dollars unless another currency is stated; $m and $bn denote millions and billions. Negative values carry a minus sign. Bracketed identifiers such as [S08] or [CL-FIN-04] refer to the source families in Appendix A. Monospaced file names refer to the research files that accompany the report.

# 1. Executive Summary: Lower Equipment Prices Require a Commercial Route to Project Value

## 1.1 Key findings

::: lead
Lower equipment prices help, but the tested 2024–2025 revenue patterns leave a large capital-recovery gap, and the positive 2023 comparison depends heavily on scarce high-price intervals. These pre-tax, unlevered results concern one hypothetical system priced at screened settlement points. They support contract and procurement screening; they do not show that ERCOT solar projects are generally uneconomic, and they do not forecast module demand.
:::

1. **Revenue falls well short of cost in the reference case.** The hypothetical 2025 reference system is modeled to earn a gross energy value of $26.4/MWh on delivered electricity (before fees, settlement losses and imbalance; not net revenue), against a delivered-energy LCOE of $48.9/MWh. Its pre-tax, unlevered NPV is −$86.0m at 4.27% real discounting, and neither base revenue route recovers its defined lifetime costs. [S08]
2. **Payment terms matter.** The 30-year node-delivered, flat nominal route breaks even near $66/MWh with 15.24% of potential energy assumed unpaid (a stress setting, not a contract term), or at $55.9/MWh if all potential output is paid. A separately calculated 10–15-year West-hub hedge with a node merchant tail needs $60.6–$84.8/MWh, depending mainly on the unsourced tail. None of these prices is an observed market offer. [S08; Section 10.3]
3. **Cheaper modules alone do not close the gap.** A hypothetical 10% reduction in the **U.S. module input** (the DOE/NLR U.S.-assembled benchmark: about $0.29/Wdc in 2024 dollars after −$0.07/Wdc of modeled 45X subsidy, about $0.36 before it; not an import or export price), passed through the component model to PV overnight cost with grid-connection cost held fixed, saves $3.76m. Even a zero-priced module input leaves the reference NPV at about −$48.3m. This cross-benchmark sensitivity does not estimate actual China-to-U.S. price transmission. [R-A; Table 5-1]
4. **Trade rules are changing the delivered-cost bridge.** From 4 December 2026, covered imports face minimum import prices (MIPs) of $0.22/W for cells and $0.38/W for modules, generally an additional 15% duty, and continuing antidumping and countervailing duties (AD/CVD). Commerce's September 2026 final determinations for India, Indonesia and Laos await U.S. International Trade Commission (USITC) injury findings, and China ended export VAT rebates for listed PV products on 1 April 2026. These provisions are not delivered prices or supplier-specific tariff outcomes. [P01; P08; Sections 4.4 and 5.7; LONGi FY2025 annual report p.297]
5. **The positive 2023 case rests on scarce high-price intervals.** Repeating 2023 conditions yields positive NPV at all 485 rule-screened nodes, versus 13 under 2024 conditions and two under 2025 conditions. The median node-level share of receipts from the top 1% of 2023 price intervals is 54.7%; removing those receipts leaves 482 nodes negative. These sample shares are historical scenario outcomes, not profitability probabilities. [E-A, E-C]
6. **Timing, not average price, drives solar value.** The reference node's 2025 average price is $46.37/MWh, but its potential-generation-weighted price is $22.13/MWh (all potential output; item 1 uses exported output after the negative-price stop rule). The corresponding West hub value is $21.46/MWh on the common calendar. A hub-settled contract leaves the seller with node-to-hub basis and needs its own settlement calculation (Section 10.3); switching benchmarks is not automatically an improvement. [S06, S07; Table 8-1]
7. **Load growth and manufacturing scale need separate commercial qualification.** ERCOT's March 2026 process table records a 238.6 GW total across all statuses in the 2030 request column, of which about 5.8 GW is observed energized, a historical noncoincident measure. Selected manufacturers report losses despite deployment growth. Neither observation determines contract or asset economics. [R-C, R-F]
8. **Recent market signals point the same way.** Public ERCOT solar offers averaged about $44.6/MWh in 2025 (25th percentile, first-year price), below every no-credit break-even in Table 1-2. The fixed-profile West hub value for January–September 2026 is $18.24/MWh, with negative prices in 14.1% of intervals versus 7.7% a year earlier. Taygete II, one of the nine named ERCOT comparables, was sold in a foreclosure purchase initiated by its senior lender. For construction starting after 4 July 2026, federal credits require service by 31 December 2027. [M01; Sections 10.10, 11.7; Appendix C; Table 10-4]

An illustrative 30% investment credit, applied to PV overnight cost only (excluding national grid-connection cost) and received at end-2027, has a present value of **$35.38m** and would move the reference NPV to **−$50.59m**. This is pre-tax NPV plus a credit that is conditional on eligibility, not an after-tax value, and the six original pre-tax scenarios are unchanged (Section 10.8). A production-credit illustration (Section 10.8) lowers the fixed-route break-even to $45.61–$47.65/MWh under the same eligibility conditions. Nine named ERCOT plants disclose no definition-matched IRR or cash flows; cost and operating comparables are diligence checks, not return benchmarks. [F01–F05]

## 1.2 Key numbers

::: kpis
$26.4/MWh | Modeled gross energy value per delivered MWh, 2025 reference case | Before fees, settlement losses and imbalance; not net revenue
$48.9/MWh | Delivered-energy LCOE | Real 2025 dollars, 4.27% real discount rate
−$86.0m | Reference-case NPV | Pre-tax, unlevered, 4.27% real
485 / 13 / 2 | Screened nodes with positive NPV, of 485 | When 2023 / 2024 / 2025 conditions repeat for 30 years
:::

**Table 1-1. Economics of the 2025 reference scenario and comparison settings.**

| Measure | Value | Basis / section |
|---|---|---|
| Capital cost | $1,437/kWac; $143.7m | National reference assumptions; 10.2 |
| Delivered-energy LCOE | $48.9/MWh | Real 2025 dollars; 4.27%; 10.6 |
| Modeled gross energy value per delivered MWh (before fees, settlement losses and imbalance) | $26.4/MWh | Reference node, stop exports below zero; 8.2 |
| Reference NPV | −$86.0m / −$95.3m / −$103.3m | 4.27% / 6% / 8% real; 10.4 |
| Break-even, 30-yr node-level fixed-price route | $66.0/MWh | 15.24% unpaid; pre-tax, no credit; 11.3 |
| HB_WEST hedge break-even strike, 10–15 yr | $60.6–84.8/MWh | Separate pre-tax, no-credit calculation; tail-dependent; 10.3 |
| Nodal break-even capital cost | $577/kWac | About 40% of base cost; 11.3 |
| Receipts needed for zero NPV | $12.1m in year 1 | Constant-real price-profile case; 10.9 |
| Module share of PV-only cost benchmark | 26.1% | About 23% of total scenario CAPEX; cross-benchmark illustration; 5.5–5.6 |
| U.S. module input falls 10% | $3.76m CAPEX / NPV improvement | PV overnight cost only; connection unchanged; 5.6 |
| Same-year positive settlement points, 2023 / 2024 / 2025 | 485 / 13 / 2 out of 485 | Common calendar, identical financial assumptions; 10.9 |

*Sources: scenario results [S08], component model [R-A], multi-year analysis [E-A]. Model assumptions are summarized in Box 1. Cost, output and revenue figures refer to a hypothetical system. LCOE is real; the break-even price is flat nominal, so the two are not directly comparable.*

## 1.3 Break-even prices on one page

The report calculates several break-even prices because each answers a different question: whether all output is paid, whether a credit is assumed, and whether the contract settles at the node or at a hub. Figure 1-1 and Table 1-2 put them on one scale beside the observed market prices.

![Figure 1-1. Price ladder: observed values, public offers and modeled break-even prices](figures/R1_price_ladder.png)

*Sources: Tables 1-1, 1-2 and 10-7; Sections 8.1, 10.3, 10.8 and 11.7. Bases differ: observed values are output-weighted energy prices, the offer index is a first-year nominal price, and break-even prices are flat nominal contract prices for the hypothetical system at 4.27% real.*

**Table 1-2. Break-even prices and market references, $/MWh.**

| Measure | 4.27% real | 6% / 8% real | What it assumes | Section |
|---|---:|---|---|---|
| Observed: reference node, modeled gross energy value, 2025 | 26.4 | — | Stop exports below zero; before fees | 8.2 |
| Observed: West hub, solar-weighted, 2025 | 21.46 | — | Common calendar | 8.1 |
| Market: ERCOT solar offers, 25th percentile, 2025 average | 44.6 | — | Public offer index; first-year nominal price; not an executed contract | 10.10 |
| Node fixed route, no credit, all output paid | 55.91 | — | Simplified paid-volume route; pre-tax | 10.3 |
| Node fixed route, no credit, 15.24% unpaid (base) | 65.97 | 74.3 / 84.6 | Unpaid share is a stress setting | 10.3, 11.3 |
| Node fixed route, no credit, 30.48% unpaid | 80.43 | — | Doubled stress | 10.3 |
| Node fixed route, illustrative 30% investment credit | 53.51 | — | Eligibility assumed; OCC basis; end-2027 receipt | 10.8 |
| Node fixed route, illustrative production credit | 45.61–47.65 | — | Full-rate credit kept or transferred at 0.90; eligibility assumed | 10.8 |
| HB_WEST hedge, 10–15 years, then node merchant tail | 60.6–84.8 | 68–107 | No credit; depends on the unsourced tail | 10.3 |

*Sources: Sections 8.1–8.2, 10.3, 10.8, 10.10 and 11.3. All break-even prices are flat nominal and pre-tax, with credits added as illustrations rather than after-tax values. The node fixed route is an analytical device, not a contract offered in the market. For comparison with a hub-settled offer, the HB_WEST row is the closest structure; credits would lower it but are not calculated for that structure.*

Read this way, no tested route without credits reaches the level of public 2025 offers, and only the full-rate production-credit illustration comes close. Offers near $44.6/MWh imply that sellers rely on credits, lower costs, higher output or different contract terms than the hypothetical case; the index does not reveal which.

## 1.4 How to interpret and use the findings

The 2025 system produces 292.4 GWh of potential AC electricity and delivers about 247.8 GWh after stopping negative-price exports. Equipment savings affect only part of cost; contracts determine which output is paid and when.

TAYGETE2_ALL is a price reference, not a verified settlement relationship for the simulated site (Section 8.1). In the separate 2025 cross-section, its absolute weighted price is near the 37th percentile, while its ratio to its own average price is near the 3rd percentile; the two measures answer different questions. The three-year panel's 2025 median NPV is −$81.3m, and neither the reference node nor the panel describes the entire market. [R-B, E-A]

Each price shape is repeated in real terms for 30 operating years, so the positive 2023 results assume that the year persists; they are not an expected return. Because receipts are concentrated, contract structure and exposure to scarce high-price hours are central diligence questions. Most 2025 intervals precede ERCOT's December 2025 launch of real-time co-optimization; Section 11.7 gives a qualified 2026 price diagnostic (not a forecast), and Section 10.3 compares contract structures.

Manufacturers can use Chapters 4–5 for procurement screening, and developers Chapters 8–11 for capital-recovery tests. Sellers should qualify the buyer's delivery profile, connection and ability to pay for reliable supply. Actual procurement, taxes and financing remain project-specific.

> **Limits of this chapter.** (1) The headline case uses one historical price reference without a verified asset settlement relationship. (2) Returns exclude taxes, credit eligibility and debt. (3) Historical-year repetition is a stress setting. (4) Output is simulated and not calibrated to operating plants (Section 9.5).

# 2. Analytical Framework: Connecting Equipment Supply to Paid Electricity

Principal abbreviations are defined here and in the glossary (Appendix D): the Electric Reliability Council of Texas (ERCOT), China's Ministry of Industry and Information Technology (MIIT), the International Renewable Energy Agency (IRENA), the Annual Technology Baseline (ATB) and the Photovoltaic System Cost Model (PVSCM). The U.S. Department of Energy (DOE) and National Laboratory of the Rockies (NLR; NREL in older publications) supply the national cost references.

## 2.1 Three analytical layers, with distinct evidence requirements

The analysis comprises three layers. The first examines Chinese and global solar supply, including manufacturing activity, equipment prices, and producer economics. The second examines the ERCOT market, including load, generation, and the geographic and temporal structure of electricity prices. The third evaluates an independently simulated solar system under specified economic scenarios.

The connections between these layers determine the strength of the commercial conclusions. Manufacturing prices enter project costs through procurement specifications and delivered-cost terms. System demand enters revenue through a particular location, delivery profile, and commercial arrangement. Weather becomes generation through system design and performance assumptions. Generation becomes cash flow through paid volumes, realized prices, operating costs, capital expenditure, and timing.

An observation in one layer cannot substitute for missing evidence in another. A site's budget requires project cost evidence; its generation requires site and system inputs; its commercial settlement point requires a documented settlement relationship.

## 2.2 Definitions that affect interpretation

**Table 2-1. Definitions used in the report.**

| Measure | Interpretation used in this report | Comparison requiring additional evidence |
|---|---|---|
| Manufacturing output | Production at a specified manufacturing stage during a stated period | Nameplate capacity, effective capacity, utilization, or installed generating capacity |
| Cumulative PV capacity | Installed capacity stock under the source's definition | Annual module purchasing or shipments |
| MWdc / MWac | DC module capacity / AC rated capacity | Cost and capacity-factor measures using a different denominator |
| Time-weighted price | Average price across available market intervals | A solar project's realized price |
| Generation-weighted price | Interval prices weighted by simulated generation | Net receipts under a commercial contract |
| LCOE | Levelized cost using the stated cost scope and energy denominator | A market quotation, achievable selling price, or complete asset cost |
| NPV | Net value of the defined cash flows at a specified discount rate | Verified market value or an actual transaction valuation |
| IRR | Discount rate at which the defined cash flows have zero NPV | A single return measure where multiple admissible roots exist |

These distinctions are particularly important when comparing manufacturing statistics with project data. Converting a module quote per Wdc to total capital cost per kWac requires the DC/AC ratio and a reconciliation of included cost categories.

## 2.3 Observations, calculations, and assumptions

The report distinguishes reported observations from derived results and analytical assumptions. MIIT's two reported annual price changes concern polysilicon and modules; no wafer or cell price change is inferred. Capture prices are calculations from the generation and price inputs. The connection between contracts and receipts is a commercial mechanism. The fixed $40/MWh price and its unpaid-energy reduction are scenario assumptions.

The underlying periods also differ. Manufacturing observations for 2024 and selected FY2025 disclosures, weather and prices for 2023–2025, publications released in 2026, and modeled demand for 2030 do not constitute a single contemporaneous dataset. Publication dates, observation periods, acquisition dates, and projection years must remain separate.

Policy context is dated to 9 October 2026. Official provisions identify diligence requirements; whether they apply to a project still depends on product, ownership, timing and contractual facts.

## 2.4 How to read scenario results

> **Box 1. How to read the numbers in this report.** The system is hypothetical: 100 MWac / 132 MWdc in Pecos County. Returns are pre-tax, unlevered and exclude tax credits, financing and unverified project costs. Nodal scenarios repeat a historical price shape for 30 years, with disclosed degradation and selected price trends; fixed-price scenarios hold a nominal price constant and deflate it by 2.5% annually. The 4.27% real discount rate is an analytical benchmark, with 6% and 8% alternatives. Statistical estimates describe conditional associations, not causal effects. Upside/downside bundles, tail stresses and three-year mixtures have no forecast probabilities attached.

The scenario results are conditional on stated assumptions and are not a verified valuation of an actual asset.

## 2.5 Two working hypotheses and three open questions

Two hypotheses can be tested with the evidence assembled here; Chapter 12 reports the results.

**H1 — Equipment price.** Lower module prices improve project economics, but their effect may be smaller than financing, interconnection delay, curtailment or realized power prices.

**H2 — Value chain.** Manufacturing scale and lower upstream prices can coexist with weak value capture along the solar value chain.

Three further questions shape the commercial thesis but need asset-level data the report does not hold. Chapter 12 states what the evidence shows about each and what would settle it.

**Q1 — Demand and value.** Does data-center load growth raise an individual solar project's realized price or bankability?

**Q2 — Grid constraints.** How much do grid constraints affect the deliverable value of solar output?

**Q3 — Storage.** Can storage improve solar economics by changing delivery timing, once its incremental costs and operating limits are counted?

> **Limits of this chapter.** (1) Source observations, accounting identities, conditional associations and hypothetical returns answer different questions. (2) Prices, costs and demand are dated separately. (3) Model boundaries are summarized in Box 1 and detailed in Appendix B.

# 3. Global Solar Demand: Industry Scale Does Not Define an Accessible Market

## 3.1 Installed capacity establishes the scale of deployment

The IRENA series reports global solar PV capacity increasing from 293,159 MW in 2016 to 2,383,162 MW in 2025. China increases from 77,788 MW to 1,200,359 MW over the same period. China is included within the world total; the two series are not additive. [S03]

![Figure 3-1. Global and Chinese cumulative solar PV capacity, 2016–2025](figures/04_irena_capacity.png)

*Source: IRENA, Renewable Capacity Statistics 2026, physical PDF pages 37–38 [S03]. China's entries carry the source flag "u" (unofficial). The series keeps the source's capacity definition; China is included in the world total.*

The data establish deployment scale, but installed stock does not measure a supplier's addressable market. It does not identify procurement volumes in a particular year, replacement demand, technology requirements, supplier eligibility, or attainable margins. For market-entry decisions, the procurement flow and the conditions of access are more directly relevant than cumulative capacity alone.

## 3.2 Capacity changes, shipments, and production measure different activity

The difference between adjacent years of capacity is a net change in the reported stock. It is not necessarily identical to new installations or module shipments. Construction timing, channel inventory, transport, retirements, revisions, and capacity definitions can separate these measures.

A manufacturing-to-demand balance therefore requires compatible flows. Subtracting changes in global installed capacity from Chinese module production would combine unlike measures and could create a misleading estimate of inventory or excess supply.

## 3.3 Regional evidence

### Country contributions reveal concentration within global growth

The IRENA tables place global PV capacity at 1,872.8 GW in 2024 and 2,383.2 GW in 2025. Their difference is 510.3 GW. China's corresponding change is approximately 314.2 GW, or 61.6% of the global change. India contributes approximately 37.0 GW and the United States 34.0 GW. Germany, Brazil, and Spain follow at approximately 15.1, 11.6, and 9.0 GW. These figures describe where installed capacity increased under IRENA's definitions; they do not identify the origin of equipment purchased or the profitability of serving each market.

![Figure 3-2. Country contributions to 2025 PV capacity growth](figures/S01_country_net_change.png)

*Source: IRENA country series [S03]; 2025 minus 2024, GW. Net capacity change can differ from gross annual installations. Small differences reflect rounding in the source and derived tables.*

Concentration matters for market development because global scale can overstate the demand directly accessible to an exporter. Country demand must be evaluated alongside trade treatment, local procurement preferences, distribution channels, and the mix of utility-scale and distributed systems. Estimating a supplier's accessible revenue pool requires regional product and market-access assumptions as well as capacity growth.

EIA's July 2026 U.S. capacity table separately reports approximately 165.3 GW of utility-scale solar and 62.8 GW of estimated small-scale solar, with a printed total of 228.2 GW. Rounded components need not sum exactly to the printed total. The observation date and measurement conventions differ from IRENA's year-end 2025 U.S. stock. The two sources are presented as separate views rather than reconciled through an unsupported adjustment.

### The manufacturing-to-installation comparison does not close a quantity balance

For the 2024 comparison (distinct from the 2025 additions above), China's reported module manufacturing output of 588 GW exceeds the 457.7 GW change in global PV capacity by approximately 130.3 GW. The arithmetic is reproducible, but its economic interpretation is limited. Output, shipments, construction, commissioning, and stock reporting occur at different times; capacity conventions and geography also differ. The residual has no validated inventory, unsold-product or overcapacity interpretation. A defensible inventory bridge would require compatible shipment, trade, opening-stock, closing-stock, and loss data.

The comparison is therefore useful as a warning about incompatible measures, rather than as an estimate of excess supply. Evidence of pricing pressure and producer margins remains analytically separate from the unclosed physical quantity balance.

## 3.4 Implications for market screening

The capacity series establishes a large and expanding deployment base, but a supplier's attainable orders, margins and delivery obligations require separate commercial evidence. Market screening should therefore proceed through four questions: the scale and composition of end demand; eligibility to supply; the ability to deliver the required product; and the economics of serving that demand. Chapters 4–8 address the mechanisms and evidence needed for the latter three questions.

> **Limits of this chapter.** (1) Net capacity additions differ from shipments and manufacturing output. (2) Country demand is not equipment origin. (3) Inventory and effective capacity remain unmeasured on a comparable basis.

# 4. China's Solar Manufacturing Industry: High Output Can Coexist with Margin Pressure

Several reported businesses combine losses or weak margins with reduced long-lived-asset spending. The company panel in this chapter distinguishes segment profitability, group cash generation and investment cash outlays. Together these measures identify commercial pressure without assigning a common cause or ranking manufacturers across different businesses and currencies.

## 4.1 Manufacturing evidence: 2024 annual cutoff

The MIIT annual bulletin, published 27 February 2025, covers 2024. It is an annual observation, not a 2026 run rate, and no later bulletin of the same type is incorporated. MIIT reports Chinese polysilicon output exceeding 1.82 million metric tonnes in 2024, alongside wafer output of 753 GW, cell output of 654 GW, and module output of 588 GW. These are successive manufacturing stages: adding their GW figures would double-count production, and differences between them do not measure inventory. [S01]

**Table 4-1. Manufacturing-stage observations, 2024.**

| Stage or indicator | Reported 2024 observation | Supported interpretation |
|---|---:|---|
| Polysilicon output | More than 1.82 million metric tonnes | Production scale at the specified stage |
| Wafer output | 753 GW | Stage-specific manufacturing output |
| Cell output | 654 GW | Manufacturing output, not generating capacity |
| Module output | 588 GW | Manufacturing output, not U.S. deliveries |
| Polysilicon price change | −39.5% | Source-reported annual price direction |
| Module price change | −29.7% | Source-reported annual price direction |

![Figure 4-1. Reported price changes at selected manufacturing stages](figures/01_miit_prices.png)

*Source: MIIT, 2024 national photovoltaic manufacturing bulletin, supplied original PDF; official Fujian republication [S01]. Two annual price changes, not a continuous transaction-price series.*

The price declines justify investigating procurement opportunities, but the observations lack a continuous product-specific price series and transaction terms. They do not identify intra-year price floors, contract lock-in, or technology premiums. Applying the reported module decline directly to U.S. project CAPEX would ignore both the module share of investment and the cost of delivery into the relevant market.

## 4.2 Company financial panel: margins and cash flows answer different questions

**Table 4-2. Company financial observations; cash amounts in billions of the stated currency.**

| Company | Stage | FY | Gross margin | Net result | OCF | Asset cash | CCY | Basis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Canadian Solar | Modules + projects | 2024 | 16.7% | n/a | −0.89 | 1.11 | USD | Group; productive-asset cash |
| Canadian Solar | Modules + projects | 2025 | 18.3% | n/a | −0.25 | 0.96 | USD | Group; productive-asset cash |
| Daqo New Energy | Polysilicon | 2024 | −20.7% | n/a | −0.44 | 0.36 | USD | Group; PPE cash |
| Daqo New Energy | Polysilicon | 2025 | −20.7% | n/a | 0.05 | 0.17 | USD | Group; PPE cash |
| First Solar | Thin-film modules | 2024 | 44.2% | n/a | 1.22 | 1.53 | USD | Group; PPE cash |
| First Solar | Thin-film modules | 2025 | 40.6% | n/a | 2.06 | 0.87 | USD | Group; PPE cash |
| JinkoSolar Holding | Integrated PV | 2024 | 10.9% | n/a | 16.85 | 9.09 | CNY | Group; PPE cash |
| JinkoSolar Holding | Integrated PV | 2025 | 2.2% | n/a | 1.08 | 3.19 | CNY | Group; PPE cash |
| Trina | Integrated PV | 2025 | 4.6% | −7.03 | 6.90 | 4.67 | CNY | Industry line (PV incl. storage/systems); LLA cash |
| JA Solar | Cells/modules | 2025 | −2.1% | −4.61 | 4.28 | 5.04 | CNY | Industry line (new energy); LLA cash |
| Tongwei | Silicon/cells + feed | 2025 | −1.12% | −9.55 | 1.38 | 13.06 | CNY | PV business line; LLA cash |
| LONGi | Modules/cells | 2024 | 6.27% | n/a | n/a | n/a | CNY | Product line only |
| LONGi | Wafers/ingots | 2024 | −14.31% | n/a | n/a | n/a | CNY | Product line only |
| LONGi | Modules/cells | 2025 | 0.19% | −6.42 | 4.36 | 5.89 | CNY | Product-line margin; LLA cash |
| LONGi | Wafers/ingots | 2025 | −5.30% | −6.42 | 4.36 | 5.89 | CNY | Product-line margin; group result and cash |

*Sources: company annual filings and XBRL [S02, R-D, R-F]. Net result is profit attributable to shareholders where available; n/a means unavailable in the extracted comparable panel, not zero. OCF is operating cash flow. PPE cash is cash paid for property, plant and equipment; Canadian Solar's productive-asset cash line has a broader reported scope. LLA cash is cash paid for fixed, intangible and other long-lived assets. The Trina, JA Solar and Tongwei asset-cash lines are from the consolidated cash-flow statements (physical PDF pp.151–152, 145–146 and 104–105, respectively).*

*Margin definitions. The A-share gross margins mix industry/business and product lines; they are not a matched product ranking. FY2025 module/cell product-line margins are Trina −1.42% (PV products), JA −4.03% (PV modules), Tongwei −0.38% (cells, modules and related) and LONGi 0.19%; LONGi's industry line is 0.81% [FY2025 annual reports, principal-business tables; CL-B-01, CL-FIN-09]. Tongwei's group cash flows include feed/food activities. LONGi's rows separate segment margins from group cash-flow and profit figures, which repeat across its segment rows and are not additive.*

*Comparability. Currencies are not converted, so cash levels are not a cross-company ranking. The panel covers listed reporting businesses and excludes exits and smaller unlisted producers; the direction of industry-wide selection bias is unestimated. U.S.-listed parents and any Chinese-listed subsidiaries have different consolidation boundaries.*

JA Solar's FY2025 attributable loss is CNY4.608bn, compared with CNY4.656bn in FY2024; these are distinct annual columns (annual report, physical p.8). Consolidated revenue of CNY49.129bn implies a −9.38% attributable net margin. The analogous FY2025 ratios are −10.50% for Trina and −11.36% for Tongwei; these group net margins should be read alongside the segment gross margins above, not substituted for them. [R-F]

Daqo's two margins both round to −20.7%, but are different observations: FY2024 gross loss of $212.932m on $1,029.080m revenue, versus FY2025 gross loss of $137.851m on $665.415m revenue. The underlying annual XBRL entries confirm that the apparent duplication is rounding, not a repeated input. [R-D]

## 4.3 Procurement implications extend beyond the quoted price

A procurement assessment needs to consider delivery continuity, warranty execution, and system compatibility alongside equipment price. The timing of these exposures differs: a lower acquisition price reduces an initial outlay, while performance or supply failures may affect subsequent delivery and operations. The evidence does not quantify supplier default probabilities or expected warranty losses.

For producers, competitiveness during a period of falling prices depends on costs, liquidity, product differentiation and market access, which one gross-margin observation cannot capture. Differences in geography and product mix can affect profitability without establishing a corresponding difference in manufacturing efficiency.

## 4.4 Policy, market access and ownership

China's January 2025 renewable electricity pricing reform moves wind and solar generation toward market-based pricing with differentiated arrangements for existing and new projects. It changes the setting for domestic demand; no installation response is estimated here. From 1 April 2026, the listed photovoltaic products lose their export VAT rebate under the January 2026 notice. This affects export economics without proving an equal increase in the U.S. delivered price. [P07; CL-B-01, LONGi FY2025 annual report p.297, post-balance-sheet note citing MOF/STA announcement 2026 No.2]

For overseas supply, four links require separate evidence: factory location, material origin, customs treatment and producer ownership/control. An overseas plant is not by itself proof of access to a particular duty treatment or tax-credit-compliant supply chain. Announced capacity is distinct from operational output; this report has no harmonized 2026 overseas capacity or ownership panel. A matched competitive panel would align product technology, segment boundaries, currency, fiscal period, utilization denominator and the treatment of incentives. Until those definitions are comparable, Table 4-2 is a financial observation panel rather than an efficiency league table.

![Figure 4-2. Evidence links from manufacturing to U.S. procurement](figures/Panel_Supply_Route.png)

*Source: analytical framework based on the manufacturing, trade and tax evidence [S01, R-T, P01–P03, P07–P08]. Boxes describe evidence requirements, not measured trade routes, capacity or eligibility.*

## 4.5 Common-period company evidence shows heterogeneous financial outcomes

The expanded panel uses the filings for JinkoSolar, Canadian Solar, Daqo, and First Solar, with FY2024 and FY2025 reported separately. The companies participate in different technologies and stages of the value chain. Consolidated gross margins are therefore useful for describing outcomes within each company over time, but differences in business scope preclude an unadjusted competitive ranking.

![Figure 4-3. Within-company gross-margin changes](figures/S02_company_margins.png)

*Source: SEC filings and annual XBRL data. Percent; consolidated reported gross profit divided by revenue. Company order is alphabetical, not a ranking of operating efficiency. First Solar's FY2025 margin includes about $1.6bn of section 45X manufacturing credits recognized as a reduction in cost of sales, so it is not directly comparable with manufacturers outside the United States without equivalent support.*

Cash generation adds another dimension. JinkoSolar's operating cash flow falls from approximately CNY16.85bn to CNY1.08bn between FY2024 and FY2025. Canadian Solar reports operating outflows in both years, while First Solar reports positive operating cash flow. Daqo's FY2025 operating cash flow is positive despite a negative gross margin. Working-capital movements, business mix, and other cash-flow items can produce such differences; equipment prices alone are not an identified explanation for reported cash flow.

Capital spending also requires account-level interpretation. Canadian Solar's extracted cash-flow item covers payments to acquire productive assets, a broader label than an automatically comparable factory-expansion measure. LONGi's FY2024 investing cash flow is broader than capital expenditure and is not used as that measure here.

## 4.6 Utilization indicators require explicit capacity denominators

A comparable utilization measure requires a period-average effective-capacity denominator and a matched production boundary. No harmonized industry utilization rate is supplied here. Daqo's annual production divided by a point-in-time nameplate figure is a different indicator: capacity may have changed during the year, so that ratio is not a validated annual utilization measure.

Daqo's disclosed selling prices likewise describe its own product mix and sales period. They provide corroborating company evidence of pressure at one manufacturing stage, rather than a continuous extension of MIIT's industry price-change series. The A-share FY2025 filings are incorporated in Section 4.7; a consistent multi-company capacity and utilization panel remains necessary before broader cycle conclusions.

## 4.7 Additional FY2025 disclosures broaden the manufacturing sample

The FY2025 annual reports for Trina Solar, JA Solar, and Tongwei extend the four-company panel. Reported revenue is approximately CNY66.97bn, CNY49.13bn, and CNY84.13bn respectively; attributable net losses are approximately CNY7.03bn, CNY4.61bn, and CNY9.55bn. Tongwei reports approximately CNY54.14bn of PV-segment revenue, distinct from its CNY84.13bn group revenue including feed-related activities, and the companies' consolidation and product boundaries differ. These results therefore broaden evidence of financial pressure without constituting a product-matched efficiency ranking. [R-F]

Reported cash payments for construction and acquisition of long-lived assets also decline: approximately CNY4.67bn versus CNY13.29bn for Trina, CNY5.04bn versus CNY11.83bn for JA Solar, and CNY13.06bn versus CNY28.39bn for Tongwei in FY2025 versus FY2024. The spending measure follows each filing's definition and is not automatically equivalent to incremental capacity investment. Lower spending can reflect project completion, reduced expansion, or financing and working-capital choices; the observations alone do not identify which mechanism dominates.

The extended sample distinguishes consolidated loss, segment gross margin, cash generation and capital spending. LONGi's FY2025 annual report shows revenue of CNY70.35bn, down 14.82%. It reports an attributable net loss of CNY6.42bn, against a restated FY2024 loss of CNY8.59bn, and operating cash flow of CNY4.36bn, against an outflow of CNY4.72bn in FY2024. The gross margin of its module-and-cell segment fell to 0.19%, down 6.08 percentage points. The wafer-and-ingot margin improved to −5.30%, up 9.01 points. Cash paid for long-lived assets fell to CNY5.89bn from CNY8.01bn. Segment and group measures are shown separately, and a harmonized segment panel across companies remains incomplete. [CL-B-01]

**Liquidity and obligations (FY2025 year-end).** Tables 4-3A and 4-3B set out each company's cash, borrowings, product-warranty provisions and net working capital in its reporting currency. Accounting differences matter when reading them. Under Chinese accounting standards, "cash and bank balances" includes restricted deposits, which are shown separately here. "Non-current liabilities due within one year" can include items other than borrowings, such as lease liabilities. US-GAAP filers report cash excluding restricted cash. For U.S.-listed filers the cash column excludes fixed-term deposits and short-term investments: Daqo also reports fixed-term deposits of $1,035.6m, and JinkoSolar restricted short-term investments of CNY3.30bn.

The tables are not a solvency ranking and support no default probability, for four reasons: currencies and accounting standards differ, the reporting dates are single points, covenant headroom is not disclosed comparably, and off-balance-sheet obligations are not captured.

Two observations are relevant to procurement:
- Several Chinese producers carry large short-term borrowings and current maturities of non-current liabilities (which may include leases) alongside their cash. The current portion of Tongwei's non-current liabilities rose to CNY14.85bn from CNY10.73bn, and LONGi's rose to CNY10.33bn from CNY1.90bn.
- Daqo reports no bank borrowings.

First Solar's margin profile also reflects section 45X manufacturing credits (Figure 4-3) and is not comparable with producers outside the United States without adjustment.

Warranty provisions are company estimates, which depend on warranty terms and failure assumptions. JinkoSolar, for example, reversed CNY1.13bn of accrued warranty cost in FY2025 after updating replacement-cost estimates. These provisions measure the accounting reserve, not the value of warranty protection. [CL-FIN-09]

**Table 4-3A. FY2025 year-end liquidity, warranties and working capital; billions of reporting currency.**

| Company | CCY | Cash & bank | of which / plus restricted | Warranty provision | Net working capital |
| --- | --- | ---: | ---: | ---: | ---: |
| JinkoSolar | CNY | 20.01 | +2.93 restricted cash | 1.83 | 13.77 |
| Trina Solar | CNY | 22.55 | of which 5.48 | 2.04 | 11.70 |
| JA Solar | CNY | 25.24 | of which 8.89 | 1.99 | 9.40 |
| Tongwei | CNY | 17.48 | of which 2.20 | 1.12 | 10.47 |
| LONGi | CNY | 55.47 | of which 2.12 | 1.89³ | 20.51 |
| Canadian Solar | USD | 1.37 | +0.57 restricted cash | 0.14 | 0.13 |
| Daqo New Energy | USD | 0.86 | +0.12 restricted cash | n/d | 2.19 |
| First Solar | USD | 2.80 | +0.004 restricted cash | 0.08 | 3.77 |

*Net working capital is current assets minus current liabilities. n/d = not disclosed as a separate line. Currencies are not converted.*

**Table 4-3B. FY2025 year-end borrowing observations; billions of reporting currency.**

| Company | CCY | Short-term borrowings and current maturities (may include leases) | Long-term borrowings | Bonds / convertibles |
| --- | --- | ---: | ---: | ---: |
| JinkoSolar | CNY | 10.66¹ | 18.21 | 10.59 |
| Trina Solar | CNY | 7.38 + 9.51² | 19.43 | 6.09 |
| JA Solar | CNY | 9.06 + 5.75² | 17.52 | 8.88 |
| Tongwei | CNY | 7.70 + 14.85² | 51.82 | 15.88 |
| LONGi | CNY | 0.30 + 10.33² | 6.83 | 9.51 |
| Canadian Solar | USD | 2.39 | 3.62 | 0.35⁴ |
| Daqo New Energy | USD | none⁵ | none⁵ | — |
| First Solar | USD | 0.22 | 0.28 | — |

*Sources: FY2025 annual reports (cninfo) and Form 20-F/10-K (SEC), consolidated statements and notes; page or locator per row in [supplier-liquidity table](closure-evidence/tables/FIN-09_Supplier-Liquidity.csv). FY2024 comparatives are in the same file.*

*Notes:*
1. *JinkoSolar's line includes the current portion of long-term borrowings and failed sale-leaseback financing.*
2. *First figure: short-term borrowings. Second: non-current liabilities due within one year, which may include non-debt items.*
3. *LONGi: warranty provision expected to be paid after one year.*
4. *Canadian Solar: green bonds 0.15 plus convertible notes 0.20.*
5. *Daqo states it had no bank borrowings at 31 December 2025, and holds fixed-term deposits of $1,035.6m.*

> **Limits of this chapter.** (1) Consolidated and segment accounts differ; currencies and business mixes remain separate. (2) Losses and lower capital spending indicate pressure but do not identify an industry-wide cause or rank producers. (3) The additional evidence required is listed in Appendix C.

# 5. Cost Transmission: A Lower Module Price Reduces Only Part of Project Investment

## 5.1 The delivered-cost bridge

Manufacturing price changes translate into project costs only after three questions are resolved: whether the products are comparable; which delivery and trade terms apply; and what share of the relevant project budget the product represents.

Prices expressed per watt may differ in technology, currency, taxes, freight, delivery date, warranty, and payment terms. A decline in an annual manufacturing-price measure does not demonstrate an equivalent saving for a U.S. buyer purchasing a compliant product under specified delivery conditions.

The commercial comparison is therefore between complete procurement packages. A lower factory price may be offset by changes in logistics, sourcing conditions, timing, or other costs. The magnitude and direction of those offsets require evidence rather than a general assumption about imported-equipment competitiveness.

## 5.2 Module share determines the direct CAPEX effect

With module quantity, system design, and all other costs held constant, the direct relationship is:

**Relative change in total CAPEX ≈ initial module share of CAPEX × relative change in module unit price.**

Let the initial module cost share be *s* and the module price change be *m*. The isolated effect on total investment is then *s* × *m*. The evidence does not support filling *s* with a verified project-specific or comparable delivered-cost share. The MIIT decline of 29.7% is therefore not applied directly to total CAPEX. Section 5.5 shows an illustrative calculation using a benchmark component share.

Changes in efficiency, module power, or system design may also affect racking, land, installation, or electrical requirements. Those effects require a component-level analysis. A single price multiplier holds product and project scope constant.

## 5.3 What the ATB benchmark contributes

The economic scenarios use ATB overnight capital cost, or OCC, plus grid-connection cost, or GCC. These references provide a national technology-cost anchor and cost definitions. They do not measure the transmission of Chinese manufacturing prices into a particular U.S. project.

The cost extract does not itemize module procurement within the scenario CAPEX, so the total-CAPEX sensitivity measures a change in the complete capital budget, not an isolated module-price effect. [S08, S09]

## 5.4 Evidence required for an empirical transmission analysis

An empirical delivered-cost bridge needs matched module specifications, dates, origin, logistics, duties and procurement terms. The next section quantifies the conditional engineering-cost channel using national model inputs; it does not measure transaction-price transmission.

## 5.5 A reproducible component model bounds the transmission mechanism

Re-evaluation of the DOE/NLR 2025Q1 utility-scale cost-model inputs produces a PV-only modeled market price of approximately $1.115/Wdc in 2024 dollars. The corresponding minimum sustainable price is approximately $1.066/Wdc. These are modeled national benchmarks with different economic interpretations, not alternative quotations offered to the hypothetical Pecos County project. Published PV-plus-storage component groups reconcile within $1/kWdc, and the rounded PV-only total provides a separate cross-check. This is not validation against observed project invoices.

![Figure 5-1. Components of the PV-only modeled market price](figures/S03_cost_components.png)

*Source: reimplementation of DOE/NLR PVSCM 2025Q1 inputs; 2024 dollars per Wdc. Storage and storage-related items excluded. Shares are derived from the unrounded total. The chart uses the DC denominator throughout.*

Modules account for approximately 26.1% of the modeled market-price total. Electrical balance of system and fieldwork are also material. The cost model includes sales tax, contingency, overhead, and developer profit, so a change in the module input affects more than the module line itself. Under the additive percentage structure, a $1/kWdc change in the module input changes total modeled cost by approximately $1.144/kWdc, with all other inputs held constant.

The preferred sensitivity varies the **U.S. module input** defined in Section 1.1 directly: the subsidy-adjusted U.S.-assembled benchmark cost, not an import quotation. A 10%, 20% or 30% module-input reduction lowers PV-only modeled cost by approximately 2.99%, 5.97% or 8.96%, respectively. The result follows from the 26.111% module share multiplied by the 1.144 marginal cost factor. The module price is the changed input; specifications, logistics and other component inputs remain fixed.

![Figure 5-2. Hypothetical U.S. module-input changes and PV-only modeled cost](figures/Panel_Module_Transmission.png)

*Source: DOE/NLR PVSCM component calculation [R-A]. Percentage changes apply to the PV-only modeled cost boundary, not separately to grid connection or a delivered procurement quote.*

## 5.6 From component savings to project value

The hypothetical financial case contains $126.04m of PV overnight cost and $17.63m of grid-connection cost. Applying the component percentage to the former while holding the latter fixed gives the following controlled comparison. It combines two national benchmarks and is therefore an illustrative cost mapping, not a measured project procurement relationship.

**Table 5-1. U.S. module-input sensitivities; real 2025 dollars.**

| Module-input reduction | Initial cost saving / pre-credit NPV gain, $m | Reference-node NPV, $m | Fixed-base NPV, $m |
|---|---:|---:|---:|
| 10% | 3.76 | −82.20 | −69.98 |
| 20% | 7.53 | −78.44 | −66.21 |
| 30% | 11.29 | −74.67 | −62.45 |
| 100%: module input set to zero | 37.65 | −48.32 | −36.09 |

*Source: component share and cost factor [R-A], scenario cost register and base cash flows [S08]. Connection cost is unchanged. A zero module price is a mathematical boundary, not a feasible commercial quotation.*

Even eliminating the module input fails to close the tested shortfall. If the illustrative credit in Section 10.8 applies and eligible basis falls with cost, a 10% module reduction improves NPV by $2.71m rather than $3.76m because the assumed credit receipt also falls. This is a conditional interaction, not evidence of actual eligibility.

**Procurement evidence boundary.** No public source located for this report gives a specification-matched, dated U.S. delivered module or EPC quotation. Such a quotation would state technology, wattage class, DC basis, currency, freight, duty and origin, delivery point and warranty. Published market price surveys report median module prices without confirming delivery terms or tariff treatment, so they are not used as project quotations. The module sensitivities in Table 5-1 therefore remain benchmark-input sensitivities. A module saving reduces an investment-credit basis only if the saved cost would have been eligible energy property, which is why the credit-adjusted gain above is $2.71m rather than $3.76m. [CL-FIN-05]

## 5.7 Policy changes make procurement dates and classification commercially relevant

Proclamation 11052 of 6 August 2026 (91 FR 51975, published 11 August 2026), issued under section 232, sets minimum import prices (MIPs) of $0.22/W for solar cells and $0.38/W for solar modules, alongside per-kilogram prices for polysilicon, ingots and wafers. It applies to goods entered on or after 12:01 a.m. ET on 4 December 2026. Covered modules are those classified under HTSUS 8541.43.0010 and 8541.43.0080, and covered cells under 8541.42.0010 and 8541.42.0080 (Annex I).

The MIP is enforced through entry documentation:
- An importer may certify either that the first arm's-length U.S. sale will be at or above the MIP, or that the sale follows fixed terms in a contract entered into before the proclamation was signed. Annex II describes this as a time-limited contract entered into prior to 6 August 2026.
- Without that documentation, the goods bear a specific tariff equal to the full MIP.
- With documentation but an entered value below the MIP, they bear a specific tariff equal to the shortfall.

If U.S. Customs and Border Protection (CBP) finds an importer's documentation materially inaccurate, the importer and its affiliates are permanently prohibited from importing polysilicon and derivatives (clause 3).

Ingots, wafers, cells and modules also bear an additional 15% ad valorem duty. Different arrangements apply to products of Japan, Korea, Taiwan, Switzerland, Liechtenstein and EU members (a combined 15% with the ordinary duty) and to the United Kingdom (10%). These duties apply in addition to other duties, and antidumping and countervailing duties continue to be imposed. The headline $0.38/W is therefore a compliance threshold and potential duty for covered imports, not a delivered project price. [P01, clauses 1–5; Annex I; Annex II, U.S. note 42 and headings 9903.45.30–9903.45.36] [CL-B-02] These country arrangements concern the additional ad valorem duty, not the MIP. The Secretary may adjust the MIP under clause 1(b). On the face of the text, covered China-origin goods fall under both the MIP program and the 15% duty; this is a reading of the proclamation, not a customs ruling.

The accompanying trade evidence identifies applicable diligence questions; it is not an all-in tariff calculator. IEEPA treatment and the complete interaction of duties remain outside the quantified cost bridge. No tariff benefit or incentive eligibility is assigned to the hypothetical project.

Separately, on 16 September 2026 Commerce published final affirmative antidumping and countervailing duty determinations on crystalline silicon photovoltaic cells, whether or not assembled into modules, from India, Indonesia and Laos (for example 91 FR 58633, 58643, 58651 and 58658). Duty orders require an affirmative final injury determination by the U.S. International Trade Commission (USITC), and none was located in the Federal Register search performed on 10 October 2026. India, Indonesia and Laos supplied about 61.5% of January–August 2025 module import value versus about 12.7% in 2026 (modules only; Section 5.8). Commerce also made affirmative critical-circumstances findings in part. Any resulting orders would further separate customs value from delivered project cost. [CL-B-02]

The cost benchmark's module line and the proclamation's import-price floor belong to different cost boundaries and dates. The DOE/NLR U.S.-assembled benchmark is about $0.29/Wdc (2024 dollars) after the model's −$0.07/Wdc 45X subsidy and about $0.36/Wdc before it; neither figure is an imported-module or export price. A common nameplate-Wdc denominator and a product, origin and exception match have not been established. The nominal comparison signals a possible limit to factory-price transmission rather than a quantified duty-inclusive procurement saving. [R-A, P01]

## 5.8 Import value and sourcing shifts provide context, not a delivered-price series

The Census analysis covers monthly U.S. imports from January 2024 through August 2026 for specified solar cell and module classifications. Module customs value under HS 854143 is approximately $14.4bn in 2024 and $6.4bn in 2025. On the comparable January–August window, values are approximately $11.64bn, $4.43bn, and $2.82bn in 2024, 2025, and 2026. A decline in customs value can reflect quantity, product mix, reported unit value, and sourcing changes; it is not itself an estimate of end-market demand contraction or project savings. [R-T]

The reported country composition changes substantially. Vietnam and Thailand represent large shares in 2024, while Indonesia and Laos become more prominent in 2025; the 2026 January–August mix includes larger shares attributed to the Philippines, Ethiopia, and Kenya. These are the categories reported in the customs data. Identifying physical production routes, circumvention or the causes of sourcing shifts requires additional evidence.

For HS 8541430010, the January–August value-per-unit calculation is approximately $152.5 in 2024, $106.6 in 2025, and $105.5 in 2026. The quantity unit is an item, not watts. Module capacity, product specification, delivery terms, tariffs, and logistics are not sufficiently matched to convert this into a U.S. delivered price per watt. The data strengthen the trade context but leave the procurement bridge open.

> **Limits of this chapter.** (1) The component-to-overnight-cost bridge is illustrative and combines two national benchmarks. (2) Delivered quotes, product specifications and full trade applicability remain missing. (3) Only DC-basis benchmark component values are used.

# 6. Data-Center Demand: Annual Energy and Continuous Supply Are Different Products

## 6.1 National scenarios establish a range of modeled demand

Berkeley Lab's United States Data Center Energy Usage Report: 2025 Update, published in June 2026, presents seven scenarios for 2030 in Table 2. The reference case is 649 TWh. The compounded-uncertainty low and high cases are 521 TWh and 843 TWh, corresponding to 9.5% and 15.3% of U.S. electricity consumption. These are modeled scenarios, not statistical confidence intervals. [S04]

![Figure 6-1. U.S. data-center electricity-demand scenarios for 2030](figures/08_lbnl_scenarios.png)

*Source: Berkeley Lab / DOE, United States Data Center Energy Usage Report: 2025 Update, physical PDF page 11 / printed page 9, Table 2 [S04]. Coverage is all U.S. data centers, not AI alone or ERCOT.*

Presenting all seven cases preserves the sensitivity to deployment and technology assumptions. Selecting only the largest outcome would conceal the range of modeled demand. Translating any national case into regional generating-project orders requires additional evidence on location, project realization, and procurement.

## 6.2 Procurement requirements determine the product being sold

Annual renewable-energy procurement concerns energy or attributes over a defined period. Hourly matching introduces a time requirement. Continuous supply additionally requires arrangements for reliability and shortfalls. A solar system's annual contribution does not eliminate the need to address nighttime or low-output periods.

For developers, these distinctions affect obligations and risk allocation. As-generated purchases, fixed delivery blocks, and continuous supply place different quantity responsibilities on the seller or buyer. Contract prices and risks consequently depend on the product and obligations as well as demand.

This section sets out commercial mechanisms. No comparable sample of contracts has been assembled, so no specific customer's procurement terms are attributed to the market as a whole.

## 6.3 ERCOT's observed operating shapes illustrate the timing issue

The sample excluding the two DST transition days for 2025 contains 363 dates and 8,712 matched hours. Mean system solar output peaks at local hour-ending 14, while mean system load peaks at hour-ending 18. This describes average system operation, not the load profile of a particular data center. [S05]

The timing difference supports investigation of complementary supply and delivery products. It does not quantify unmet data-center demand. ERCOT includes other generation resources and non-data-center loads; subtracting the two system curves would not establish a customer's storage requirement.

## 6.4 Regional process evidence separates requested load from operating demand

ERCOT's regional process records separate requests, approvals and observed energized load. Commercial qualification additionally needs a customer, a connection date and a specified procurement product, all of which are distinct from the national energy-demand scenarios.

ERCOT's March 2026 status deck reports a 238.6 GW total in its 2030 large-load process table. Approximately 5.8 GW is classified as observed energized. The source defines that operating measure through historical noncoincident peak observations, so it should not be described as simultaneous metered demand. The other categories concern requests, studies, or approvals and represent materially different levels of completion.

The disparity between requested and operating quantities makes project qualification more important than the headline queue size. An equipment supplier or developer needs to know whether a prospective customer's location, electrical connection, construction schedule, and power procurement have progressed together. The public status table does not reveal customer-specific conversion probabilities or contracted solar requirements.

![Figure 6-2. Large-load process categories in the March 2026 snapshot](figures/S05_load_status.png)

*Source: ERCOT March 2026 large-load status table, 2030 column; GW. Category totals describe the source's process snapshot, not a probability-weighted load forecast. Observed energized is a noncoincident historical measure. The chart does not add Batch Zero quantities.*


September 2026 Batch Zero materials classify 204 projects and 66.4 GW as conditional base load, and 158 projects as conditional studied load. For studied load the deck gives two totals: 125.4 GW in the chart legend (physical page 6) and 127.9 GW in the summary text (physical page 1). The category values in the chart sum to 125.4 GW, so this report uses 125.4 GW and discloses 127.9 GW as the deck's alternative figure. No official correction had been published as of the report date. Final classifications follow ERCOT's verification process. Requests excluded from Batch Zero (373 projects, 302.2 GW) form a separate category. None of these September quantities is added to March's process total, because different dates, population definitions and conditional treatment prevent a defensible additive estimate. [R-C: Batch Zero deck, physical pages 1 and 5–8] [CL-B-03]

## 6.5 Self-supply evidence indicates a requirement for more than solar energy

The September deck reports resource power capacities associated with 11 WLPUN projects: approximately 12.824 GW of gas, 1.654 GW of solar, 0.637 GW of wind, and 0.330 GW of battery capacity. Gas represents approximately 83.0% and solar 10.7% of the reported mix. Component sums differ by 1 MW from the printed total, consistent with source rounding. These are reported power-capacity categories, including storage, rather than shares of generated energy or a census of data-center supply contracts.

![Figure 6-3. Resource power capacities associated with 11 WLPUN projects](figures/S06_wlpun_capacity.png)

*Source: ERCOT September Batch Zero deck; GW. Battery capacity is a power rating, not primary energy generation. The sample is not a census of data-center procurement.*

The sample points to a supply-service distinction: a solar offer to a buyer requiring continuous supply may need firming, storage or coordination with dispatchable generation. Procurement preferences outside the sample remain unmeasured. The sample does not quantify the cost premium for continuous supply, determine the optimal gas/solar/storage combination, or show that an individual buyer has selected a particular product; those conclusions require dispatch, reliability, fuel, emissions, network and contract analysis on a common service basis.

> **Limits of this chapter.** (1) Process requests and observed noncoincident peaks are different quantities. (2) March and September snapshots are not additive. (3) The 11-project self-supply mix is power capacity, not energy or a census of data-center procurement.

# 7. ERCOT Market Conditions: Location and Timing Jointly Shape Value

## 7.1 Market references and settlement exposure

Nodal prices provide historical references for specific settlement locations. Hubs and load zones provide broader market context. These locations are not interchangeable, and the hypothetical system has no documented actual settlement relationship.

The NP6-905-CD product examined here reports 15-minute real-time settlement-point prices. Combining day-ahead, real-time or different-location prices requires explicit identification of the change in price basis. Actual receipts may also depend on contracts, dispatch, fees, and quantity obligations. The modeled nodal revenue is gross energy value under the specified reference-price rule. [S06]

## 7.2 Intraday and seasonal system conditions

![Figure 7-1. Mean intraday load and solar output in ERCOT, 2025](figures/05_ercot_hourly.png)

*Source: ERCOT native-load and Solar/FINAL files, system hourly profile [S05]. The sample covers 363 dates, excluding the two DST transition days. Load and solar output are shown on separate panels and scales.*

![Figure 7-2. Seasonal ERCOT load and solar output, 2025](figures/06_ercot_seasonal.png)

*Source: ERCOT system seasonal aggregation [S05]. All 365 dates are used. Monthly mean load is weighted by actual source hours; solar is summed from source-aligned intervals. Annual coverage reconciles to 8,760 load hours and 35,040 solar intervals.*

Average load is approximately 66.4 GW in August and 46.7 GW in March. System solar generation is approximately 7.42 TWh in August and 3.34 TWh in January. These observations show seasonal variation. They do not isolate weather effects: installed-capacity changes, availability, and dispatch can also affect system generation. [S05]

The residual-load curve identifies the hours that still require other supply after wind and solar. It is a system timing comparison, with no inference about an individual plant's dispatch or achievable selling price.

![Figure 7-3. Load, wind, solar and residual load across the day, 2025](figures/Panel_Net_Load.png)

*Source: ERCOT hourly system panel [E-B]; arithmetic hourly means on the America/Chicago civil clock, all 2025 dates. Residual load equals load less wind and solar, before other generation, storage, imports and operational constraints; it is not a shortage measure.*


## 7.3 Regional screening requires more than solar-resource quality

A high-resource location need not be the preferred commercial location. Resource quality, construction cost, connection timing, and energy value may favor different sites. A regional ranking requires comparable site, cost, connection and settlement evidence beyond the single-node example.

A stronger screening framework would compare resource, network access, development conditions, and price exposure on compatible geographic and temporal bases. Network mechanisms require direct evidence; a low or negative price alone does not quantify a transmission constraint or connection delay.

## 7.4 Pipeline and network records support screening rather than guaranteed supply

The analysis uses EIA generator records and ERCOT pipeline snapshots with fuel, county, expected commissioning year, and process-status fields. These separate operating capacity from planned projects and show changes between successive snapshots. A signed interconnection agreement is stronger evidence of process advancement than an announcement, but commissioning, final costs and actual delivery remain separate milestones.

Installed and planned capacity must keep the source denominator. The records include ERCOT-area nameplate capacity and national net-summer capacity; dividing one by the other would create a mixed-basis market share. That comparison is excluded. Texas geography is also not identical to the ERCOT balancing-authority footprint.

Official transmission-constraint and interconnection materials identify mechanisms and locations warranting further examination. They do not by themselves attribute the reference node's negative-price exposure to a particular binding constraint. A causal assessment would require interval-level constraint status, shadow prices, dispatch or curtailment records, and a supported counterfactual. The grid-constraint hypothesis therefore retains its evidence limit.

> **Limits of this chapter.** (1) The prices are real-time settlement references. (2) Site settlement rights, losses, fees and price finality require project evidence. (3) Pipeline status and persistent price differences are screening information, with causes unassigned.

# 8. Solar Value Capture: High-Output Hours May Have Lower Prices

## 8.1 The reference-node price comparison

TAYGETE2_ALL is the historical price reference used in this study. ERCOT's resource-node mapping associates it with TAYGETE2_UNIT1/UNIT2 at substation TAYGETE2. ERCOT's resource list identifies two 101.9 MW units in Pecos County, West zone, with a 2023 in-service year. Their combined 203.8 MW, name, county and year match EIA plant 64075, Taygete II Energy Project: 203.8 MWac / 258.4 MWdc, single-axis PV, first in service July 2023. EIA names West Texas Solar Project II LLC, also identified in Comptroller agreement #1377. [F01]

The ERCOT-to-EIA step is an **attribute match on name, county, capacity and in-service year, not an official crosswalk**; no official crosswalk was identified, and the mapping files used are current (September/October 2026) versions rather than the 2023–2025 versions. The records support a same-county operating-plant reference, but the research records do not document why this node was originally chosen as the reference. The hypothetical 100 MWac system is not Taygete II, and its settlement rights at this node remain unestablished. The 2025 series provides 35,038 of 35,040 expected intervals. Its time-weighted price is $46.37/MWh and potential-generation-weighted price $22.13/MWh, before the negative-price response. [S06, S07]

The current owner's 2025 Comptroller filing reports a senior-lender-initiated foreclosure purchase after the previous owner failed to repay its loan. This is direct evidence of a financing event at the matched plant; it supplies neither an IRR nor the cause or scale of any investor loss. [F02, physical PDF p. 1, filing Section 2.7] The filing does not date the default or auction, so the event cannot be attributed to post-2023 operating prices at this node.

**Table 8-1. Reference node and hub comparisons, same output profile and common calendar.**

| Price year | Reference-node weighted price, $/MWh | West hub weighted price, $/MWh | ERCOT Bus Average hub weighted price, $/MWh |
|---|---:|---:|---:|
| 2023 | 64.89 | 64.94 | 67.70 |
| 2024 | 20.85 | 20.60 | 23.40 |
| 2025 | 22.13 | 21.46 | 24.94 |

*Source: weather-price comparison tables [E-A]; selection of TAYGETE2_ALL, HB_WEST and HB_BUSAVG. Potential-output weighting, before the shutdown rule; each year uses that year's simulated profile. Different years retain historical numerical price levels without CPI harmonization (Section 10.9).*

The West hub does not improve this particular 2025 weighted-price comparison. ERCOT Bus Average (HB_BUSAVG) is the 345-kV bus-average hub introduced under NPRR817, excluding Panhandle buses; it is a system reference rather than a four-hub simple average. [P09] Neither benchmark verifies the asset's settlement node or supplies the cash flows of a hub-settled contract.

**Reference-node status.** Section 8.5 shows where the node sits in the 2025 cross-section. [CL-FIN-06]

These results show why temporal alignment matters: annual generation multiplied by the average market price would omit the covariance between output and price. The capture ratio is specific to the priced output profile, and the observed relationship has no identified single cause.

![Figure 8-1. Hypothetical solar output and reference-node intraday prices](figures/S1_intraday_output_and_price.png)

*Source: NSRDB/PVWatts generation simulation and 2025 NP6-905-CD prices. The system design is hypothetical, and the reference node has not been established as its actual commercial settlement point. [S06, S07]*

## 8.2 Negative-price exposure and the assumed operating response

Negative prices occur in 2,189 available intervals, approximately 6.2% of priced intervals, but those intervals coincide with approximately 15.24% of potential simulated generation. Because negative prices overlap with high-output periods, they affect more energy than their interval count suggests. [S07]

The nodal route assumes zero exports whenever the reference price is below zero. Delivered energy falls to approximately 247.8 GWh, gross first-year energy revenue is approximately $6.55m, and the delivered-energy-weighted price is $26.43/MWh. The higher weighted price applies to the remaining exports; it does not indicate additional generation. [S08]

This calculation assumes complete responsiveness to interval prices; actual dispatch feasibility, negative-price contract provisions, and other market costs have not been verified. Economic shutdown in response to price also differs from forced curtailment, which requires separate operating or constraint evidence.

For comparison, exporting through negative prices gives modeled first-year receipts of $6.471m and NPV of −$87.20m in the rule-off sensitivity, versus $6.551m and −$85.97m when negative-price exports stop. This small difference is specific to the zero-incentive, pre-tax merchant case; contracts or production-linked benefits can change the preferred behavior. Receipts are derived from the generation-weighted price and output, and NPV from the sensitivity table. [S08]

## 8.3 Monthly outcomes separate volume from value

![Figure 8-2. Monthly simulated generation and price capture](figures/S2_monthly_energy_and_capture.png)

*Source: monthly generation and price pairing [S07, S08]. Potential generation, time-weighted price, potential-output-weighted price and delivered-energy-weighted price after shutdown are shown separately.*

March and August have similar simulated generation, approximately 27.5 GWh and 27.7 GWh, respectively. Their generation-weighted prices before shutdown differ substantially, at approximately $11.84/MWh and $31.11/MWh. Similar monthly energy volumes therefore do not imply similar revenue.

The monthly comparison includes simultaneous changes in weather, load, supply, and market conditions. It is a descriptive result rather than a causal attribution to any one mechanism.

## 8.4 A common three-year sample

The main comparison contains 485 resource nodes selected by explicit coverage and identity rules, rather than a random sample. All are RN-type points on the 10 September 2026 official list with complete prices on the shared published grid in 2023–2025. The current list does not establish each point's historical identity or commissioning date. The separate 641-node population requires complete coverage in 2025 only; excluded points are not automatically newly commissioned plants. Market-wide unpublished intervals are excluded uniformly; no price is interpolated or replaced with zero. One simulated output profile is valued against all nodes. The technical appendix documents the calendar and classification rules. [E-S] Counts refer to settlement points: some share identical receipt series (about 400 distinct three-year series among 485), and some are wind or storage resources. These shares do not count independent solar sites. [E-C, three-year node-receipt table]

## 8.5 Reference-node representativeness

In a separate 2025 cross-section, TAYGETE2_ALL lies near the 37th percentile of absolute production-weighted prices but near the third percentile of the ratio to its own time-weighted price. The low ratio indicates unfavorable timing relative to this node's own price level; it does not place the node at the 3rd percentile of absolute revenue. The 2025 distribution below and the three-year panel use different samples, and the node-selection and mapping limitations are stated in Section 8.1. [R-B]

![Figure 8-3. 2025 production-weighted price distribution](figures/S07_node_prices.png)

*Source: 2025 one-year resource-node cross-section [R-B]. Potential-output weighting precedes the export response. Detailed sample counts and the sample-reconciliation exhibit are in Appendix B.*

## 8.6 What the statistical comparisons indicate

Across the pooled hourly data, higher system solar output is associated with lower HB_BUSAVG hub prices after accounting for the included load, wind, gas, temperature and calendar measures. The pooled linear specifications (excluding the nonlinear and interaction models) give approximately −$2.7 to −$3.8/MWh per additional GW; the association is stronger in 2023 and weaker when extreme-price influence is reduced. These are conditional relationships, not the price effect of building an additional GW. Actual solar generation can also respond to price and dispatch, while missing outages, imports and constraints leave important common drivers unmeasured. [E-B]

## 8.7 What the statistical comparisons can be used for

The analysis does not yield a stable relationship between solar output and the probability of a negative hourly price across model choices. A negative hourly mean is also a different outcome from a negative 15-minute interval. The 2025 prediction test performs worse than simple historical averages: approximately $66/MWh root-mean-square prediction error versus $45 for an hour-of-week average and $39 for a constant benchmark. The regressions are useful for examining a mechanism; they should not supply future project prices or receipts. Both changing market price levels and extreme-hour errors matter to this prediction failure. Coefficients, uncertainty methods and nonlinear-model qualifications are in Appendix B. [E-B]

![Figure 8-4. Observed price patterns and negative-hour incidence](figures/empirical/F6_price_vs_solar_and_negative_hours.png)

*Source: hourly benchmark and system-solar data [E-B]. Binned patterns are descriptive; hourly aggregation and other changing conditions limit their interpretation. Colors distinguish years. Left panel: circle, square and triangle markers identify yearly mean prices; thin dotted lines with crosses are medians. Right panel: negative-hour incidence by America/Chicago civil-clock hour, not a count of negative 15-minute intervals.*

## 8.8 Node basis persists, but its cause remains unidentified

The rank correlation of node mean basis to HB_BUSAVG is approximately 0.77–0.88 across pairs of years. A descriptive variance decomposition assigns approximately 83.4% of node-year mean-basis variation to node identity, 0.4% to common year differences, and 16.2% to the remaining node-by-year component. This shows persistence in the sampled price differentials; it does not identify the economic cause of that persistence. [E-B]

![Figure 8-5. Cross-year persistence of node basis](figures/empirical/F7_node_basis_persistence.png)

*Source: multi-year analysis, node-basis tables. Basis is node price less the specified benchmark, not a direct measure of congestion cost. The panel uses one current classification snapshot. The right panel displays basis volatility only up to $200/MWh; some nodes exceed this range.*

The load-zone association results add geographic context, but do not isolate congestion. Persistent differences could reflect network conditions, settlement definitions, supply composition, or other unobserved factors. Direct interval constraints, shadow prices, dispatch information, and a supported counterfactual would be required for a stronger attribution.

> **Limits of this chapter.** (1) One simulated site profile is priced at different nodes; these are not different asset valuations. (2) Output weighting precedes the negative-price response unless labeled otherwise. (3) Regressions describe associations; forecast performance is weak and network causality is unresolved.

# 9. Independent Generation Simulation: Resource, Design, and Weather-Year Effects

## 9.1 Reference location and weather coverage

The hypothetical system uses NSRDB grid cell 1142134 near the Pecos County internal point, at approximately 30.78°N, 102.71°W, about 1.08 km from that reference. The location is neither a county average nor a verified operating asset site. [S07]

Variables include irradiance, temperature, wind speed and surface albedo. The NSRDB fill flag is non-zero for 4.1% of 2025 five-minute records: codes 1, 5 and 7 account for 1.25%, 1.24% and 1.62% of records. The non-zero share is 2.8% for 2023 and 2.5% for 2024. Flagged records are used as published, with no record removed or replaced. Their effect on simulated output has not been quantified. [CL-B-04]

The three-year extension adds 2023 and 2024 extracts from the same weather location (Section 9.4). An actual weather year describes the conditions of that year; it does not establish long-run typical output or a probability distribution of generation.

## 9.2 System configuration

**Table 9-1. Hypothetical system design.**

| Parameter | Setting | Evidence class |
|---|---:|---|
| AC / DC capacity | 100 MWac / 132 MWdc | Hypothetical case scale |
| DC/AC ratio | 1.32 | Reference design |
| Tracking | Single-axis with backtracking | Reference and design assumptions |
| Ground-coverage ratio / inverter efficiency | 0.30 / 96% | Software defaults |
| Bifaciality | 0.70 | Analytical assumption |
| Initial aggregate losses | 14.0757% | Software loss stack |
| Annual degradation | 0.7%, from operating year 2 | Cash-flow reference assumption |

Generation is simulated with PVWatts; the software version is recorded in Appendix B.2. Degradation and subsequent export reductions are applied in the financial layer, while availability is already included in the initial loss stack and is not deducted again. These conventions prevent the same loss from being applied twice. [S07, S09]

## 9.3 Generation and design sensitivities

Potential first-year generation is approximately 292.4 GWh, equivalent to an AC capacity factor of 33.38% under the assumed DC/AC ratio of 1.32, single-axis tracking and bifacial design. These design choices raise output per unit of inverter capacity; the factor is not an observed fleet benchmark. Tests using aggregate losses of 10% and 18% produce approximately 302.4 GWh and 280.7 GWh, respectively. The monofacial test produces approximately 282.3 GWh. Annual generation at the other sampled weather locations ranges from approximately 290.6 GWh to 299.2 GWh. That range describes the sampled locations rather than the county as a whole. [S07, S10]

These results quantify the influence of selected design and loss assumptions. They are not plant-performance guarantees. Terrain, actual layout, seasonal soiling, equipment failures, and construction quality have not been constrained by site-specific evidence. AC capacity factors and DC energy yields require their respective denominators and are not interchangeable.

## 9.4 Three weather years improve comparison without establishing long-run uncertainty

The extension adds 2023 and 2024 weather from the same NSRDB cell and retains the 2025 design. Annual AC generation is approximately 282.3, 292.1, and 292.4 GWh, a spread of about 3.6%. The comparison shows observed weather-year variation within this simulation; it does not estimate the long-run output distribution, a P50, or a P90. [E-S]

Calendar handling and the leap-day approximation are documented in Appendix B.

## 9.5 Operating-plant evidence: a plausibility check, not calibration

The operating-plant comparison joins EIA-923 net generation with EIA-860 plant design and capacity records. The EIA county field defines an **EIA-record Pecos cohort**. The full-year standalone screen excludes hybrid sites, partial years, multi-unit aggregates and annual respondents. Because the standalone cohort also includes plants not flagged as tracking, a separate screen keeps only plants with EIA tracking flag Y. [F03]

**Table 9-2. Operating AC capacity factors under explicit sample definitions.**

| Year | Screen | Plants | Median AC capacity factor |
|---|---|---:|---:|
| 2024 | All tracking types | 10 | 24.8% |
| 2024 | Tracking Y | 9 | 23.8% |
| 2024 | Tracking Y; Emerald excluded | 8 | 23.4% |
| 2025 | All tracking types | 11 | 24.6% |
| 2025 | Tracking Y | 10 | 25.0% |
| 2025 | Tracking Y; Emerald excluded | 9 | 24.5% |

*Source: EIA comparison table [F03]; cohort screening in `data/finance/EIA-Cohort-Reconciliation.csv`. Capacity factor = annual generation / (2025 recorded MWac × calendar hours); 2024 has 8,784 hours. Full-year and COD screening does not independently establish every historical nameplate denominator.*

![Figure 9-1. 2025 operating capacity factors and simulated output](figures/Finance_Operating_CF.png)

*Source: EIA-860/923 comparison outputs [F03]; scenario design [S07]. Emerald Grove is classified as Pecos in the EIA record but Crane in ERCOT/Comptroller records; the table reports the result with that plant excluded. Other observed differences in technology, design, availability, curtailment and weather remain uncontrolled.*

The broader standalone cohort has medians of 24.8% in 2024 and 24.6% in 2025; restricting it to tracking Y gives 23.8% and 25.0%. The simulated 2025 potential factor of 33.38% exceeds every observed plant in these screened cohorts. Its 28.29% delivered factor falls within the 25.5%–29.7% range for three plants with 2023–2024 commercial operation dates (COD): Taygete II, Emerald Grove and Greasewood II. That overlap does not validate the simulated system. Net operating generation and potential simulated output have different loss and operating boundaries, and the observed values are not weather-normalized.

**Operating-benchmark boundary.** The EIA comparison uses each plant's 2025 recorded AC nameplate capacity as the denominator for both 2024 and 2025 generation, so a capacity change between years would bias the 2024 factor.

Plant-level availability, forced outage and curtailment are not publicly disclosed for the screened plants. Only system-level indicators are available, and they come from different sources and years:
- Berkeley Lab reports 7.1% solar curtailment in ERCOT for 2024.
- The ERCOT Independent Market Monitor reports that roughly 6% of ERCOT solar generation was curtailed in 2025.

These indicators show that net operating generation already excludes material curtailed energy. They do not apportion the gap between the simulated 33.38% potential factor and the 24.6%–25.0% screened medians among weather, design, availability and curtailment. The simulated output is therefore not calibrated, and no P50/P90 is available. The 10% export sensitivity, which adds about $10.14m to NPV with costs unchanged, is a sensitivity and not a calibrated forecast. [CL-FIN-02]

> **Limits of this chapter.** (1) Output is simulated for a reference weather location and assumed design, and is not calibrated to operating plants. (2) Three weather years do not establish P50/P90 output. (3) Weather fill flags are counted and disclosed but not used to filter or adjust output; the leap-day approximation and time mapping are described in Appendix B.

# 10. Financial Scenarios: Cash-Flow Definitions Precede Return Interpretation

## 10.1 Timing, currency basis, and model scope

The model assumes all capital expenditure is paid at the end of 2026, followed by 30 operating years from 2027 to 2056. Real values are expressed in 2025 dollars, and NPV is measured at the 2026 valuation point. ATB capital and fixed operating costs, originally in 2023 dollars, are converted using CPI-U, with a factor of approximately 1.0566. [S08, S09]

The analysis is pre-tax and unlevered. Income taxes, tax incentives, depreciation tax shields, debt proceeds, interest, and principal repayments are excluded. These are scope choices rather than findings that such items are immaterial to an actual project.

The 4.27% real discount rate is derived from the ATB workbook's reference nominal debt cost of 6.5%, equity return of 8.0% and debt fraction of 0.7457, without a tax shield: [(0.065 × 0.7457 + 0.080 × 0.2543) + 1] / 1.025 − 1 ≈ 4.27%. It is a scenario discount convention, not a verified project WACC or investor hurdle, and results at 6% and 8% are reported alongside it. [S09]

## 10.2 Cost coverage and unquantified items

Base capital expenditure is approximately $1,436.75/kWac, or $143.67m, using ATB OCC plus GCC. Fixed O&M is approximately $24.49/kWac-year. Variable O&M follows the ATB value of zero; this does not imply that other cost categories are zero. [S08]

Additional assumptions include $35/kWac of replacement expenditure in operating year 16 and $30/kWac of net decommissioning expenditure in year 30. Replacement costs may overlap with component-failure provisions in FOM; a zero-replacement sensitivity is reported (Section 10.7), but it does not rule out every potential overlap. ATB fixed O&M includes broad system, property and administration expenses, including insurance and component-failure allowances. Its published categories do not establish this site's actual land, property-tax or insurance payments. A project-specific crosswalk is required before adding costs, so included benchmark categories are not counted twice. Network and market-service obligations also require documented scope. [S09]

The ±20% CAPEX and ±30% FOM sensitivities are selected analytical stresses. They are not verified bounds on unknown costs and do not demonstrate that all omitted categories are covered.

## 10.3 Two distinct revenue mechanisms

The nodal route uses the 2025 reference-price and output shapes, holds the base price profile constant in real terms over subsequent years, and adjusts output for degradation. Exports during negative-price intervals are set to zero. The price path is a scenario convention, not a forecast; the hypothetical plant's impact on market prices is not modeled.

The simplified node-level fixed-price route is a paid-volume arrangement, not an observed PPA and not a hub-settled virtual PPA. It holds $40/MWh constant in nominal terms for the full 30-year life and deducts 15.24% of potential energy from payment. That deduction is borrowed from the negative-price energy share solely as a stress assumption. Its downside value, 30.48%, doubles the stress rather than describing an empirical contract clause. Inflation reduces the real value of the flat nominal price.

The 2025 price averaged over negative-price energy is only about −$1.79/MWh. For a buyer who pays the fixed price through those intervals, physical negative prices do not automatically erase contract receipts; actual economic shutdown depends on energy settlement, contract rights, production incentives and delivery obligations together.

**Paid-volume stress.** Holding the contract cash-flow shape and costs fixed, the flat nominal break-even is $55.91/MWh at zero unpaid energy, $65.97/MWh at the 15.24% base share, and $80.43/MWh at 30.48%. The last value is arithmetic scaling of paid volume, not a new dispatch or contract simulation. [F04]

**Hub-settled contracts.** For a simplified hub-settled financial contract, interval receipts would be **node energy receipts + contracted quantity × (strike price − hub price)**, before fees, deviations and other clauses. If contracted quantity equals generated output, node-to-hub basis remains an exposure. Different volume shapes, negative-price provisions, payment suspensions and credit terms can change the result. REC proceeds and fees are separate from the two energy-settlement legs, and fixed-shape hedge quantities, shutdown provisions and losses can break the matching-volume simplification. A hub hedge transfers price and shape exposures; substituting hub prices for node receipts does not model the hedge.

The output-weighted reference-node-minus-West basis is −$0.05, +$0.25 and +$0.67/MWh for 2023–2025. West hub weighted prices are $64.94, $20.60 and $21.46/MWh, with capture ratios 1.30, 0.75 and 0.65. A small annual weighted basis does not establish a small interval basis or low contract risk. [F04]

**Separately versioned hub-hedge calculation.** This calculation models the hypothetical plant selling metered output at the reference node, with a financial swap at HB_WEST. The swap pays contract quantity × (strike − hub price) with quantity equal to generation, over a 10- or 15-year tenor followed by a merchant tail at the node. The tail repeats the 2025 price path and is a scenario, not a forecast. Fees, REC cash flows and imbalance charges are omitted from this calculation; their economic values are unknown, rather than established as zero.

On the 2025 price path at 4.27% real, the break-even flat nominal strike ranges from **$60.6/MWh** to **$84.8/MWh** across the eight tenor, dispatch and negative-hub-clause combinations. With a 10-year tenor and a $40/MWh strike, the merchant tail supplies about 43% of revenue present value. The break-even therefore depends heavily on the unsourced tail price. At 6% and 8% the break-even strikes rise to about $68–$107/MWh.

These are hypothetical contract settings, and the original six scenarios are unchanged.

**Public contract evidence.** A lender release identifies a long-term J. Aron hedge for part of Taygete I output and another rated purchaser. The developer's 9 December 2020 press release for Taygete I (250 MWac), available as a screenshot rather than an executed agreement, states that the project's sole tax-equity investor, Nestlé, will also purchase 100% of the project's renewable electricity attributes, estimated at 750,000 MWh per year, for 15 years. That is the disclosed tenor of the environmental-attribute agreement, not of the energy hedge. No complete executed energy contract is available: its strike, tenor, settlement hub, volume rule, negative-price clauses and credit support remain undisclosed, and no indicative offer is treated as a comparable transaction. [F05; CL-FIN-03]

**Table 10-1. Scenario settings — price, cost and operating assumptions.**

| Scenario | Price rule / level | Unpaid energy / response | CAPEX $/kWac | FOM $/kWac-year | Initial losses | Degradation /yr | Inflation /yr |
|---|---|---|---|---|---|---|---|
| Node base | 2025 reference profile; +0.0%/yr real | Stop exports below $0 | 1,436.7 | 24.49 | 14.0757% | 0.7% | 2.5% |
| Node downside | 2025 reference profile; −1.5%/yr real | Stop exports below $0 | 1,504.1 | 25.05 | 18% | 1.0% | 2.5% |
| Node upside | 2025 reference profile; +0.5%/yr real | Stop exports below $0 | 1,346.9 | 23.77 | 10% | 0.5% | 2.5% |
| Fixed base | $40/MWh nominal flat | 15.24% | 1,436.7 | 24.49 | 14.0757% | 0.7% | 2.5% |
| Fixed downside | $32/MWh nominal flat | 30.48% | 1,504.1 | 25.05 | 18% | 1.0% | 2.5% |
| Fixed upside | $48/MWh nominal flat | 15.24% | 1,346.9 | 23.77 | 10% | 0.5% | 2.5% |

*Sources: scenario input register and scenario outputs [S08, S09]. CAPEX and FOM are in real 2025 dollars. Downside/base/upside costs follow ATB Conservative/Moderate/Advanced technology cases, respectively; the labels describe bundled assumptions, not probabilities. Replacement is $35/kWac in operating year 16 and net decommissioning $30/kWac in year 30 across all cases. Nodal delivery responds to each interval price; its negative-price output share is endogenous. Fixed-route shares are imposed assumptions.*

The 2.5% inflation input follows the ATB workbook's financial-assumption row 52. For Fixed base, 247.8195 GWh × $40/MWh gives $9.9128m nominal receipts in 2027; dividing by 1.025 squared gives $9.4351m in 2025 dollars. The two-year deflation follows the model's stated calendar convention.

## 10.4 Scenario results

**Table 10-2. Six scenarios priced at reference node TAYGETE2_ALL or the fixed contract setting.**

| Scenario | First-year delivered (node) / paid (fixed), GWh | First-year real revenue, $m | NPV at 4.27% / 6% / 8%, $m | Real LCOE at 4.27%, $/MWh | Single real IRR |
|---|---:|---:|---|---:|---|
| Node base | 247.8 | 6.55 | −86.0 / −95.3 / −103.3 | 48.9 | Not a single rate: multiple roots |
| Node downside | 237.7 | 6.27 | −114.6 / −118.9 / −122.9 | 54.8 | Not a single rate: multiple roots |
| Node upside | 256.6 | 6.80 | −63.3 / −75.7 / −86.2 | 43.6 | −0.42% |
| Fixed base | 247.8 | 9.44 | −73.7 / −82.8 / −91.0 | 48.9 | Not a single rate: multiple roots |
| Fixed downside | 195.2 | 5.94 | −125.4 / −127.5 / −129.7 | 66.7 | No root found (search not certified complete) |
| Fixed upside | 256.3 | 11.71 | −33.5 / −47.5 / −60.0 | 43.7 | Not a single rate: multiple roots |

*Source: six-scenario cash-flow outputs [S08, S10]. Upside and downside bundles have no probabilities assigned. Fixed-route LCOE uses paid energy as its denominator. Fixed base LCOE equals Node base because the 15.24% unpaid share was set equal to the node's negative-price energy share; the gap between Fixed downside and Node downside LCOE arises only from the denominator.*

![Figure 10-1. Scenario NPV under three real discount rates](figures/Panel_Scenario_NPV.png)

*Source: scenario outputs [S08, S10]; six hypothetical scenario settings under the stated unlevered financial assumptions. These results are not verified asset returns.*

## 10.5 Operating receipts and capital recovery answer different questions

![Figure 10-2. Annual real cash flows](figures/S4_annual_cash_flows.png)

*Source: annual scenario cash flows [S08]. Initial capital expenditure, operating flows, replacement and decommissioning are shown separately. Left panel: Node base; right panel: Fixed base. The axis is limited to ±$20m, so the initial capital bar extends beyond the plotted range.*

In both base cases, revenue exceeds modeled FOM in every operating year, although the difference between the reference allowance and actual operating obligations remains unverified. Cumulative undiscounted real cash flow nevertheless remains negative in both base cases: the modeled revenue does not recover the defined capital outlay and subsequent costs over the operating period.

The shortfall is specific to the tested revenue and cost definitions; actual procurement, contracts, incentives and financing may produce different outcomes. It is not a market-wide finding about solar development.

## 10.6 LCOE, contract duration and IRR

Base LCOE is $48.85/MWh using delivered energy and 4.27% real discounting. Using potential generation instead gives $41.41/MWh because the denominator includes energy not sold. Both measures use the same real cost stream; a flat nominal contract needs a separate inflation adjustment. [S08]

In Fixed upside, first-year realized price is $45.69/MWh and real LCOE is $43.69/MWh, yet NPV is −$33.45m. The contract price stays flat in nominal terms, so its real value falls with 2.5% annual inflation. A first-year price above a constant-real levelized cost therefore does not ensure lifetime capital recovery.

All six scenarios have negative NPV at the modeled positive discount rates. A single IRR is not a reliable comparison here: four of the six cases have more than one numerical root, the Node upside case has a unique root of about −0.42%, and no root at or above 4.27% was found. NPV and cash flows therefore provide the decision measure; the roots are listed in Appendix B.2. [S10]

## 10.7 Benchmark scope and project cost reconciliation

The cost crosswalk distinguishes modeled national overnight cost from observed commissioned-project cost. Berkeley Lab's utility-scale publication reports a 2024 commissioned-project cost reference of approximately $1.22/Wdc or $1.61/Wac. Its coverage and sample differ from PVSCM, and the publications use different deflation conventions. A shared real-dollar label does not make the figures fully harmonized, and attributing the difference to scope requires a component-level reconciliation.

PVSCM's land-lease and operating-cost treatment also differs from a complete site budget. Benchmark O&M or replacement allowances should be reconciled before combining them with scenario cash-flow lines. Public reference costs do not verify the hypothetical site's land, insurance, property tax, market-service, network-upgrade, or decommissioning obligations.

**Limited-scope cost observations.** Nine named comparables comprise eight standalone PV plants and one storage-hybrid site; two standalone plants entered service in 2021 and are earlier-vintage references. Five selected Comptroller filings imply $0.92–$1.10/Wac of self-reported qualified investment. These are mid-2023 nominal amounts divided by 2025 recorded capacity, with COD/reporting inconsistencies and possible later spending. Qualified investment excludes land and property outside the applicant's qualifying ownership scope and does not reconcile every soft or financing cost. The figures are neither all-in construction prices nor a return range. [F01, F04]

![Figure 10-3. Selected qualified-investment observations](figures/Finance_Qualified_Investment.png)

*Source: Comptroller Form 773 amounts and EIA capacity [F04]. Narrow reporting scope and mismatched vintages preclude replacing the $1.437/Wac national scenario input. The five selected comparisons exclude zero-spend and clearly incomplete construction cases; other observations are documented in the finance supplement files.*

**Replacement accounting.** PVSCM itemizes annualized component replacement alongside land, insurance, property and administration expenses. Its linkage to ATB is inferred from ATB citations, and the exact FOM vintage and component amount used here have not been reconciled. The year-16 reserve therefore remains in the baseline. A separate accounting variant removes only the $3.5m real reserve, improving either base NPV by **$1.79m** at 4.27%: node **−$84.17m**, fixed **−$71.95m**. This arithmetic sensitivity identifies the scale of possible overlap without asserting that the entire reserve is duplicated. [F04]

**ERCOT connection-cost allocation.** Under 16 TAC §25.195(f), a generator pays its step-up transformers and protective devices. For SGIAs executed after 31 December 2025, transmission-provider interconnection-facility funding is capped at an allowance: $14m at or below 138 kV and $20m above 138 kV in the 2024 base, indexed annually by CPI. The applicable allowance is fixed at the generator's notice-to-proceed date; costs above it are billed to the generator. Defined shared system upgrades remain the transmission provider's responsibility, while connection substations are not treated as shared upgrades. [F06]

These allowances are not deductions from the national $17.63m GCC input. The facility scope, voltage, agreement date and ownership of the hypothetical connection are unverified. Likewise, a generic PVSCM network line cannot be removed from ATB GCC before a component match. Site-specific property tax should replace or reconcile the embedded allowance, not be added in full to unchanged FOM.

**Cost scope and vintage.** The scenario CAPEX uses ATB 2025 overnight capital cost (OCC) plus grid-connection cost (GCC), 2026 values, converted from 2023 to 2025 dollars. ATB 2025 states that its 2024 overnight cost is based on modeled pricing for a 100-MWdc one-axis tracking system quoted in Q1 2024 (DOE, 2024), adjusted by an ILR of 1.32, and that 2024 fixed O&M of $24.66/kWac-year splits into system ($10.88), property ($11.41) and administration ($2.38) expenses. The rounded components sum to $24.67; the published total is $24.66. The component analysis in Chapter 5 instead uses PVSCM 2025Q1. The two are therefore related but not identical cost vintages, and the module share from PVSCM 2025Q1 is applied to ATB OCC only as an illustration. The $24.66 FOM quote refers to 2024 source pricing; its dollar basis has not been separately reconciled here with the ATB workbook. The scenario's $24.49 uses the 2026 Moderate projection converted from 2023 to real 2025 dollars.

PVSCM itemizes a network-upgrade line inside electrical balance of system ($66/kWac in the 2024Q1 inputs and $51.26/kWac in 2025Q1) and annualized inverter and component replacement inside O&M. A generic network-upgrade allowance and a separate year-16 replacement reserve may therefore overlap with costs already embedded in the benchmarks; the overlap cannot be quantified without the ATB component table.

Texas property-tax relief for a new standalone PV plant is narrower than for earlier projects. Tax Code Chapter 313 no longer provides new appraised-value limitations, and Government Code §403.602(8)(B) excludes non-dispatchable generation from the JETI program. The PVSCM property-tax allowance of 0.2% of system price per year is therefore not a verified Texas liability. [CL-FIN-05]

**Table 10-3. Cost-scope crosswalk: benchmark coverage and unresolved site costs.**

| Item | In ATB OCC | In ATB GCC | In FOM / PVSCM O&M | Scenario line | Status |
|---|---|---|---|---|---|
| Modules, inverters, trackers, BOS | Yes | No | Replacement lines in PVSCM O&M | OCC | Included; replacement overlap possible |
| Generator step-up and protection | No | Yes (national row) | No | GCC | Included; site value unknown |
| TSP interconnection above allowance | No | Possibly | No | GCC | Rule-dependent; site study absent |
| Network upgrades | Possibly (PVSCM line) | Possibly | No | OCC and/or GCC | Possible overstatement in ERCOT |
| Land lease, insurance, management | No | No | Yes | FOM | Included; do not add again |
| Texas property tax | No | No | 0.2%/yr of price | FOM | Gap risk; site tax needed |
| QSE fees, imbalance, RECs | No | No | No | None | Not modeled; not zero-cost |
| Construction financing | Excluded | Excluded | — | Excluded | Excluded by convention; capital timing within the construction year not modeled |
| Year-16 replacement reserve | — | — | Possible overlap | $35/kWac | Zero-reserve variant +$1.79m |

*Sources: ATB 2025 utility PV page and workbook rows in the scenario register [S09, P10]; PVSCM 2024Q1/2025Q1 parameter files as itemized in the finance supplement [F04]; 16 TAC §25.195(f)(1)–(3), pp.2–3 [F06]; Texas statute excerpts [CL-FIN-05].*

## 10.8 Tax timing and basis: an illustration, not an entitlement

The six baseline scenarios remain pre-tax and unlevered. The illustration applies an assumed 30% rate only to **$126.04m of national PV overnight cost (OCC)**, excluding $17.63m GCC from the assumed basis. With a timing convention of 2026 nominal basis, unchanged nominal receipt at end-2027, 2025-dollar deflation and one-year discounting at 4.27%—the credit PV is **$35.38m**. Node-base NPV becomes **−$50.59m**, fixed-base NPV **−$38.36m**, and fixed-route break-even **$53.51/MWh**. No benefit is inserted into the original six scenarios. [F04]

Applying the same rate to full CAPEX would give $40.33m PV. Excluding GCC reduces it by $4.95m. This is a conservative boundary for an unresolved national aggregate, not a determination that every OCC item qualifies or every generator-owned connection asset is ineligible. The special qualified-interconnection-property provision of section 48E applies only to facilities no larger than 5 MWac; it does not establish eligibility for this 100 MWac setting. [F07]

**Table 10-4. Timing branches requiring project evidence.**

| Construction and service facts | Timing interpretation | Treatment here |
|---|---|---|
| Construction begins on or before 4 July 2026 | Outside the new end-2027 termination branch, subject to other requirements | No qualifying start evidence supplied |
| Construction begins after 4 July 2026; service by 31 December 2027 | Service cutoff may be satisfied | Illustrative late-start route; schedule unverified |
| Construction begins after 4 July 2026; service after 31 December 2027 | Relevant wind/solar termination applies | No credit assumed |

*Source: P.L. 119-21 sections 70512/70513 [F07]. Payment at end-2026 is not evidence of actual construction commencement. The early-start branch remains available for evaluation if supported by qualifying contemporaneous records; for construction starting after 4 July 2026, only the placed-in-service-by-2027 branch can apply.*

Notice 2025-42 on the beginning of construction was vacated by a District Court on 6 June 2026 and is not treated as controlling; the docket status is set out in Appendix C. [CL-FIN-04]

For facilities beginning construction after 2025, the material-assistance test includes a cost-ratio threshold of 40% for a 2026 construction start and 45% for 2027. These are the defined material-assistance cost ratios, not percentages of module origin or a generic permitted foreign-content share. Taxpayer ownership/control, supply-chain tracing and the applicable safe-harbor rules also matter. [F07; F09]

The 30% rate, wage/apprenticeship compliance, qualified basis, transfer price, cash timing and recapture exposure remain assumptions or missing inputs. An eventual after-tax model must reflect the section 50(c)(3) basis reduction—half the credit—as well as depreciation and other taxes. This edition does not claim the illustration is a complete after-tax NPV. [F07]

**Tax qualifications.** The statutory timing branches (Table 10-4), the material-assistance thresholds and the 5 MWac limit on the special interconnection-property provision are taken from the statute and IRS notice text. The hypothetical case has no construction-start date, placed-in-service date, owner, supplier certifications, wage and apprenticeship records, or transfer agreement, so the $35.38m OCC-basis credit illustration is a conditional scenario, not an eligibility finding or an after-tax valuation. Its variants, all as PV at 4.27%, are: receipt one year later, $33.10m; transfer at 0.90 per credit dollar, $31.84m; and a 6% statutory credit rate (prevailing-wage and apprenticeship conditions not met), $7.08m. [CL-FIN-04]

> **Illustration — production credit.** A qualifying facility can elect the section 45Y production credit instead of the investment credit, not both. The 2025 applicable amount is 3.0¢/kWh when prevailing-wage and apprenticeship (PWA) requirements are met and 0.6¢/kWh otherwise, adjusted annually for inflation. The illustration pays $30/MWh, held constant in real 2025 dollars, on the base delivered energy (247.8 GWh in the first year, 0.7% annual degradation) for 10 years, discounted at 4.27% real in the year of production. Its PV is **$57.80m**: node-base NPV becomes −$28.17m, fixed-base NPV −$15.94m, and the fixed-route break-even **$45.61/MWh**. Transferred at $0.90 per credit dollar, the PV is $52.02m and the break-even $47.65/MWh; at the 0.6¢ base rate, $11.56m and $61.90/MWh. The timing branches in Table 10-4 and the eligibility conditions above apply unchanged, and the result is pre-tax NPV plus a credit, not an after-tax valuation. [M05]

## 10.9 Historical price-year substitution changes the sign of modeled NPV

The extended empirical scenario preserves the pre-tax unlevered cost structure and the 4.27% real discount rate. Under those assumptions, discounted project value is an affine function of first-year modeled receipts: approximately NPV = 15.47 × receipts − $187.3m for the constant-real nodal route. Each extra $1m of first-year real receipts adds approximately $15.47m to NPV under this convention; the identity does not apply directly to the flat nominal contract. The revenue threshold is about $12.1m. The multiplier incorporates the degradation and discounting assumptions. The $187.3m intercept comprises initial CAPEX and the present value of modeled fixed operating costs, replacement and decommissioning; this is a cash-flow identity, not a market valuation multiple. [E-A, E-C]

**Table 10-5. Same-year comparison: median across 485 resource nodes.**

| Same-year price and weather pairing, common calendar | Median first-year receipts, $m | Median NPV if the setting repeats for 30 years, $m | Share of 485 screened nodes with positive NPV |
|---|---:|---:|---:|
| 2023 | 18.56 | +99.8 | 100% |
| 2024 | 6.83 | −81.6 | 2.68% |
| 2025 | 6.85 | −81.3 | 0.41% |

*Source: multi-year analysis, weather-price matrix summary. All rows use the hypothetical Pecos profile, common calendar, negative-price export rule, and identical finance assumptions. Medians describe each distribution separately; no actual asset portfolio is valued.*

**Currency qualification.** The historical price files keep their original nominal numerical levels. The financial experiment reuses each level as a constant-real-2025 scenario assumption; 2023 and 2024 prices were not CPI-converted before reuse. These are fixed-cost scenario contrasts, not fully inflation-harmonized historical investment returns. A CPI-restated version is reported below.

**Table 10-6. Discount-rate sensitivity of same-year median NPV; $m.**

| Real discount rate | 2023 setting | 2024 setting | 2025 setting |
|---|---:|---:|---:|
| 4.27% | +99.78 | −81.59 | −81.26 |
| 6% | +58.61 | −91.68 | −91.40 |
| 8% | +23.55 | −100.34 | −100.12 |

*Source: annual cash-flow cost stream and same-year receipts [E-A]; 485-node common-calendar sample. No price forecast or regression is involved.*

**Comparable returns remain undisclosed.** Public records for the nine named ERCOT plants contain three kinds of financial observation: a financing amount (Taygete I), a lender-initiated foreclosure (Taygete II), and self-reported qualified investment (Comptroller Form 773). Each answers a different question. None reports a project or equity IRR, a project-level cash-flow series, or the return definition needed for comparison (levered or unlevered, pre- or post-tax, target or realized, development or acquisition), so no defensible "typical solar IRR" range can be formed. The ATB 6.5% nominal debt and 8.0% equity assumptions equal 3.90% and 5.37% real at 2.5% inflation, respectively; they are reference inputs, not observed investment returns. The model keeps its 4.27% real convention, a pre-tax analytical rate rather than a market hurdle rate; NPV results at 6% and 8% show the effect of higher required returns. [F01, F04]

**CPI-restated price years.** A CPI-restated variant restates the 2023 and 2024 nominal price levels in 2025 dollars using CPI-U annual-average ratios of 1.0566 and 1.0263. All other inputs are unchanged. The restatement raises the value of the older price years without changing the signs of the reported comparisons:
- reference node 2023: NPV moves from +$97.76m to +$113.89m;
- reference node 2024: NPV moves from −$92.15m to −$89.64m;
- 485-node median 2023: NPV moves from +$99.78m to +$116.02m.

The share of nodes with positive NPV is unchanged in every year: 100% in 2023, 2.7% in 2024 and 0.4% in 2025. The same-year results in Tables 10-5 and 10-6 remain the primary presentation, and the CPI version is a purchasing-power check on them.

The CPI-restated 2024 median uses the full-year calendar; Tables 10-5 and 10-6 use the common-calendar sample. Those medians are not interchangeable. The reference-node 2024 comparison above is on the common-calendar basis. [CL-FIN-07]

All 13 positive 2024 nodes map to the South load zone, with 10 distinct receipt series among them. The mapping is descriptive and does not identify an actual asset portfolio.

Positive cases are therefore not exclusive to 2023; what distinguishes 2023 is their prevalence across the sample and their dependence on that year's high-price opportunities. The reference node is negative in 2024 and 2025; the sample contains a small positive tail. Neither statement should be substituted for the other.

The original six scenarios in Section 10.4 remain 2025-based cost and commercial stress settings. They are not replaced by the three historical-year experiments. Taxes, financing, actual commercial mapping and complete project cost remain absent from both sets.

## 10.10 Public market reference points

The prices in this chapter are model outputs for one hypothetical system. Table 10-7 sets them beside public observations of ERCOT solar offers, receipts and costs in 2025–2026. The sources are indices, monitor reports and cost surveys, not executed contracts for this site.

**Table 10-7. Public market reference points.**

| Reference | Value | Period | What it measures | Source |
|---|---|---|---|---|
| LevelTen ERCOT solar PPA index, 25th percentile | $43.6–45.5/MWh by quarter; 2025 average $44.6 | 4Q24–4Q25 | First-year offer prices, nominal | [M01] |
| LevelTen / Trio levelized ERCOT solar index | $39.2 / $40.7/MWh | 2024 | Levelized offers, real 2024 dollars | [M01] |
| LevelTen North America solar index, 25th percentile | $64.49 / $61.40/MWh | 1Q26 / 2Q26 | Average across North American markets | [M02] |
| Market monitor: average price captured by ERCOT solar | $21/MWh | 2025 | Generation-weighted energy price | [M03] |
| Market monitor: solar curtailment; new solar / storage capacity | 6%; 6.2 GW / 7.3 GW | 2025 | System level | [M03] |
| Lazard unsubsidized utility-scale PV LCOE | $40–98/MWh | July 2026 edition | U.S. range; capital $1,250–1,850/kW, fixed O&M $8.25–26.25/kW-year | [M04] |
| Lazard unsubsidized PV-plus-storage LCOE | $61–156/MWh | July 2026 edition | 100 MW PV with 50 MW / 200 MWh storage | [M04] |

*Sources: Appendix A.3; values as published, with periods and bases as stated by each source. The accompanying research files record the table, tab or section of each value.*

Three readings follow. First, the market monitor's 2025 solar captured price of $21/MWh is close to the West hub value of $21.46/MWh and the reference node's $22.13/MWh (Section 8.1), so the reference case is not an outlier against the market-wide figure. Second, the report's $1,437/kWac capital cost and $24.49/kWac-year fixed O&M fall within Lazard's ranges, although Lazard's capacity basis is not reconciled with this report's. Third, ERCOT solar offers near $44.6/MWh in 2025 sit below every no-credit break-even in Table 1-2 and below the $53.51/MWh investment-credit illustration; only the full-rate production-credit illustration comes close. The ERCOT index is far below the North American average, so a national PPA price is not a usable reference for this market.

> **Limits of this chapter.** (1) Returns are pre-tax and unlevered. (2) Actual taxes, credit eligibility, financing and complete project costs remain unverified; benchmark expense coverage needs reconciliation. (3) Flat nominal contracts lose real value over time. Multiple cash-flow sign changes make a single IRR ambiguous.

# 11. Sensitivity and Break-Even Analysis: Turning Results into Testable Conditions

## 11.1 One-way sensitivities measure effects within chosen ranges

![Figure 11-1. One-way sensitivities over specified parameter ranges](figures/S5_one_way_sensitivity.png)

*Source: one-way sensitivity table [S08], 49 uniquely identified settings. Perturbations are analytical ranges, not probabilities or certified limits on unknown costs.*

Around the nodal base case, a ±20% CAPEX change moves NPV by approximately ±$28.7m, while a ±20% price-level change moves it by approximately ±$20.3m. In the fixed-price route, changing the price by ±$8/MWh moves NPV by approximately ±$22.7m. The tested unpaid-energy reduction range produces an NPV change of approximately ±$20.4m. [S08]

Both construction outlays and commercial realization therefore materially affect the tested cases. The comparisons provide no universal ranking of return drivers: wider perturbations generally produce larger effects, and some inputs are correlated. Total-CAPEX sensitivity is also not an isolated module-price sensitivity.

## 11.2 Physical performance and commercial realization interact

Losses, bifacial design, and degradation change potential generation. Prices, negative-price responsiveness, and unpaid-energy rules determine the value assigned to that generation. Incremental physical output need not produce proportional incremental revenue if it occurs in lower-value intervals.

The spatial financial sensitivity mainly scales the base output curve by annual-energy ratios and does not simulate capture prices for every location. Its financial range therefore describes an output-scaling sensitivity, not a fully spatially resolved revenue comparison. [S10]

## 11.3 Break-even conditions

**Table 11-1. Break-even conditions under base assumptions.**

| All other base assumptions held constant | 4.27% real discount rate | 6% | 8% |
|---|---:|---:|---:|
| Flat nominal fixed price, $/MWh | 66.0 | 74.3 | 84.6 |
| Break-even CAPEX, nodal route, $/kWac | 577 | 484 | 403 |
| Multiplier on the nodal price profile | 1.85 | 2.13 | 2.49 |
| Break-even CAPEX at a fixed $40/MWh, $/kWac | 699 | 609 | 527 |
| Flat nominal contract, no unpaid energy; 4.27% only | $55.91/MWh | — | — |

*Source: scenario break-even tables [S08]. Fixed-price thresholds keep the nominal-price convention, costs and degradation. The $55.91/MWh row pays for all potential generation; other fixed-price rows retain the base unpaid-energy deduction. They are not market PPA quotations. Nodal multipliers scale the price profile and are not forecasts.*

The nodal break-even capital cost of $577/kWac is about 40% of the base $1,437/kWac, a reduction of roughly 60%. The thresholds turn a general question about economic viability into conditions that can be checked: the achievable price and paid-volume rule, the construction cost consistent with that revenue, and the effect of eligible incentives or alternative risk allocation on cash flows.

A modeled break-even price requires a willing buyer before it becomes a contracting opportunity. Similarly, a break-even capital budget is not evidence that the system can be built for that amount.

## 11.4 Two-way sensitivities

![Figure 11-2. Two-way cost and price break-even analysis](figures/S6_two_way_breakeven.png)

*Source: two-way sensitivity table [S08]. Each plotted cell is a modeled cost/price combination. The fixed-price grid and the nodal-price scaling grid represent different revenue mechanisms.*

Lower costs reduce the required selling price but may not fully offset weak value capture. Around base CAPEX, the fixed-price grid crosses zero NPV between approximately $65/MWh and $70/MWh on a flat nominal basis. When costs, prices, and coverage change jointly, the case must be recalculated rather than inferred by adding separate sensitivity effects.

## 11.5 The price year matters far more than the weather year

The central robustness question is whether capital recovery survives a different price year, removal of the highest-price intervals and alternative output-price pairing. The answers below are historical stress tests, with no probability assigned to their recurrence; the full matrix, accounting tables and resampling results are in Appendix B.6–B.8.

Under 2023 prices, every weather profile leaves median NPV positive; under 2024–2025 prices, the median stays negative for all three, so weather volume alone does not explain the sign change. Changing price and weather together from 2023 to 2024 reduces mean NPV by $179.31m across the 485 nodes, of which an equal-interaction allocation assigns −$174.68m to the price profile and −$4.63m to weather: about 97% and 3%. This is model accounting, not an explanation of what caused market prices to change. From 2024 to 2025, a higher average price was largely offset by less favorable output-price timing, so a higher annual average price alone does not guarantee better solar receipts. [E-A]

**Table 11-2. Financial effects in NPV dollars, with comparison boundaries.**

| Comparison (baselines differ) | Change in NPV, $m | Starting point and interpretation |
|---|---:|---|
| 2023 to 2024 same-year setting | −179.31 | Mean across 485 nodes; both weather and prices change |
| U.S. module input −10% | +3.76 | 2025 reference; PV overnight scope, connection unchanged |
| U.S. module input −30% | +11.29 | Same reference; hypothetical procurement sensitivity |
| Reference export profile +10% | +10.14 | Same reference; shape and unit prices unchanged |
| Illustrative 30% credit, OCC-only basis | +35.38 | Same reference; eligibility unproven; end-2027 receipt; not complete after-tax DCF |

*Source: component outputs and scenario cash flows [E-A, S08, R-A, F04]. Dollar units are shared, but baselines and perturbation sizes differ. Rows are neither equally likely nor an empirical ranking of investment drivers; combined effects may interact.*

## 11.6 Tail dependence qualifies the positive historical scenario

In the empirical sample, the median node-level share of modeled receipts from the top 1% of 2023 price intervals is 54.7%. The corresponding shares are much smaller in 2024 and 2025, approximately 13.6% and 4.9%. The concentration statistic is specific to the output weights, price ranking, export rule, and sample. [E-C]

![Figure 11-3. Revenue concentration and tail stresses: reference node only](figures/empirical/F4_tail_concentration_and_stress.png)

*Source: multi-year analysis, tail-stress tables [E-C]. The figure shows reference-node results, which are distinct from the cross-node medians reported in the text. Tail deletion and caps are stress scenarios beside the original prices, not corrections to history. Tail stresses use full annual calendars, unlike the common-calendar matrix in Figure B-2.*

Removing receipts from the top 1% of intervals turns modeled NPV negative for 99.4% of the sample under 2023 conditions. The reported median stress-case NPV is approximately −$56.6m. A 99th-percentile price cap produces a median around −$10.6m; removing receipts on dates containing an interval at or above $1,000/MWh produces a median around −$82.5m. Those settings retain costs while deliberately reducing receipts and do not represent forecasts of attainable annual revenue.

A gentler cap at the 99.9th percentile leaves the 2023 median NPV at approximately +$98.25m, whereas the 99th-percentile cap gives −$10.61m. This difference identifies sensitivity to a broader upper tail rather than just the most extreme 0.1%. A separate variant replaces daily receipts with the median receipts of nonflagged dates; it does not replace an interval price profile. Across nodes its median count is 34 flagged dates. [E-C]

ERCOT initiated an Energy Emergency Alert Level 2 on 6 September 2023, reporting a September peak of 82,705 MW. That official event provides context for the high-price environment; this study has not matched its individual revenue intervals to event or constraint records. ERCOT subsequently launched real-time co-optimization of energy and ancillary services, with its battery enhancements, on **5 December 2025**. The years 2023–2024 therefore predate the change and **2025 straddles it**, so the three-year sample should not be described as entirely pre-reform. No causal battery or reform effect is estimated. [P05, P06]

The best-hours statistic has a median of about 23 accumulated hours, with node-level values from 1 to 198.25 hours among positive 2023 cases. It sorts 15-minute intervals by modeled receipts and removes them until the NPV surplus is exhausted. The intervals need not be consecutive or identifiable in advance. This measures the narrow revenue buffer, not a schedule of hours a developer can guarantee. [E-C]

## 11.7 Evidence from 2026, after the market redesign

Real-time settlement-point prices for 2026 were obtained from ERCOT's public API for product NP6-905-CD, covering 1 January to 9 October 2026 and all 1,133 published settlement points. All 485 screened nodes and seven benchmarks are present.

- **Coverage.** Through 8 October, the range covers 281 calendar days. Only 270 of them have every interval published: 125 intervals on 11 days are absent for every settlement point and are not filled. 9 October was partial when retrieved.
- **Finality.** Under the Nodal Protocols, prices become final at 16:00 on the second business day after the operating day. Using a Monday–Friday business-day count without independently applying the ERCOT holiday calendar, data through 7 October were inferred to have passed that time at retrieval, but the API supplies no version field. Row-level finality is therefore not verified.
- **Cross-product differences.** A cross-check of West hub prices against ERCOT's separate year-to-date hub file found 423 interval differences above $0.005/MWh, up to $4.01/MWh, mostly in January 2026. Their cause is not established.

No 2026 generation series exists for the hypothetical site, so no same-year 2026 capture price, project revenue or NPV is reported. As context only, ERCOT's separate year-to-date West hub file (NP6-785-ER; different from the API series in 423 intervals) gives a fixed-2025-profile-weighted January–September 2026 value of $18.24/MWh, versus $21.36/MWh for January–September 2025 with that year's profile. West hub prices are negative in 14.1% of 2026 intervals versus 7.7% (23.6% versus 13.7% of the profile's energy). Compare the reference node's full-year 2025 interval share of 6.2% in Section 8.2: hub/node and seasonal/full-year measures differ. This is a fixed-profile price diagnostic, not realized 2026 capture. It does not isolate the effect of the December 2025 co-optimization launch because weather, load, fuel prices and competing capacity also changed. [CL-FIN-08]

The ERCOT Independent Market Monitor reports for 2025 that the ORDC shortage adder was active for only 57 hours and that energy-storage capacity exceeded 17 GW. Three historical years provide no recurrence probability for 2023-type scarcity receipts. [CL-FIN-08]

> **Limits of this chapter.** (1) Perturbation ranges are analyst-selected, with some correlated inputs. (2) Component means in Table B-3 add to their mean total; accounting contributions are not causal effects. (3) Tail deletions, resampling and equal-year mixtures are stresses, not event probabilities or price forecasts.

# 12. Research Hypotheses: What the Evidence Supports and What Remains Open

Two working hypotheses can be tested with the evidence assembled here, and Sections 12.1–12.2 report the results. The three open questions in Section 2.5 need asset-level data the report does not hold; Section 12.3 states what the evidence shows and what would settle each, and Section 12.4 adds a first screen of the storage question.

## 12.1 Equipment-price hypothesis (H1) — Mixed

**Working hypothesis:** Lower module prices improve project economics, but their effect may be smaller than financing, interconnection delay, curtailment or realized power prices.

Manufacturing evidence supports price pressure, and the scenario sensitivities establish that total CAPEX affects NPV. The direct bridge from delivered module prices to project capital expenditure is still absent. The full comparative proposition has therefore not been established.

Alternative explanations include changes in technology, non-module scope, delivery terms, trade duties and tax-credit eligibility tied to equipment origin and supplier ownership. A stronger conclusion requires the delivered-cost evidence listed in Appendix C and comparisons using consistent, justified perturbations; national total-cost variation and isolated component-price effects have different scopes.

**Practical implication.** Use component-specific delivered quotes before ranking cost savings against other risks.

## 12.2 Value-chain hypothesis (H2) — Supported for the observed businesses

**Working hypothesis:** Manufacturing scale and lower upstream prices can coexist with weak value capture along the solar value chain.

The existence claim is supported within the observed businesses: large manufacturing scale and falling upstream prices coexist with weak or negative reported profitability. The FY2025 Trina, JA Solar and Tongwei disclosures provide direct loss observations, alongside the other annual company evidence. This is stronger than mere consistency with pressure, but it establishes neither industry-average profitability nor its cause. [S01, S02, R-D, R-F]

Product mix, technology, incentives, impairment charges, utilization and working-capital changes remain alternative explanations. Industry-wide or causal conclusions require matched segment production, prices, capacity, costs and inventory. The observations also do not measure the pass-through to a U.S. asset's delivered cost.

**Practical implication.** Assess company-specific cash generation and product economics alongside manufacturing volumes.

## 12.3 Open questions: demand, grid constraints and storage

**Q1 — Demand and value.** National demand scenarios coexist with low historical solar capture prices, but that coexistence is not a causal test of demand growth at a specific node, and asset-level contracts, location and credit conditions are absent. Non-data-center load, network conditions, other supply and fixed-price contracts can all separate receipts from load growth. *What would settle it:* customer-level procurement and timed local load linked to project settlement. *Practical implication:* qualify the buyer, settlement location and payment shape; a load request alone is not a price uplift.

**Q2 — Grid constraints.** System timing differences, negative-price exposure and the persistent node basis motivate the question but do not measure the cost of network constraints or the marginal value of adding the hypothetical system; weather, fleet composition and other market conditions can also explain them. *What would settle it:* interval constraint or curtailment records, interconnection timing and costs, or a supported counterfactual. *Practical implication:* investigate actual constraints and settlement exposure before attributing a node price difference to congestion.

**Q3 — Storage.** Shifting midday output into higher-priced hours is the obvious response to the timing pattern in Chapter 8, but a timing mismatch is not proof of positive storage value. The report has no storage configuration, dispatch or cost model; Section 12.4 gives a first screen of the question.

## 12.4 Storage screen

The screen asks whether the best possible energy arbitrage in the observed price years could pay for a standard 4-hour battery. It compares a perfect-foresight upper bound on daily arbitrage with Lazard's 2026 cost range; method details are in Appendix B.9.

**Table 12-1. Storage screen: energy-arbitrage upper bound and annualized cost, 1 MW / 4 MWh, $/kW-year.**

| Item | Basis | $/kW-year |
|---|---|---:|
| Upper bound, reference node, 2025 | Hourly averages of 15-minute prices; round-trip efficiency 86%–92% | 104.4–113.0 |
| Upper bound, HB_BUSAVG hub, 2023 | Hourly means; same efficiency range | 188.3–202.7 |
| Upper bound, HB_BUSAVG hub, 2024 | Same | 68.6–74.4 |
| Upper bound, HB_BUSAVG hub, 2025 | Same | 61.6–67.5 |
| Annualized cost at 4.27% real | Lazard 4-hour capital $270–365/kWh, O&M $3.75–7.75/kWh-year, 20 years | 96.4–141.0 |
| Annualized cost at 6% real | Same | 109.2–158.3 |
| Annualized cost at 8% real | Same | 125.0–179.7 |

*Sources: reference-node and hub prices as in Chapter 8 and Appendix B.1; Lazard LCOS v11.0 [M04]; `data/r1/Storage-Screen.csv` and `Storage-Cost.csv`. The upper bound assumes perfect daily foresight and ignores charge order and degradation; it omits ancillary-service revenue.*

At the reference node in 2025, even perfect arbitrage reaches only the bottom of the cost range at 4.27% and 6%, and it falls short of the whole range at 8%. Hub bounds for 2024 and 2025 are below the lowest cost at every rate; only 2023's scarcity prices clear the full cost range. The market monitor reports that storage revenue per unit of capacity fell 37% in 2025 as 7.3 GW of storage was added. [M03]

**Practical implication.** An energy-only storage addition is unlikely to pay for itself on the 2024–2025 price pattern; a storage case needs ancillary-service, scarcity or contracted revenue, and should be modeled as a separate incremental investment with its own dispatch and cost evidence.

## 12.5 Summary of conclusions

**Table 12-2. Conclusions and revision evidence.**

| Hypothesis or question | Conclusion | Additional support | Alternative explanation and revision evidence |
|---|---|---|---|
| H1 Equipment price | Mixed | Component model quantifies a conditional cost mechanism; customs data adds sourcing context | Trade treatment, specifications and non-module costs can offset savings; matched procurement and complete budgets remain necessary |
| H2 Value chain | Supported as an existence claim for the observed businesses | Annual losses and company-specific margins alongside large manufacturing scale | Technology, incentives, financing, working capital and market price shape differ; matched segment and procurement evidence is needed |
| Q1 Demand and value | Open; not testable as a causal or asset-level proposition | Dated large-load categories and hourly market associations improve context | Load requests may not connect or may procure a different product; actual timed local load and procurement are absent |
| Q2 Grid constraints | Open; not testable causally | Node basis persists in the 485-point common-calendar panel | Settlement, supply and network factors are not separated; interval constraints, dispatch and a credible counterfactual remain necessary |
| Q3 Storage | Screened: even perfect energy arbitrage at the reference node in 2025 reaches only the bottom of the cost range | Upper bound from observed prices against Lazard cost ranges | Ancillary services, contracts and dispatch rules can change the result; no storage investment case is modeled |

*Hypotheses and questions are stated in full in Section 2.5.*

Statistical association, accounting contribution, and investment relevance remain distinct. The empirical findings support conditional screening, within the asset-level boundaries set out in Box 1.

> **Limits of this chapter.** (1) Conclusions apply only to their stated evidence. (2) Comparative driver rankings and causal demand or congestion claims remain untested; the storage result is a screen, not a valuation. (3) The additional evidence required is listed in Appendix C.

# 13. Commercial Applications: Procurement, Development, and Market Screening

::: lead
**Bottom line by reader.** Suppliers: a 10% cheaper module saves $3.76m against an $86.0m modeled gap, so sell delivered value and documentation, not price alone. Developers: no tested route without credits reaches public 2025 ERCOT offers of about $44.6/MWh, so a project needs credits it can actually claim, a lower all-in cost or a buyer paying for more than energy. Buyers: compare an offer with the hub-hedge row of Table 1-2 and the terms in Table 13-2, not with a headline average. Storage: even perfect energy arbitrage at the reference node in 2025 reaches only the bottom of the cost range (Section 12.4).
:::

## 13.1 Equipment suppliers: demonstrate value within the customer's system

A commercially useful procurement assessment has three stages: compare delivered prices for comparable specifications; assess compatibility, performance, and reliability; and evaluate the customer's connection and revenue conditions. Equipment-price reductions directly affect only part of that assessment and do not guarantee a construction decision.

Sales and strategy materials should therefore connect product attributes with customer requirements. The evidence does not measure service premiums or identify supplier winners; those conclusions require comparable product, delivery and customer evidence.

For the component-price example, a 10% U.S. module-input reduction saves $3.76m and leaves reference NPV at −$82.20m. A supplier should therefore show the delivered project saving, warranty and system consequences alongside the module quote. Covered import rules may limit transmission; the comparison with the subsidy-adjusted U.S.-assembled benchmark defined in Section 1.1 remains conditional on compatible product, date and denominator definitions. [R-A, P01]

**Table 13-1. Questions for a U.S. procurement contract.**

| Question | Evidence required before signing |
|---|---|
| Who pays if trade treatment changes after signing? | Change-in-law, price adjustment and termination provisions |
| Who is responsible for customs entry and duties? | Importer-of-record identity, delivery terms and accuracy of MIP certification (clause 3 penalty) |
| Can materials and their origins be traced? | Documented upstream sourcing and customs-compliance evidence |
| Can ownership and equipment eligibility be substantiated? | Ownership/control records and applicable tax eligibility documents (see Section 10.8) |
| What happens if equipment is late or underperforms? | Delivery milestones, damages, acceptance and warranty remedies |
| What does the quoted price include? | Common specifications, DC basis, freight, taxes, insurance and warranty scope |

*Source: Sections 5.7 and 10.8. Questions restate analytical fields, not legal advice or indicative contract terms.*

An equipment-only supplier should demonstrate the delivered product and service obligations. An integrated equipment/development business also needs to explain asset risk, ownership and financing; a component quotation does not establish those project economics.

## 13.2 Developers: assess generation and payment rules together

Identical annual generation can produce different receipts when settlement timing, location, or contract rules change. Development screening should identify the site, system design, settlement point, and commercial arrangement before assigning asset-level meaning to a result.

The thresholds can support internal questions: whether a quotation change is large enough to alter the scenario; whether a nominal contract price is consistent with real costs; and how unpaid-energy provisions affect capital recovery. They do not constitute an available financing solution or a completed project appraisal.

Under the reference assumptions, the simplified node-level fixed-price route needs about $66/MWh flat nominal (see Section 10.3 for the hub-hedge range), while the nodal route requires CAPEX near $577/kWac or a price-profile multiplier near 1.85. These are alternative break-even tests. The −$81.3m 2025 median-node NPV shows that switching to the median price reference alone still leaves a sizeable modeled gap. [S08, E-A]

## 13.3 Electricity buyers: compare the product and the obligations

Energy, environmental attributes, scheduled delivery, and continuous supply are distinct procurement objectives. Their quantity, location, and shortfall responsibilities differ. Two prices expressed per MWh may therefore refer to materially different products.

A contract-reading framework should identify those responsibilities before comparing prices. Customer-specific procurement recommendations require evidence about the actual product and obligation, which is not part of this report. Section 10.3 calculates the hub-hedge break-even, Section 10.10 gives public offer references, Appendix B.2 sets out contract risk allocation, and Appendix C lists the undisclosed terms needed for transaction diligence.

**Table 13-2. Contract questions before comparing headline prices.**

| Question | Field to reconcile |
|---|---|
| What is bought and what is paid? | Energy versus environmental attributes; metered generation versus contracted quantity; payment suspensions |
| Where does it settle? | Physical node and financial hub; node-to-hub basis allocation |
| What happens after the term? | Contract tenor, remaining asset life and merchant-tail price assumption |
| Who carries adverse events? | Negative-price rules, shortfall obligations, imbalance, fees and collateral |
| Is the offer executable? | Counterparty credit, guarantees, termination, change-in-law and actual executed terms |

*Source: Section 10.3, Appendix B.2 and Appendix C. Questions restate analytical fields, not indicative market terms.*

## 13.4 Research teams: test each link in the market thesis

Lower equipment costs, growing electricity demand, and stronger project returns are separate propositions. Examining each link identifies which additional evidence could change the conclusion and avoids repeated collection of general background material.

This report contributes manufacturing observations, regional operating context, and economic thresholds. The most useful extensions concern transmission into delivered costs, the representativeness of market outcomes, and customer procurement needs.

## 13.5 A decision matrix for using the expanded evidence

**Table 13-3. Commercial decisions and evidence requirements.**

| Reader decision | Evidence available now | Required commercial qualification | What this report shows |
|---|---|---|---|
| Test whether a lower module quote is material | PV-only component shares and conditional transmission factor | Match specifications, tax basis, delivery terms, and non-module scope | 10% module-input reduction improves reference NPV by $3.76m |
| Qualify supplier and equipment eligibility | Official timing and ownership/material-assistance provisions | Establish project eligibility, eligible basis and supply-chain documents | 40%/45% material-assistance cost ratio for 2026/2027 construction starts: manufactured-product cost not attributable to a prohibited foreign entity; ownership/control rules also apply (Section 10.8). The $35.38m illustration assumes eligibility, not a supplier/product finding |
| Challenge a claim based on average power prices | Common-output nodal capture-price distribution | Match actual settlement point, hourly output, and payment rules | 2025 reference capture ratio about 48%, before export response (near the 3rd percentile of the cross-section; HB_WEST about 65%) |
| Qualify a large-load prospect | Dated process categories and conditional Batch Zero results | Verify customer identity, connection milestones, operating date, and procurement status | 238.6 GW total across all statuses, of which about 5.8 GW is observed energized; different time bases |
| Compare solar with broader supply products | Public self-supply capacity mix and service distinctions | Evaluate reliability and dispatch on a common service basis; do not compare energy-only LCOE with firm supply cost | 11 WLPUN projects: about 83% gas and 11% solar by power capacity, not energy; not a census |
| Compare a PPA offer with this report | Public ERCOT offer indices and the hub-hedge break-even range | Match tenor, settlement hub, volume rule and credit treatment before comparing prices | ERCOT solar offers about $44.6/MWh (2025, 25th percentile) against $60.6–84.8/MWh hub-hedge break-even without credits (Table 1-2) |
| Screen a storage addition | Perfect-foresight arbitrage bound and Lazard cost range | Model dispatch, ancillary services, contracts and site cost | Reference-node 2025 bound $104.4–113.0/kW-year against $109.2–158.3 cost at 6% (Section 12.4) |
| Assess a scenario's capital recovery conditions | Break-even thresholds and historical price-year substitution | Replace assumptions only with sourced inputs; preserve excluded taxes, debt, and cost items until modeled | About $66/MWh flat nominal on the simplified node-level fixed-price route, or $577/kWac on the nodal route (hub-hedge range: Section 10.3) |

The practical product of this research is a set of screening questions and transparent conditional calculations. It is suitable for initial market development, commercial hypothesis testing, and planning subsequent diligence. Customer acquisition forecasts, investment recommendations, and guaranteed procurement savings remain outside the evidence supported by the report.

> **Limits of this chapter.** (1) The screening thresholds are conditional and provide questions for diligence. (2) Actual orders, settlement terms, buyer credit, all-in budgets and contracting rights are still needed before an investment or procurement decision. (3) The additional evidence required is listed in Appendix C.

# 14. Outlook and Updates: Conditional Scenarios with Identifiable Evidence

## 14.1 What the present evidence permits

The evidence supports an analytical monitoring framework, but not an independent market-size or electricity-price forecast. Manufacturing conditions, load realization, network development, and procurement can evolve at different speeds and require separate indicators. Unsupported growth rates are not inserted into future-year tables.

## 14.2 Conditional market developments

On the supply side, a sustained reduction in manufacturing output relative to sales could firm equipment prices and reduce the module savings tested in Chapter 5. Continued price competition could lower factory prices further, while delivered U.S. savings would still depend on product access, duties, logistics and tax eligibility. These are conditional paths; no success probability is assigned to industry consolidation or production restraint.

If load materializes faster than network expansion, location differentials, connection timing, and reliable delivery become important questions for further analysis. If demand and network development advance together, procurement, competing supply, and contract transmission become central. If announced demand materializes more slowly, customer pipelines and equipment-demand expectations require reassessment.

These are logical scenarios awaiting quantification. They carry no assigned probabilities and do not substitute for a forecast model.

For solar receipts, the first path is ambiguous: scarcity can support market prices while connection delays and delivery restrictions impair realization. Coordinated load and network expansion can improve market access, but competing supply may absorb the demand increase. Slower load realization weakens the demand-side thesis, holding supply and other conditions constant. None of these paths has a quantified net price effect here.

## 14.3 Indicators and revision triggers

**Table 14-1. Indicators that would change the assessment.**

| Area | Proposed indicators | Analysis potentially affected |
|---|---|---|
| Manufacturing supply | Stage-specific output, shipments, inventory days, utilization with matched capacity denominators, product-specific prices | Whether production restraint is followed by sustained price/margin recovery |
| Trade and tax policy | Product/origin/date-specific customs rules; equipment and ownership eligibility; construction/service milestones | Delivered cost and credit eligibility |
| Regional demand | Actual load, approved connections, project-status changes | Regional demand assessment and customer screening |
| Supply and networks | Commissioning, constraints, connection timing, network progress | Location and delivery risks |
| Electricity value | Capture prices, negative-price energy, nodal differentials | Revenue assumptions and scenario recalculation |
| Costs and contracts | Component costs, delivered prices, quantity and payment rules | CAPEX transmission and break-even conditions |

*The framework is a proposed update process, not an operating monitoring system or a service commitment.*

## 14.4 Interpretation of the extended investment evidence

Three distinctions govern the use of the empirical results. First, a historically positive modeled outcome is conditional on that price pattern, not an expected return. Second, broad negative outcomes under two historical price years do not prove that every solar project is uneconomic. Third, persistent node price differences do not identify their cause. Each stronger claim would require additional evidence beyond the present scenario and association framework.

The most useful investment question is whether a proposed commercial structure can support the required receipts at a complete and substantiated cost. The present study supplies conditional thresholds and identifies exposure to a concentrated price pattern. Future prices, contracting rights, tax eligibility, financing terms and collection probabilities remain unresolved.

For readers assessing entry into the market, the immediate implication is to qualify the revenue product as carefully as the equipment price: energy-only sales, fixed-price contracts, shape guarantees, scarcity participation and firm supply allocate different risks. A contract can transfer exposure rather than eliminate its cost. No unsupported ranking of these routes is made.

> **Limits of this chapter.** (1) The outlook uses qualitative conditional paths without assigned probabilities. (2) Faster load growth may support prices yet worsen access and delivery risks; the net project effect depends on location, competing supply and contract terms. (3) The additional evidence required is listed in Appendix C.

# Appendix A. Source Bibliography

Bracketed identifiers refer to source families. Official observations and research calculations remain distinct; repeated use of one source is not independent corroboration. Annual periods, publication dates and projection years are stated separately.

**S01.** Ministry of Industry and Information Technology, 2024 national photovoltaic manufacturing bulletin (published 27 February 2025); supplied original PDF and Fujian official republication: [official source](https://gxt.fujian.gov.cn/zwgk/gysj/xysj/xxcy/202504/t20250418_6902400.htm)

**S02.** LONGi Green Energy, Annual Report FY2024: [official source](https://static.longi.com/LON_Gi_annual_report_2024_0026f3477f.pdf)

**S03.** IRENA, Renewable Capacity Statistics 2026 (2016–2025 series): [official source](https://www.irena.org/Publications/2026/Mar/Renewable-capacity-statistics-2026)

**S04.** Berkeley Lab / DOE, United States Data Center Energy Usage Report, 2025 update (published June 2026; modeled 2030): [official source](https://www.energy.gov/documents/united-states-data-center-energy-usage-report-2025-update)

**S05.** ERCOT-LOAD (2025): [official source](https://www.ercot.com/gridinfo/load/load_hist); ERCOT-SOLAR (2025): [official source](https://www.ercot.com/gridinfo/generation)

**S06.** NP6-905-CD 2025 monthly archives (2025): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD)

**S07.** NSRDB V4 5-minute block extract, gid 1142134, 2025 (2025): [official source](https://developer.nrel.gov/docs/solar/nsrdb/)

**S08.** Scenario input register (finance parameters, 2026-10-07; project model; not separately published); Scenario finance model code (unmodified, 2026-10-07; project model; not separately published)

**S09.** NLR-2025-ATB (2026 projection): [official source](https://atb.nlr.gov/electricity/2025/data)

**S10.** Scenario finance model code (unmodified, 2026-10-07; project model; not separately published)

**R-A.** U.S. Utility-Scale Solar, 2025 Data Update (slides PDF) (2025-10): [official source](https://emp.lbl.gov/sites/default/files/2025-10/Utility%20Scale%20Solar%202025%20Edition%20Slides.pdf); Solar Photovoltaic System Cost Benchmarks (web page) (2026-09-02 (page modified)): [official source](https://www.energy.gov/eere/solar/solar-photovoltaic-system-cost-benchmarks); Q1-2024 Solar Cost Benchmarks (dataset page) (2025-12-01 (submitted)): [official source](https://data.nlr.gov/submissions/307); 2025Q1 PV System Cost Benchmark Model (zip: PVSCM 2025.xlsm, UPV/CPV/RPV 2025Q1.txt, description PDF, ReadMe) (2025-11-13 (Program.Date in parameter file)): [official source](https://data.nlr.gov/system/files/304/1767739491-2025Q1%20PV%20System%20Cost%20Benchmark%20Model.zip)

**R-B.** NP6-905-CD SPP at resource nodes, hubs and load zones, 2023 monthly archives (2023): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); NP6-905-CD 2024 monthly archives (2024): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); NP6-905-CD 2025 monthly archives (2025): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); CIM SP List and EB Mapping (snapshot 2026-09-10) (snapshot 2026-09-10): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP4-160-SG)

**R-C.** Large Load Interconnection Status Update (TAC report), 2026-03-13 (2026-03-12 (posted; deck dated 2026-03-13)): [official source](https://www.ercot.com/files/docs/2026/03/12/March-TAC-Report.pdf); Board Item 14: Batch Zero Update, 2026-09-14/15 (2026-09-11 (posted)): [official source](https://www.ercot.com/files/docs/2026/09/11/14-Batch-Zero-Update.pdf); Board Item 9.1: Batch Study Update, 2026-04 (2026-04-13 (posted)): [official source](https://www.ercot.com/files/docs/2026/04/13/9.1-Batch-Study-Update.pdf)

**R-D.** Electric Power Monthly Table 6.1 (June to July 2026) (2026-09 (release for July 2026 data)): [official source](https://www.eia.gov/electricity/monthly/xls/table_6_01.xlsx); EIA-860M, August 2026 generator file (2026-09 (file for August 2026)): [official source](https://www.eia.gov/electricity/data/eia860m/xls/august_generator2026.xlsx); JinkoSolar Holding, Form 20-F FY2025 (29 April 2026): [official source](https://www.sec.gov/Archives/edgar/data/1481513/000110465926050737/jks-20251231x20f.htm); Canadian Solar, Form 20-F FY2025 (10 April 2026): [official source](https://www.sec.gov/Archives/edgar/data/1375877/000110465926041976/csiq-20251231x20f.htm); Daqo New Energy, Form 20-F FY2025 (20 April 2026): [official source](https://www.sec.gov/Archives/edgar/data/1477641/000110465926045134/dq-20251231x20f.htm); First Solar, Form 10-K FY2025 (24 February 2026): [official source](https://www.sec.gov/Archives/edgar/data/1274494/000127449426000021/fslr-20251231.htm)

**R-T.** Census International Trade API: HS6/HS10 solar imports by country, monthly, January 2024 to August 2026: [official source](https://api.census.gov/data/timeseries/intltrade/imports/hs); with the corresponding API query log.

**R-F.** Trina Solar, 2025 Annual Report (FY2025 (calendar), comparatives FY2024): [official source](https://static.cninfo.com.cn/finalpage/2026-04-30/1225263857.PDF); JA Solar, 2025 Annual Report (FY2025 (calendar), comparatives FY2024): [official source](https://static.cninfo.com.cn/finalpage/2026-04-29/1225249462.PDF); Tongwei, 2025 Annual Report (FY2025 (calendar), comparatives FY2024): [official source](https://static.cninfo.com.cn/finalpage/2026-04-30/1225259224.PDF)

**E-S.** NP6-905-CD SPP at resource nodes, hubs and load zones, 2023 monthly archives (2023): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); NP6-905-CD 2024 monthly archives (2024): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); NP6-905-CD 2025 monthly archives (2025): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); CIM SP List and EB Mapping (snapshot 2026-09-10) (snapshot 2026-09-10): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP4-160-SG)

**E-A.** NSRDB V4 5-minute block extract, gid 1142134, 2023 (2023): [official source](https://developer.nrel.gov/docs/solar/nsrdb/); NSRDB V4 5-minute block extract, gid 1142134, 2024 (2024): [official source](https://developer.nrel.gov/docs/solar/nsrdb/); NSRDB V4 5-minute block extract, gid 1142134, 2025 (2025): [official source](https://developer.nrel.gov/docs/solar/nsrdb/); Scenario input register (finance parameters, 2026-10-07; project model; not separately published); Scenario finance model code (unmodified, 2026-10-07; project model; not separately published)

**E-B.** Fuel Mix archive 2007-2024 (IntGenbyFuel2023, IntGenbyFuel2024 used) (2023-2024): [official source](https://www.ercot.com/gridinfo/generation); Fuel Mix IntGenbyFuel2025 (2025): [official source](https://www.ercot.com/files/docs/2025/02/07/IntGenbyFuel2025.xlsx); Native Load 2023 (2023): [official source](https://www.ercot.com/files/docs/2023/02/09/Native_Load_2023.zip); Native Load 2024 (2024): [official source](https://www.ercot.com/files/docs/2024/02/06/Native_Load_2024.zip); Native Load 2025 (2025): [official source](https://www.ercot.com/files/docs/2025/02/11/Native_Load_2025.zip); Henry Hub natural gas spot price, daily (1997-2026): [official source](https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls); GHCN-Daily TMAX/TMIN, DFW IAH SAT AUS (2023-2025): [official source](https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries)

**E-C.** NP6-905-CD SPP at resource nodes, hubs and load zones, 2023 monthly archives (2023): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); NP6-905-CD 2024 monthly archives (2024): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); NP6-905-CD 2025 monthly archives (2025): [official source](https://www.ercot.com/mp/data-products/data-product-details?id=NP6-905-CD); Scenario finance model code (unmodified, 2026-10-07; project model; not separately published)

**P01.** Adjusting Imports of Polysilicon and Its Derivatives Into the United States (91 FR 51975) (2026-08-11): [official source](https://www.federalregister.gov/documents/2026/08/11/2026-16400/adjusting-imports-of-polysilicon-and-its-derivatives-into-the-united-states)

**P02.** Notice 2025-42 (beginning of construction, wind and solar) (2025-08-15; vacated in full 6 June 2026, F08 and Section 10.8; history only): [official source](https://www.irs.gov/pub/irs-drop/n-25-42.pdf)

**P03.** Notice 2026-15 (prohibited foreign entity / material assistance cost ratio interim guidance) (2026-02-12): [official source](https://www.irs.gov/pub/irs-drop/n-26-15.pdf)

**P04.** U.S. Utility-Scale Solar, 2025 Data Update (slides PDF) (2025-10): [official source](https://emp.lbl.gov/sites/default/files/2025-10/Utility%20Scale%20Solar%202025%20Edition%20Slides.pdf)

**P05.** ERCOT, Energy Emergency Alert Level 2, 6 September 2023: [official release](https://www.ercot.com/news/release/2023-09-06-ercot-has-initiated).

**P06.** ERCOT, real-time co-optimization and battery-enhancement launch, 5 December 2025: [official release](https://www.ercot.com/news/release/12052025-ercot-goes-live).

**P07.** National Development and Reform Commission, explanation of renewable market-pricing reform, 9 February 2025: [official explanation](https://www.ndrc.gov.cn/xxgk/jd/jd/202502/t20250209_1396070.html).

**P08.** Ministry of Finance / State Taxation Administration, 2026 announcement no.2, export VAT rebate adjustment: [official announcement](https://szs.mof.gov.cn/zhengcefabu/202601/t20260109_3981637.htm).

**P09.** ERCOT, implementation of the Bus Average 345-kV Hub under NPRR817, 2019 market notice: [official notice](https://www.ercot.com/services/comm/mkt_notices/archives/4100).

**P10.** NLR, Utility-Scale PV, ATB 2025, including fixed O&M definition: [official technology documentation](https://atb.nlr.gov/electricity/2025/utility-scale_pv).

**Derived calculations.** Arithmetic sensitivities and summary tables are derived from the scenario and empirical outputs; no regression, physical simulation, decomposition estimation or resampling was re-estimated for them. Inputs and reproducible transformations accompany the research files.

## A.1 Comparable-project, cost, contract and tax sources (F references)

- **[F01]** Finance supplement, Comparable-Projects.csv and Entity-Node-Mapping.csv; ERCOT NP4-160, MORA resource records and EIA-860 design/capacity records. The ERCOT–EIA plant link is attribute-matched; source locators are in finance-supplement/Source-Catalog.csv.
- **[F02]** Texas Comptroller, agreement #1377, TY2024 Form 772 (2025 filing), physical PDF p. 1, filing Section 2.7. Retained copy: [Form 772](sources/finance/comparables/C06_ch313_1377_772_2025.pdf). Financing event; no return disclosure.
- **[F03]** EIA-860/923, retained annual comparison and monthly generation tables in finance-supplement/data/. Full workbooks remain in the project's raw-data archive; geographic and capacity-vintage limitations are described in Section 9.5.
- **[F04]** Finance supplement, Finance-Arithmetic-Checks.csv, Cost-Coverage-Crosswalk.csv, Node-Hub-Solar-Capture-2023-2025.csv, plus retained scenario cash flows. The stated arithmetic and sample screens are recomputed from these files.
- **[F05]** CIT/First Citizens, Taygete I financing announcement, 9 December 2020; source F01 in finance-supplement/Source-Catalog.csv and Contract-Terms.csv. Financing amount is not construction cost or IRR. Secondary fixed-shape description is separately marked F03 in that catalog.
- **[F06]** PUCT, [16 TAC §25.195](https://www.puc.texas.gov/agency/rulesnlaws/subrules/electric/25.195/25.195.pdf), subsection (f)(1)–(3). [Retained original](sources/finance/ERCOT/PUCT_16TAC_25.195_current.pdf).
- **[F07]** [P.L. 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/pdf/PLAW-119publ21.pdf), §§70512–70513 and amendments to §§48E, 7701; [retained original](sources/finance/tax/PLAW-119publ21.pdf). Eligible-basis and section 50 treatment are also referenced in the finance supplement's tax matrix; no taxpayer-specific conclusion is drawn.
- **[F08]** District Court, case 1:25-cv-04400, opinion dated 6 June 2026, physical pp. 1, 57: [GovInfo](https://www.govinfo.gov/content/pkg/USCOURTS-dcd-1_25-cv-04400/pdf/USCOURTS-dcd-1_25-cv-04400-0.pdf), [retained original](sources/finance/tax/USCOURTS-dcd-1_25-cv-04400-0.pdf). Appellate/stay status is unresolved.
- **[F09]** IRS Notice 2026-15, material-assistance cost-ratio and prohibited-foreign-entity provisions; [retained original](sources/finance/tax/n-26-15.pdf).


## A.2 Supplementary verification sources (CL references)

CL references identify the corresponding FIN-01–FIN-11 or B-01–B-05 section in the [closure findings](closure-evidence/Findings-and-Replacement-Text-EN.md). The [closure source catalog](closure-evidence/Sources.csv) supplies original URLs, retained file paths, page locators and hashes; the [claim register](closure-evidence/Numbers-and-Claims.csv) records numerical and legal scope. Search leads are not used as evidence. Selected new inputs include FY2025 SEC and A-share annual filings, the full Federal Register proclamation and annexes, the public RECAP docket, the ERCOT Batch Zero deck and the 2025 IMM report. The Business Wire source is a screenshot of a developer press release, not an executed contract. Source checks were completed on 10 October 2026 UTC (9 October US Eastern).

The separately versioned CPI, credit and VPPA calculations are documented in the [scenario notes](scenario-versions/Scenario-Notes-EN.md) and their accompanying CSV files. They do not revise the original six baseline scenarios.

## A.3 Sources for the market, credit and storage calculations (M references)

- **[M01]** Berkeley Lab, U.S. Utility-Scale Solar, 2025 Data Update, data file (tabs "LevelTen Solar PPA Prices" and "LevelTen & Trio 2024 PPA Index", LevelTen Energy and Trio data): [publication page](https://emp.lbl.gov/publications/us-utility-scale-solar-2025-data).
- **[M02]** LevelTen North American solar PPA price index as reported by pv magazine USA, 20 April 2026 (1Q26): [article](https://pv-magazine-usa.com/2026/04/20/permitting-headwinds-and-geopolitics-drive-solar-ppa-prices-higher-in-q/); and by TaiyangNews (2Q26): [article](https://taiyangnews.info/business/levelten-energy-q2-2026-report-for-north-america-europe).
- **[M03]** Potomac Economics, 2025 State of the Market Report for the ERCOT Electricity Markets (June 2026), Sections II.A, II.D and II.E: [report](https://www.potomaceconomics.com/wp-content/uploads/2026/06/2025-State-of-the-Market-Report-for-ERCOT.pdf).
- **[M04]** Lazard, Levelized Cost of Energy+ (July 2026; LCOE v19.0, LCOS v11.0), key assumptions and comparison pages: [report](https://www.lazard.com/media/kcfconhf/lazards-lcoeplus_vf.pdf).
- **[M05]** IRS, inflation adjustment factor and applicable amounts for the clean electricity production credit, calendar year 2025 (FR Doc. 2025-16249, 25 August 2025): [Federal Register](https://www.federalregister.gov/d/2025-16249).

# Appendix B. Methods and Interpretation

## B.1 Market data and node selection

ERCOT NP6-905-CD supplies 15-minute real-time settlement-point prices. Delivery date, hour, interval and DST flag determine UTC timestamps. The local-year grid has 35,040 intervals, or 35,136 in leap-year 2024. Shared unpublished intervals are excluded from all points, with no interpolation or zero fill: three intervals in 2023, one in 2024 and two in 2025. The daytime 2023 gaps coincide with about 47.6 MWh of simulated energy. Hubs and load zones remain distinct benchmark types.

The 641-node cross-section requires RN type, membership in the 10 September 2026 official list and coverage in 2025. The 485-node panel adds three-year common coverage. Coverage rules favor continuously observed points and need not represent future entrants; commissioning dates have not been reconciled. Sample fractions describe the screened population and are not investment probabilities.

The weather-price matrix uses a fixed UTC−6 calendar key, drops 29 February and intersects valid intervals across years. Full-year reference NPV is approximately +$97.76m, −$91.84m and −$85.97m for 2023–2025; common-calendar values are +$97.76m, −$92.15m and −$85.97m. The 2024 difference is mostly the leap-day exclusion. Common-calendar results are labeled throughout the comparison tables.

The original 2025 system intraday exhibit uses 363 dates excluding the two DST transition days and 8,712 hours; the seasonal exhibit retains 365 dates. The added residual-load exhibit instead uses all 2025 hourly observations grouped by America/Chicago civil hour. Fuel-mix average MW is consistent with hourly load MW; residual load subtracts wind and solar only. It is not net of all supply or storage.


**Table B-1. Coverage-screen comparison using the original 2025 cross-section.**

| Coverage cohort | Nodes | Median output-weighted price, $/MWh | Mean output-weighted price, $/MWh |
|---|---:|---:|---:|
| 2025-only eligible | 156 | 23.86 | 24.24 |
| Three-year screened | 485 | 22.94 | 23.50 |

*Source: original 2025 eligible-node screen, same reference output weights; three-year cohort membership from the weather-price matrix. The 156 points outside the common panel are not labeled as new plants; their commissioning histories are unverified. Different coverage cohorts are not a randomized comparison.*

## B.2 Output and financial conventions

The hypothetical system is 100 MWac / 132 MWdc in one Pecos County NSRDB location (identifier 1142134), simulated with PVWatts v8 through PySAM 7.1.1. Design, losses and degradation remain as stated in Chapter 9. It is neither an operating-plant measurement nor a county average. Leap-day output uses a neighboring-day approximation; comparing two such approximations changes annual energy by about 0.002%, which is not a bound on actual leap-day error.

The aggregate loss of 14.0757% is the PVWatts v8 default stack in PySAM 7.1.1: soiling 2%, shading 3%, mismatch 2%, wiring 2%, connections 0.5%, light-induced degradation 1.5%, nameplate 1% and availability 3%. It is not derived from site measurements. NSRDB timestamps are in UTC. The simulation aligns five-minute weather to 15-minute price intervals, and the multi-year matrix uses the fixed UTC−6 calendar key described in B.1. [CL-B-04]

End-2026 CAPEX and 30 operating years from 2027 are valued in real 2025 dollars at a 2026 valuation point. For the unchanged base price shape, NPV = 15.471935 × first-year real receipts − $187.321206m. The intercept includes CAPEX and discounted FOM, replacement and decommissioning. Different price trends or fixed nominal receipts need their own cash-flow evaluation.

Historical price files are not CPI-harmonized before the multi-year financial experiment; each original numerical level becomes a constant-real scenario input. This convention preserves the original estimates but differs from a same-purchasing-power historical comparison. The base ATB cost conversion uses CPI-U from 2023 to 2025; the conversion alone does not harmonize those historical prices.

The original single-IRR field stays null for multiple-root and uncertified-root cases. Node base has numerical roots near −96.52% and −2.53%; node downside −24.85% and −8.60%; fixed base −48.21% and −2.60%; fixed upside −86.48% and +1.41%. Node upside has a unique reported root near −0.42%; fixed downside has no root found, with search completeness uncertified. No root at or above 4.27% was found; NPV is negative at all three tested rates. Selecting the root nearest zero would not establish a unique investment return. NPV is the primary comparison.

ATB FOM includes system, property and administration allowances. Insurance and component-failure costs are among the published categories. The exact project budget, replacement overlap and any unrepresented costs remain open. Baseline returns exclude income tax, credits and financing; the separate nominal credit example is not an after-tax valuation.

**Table B-2. Contract risk allocation: structural comparison, subject to the actual agreement.**

| Exposure | Merchant node sale | Simplified node-level fixed-price route | Hub-settled financial PPA |
|---|---|---|---|
| Output and availability | Seller | Seller unless contracted otherwise | Seller; contracted quantity may differ from output |
| Timing/shape | Seller | Depends on paid volume and delivery obligation | Generation-versus-contract shape and hedge reference matter |
| Node-to-hub basis | Embedded in node price | No separate hub leg in this simplified route | Seller retains node-minus-hub exposure if quantities match |
| Negative prices | Dispatch and incentive decision | Payment suspension and delivery clauses determine exposure | Physical node receipts and financial hub settlement both matter |
| Policy and counterparty | Owner's tax and market exposure | Allocation, change-in-law and credit terms required | Same, plus collateral and financial-settlement obligations |

## B.3 Conditional regressions and inference

Hourly benchmark-price regressions include solar, load, wind, Henry Hub daily gas prices, daily temperature summaries and calendar controls. Variants include nonlinear terms, date fixed effects, interactions, tail restrictions and a median regression. The solar-level coefficient in an interaction or nonlinear specification is not a constant marginal association. Actual solar output may respond to prices, and missing available capacity, outages, imports and constraints leave simultaneity and omitted-variable concerns unresolved.

The out-of-sample exercise fits 2023–2024 and predicts 2025. Unseen year-month fixed-effect columns are set to the training base, so level shifts are not supplied as known future effects. The hour-of-week comparator is the training-sample mean for each weekday/hour; the constant comparator is the training mean. The error comparison tests this forecast construction rather than a model supplied with realized 2025 fixed effects.

The principal hourly uncertainty estimates use heteroskedasticity- and autocorrelation-consistent errors with a 168-hour lag, with 24- and 336-hour alternatives. Block checks preserve contiguous observations; details of successful and failed fits are in the accompanying technical outputs. Negative-price models use hourly means rather than interval-level events; failed or nonconvergent models are not treated as null findings. Three years provide limited regime variation. No instrument, natural experiment or other causal design is used.

![Figure B-1. Conditional solar-price coefficients across model choices](figures/empirical/F5_solar_price_association_forest.png)

*Source: coefficient and block-uncertainty tables [E-B]. Coefficients are conditional associations. The held-out prediction comparison is weaker than simple averages and does not justify future price forecasts.*

## B.4 Accounting contributions and tail stresses

Weather/price Shapley allocation divides their interaction equally. Log-mean Divisia index (LMDI) accounting instead splits the change into volume, average price and output-price matching, with the export-rule change recorded separately. These are alternative identities, not a nested causal model. Means in Table B-3 add to the mean total; medians of separate components generally do not add.

The top-price deletion holds costs fixed while removing receipts in selected intervals; percentile caps replace prices above the cap. The quoted scarcity-date variant deletes daily receipts on dates reaching $1,000/MWh; a separate variant replaces each flagged daily receipt with the median nonflagged daily receipt. The best-hours statistic accumulates the highest-receipt 15-minute intervals until the positive NPV buffer is exhausted. Each asks a different stress question. None is a correction to actual prices.

Within-year paired weather/price day-block resampling uses 2,000 draws and alternative block lengths. It conditions on that year's empirical regime; it is not season-stratified long-run uncertainty. Equal three-year receipt weights are chosen assumptions. The additional break-even mixture uses a discounted receipt weight for 2023 versus the average of the other two years; it does not estimate a frequency or an optimal sequence of years.

## B.5 Finance integration: reproducible arithmetic and evidence boundaries

The finance calculation layer reads the scenario cash flows and finance-supplement tables. It changes no regression coefficient, simulated output, decomposition, sample estimate or baseline return. Credit PV scales the earlier illustration by OCC / total CAPEX; the year-16 zero-reserve variant adds $3.5m / 1.0427^16; paid-volume stress divides the no-unpaid break-even by one minus the assumed unpaid share. These are separately labeled financial settings.

EIA cohort statistics are re-screened explicitly by year, county field, quality flag and tracking field. Both the broader and tracking-only samples are retained, along with a sensitivity excluding Emerald Grove's disputed county assignment. Their nameplate denominator comes from the 2025 EIA record. No weather normalization, causal calibration or EIA raw-workbook rebuild is claimed. Selected source PDFs accompany the report in the research companion; the full raw-data archives are needed only to reproduce the upstream research.

## B.6 Crossed weather and price years

The 3×3 experiment holds the site design constant and pairs each of three weather profiles with each of three historical price shapes. Diagonal cells are same-year pairings of simulated output and observed prices; off-diagonal cells are counterfactual combinations. Calendar mapping and common exclusions are held fixed, using the fixed UTC−6 calendar key described in Appendix B.1. [E-A]

![Figure B-2. Weather-year and price-year scenario matrix](figures/empirical/F2_weather_by_price_matrix.png)

*Source: multi-year analysis, weather-price comparison tables [E-A]. NPV uses 4.27% real discounting and a 30-year repetition of first-year price conditions. The common-calendar matrix is not a probability distribution or a price forecast. Left: median NPV across 485 settlement points; center: TAYGETE2_ALL; right: share of points with positive NPV, not a probability. The color bar applies to the NPV panels.*

Under 2023 prices, changing the weather profile leaves median NPV positive, although it changes its magnitude. Under 2024–2025 prices, the median remains negative across all three weather profiles, so weather volume alone does not explain the sign change. More energy can coincide with lower value when its timing matches high prices less well.

## B.7 Model accounting of the NPV change

Changing price and weather together from 2023 to 2024 reduces mean NPV by $179.31m across the 485 nodes. An allocation that splits the interaction equally assigns −$174.68m to the price profile and −$4.63m to weather: about 97% and 3% of the net decline. This is model accounting, not an explanation of what caused market prices to change. [E-A]

The separate accounting table below asks how changes in total volume, average price, output-price timing and the negative-price operating rule combine. **Means are used so the displayed contributions add to the displayed total**, apart from rounding. This is a second allocation of the same change, rather than a breakdown of the price contribution above.

**Table B-3. Mean contributions to the NPV change across 485 nodes; $m.**

| Transition | Volume | Average price | Output-price timing | Export-rule adjustment | Total |
|---|---:|---:|---:|---:|---:|
| 2023 to 2024 | +5.64 | −102.49 | −83.13 | +0.67 | −179.31 |
| 2023 to 2025 | +6.36 | −72.24 | −114.08 | +1.88 | −178.08 |
| 2024 to 2025 | +0.42 | +17.74 | −18.13 | +1.21 | +1.23 |

*Source: node-level component outputs [E-A]; arithmetic means across nodes, used so that components add to the total (medians of separate components generally do not). Definitions and alternative accounting are in Appendix B.4.*

![Figure B-3. Mean components and total NPV change](figures/Panel_Mean_Decomposition.png)

*Source: same component means as Table B-3. Markers show totals; bars show accounting contributions, not causal effects.*

From 2024 to 2025, the average-price improvement is largely offset by less favorable output-price timing. This distinction matters commercially: a higher annual average price alone does not guarantee better solar receipts. Historical price currency treatment is stated in Section 10.9.

## B.8 Resampling and mixture scenarios

Within-year block resampling preserves some local dependence but conditions on the historical year's market environment. Reported 2023 NPV intervals change materially with block length, illustrating uncertainty within that year. They do not estimate how often a 2023-like regime will occur. In particular, the fraction of positive resampled draws is not a probability that a future project will be profitable. [E-C]

![Figure B-4. Reference-node resampling and the screened-node mixture distribution](figures/empirical/F8_bootstrap_and_mixture_scenario.png)

*Source: multi-year analysis, within-year resampling and mixture tables [E-C]. Resampling is conditional on a particular year. The mixture is an equal-weight analytical setting rather than an estimated probability-weighted expectation. Tail and resampling inputs use full annual calendars; the common-calendar matrix is a separate comparison.*

An equal-weight average of each node's first-year receipts across the three years gives a median NPV of approximately −$21.4m, with 12.2% of screened nodes positive. A separate break-even calculation mixes the 2023 receipts with the average of 2024–2025 receipts: the median of node-level required weights is approximately **44.9%** of discounted revenue weight assigned to the 2023 setting; the reference needs **47.7%**. These are analytical mixture weights, not probabilities or an integer count of profitable years. The timing of high-price years matters because earlier receipts carry more present value. Equal weights are a chosen stress setting. With only three observed years, neither those weights nor the resulting positive share establish a long-run return distribution.

## B.9 Market, credit and storage calculations: methods

The three calculations in Sections 10.8 (production credit), 10.10 and 12.4 are arithmetic on the reviewed-edition outputs and public sources; `build/r1_calcs.py` reproduces them and writes `data/r1/`. No model in the original research chain was rerun, and no earlier estimate changes.

**Production credit (Section 10.8).** Fixed-route NPV is linear in the flat nominal price, with a slope of about $2.84m per $1/MWh at 4.27% (from −$73.74m at $40/MWh and zero at $65.97/MWh); the slope reproduces the investment-credit break-even of $53.51/MWh. Credit PV is the sum over years 1–10 of delivered energy × $30/MWh (or $6/MWh) ÷ 1.0427 to the power of the year. Cash timing within the year, transfer costs other than the stated price and the owner's tax capacity are not modeled. [M05]

**Storage screen (Section 12.4).** For a 1 MW / 4 MWh battery, each day's value is round-trip efficiency × the sum of the four highest hourly prices minus the sum of the four lowest, floored at zero, summed over the year. The order of charge and discharge within the day is ignored, prices are known in advance and degradation is excluded, so the result is an upper bound on energy arbitrage; ancillary-service revenue, which can be material in ERCOT, is not included. Reference-node 15-minute prices are averaged to hours; hub values use HB_BUSAVG hourly means on the fixed UTC−6 calendar key. Cost annualizes Lazard's capital and operating ranges over a 20-year life with a capital-recovery factor of 0.0754, 0.0872 or 0.1019 at 4.27%, 6% or 8%; augmentation, warranty and charging costs are excluded, which understates cost. [M04]

**Market references (Section 10.10).** Values are copied from the sources with their stated periods; none is adjusted to this report's dollar year or contract terms.

# Appendix C. Evidence Boundaries and Undisclosed Fields

The report supports procurement screening, contract comparison and tests of capital-recovery conditions. A verified asset valuation would require documented location, generation, settlement, contracts, all-in costs, tax eligibility and financing. The scenario results do not supply these.

**Table C-1. Specific fields not disclosed or not established in this edition.**

| Area | Field not available | Result it would affect | Status in this edition |
|---|---|---|---|
| Returns (FIN-01) | Definition-matched project or equity IRR for the nine named plants | Return comparison, hurdle rates | Not publicly disclosed |
| Operating output (FIN-02) | Plant availability, curtailment, same-year nameplate, metered delivery | Output calibration | System-level curtailment only |
| Contracts (FIN-03) | Energy-contract strike, tenor, hub, volume rule, negative-price clause and credit support; full REC agreement terms | Paid revenue and basis | Selected structures and environmental-attribute tenor disclosed; hub-hedge version hypothetical |
| Tax (FIN-04) | Construction start, placed-in-service date, material-assistance ratio, PWA, transfer price; PACER-complete appeal status | Credit cash and timing | Statute verified; public docket shows no appeal entry; case facts absent |
| Costs (FIN-05) | Delivered module and EPC quotations; ATB component table; site property tax and interconnection scope | Capital and operating cost | Scope crosswalk only |
| Location (FIN-06) | Official ERCOT–EIA crosswalk; historical mapping versions; original node-selection rationale | Applicability of the reference node | Attribute match; no settlement agreement exists for the hypothetical case |
| Currency (FIN-07) | — | — | CPI-restated version reported (Section 10.9) |
| Market regime (FIN-08) | Row-level 2026 price finality; 2026 site generation | Post-launch merchant value | Price coverage documented; no same-year 2026 return |
| Suppliers (FIN-09) | Covenant headroom; full maturity ladders (A-shares, JinkoSolar); A-share grants | Supplier resilience | Cash, borrowings, warranties and working capital compiled (Tables 4-3A and 4-3B) |
| Financing (FIN-10) | Coupon, tenor, sizing, reserves, tax-equity terms | Levered returns | Not publicly disclosed |
| Net receipts (FIN-11) | Loss factor, QSE fees, imbalance, REC price | Net cash receipts | Gross energy value only |

**Outside the scope of this edition.** The following topics lie outside the present analysis: expanding the overseas-factory sample; estimating industry inventory; local gas prices; attributing congestion with interval constraint data; a storage investment case (Section 12.4 gives only a screen); and new causal or forecasting methods. Three weather and price years provide neither validated P50/P90 output nor a long-run regime probability.

**Financing terms.** For Taygete I, the lead arranger's release reports a $256m financing arranged by CIT with five other lenders. For Taygete II, the Comptroller filing reports a foreclosure purchase initiated by the senior lender after the previous owner failed to repay its loan. Neither public record discloses the debt size relative to project cost, coupon or spread, tenor, amortization, sizing ratios (DSCR), reserve accounts, fees or a tax-equity allocation. The $256m is a financing amount, not a construction cost or a return. No levered or equity return is estimated.

The developer's release names the other lenders in the Taygete I financing as Deutsche Bank, National Bank of Canada, CIBC, Rabobank and Amalgamated Bank, with CIT as coordinating lead arranger. It names Nestlé as sole tax-equity investor, with Marathon Capital as Nestlé's financial advisor. It does not disclose the debt-to-cost ratio, pricing, tenor, the tax-equity flip date, target yield or allocation terms. [CL-FIN-10]

**Gross energy value versus net receipts.** Modeled revenue is gross energy value: metered-equivalent output multiplied by the 15-minute real-time settlement-point price. Net cash receipts would also reflect several items:
- losses between inverter and settlement meter, which sit inside the simulation's loss stack and are not separated to the settlement point;
- scheduling-entity fees;
- real-time deviation and uplift allocations;
- REC sales and registration costs;
- any hedge settlement.

Complete amounts and allocation terms are unavailable for the comparable plants. Selected environmental-attribute rights are disclosed, but their cash proceeds are not; omitted items are not established as zero-cost.

**Status of construction-start guidance.** A District Court memorandum opinion and order dated 6 June 2026 (Oregon Environmental Council v. IRS, D.D.C. No. 25-4400) declare Notice 2025-42 arbitrary and capricious under the Administrative Procedure Act, vacate it in full and remand it to the IRS. The court decided the claims of five of the seven plaintiffs. The public RECAP copy of the district-court docket, retrieved on 10 October 2026 (RECAP record last refreshed 16 September 2026), shows the case terminated on 8 June 2026 and lists no later filing; no appellate docket was located. RECAP is not a complete PACER record, and the IRS credit pages reviewed list no replacement guidance. The vacated notice is therefore not treated as controlling. Appeal and remand developments should be rechecked before any project-specific conclusion. Whether a given project began construction by 4 July 2026 remains a project-specific legal question, and the hypothetical case supplies no construction-start facts. [CL-FIN-04]

On price finality, the 2023–2025 archive prices follow the protocol rule that real-time prices are final at 16:00 on the second business day. The 2026 API data carry no version field. For the West hub, 423 intervals differ by more than $0.005/MWh from ERCOT's separate hub file, and the cause is not established. Successful download, or passage of the finality time, is therefore not treated as row-level proof of final prices. [CL-FIN-11]

# Appendix D. Glossary

**Table D-1. Abbreviations and terms.**

| Term | Meaning |
|---|---|
| ERCOT | Electric Reliability Council of Texas; system and wholesale-market operator |
| MIIT / IRENA | China's Ministry of Industry and Information Technology / International Renewable Energy Agency |
| ATB / PVSCM | Annual Technology Baseline / Photovoltaic System Cost Model; national references |
| OCC / GCC / FOM | Overnight capital cost / grid-connection cost / fixed operating and maintenance expense |
| MWdc / MWac | Module DC capacity / rated AC capacity; cost denominators must match |
| NSRDB / PVWatts / PySAM | Solar resource database / generation model / Python interface to the System Advisor Model |
| Capture price / ratio | Output-weighted price / output-weighted price divided by time-weighted price |
| Basis / HB_BUSAVG | Node minus benchmark price / ERCOT Bus Average 345-kV Hub |
| PPA / VPPA | Power purchase agreement / financial contract settled against a price reference |
| LCOE / NPV / IRR | Levelized energy cost / discounted net cash value / zero-NPV discount rate |
| WACC / DSCR | Weighted average cost of capital / debt-service coverage ratio |
| ITC / PTC / PFE | Investment tax credit / production tax credit / prohibited foreign entity |
| P50 / P90 | Output exceeded with specified probability over a stated horizon; not established here |
| HS / HTS / IEEPA | Harmonized trade classifications / U.S. tariff schedule / emergency economic powers statute |
| OCF / PPE / LLA | Operating cash flow / property, plant and equipment / long-lived assets |
| RMSE / HAC | Prediction-error measure / serial-correlation-robust uncertainty method |
| Batch Zero / WLPUN | Transitional large-load process / withdrawal-limited private-use network |
| MIP / AD/CVD | Minimum import price / antidumping and countervailing duties |
| CBP / USITC | U.S. Customs and Border Protection / U.S. International Trade Commission |
| 45X | U.S. advanced manufacturing production credit for qualifying components |
| PWA | Prevailing wage and apprenticeship requirements for full-rate tax credits |
| ORDC / QSE | Operating Reserve Demand Curve / Qualified Scheduling Entity in ERCOT |
| REC | Renewable energy certificate (environmental attribute) |
| SGIA / TSP | Standard generation interconnection agreement / transmission service provider |
| NPRR | Nodal Protocol Revision Request (ERCOT rule change) |
| LMDI | Log-mean Divisia index; an additive decomposition method |
