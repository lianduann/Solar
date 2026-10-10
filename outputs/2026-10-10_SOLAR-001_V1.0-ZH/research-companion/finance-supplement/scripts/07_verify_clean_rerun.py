"""Clean-directory re-run and verification for the 2026-10-09 finance-deepening supplement.
Re-runs scripts 02-06 into a fresh directory, compares every regenerated table with the delivered one, checks the delivered
node-hub tables (script 01, not re-run) against the frozen panel Node-Hub-Comparisons.csv, and writes Verification.json.
Usage: 07_verify_clean_rerun.py <project_root> <clean_dir>"""
import json, shutil, subprocess, sys, platform
from pathlib import Path
import pandas as pd
ROOT = Path(sys.argv[1]).resolve(); CLEAN = Path(sys.argv[2]).resolve(); SUP = ROOT / "Deliverables/2026-10-09_Finance-Deepening-Supplement"; SC = ROOT / "Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts"
E = ROOT / "Data/raw/2026-10-09_Finance-Deepening/EIA"
if CLEAN.exists(): shutil.rmtree(CLEAN)
(CLEAN / "data").mkdir(parents=True)
runs = []
def run(args):
    p = subprocess.run([sys.executable] + [str(a) for a in args], cwd=ROOT, capture_output=True, text=True); runs.append(dict(cmd=" ".join(str(a) for a in args), exit=p.returncode, stderr_tail=p.stderr[-400:])); return p.returncode
run([SC / "02_eia_operating_generation.py", "--eia860", E / "eia8602025.zip", "--eia923", E / "f923_2023.zip", ROOT / "Data/raw/2026-08-25/US/EIA/2024_EIA-923_final.zip", E / "f923_2025.zip", "--out", CLEAN / "data"])
run([SC / "03_ercot_battery_vintage.py", E / "eia8602025.zip", CLEAN / "data/ERCOT-Battery-Capacity-by-Vintage-EIA860-2025.csv"])
run([SC / "04_extract_ch313_773.py", ROOT / "Data/raw/2026-10-09_Finance-Deepening/comparables", CLEAN / "data/Ch313-Form773-2023-Extract.csv"])
run([SC / "05_finance_arithmetic.py", "--panel", ROOT / "Deliverables/2026-10-09_Panel-Revision-Client-Edition", "--supp", CLEAN])
cmp = []
for f in ["EIA-860-2025_WestTX_PV_generators.csv", "EIA-Operating-Generation-Comparables.csv", "EIA-Operating-Generation-Monthly-2023-2025.csv", "ERCOT-Battery-Capacity-by-Vintage-EIA860-2025.csv", "Ch313-Form773-2023-Extract.csv", "Finance-Arithmetic-Checks.csv"]:
    a, b = pd.read_csv(SUP / "data" / f), pd.read_csv(CLEAN / "data" / f)
    cmp.append(dict(file=f, rows=len(a), identical=bool(a.equals(b))))
# script 01 outputs vs frozen panel table (independent reproduction check)
nh = pd.read_csv(ROOT / "Deliverables/2026-10-09_Panel-Revision-Client-Edition/data/panel/Node-Hub-Comparisons.csv")
cap = pd.read_csv(SUP / "data/Node-Hub-Solar-Capture-2023-2025.csv"); bas = pd.read_csv(SUP / "data/Node-Hub-Basis-2023-2025.csv")
x = []
for y in (2023, 2024, 2025):
    lab = "2024_excl_Feb29" if y == 2024 else str(y)
    for node in ("TAYGETE2_ALL", "HB_WEST", "HB_BUSAVG"):
        mine = cap[(cap.period == lab) & (cap.point == node)].iloc[0]; frz = nh[(nh.price_year == y) & (nh.node == node)].iloc[0]
        x.append(dict(year=y, point=node, capture_mine=round(mine.generation_weighted_usd_mwh, 4), capture_frozen=round(frz.capture_price, 4), mean_mine=round(mine.time_weighted_usd_mwh, 4), mean_frozen=round(frz.mean_price, 4),
                      abs_diff_capture=round(abs(mine.generation_weighted_usd_mwh - frz.capture_price), 4)))
    mb = bas[(bas.period == lab) & (bas.hub == "HB_WEST")].iloc[0].generation_weighted_basis_usd_mwh; fb = nh[(nh.price_year == y)].iloc[0].generation_weighted_node_minus_west_basis
    x.append(dict(year=y, point="basis TAYGETE2_ALL-HB_WEST", capture_mine=round(mb, 4), capture_frozen=round(fb, 4), abs_diff_capture=round(abs(mb - fb), 4)))
out = dict(executed_local=pd.Timestamp.now(tz="America/New_York").isoformat(), python=platform.python_version(), pandas=pd.__version__, clean_dir=str(CLEAN), runs=runs, table_comparisons=cmp,
           node_hub_vs_frozen_panel=x, max_abs_diff_vs_frozen=max(r["abs_diff_capture"] for r in x),
           note="Script 01 (price extraction) was not re-run in the clean directory; its delivered outputs are checked against the frozen panel table. 2024 compared on the Feb-29-excluded calendar used by the panel. No regression, bootstrap or weather simulation was run.")
json.dump(out, open(SUP / "Verification.json", "w"), indent=1, default=str)
print(json.dumps({k: out[k] for k in ("runs", "table_comparisons", "max_abs_diff_vs_frozen")}, indent=1, default=str))
