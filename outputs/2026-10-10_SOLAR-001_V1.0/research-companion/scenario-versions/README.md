# SOLAR-001 Finance Scenario Versions

**Date:** 2026-10-09 (America/New_York). I built these versions after the author authorised them on 2026-10-09: an OCC credit-base scenario, a VPPA route and a CPI-harmonised scenario.

They sit beside the frozen panel edition and the 2026-10-09 finance-deepening supplement. Neither of those is modified.

## Files

| File | Content |
|---|---|
| `Scenario-Notes-EN.md` | Method, labels (observed / reference / assumed / missing), results and how they differ from the frozen outputs |
| `data/Credit-Base-Scenarios.csv` | A0 original (OCC+GCC, kept for tracking); A1 OCC-only (approved assumption); A2 scope check. Variants: timing, transfer price and PWA. Rates: 4.27 / 6 / 8% |
| `data/VPPA-Route-Scenarios.csv` | Node sale plus HB_WEST swap, H = G, strike 40 or 49, tenor 10 or 15 years, two dispatch rules, two negative-hub clauses, five price paths, three rates |
| `data/VPPA-Breakeven-Strikes.csv` | Break-even nominal flat strike for each combination |
| `data/CPI-Harmonised-Scenario.csv` | Frozen and CPI-restated NPV side by side, for the reference points and the 485-node strict sample |
| `data/Node-Hub-Intervals-2023-2025.csv.gz` | 15-minute TAYGETE2_ALL and HB_WEST prices with same-year site energy. The 2025 node price and energy are identical to the frozen `interval_energy_price_2025.csv` |
| `data/scenario_build_log.json` | Reproduction checks: frozen K, node-route NPV, panel credit, tenor-0 VPPA, CPI annuity |
| `Followup-Evidence-No-Login.md`, `Followup-Sources.csv`, `data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv` | No-login follow-up: Texas statutes, IMM 2025 report, HB_WEST Jan-Sep 2026 context (script 10) |
| `Free-Login-Source-Guide-ZH.md` | Free sources that need the author's own login: links, purpose, files and fields, steps and stop conditions |
| `Verification.json`, `MANIFEST.csv`, `SHA256SUMS.txt` | Clean re-run and integrity records |

## Reproduce from the project root

```bash
python3 -I Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/08_extract_node_hub_intervals.py . Deliverables/2026-10-09_Finance-Scenario-Versions/data/Node-Hub-Intervals-2023-2025.csv.gz
```

```bash
python3 Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/09_finance_scenarios.py . Deliverables/2026-10-09_Finance-Scenario-Versions/data
```

Inputs:

- the retained NP6-905-CD archives;
- the reused site-energy weights in `Data/raw/2026-10-09_Finance-Deepening/solar-weights-reused/`;
- the frozen panel-edition data, which is read-only.

No regression, resampling or weather simulation is run.
