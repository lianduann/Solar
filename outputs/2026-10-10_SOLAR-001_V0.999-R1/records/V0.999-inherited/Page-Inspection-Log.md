# SOLAR-001 V0.999 page inspection log

Every page of the final PDF (85 pages) was rendered to PNG and inspected visually. Page images: `page-inspection/pages/page-NNN.png` (100 dpi); contact sheets of six pages: `page-inspection/sheets/`.

## Inspection rounds

1. First full build (90 pages): all pages rendered at 80 dpi and inspected. Defects found are listed below.
2. Fixes applied to the layout source; affected pages rebuilt and re-inspected; then every page of the final build re-rendered and checked again.

## Defects found and fixed

| # | Where (first build) | Defect | Fix | Re-check |
|---|---|---|---|---|
| 1 | Contents | Page numbers rendered as 0, no leaders; contents ran to a third, almost empty page | Contents entries laid out without flex so `target-counter()` and leaders resolve; spacing tightened to two pages | Pages 2–3 |
| 2 | Cover | Wordmark wrapped onto two lines | No-wrap | Page 1 |
| 3 | Running text | Values split across lines ('$48.9/ MWh', '− $103.3m') | Signed values and value/unit expressions kept on one line | All text pages |
| 4 | Table 10-2, Table 4-3B | Table wider than the text column (long nowrap headers) | Header cells wrap; only numeric data cells stay unbroken | Pages 20–21, 47–48 |
| 5 | Table 1-1 and other long tables | Whole table pushed to next page leaving a large gap | Tables over eight rows may break between rows; header row repeats | Pages 5–7 and all tables |
| 6 | Chapter 11 opener | Chapter number alone on one page, title on the next | Opener kept together; Figure 11-1 height capped so the opener, 11.1 and the figure fit | Page 56 |
| 7 | Table 4-3B notes | One footnote line and an unrelated note stranded on the next page | Notes kept together and with the table; NWC note moved under Table 4-3A | Pages 20–21 |
| 8 | Figures 6-2, 7-3 | Large blank areas before tall figures | Following paragraph placed before the figure (same section) | Pages 28–29, 32–33 |
| 9 | Appendix D | One glossary row alone on the last text page | Glossary rows tightened; table fits one page | Page 84 |
| 10 | Back cover | Straight apostrophe and hyphenated subtitle | Typographic apostrophe; no hyphenation | Page 85 |
| 11 | Figure 6-1 note | Source written as 'the original report from the official DOE document path' | Named publication, page and table | Page 27 |
| 12 | B.5 | '(1.0427)^16' shown literally | Exponent typeset | Page 81 |
| 13 | PDF bookmarks | Chapter bookmarks ran label and title together | 'Chapter N. Title' | Bookmark panel |

## Remaining layout characteristics (not defects)

- Chapters start on a new page, so the last page of some chapters is partly empty (for example pages 21, 44, 64, 71).
- Where a figure or table does not fit in the remaining space, the page ends early (for example pages 32 and 48).

## Page-by-page record (final build)

| Page | Content starting on the page | Result |
|---|---|---|
| 1 | Cover: title, subtitle, tagline, edition line; art does not overlap text | Inspected; no open defect |
| 2 | Contents page 1; leaders and page numbers present | Inspected; no open defect |
| 3 | Contents page 2 | Inspected; no open defect |
| 4 | About this report — Table 0-1 | Inspected; no open defect |
| 5 | Executive Summary: Lower Equipment Prices Require a Commercial Route to Project Value; 1.1 Key findings | Inspected; no open defect |
| 6 | 1.2 Key numbers — Table 1-1 | Inspected; no open defect |
| 7 | 1.3 How to interpret and use the findings | Inspected; no open defect |
| 8 | Analytical Framework: Connecting Equipment Supply to Paid Electricity; 2.1 Three analytical layers, with distinct evidence requirements; 2.2 Definitions that affect interpretation — Table 2-1 | Inspected; no open defect |
| 9 | 2.3 Observations, calculations, and assumptions; 2.4 How to read scenario results | Inspected; no open defect |
| 10 | 2.5 Five working hypotheses | Inspected; no open defect |
| 11 | Global Solar Demand: Industry Scale Does Not Define an Accessible Market; 3.1 Installed capacity establishes the scale of deployment; 3.2 Capacity changes, shipments, and production measure different activity — Figure 3-1 | Inspected; no open defect |
| 12 | 3.3 Regional evidence — Figure 3-2 | Inspected; no open defect |
| 13 | 3.4 Implications for market screening | Inspected; no open defect |
| 14 | China’s Solar Manufacturing Industry: High Output Can Coexist with Margin Pressure; 4.1 Manufacturing evidence: 2024 annual cutoff — Table 4-1 | Inspected; no open defect |
| 15 | 4.2 Company financial panel: margins and cash flows answer different questions — Figure 4-1, Table 4-2 | Inspected; no open defect |
| 16 | 4.3 Procurement implications extend beyond the quoted price | Inspected; no open defect |
| 17 | 4.4 Policy, market access and ownership; 4.5 Common-period company evidence shows heterogeneous financial outcomes — Figure 4-2 | Inspected; no open defect |
| 18 | 4.6 Utilization indicators require explicit capacity denominators — Figure 4-3 | Inspected; no open defect |
| 19 | 4.7 Additional FY2025 disclosures broaden the manufacturing sample | Inspected; no open defect |
| 20 | continued text — Table 4-3A, Table 4-3B | Inspected; no open defect |
| 21 | continued text | Inspected; no open defect |
| 22 | Cost Transmission: A Lower Module Price Reduces Only Part of Project Investment; 5.1 The delivered-cost bridge; 5.2 Module share determines the direct CAPEX effect; 5.3 What the ATB benchmark contributes | Inspected; no open defect |
| 23 | 5.4 Evidence required for an empirical transmission analysis; 5.5 A reproducible component model bounds the transmission mechanism — Figure 5-1 | Inspected; no open defect |
| 24 | 5.6 From component savings to project value — Figure 5-2, Table 5-1 | Inspected; no open defect |
| 25 | 5.7 Policy changes make procurement dates and classification commercially relevant | Inspected; no open defect |
| 26 | 5.8 Import value and sourcing shifts provide context, not a delivered-price series | Inspected; no open defect |
| 27 | Data-Center Demand: Annual Energy and Continuous Supply Are Different Products; 6.1 National scenarios establish a range of modeled demand — Figure 6-1 | Inspected; no open defect |
| 28 | 6.2 Procurement requirements determine the product being sold; 6.3 ERCOT’s observed operating shapes illustrate the timing issue; 6.4 Regional process evidence separates requested load from operating demand | Inspected; no open defect |
| 29 | 6.5 Self-supply evidence indicates a requirement for more than solar energy — Figure 6-2 | Inspected; no open defect |
| 30 | continued text — Figure 6-3 | Inspected; no open defect |
| 31 | ERCOT Market Conditions: Location and Timing Jointly Shape Value; 7.1 Market references and settlement exposure; 7.2 Intraday and seasonal system conditions — Figure 7-1 | Inspected; no open defect |
| 32 | continued text — Figure 7-2 | Inspected; no open defect |
| 33 | 7.3 Regional screening requires more than solar-resource quality; 7.4 Pipeline and network records support screening rather than guaranteed supply — Figure 7-3 | Inspected; no open defect |
| 34 | continued text | Inspected; no open defect |
| 35 | Solar Value Capture: High-Output Hours May Have Lower Prices; 8.1 The reference-node price comparison — Table 8-1 | Inspected; no open defect |
| 36 | 8.2 Negative-price exposure and the assumed operating response — Figure 8-1 | Inspected; no open defect |
| 37 | 8.3 Monthly outcomes separate volume from value; 8.4 A common three-year sample — Figure 8-2 | Inspected; no open defect |
| 38 | 8.5 Reference-node representativeness; 8.6 What the statistical comparisons indicate — Figure 8-3 | Inspected; no open defect |
| 39 | 8.7 What the statistical comparisons can be used for; 8.8 Node basis persists, but its cause remains unidentified — Figure 8-4 | Inspected; no open defect |
| 40 | continued text — Figure 8-5 | Inspected; no open defect |
| 41 | Independent Generation Simulation: Resource, Design, and Weather-Year Effects; 9.1 Reference location and weather coverage; 9.2 System configuration — Table 9-1 | Inspected; no open defect |
| 42 | 9.3 Generation and design sensitivities; 9.4 Three weather years improve comparison without establishing long-run uncertainty; 9.5 Operating-plant evidence: a plausibility check, not calibration — Table 9-2 | Inspected; no open defect |
| 43 | continued text — Figure 9-1 | Inspected; no open defect |
| 44 | continued text | Inspected; no open defect |
| 45 | Financial Scenarios: Cash-Flow Definitions Precede Return Interpretation; 10.1 Timing, currency basis, and model scope; 10.2 Cost coverage and unquantified items | Inspected; no open defect |
| 46 | 10.3 Two distinct revenue mechanisms | Inspected; no open defect |
| 47 | continued text — Table 10-1 | Inspected; no open defect |
| 48 | 10.4 Scenario results — Figure 10-1, Table 10-2 | Inspected; no open defect |
| 49 | 10.5 Operating receipts and capital recovery answer different questions; 10.6 LCOE, contract duration and IRR — Figure 10-2 | Inspected; no open defect |
| 50 | 10.7 Benchmark scope and project cost reconciliation — Figure 10-3 | Inspected; no open defect |
| 51 | continued text | Inspected; no open defect |
| 52 | 10.8 Tax timing and basis: a revised illustration, not an entitlement — Table 10-3 | Inspected; no open defect |
| 53 | continued text — Table 10-4 | Inspected; no open defect |
| 54 | 10.9 Historical price-year substitution changes the sign of modeled NPV — Table 10-5, Table 10-6 | Inspected; no open defect |
| 55 | continued text | Inspected; no open defect |
| 56 | Sensitivity and Break-Even Analysis: Turning Results into Testable Conditions; 11.1 One-way sensitivities measure effects within chosen ranges — Figure 11-1 | Inspected; no open defect |
| 57 | 11.2 Physical performance and commercial realization interact; 11.3 Break-even conditions — Table 11-1 | Inspected; no open defect |
| 58 | 11.4 Two-way sensitivities; 11.5 Remaining robustness questions — Figure 11-2 | Inspected; no open defect |
| 59 | 11.6 Crossed weather and price years locate the model’s sensitivity; 11.7 Model accounting assigns most of the change to the price setting — Figure 11-3 | Inspected; no open defect |
| 60 | continued text — Figure 11-4, Table 11-2 | Inspected; no open defect |
| 61 | 11.8 Tail dependence qualifies the positive historical scenario — Figure 11-5, Table 11-3 | Inspected; no open defect |
| 62 | continued text | Inspected; no open defect |
| 63 | 11.9 Resampling and mixture scenarios have limited meanings — Figure 11-6 | Inspected; no open defect |
| 64 | continued text | Inspected; no open defect |
| 65 | Five Research Hypotheses: Evidence, Alternative Explanations, and Revision Conditions; 12.1 Equipment-price hypothesis — Mixed; 12.2 Demand-value hypothesis — Not testable; 12.3 Value-chain hypothesis — Supported for the observed businesses | Inspected; no open defect |
| 66 | 12.4 Grid-constraint hypothesis — Not testable; 12.5 Storage hypothesis — Not yet tested | Inspected; no open defect |
| 67 | 12.6 Controlled update after the empirical extension — Table 12-1 | Inspected; no open defect |
| 68 | Commercial Applications: Procurement, Development, and Market Screening; 13.1 Equipment suppliers: demonstrate value within the customer’s system — Table 13-1 | Inspected; no open defect |
| 69 | 13.2 Developers: assess generation and payment rules together; 13.3 Research teams: test each link in the market thesis; 13.4 Electricity buyers: compare the product and the obligations | Inspected; no open defect |
| 70 | 13.5 A decision matrix for using the expanded evidence — Table 13-2, Table 13-3 | Inspected; no open defect |
| 71 | continued text | Inspected; no open defect |
| 72 | Outlook and Updates: Conditional Scenarios with Identifiable Evidence; 14.1 What the present evidence permits; 14.2 Conditional market developments | Inspected; no open defect |
| 73 | 14.3 Indicators and revision triggers; 14.4 Interpretation of the extended investment evidence — Table 14-1 | Inspected; no open defect |
| 74 | Source Bibliography | Inspected; no open defect |
| 75 | A.1 Comparable-project, cost, contract and tax sources (F references) | Inspected; no open defect |
| 76 | A.2 Supplementary verification sources (CL references) | Inspected; no open defect |
| 77 | Methods and Interpretation; B.1 Market data and node selection — Table B-1 | Inspected; no open defect |
| 78 | B.2 Output and financial conventions | Inspected; no open defect |
| 79 | B.3 Conditional regressions and inference — Table B-2 | Inspected; no open defect |
| 80 | B.4 Accounting contributions and tail stresses — Figure B-1 | Inspected; no open defect |
| 81 | B.5 Finance integration: reproducible arithmetic and evidence boundaries | Inspected; no open defect |
| 82 | Evidence Boundaries and Undisclosed Fields — Table C-1 | Inspected; no open defect |
| 83 | continued text | Inspected; no open defect |
| 84 | Glossary — Table D-1 | Inspected; no open defect |
| 85 | Back cover: boundary statement; typographic apostrophe | Inspected; no open defect |
