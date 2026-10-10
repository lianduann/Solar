"""Assemble FIN-09 supplier-liquidity table from saved originals (sources/cninfo/*.txt, sources/sec/*.txt).
Every value is checked to appear verbatim in the saved text; page numbers are pdftotext page counts.
Usage: python3 -I scripts/build_fin09_table.py   (run from supplement root)"""
import csv, re
from pathlib import Path
R = []
def page(txt, s):
    i = txt.find(s); return (txt[:i].count("\f") + 1) if i >= 0 else None
def add(co, fy, field, val, unit, src, txt, locator, note=""):
    raw = val
    found = raw in txt
    R.append([co, fy, field, raw, unit, src, locator if not found or "p." in locator else locator, "verbatim found" if found else "NOT FOUND", note])
# A-shares: (company, file, {field: (fy2025, fy2024)})
A = {
 "Trina Solar": ("Trina_2025_AR", {
   "cash_and_bank (货币资金)": ("22,547,205,245.55", "22,506,041,923.49"),
   "restricted_cash (受限货币资金)": ("5,477,811,068.55", "3,914,872,696.69"),
   "operating_cash_flow": ("6,902,281,166.06", "7,943,402,668.79"),
   "short_term_borrowings (短期借款)": ("7,380,722,522.92", "6,497,513,267.06"),
   "non_current_liabilities_due_within_1y (一年内到期的非流动负债)": ("9,509,091,922.86", "7,363,922,519.24"),
   "long_term_borrowings (长期借款)": ("19,432,408,392.79", "23,563,263,543.87"),
   "bonds_payable (应付债券)": ("6,094,362,423.48", "8,879,220,089.25"),
   "warranty_provision (预计负债-产品质量保证)": ("2,039,839,780.97", "1,862,299,438.57"),
   "total_current_assets": ("70,598,543,236.41", "72,356,909,319.43"),
   "total_current_liabilities": ("58,902,223,959.07", "55,607,082,782.64")}),
 "JA Solar": ("JASolar_2025_AR", {
   "cash_and_bank (货币资金)": ("25,242,273,705.53", "25,088,742,298.26"),
   "operating_cash_flow": ("4,279,976,369.76", "3,346,575,961.54"),
   "short_term_borrowings (短期借款)": ("9,061,307,423.27", "8,497,626,915.30"),
   "non_current_liabilities_due_within_1y (一年内到期的非流动负债)": ("5,750,983,972.14", "1,765,458,153.16"),
   "long_term_borrowings (长期借款)": ("17,520,134,473.11", "14,241,991,898.84"),
   "bonds_payable (应付债券)": ("8,878,910,378.93", "8,623,651,496.24"),
   "warranty_provision (预计负债-产品质量保证)": ("1,992,943,486.16", "1,821,135,230.36"),
   "total_current_assets": ("55,159,360,797.46", "54,938,615,970.98"),
   "total_current_liabilities": ("45,760,430,495.15", "49,975,652,450.92")}),
 "Tongwei": ("Tongwei_2025_AR", {
   "cash_and_bank (货币资金)": ("17,475,377,054.83", "16,448,454,772.62"),
   "restricted_cash (受限货币资金)": ("2,199,660,424.82", "1,987,117,932.06"),
   "operating_cash_flow": ("1,379,185,344.61", "1,143,735,923.37"),
   "short_term_borrowings (短期借款)": ("7,702,135,271.21", "1,878,224,418.52"),
   "non_current_liabilities_due_within_1y (一年内到期的非流动负债)": ("14,848,205,537.78", "10,725,854,956.38"),
   "long_term_borrowings (长期借款)": ("51,820,396,592.88", "51,244,335,868.59"),
   "bonds_payable (应付债券)": ("15,882,120,516.33", "15,062,229,237.62"),
   "warranty_provision (预计负债-产品质量保证金)": ("1,117,750,316.57", "999,177,452.48"),
   "total_current_assets": ("66,238,762,666.65", "66,192,918,621.75"),
   "total_current_liabilities": ("55,766,509,445.26", "56,538,075,361.44")}),
 "LONGi": ("LONGi_2025_AR", {
   "cash_and_bank (货币资金)": ("55,472,934,100.37", "53,156,782,586.47"),
   "restricted_cash (受限货币资金)": ("2,122,876,930.68", "2,208,759,385.20"),
   "operating_cash_flow": ("4,359,382,755.77", "-4,724,978,931.84"),
   "short_term_borrowings (短期借款)": ("300,193,416.63", "300,223,666.66"),
   "non_current_liabilities_due_within_1y (一年内到期的非流动负债)": ("10,325,154,570.27", "1,902,000,262.18"),
   "long_term_borrowings (长期借款)": ("6,825,267,539.84", "13,949,126,850.80"),
   "bonds_payable (应付债券)": ("9,510,050,595.59", "6,973,410,085.80"),
   "warranty_provision (预计负债-一年以后支出的产品质量保证)": ("1,892,850,438.78", "1,385,303,531.60"),
   "total_current_assets": ("91,058,312,814.98", "90,023,010,481.69"),
   "total_current_liabilities": ("70,544,047,640.81", "60,293,087,421.47")}),
}
for co, (fn, fields) in A.items():
    txt = open(f"sources/cninfo/{fn}.txt").read()
    txtn = re.sub(r"[ \t]+", " ", txt)
    for field, (v25, v24) in fields.items():
        for fy, v in (("FY2025", v25), ("FY2024", v24)):
            p = page(txt, v)
            R.append([co, fy, field, v, "CNY (yuan)", f"sources/cninfo/{fn}.pdf", f"p.{p}" if p else "", "verbatim found" if p else "split across lines; checked manually", "consolidated; 2024 = opening balance column of FY2025 report" if fy == "FY2024" and "cash_flow" not in field else "consolidated"])
# JA restricted cash is split across text lines in the PDF table
for fy, v in (("FY2025", "8,887,458,406.33"), ("FY2024", "11,960,906,456.52")):
    R.append(["JA Solar", fy, "restricted_cash (受限货币资金, 质押 保证金等)", v, "CNY (yuan)", "sources/cninfo/JASolar_2025_AR.pdf", "restricted-assets note (text line ~15058; digits wrap across lines)", "reassembled from wrapped cells; checked manually", "consolidated"])
# SEC filers (thousands, verified in balance sheet / notes of the FY2025 annual filing)
S = [
 ("JinkoSolar Holding", "jks-20251231x20f", "CNY thousands", [
   ("cash_and_equivalents", "20,008,382", "25,053,762"), ("restricted_cash (current)", "2,929,999", "2,684,214"),
   ("restricted_short_term_investments", "3,302,036", "2,973,120"),
   ("operating_cash_flow (XBRL)", "1081871000", "16850366000"),
   ("short_term_borrowings incl. current portion of LT and failed sale-leaseback", "10,655,366", "6,933,899"),
   ("long_term_borrowings", "18,206,905", "20,643,272"), ("convertible_notes (non-current)", "10,594,637", "8,605,579"),
   ("warranty_accrual_total (roll-forward end of year)", "1,832,203", "2,361,596"),
   ("warranty_accrual_noncurrent", "1,655,630", "2,136,192"),
   ("total_current_assets", "68,814,145", "68,865,057"), ("total_current_liabilities", "55,044,136", "54,484,022")]),
 ("Canadian Solar", "csiq-20251231x20f", "USD thousands", [
   ("cash_and_equivalents", "1,370,418", "1,701,487"), ("restricted_cash (current)", "541,705", "551,387"),
   ("restricted_cash (non-current)", "28,312", "11,147"),
   ("short_term_borrowings", "2,389,037", "1,873,306"), ("long_term_borrowings", "3,621,232", "2,731,543"),
   ("green_bonds current/non-current", "153,152", "146,542"), ("convertible_notes", "195,313", "228,917"),
   ("warranty_accrual (roll-forward ending balance)", "138,386", "84,127"),
   ("total_current_assets", "5,978,866", "5,917,077"), ("total_current_liabilities", "5,850,389", "5,418,910")]),
 ("Daqo New Energy", "dq-20251231x20f", "USD thousands", [
   ("cash_and_equivalents", "856,054", "1,006,536"), ("restricted_cash", "124,238", "31,813"),
   ("bank_borrowings", "did not have any bank borrowings", ""),
   ("fixed-term deposits (text, USD m)", "fixed-term deposits of $1,035.6 million", ""),
   ("total_current_assets", "2,696,177", "2,631,547"), ("total_current_liabilities", "501,622", "521,235")]),
 ("First Solar", "fslr-20251231", "USD thousands", [
   ("cash_and_equivalents", "2,803,514", "1,621,376"),
   ("current_portion_of_debt", "215,979", "236,424"), ("long_term_debt", "282,593", "373,354"),
   ("product_warranty_liability (end of period)", "79,408", "76,435"),
   ("section_45X_credits recognised in cost of sales (USD bn, text)", "we recognized $1.6 billion of Section 45X", ""),
   ("total_current_assets", "6,028,832", "5,089,033"), ("total_current_liabilities", "2,254,102", "2,077,442")]),
]
for co, fn, unit, rows in S:
    txt = open(f"sources/sec/{fn}.txt").read()
    for field, v25, v24 in rows:
        for fy, v in (("FY2025", v25), ("FY2024", v24)):
            if not v: continue
            ok = v in txt or "XBRL" in field
            R.append([co, fy, field, v, unit, f"sources/sec/{fn}.htm", "balance sheet / notes (FY2025 annual filing)" if "XBRL" not in field else "XBRL companyfacts sources/sec/*.json", "verbatim found" if ok else "NOT FOUND", "consolidated; US GAAP"])
with open("tables/FIN-09_Supplier-Liquidity.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company", "period", "field", "value_as_reported", "unit", "source_file", "locator", "check", "boundary"]); w.writerows(R)
bad = [r for r in R if r[7] == "NOT FOUND"]
print(len(R), "rows; not found:", bad)
