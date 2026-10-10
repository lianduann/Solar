"""Interval-level TAYGETE2_ALL and HB_WEST 15-minute RTM prices (2023-2025) joined to the existing same-year site-energy weights,
for the separately versioned VPPA and CPI scenarios. Reuses the extraction rule of 01_node_hub_capture.py unchanged (imported).
For 2025 it also joins the frozen interval_energy_price_2025.csv and asserts the node price equals the frozen model's price.
Usage: 08_extract_node_hub_intervals.py <project_root> <out_csv_gz>"""
import importlib.util, sys
from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("nh", ROOT / "Analysis/2026-10-09_Finance-Deepening/Claude-Research/scripts/01_node_hub_capture.py"); nh = importlib.util.module_from_spec(spec); spec.loader.exec_module(nh)
nh.POINTS = ["TAYGETE2_ALL", "HB_WEST"]
R = ROOT / "Data/raw"; arch = {2023: R / "2026-10-08_Deep-Report-Supplement/B_ERCOT-Nodes/NP6-905-CD-2023", 2024: R / "2026-10-08_Deep-Report-Supplement/B_ERCOT-Nodes/NP6-905-CD-2024", 2025: R / "2026-10-07_Scenario-and-Sensitivity/ERCOT-NP6-905-CD-2025"}
frames = []
for Y, d in arch.items():
    wide, rec = nh.extract(d, Y); z = np.load(R / "2026-10-09_Finance-Deepening/solar-weights-reused" / f"energy15_{Y}.npz")
    assert (pd.to_datetime(z["utc"], utc=True) == wide.index).all()
    f = pd.DataFrame({"year": Y, "interval_start_utc": wide.index, "p_node": wide["TAYGETE2_ALL"].to_numpy(), "p_hub": wide["HB_WEST"].to_numpy(), "energy_mwh": z["mwh"].astype(float)})
    frames.append(f); print(Y, rec["duplicate_rows_dropped"], "dups;", int(f.p_node.isna().sum()), "node NaN;", int(f.p_hub.isna().sum()), "hub NaN")
out = pd.concat(frames, ignore_index=True)
fz = pd.read_csv(ROOT / "Deliverables/2026-10-09_Panel-Revision-Client-Edition/data/interval_energy_price_2025.csv")
fz["interval_start_utc"] = pd.to_datetime(fz.interval_start_utc, utc=True)
m = out[out.year == 2025].merge(fz[["interval_start_utc", "energy_mwh_base", "price_usd_mwh", "price_available"]], on="interval_start_utc", how="left")
ok = m.price_available.fillna(False).astype(bool)
assert np.allclose(m.loc[ok, "p_node"], m.loc[ok, "price_usd_mwh"], atol=1e-6), "node price differs from frozen 2025 interval file"
assert np.allclose(m.energy_mwh, m.energy_mwh_base, atol=1e-6), "energy differs from frozen 2025 interval file"
print("2025 node price and energy identical to frozen interval_energy_price_2025.csv on", int(ok.sum()), "priced intervals")
out.to_csv(OUT, index=False, float_format="%.6f", compression="gzip"); print(len(out), "rows ->", OUT)
