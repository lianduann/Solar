"""SOLAR-001 V1.0 Chinese edition - assemble the translated parts into the Chinese Markdown source.

The English V1.0 source was translated in 13 line ranges (source/translation-parts/, rules in records/Translation-Guide.md).
This script writes months as numbers (some parts wrote 九月-style months), restores trailing blank lines so the Chinese
source stays line-aligned with the English, and applies the editorial fixes listed below.
Usage: python3 build/assemble_translation.py   (rewrites source/SOLAR-001_V1.0_Report-ZH.md)
"""
import re
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
PARTS = ["part01","part02","part03","part04a","part04b","part05","part06a","part06b","part07","part08","part09a","part09b","part10"]
N = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10,"十一":11,"十二":12}
NUMW = "十二|十一|十|一|二|三|四|五|六|七|八|九"
BAD_BEFORE = "第个统单每唯同一二三四五六七八九十逐"
log = []
def month(m):
    log.append(m.group(0)); return f" {N[m[1]]} 月"
def months(t):
    # ranges first: 一至八月 -> 1–8 月
    t = re.sub(rf"(?<![{BAD_BEFORE}])({NUMW})至({NUMW})月(?!度)", lambda m: (log.append(m.group(0)), f" {N[m[1]]}–{N[m[2]]} 月")[1], t)
    t = re.sub(rf"(?<![{BAD_BEFORE}])({NUMW})月(?!度)", month, t)
    t = re.sub(r"(?<=[（(“《、，：；/\[])\s+(?=\d)", "", t)
    t = re.sub(r"^ (?=\d)", "", t, flags=re.M)
    t = re.sub(r"(?<=\S)  +(?=\d)", " ", t)
    return t
EN = (PKG / "source" / "SOLAR-001_V1.0_Report-EN.md").read_text(encoding="utf-8").split("\n")
R = {"part01":(1,134),"part02":(135,239),"part03":(240,389),"part04a":(390,483),"part04b":(484,579),"part05":(580,736),"part06a":(737,868),
     "part06b":(869,959),"part07":(960,1123),"part08":(1124,1244),"part09a":(1245,1337),"part09b":(1338,1461),"part10":(1462,len(EN))}
out = []
for p in PARTS:
    s_, e_ = R[p]
    zl = months((PKG / "source" / "translation-parts" / f"{p}.md").read_text(encoding="utf-8")).rstrip("\n").split("\n")
    want = e_ - s_ + 1
    assert len(zl) <= want and all(not x.strip() for x in EN[s_ - 1 + len(zl):e_]), p
    out += zl + [""] * (want - len(zl))   # restore trailing blank lines so the Chinese source stays line-aligned with the English
md = "\n".join(out)
# editorial fixes after review of the assembled text
FIXES = [("**单独版本化的枢纽对冲计算。**", "**单独版本的枢纽对冲计算。**"),
         ("PDF 物理页第 1 页，申报表第 2.7 节", "PDF 物理页第 1 页，申报文件第 2.7 节"),
         ("[P01; P08; 第 4.4 节和第 5.7 节; LONGi FY2025 annual report p.297]", "[P01；P08；第 4.4 节和第 5.7 节；隆基 FY2025 年度报告 p.297]"),
         ("[R-C: Batch Zero deck, physical pages 1 and 5–8]", "[R-C：Batch Zero 演示材料，物理页第 1 页及第 5–8 页]"),
         ("产量超过 1.82 百万公吨", "产量超过 1.82 百万吨"),
         ("| 超过 1.82 百万公吨 |", "| 超过 1.82 百万吨 |")]
for a, b in FIXES:
    assert md.count(a) == 1, a
    md = md.replace(a, b)
(PKG / "source" / "SOLAR-001_V1.0_Report-ZH.md").write_text(md, encoding="utf-8")
print(len(log), "month rewrites"); print(" | ".join(log))
