"""SOLAR-001 V0.999-R1 - write MANIFEST.csv (path, bytes, sha256) and SHA256SUMS.txt for every file in the package.
Usage: python3 build/make_manifest.py"""
import csv, hashlib, shutil
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
SKIP = {"MANIFEST.csv", "SHA256SUMS.txt"}
for d in PKG.rglob("__pycache__"): shutil.rmtree(d)
files = sorted(p for p in PKG.rglob("*") if p.is_file() and p.relative_to(PKG).as_posix() not in SKIP)
rows = [(p.relative_to(PKG).as_posix(), p.stat().st_size, hashlib.sha256(p.read_bytes()).hexdigest()) for p in files]
with open(PKG / "MANIFEST.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["path", "bytes", "sha256"]); w.writerows(rows)
(PKG / "SHA256SUMS.txt").write_text("".join(f"{h}  {p}\n" for p, _, h in rows))
print(len(rows), "files,", sum(s for _, s, _ in rows), "bytes")
