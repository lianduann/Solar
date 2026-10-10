# SOLAR-001 V0.999-R1 — change log (from V0.999)

R1 is a usability revision of V0.999, built at Lian's request of 10 October 2026 ("看你推荐的来吧"). It is not the
original project's Version 1.0 acceptance. V0.999 files are untouched; its records are kept in `records/V0.999-inherited/`.

## Design

| # | Location | Change | Meaning affected |
|---|---|---|---|
| D1 | Palette (layout and all 35 exhibits) | Amber/yellow replaced by navy + brick (#B4523A); slate, sage and teal for categories; diverging scale brick ↔ teal | No |
| D2 | Type | Body stays Source Serif 4; headings, tables and charts use Liberation Sans (Helvetica-metric, OFL). TeX Gyre Heros was intended but could not be downloaded from this environment | No |
| D3 | Page | Wider margins (1.15 in sides), more space under the running header, body 10.2 pt / 1.55, larger table type and padding | No |
| D4 | Cover | Italic tagline removed | No |
| D5 | Exhibits | Four same-hue collisions after recoloring fixed (mean node-price line, Figure 10-2 cost bars, net-load panel line, Houston zone) | No |
| D6 | R1 boxes | R1 additions in a brick-topped box | No |

## Structure and wording

| # | Location | Change | Meaning affected |
|---|---|---|---|
| S1 | About | Edition paragraph rewritten for R1; Table 0-1 updated (new storage row; new section numbers) | No |
| S2 | 1.1 | Finding 8 added: 2025 ERCOT offer index, 2026 West hub diagnostic, Taygete II foreclosure, credit deadline (all existing report facts except the offer index) | Adds context |
| S3 | 1.3 (new) | Figure 1-1 price ladder and Table 1-2 break-even master table; former 1.3 is 1.4 | No new estimate except R1 rows |
| S4 | 2.5 | Five hypotheses → two tested hypotheses (H1, H2) and three open questions (Q1–Q3) | Labels only |
| S5 | 3.2, 3.4 | One paragraph removed (no numbers), two paragraphs merged | No |
| S6 | 10.6 | IRR root list replaced by pointer to B.2 (list unchanged there) | No |
| S7 | 10.8 | Court-docket paragraph moved to Appendix C; one-sentence summary left | No |
| S8 | 11.5–11.7 | Crossed-year matrix, accounting decomposition and resampling moved to Appendix B.6–B.8; new 11.5 summary; 2026 evidence split into 11.7; Figures 11-3/11-4/11-6 → B-2/B-3/B-4, 11-5 → 11-3; Tables 11-2 → B-3, 11-3 → 11-2 | No |
| S9 | Ch. 12 | Retitled "Research Hypotheses: What the Evidence Supports and What Remains Open"; H2/H4/H5 folded into 12.3 open questions; Table 12-1 → 12-2 with Q rows | Labels only; Q3 status now "Screened (R1)" |
| S10 | Ch. 13 | "Bottom line by reader" lead; buyers moved before research teams (13.3/13.4); two rows added to Table 13-3 | Adds R1 figures |
| S11 | Appendix C | Court-docket paragraph (from 10.8); storage scope note now points to the R1 screen | No |
| S12 | A.3, B.9 (new) | Sources (M01–M05) and methods for R1 additions | — |

## R1 additions (labeled R1; arithmetic only, no model rerun)

| # | Location | Content | Source |
|---|---|---|---|
| R1-1 | 10.8 box, Table 1-2 | Production-credit (45Y) illustration: PV $57.80m; break-even $45.61/MWh (transferred at 0.90: $47.65; base rate: $61.90) | `build/r1_calcs.py`, `data/r1/PTC-Illustration.csv`; IRS FR Doc. 2025-16249 |
| R1-2 | 10.10, Table 10-7 | Public market reference points: LevelTen ERCOT P25 (2025 avg $44.6), LevelTen/Trio 2024, North America P25, IMM 2025, Lazard 2026 | `data/r1/Market-References.csv`; LBNL data file, IMM, Lazard, press |
| R1-3 | 12.4, Table 12-1 | Storage screen: perfect-foresight 4-hour arbitrage bound vs Lazard cost range | `data/r1/Storage-Screen.csv`, `Storage-Cost.csv` |

Every new number is registered with its source in `records/R1-New-Numbers.csv`; `build/check_numbers.py` fails on any
unregistered new number or unexplained dropped number.
