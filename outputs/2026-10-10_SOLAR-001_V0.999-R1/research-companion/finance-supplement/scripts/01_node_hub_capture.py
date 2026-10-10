"""Node-hub solar capture and basis, 2023-2025, from the retained NP6-905-CD monthly archives (15-minute RTM settlement point prices).

Inputs (read-only):
  * retained NP6-905-CD archives (2023, 2024: Data/raw/2026-10-08_Deep-Report-Supplement/B_ERCOT-Nodes/NP6-905-CD-YYYY;
    2025: Data/raw/2026-10-07_Scenario-and-Sensitivity/ERCOT-NP6-905-CD-2025)
  * existing same-year 15-minute site energy weights energy15_YYYY.npz (hypothetical 100 MWac / 132 MWdc PVWatts design at the
    retained Pecos NSRDB gid), copied unchanged into Data/raw/2026-10-09_Finance-Deepening/solar-weights-reused/.
Rules (same as the frozen empirical build): local CPT interval start = DeliveryDate + (DeliveryHour-1) h + (DeliveryInterval-1)*15 min;
DSTFlag=='Y' marks the repeated fall-back hour; converted to UTC; kept only inside the local calendar year; exact duplicate rows dropped;
names published under two settlement-point types are kept separately as NAME__TYPE. No interpolation; an interval enters the common
calendar only if every selected point is priced. Energy is the variant-A series (Feb 29 2024 simulated with Feb 28 geometry).
No regression, no model run.
"""
import argparse, csv, hashlib, io, json, zipfile
from pathlib import Path
import numpy as np, pandas as pd

POINTS = ["TAYGETE2_ALL", "HB_WEST", "HB_BUSAVG", "HB_HUBAVG", "LZ_WEST"]
HDR = ["DeliveryDate", "DeliveryHour", "DeliveryInterval", "SettlementPointName", "SettlementPointType", "SettlementPointPrice", "DSTFlag"]
RTCB_UTC = pd.Timestamp("2025-12-05 06:00", tz="UTC")  # operating day 2025-12-05 00:00 CST; go-live date cited in Source-Catalog (ERCOT RTC+B)


def extract(archdir, year):
    recs, arch = [], []
    for p in sorted(Path(archdir).glob("*.zip")):
        b = p.read_bytes(); arch.append({"file": p.name, "sha256": hashlib.sha256(b).hexdigest(), "bytes": len(b)})
        with zipfile.ZipFile(io.BytesIO(b)) as outer:
            for m in outer.infolist():
                with zipfile.ZipFile(io.BytesIO(outer.read(m))) as inner:
                    for it in inner.infolist():
                        rd = csv.reader(io.StringIO(inner.read(it).decode("utf-8-sig"))); hdr = next(rd); assert hdr == HDR, hdr
                        recs.extend(r for r in rd if r[3] in POINTS)
    df = pd.DataFrame(recs, columns=["d", "h", "i", "name", "type", "price", "dst"]); df["price"] = df.price.astype(float)
    local = pd.to_datetime(df.d, format="%m/%d/%Y") + pd.to_timedelta(df.h.astype(int) - 1, unit="h") + pd.to_timedelta((df.i.astype(int) - 1) * 15, unit="min")
    df["utc"] = local.dt.tz_localize("America/Chicago", ambiguous=(df.dst != "Y").to_numpy(), nonexistent="raise").dt.tz_convert("UTC")
    full = pd.date_range(pd.Timestamp(f"{year}-01-01", tz="America/Chicago").tz_convert("UTC"), pd.Timestamp(f"{year+1}-01-01", tz="America/Chicago").tz_convert("UTC"), freq="15min", inclusive="left")
    df = df[df.utc.isin(full)]
    multi = df.groupby("name").type.nunique(); multi = set(multi[multi > 1].index)
    df["key"] = np.where(df.name.isin(multi), df.name + "__" + df.type, df.name)
    conflicts = int((df[df.duplicated(["key", "utc"], keep=False)].groupby(["key", "utc"]).price.nunique() > 1).sum())
    ndup = int(df.duplicated(["key", "utc"]).sum()); df = df.drop_duplicates(["key", "utc"])
    wide = df.pivot(index="utc", columns="key", values="price").reindex(full)
    return wide, dict(year=year, archives=arch, rows_kept=len(df), duplicate_rows_dropped=ndup, duplicate_conflicting_price=conflicts, split_names=sorted(multi), expected_intervals=len(full),
                      dst_flag_Y_rows=int((df.dst == "Y").sum()))


def metrics(wide, e, label, mask):
    out = []
    w = wide[mask]; g = e[mask]
    for k in wide.columns:
        p = w[k].to_numpy(); n = len(p)
        tw = p.mean(); gw = (p * g).sum() / g.sum()
        out.append(dict(period=label, point=k, common_intervals=n, energy_mwh=round(g.sum(), 3), time_weighted_usd_mwh=tw, generation_weighted_usd_mwh=gw, capture_ratio=gw / tw,
                        negative_price_interval_share=(p < 0).mean(), energy_share_in_negative_price_intervals=g[p < 0].sum() / g.sum(),
                        max_usd_mwh=p.max(), min_usd_mwh=p.min()))
    return out


def basis(wide, e, label, mask, node, hub):
    w = wide[mask]; g = e[mask]; d = (w[node] - w[hub]).to_numpy()
    return dict(period=label, node=node, hub=hub, common_intervals=len(d), time_weighted_basis_usd_mwh=d.mean(), generation_weighted_basis_usd_mwh=(d * g).sum() / g.sum(),
                generation_weighted_abs_basis_usd_mwh=(np.abs(d) * g).sum() / g.sum(), share_solar_mwh_with_node_below_hub=g[d < 0].sum() / g.sum(),
                p05_basis_solar_intervals=np.percentile(d[g > 0], 5), p50_basis_solar_intervals=np.percentile(d[g > 0], 50), p95_basis_solar_intervals=np.percentile(d[g > 0], 95))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--arch", nargs=3, required=True, help="dirs for 2023 2024 2025"); ap.add_argument("--energy", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args(); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows, brows, rec, cal = [], [], [], []
    for Y, d in zip((2023, 2024, 2025), a.arch):
        wide, r = extract(d, Y); z = np.load(Path(a.energy) / f"energy15_{Y}.npz")
        assert (pd.to_datetime(z["utc"], utc=True) == wide.index).all(); e = z["mwh"].astype(float)
        cols = [c for c in wide.columns if c in POINTS or c.startswith("LZ_WEST__LZ")]
        cols = [c for c in cols if c != "LZ_WEST__LZEW"]; wide = wide[cols]
        allp = wide.notna().all(axis=1).to_numpy()
        r.update(points=list(wide.columns), priced_by_point={c: int(wide[c].notna().sum()) for c in wide.columns}, common_intervals=int(allp.sum()), excluded_intervals_missing_any_point=int((~allp).sum()),
                 energy_total_mwh=float(e.sum()), energy_in_excluded_intervals_mwh=float(e[~allp].sum()))
        rec.append(r)
        periods = [(str(Y), allp)]
        if Y == 2025:
            periods += [("2025_pre_RTCB", allp & (wide.index < RTCB_UTC)), ("2025_post_RTCB_Dec5-31", allp & (wide.index >= RTCB_UTC))]
        if Y == 2024:
            c = wide.index.tz_convert("Etc/GMT+6"); periods += [("2024_excl_Feb29", allp & ~((c.month == 2) & (c.day == 29)))]
        for lab, m in periods:
            rows += metrics(wide, e, lab, m)
            for hub in [h for h in wide.columns if h != "TAYGETE2_ALL"]:
                brows.append(basis(wide, e, lab, m, "TAYGETE2_ALL", hub))
        # monthly for 2023-2025 (common calendar only)
        mo = wide.index.tz_convert("America/Chicago").month
        for M in range(1, 13):
            m = allp & (mo == M)
            for x in metrics(wide, e, f"{Y}-{M:02d}", m): cal.append(x)
    pd.DataFrame(rows).to_csv(out / "Node-Hub-Solar-Capture-2023-2025.csv", index=False, float_format="%.4f")
    pd.DataFrame(brows).to_csv(out / "Node-Hub-Basis-2023-2025.csv", index=False, float_format="%.4f")
    pd.DataFrame(cal).to_csv(out / "Node-Hub-Solar-Capture-Monthly-2023-2025.csv", index=False, float_format="%.4f")
    json.dump(rec, open(out / "node_hub_extraction_receipt.json", "w"), indent=1)
    print(pd.DataFrame(rows)[["period", "point", "common_intervals", "time_weighted_usd_mwh", "generation_weighted_usd_mwh", "capture_ratio"]].round(3).to_string())
    print(pd.DataFrame(brows)[["period", "hub", "time_weighted_basis_usd_mwh", "generation_weighted_basis_usd_mwh", "share_solar_mwh_with_node_below_hub"]].round(3).to_string())


if __name__ == "__main__":
    main()
