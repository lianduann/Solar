"""Build the small closure tables from files in the uploaded handoff package.

Usage: python3 -I build_closure_tables.py <HANDOFF_ROOT> <OUTPUT_TABLES_DIR>
Reads only; performs counting, sums and ratios. No model, regression or simulation.
"""
import csv, json, sys
from pathlib import Path

root = Path(sys.argv[1]) / "project" / "Deliverables"
out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
api = root / "2026-10-09_ERCOT-API-2026-Price-Data" / "data"
ed = root / "2026-10-09_Finance-Integrated-Client-Edition" / "data"

def w(name, header, rows):
    with open(out / name, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(header); wr.writerows(rows)

# 1. 2026 price coverage summary (FIN-08)
cov = list(csv.DictReader(open(api / "coverage_by_day_all_points.csv")))
qa = json.load(open(api / "qa_summary.json"))
thru = [r for r in cov if r["deliveryDate"] <= "2026-10-08"]
gap_days = [r for r in thru if int(r["system_wide_missing"]) > 0]
prio = list(csv.DictReader(open(api / "system_wide_missing_intervals_priority.csv")))
allp = list(csv.DictReader(open(api / "system_wide_missing_intervals_all.csv")))
src = "2026-10-09_ERCOT-API-2026-Price-Data/data/"
rows = [
 ["calendar days 2026-01-01..2026-10-08 with any published price", len(thru), "days", src + "coverage_by_day_all_points.csv", "range completeness, not interval completeness"],
 ["of which days with >=1 system-wide missing interval", len(gap_days), "days", src + "coverage_by_day_all_points.csv", ";".join(r["deliveryDate"] for r in gap_days)],
 ["days with every expected interval published (system-wide)", len(thru) - len(gap_days), "days", "derived", "281 minus 11"],
 ["system-wide missing intervals through 2026-10-08", sum(int(r["system_wide_missing"]) for r in thru), "15-min intervals", src + "coverage_by_day_all_points.csv", "not interpolated"],
 ["system-wide missing intervals incl. 2026-10-09 tail, all-points pull", len(allp), "15-min intervals", src + "system_wide_missing_intervals_all.csv", "16 of these are the 2026-10-09 unpublished tail"],
 ["system-wide missing intervals incl. tail, priority-point pull", len(prio), "15-min intervals", src + "system_wide_missing_intervals_priority.csv", "one more than all-points pull: 2026-10-09 19:45 CDT was published between the two pulls"],
 ["latest day with 96/96 intervals", qa["latest_day_with_full_interval_count"], "date", src + "qa_summary.json", ""],
 ["latest day presumed past 16:00 second-business-day finality time at QA run", qa["latest_day_presumed_past_finality_time"], "date", src + "qa_summary.json", "timing inference; Mon-Fri, ERCOT holidays not applied; no row-level version field"],
 ["HB_WEST intervals matched API vs NP6-785-ER (to 2026-10-03)", qa["hb_west_vs_np6_785_er"]["both"], "intervals", src + "qa_summary.json", ""],
 ["HB_WEST price differences > $0.005/MWh", qa["hb_west_vs_np6_785_er"]["price_mismatch_gt_0p005"], "intervals", src + "qa_summary.json", "max abs diff $%.2f/MWh; cause not established" % qa["hb_west_vs_np6_785_er"]["price_abs_diff_max"]],
 ["settlement points in all-points pull", qa["all_points"]["points"], "points", src + "qa_summary.json", ""],
 ["strict 485 nodes present / 7 benchmarks present", "%d / %d" % (qa["frozen_universe"]["strict_485_present"], qa["frozen_universe"]["benchmark_present"]), "points", src + "qa_summary.json", "no point-specific gaps through 2026-10-08"],
]
w("FIN-08_2026-Price-Coverage-Summary.csv", ["item", "value", "unit", "source_file", "note"], rows)

# 2. Weather fill-flag summary (B-04)
wq = json.load(open(ed / "weather_qa.json"))
fc = wq["fill_flag_counts"]; n = wq["time"]["n"]
rows = [[k, v, n, round(v / n, 6), "2025 weather_qa.json"] for k, v in fc.items()]
for r in csv.DictReader(open(ed / "empirical" / "site_energy_qa.csv")):
    rows.append(["nonzero (all codes)", "", r["nsrdb_steps"], r["fill_flag_nonzero_share"], "%s site_energy_qa.csv" % r["year"]])
w("B-04_Weather-Fill-Flag-Counts.csv", ["fill_flag_code", "count", "denominator_5min_steps", "share", "source"], rows)

# 3. Batch Zero chart vs narrative (B-03)
hb = list(csv.DictReader(open(ed / "supplement" / "C" / "C_batch_zero_headlines_2026-09.csv")))
by = list(csv.DictReader(open(ed / "supplement" / "C" / "C_batch_zero_conditional_by_year_2026-09.csv")))
stud2032 = sum(float(r["mw"]) for r in by if r["group"] == "Studied load" and r["year"] == "2032")
base2032 = sum(float(r["mw"]) for r in by if r["group"] == "Base load" and r["year"] == "2032")
rows = [[r["metric"], r["projects"], r["mw"], r["source"]] for r in hb]
rows.append(["Sum of studied-load category rows, 2032 column (transcribed table)", 158, stud2032, "C_batch_zero_conditional_by_year_2026-09.csv"])
rows.append(["Sum of base-load category rows, 2032 column (transcribed table)", 204, base2032, "C_batch_zero_conditional_by_year_2026-09.csv"])
w("B-03_Batch-Zero-Figure-vs-Narrative.csv", ["metric", "projects", "mw", "source_location"], rows)
print("ok", len(thru), len(gap_days), stud2032, base2032)
