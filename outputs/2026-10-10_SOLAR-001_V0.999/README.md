> This directory holds the V0.999 deliverables: the complete package `2026-10-10_SOLAR-001_V0.999.zip` (with its `.sha256`), the final PDF, the English Markdown source, the Chinese closing note, the change log and the page inspection log. Paths below refer to the package inside the ZIP. `2026-10-10_SOLAR-001_V0.999_Delivery-Verification.json` records the ZIP CRC test, path safety, independent extraction and the rebuild from the extracted copy.

# SOLAR-001 V0.999 — final edit, design and PDF production

**Report:** *From China's Solar Supply Chain to U.S. Power Markets: Industry Restructuring, Value Capture in ERCOT, and Utility-Scale Solar Economics*
**Edition:** Version 0.999, 10 October 2026 — editorial and production release
**Final PDF:** `SOLAR-001_V0.999_Integrated-Market-Research-Report-EN.pdf` (85 pages, US Letter)

V0.999 completes editing and production of the reviewed research candidate. It is **not** an acceptance of the original
project's Version 1.0. Estimates, model inputs, samples, results and evidence boundaries are those of the input
candidate; no model was rerun and no new scenario or research was added.

## Input

| Item | Value |
|---|---|
| Repository / branch | `lianduann/Solar`, `codex/closure-client-review-20261010` |
| Commit | `1a3c64119729aabce2640ae51e5160afed089845` |
| Directory | `outputs/2026-10-10_Reviewed-Client-Research-Candidate/` |
| Report ZIP SHA-256 | `f5c36e121fbe4c4b54ab8009074c8de7a5585f05a71fcacdb3baffb1497960c4` (matches its `.sha256`) |
| Supplement ZIP SHA-256 | `838b7707dbbfab8162908df209e7aeb3e31203d42f50500271000ff384d01307` (matches its `.sha256`) |
| Input Markdown (copy) | `baseline/Integrated-Market-Research-Report-EN_Reviewed-Candidate.md` |

Both ZIPs passed `unzip -t` and were extracted into one parent directory before editing.

## Contents

| Path | What it is |
|---|---|
| `SOLAR-001_V0.999_Integrated-Market-Research-Report-EN.pdf` | Final PDF: clickable contents, 111 bookmarks, page numbers, linked cross-references, external links, links to accompanying research files |
| `V0.999-Closing-Note-ZH.md` | Short closing note (Chinese) |
| `source/SOLAR-001_V0.999_Report-EN.md` | English Markdown source (single content source for the PDF) |
| `assets/report.css` | Editable layout source: page setup, type, colors, cover/back cover, openers, key-finding, data and limits styles, tables, figures |
| `build/build_report.py` | Markdown → designed HTML → PDF (WeasyPrint); cover and back-cover art are drawn here as SVG |
| `assets/fonts/` | Embedded fonts with licenses: Source Serif 4 (OFL), Inter (OFL), DejaVu Sans Mono |
| `figures/` | 34 vector exhibits (SVG) and 200 dpi PNG previews; 29 appear in the report, 5 are produced by the upstream figure registry but not placed (as in the input) |
| `figures/Figure-Plot-Data-V0999.json`, `Figure-Map.json` | Plotted values of every exhibit; map from input figure files to V0.999 exhibits |
| `build/render_figures.py` | Redraws the exhibits with the unchanged upstream plotting code in `build/upstream/` (presentation settings only) |
| `build/build_all.py` | **Rebuild entry point** (figures → figure-data check → PDF → numeric and structural checks) |
| `build/check_figures.py`, `check_numbers.py`, `check_report.py`, `render_pages.py` | Verification scripts |
| `build/verify_rebuild.py` | Rebuilds into an empty directory and compares pages, bookmarks and figures with the delivered files |
| `build/make_manifest.py` | Writes `MANIFEST.csv` and `SHA256SUMS.txt` |
| `data/` | Data tables used by the figures (byte-identical copy of the input `data/`) |
| `research-companion/` | Unchanged copies of the input's closure evidence, finance supplement, source copies and separately versioned scenarios; PDF file links point here |
| `records/` | Change log, source diff, page inspection log and images, check results, build log |
| `MANIFEST.csv`, `SHA256SUMS.txt` | File list with sizes and SHA-256 |

## Rebuild

Requirements: Python 3.10+ with `weasyprint` (60 or later; built with 70.0), `matplotlib` (3.11.2), `numpy`, `pandas`,
`pymupdf`, `pillow`. Fonts are bundled; no network access, login or paid service is needed.

```bash
python3 -m pip install weasyprint matplotlib numpy pandas pymupdf pillow
python3 build/build_all.py                          # rebuild in place
python3 build/build_all.py --output-dir /tmp/v0999  # rebuild into an empty directory
```

To repeat the empty-directory comparison: `python3 build/verify_rebuild.py /tmp/v0999-check`. Check file integrity with
`sha256sum -c SHA256SUMS.txt`.

Exit status 0 means every step exited 0 and every check reported PASS. The log is written to
`<output-dir>/records/Build-Log.json`. Links to accompanying research files are relative to the package root, so they
resolve from the PDF in the package root. To render page images for inspection:
`python3 build/render_pages.py <pdf> <out-dir> --dpi 100`.

## Verification records (`records/`)

| File | Result |
|---|---|
| `Number-Preservation-Check.json` | PASS — every number in the V0.999 source occurs in the input; only new token is the edition number 0.999; two input tokens no longer appear, both explained (a duplicated date range and the old section number 6.6) |
| `Figure-Data-Check.json` | Plotted data of all exhibits with an upstream snapshot are identical; the five panel exhibits have no upstream snapshot and are drawn by unchanged code from byte-identical tables |
| `Report-Structure-Check.json` | PASS — figure and table numbering in order, every reference resolves, required qualifiers present, 625 internal links resolve, 13 file links resolve, 65 external links (45 unique, all https), contents numbers equal bookmark pages |
| `Rebuild-Verification.json` | Rebuild from an empty directory: commands, exit status, page count and text comparison with the delivered PDF |
| `Page-Inspection-Log.md`, `page-inspection/` | Every page rendered and inspected; defects found and fixed; page images and contact sheets |
| `Change-Log.md` / `.csv` | Location, issue, change, meaning affected (52 entries) |
| `Source-Diff_Input-to-V0.999.diff` | Unified diff of input Markdown → V0.999 source |
| `Build-Log.json` | Last in-place build: commands and exit statuses |

## Boundaries carried unchanged

The following qualifiers stay next to the results they qualify: Figure 8-4 left panel, thin dotted lines with crosses
are medians; $26.4/MWh is modeled gross energy value, not net revenue; the 30-year node fixed price and the 10–15-year
hub hedge are separate calculation versions; pre-tax NPV plus the illustrative credit is not a complete after-tax
valuation; historical scenarios are not ERCOT market-wide conclusions; industry-line and product-line margins are not
a ranking; the 2026 fixed-profile price diagnostic is not a realized 2026 capture price.
