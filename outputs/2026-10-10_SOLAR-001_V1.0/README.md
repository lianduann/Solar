# SOLAR-001 Version 1.0 — delivery edition

**Report:** *From China's Solar Supply Chain to U.S. Power Markets: Industry Restructuring, Value Capture in ERCOT, and Utility-Scale Solar Economics*
**Edition:** Version 1.0, 10 October 2026
**PDF:** `SOLAR-001_V1.0_Integrated-Market-Research-Report-EN.pdf` (106 pages, US Letter)

Version 1.0 is the formal delivery edition for the uses stated on the report's "About" page. It is accepted under the
**delivery-edition standard** chosen by the business owner on 10 October 2026 and recorded in
`records/V1.0-Acceptance-Record.md`. That record also lists the original ten Version 1.0 criteria with their current
status; they are not all met (Criterion 6 cannot be closed for a hypothetical project), and this edition does not claim
otherwise.

## Lineage

| Step | Edition | What it did |
|---|---|---|
| 1 | Reviewed research candidate (commit 1a3c641) | Independent expert and client review; minimal edits applied |
| 2 | V0.999 | Editing and production (85 pages) |
| 3 | V0.999-R1 | Design (navy + brick), structure (Chapter 1 price ladder and break-even table; Chapter 12 as two hypotheses + three open questions), and three supplementary calculations (production credit, market references, storage screen) |
| 4 | **V1.0** | Version labels, removal of internal revision tags, final client-reader review (25 findings applied), acceptance record |

No upstream model was rerun at any step. Every number is either in the reviewed edition or registered with its source
in `records/R1-New-Numbers.csv`.

## Contents

| Path | What it is |
|---|---|
| `SOLAR-001_V1.0_…-EN.pdf` | Final PDF: clickable contents, 115 bookmarks, linked cross-references and sources |
| `V1.0-Closing-Note-ZH.md` | Closing note (Chinese) |
| `source/SOLAR-001_V1.0_Report-EN.md` | English Markdown source (single content source) |
| `baseline/` | V0.999 source (numeric baseline) and V0.999-R1 source (diff baseline) |
| `assets/report.css`, `assets/fonts/` | Layout and embedded fonts (Source Serif 4, Liberation Sans, DejaVu Sans Mono; licenses included) |
| `build/` | Build and check scripts; `build/upstream/` holds the unchanged upstream plotting code |
| `figures/` | 35 SVG exhibits with PNG previews, `Figure-Plot-Data.json`, `Figure-Map.json` |
| `data/` | Data tables (unchanged from the reviewed edition) plus `data/r1/` (supplementary-calculation inputs and outputs) |
| `research-companion/` | Unchanged accompanying research files; PDF file links point here |
| `records/` | Acceptance record, change log, checks, build log, rebuild verification, page inspection, number registry; earlier records in `R1-inherited/` |

## Rebuild

Requirements: Python 3.10+ with `weasyprint` (built with 70.0), `matplotlib`, `numpy`, `pandas`, `pymupdf`, `pillow`.
No network access, login or paid service is needed.

```bash
python3 build/build_all.py                          # rebuild in place
python3 build/build_all.py --output-dir /tmp/v10    # rebuild into an empty directory
python3 build/verify_rebuild.py /tmp/v10-check      # rebuild and compare with the delivered PDF
sha256sum -c SHA256SUMS.txt
```

## Verification (`records/`)

| File | Result |
|---|---|
| `V1.0-Acceptance-Record.md` | Delivery-edition criteria D1–D10 all met; original ten criteria listed with status |
| `Number-Preservation-Check.json` | PASS — 47 registered new tokens; four dropped tokens are the old edition number and old section numbers |
| `Figure-Data-Check.json` | All 34 upstream exhibits identical to the upstream snapshots; Figure 1-1 uses Table 1-2 values |
| `Report-Structure-Check.json` | PASS — numbering, references, 12 required qualifiers, links, contents = bookmarks |
| `Rebuild-Verification.json` | PASS — empty-directory rebuild: 106 pages, identical text and bookmarks, 35/35 identical SVGs |
| `Page-Inspection-Log.md` | Every page inspected; contact sheets in `page-inspection/sheets/` |
| `Change-Log.md`, `Source-Diff_R1-to-V1.0.diff` | What changed from V0.999-R1 |

## Font note

Headings, tables and charts use Liberation Sans (Helvetica/Arial metrics, OFL). To switch to TeX Gyre Heros, place the
four `texgyreheros-*.otf` files in `assets/fonts/`, change the four `Sans R` `@font-face` sources in
`assets/report.css` and the font path in `build/render_figures.py`, then rebuild.
