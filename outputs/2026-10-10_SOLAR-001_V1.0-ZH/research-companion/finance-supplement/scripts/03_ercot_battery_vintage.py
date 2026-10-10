"""Cumulative ERCOT (BA code ERCO) battery nameplate by operating year, from EIA-860 2025 final (3_4_Energy_Storage x 2___Plant).
Survivor-based: counts units with Status OP at end-2025 by their first operating year; retired/derated units before 2025 are not included.
Descriptive background only; no causal interpretation."""
import io, sys, zipfile
import pandas as pd
z = zipfile.ZipFile(sys.argv[1]); rd = lambda pre: pd.read_excel(io.BytesIO(z.read([n for n in z.namelist() if n.startswith(pre)][0])), header=1)
s = rd("3_4_Energy_Storage").merge(rd("2___Plant")[["Plant Code", "Balancing Authority Code"]], on="Plant Code")
s = s[(s["Balancing Authority Code"] == "ERCO") & (s["Prime Mover"] == "BA") & (s.Status == "OP")]
rows = [dict(year_end=y, cumulative_operating_battery_mw=s[s["Operating Year"] <= y]["Nameplate Capacity (MW)"].sum(), cumulative_operating_battery_mwh=s[s["Operating Year"] <= y]["Nameplate Energy Capacity (MWh)"].sum(),
             units=int((s["Operating Year"] <= y).sum()), basis="EIA-860 2025 final; survivors with Status OP; by Operating Year") for y in range(2019, 2026)]
pd.DataFrame(rows).to_csv(sys.argv[2], index=False, float_format="%.1f"); print(pd.DataFrame(rows))
