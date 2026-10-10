# Follow-up Evidence Obtained Without Login

**Date:** 2026-10-09 (America/New_York); files retrieved 2026-10-10 00:11–00:13 UTC.

**Files:** originals and receipts (URL, time, SHA-256) are in `Data/raw/2026-10-09_Finance-Deepening/followup/`, receipts in `fetch_receipts.csv`. This file updates the 2026-10-09 supplement. It does not modify the supplement.

## 1. Texas statutes (browser-rendered official site)

### Chapter 313 (FIN-05 property tax)

The current Tax Code Chapter 313 no longer contains Subchapters B and C, the appraised-value limitation programs. The saving provision in §313.171(a) refers to limitations "approved ... before the expiration of that subchapter".

**Status:** confirmed from the official code text that a new 2026–27 project cannot obtain a Chapter 313 limitation. The expiry date itself is not stated in the retained text.

### JETI (FIN-05)

Government Code §403.602(8)(B) states that an eligible project "does not include a project to construct or expand a new or existing: (i) nondispatchable electric generation facility; or (ii) electric energy storage facility."

**Status:** confirmed. A standalone PV plant is outside JETI, so the only remaining property-tax incentive route is a county Chapter 312 abatement.

### Interconnection allowance (FIN-05)

PURA §35.004(d-1)–(d-3) directs the PUCT to set an allowance for transmission-owner interconnection costs. Costs above it "must be directly assigned to and collected from the generation resource". The allowance is reviewed at least every fifth year.

**Status:** this matches the PUCT rule already retained.

## 2. ERCOT Independent Market Monitor, 2025 State of the Market Report (Potomac Economics, published 2026)

All points below are from the report itself.

- **RTC go-live (p.30).** RTC went live on 5 December 2025. Before then, shortage pricing came through the ORDC adder. In 2025 the ORDC was active for only 57 hours, "just over one-third of the previous year's total and less than 8% of the annual average for 2021-2024".
- **West zone prices and congestion (p.29, p.15).** The West zone had the highest average zonal price in 2025 for the second year running. It also had the highest number of negative-price intervals and the most price spikes of any load zone. The report attributes this to West-zone congestion: transmission has not kept pace with Panhandle renewables and Permian demand growth.
- **Solar curtailment (p.40).** "Roughly 6% of solar generation was curtailed in 2025, similar to 2024 levels."
- **Storage fleet (p.35).** "Total energy storage capacity exceeded 17 GW." This is higher than the 13.7 GW survivor-based EIA-860 count in the supplement. The IMM figure's reference date and scope (registered capacity, possibly including early 2026) differ from the EIA count, and both are reported as stated.
- **Use in the analysis.** These are descriptive facts. No causal effect of RTC+B or storage on the reference node is estimated.

## 3. HB_WEST, January–September 2026 (post-RTC+B), no login (`data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv`)

**Method.** Source: ERCOT NP6-785-ER 2026 year-to-date file, published 2026-10-04. The 2026 prices are weighted with the 2025 simulated solar profile, matched by local month, day and interval, because no 2026 energy series exists. The result is a profile-weighted hub price, not an observed capture price.

| Jan–Sep | Time-weighted | Profile-weighted | Ratio | Share of negative intervals | Profile energy in negative intervals |
|---|---:|---:|---:|---:|---:|
| 2025 (pre-RTC+B) | 32.43 | 21.36 | 0.66 | 7.7% | 13.7% |
| 2026 (post-RTC+B) | 29.40 | 18.24 | 0.62 | 14.1% | 23.6% |

**Reading.** In the first nine months after RTC+B, the West hub's solar-hour value was lower than in the same months of 2025, and negative prices were about twice as frequent. This supports using the weak 2024–2025 shape, not 2023, as the starting point for merchant-tail scenarios.

It does not isolate RTC+B: weather, load, fuel prices and new solar and storage all changed at the same time. The reference node TAYGETE2_ALL is not in this product. Node-level 2026 data needs the free ERCOT archive login described in `Free-Login-Source-Guide-ZH.md`.

## 4. Still blocked

The Business Wire release returned "Access Denied" again, this time in a browser (second attempt). The lender names and tax-equity investor for Taygete I therefore remain unconfirmed from a primary page. This path is closed for now.
