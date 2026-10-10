# SOLAR-001 Report Closure Supplement (2026-10-10)

This supplement closes the 16 fixed items (FIN-01 to FIN-11, B-01 to B-05) of the SOLAR-001 report. Its contents are dispositions, client-ready English replacement text, source records and small tables. It does not modify the uploaded handoff package, the manuscript, any model or any acceptance record.

Execution: cloud container, 2026-10-10 UTC (evening of 2026-10-09 America/New_York). Round 1: official hosts were blocked by the environment's egress policy, so evidence came from package originals and prior-round extracts. Round 2 (03:15–03:35 UTC), after the author opened network access, downloaded official originals (SEC, cninfo, Federal Register, CourtListener RECAP, ERCOT, ATB) into `sources/`. Round 3: IMM 2025 report downloaded, with a hash identical to the prior record, and a Business Wire screenshot supplied by the author. Web-search results remain leads only. See `Search-and-Access-Log.csv` (S-* and R2-* rows).

## Files

| File | Content |
|---|---|
| `Chinese-Brief-ZH.md` | 中文简报：新增、影响、缺口、作者事项、停止声明 |
| `Closure-Disposition.csv` | 16 rows, with a final disposition for each |
| `Findings-and-Replacement-Text-EN.md` | Anchor, action and English text for each ID |
| `Numbers-and-Claims.csv` | 38 numbers and legal facts, with source location and allowed scope |
| `Sources.csv` | Package sources (with SHA-256) and search leads (no local file) |
| `Search-and-Access-Log.csv` | Access attempts and searches, with stop reasons |
| `tables/` | `FIN-08_2026-Price-Coverage-Summary.csv`, `B-03_Batch-Zero-Figure-vs-Narrative.csv`, `B-04_Weather-Fill-Flag-Counts.csv`, `FIN-09_Supplier-Liquidity.csv` (145 verified values), `FIN-09_SEC-XBRL-Liquidity-Long.csv` (raw XBRL pull; see Sources note on tags) |
| `sources/` | Round-2 originals: `sec/`, `cninfo/`, `trade/`, `legal/`, `other/` (with derived `.txt` text for search) |
| `scripts/` | `build_closure_tables.py`, `extract_sec_liquidity.py`, `build_fin09_table.py` (build tables/) and `verify_closure.py` (checks) |
| `Existing-Work-Reuse.md`, `Verification.md`, `verification_results.json`, `CHECKPOINT.md` | Reuse record, checks, status |
| `File-Manifest.csv`, `SHA256SUMS.txt` | Integrity records |

## Commands actually run in the cloud (relative to this folder)

`HANDOFF_ROOT` is the unzipped `2026-10-09_Report-Closure-Cloud-Handoff/`, which the session placed in its scratchpad.

```
python3 -I verify_handoff.py                       # in HANDOFF_ROOT: Input hash check PASS errors=0
python3 -I scripts/build_closure_tables.py "$HANDOFF_ROOT" tables
python3 -I scripts/extract_sec_liquidity.py sources/sec tables/FIN-09_SEC-XBRL-Liquidity-Long.csv
python3 -I scripts/build_fin09_table.py
python3 -I scripts/verify_closure.py "$HANDOFF_ROOT" .
```

## Integration actions for local Codex (only these)

1. Apply the REPLACE/INSERT/RETAIN actions in `Findings-and-Replacement-Text-EN.md` to a new manuscript version.
2. FIN-03 and FIN-10 inserts are verified against the author-supplied Business Wire screenshot (round 3). Keep the source label "developer release".
3. Use the round-2 B-02 wording (full clauses 1–5 and Annexes); the round-1 'conflict' note is withdrawn.
4. Insert Table 4-3 (FIN-09) and LONGi FY2025 rows (B-01) with their footnotes.
5. Keep the FIN-07 calendar-basis warning: do not place the CPI-file 2024 median beside Table 10-4.
6. Rebuild the PDF and the package checks locally. Keep the "candidate edition" label, because the original acceptance criteria are not all met.
