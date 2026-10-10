"""SOLAR-001 V0.999-R1 - single rebuild entry point.

Runs, in order: the R1 arithmetic (build/r1_calcs.py, writes data/r1/), figure rendering, figure-data comparison with the upstream snapshots, PDF build, numeric-preservation
check against the V0.999 Markdown, and structural/link checks. Every command, exit status and duration is written to
<output-dir>/records/Build-Log.json. No upstream model, regression or simulation is rerun; the only calculations are the
labeled R1 arithmetic.

Usage:
  python3 build/build_all.py                       # rebuild in place (package root)
  python3 build/build_all.py --output-dir /tmp/x   # rebuild into an empty directory
Exit status is 0 only if every step exits 0 and every check reports PASS.
"""
import argparse, datetime, json, subprocess, sys, time
from pathlib import Path

B = Path(__file__).resolve().parent
PKG = B.parent
PDF_NAME = "SOLAR-001_V0.999-R1_Integrated-Market-Research-Report-EN.pdf"
SRC = PKG / "source" / "SOLAR-001_V0.999-R1_Report-EN.md"
BASELINE = PKG / "baseline" / "SOLAR-001_V0.999_Report-EN.md"  # R1 is checked against the delivered V0.999 source


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--output-dir", default=str(PKG)); a = ap.parse_args()
    out = Path(a.output_dir).resolve(); (out / "records").mkdir(parents=True, exist_ok=True)
    py = [sys.executable, "-I"]
    steps = [
        ("R1 additions: production-credit, storage-screen and market-reference arithmetic", py + [str(B / "r1_calcs.py")]),
        ("render figures", py + [str(B / "render_figures.py"), "--out", str(out / "figures")]),
        ("compare plotted data with upstream snapshots", py + [str(B / "check_figures.py"), "--upstream", str(B / "upstream" / "snapshots"),
                                                               "--figures", str(out / "figures"), "--out", str(out / "records" / "Figure-Data-Check.json")]),
        ("build PDF", py + [str(B / "build_report.py"), "--figures", str(out / "figures"), "--out", str(out / PDF_NAME)]),
        ("numeric-preservation check", py + [str(B / "check_numbers.py"), str(BASELINE), str(SRC), str(out / "records" / "Number-Preservation-Check.json")]),
        ("structure, reference and link check", py + [str(B / "check_report.py"), str(SRC), str(out / PDF_NAME), str(out / "records" / "Report-Structure-Check.json")]),
    ]
    log = {"started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "python": sys.version.split()[0],
           "output_dir": "." if out == PKG else str(out), "steps": []}
    ok = True
    for name, cmd in steps:
        t = time.time(); r = subprocess.run(cmd, cwd=str(PKG), capture_output=True, text=True)
        tail = [l.replace(str(PKG), ".") for l in (r.stdout + r.stderr).strip().splitlines()[-3:]]
        passed = r.returncode == 0 and not any(l.startswith("REVIEW") or "MISMATCH" in l for l in tail)
        log["steps"].append({"step": name, "command": " ".join(["python3"] + [c.replace(str(PKG) + "/", "").replace(str(PKG), ".") for c in cmd[2:]]),
                             "exit_status": r.returncode, "seconds": round(time.time() - t, 1), "output_tail": tail, "ok": passed})
        print(f"[{'ok' if passed else 'FAIL'}] {name} (exit {r.returncode})")
        if not passed:
            ok = False
            if r.returncode != 0: break
    log["result"] = "PASS" if ok else "FAIL"
    (out / "records" / "Build-Log.json").write_text(json.dumps(log, indent=1))
    print(log["result"], PDF_NAME if out == PKG else out / PDF_NAME)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
