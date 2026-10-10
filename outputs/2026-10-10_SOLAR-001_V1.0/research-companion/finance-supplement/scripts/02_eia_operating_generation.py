"""EIA-860 (2025 final) x EIA-923 (2023 final revision, 2024 final, 2025 final) operating-generation comparables for West Texas PV.

Sanity check only: different plants, weather, DC/AC ratios, curtailment and equipment; no calibration of the hypothetical 100 MWac / 132 MWdc case.
Capacity factor denominator = AC nameplate of PV generators in service for the whole month (operating month/year strictly before the month)
x calendar hours of the month (leap February 2024 = 696 h; DST ignored because EIA monthly MWh are calendar-month totals).
The COD month is flagged partial and excluded from CF. Annual CF is computed only when all 12 months are full in-service months with the same
capacity. Plants with storage at site (EIA-860 Plant 'Energy Storage' = Y, or an Energy_Storage generator) or a 'Hybrid' name are flagged.
EIA-923 'Respondent Frequency' A = annual respondent whose monthly values are EIA-imputed/allocated; flagged.
"""
import argparse, io, zipfile
from pathlib import Path
import numpy as np, pandas as pd

COUNTIES = {"Pecos": "same county", "Reeves": "adjacent", "Ward": "adjacent", "Crane": "adjacent", "Upton": "adjacent", "Crockett": "adjacent", "Terrell": "adjacent",
            "Brewster": "adjacent", "Jeff Davis": "adjacent", "Winkler": "nearby", "Ector": "nearby", "Andrews": "nearby", "Reagan": "nearby", "Loving": "nearby", "Midland": "nearby",
            "Concho": "other ERCOT (Ch313 comparable)", "Tom Green": "other ERCOT (Ch313 comparable)", "Runnels": "other ERCOT (Ch313 comparable)"}
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def xl(zpath, member_prefix, **kw):
    with zipfile.ZipFile(zpath) as z:
        name = [n for n in z.namelist() if n.startswith(member_prefix)][0]
        return pd.read_excel(io.BytesIO(z.read(name)), **kw), name


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--eia860", required=True); ap.add_argument("--eia923", nargs=3, required=True, help="2023 2024 2025 zips"); ap.add_argument("--out", required=True)
    a = ap.parse_args(); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    sol, _ = xl(a.eia860, "3_3_Solar", header=1); plant, _ = xl(a.eia860, "2___Plant", header=1); sto, _ = xl(a.eia860, "3_4_Energy_Storage", header=1)
    sol = sol[(sol.State == "TX") & sol.County.isin(COUNTIES) & (sol["Prime Mover"] == "PV")].copy()
    sol["cap"] = pd.to_numeric(sol["Nameplate Capacity (MW)"], errors="coerce"); sol["dc"] = pd.to_numeric(sol["DC Net Capacity (MW)"], errors="coerce")
    sol["start"] = pd.to_datetime(dict(year=sol["Operating Year"], month=sol["Operating Month"], day=1))
    pl = plant.set_index("Plant Code")
    sto_codes = set(sto[sto.State == "TX"]["Plant Code"])
    gens = sol[["Plant Code", "Plant Name", "County", "Generator ID", "Status", "cap", "dc", "start", "Single-Axis Tracking?", "Bifacial?", "Utility Name"]]
    gens.to_csv(out / "EIA-860-2025_WestTX_PV_generators.csv", index=False)
    rows = []
    for Y, z in zip((2023, 2024, 2025), a.eia923):
        g, member = xl(z, "EIA923_Schedules_2_3_4_5", sheet_name="Page 1 Generation and Fuel Data", header=5)
        g.columns = [c.replace("\n", " ") for c in g.columns]
        g = g[(g["Plant State"] == "TX") & (g["Reported Prime Mover"] == "PV") & g["Plant Id"].isin(sol["Plant Code"])]
        for pid, gg in g.groupby("Plant Id"):
            gp = gens[gens["Plant Code"] == pid]
            for mi, M in enumerate(MONTHS, 1):
                ms = pd.Timestamp(Y, mi, 1); hours = ms.days_in_month * 24
                full_cap = gp[gp.start < ms].cap.sum(); any_cod_this_month = bool((gp.start == ms).any())
                ng = pd.to_numeric(gg[f"Netgen {M}"], errors="coerce").sum(min_count=1)
                rows.append(dict(year=Y, month=mi, plant_id=int(pid), plant_name=gp["Plant Name"].iloc[0], county=gp.County.iloc[0], proximity=COUNTIES[gp.County.iloc[0]],
                                 utility_2025=gp["Utility Name"].iloc[0], latitude=pl.loc[pid, "Latitude"], longitude=pl.loc[pid, "Longitude"], ba=pl.loc[pid, "Balancing Authority Code"],
                                 respondent_frequency="/".join(sorted(gg["Respondent Frequency"].astype(str).unique())), net_generation_mwh=ng, hours=hours,
                                 inservice_full_month_mwac=full_cap, mwdc_total_2025=gp.dc.sum(), mwac_total_2025=gp.cap.sum(), cod_month_flag=any_cod_this_month,
                                 capacity_factor_ac=(ng / (full_cap * hours)) if (full_cap > 0 and not any_cod_this_month and pd.notna(ng)) else np.nan,
                                 storage_at_site=(pl.loc[pid, "Energy Storage"] == "Y") or (pid in sto_codes) or ("Hybrid" in str(gp["Plant Name"].iloc[0])),
                                 multi_generator=len(gp) > 1, first_cod=gp.start.min().strftime("%Y-%m"), last_cod=gp.start.max().strftime("%Y-%m"),
                                 tracking=",".join(sorted(gp["Single-Axis Tracking?"].fillna("N").astype(str).unique())), eia923_member=member))
    m = pd.DataFrame(rows); m.to_csv(out / "EIA-Operating-Generation-Monthly-2023-2025.csv", index=False, float_format="%.5f")
    ann = []
    for (Y, pid), d in m.groupby(["year", "plant_id"]):
        full = d.capacity_factor_ac.notna().all() and d.inservice_full_month_mwac.nunique() == 1
        hrs = d.hours.sum(); ng = d.net_generation_mwh.sum(min_count=12)
        r = d.iloc[0]
        cls = []
        if r.storage_at_site: cls.append("storage-hybrid site")
        if r.multi_generator: cls.append("multi-generator aggregate")
        if not full: cls.append("partial year / new or expanded capacity")
        if "A" in r.respondent_frequency: cls.append("annual respondent (monthly values allocated by EIA)")
        ann.append(dict(year=Y, plant_id=pid, plant_name=r.plant_name, county=r.county, proximity=r.proximity, mwac_2025=r.mwac_total_2025, mwdc_2025=r.mwdc_total_2025,
                        dc_ac_ratio=r.mwdc_total_2025 / r.mwac_total_2025, first_cod=r.first_cod, last_cod=r.last_cod, tracking=r.tracking, months_reported=int(d.net_generation_mwh.notna().sum()),
                        full_year_constant_capacity=bool(full), annual_net_generation_mwh=ng, hours=hrs, leap_year=(Y == 2024),
                        annual_capacity_factor_ac=(ng / (d.inservice_full_month_mwac.iloc[0] * hrs)) if full else np.nan,
                        flags="; ".join(cls) if cls else "clean full-year standalone PV", respondent_frequency=r.respondent_frequency))
    A = pd.DataFrame(ann).sort_values(["plant_name", "year"]); A.to_csv(out / "EIA-Operating-Generation-Comparables.csv", index=False, float_format="%.5f")
    print(A[["year", "plant_name", "county", "mwac_2025", "dc_ac_ratio", "first_cod", "annual_capacity_factor_ac", "flags"]].round(4).to_string())


if __name__ == "__main__":
    main()
