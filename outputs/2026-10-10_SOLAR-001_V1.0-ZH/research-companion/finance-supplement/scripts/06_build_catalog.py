"""Build Sources.csv / Source-Catalog.csv from every fetch receipt under Data/raw/2026-10-09_Finance-Deepening plus the earlier-retained files this
supplement re-used, re-hash every local file, and attach url / retrieval time / SHA-256 to Project-Finance-Input-Evidence.csv.
Usage: 06_build_catalog.py <project_root> <supplement_dir>"""
import csv, glob, hashlib, sys
from pathlib import Path
import pandas as pd

ROOT = Path(sys.argv[1]); SUP = Path(sys.argv[2]); RAW = ROOT / "Data/raw/2026-10-09_Finance-Deepening"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

LIMITS = {"tax": "Official legal text (public domain) or court record; LII copy is a secondary rendering of the U.S. Code; not tax advice",
          "EIA": "U.S. government data (public domain); annual final releases may be revised",
          "ERCOT": "ERCOT/PUCT public material; ERCOT terms of use apply; reference only",
          "comparables": "Public records of the Texas Comptroller and ERCOT; self-reported filings; not audited cost",
          "comparables-added": "Company press releases and trade press (secondary where marked); copyright - quote briefly only",
          "PPA": "Trade-press reports of a paywalled index (secondary); LevelTen post is the publisher's public summary",
          "property-tax": "Texas Comptroller public web pages",
          "solar-weights-reused": "Project-internal simulated weights reused unchanged from the 2026-10-08 empirical build"}
rows = []
for rec in sorted(glob.glob(str(RAW / "*/*receipts*.csv"))):
    sub = Path(rec).parent.name
    for r in csv.DictReader(open(rec, encoding="utf-8")):
        lf = r.get("local_file", "").strip()
        p = Path(rec).parent / lf if lf else None
        exists = bool(lf) and p.exists()
        rows.append(dict(source_id=r.get("source_id", ""), title=r.get("title", r.get("project", "")), publisher=r.get("publisher", ""), url=r.get("url", ""),
                         local_file=str(p.relative_to(ROOT)) if p else "", retrieved_utc=r.get("retrieved_utc", ""), http_status=r.get("http_status", ""),
                         sha256_receipt=r.get("sha256", ""), sha256_now=sha(p) if exists else "", file_present=exists,
                         hash_match=(sha(p) == r.get("sha256", "")) if exists and r.get("sha256") else "", use_limits=LIMITS.get(sub, ""), retained_in_round="2026-10-09 finance deepening"))
# earlier-retained files re-used here (not re-downloaded)
REUSED = [
    ("PRIOR-NP6-905-2023", "Data/raw/2026-10-08_Deep-Report-Supplement/B_ERCOT-Nodes/NP6-905-CD-2023", "ERCOT NP6-905-CD monthly archives 2023"),
    ("PRIOR-NP6-905-2024", "Data/raw/2026-10-08_Deep-Report-Supplement/B_ERCOT-Nodes/NP6-905-CD-2024", "ERCOT NP6-905-CD monthly archives 2024"),
    ("PRIOR-NP6-905-2025", "Data/raw/2026-10-07_Scenario-and-Sensitivity/ERCOT-NP6-905-CD-2025", "ERCOT NP6-905-CD monthly archives 2025"),
    ("PRIOR-NP4-160-2026-09", "Data/raw/2026-09-24/US/ERCOT/RPT.00010008.20260923.CIM_Sep_ML3_1_09302026_SP_List_and_EB_Mapping.zip", "ERCOT NP4-160 settlement points and electrical bus mapping (Sep 2026)"),
    ("PRIOR-EIA-923-2024", "Data/raw/2026-08-25/US/EIA/2024_EIA-923_final.zip", "EIA-923 2024 final"),
    ("PRIOR-ATB-2025-PV-page", "Data/raw/2026-10-07_ATB-Method-Trace/County-Trace/atb2025_utility_pv.html", "NREL/NLR ATB 2025 utility-scale PV page"),
    ("PRIOR-PVSCM-2024", "Data/raw/2026-10-08_Deep-Report-Supplement/A_US-Cost-Trade/A06__NLR_PVSCM_2024.zip", "NLR PV System Cost Model 2024 (UPV 2024Q1 parameters)"),
    ("PRIOR-PVSCM-2025Q1", "Data/raw/2026-10-08_Deep-Report-Supplement/A_US-Cost-Trade/A05__NLR_2025Q1_PV_System_Cost_Benchmark_Model.zip", "NLR 2025Q1 PV System Cost Benchmark Model"),
    ("PRIOR-LBNL-USS-2025-ES", "Data/raw/2026-10-08_Deep-Report-Supplement/A_US-Cost-Trade/A02__LBNL_USS_2025_DataUpdate_ExecSummary.pdf", "Berkeley Lab Utility-Scale Solar 2025 Data Update executive summary"),
    ("PRIOR-LBNL-USS-2025-SL", "Data/raw/2026-10-08_Deep-Report-Supplement/A_US-Cost-Trade/A01__LBNL_USS_2025_Slides.pdf", "Berkeley Lab Utility-Scale Solar 2025 slides"),
    ("PRIOR-BLS-CPI", "Data/raw/2026-10-07_Scenario-and-Sensitivity/BLS/CUUR0000SA0_2022-2025_api_v2.json", "BLS CPI-U annual averages 2022-2025"),
    ("PRIOR-ATB-OPEX-TWB", "Data/raw/2026-10-07_ATB-Method-Trace/County-Trace/2025 OPEX.twb", "ATB 2025 OPEX Tableau workbook definition (item dictionary only)")]
for sid, rel, title in REUSED:
    p = ROOT / rel
    files = sorted(p.glob("*.zip")) if p.is_dir() else [p]
    for f in files:
        rows.append(dict(source_id=sid, title=title, publisher="see earlier SOLAR-001 source catalogs", url="see earlier catalog for this retained file", local_file=str(f.relative_to(ROOT)), retrieved_utc="retained before 2026-10-09",
                         http_status="", sha256_receipt="", sha256_now=sha(f) if f.exists() else "", file_present=f.exists(), hash_match="", use_limits="Previously retained; unchanged; re-hashed in this round", retained_in_round="earlier round (re-used)"))
cat = pd.DataFrame(rows)
for name in ("Sources.csv", "Source-Catalog.csv"):
    cat.to_csv(SUP / name, index=False)
ev = pd.read_csv(ROOT / "Analysis/2026-10-09_Finance-Deepening/Claude-Research/inputs/Project-Finance-Input-Evidence.src.csv")
look = {r["local_file"]: r for r in rows if r["local_file"]}
def attach(lf, key):
    first = str(lf).split(";")[0].strip()
    if first.startswith("Deliverables/"):
        return {"url": "derived in this supplement", "retrieved_utc": "", "sha256": sha(ROOT / first) if (ROOT / first).exists() else ""}[key]
    r = look.get(first)
    if r is None:
        return ""
    return {"url": r["url"], "retrieved_utc": r["retrieved_utc"], "sha256": r["sha256_now"]}[key]
for k in ("url", "retrieved_utc", "sha256"):
    ev[k] = ev.local_file.map(lambda x: attach(x, k))
ev.to_csv(SUP / "Project-Finance-Input-Evidence.csv", index=False)
print(len(cat), "catalog rows;", int((~cat.file_present.astype(bool)).sum()), "missing files;", int((cat.hash_match == False).sum()), "hash mismatches;",
      int((ev.sha256 == "").sum()), "evidence rows without a hashed source")
