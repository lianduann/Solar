"""Assemble the SOLAR-001 V1.0 client delivery package and the Lian Duan author edition, then verify both.

Inputs are the three rebuilt working copies (en-client, zh-client, en-liandian) and the delivered V1.0 / V1.0-ZH PDFs.
Writes the package folder, its ZIP, and Client-Package-Check.json; exits non-zero if any check fails."""
import hashlib, json, re, shutil, sys, zipfile
from pathlib import Path
import pymupdf

W = Path(__file__).resolve().parent
V10 = Path("/home/claude/work/v10/2026-10-10_SOLAR-001_V1.0")
V10ZH = Path("/home/claude/work/zh/2026-10-10_SOLAR-001_V1.0-ZH")
EN_PDF = "SOLAR-001_V1.0_Integrated-Market-Research-Report-EN.pdf"
ZH_PDF = "SOLAR-001_V1.0_Integrated-Market-Research-Report-ZH.pdf"
OUT = W / "out"
PKG_NAME = "SOLAR-001_Client-Delivery_V1.0_2026-10-10"
PKG = OUT / PKG_NAME
AUTHOR_PDF = "SOLAR-001_Market-Research-Report_V1.0_EN_Lian-Duan.pdf"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
BOM = b"\xef\xbb\xbf"

shutil.rmtree(OUT, ignore_errors=True); PKG.mkdir(parents=True)
(PKG / "00_README.txt").write_bytes(BOM + (W / "00_README.txt").read_bytes())
shutil.copy2(W / "en-client" / EN_PDF, PKG / "01_SOLAR-001_Market-Research-Report_V1.0_EN.pdf")
shutil.copy2(W / "zh-client" / ZH_PDF, PKG / "02_SOLAR-001_Market-Research-Report_V1.0_ZH.pdf")
shutil.copytree(W / "fig-export", PKG / "03_Figures")
shutil.copytree(W / "en-client" / "04_Source-Documents", PKG / "04_Source-Documents")
sd = PKG / "05_Supporting-Data"; sd.mkdir()
for name, src in [("Supplier-Liquidity_FY2025-FY2024.csv", V10 / "research-companion/closure-evidence/tables/FIN-09_Supplier-Liquidity.csv"),
                  ("EIA-Cohort-Reconciliation.csv", V10 / "data/finance/EIA-Cohort-Reconciliation.csv"),
                  ("Storage-Screen.csv", V10 / "data/r1/Storage-Screen.csv"),
                  ("Storage-Cost.csv", V10 / "data/r1/Storage-Cost.csv")]:
    b = src.read_bytes()
    (sd / name).write_bytes(BOM + b if re.search(rb"[\x80-\xff]", b) else b)  # BOM so spreadsheet programs read the Chinese field labels
shutil.copy2(W / "en-liandian" / EN_PDF, OUT / AUTHOR_PDF)

rec, ok = {}, True
def check(name, cond, detail=None):
    global ok
    rec[name] = {"pass": bool(cond), **({"detail": detail} if detail is not None else {})}
    ok &= bool(cond)

def same_text(a, b):
    A, B = pymupdf.open(a), pymupdf.open(b)
    ws = lambda t: "\n".join(l.rstrip() for l in t.splitlines())  # unlinked phrases can drop a trailing space at a line end
    diff = [i + 1 for i in range(min(len(A), len(B))) if ws(A[i].get_text()) != ws(B[i].get_text())]
    ws_only = [i + 1 for i in range(min(len(A), len(B))) if A[i].get_text() != B[i].get_text() and i + 1 not in diff]
    return len(A), len(B), diff, A.get_toc() == B.get_toc(), ws_only

def file_links(p):
    return [(i + 1, l.get("file") or l.get("uri")) for i, pg in enumerate(pymupdf.open(p)) for l in pg.get_links() if l["kind"] in (pymupdf.LINK_GOTOR, pymupdf.LINK_LAUNCH)]

# client PDFs: same text and bookmarks as the delivered V1.0 PDFs; every file link resolves inside the package
for tag, new, old in [("EN", PKG / "01_SOLAR-001_Market-Research-Report_V1.0_EN.pdf", V10 / EN_PDF),
                      ("ZH", PKG / "02_SOLAR-001_Market-Research-Report_V1.0_ZH.pdf", V10ZH / ZH_PDF)]:
    n_new, n_old, diff, toc, ws_only = same_text(new, old)
    check(f"{tag} client PDF: pages, per-page text (line by line) and bookmarks identical to delivered V1.0", n_new == n_old and not diff and toc,
          {"pages": n_new, "pages_V1.0": n_old, "pages_with_text_difference": diff, "pages_with_trailing_space_difference_only": ws_only})
    fl = file_links(new)
    missing = [f for _, f in fl if not (PKG / f).exists()]
    check(f"{tag} client PDF: file links resolve inside the package", fl and not missing,
          {"file_links": len(fl), "targets": sorted({f for _, f in fl}), "missing": missing})
    old_targets = {f for _, f in file_links(old)}
    check(f"{tag} client PDF: no link into research working files", not any("research-companion" in f for _, f in fl),
          {"V1.0 file links": len(file_links(old)), "unlinked (now plain text)": sorted(t for t in old_targets if not any(t.endswith(k) for k in
           ["FIN-09_Supplier-Liquidity.csv", "C06_ch313_1377_772_2025.pdf", "PUCT_16TAC_25.195_current.pdf", "PLAW-119publ21.pdf",
            "USCOURTS-dcd-1_25-cv-04400-0.pdf", "n-26-15.pdf"]))})

# source documents: byte-identical to the retained originals
lm = json.loads((W / "link_map.json").read_text())
check("source documents and supplier table byte-identical to retained originals (CSV: apart from the added UTF-8 BOM)",
      all(sha(V10 / "research-companion" / s) == sha(PKG / d) or (PKG / d).read_bytes() == BOM + (V10 / "research-companion" / s).read_bytes()
          for s, d in lm.items()))

# figures: 30, one per report figure
figs = sorted(p.name for p in (PKG / "03_Figures").glob("*.png"))
n_report_figs = len(re.findall(r"!\[Figure ", (V10 / "source/SOLAR-001_V1.0_Report-EN.md").read_text()))
check("figures: one PNG per report figure", len(figs) == n_report_figs == 30, {"png": len(figs), "report_figures": n_report_figs})

# package hygiene: nothing internal
names = [str(p.relative_to(PKG)) for p in PKG.rglob("*") if p.is_file()]
bad = [n for n in names if re.search(r"\.(py|json|md|sh|log)$|records|build|baseline|translation|research-companion|SHA256|MANIFEST", n, re.I)]
check("package contains no scripts, records, baselines or working files", not bad, {"files": len(names), "flagged": bad})

# author edition: no company name anywhere; only cover, back cover and footers differ from V1.0
A = pymupdf.open(OUT / AUTHOR_PDF); V = pymupdf.open(V10 / EN_PDF)
txt = "".join(p.get_text() for p in A)
meta = json.dumps(A.metadata) + (A.get_xml_metadata() or "")
raw = (OUT / AUTHOR_PDF).read_bytes()
check("author edition: no 'Lucid' / 'Direction Insights' in text, metadata or raw bytes",
      "lucid" not in (txt + meta).lower() and "direction insights" not in (txt + meta).lower() and b"Lucid" not in raw and b"LUCID" not in raw,
      {"metadata_author": A.metadata.get("author")})
llc = sorted(set(re.findall(r"[A-Za-z&.' ]{0,40}\bLLC\b", txt)))
check("author edition: remaining 'LLC' strings are third-party project entities only", all("Lucid" not in s for s in llc), llc)
norm = lambda s: re.sub(r"\s+", " ", s.replace("Lucid Direction Insights LLC", "@").replace("Lucid Direction Insights", "@")
                        .replace("LUCID DIRECTION INSIGHTS", "@").replace("Lian Duan", "@")).strip()
body_diff = [i + 1 for i in range(1, len(A) - 1) if norm(A[i].get_text()) != norm(V[i].get_text())]
check("author edition: body pages identical to V1.0 apart from the footer name", len(A) == len(V) and not body_diff and A.get_toc() == V.get_toc(),
      {"pages": len(A), "pages_with_other_differences": body_diff})
check("author edition: 'Lian Duan' on cover, back cover and every body-page footer",
      "Lian Duan" in A[0].get_text() and "Lian Duan" in A[-1].get_text() and all("Lian Duan" in A[i].get_text() for i in range(1, len(A) - 1)))
check("author edition: no local file links (standalone PDF)", not file_links(OUT / AUTHOR_PDF), {"V1.0 file links": len(file_links(V10 / EN_PDF))})

# zip
zp = OUT / f"{PKG_NAME}.zip"
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in sorted(PKG.rglob("*")):
        z.write(p, p.relative_to(OUT))
(OUT / f"{PKG_NAME}.zip.sha256").write_text(f"{sha(zp)}  {zp.name}\n")
(OUT / f"{AUTHOR_PDF}.sha256").write_text(f"{sha(OUT / AUTHOR_PDF)}  {AUTHOR_PDF}\n")
rec["_package_files"] = sorted(names)
rec["_sizes_bytes"] = {"zip": zp.stat().st_size, "author_pdf": (OUT / AUTHOR_PDF).stat().st_size}
rec["_result"] = "PASS" if ok else "FAIL"
(OUT / "Client-Package-Check.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False))
print(json.dumps({k: v for k, v in rec.items() if k != "_package_files"}, indent=1, ensure_ascii=False))
sys.exit(0 if ok else 1)
