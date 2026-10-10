"""Compare data plotted in the V0.999-R1 exhibits with the upstream plot-data snapshots (lines, bars, scatter offsets, images).
Usage: python3 build/check_figures.py --upstream <dir with Figure-Plot-Data-Snapshot.json etc.> [--figures DIR] [--out FILE]"""
import argparse, json
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument("--upstream", required=True); ap.add_argument("--figures", default=str(PKG / "figures")); ap.add_argument("--out", default=str(PKG / "records/Figure-Data-Check.json")); a = ap.parse_args()
new = json.loads((Path(a.figures) / "Figure-Plot-Data.json").read_text())
old = {}
for f in ["Figure-Plot-Data-Snapshot.json", "Finance-Chart-Snapshots.json"]:
    p = Path(a.upstream) / f
    if p.exists(): old.update({k.replace("empirical/", "empirical_"): v for k, v in json.loads(p.read_text()).items()})
import math
def same(x, y):
    if isinstance(x, dict) and isinstance(y, dict): return x.keys() == y.keys() and all(same(x[k], y[k]) for k in x)
    if isinstance(x, list) and isinstance(y, list): return len(x) == len(y) and all(same(a, b) for a, b in zip(x, y))
    if isinstance(x, float) or isinstance(y, float): return math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-9)  # summation-order rounding only
    return x == y
def data(ax):
    return {k: ax[k] for k in ("lines", "rects", "scatter", "images")}
res = {}
for k, v in sorted(new.items()):
    if k.startswith("R1_"): res[k] = "R1 exhibit (no upstream counterpart); values from Table 1-2 and data/r1/"; continue
    if k not in old: res[k] = "no upstream snapshot; drawn by unchanged upstream code from byte-identical data tables"; continue
    o = old[k]
    if len(o) != len(v): res[k] = f"MISMATCH: axes {len(o)} vs {len(v)}"; continue
    bad = [i for i, (x, y) in enumerate(zip(o, v)) if not same(data(x), data(y))]
    res[k] = "identical plotted data" if not bad else f"MISMATCH in axes {bad}"
Path(a.out).parent.mkdir(parents=True, exist_ok=True); Path(a.out).write_text(json.dumps(res, indent=1))
for k, v in res.items(): print(f"{k:55s} {v}")
print("mismatches:", sum(v.startswith("MISMATCH") for v in res.values()))
raise SystemExit(1 if any(v.startswith("MISMATCH") for v in res.values()) else 0)
