# SOLAR-001 Version 1.0 — change log (from V0.999-R1)

Version 1.0 is the delivery edition, built from V0.999-R1 at Lian's request of 10 October 2026 ("推进到v1.0正式交付版")
under the delivery-edition standard recorded in `V1.0-Acceptance-Record.md`. R1 and V0.999 are untouched; R1 records are
in `records/R1-inherited/`, V0.999 records in `records/R1-inherited/V0.999-inherited/`.

No number changed. No model was rerun. The full text diff is `Source-Diff_R1-to-V1.0.diff`.

## Edition and labels

| # | Location | Change |
|---|---|---|
| E1 | Front matter, cover, running header, back cover, PDF metadata | Version 1.0 |
| E2 | About — Edition | Rewritten as the delivery edition; the three calculations added in R1 are described as supplementary calculations, with pointers to A.3 and B.9 |
| E3 | 1.1, Table 1-2, 10.8 box, 10.10, 12.3, 12.4, Table 12-2, A.3, B.9, Appendix C | Internal "R1" revision tags removed; the 10.8 box is titled "Illustration — production credit" |

## Final client-reader review (25 findings, all applied)

| # | Location | Finding | Change |
|---|---|---|---|
| C1 | 1.1 finding 4 | Export-VAT sentence cited only Section 5.7 | Citation now `[P01; P08; Sections 4.4 and 5.7; …]` |
| C2 | 1.1 finding 8 | "passed to its senior lender through foreclosure" overstated 8.1 and Appendix C | "was sold in a foreclosure purchase initiated by its senior lender" |
| C3 | Ch. 13 lead; Table 12-2 Q3 | Storage statement lacked the reference-node 2025 scope (2023 hub bound clears the cost range) | "at the reference node in 2025" added in both places |
| C4 | 10.8 | "revised illustration", "prior timing convention", "earlier full-CAPEX illustration" referred to unseen drafts | Neutral wording; "Applying the same rate to full CAPEX would give $40.33m PV." |
| C5 | 11.7 | Internal file path with an undefined code name in a body citation | `[CL-FIN-08]` |
| C6 | 8.1 | "[F02, physical PDF p. 1, Section 2.7]" read as a report section | "filing Section 2.7"; check script updated |
| C7 | 10.3, 10.8, 10.9, 13.3, Table 1-1, Table 1-2 note | "separately versioned / labeled version" wording | "calculation", "variant", "structure" |
| C8 | 10.3, 10.8 box, 10.10 note | File paths in body citations | Removed; sources remain in A.3 and B.9 |
| C9 | 12.5 | "Controlled update after the empirical extension", "controlled conclusion" | "Summary of conclusions", "Conclusion" |
| C10 | 8.1 | "inherited by this study" | "used in this study" |
| C11 | 4.7, 7.x | "this edition" in body text | "this report", "the report date" |
| C12 | 9.5 | "COD" undefined; "in the supplement" | "commercial operation dates (COD)"; internal reference dropped |
| C13 | 4.5, 5.6, 5.7, 8.1, 9.5, 10.3, 10.7, 10.8, 11.3, 11.6 | Ten sentences that restated a qualification made in the same passage | Deleted (the protected qualifier phrases are untouched; `build/check_report.py` enforces them) |

## Records

- `V1.0-Acceptance-Record.md` — delivery-edition criteria D1–D10 and the status of the original ten criteria.
- `R1-New-Numbers.csv` — every number added since V0.999, with its source.
- Checks: `Number-Preservation-Check.json`, `Figure-Data-Check.json`, `Report-Structure-Check.json`, `Rebuild-Verification.json`, `Build-Log.json`, `Page-Inspection-Log.md`.
