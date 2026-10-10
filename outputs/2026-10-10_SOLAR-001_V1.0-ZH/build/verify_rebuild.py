"""SOLAR-001 V1.0 Chinese edition - rebuild into an empty directory and compare with the delivered PDF and figures.
Usage: python3 build/verify_rebuild.py EMPTY_DIR [--record FILE]
Records the command, exit status, page count, per-page text comparison and figure hashes."""
import argparse, datetime, hashlib, json, subprocess, sys
from pathlib import Path
import pymupdf

B = Path(__file__).resolve().parent; PKG = B.parent
PDF = "SOLAR-001_V1.0_Integrated-Market-Research-Report-ZH.pdf"
ap = argparse.ArgumentParser(); ap.add_argument("dir"); ap.add_argument("--record", default=str(PKG / "records" / "Rebuild-Verification.json")); a = ap.parse_args()
out = Path(a.dir).resolve()
if out.exists() and any(out.iterdir()): sys.exit(f"{out} is not empty")
out.mkdir(parents=True, exist_ok=True)
cmd = [sys.executable, "-I", str(B / "build_all.py"), "--output-dir", str(out)]
r = subprocess.run(cmd, cwd=str(PKG), capture_output=True, text=True)
rec = {"checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
       "command": f"python3 build/build_all.py --output-dir {out}", "exit_status": r.returncode, "output_tail": r.stdout.strip().splitlines()[-7:]}
if r.returncode == 0:
    a_, b_ = pymupdf.open(str(PKG / PDF)), pymupdf.open(str(out / PDF))
    rec["pages_delivered"], rec["pages_rebuilt"] = len(a_), len(b_)
    rec["pages_with_text_difference"] = [i + 1 for i in range(min(len(a_), len(b_))) if a_[i].get_text() != b_[i].get_text()]
    rec["bookmarks_equal"] = a_.get_toc() == b_.get_toc()
    h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    figs = sorted(p.name for p in (PKG / "figures").glob("*.svg"))
    rec["figure_svgs_identical"] = sum(h(PKG / "figures" / f) == h(out / "figures" / f) for f in figs); rec["figure_svgs_total"] = len(figs)
    rec["result"] = "PASS" if (len(a_) == len(b_) and not rec["pages_with_text_difference"] and rec["bookmarks_equal"]
                               and rec["figure_svgs_identical"] == len(figs)) else "REVIEW"
else:
    rec["result"] = "FAIL"
Path(a.record).write_text(json.dumps(rec, indent=1)); print(json.dumps(rec, indent=1))
sys.exit(0 if rec["result"] == "PASS" else 1)
