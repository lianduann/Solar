# Common fact pack (identical for every reviewer)

You are one of six INDEPENDENT reviewers of a 73-page English market-research report (SOLAR-001, "closure-integrated candidate edition", dated 9 Oct 2026). Work alone in this first round: you have not seen and must not look for any other reviewer's output (do not open anything under outputs/2026-10-10_Independent-Expert-and-Client-Review/ except to write your own file).

## Files (read-only; do NOT modify anything except your own output file)
- Review brief (Chinese; read §4 "适用边界" and §6 "严重性与结论标准" in full — these are binding): /home/user/Solar/outputs/2026-10-10_Independent-Review-Handoff/2026-10-10_Independent-Expert-and-Client-Review-Prompt-for-Claude.md
- PDF text with physical page markers ("===== PDF PHYSICAL PAGE n ====="): /tmp/claude-0/-home-user-Solar/20292376-c0e2-559e-b08d-17bd20d0b064/scratchpad/review/REPORT_PDF_TEXT_BY_PAGE.txt
- Markdown with line numbers ("  123| text"): /tmp/claude-0/-home-user-Solar/20292376-c0e2-559e-b08d-17bd20d0b064/scratchpad/review/REPORT_MD_WITH_LINE_NUMBERS.txt
- The PDF itself (you may view pages with the Read tool, pages param, e.g. to check a figure): /tmp/claude-0/-home-user-Solar/20292376-c0e2-559e-b08d-17bd20d0b064/scratchpad/review/2026-10-09_Closure-Integrated-Client-Edition/Integrated-Market-Research-Report-EN_Closure-Integrated.pdf
- Extracted evidence package root: /tmp/claude-0/-home-user-Solar/20292376-c0e2-559e-b08d-17bd20d0b064/scratchpad/review/2026-10-09_Closure-Integrated-Client-Edition/
  - data/ (frozen tables), figures/, closure-evidence/ (Closure-Disposition.csv, Findings-and-Replacement-Text-EN.md, Numbers-and-Claims.csv, Sources.csv, tables/, sources/ originals), scenario-versions/ (Scenario-Notes-EN.md, data/), finance-supplement/, Closure-Integration-Change-Log.*, internal/ (history only — NOT current text).

## Product boundary (summary; the brief §4 governs)
Supports: understanding links manufacturing → ERCOT → hypothetical plant; initial commercial screening; comparing cost/timing/node price/contract mechanisms; conditional NPV/LCOE/sensitivity/break-even under stated assumptions; diligence questions.
Does NOT support: real asset valuation or actual IRR; "solar is generally uneconomic"; market IRR ranges; price forecasts, profit probabilities, P50/P90; causal identification; verified tax eligibility, executable quotes/budgets, realised net settlement.
Candidate edition, not original Version 1.0. 16 evidence gaps have final dispositions (some = disclosed non-disclosure). Do NOT convert disclosed limitations into new research tasks.

## Rules
- Do not rerun regressions/models/simulations, do not fetch the web, do not add data. Simple arithmetic is fine — label it "reviewer arithmetic".
- If you cannot verify something, write "未能核查 / could not verify" — never infer it is wrong or right.
- Do not manufacture problems; "no change needed" is an acceptable conclusion for an area.
- Classify each finding: P0 (supported factual/arithmetic/unit error, text–figure conflict, core misleading claim, unreadable/leaked file — blocks the stated use), P1 (important interpretation/structure/navigation/evidence-label issue fixable with existing materials), P2 (wording/format), "Disclosed limitation" (already disclosed and within boundary), "Optional future scope".
- Each finding must have: ID (your prefix + number), PDF physical page, MD section + line number(s), short quote (≤25 words), problem, evidence (file path + location, or the report's own text), client consequence, minimal fix (concrete replacement wording when possible), changes an existing number? (Y/N), confidence (High/Med/Low), in scope? (Y/N).
- Choose your own priorities/spot checks; you need not comment on every chapter. Quality over quantity: typically 6–15 findings.
- End with an overall verdict choosing exactly one: ① reviewable/handover-ready for the stated use; ② handover-ready after the listed minimal edits; ③ specific P0 prevents handover for the stated use.

## Output
Write your full review to the file path given in your role instructions (Markdown). Then reply with a compact summary: verdict + a table of your findings (ID | severity | page | MD line | one-line problem | minimal fix). Keep the reply under ~900 words.
