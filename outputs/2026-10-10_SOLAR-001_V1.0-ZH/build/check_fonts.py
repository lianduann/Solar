"""SOLAR-001 V1.0 Chinese edition - every character of the Chinese source must be in an embedded font, and the PDF must embed
only the report fonts.
Usage: python3 build/check_fonts.py SOURCE.md REPORT.pdf OUT.json"""
import json, sys
from pathlib import Path
import pymupdf
from fontTools.ttLib import TTFont

PKG = Path(__file__).resolve().parents[1]; FD = PKG / "assets" / "fonts"
md, pdf, out = map(Path, sys.argv[1:4])
cover = set()
for f in FD.iterdir():
    if f.suffix in (".ttf", ".otf"): cover |= set(TTFont(str(f), lazy=True).getBestCmap())
chars = sorted({c for c in md.read_text(encoding="utf-8") if ord(c) > 0x20 and c not in "\n\r\t"})
missing = [c for c in chars if ord(c) not in cover]
d = pymupdf.open(str(pdf)); fonts = sorted({f[3] for p in d for f in p.get_fonts()})
# embedded names are the CSS family names of assets/report.css (Source Serif, Sans R = Liberation Sans, Serif SC / Sans SC =
# Noto CJK SC subsets, Report Mono = DejaVu Sans Mono)
allowed = ("Source-Serif", "Sans-R", "Serif-SC", "Sans-SC", "Report-Mono")
other = [f for f in fonts if not any(a in f for a in allowed)]
rep = {"source_distinct_chars": len(chars), "chars_without_embedded_font": missing, "pdf_fonts": fonts, "pdf_fonts_not_from_package": other,
       "result": "PASS" if not missing and not other else "REVIEW"}
out.write_text(json.dumps(rep, indent=1, ensure_ascii=False)); print(rep["result"], "missing:", missing, "other fonts:", other)
