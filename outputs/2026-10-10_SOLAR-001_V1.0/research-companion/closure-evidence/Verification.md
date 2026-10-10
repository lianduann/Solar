# Verification

| Check | Result |
|---|---|
| Input package hash check (`verify_handoff.py`) | PASS, errors = 0 |
| Uploaded brief identical to the copy inside the ZIP | PASS (`diff` empty) |
| New numbers traced to package files and round-2 originals (`scripts/verify_closure.py`, 23 checks) | PASS; see `verification_results.json` |
| FIN-09: each of 145 values found verbatim in the saved filing text (`build_fin09_table.py`) | PASS (0 not found) |
| JinkoSolar XBRL `ProductWarrantyAccrual` checked against filing note | Tag holds the estimate reversal, not the balance; the balance (1,832,203k) is taken from the filing note |
| Proclamation 11052 annexes | Read from page images of the official PDF (pp.51982–51987); HTS lines transcribed manually |
| 16 IDs present, each with a final disposition (none pending) and a Findings section | PASS |
| Statute, opinion, Notice 2026-15 and PUCT rule wording and pages | Checked manually with pdftotext against package PDFs |
| Loss-stack total 14.0757% recomputed from listed components | PASS (14.0757) |
| Credential scan of outputs (key, token, bearer, password patterns) | PASS, no hits |
| ZIP path safety and CRC test | PASS (`unzip -t`; no absolute or `..` paths). The ZIP's own SHA-256 is in `../2026-10-10_Report-Closure-Supplement.zip.sha256`, because a file cannot contain its own hash |

## Not performed, and why

- Round 1 could not download originals (egress policy). Round 2 did; hashes are in `SHA256SUMS.txt` and `Sources.csv`.
- PACER (account required) not used; the public RECAP copy may be incomplete.
- usitc.gov and static.longi.com (site 403) and nsrdb.nrel.gov (502) not retrieved. Business Wire is covered by an author-supplied screenshot, read visually. The IMM report was downloaded in round 3; SHA-256 8febb03a…c6db equals the prior-round receipt.
- Decoding of NSRDB fill-flag codes: the documentation was not reachable.
- No model, regression, weather simulation or financial version was run (by design).
