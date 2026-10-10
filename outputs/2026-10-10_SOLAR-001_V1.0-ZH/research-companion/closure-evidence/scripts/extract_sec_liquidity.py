"""Extract FY2024/FY2025 liquidity fields from SEC XBRL companyfacts JSON (saved in sources/sec).
Usage: python3 -I extract_sec_liquidity.py <sources/sec> <out_csv>. Values as reported; no conversion."""
import csv, json, sys
from pathlib import Path
SRC = Path(sys.argv[1])
CO = {1481513: "JinkoSolar Holding", 1375877: "Canadian Solar", 1477641: "Daqo New Energy", 1274494: "First Solar"}
FIELDS = [
 ("cash_and_equivalents", ["CashAndCashEquivalentsAtCarryingValue"]),
 ("restricted_cash_current", ["RestrictedCashAndCashEquivalentsAtCarryingValue", "RestrictedCashCurrent", "RestrictedCash"]),
 ("restricted_cash_noncurrent", ["RestrictedCashAndCashEquivalentsNoncurrent", "RestrictedCashNoncurrent"]),
 ("cash_restricted_total_cf", ["CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]),
 ("operating_cash_flow", ["NetCashProvidedByUsedInOperatingActivities"]),
 ("short_term_borrowings", ["ShortTermBorrowings", "OtherShortTermBorrowings"]),
 ("long_term_debt_current", ["LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent"]),
 ("debt_current_total", ["DebtCurrent"]),
 ("long_term_debt_noncurrent", ["LongTermDebtNoncurrent"]),
 ("ltd_maturity_next_12m", ["LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths"]),
 ("ltd_maturity_year2", ["LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo"]),
 ("ltd_maturity_year3", ["LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree"]),
 ("ltd_maturity_year4", ["LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour"]),
 ("ltd_maturity_year5", ["LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive"]),
 ("ltd_maturity_after5", ["LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive"]),
 ("warranty_accrual_total", ["ProductWarrantyAccrual", "StandardProductWarrantyAccrual"]),
 ("warranty_accrual_current", ["ProductWarrantyAccrualClassifiedCurrent", "StandardProductWarrantyAccrualCurrent"]),
 ("warranty_accrual_noncurrent", ["ProductWarrantyAccrualNoncurrent", "StandardProductWarrantyAccrualNoncurrent"]),
]
out = []
for cik, name in CO.items():
    d = json.load(open(SRC / f"CIK{cik}.json"))
    facts = d["facts"].get("us-gaap", {})
    for field, tags in FIELDS:
        for fy in ("2024", "2025"):
            found = None
            for tag in tags:
                if tag not in facts: continue
                for unit, arr in facts[tag]["units"].items():
                    def ok(x):
                        if x.get("form") not in ("10-K", "20-F") or x.get("end") != fy + "-12-31": return False
                        return "start" not in x or x["start"] == fy + "-01-01"
                    cand = [x for x in arr if ok(x)]
                    cand = [x for x in cand if x.get("fy") == 2025] or cand
                    if cand:
                        x = sorted(cand, key=lambda x: x["filed"])[-1]
                        found = (tag, unit, x["val"], x["accn"], x["form"], x["filed"], x.get("fy"))
                        break
                if found: break
            out.append([name, cik, "FY" + fy, field] + (list(found) if found else ["", "", "", "", "", "", ""]) + ["found" if found else "not tagged in XBRL (check filing note)"])
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f); w.writerow(["company", "cik", "period", "field", "xbrl_tag", "unit", "value", "accession", "form", "filed", "filing_fy", "status"]); w.writerows(out)
print(len(out), sum(1 for r in out if r[-1] == "found"))
