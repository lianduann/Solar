# Model Upgrade Specification

**Prepared:** 2026-10-09 (America/New_York). **Status:** specification only. The frozen panel-edition model, its register and its outputs stay unchanged. Nothing here was run against the old model, and no new NPV/IRR is reported.

## 1. Principles

1. Each layer gets its own cash-flow definition. A project IRR and an equity IRR never appear in the same column.
2. Every input carries one of four tags: `observed`, `reference`, `assumed` or `unknown`. If an output depends on an `unknown` input, the output is `null`.
3. No cost or benefit is counted twice. In particular:
   - FOM already contains land, property tax at 0.2%, insurance, management and annualised component replacement.
   - Credit-transfer proceeds and tax-equity benefits are alternatives for the same credit, never added together.
   - Interest is never deducted from an unlevered cash flow that is then discounted at a WACC.
4. All cash flows are annual, in real 2025 USD. Nominal contract prices are deflated at 2.5%, as in the frozen register.

## 2. Annual cash-flow structure

| Line | Formula | Inputs and tags |
|---|---|---|
| Construction spend | Σ_s CAPEX_s by period *s*. The frozen model uses 100% at end-2026; a phased profile is optional | OCC, GCC `reference`; phasing `assumed` |
| Net generation | *E_t* = *E_1*·(1 − d)^(t−1) − stopped MWh_t. Either simulated (frozen), or a sensitivity band at 25–29% AC from EIA comparables | *E_1* simulated; band `observed` (Finance-Input-Recommendations FR-01) |
| Contract revenue | VPPA: Σ_i [*H_i*·(*K* − *P_hub,i*)] in contract years; physical: *K*·*E_t*·(1 − unpaid) | *K*, tenor, *H* rule `assumed`; *P_hub* historical `observed` |
| Merchant revenue | Σ_i *G_i*·*P_node,i* (node), all years | price path `observed` for 2023–2025, scenario otherwise; tail `unknown` → null |
| REC revenue | *E_t*·*P_REC,t* if retained | `unknown` → 0 only in a scenario labelled "REC excluded" |
| Opex | FOM·MWac + Texas property-tax increment + QSE/settlement fees + decommissioning (year 30) | FOM `reference`; increment `assumed` 0–8 USD/kWac-yr; fees `unknown` |
| EBITDA | revenue − opex | — |
| Tax depreciation | MACRS 5-yr on depreciable basis (less 50% of ITC if ITC), bonus per 168(k) if elected | after-tax layers only |
| Cash taxes | τ·(EBITDA − depreciation − interest_if_levered) with loss-use rule stated (stand-alone NOL carry-forward vs consolidated taxpayer) | τ `assumed`; loss-use rule must be chosen |
| Credit | ITC: 30% (or 6%) × qualified basis, in the year placed in service. PTC: credit rate × kWh for 10 years. Received in cash at transfer price *x* with lag *L*, or used by the owner | eligibility switch (Tax-Eligibility-Matrix); *x*, *L* `unknown` |
| Unlevered after-tax CF | EBITDA − cash taxes (no interest) + credit cash − capex − ΔWC | — |
| Levered equity CF | Unlevered after-tax CF + debt draws − fees − interest − principal − reserve funding + reserve releases − interest tax shield adjustment (already inside cash taxes when interest is deducted) | all debt terms `unknown` → null |

## 3. Layers that can be calculated now

| Layer | Calculable now? | What it adds | Still null |
|---|---|---|---|
| L1. Frozen pre-tax unlevered baseline | Yes (frozen) | Payment stress on the fixed route at 0% / 15.24% / 30.48% unpaid energy. The break-even moves from 55.91 to 65.97 to 80.43 USD/MWh nominal flat (Finance-Arithmetic-Checks M-01, M-02: arithmetic scaling of the frozen break-even, not a new model run) | — |
| L2. Hub-settled VPPA (10 or 15 years) plus merchant node tail | Partly. The contract leg is computable for any assumed *K* using historical hub prices and *H = G*. The tail needs a dated price scenario | Separates the basis term (−0.05 / +0.25 / +0.67 USD/MWh in 2023/24/25) from the hub shape | *K* market value; tail price; negative-price clause; fees; REC |
| L3. After-tax unlevered, ITC **or** PTC | Only as a labelled eligibility scenario | Depreciation, 50% basis reduction, exclusion of GCC from the ITC base, transfer discount | Eligibility facts (PIS ≤ 2027-12-31, MACR, PWA); transfer price; tax rate and loss use |
| L4. Levered equity (DSCR/LLCR, distributions, IRR/MOIC) | No | — | Debt size, rate, tenor, sculpting, reserves, fees, sweep; tax-equity flip terms |

## 4. IRR controls

- Report the NPV curve over 0–12% (real), MOIC and the undiscounted payback year next to any IRR.
- If cash flows change sign more than once, list all real roots. Report a single "economic" IRR only when the NPV curve is monotonic over the reported range. Otherwise set IRR to `null` and point to the NPV curve.
- MIRR is optional. If used, state the finance rate and the reinvestment rate, both real 2025 USD, and do not present MIRR as more objective than NPV.
- An equity hurdle (for example ATB 8% nominal) must not be used to discount unlevered cash flows.

## 5. Sensitivities

Each sensitivity is run one at a time first, then in coherent groups. No probability of "success" may be computed without an estimated joint distribution.

1. Price level, shape and basis.
2. Tenor: 10 or 15 years, and the tail price.
3. Qualified basis and placed-in-service delay, which switches the credit on or off.
4. All-in CAPEX: the network-upgrade overlap of −51 to −66 USD/kWac, and the interconnection allowance.
5. FOM: the Texas property-tax increment.
6. Availability and curtailment: delivered CF band 25–29%.
7. Interest rate and DSCR, in layer L4 only.

## 6. Results this specification forbids until evidence arrives

- Any comparable "industry IRR" range: no comparable discloses a project IRR (Return-Metric-Comparability.csv).
- Any levered equity IRR or DSCR.
- Any post-RTC+B merchant price path presented as observed.
- Any credit value presented as received.
