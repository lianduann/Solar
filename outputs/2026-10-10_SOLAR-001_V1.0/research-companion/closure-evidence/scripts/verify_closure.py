"""Verify closure outputs against package inputs. Usage: python3 -I verify_closure.py <HANDOFF_ROOT> <OUTPUT_DIR>"""
import csv, json, re, sys
from pathlib import Path
H = Path(sys.argv[1]) / "project" / "Deliverables"; O = Path(sys.argv[2])
res = []
def chk(name, ok, detail=""): res.append((name, bool(ok), detail))
sv = H / "2026-10-09_Finance-Scenario-Versions" / "data"
cpi = {(r["point"], r["price_year"]): r for r in csv.DictReader(open(sv / "CPI-Harmonised-Scenario.csv"))}
t = cpi[("TAYGETE2_ALL", "2023")]; chk("CPI ref 2023 113.89", round(float(t["npv_4p27_cpi"]) / 1e6, 2) == 113.89)
t = cpi[("TAYGETE2_ALL", "2024")]; chk("CPI ref 2024 -89.64", round(float(t["npv_4p27_cpi"]) / 1e6, 2) == -89.64)
t = cpi[("485 nodes", "2023")]; chk("CPI median 2023 116.02", round(float(t["npv_4p27_cpi_median"]) / 1e6, 2) == 116.02)
a3 = [r for r in csv.DictReader(open(H / "2026-10-09_Finance-Integrated-Client-Edition/data/empirical/A_3x3_summary.csv")) if r["grp"].startswith("strict") and r["weather_year"] == r["price_year"] == "2024"][0]
chk("Table 10-4 2024 median -81.59 (common calendar)", round(float(a3["npv_4p27_median"]) / 1e6, 2) == -81.59)
chk("CPI file 2024 frozen median -81.33 (differs)", round(float(cpi[("485 nodes", "2024")]["npv_4p27_frozen_median"]) / 1e6, 2) == -81.33)
v = [float(r["breakeven_strike_nominal_flat"]) for r in csv.DictReader(open(sv / "VPPA-Breakeven-Strikes.csv")) if r["price_year"] == "2025" and r["discount_rate"] == "0.0427"]
chk("VPPA 4.27% range 60.6-84.8", (round(min(v), 1), round(max(v), 1), len(v)) == (60.6, 84.8, 8), str((min(v), max(v), len(v))))
cr = {(r["variant"]): r for r in csv.DictReader(open(sv / "Credit-Base-Scenarios.csv")) if r["scenario"] == "A1_OCC_only" and r["discount_rate"] == "0.042700"}
chk("credit variants 33.10/31.84/7.08", [round(float(cr[k]["credit_pv"]) / 1e6, 2) for k in ("recv_end2028", "transfer_0.90", "pwa_not_met_6pct")] == [33.10, 31.84, 7.08])
hb = {(r["period"], r["year"]): r for r in csv.DictReader(open(sv / "HB_WEST-2026-JanSep-Post-RTCB-Context.csv"))}
chk("HB_WEST 18.24/21.36", (round(float(hb[("Jan-Sep", "2026")]["profile_weighted_usd_mwh"]), 2), round(float(hb[("Jan-Sep", "2025")]["profile_weighted_usd_mwh"]), 2)) == (18.24, 21.36))
chk("HB_WEST neg share 14.1/7.7", (round(100 * float(hb[("Jan-Sep", "2026")]["negative_interval_share"]), 1), round(100 * float(hb[("Jan-Sep", "2025")]["negative_interval_share"]), 1)) == (14.1, 7.7))
cov = {r["item"]: r["value"] for r in csv.DictReader(open(O / "tables/FIN-08_2026-Price-Coverage-Summary.csv"))}
chk("2026 coverage 281/270/125", [cov[k] for k in list(cov)[:4]] == ["281", "11", "270", "125"])
wq = json.load(open(H / "2026-10-09_Finance-Integrated-Client-Edition/data/weather_qa.json"))
n = wq["time"]["n"]; f = wq["fill_flag_counts"]
chk("fill flag shares 1.25/1.24/1.62/4.1", [round(100 * f[k] / n, 2) for k in ("1", "5", "7")] == [1.25, 1.24, 1.62] and round(100 * (n - f["0"]) / n, 1) == 4.1)
d = list(csv.DictReader(open(O / "Closure-Disposition.csv")))
allowed = {"evidence integrated", "partially disclosed", "not publicly disclosed / inaccessible in this pass", "inaccessible in this pass", "not an existing fact of the hypothetical case (settlement agreement); identity chain partially disclosed"}
ids = [r["id"] for r in d]
chk("16 dispositions", ids == [f"FIN-{i:02d}" for i in range(1, 12)] + [f"B-0{i}" for i in range(1, 6)])
chk("no pending disposition", all(r["disposition"] in allowed for r in d), str([r["disposition"] for r in d if r["disposition"] not in allowed]))
chk("no empty required fields", all(all(r[k] for k in r) for r in d))
fx = (O / "Findings-and-Replacement-Text-EN.md").read_text()
chk("every ID has a Findings section", all(f"## {i} " in fx for i in ids))

# ---- round 2 checks (saved originals)
lt = (O / "sources/cninfo/LONGi_2025_AR.txt").read_text()
chk("LONGi KPIs verbatim", all(s in lt for s in ["70,347,049,950.42", "-6,419,556,843.85", "4,359,382,755.77", "5,893,972,740.27"]))
chk("LONGi segment margins 0.19 / -5.30", ("59,920,375,950.77" in lt) and ("6,539,863,524.01" in lt))
fin09 = list(csv.DictReader(open(O / "tables/FIN-09_Supplier-Liquidity.csv")))
chk("FIN-09 145 values, none NOT FOUND", len(fin09) == 145 and not [r for r in fin09 if r["check"] == "NOT FOUND"])
fr = (O / "sources/trade/FR-2026-16400_plain.txt").read_text()
chk("Proclamation clause 2(c) shortfall text", "specific tariff equal to the difference between" in fr and "$0.38 per watt for solar modules" in fr)
dk = (O / "sources/legal/CourtListener_RECAP_docket_dcd_1-25-cv-04400_retrieved_2026-10-10.html").read_text(errors="ignore")
chk("RECAP docket terminated June 8, 2026", "June 8, 2026" in dk)
bz = (O / "sources/other/bz.txt").read_text()
chk("Batch Zero 127.9 and 125.4 in deck", "127.9 GW" in bz and "125.4 GW" in bz)
im = (O / "sources/other/IMM_2025_State-of-the-Market_ERCOT.txt").read_text()
chk("IMM quotes (57 hours; 17 GW; Roughly 6% of solar)", "ORDC was active for only 57 hours" in im and "exceeded 17 GW" in im and "Roughly 6% of solar generation was curtailed" in re.sub(r"\s+", " ", im))
pat = re.compile(r"(api[_-]?key\s*[:=]\s*\S{12,}|bearer\s+[a-z0-9\-_\.]{20,}|Ocp-Apim-Subscription-Key\s*[:=]|password\s*[:=]\s*\S+|eyJ[a-zA-Z0-9_\-]{20,}\.)", re.I)
hits = [str(p) for p in O.rglob("*") if p.is_file() and p.suffix in (".md", ".csv", ".py", ".txt", ".json") and pat.search(p.read_text(errors="ignore"))]
chk("credential scan", not hits, str(hits))
for name, ok, det in res: print(("PASS" if ok else "FAIL"), name, det)
json.dump([{"check": a, "pass": b, "detail": c} for a, b, c in res], open(O / "verification_results.json", "w"), indent=1)
sys.exit(0 if all(b for _, b, _ in res) else 1)
