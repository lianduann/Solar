# Existing Work Reused (no recomputation)

| Prior output (package path under `project/Deliverables/`) | Used for | How used |
|---|---|---|
| `2026-10-09_Finance-Scenario-Versions/data/CPI-Harmonised-Scenario.csv`, `scenario_build_log.json` | FIN-07 | Values quoted; calendar basis checked against `A_3x3_summary.csv` and `C_tail_results_by_node_year.csv`. Not rerun |
| `2026-10-09_Finance-Scenario-Versions/data/VPPA-Breakeven-Strikes.csv`, `VPPA-Route-Scenarios.csv`, `Scenario-Notes-EN.md` | FIN-03 | Min/max of existing rows and one ratio (tail share). Not rerun |
| `2026-10-09_Finance-Scenario-Versions/data/Credit-Base-Scenarios.csv` | FIN-04 | A1 variants quoted |
| `2026-10-09_Finance-Scenario-Versions/data/HB_WEST-2026-JanSep-Post-RTCB-Context.csv`, `Followup-Evidence-No-Login.md` | FIN-08, FIN-02, FIN-05 | Jan–Sep rows; IMM quotations; Texas statute excerpts (inherited) |
| `2026-10-09_ERCOT-API-2026-Price-Data/data/*` (QA, coverage, gap tables) | FIN-08, FIN-11 | Recounted into `tables/FIN-08_2026-Price-Coverage-Summary.csv`. No API call or rebuild |
| `2026-10-09_Finance-Deepening-Supplement/*.csv` (Comparable-Projects, Contract-Terms, Debt-and-Waterfall-Inputs, Entity-Node-Mapping, Cost-Coverage-Crosswalk, Settlement-and-Net-Receipts, Regime-Evidence, Tax-Eligibility-Matrix) | FIN-01/02/03/05/06/10/11 | Read and condensed into client text |
| `2026-10-09_Finance-Integrated-Client-Edition/sources/finance/*` (P.L. 119-21, D.D.C. opinion, Notice 2026-15, 16 TAC §25.195, Form 772) | FIN-04, FIN-05 | Re-read with pdftotext; page-cited |
| `2026-10-09_Finance-Integrated-Client-Edition/support/Policy-and-Cost-Web-Checks.json`, `Official-Web-Extracts.json` | B-02, FIN-08 | Prior-round rendered official extracts |
| `.../data/weather_qa.json`, `data/empirical/site_energy_qa.csv`, `data/scenario_input_register.csv` | B-04 | Counts and register rows |
| `.../data/supplement/C/C_batch_zero_*.csv` | B-03 | Category sums |

Not rerun: the 2026 API download, the EIA extraction, the weather simulation, the regressions and resampling, and the finance scenario scripts 08–10.

Round 2 added original downloads only (no recomputation). FIN-09 arithmetic is limited to current assets minus current liabilities, and to unit scaling for display.
