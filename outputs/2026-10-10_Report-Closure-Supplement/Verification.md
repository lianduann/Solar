# Verification

| Check | Result |
|---|---|
| Input package hash check (`verify_handoff.py`) | PASS, errors = 0 |
| Uploaded brief identical to the copy inside the ZIP | PASS (`diff` empty) |
| New numbers traced to package files (`scripts/verify_closure.py`, 16 checks) | PASS; see `verification_results.json` |
| 16 IDs present, each with a final disposition (none pending) and a Findings section | PASS |
| Statute, opinion, Notice 2026-15 and PUCT rule wording and pages | Checked manually with pdftotext against package PDFs |
| Loss-stack total 14.0757% recomputed from listed components | PASS (14.0757) |
| Credential scan of outputs (key, token, bearer, password patterns) | PASS, no hits |
| ZIP path safety and CRC test | PASS (`unzip -t`; no absolute or `..` paths). The ZIP's own SHA-256 is in `../2026-10-10_Report-Closure-Supplement.zip.sha256`, because a file cannot contain its own hash |

## Not performed, and why

- Re-download or hash of any official original: the hosts were blocked by the environment egress policy.
- Primary docket check for the appeal or stay: PACER and CourtListener were not reachable.
- Annex I/II HTS verification: the annex text was not in the package and the host was blocked.
- Decoding of NSRDB fill-flag codes: the documentation was not reachable.
- No model, regression, weather simulation or financial version was run (by design).
