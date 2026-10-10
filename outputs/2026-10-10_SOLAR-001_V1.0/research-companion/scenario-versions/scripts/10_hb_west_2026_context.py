"""Post-RTC+B context: HB_WEST 15-minute RTM prices January-September 2026 (ERCOT NP6-785-ER 2026 year-to-date file, no login),
compared with the same months of 2025. Solar weighting uses the 2025 simulated site profile mapped by local month-day-interval
(fixed CST key, as in the frozen empirical build) because no 2026 weather/energy series exists - a profile-weighted hub price,
not an observed capture price. Hub only: the resource node TAYGETE2_ALL is not in this product (see Free-Login-Source-Guide).
Usage: 10_hb_west_2026_context.py <project_root> <out_csv>"""
import io, sys, zipfile
from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2])
z = zipfile.ZipFile(ROOT / "Data/raw/2026-10-09_Finance-Deepening/followup/rpt.00013061.20261004.RTMLZHBSPP_2026.zip")
x = pd.ExcelFile(io.BytesIO(z.read(z.namelist()[0])))
frames = []
for s in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]:
    d = pd.read_excel(x, sheet_name=s); d = d[d["Settlement Point Name"] == "HB_WEST"]; frames.append(d)
d = pd.concat(frames)
local = pd.to_datetime(d["Delivery Date"], format="%m/%d/%Y") + pd.to_timedelta(d["Delivery Hour"].astype(int) - 1, unit="h") + pd.to_timedelta((d["Delivery Interval"].astype(int) - 1) * 15, unit="min")
d["utc"] = local.dt.tz_localize("America/Chicago", ambiguous=(d["Repeated Hour Flag"] != "Y").to_numpy(), nonexistent="raise").dt.tz_convert("UTC")
d = d.drop_duplicates("utc")
iv = pd.read_csv(ROOT / "Deliverables/2026-10-09_Finance-Scenario-Versions/data/Node-Hub-Intervals-2023-2025.csv.gz", parse_dates=["interval_start_utc"])
e25 = iv[iv.year == 2025].copy()
key = lambda u: (u.dt.tz_convert("Etc/GMT+6").dt.month * 100000 + u.dt.tz_convert("Etc/GMT+6").dt.day * 1000 + u.dt.tz_convert("Etc/GMT+6").dt.hour * 4 + u.dt.tz_convert("Etc/GMT+6").dt.minute // 15)
e25["k"] = key(e25.interval_start_utc); d["k"] = key(d.utc)
w = e25.set_index("k").energy_mwh
d["w"] = d.k.map(w); d["p"] = d["Settlement Point Price"].astype(float)
rows = []
for label, g26, g25 in [(f"{m:02d}", d[d.utc.dt.tz_convert("Etc/GMT+6").dt.month == m], e25[e25.interval_start_utc.dt.tz_convert("Etc/GMT+6").dt.month == m]) for m in range(1, 10)] + [("Jan-Sep", d, e25[e25.interval_start_utc.dt.tz_convert("Etc/GMT+6").dt.month <= 9])]:
    g26 = g26.dropna(subset=["w"]); g25 = g25.dropna(subset=["p_hub"])
    for yr, p, ww in [(2026, g26.p.to_numpy(), g26.w.to_numpy()), (2025, g25.p_hub.to_numpy(), g25.energy_mwh.to_numpy())]:
        rows.append(dict(period=label, year=yr, intervals=len(p), time_weighted_usd_mwh=p.mean(), profile_weighted_usd_mwh=(p * ww).sum() / ww.sum(), ratio=(p * ww).sum() / ww.sum() / p.mean(),
                         negative_interval_share=(p < 0).mean(), profile_energy_share_negative=ww[p < 0].sum() / ww.sum(),
                         basis="2026 = post-RTC+B prices weighted by the 2025 simulated profile; 2025 = same-year profile (pre-RTC+B for Jan-Sep)"))
out = pd.DataFrame(rows); out.to_csv(OUT, index=False, float_format="%.4f"); print(out[out.period == "Jan-Sep"].round(3).to_string()); print(out.round(2).to_string())
