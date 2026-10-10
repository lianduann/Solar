# Separately Versioned Finance Scenarios: OCC Credit Base, Hub-Settled VPPA, CPI Harmonisation

**Version:** 2026-10-09 (America/New_York), authorised by the author on the same day.

**Relationship to the frozen panel edition:** these are new, independent calculation versions placed beside the frozen results. The frozen model, register and outputs are unchanged, and every frozen figure used here was reproduced to within USD 1 before use (`data/scenario_build_log.json`). All results are pre-tax, unlevered and in real 2025 USD, discounted to end-2026, on the same cost side as the frozen node route:

- CAPEX 143.67m;
- ATB FOM;
- year-16 replacement;
- year-30 decommissioning;
- 0.7%/yr degradation.

## 1. Credit-base scenarios (`data/Credit-Base-Scenarios.csv`)

### What the "OCC-only" base means

It is an analytical assumption, as approved by the author: OCC is used as the credit base. It does **not** mean every OCC item qualifies. The scope check behind it:

1. **Statute.** For a facility above 5 MWac, 48E(b)(1)(B) admits no interconnection property. Grid-connection cost (GCC, 17.63m) is therefore removed. That removal is the only difference between A0 and A1.
2. **Remaining OCC is not all energy property.** The DOE/NLR PVSCM 2025Q1 benchmark (PV-only, MMP) puts 10.9% of system price in generator substation, generator transmission line and a generic network-upgrade line. Scenario A2 removes that share as a scope check. If ATB has already moved these items into GCC, A2 excludes them twice; this cannot be confirmed because the ATB component table is Tableau-only.
3. **Soft costs.** In the same benchmark, 37.7% of price is field labour, office work and "Other" (overhead, profit, contingency, sales tax). These enter basis only to the extent they are allocable to energy property. No item-level allocation exists, so none is applied.

### Dollar basis and timing

The frozen convention is kept, so A0 reproduces the panel figure exactly:

| Step | Formula |
|---|---|
| Nominal base in the construction year | Real 2025 base × 1.025 |
| Credit | 30% of the nominal base, as a fixed nominal receipt at end-2027 |
| Deflation | Divide by 1.025² to 2025 USD |
| Discounting | One year at the scenario rate |

Variants:

- receipt at end-2028;
- transfer at 0.95 or 0.90 per credit dollar — assumed values, since no market price is retained;
- a 6% rate if the prevailing wage and apprenticeship requirements are not met.

### Results at 4.27% (USD m)

| Base | Credit cash (nominal) | PV | Node-route NPV | Fixed-route NPV |
|---|---:|---:|---:|---:|
| Frozen, no credit | — | — | −85.97 | −73.74 |
| A0 OCC+GCC (original, kept for tracking) | 44.18 | 40.33 | −45.64 | −33.41 |
| **A1 OCC only (approved assumption)** | **38.76** | **35.38** | **−50.59** | **−38.36** |
| A2 OCC less PVSCM grid items (scope check) | 34.55 | 31.54 | −54.43 | −42.20 |
| A1 with cash at end-2028 | 38.76 | 33.10 | −52.86 | −40.64 |
| A1 transferred at 0.90 | 34.88 | 31.84 | −54.12 | −41.90 |
| A1 at 6% (PWA not met) | 7.75 | 7.08 | −78.89 | −66.66 |

Every credit row remains an eligibility-unproven scenario. Eligibility requires all of:

- placed in service by 2027-12-31, because the early-construction window has closed;
- a material-assistance cost ratio of at least 40% for a 2026 construction start, or 45% for 2027;
- PWA;
- an item-level basis study.

The pre-tax convention also omits depreciation and the 50% basis reduction, which only an after-tax layer can capture.

## 2. Hub-settled VPPA route (`data/VPPA-Route-Scenarios.csv`, `data/VPPA-Breakeven-Strikes.csv`)

### Structure

| Element | Setting | Status |
|---|---|---|
| Physical sale | Metered output *G* sold at TAYGETE2_ALL 15-minute RT prices | price observed (historical path) |
| Financial hedge | Swap at HB_WEST: interval payment *H·(K − P_hub)* | structure assumed |
| Volume | *H = G*, as-generated | assumed |
| Strike *K* | Nominal flat: 40 (the frozen hypothetical fixed price) or 49 (LevelTen ERCOT solar P25 offer, Q4 2025, a secondary report with tenor not visible) | assumed |
| Tenor | 10 or 15 years | assumed; no public tenor for comparable projects |
| Merchant tail | Node sale at the same historical price path, real-flat | scenario, not a forecast; no dated forward curve retained |
| Negative-hub clause | (i) settle through; (ii) settlement suspended when *P_hub* < 0 | assumed switch |
| Dispatch | (a) stop when *P_node* < 0, the frozen merchant rule; (b) run while *P_node* + hedge ≥ 0 | assumed switch |
| Fees, RECs, imbalance | 0 | missing, not zero-cost |
| Price paths | 2025 (frozen base). 2024 and 2023 with same-year weather, each both CPI-restated and as the frozen nominal-reuse convention | observed history |

**Check:** with tenor = 0 the route reproduces the frozen node-route NPV (−85,965,281 USD).

### Results on the 2025 price path at 4.27%

| Tenor | Dispatch / clause | NPV at K = 40 | NPV at K = 49 | Break-even K (nominal flat) |
|---|---|---:|---:|---:|
| 10 | stop if node < 0 / settle through | −69.18m | −54.22m | 81.6 |
| 10 | run if node + hedge ≥ 0 / settle through | −56.90m | −39.30m | 69.1 |
| 10 | run / suspend if hub < 0 | −69.53m | −54.49m | 81.5 |
| 15 | stop / settle through | −67.44m | −48.25m | 71.6 |
| 15 | run / settle through | −51.66m | −29.07m | 60.6 |
| 15 | run / suspend if hub < 0 | −67.93m | −48.64m | 71.7 |

At 6% and 8% the break-even strikes rise to 68–107 USD/MWh.

### Reading the results

- **Realised value per MWh.** Year-1 realised value is close to the real strike plus the small node-HB_WEST basis: 38.73 USD/MWh at K = 40 nominal, which is 38.07 real in 2027 plus 0.67 basis. A hub-settled contract converts the low hub capture (HB_WEST 0.65 in 2025) into the strike for the contract years. It does not remove basis risk, but at this location that risk has been small on average.
- **Tail dependence.** With a 10-year tenor, 43% of the revenue present value at K = 40 comes from the merchant tail (50.4m of 118.1m). The break-even strike therefore depends heavily on the unsourced tail price.
- **2023 path.** A repeated 2023 price path implies break-even strikes of only about 19–46 USD/MWh, because the 2023 scarcity prices are repeated through the tail. This is why historical-path tails cannot stand in for a forecast.
- **Settle-through is worth about 12 USD/MWh of strike.** Combined with contract-aware dispatch, settling through negative hub prices lowers the 10-year break-even by about 12.6 USD/MWh. The plant keeps generating when the swap pays more than the node loss. Whether a buyer accepts settle-through is a negotiated term, and suspension clauses remove most of this benefit.
- **Comparison with market quotes.** No scenario breaks even at the LevelTen ERCOT P25 offer of 49 USD/MWh on the 2025 price path. That offer's tenor, settlement point and terms are not visible, so this is a scenario comparison, not a market test.

## 3. CPI-harmonised scenario (`data/CPI-Harmonised-Scenario.csv`)

### What changes

The frozen outputs reuse 2023 and 2024 nominal prices as if they were 2025-dollar real prices. The CPI version multiplies those prices by the CPI-U annual-average ratios: 1.0566 for 2023 and 1.0263 for 2024. Everything else is unchanged.

The economic-stop rule is unaffected, because the sign of prices does not change. Year-1 revenue therefore scales by the factor, and NPV changes by *a* × revenue × (factor − 1), where *a* = 15.4719 is the frozen degradation-and-discount annuity at 4.27%.

### Results

| Point / sample | Year | Frozen NPV | CPI NPV | Difference |
|---|---|---:|---:|---:|
| TAYGETE2_ALL | 2023 | +97.76m | +113.89m | +16.13m |
| TAYGETE2_ALL | 2024 | −92.15m | −89.64m | +2.50m |
| TAYGETE2_ALL | 2025 | −85.97m | −85.97m | 0 |
| 485-node median | 2023 | +99.78m | +116.02m | +16.25m |
| 485-node median | 2024 | −81.33m | −78.55m | +2.79m |

The share of nodes with positive NPV does not change: 100% in 2023, 2.7% in 2024, 0.4% in 2025. CPI restatement raises the older price years' value by 2.6–5.7%. It changes no sign at the reference node and no qualitative conclusion.

## 4. Still missing

- A dated merchant tail price.
- Actual contract terms: strike, tenor, negative-price clause, credit support.
- Fees, RECs and imbalance.
- Credit eligibility facts and the transfer price.
- An after-tax layer: tax rate, loss use, MACRS and bonus depreciation, basis reduction.
- Any debt terms.

No IRR is reported. Most of these cash flows change sign only once, but they are scenario constructs, so NPV and break-even strikes are the stated outputs.
