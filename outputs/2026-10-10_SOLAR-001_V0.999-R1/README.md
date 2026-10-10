# SOLAR-001 V0.999-R1 — usability revision of V0.999

**Report:** *From China's Solar Supply Chain to U.S. Power Markets: Industry Restructuring, Value Capture in ERCOT, and Utility-Scale Solar Economics*
**Edition:** Version 0.999-R1, 10 October 2026
**PDF:** `SOLAR-001_V0.999-R1_Integrated-Market-Research-Report-EN.pdf` (106 pages, US Letter)

R1 revises the design and structure of V0.999 and adds three clearly labeled R1 items. It is **not** an acceptance of
the original project's Version 1.0. V0.999's estimates, model inputs, samples and evidence boundaries are unchanged;
no upstream model was rerun. V0.999 itself (branch `claude/solar-001-v0999-production-20261010`) is not modified.

## What changed

- **Design:** navy + brick palette (no amber/yellow) in the layout and all 35 exhibits; serif body with a Helvetica-metric
  sans (Liberation Sans) for headings, tables and charts; wider margins and looser spacing; cover tagline removed.
- **Structure:** one-page break-even comparison in Chapter 1 (Figure 1-1, Table 1-2); finding 8 on recent market
  signals; Chapter 12 reduced to two tested hypotheses plus three open questions; Chapter 13 opens with a bottom line
  by reader; technical robustness detail moved from Chapter 11 to Appendix B.6–B.8.
- **R1 additions** (arithmetic on existing outputs and public sources, `build/r1_calcs.py`):
  production-credit illustration (10.8), public market reference points (10.10), storage screen (12.4).

Details: `records/Change-Log.md`; full text diff: `records/Source-Diff_V0.999-to-R1.diff`.

## Contents

| Path | What it is |
|---|---|
| `SOLAR-001_V0.999-R1_…-EN.pdf` | Final PDF: clickable contents, 115 bookmarks, linked cross-references and sources |
| `source/SOLAR-001_V0.999-R1_Report-EN.md` | English Markdown source (single content source) |
| `baseline/SOLAR-001_V0.999_Report-EN.md` | V0.999 source, the baseline for the numeric check |
| `assets/report.css`, `assets/fonts/` | Layout and embedded fonts (Source Serif 4, Liberation Sans, DejaVu Sans Mono; licenses included) |
| `build/` | Build and check scripts; `build/upstream/` holds the unchanged upstream plotting code |
| `figures/` | 35 SVG exhibits with PNG previews, `Figure-Plot-Data.json`, `Figure-Map.json` |
| `data/` | V0.999 data tables (unchanged) plus `data/r1/` (R1 inputs and outputs) |
| `research-companion/` | Unchanged accompanying research files; PDF file links point here |
| `records/` | Checks, build log, rebuild verification, change log, page inspection, `R1-New-Numbers.csv`; V0.999 records in `V0.999-inherited/` |

## Rebuild

Requirements: Python 3.10+ with `weasyprint` (built with 70.0), `matplotlib`, `numpy`, `pandas`, `pymupdf`, `pillow`.
No network access, login or paid service is needed.

```bash
python3 build/build_all.py                          # rebuild in place
python3 build/build_all.py --output-dir /tmp/r1     # rebuild into an empty directory
python3 build/verify_rebuild.py /tmp/r1-check       # rebuild and compare with the delivered PDF
sha256sum -c SHA256SUMS.txt
```

## Verification (`records/`)

| File | Result |
|---|---|
| `Number-Preservation-Check.json` | PASS — every number is in V0.999 or registered with its source in `R1-New-Numbers.csv` (47 registered); three dropped tokens are old section numbers |
| `Figure-Data-Check.json` | Plotted data of all upstream exhibits identical to the upstream snapshots; the R1 price ladder uses Table 1-2 values |
| `Report-Structure-Check.json` | PASS — numbering, references, required qualifiers (including three for R1), internal/external/file links, contents pages = bookmark pages |
| `Rebuild-Verification.json` | PASS — empty-directory rebuild: same 106 pages, identical text and bookmarks, 35/35 identical SVGs |
| `Page-Inspection-Log.md` | Every page inspected; contact sheets in `page-inspection/sheets/` |

## Font note

TeX Gyre Heros (the free Helvetica clone that was planned) could not be downloaded in this environment. Liberation Sans
has Helvetica/Arial metrics and is used instead. To switch, place the four `texgyreheros-*.otf` files in
`assets/fonts/`, change the four `Sans R` `@font-face` sources in `assets/report.css` and the font path in
`build/render_figures.py`, then rebuild.
