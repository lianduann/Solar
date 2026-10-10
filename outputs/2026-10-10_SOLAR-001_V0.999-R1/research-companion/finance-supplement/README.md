# SOLAR-001 Finance-Deepening Supplement

**Date:** 2026-10-09 (America/New_York). **Status:** research supplement for Codex to integrate into the panel-revision edition.

This supplement does not modify any existing report, frozen data, model register or quality status. It does not report any comparable IRR, any levered equity return or any new model NPV.

## Start here

| Need | File |
|---|---|
| Report-ready English text by FIN number | `Findings-and-Replacement-Text-EN.md` |
| What is done, partial or not done | `Research-Disposition.md`, `Gap-Disposition.csv` |
| Model inputs I recommend, and whether each may be used | `Finance-Input-Recommendations.csv` |
| Next model structure | `Model-Upgrade-Specification.md` |
| Contract identities and tax decision tree | `Contract-and-Tax-Decision-Tree.md` |

## Tables by placeholder

| FIN | Files |
|---|---|
| FIN-01 | `Comparable-Projects.csv`, `Return-Metric-Comparability.csv` |
| FIN-02 | `data/EIA-Operating-Generation-Comparables.csv` (annual), `data/EIA-Operating-Generation-Monthly-2023-2025.csv`, `data/EIA-860-2025_WestTX_PV_generators.csv` |
| FIN-03 | `Contract-Terms.csv`; `data/Node-Hub-Solar-Capture-2023-2025.csv`, `data/Node-Hub-Basis-2023-2025.csv` and `data/Node-Hub-Solar-Capture-Monthly-2023-2025.csv` (independent reproduction of the frozen panel table) |
| FIN-04 | `Tax-Eligibility-Matrix.csv`, `Basis-Crosswalk.csv` |
| FIN-05 | `Cost-Coverage-Crosswalk.csv` |
| FIN-06 | `Entity-Node-Mapping.csv` |
| FIN-07 | `Currency-Timing-Crosswalk.csv` |
| FIN-08 | `Regime-Evidence.csv`, `data/ERCOT-Battery-Capacity-by-Vintage-EIA860-2025.csv` |
| FIN-09 | `Supplier-Liquidity.csv` (not done) |
| FIN-10 | `Debt-and-Waterfall-Inputs.csv` |
| FIN-11 | `Settlement-and-Net-Receipts.csv` |

**Field-level evidence:** `Project-Finance-Input-Evidence.csv` gives the URL, retrieval time, SHA-256 and location for each field. `Sources.csv` and `Source-Catalog.csv` are the same catalog under the two names the briefs use.

**Records:** `Access-Blockers.md`, `Research-Log.md`, `Verification.json`, `MANIFEST.csv`, `SHA256SUMS.txt`, `Chinese-Brief-ZH.md`.

## Reproduction

The raw sources are under `Data/raw/2026-10-09_Finance-Deepening/` (about 290 MB; one Comptroller agreement PDF alone is 124 MB), together with the earlier retained archives listed in `Sources.csv`. They are **not** inside the ZIP. The ZIP holds this folder plus the scripts.

**Environment:** Python 3.12, pandas, numpy, openpyxl; `pdftotext` and `pdftoppm` were used only for reading PDFs.

Run from the project root:

```bash
python3 Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/02_eia_operating_generation.py --eia860 Data/raw/2026-10-09_Finance-Deepening/EIA/eia8602025.zip --eia923 Data/raw/2026-10-09_Finance-Deepening/EIA/f923_2023.zip Data/raw/2026-08-25/US/EIA/2024_EIA-923_final.zip Data/raw/2026-10-09_Finance-Deepening/EIA/f923_2025.zip --out Deliverables/2026-10-09_Finance-Deepening-Supplement/data
```

```bash
python3 Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/03_ercot_battery_vintage.py Data/raw/2026-10-09_Finance-Deepening/EIA/eia8602025.zip Deliverables/2026-10-09_Finance-Deepening-Supplement/data/ERCOT-Battery-Capacity-by-Vintage-EIA860-2025.csv
```

```bash
python3 Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/04_extract_ch313_773.py Data/raw/2026-10-09_Finance-Deepening/comparables Deliverables/2026-10-09_Finance-Deepening-Supplement/data/Ch313-Form773-2023-Extract.csv
```

```bash
python3 Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/05_finance_arithmetic.py --panel Deliverables/2026-10-09_Panel-Revision-Client-Edition --supp Deliverables/2026-10-09_Finance-Deepening-Supplement
```

```bash
python3 Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/06_build_catalog.py . Deliverables/2026-10-09_Finance-Deepening-Supplement
```

```bash
python3 Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/07_verify_clean_rerun.py . /tmp/solar001_clean_rerun
```

Script `01_node_hub_capture.py` produced the node and hub tables from the retained NP6-905-CD archives. Under the updated brief it is not re-run. `07` checks its delivered outputs against the frozen panel table instead: the maximum absolute difference is 0.004 USD/MWh, which comes from slightly different common-interval counts.

`fetch.sh` is the download helper that wrote each `fetch_receipts.csv`. A ZIP that verifies only proves file integrity. It does not validate the sources.

## Evidence labels

- `direct` means primary documents: statute, court record, Comptroller filing, ERCOT or EIA files, lender release.
- `public reference` means national-laboratory benchmarks or parameter files.
- `secondary` means trade press. It is used only where marked.
- `derived` means my arithmetic, which is reproducible in `data/Finance-Arithmetic-Checks.csv`.
- `analysis assumption` means a frozen-model setting.

`unknown` is never treated as zero.
