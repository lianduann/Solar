# Contract and Tax Decision Tree

**Executed:** 2026-10-09 (America/New_York). **Scope:** the hypothetical 100 MWac / 132 MWdc Pecos County standalone PV case with all capital paid at end-2026 and operations 2027–2056. This is a modelling decision map. It is not tax or legal advice and it does not establish that any credit is available.

## A. Revenue contract structure

### A.1 Executable identities

Notation per settlement interval *t*: metered output *G*, contract volume *H*, resource-node price *P_node*, hub price *P_hub*, strike *K*, renewable-certificate revenue *REC*, contract and market fees *fees*.

| Structure | Cash revenue in interval *t* | Who carries basis / shape / volume |
|---|---|---|
| Merchant at node (frozen node route) | *G·P_node* (output stopped when *P_node* < 0 in the frozen rule) | Seller carries everything |
| Physical fixed price (frozen fixed route) | *K·G·(1 − unpaid share)* | Seller carries unpaid energy; buyer carries price |
| Hub-settled virtual PPA | *G·P_node + H·(K − P_hub) + REC − fees* | Seller carries basis (*P_node − P_hub*) and any shape gap (*H ≠ G*) |
| Hub-settled VPPA, as-generated (*H = G*) | *G·(K + P_node − P_hub) + REC − fees* | Seller carries basis only |
| Fixed-shape / block hedge | *G·P_node + H_shape·(K − P_hub) − fees* with *H_shape* fixed in advance | Seller carries basis, shape and volume risk |

A contract must also state four things before it can be modelled:

1. How settlement works when *P_hub* < 0. Either the swap pays *K − P_hub*, so the seller receives more than *K*, or settlement is suspended.
2. Whether curtailed or economically stopped MWh count in *H*.
3. Who keeps the RECs.
4. Credit support and the termination payment.

None of these is public for the comparable projects reviewed (Contract-Terms.csv CT-01 to CT-03).

### A.2 Evidence for the reference location (frozen panel table, recomputed independently)

The table below uses 15-minute RTM settlement point prices from the retained NP6-905-CD archives, weighted by same-year simulated output on the common calendar. All values are in USD/MWh.

| Year | TAYGETE2_ALL capture | HB_WEST capture | Gen-weighted basis (node − HB_WEST) | Time-weighted basis |
|---|---:|---:|---:|---:|
| 2023 | 64.89 | 64.94 | −0.05 | +10.82 |
| 2024 | 20.85 | 20.60 | +0.25 | +11.33 |
| 2025 | 22.13 | 21.46 | +0.67 | +13.45 |

**Reading.**

- In solar hours the reference node and HB_WEST price almost the same. The node's premium over the hub appears outside solar hours.
- Settling a contract at HB_WEST therefore does not by itself raise the solar unit value: the West-hub capture ratio is 0.65–0.75 in 2024–2025.
- What a hub-settled contract transfers to the buyer is the hub price level and shape. The seller keeps a small average basis, but interval-level dispersion is large. The 5th–95th percentile ranges in solar intervals are in `data/Node-Hub-Basis-2023-2025.csv`.

Under *H = G* with no fees or RECs, realised revenue per MWh equals *K* plus the basis term: *K* − 0.05, *K* + 0.25 and *K* + 0.67 for 2023, 2024 and 2025 (Finance-Arithmetic-Checks V-2023 to V-2025).

### A.3 Tenor and tail

No public tenor was found for any comparable project. Two references exist, and neither is an observed tenor for a West Texas project:

- LevelTen's public material does not state tenor.
- Berkeley Lab assumes, for its own levelisation, that LevelTen offers are 12-year flat nominal contracts.

The 10- and 15-year cases therefore remain scenario settings. The merchant tail must use a separately dated price scenario. Until one is retained, the tail stays null (Contract-Terms.csv CT-08).

### A.4 Decision points for the author

1. Keep the 30-year physical fixed-price route as a simplification, and label it that way.
2. Add a hub-settled VPPA route with *H = G* and scenario tenors of 10 and 15 years.
3. Choose a negative-price rule: settle through, or suspend below zero.
4. Decide whether the 15.24% unpaid share is kept for the physical route only.

## B. Tax-credit availability (law as retrieved 2026-10-09)

```text
Q1  Did physical work of a significant nature (or, after the 2026-06-06 vacatur of Notice 2025-42,
    a restored 5% safe harbour with costs paid/incurred) begin ON OR BEFORE 2026-07-04?
    ├─ YES (branch A) → no 2027 placed-in-service cut-off; continuity rules apply
    │      (with Notice 2025-42 vacated, the continuity rules of the earlier beginning-of-construction
    │       notices govern; their text was not retained in this round — verify before modelling)
    └─ NO / unknown (branch B) → credit only if PLACED IN SERVICE ON OR BEFORE 2027-12-31
           └─ PIS after 2027-12-31 → no 45Y/48E credit (pre-tax baseline is then also the after-tax credit case)
Q2  Construction begins after 2025-12-31?  → material-assistance cost ratio ≥ 40% (2026 start) / ≥ 45% (2027 start)
Q3  Taxpayer a specified or foreign-influenced entity?  → yes: no credit
Q4  Prevailing wage & apprenticeship met?  → yes: 30% ITC or 1.5¢/kWh indexed PTC (3.1¢ for 2026); no: 6% / 0.3¢ indexed
Q5  ITC (48E) or PTC (45Y)?  (one per facility; scenario choice)
      ITC: base = qualified energy property only; interconnection property excluded above 5 MWac;
           depreciable basis reduced by 50% of credit; 10-year SFE-payment recapture
      PTC: 10 years of metered kWh sold; output worth producing while P_node > −PTC value
Q6  Monetisation: own use (needs tax capacity) | transfer under 6418 (not to an SFE; price discount and timing) |
    tax-equity partnership (flip). Never count transfer proceeds and tax-equity benefits for the same credit.
```

**What the hypothetical case would still have to prove:**

- the construction-start method and date;
- the placed-in-service date;
- supplier MACR certifications;
- owner and lender foreign-entity screens;
- PWA payroll records;
- an item-level basis study;
- binding-contract and acquisition dates for bonus depreciation;
- owner type (regulated or not);
- the credit buyer or tax-equity terms.

A late-2026 payment does not prove construction began. A model calendar year "2027" is not a placed-in-service date.

**Expert-review check:**

- The review's "start before July 4, 2026 **or** placed in service by end-2027" structure is correct as an either/or test.
- The protected start window, however, includes July 4, 2026 itself.
- As of 2026-10-09 that window has closed, so for this case the only open route is placed-in-service by 2027-12-31. Within that route, the material-assistance test applies because construction would begin after 2025-12-31.

## C. Property-tax treatment (Texas)

| Instrument | Evidence | Status for a 2026–27 case |
|---|---|---|
| Chapter 313 school M&O limitation | Taygete II (#1377): USD 30m limitation. Comptroller estimate of the 15-year M&O levy: 20.57m without the limit, 6.61m with it, for a 255 MW plan | Secondary sources say Chapter 313 closed to new agreements at end-2022 (primary statement not retained). Do not assume |
| Chapter 403 (JETI) | Comptroller FAQ: "All manufacturing projects and dispatchable electric generation facilities are eligible" | Standalone PV is not shown as eligible. Do not assume |
| Chapter 312 county abatement | Taygete II application, Schedule D: Pecos County, 10 years, levy 1,169,058/yr without incentive, net 1,000/MW | Local and negotiated. A sensitivity input, not a default |

The ATB/PVSCM FOM embeds property tax at 0.2% of system price per year. A Texas-specific property-tax line should be tested as an increase relative to FOM, not added on top of an unchanged FOM.
