# Expert D — Round 2: Cross-Examination and Client Responses

**Reviewer:** Expert D (industry, trade policy, evidence presentation). **Date:** 10 October 2026.
**Read in this round:**
- `Expert-A-Energy-Markets-Review-EN.md`
- `Client-E-Manufacturer-Review-ZH.md`
- `Client-F-Developer-Buyer-Review-ZH.md` (F-02 only, because it is in my tax area)

**Rules:** The same rules as round 1 apply:
- Judgments rest only on retained originals.
- Derived figures are labelled "reviewer arithmetic".
- Where a source is not retained, I say "could not verify".
- Nothing here is legal advice.

---

## 1. Cross-examination of Expert A

### A-04 (foreclosure timing): partly agree. Keep it at P1, but change the fix.

**What the retained originals show:**

| Source | Retained? | What it establishes |
|---|---|---|
| `sources/finance/comparables/C06_ch313_1377_772_2025.pdf` (Form 50-772-A, TY2024), p.1 §2 item 7 | **Yes** (viewed) | "West Texas Solar Project II LLC purchased the project in a foreclosure auction initiated by the project's senior lender when the project's previous owner (Taygete Energy Project II, LLC) failed to repay its loan." **No date, lender or price.** |
| `sources/finance/comparables/C07_ch313_1377_773_2023.xlsx` (biennial progress report, reporting year 2023; file name `01377-773-SR-2023-0730`) | **Yes** (read) | "Company Name of Agreement Holder" and "Names of all the Current Holders" are both **West Texas Solar Project II LLC** |
| C09 amended certification packet ("On October 6, 2022, the Comptroller received an amendment … to assign the project to West Texas Solar Project II LLC") | **No.** It is listed only in `finance-supplement/Source-Catalog.csv` and quoted in `Entity-Node-Mapping.csv` L10, with a raw path outside this package | **Could not verify against the original** |
| COD July 2023 (EIA-860 plant 64075) | Quoted in `Entity-Node-Mapping.csv` L05. The link is "attribute_matched_not_document_linked" | Could not verify the original here |

**My conclusion:**
- The retained originals confirm that the current owner already held the agreement **in the 2023 progress report**. The file is dated about 30 July 2023, the same month as the attribute-matched COD.
- The 6 October 2022 date rests on a supplement quote of an unretained file. A's Medium confidence is right.
- No retained document states that the October 2022 assignment *is* the foreclosure purchase. The C06 wording is consistent with that reading, but it is not proven.

**Revised fix (append to L533 and L1381):**

> "The retained Comptroller filings show West Texas Solar Project II LLC as agreement holder by the 2023 progress report (filed around July 2023, the plant's reported in-service month); the finance supplement records a 6 October 2022 assignment notice, and the foreclosure date itself is not disclosed. The ownership change therefore cannot be read as evidence about 2024–2025 prices at this node."

This sentence avoids asserting "assignment = foreclosure" and does not rely on the unretained C09 file for its core claim.

**Severity:** P1 (agree). The timing context stops a causal reading that the brief's §4 rules out ("真实电站止赎也不证明假设项目回报"), i.e. a real-plant foreclosure does not prove the returns of the hypothetical project.

### A-01 ($66 break-even qualifiers; hub-hedge range): agree, P1. Two adjustments for tax framing.

1. **Pre-tax label.** The report also carries a credit-illustrated fixed-route break-even of **$53.51/MWh** (L822). If Table 1-1 gets a hub-hedge row, both rows should be labelled "pre-tax, no credit". Otherwise a reader may set $66 against $53.51 and treat them as alternative market prices. Suggested Table 1-1 label: "Flat nominal break-even, 30-yr node-level route (15.24% unpaid), pre-tax, no credit".
2. **Keep the unsourced market claim out of the report.** A's problem statement says "Market solar offers in ERCOT are usually hub-settled and have 10–15-year tenors". No retained original in the package supports that, and A's replacement text does not include it. It should stay that way.

There is no conflict with the trade framing.

### A-03 (2025 base mostly pre-RTC+B; 2026 diagnostic): agree, P1. No conflict.

The proposed sentence keeps the brief's boundary ("price diagnostic, not a 2026 capture price or forecast"), and it touches neither trade nor tax statements.

One linkage note for the coordinator (**not** a new task): the model pays CAPEX at end-2026 (L688). That falls just after the Proclamation 11052 effective date of 4 December 2026. A reader linking Chapters 5 and 10 may ask whether the hypothetical procurement would face the MIP. The report already says no tariff treatment is assigned to the hypothetical project (L407), so no edit is needed. I record the point only so that A-03's "latest market design" sentence is not extended into a claim about procurement conditions.

### A-05 (capture-ratio rule of thumb): agree, P1.

I verified the figures in `data/panel/Node-Hub-Comparisons.csv` (2025 rows):

| Location | Mean price | Capture price | Capture ratio |
|---|---|---|---|
| TAYGETE2_ALL | 46.37 | 22.13 | 0.477 |
| HB_WEST | 32.92 | 21.46 | 0.652 |

- The 3rd-percentile statement is the report's own (L60).
- Optional addition from the same file: HB_BUSAVG is 0.772. That shows how strongly the ratio depends on the reference location.

A's fix stands.

---

## 2. Responses to client items

### E-01 + D-11: dated trade facts in the executive summary. Merged; I accept E's P1 grading.

The client's concrete misreading ("the report only covers project returns; the 4 December date is missed") is plausible and costly. I upgrade my D-11 from P2 to P1 and merge it into E-01.

**One merged sentence** (new item 7 in §1.1, or appended to item 3):

> "From 4 December 2026, covered imported cells and modules face Proclamation 11052 minimum import prices ($0.22/W and $0.38/W) and, for most origins, an additional 15% ad valorem duty on top of continuing antidumping and countervailing duties; Commerce's 16 September 2026 final AD/CVD determinations for India, Indonesia and Laos await the ITC injury decision, and China ended export VAT rebates for listed PV products from 1 April 2026 — compliance thresholds and potential duties, not delivered prices or any supplier's tariff outcome. [P01; CL-B-02; P08, LONGi FY2025 AR p.297; Sections 4.4, 5.7]"

**Notes on the wording:**
- "For most origins" reflects clause 5(b)–(c): JP/KR/TW/CH/LI/EU have a combined 15%, and the UK has 10%.
- The ITC clause keeps the status conditional. E's draft omitted it. The VAT claim gets a retained-filing locator (my D-10), because the P08 page was never retrieved.
- I dropped "P07" from E's citation, because P07 is the NDRC power-pricing reform, not trade.

### E-03: Table 13-1 supplier-eligibility row and the MACR pointer. Agree, P1, with one correction to the substance.

E's analysis frames the material-assistance test as "China-owned or China-origin supply chains". The statute measures something different:
- The material assistance cost ratio is built from the taxpayer's direct costs of all manufactured products incorporated into the facility, minus those "mined, produced, or manufactured by a **prohibited foreign entity**".
- Source: P.L. 119-21, new §7701(a)(52)(D)(i), `sources/finance/tax/PLAW-119publ21.pdf`.
- The test turns on the producer's PFE status (ownership/control), **not on country of origin**. The report's L838 already says this correctly ("not percentages of module origin").

**Revised Table 13-1 cell ("What this report shows"):**

> "Facilities starting construction in 2026/2027 must meet material-assistance cost-ratio thresholds of 40%/45% — the share of manufactured-product cost not produced by a prohibited foreign entity — plus ownership/control rules (Section 10.8); the $35.38m credit illustration assumes eligibility and is not a supplier- or product-level finding."

I also agree with the two navigation edits:
- add "10.8" to the manufacturer reading path (L17);
- add "(see Section 10.8)" in the §13.1 question table.

I could not verify Notice 2026-15's safe-harbor detail beyond its title. The thresholds above come from the statute.

### E-04 + D-01: "U.S. module input" vs imported module price. Merged, P1.

**One merged wording.** Insert at the first use (L30), at the first bold use in §5.5 (L371), and in the Figure 5-1 caption:

> "U.S. module input (the DOE/NLR benchmark's bottom-up cost for a U.S.-assembled module: about $0.29/Wdc in 2024 dollars after the model's −$0.07/Wdc section 45X subsidy, about $0.36/Wdc before it; not an imported-module or export price)"

At L411, replace "including its stated subsidy treatment" with "net of the model's −$0.069/Wdc section 45X subsidy (about $0.36/Wdc before it)".

Evidence: `data/supplement/A/A_pvscm_item_level_pv_only.csv`. The Module rows sum to 291.21 $/kWdc; excluding the Subsidy row (−68.88) they sum to 360.09 (reviewer arithmetic).

E's draft text repeats the report's vague phrase "including its stated subsidy treatment". The merged version replaces it, because the vagueness is the problem.

### E-05: China-origin treatment under Proclamation 11052. "General MIP + 15%" is supportable but needs softer wording.

**What the retained text supports** (`closure-evidence/sources/trade/FR-2026-16400.txt` and PDF annex images):
- **No China-specific provision.** A grep for "China/Chinese/People's Republic" returns zero hits. This agrees with E's check.
- **The MIP has no country carve-out.** Clause 2 applies the MIP to all imports specified in Annexes I–II. Clause 5(b)–(c) modifies only the **clause (4) ad valorem duty**, for JP/KR/TW/CH/LI/EU and the UK.
- **Other routes can alter treatment:**
  - clause 6: approved onshoring plans, which allow imports "without paying applicable section 232 duties" and are company-specific;
  - clause 7: foreign-trade-zone status;
  - clause 8: drawback;
  - clause 10: the Secretary may alter MIP/tariff applicability for a trading partner with an equivalent MIP;
  - clause 1(b): the Secretary may adjust the MIPs.
- **Other duties remain in addition** (clause 5(a); Annex II note 42(b)).

**Is "therefore fall under the general MIP and additional 15%" safe?** The direction is supportable, but "therefore" overstates certainty, given company-specific relief and the Secretary's adjustment powers. **Use softer wording:**

> "The proclamation contains no China-specific rate; China is not among the listed country arrangements in clause 5, so covered Chinese-origin products are, on the face of the text, subject to the MIP program and the additional 15% ad valorem duty, subject to company-specific onshoring relief, later adjustments by the Secretary and other duties outside this report's quantification. This is not a customs ruling."

**Related clarification (P2, new):** The report's L405 sentence "Different arrangements apply to products of Japan, Korea, …" can be read as exempting those origins from the MIP. Add "(for the additional ad valorem duty; the MIP itself has no country carve-out in the text)".

Severity: P2 (agree with E). Confidence: High that the text is as described; this is not legal advice.

### E-07: First Solar 45X in the Figure 4-3 caption. Agree, P2.

- **Verified:** the fslr 10-K says "we recognized $1.6 billion of Section 45X credits as a reduction to 'Cost of sales'". This is the report's L283.
- E's caption text is correct as written.
- It complements my D-02: both concern margin comparisons across different bases.

### F-02 (tax area): agree, P1.

The −$50.59m figure is the pre-tax NPV plus one illustrative credit PV. F's replacement wording is accurate: the section 50(c) basis reduction, depreciation and income tax are not modelled (L840). No conflict with my findings.

---

## 3. Withdrawals and re-grades of my own findings

| ID | Round-1 grade | Round-2 grade | Change |
|---|---|---|---|
| D-01 | P1 | **P1, merged with E-04** | Use the merged wording in §2 |
| D-02 | P1 | **P1 (kept)** | Prefer option (a), relabel only, so that no numbers change. Use these labels: A-share rows "Industry-line margin (分行业), includes non-module businesses"; LONGi rows "Product-line margin (分产品)". Give the four module product-line margins in the note (Trina −1.42%, JA −4.03%, Tongwei −0.38%, LONGi 0.19%) plus LONGi's industry line of 0.81%. Harmonize the LONGi basis label. E-07 is a complementary caption fix, not a substitute |
| D-03 | P1 | P1 (kept) | None |
| D-04 to D-09 | P2 | P2 (kept) | None |
| D-10 | P2 | **P2, folded into E-01** | The merged summary sentence carries the retained-filing locator. The body-text fix at L237 still applies |
| D-11 | P2 | **P1, merged into E-01** | Upgraded on the client's evidence of a real misreading risk |
| D-12 | Disclosed limitation | Unchanged | — |
| New (from E-05) | — | **P2** | Clarify at L405 that the country arrangements concern the ad valorem duty, not the MIP |

I withdraw nothing. My round-1 verdict is unchanged: **② handover-ready after the listed minimal edits.**
