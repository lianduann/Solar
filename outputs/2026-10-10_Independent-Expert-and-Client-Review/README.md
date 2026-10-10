# SOLAR-001 Independent Expert and Client Review (2026-10-10)

**Verdict: ② handover-ready for the stated use after the listed minimal edits.** All six reviewers reached this verdict independently in round 1 and kept it in round 2. No P0 was found. The verdict is not a publication authorisation and not original Version 1.0 acceptance.

## What was reviewed

- **Branch:** `codex/closure-client-review-20261010`, input commit `569a45c3f61c478c9996030afc1ee97174139b77`.
- **Handoff directory:** `outputs/2026-10-10_Independent-Review-Handoff/`.
  - The task file was read in full.
  - `Review-Input-SHA256SUMS.txt` passed.
  - Both ZIP files matched their adjacent `.sha256` files:
    - `…-Report.zip`: `39d63b18…0e7d`
    - `…-Supplement-Sources.zip`: `7ef69c8e…88ed`
  - ZIP CRC and safe-path checks passed (434 and 41 entries).
  - Both ZIPs were extracted into the same parent directory, outside the repository (session scratchpad).
  - The extracted Markdown is byte-identical to the handoff copy.
- **Reading aids**, generated without changing any input: page-marked PDF text (73 physical pages) and a line-numbered Markdown file.
- **Reviewers read:** the PDF and Markdown, the change logs, `closure-evidence/`, `scenario-versions/`, `data/` and appendices A–D. `internal/` was used only as history.

## How the review was run

Six independent agents ran as separate subagent processes. Each started with the same fact pack (`COMMON_FACT_PACK.md`, a copy is included) carrying the brief's §4 boundaries and §6 severity rules, and had no access to the others' output in round 1.

| Role | Round 1 file | Round 2 file |
|---|---|---|
| Expert A: energy economics and power markets | `Expert-A-Energy-Markets-Review-EN.md` | `round2/Expert-A-Round2.md` |
| Expert B: project finance and financial modelling | `Expert-B-Project-Finance-Review-EN.md` | `round2/Expert-B-Round2.md` |
| Expert C: econometrics and research methods | `Expert-C-Methods-Review-EN.md` | `round2/Expert-C-Round2.md` |
| Expert D: industry, trade and evidence presentation | `Expert-D-Industry-Trade-Review-EN.md` | `round2/Expert-D-Round2.md` |
| Client E: manufacturer or exporter strategy lead | `Client-E-Manufacturer-Review-ZH.md` | `round2/Client-E-Round2.md` |
| Client F: developer or ERCOT buyer, investment/procurement lead | `Client-F-Developer-Buyer-Review-ZH.md` | `round2/Client-F-Round2.md` |

**Round 2 (interaction).** The reviewers were resumed with their own context and cross-examined each other:

- B against C;
- A against D, on how the three layers connect;
- E and F against all four experts, with each expert answering the client items in its own area.

**Synthesis.** The coordinator wrote these files:

- `Cross-Review-and-Disagreements.md`: what was asked and answered, consensus, and open disputes.
- `Consolidated-Findings.csv`: 27 deduplicated items with their source roles.
- `Minimal-Revision-Plan-for-Codex.md`: exact edits with line numbers.
- `Chinese-Brief-ZH.md`: the summary for the author.

## Independence and conflict-of-interest disclosure

The coordinator (this session) wrote the earlier cloud closure supplement (commit `fe7afe5`) that the reviewed report integrates. To limit bias:

- the coordinator gave no findings or opinions to the reviewers;
- the coordinator did not add findings of its own, apart from evidence checks;
- where it settled a dispute, it did so only by checking evidence, and says so.

Reviewers' findings about text that came from that supplement were kept as written. Examples are D-01 on the "stated subsidy treatment" wording and the trade-paragraph refinements.

The six reviewers are separate model instances of the same underlying model, not human experts. Their independence lies in separate contexts and the fact that none saw another's work before round 1 was complete.

## Coordinator evidence checks

- **C-03:** recount from the frozen node file: 485 points → 400 distinct receipt series; 13 positive in 2024 → 10; the two 2025 positives are NF_BRP_RN and RHESS2_ESS1.
- **D-01:** the PVSCM module item total is 291.214 $/kWdc, including a subsidy line of −68.88.
- **D-02:** product-line margins confirmed in the four retained 2025 annual reports: Trina −1.42%, JA −4.03%, Tongwei −0.38%, LONGi industry line 0.81%.
- **Proclamation 11052 clauses 1(b) and (3):** confirmed in the official PDF and confirmed absent from the report.
- **AD/CVD:** the critical-circumstances findings appear in the Federal Register titles.
- **Export-VAT rebate:** confirmed in the LONGi FY2025 annual report, p.297.
- **Quotes:** every short quote in `Consolidated-Findings.csv` was matched verbatim against the manuscript.

## Scope kept

- No regression, model, simulation, decomposition, bootstrap or financial version was run.
- No web access was used for this review, and no data was added.
- The manuscript, inputs, frozen outputs and originals were not modified.
- Simple calculations are labelled "reviewer arithmetic" in each file.
- No login, payment, external contact or publication took place.

## Could not verify

Each review file lists what its author could not verify. Highlights:

- P07 (China's 2025 pricing reform): no retained original.
- The PVSCM workbook itself (only the frozen item-level CSV is available).
- Docket activity after 16 Sep 2026 and the ITC injury outcome.
- The NPRR817 market notice.
- The C09 assignment-date document (not in the package).

## Integrity

`File-Manifest.csv` and `SHA256SUMS.txt` cover every file in this folder. No package ZIP was created, because the folder is small, and the input packages were not copied.
