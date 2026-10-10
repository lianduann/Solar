"""SOLAR-001 V1.0 Chinese edition - numeric-preservation check of the translation against the English V1.0 source.

The Chinese Markdown is line-aligned with the English source (same line count; every heading, table row, list item, box and
paragraph on the same line). For every line, the multiset of numeric tokens must be identical in both languages after
normalizing: minus sign and en dash, '$X million/billion' -> '$Xm/$Xbn', thousands separators, link targets, English month
names -> month numbers (Chinese dates write months as numbers), and a break between letters and digits (FY2025 -> FY 2025).
Table cells are compared cell by cell. Any remaining difference must be listed in ALLOWED with a reason.
Usage: python3 build/check_numbers_zh.py EN.md ZH.md OUT.json
"""
import collections, json, re, sys
from pathlib import Path

NUM = re.compile(r"(?<![A-Za-z0-9_.])-?\d[\d,]*(?:\.\d+)?")
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MRE = re.compile(r"\b(" + "|".join(MONTHS + [m[:3] for m in MONTHS]) + r")\b\.?")
ALLOWED = {  # EN line number -> reason, for differences reviewed and accepted
    580: "chapter title: the English modal verb 'May' is read as a month name; the title has no number",
    847: "'Q1 2024' is written 2024 年第一季度 (quarter as a Chinese numeral)",
    1303: "'announcement no.2' is written 第2号公告; the English 'no.2' is not tokenized because of the period",
}


def norm(t, en):
    t = t.replace("−", "-").replace("–", "-").replace("—", " ")
    t = re.sub(r"\]\([^)]*\)", "]", t)
    t = re.sub(r"(\d) million\b", r"\1m", t); t = re.sub(r"(\d) billion\b", r"\1bn", t)
    if en: t = MRE.sub(lambda m: f" {[x[:3] for x in MONTHS].index(m[1][:3]) + 1} ", t)
    t = re.sub(r"(?<=[A-Za-z])(?=\d)", " ", t)
    return t


def toks(t, en):
    return collections.Counter(m.replace(",", "") for m in NUM.findall(norm(t, en)))


def main():
    a, b, out = map(Path, sys.argv[1:4])
    en, zh = a.read_text(encoding="utf-8").split("\n"), b.read_text(encoding="utf-8").split("\n")
    rep = {"english": a.name, "chinese": b.name, "lines_english": len(en), "lines_chinese": len(zh)}
    kind = lambda x: "blank" if not x.strip() else next((k for k, p in (("heading", "#"), ("table", "|"), ("figure", "!["), ("box", ">"), ("block", ":::"), ("bullet", "- ")) if x.strip().startswith(p)), "text")
    rep["line_kind_mismatches"] = [i + 1 for i, (x, y) in enumerate(zip(en, zh)) if kind(x) != kind(y)]
    diffs, cells, allowed, n_en = [], [], [], 0
    for i, (x, y) in enumerate(zip(en, zh)):
        tx, ty = toks(x, True), toks(y, False); n_en += sum(tx.values())
        if tx != ty:
            d = {"line": i + 1, "missing_in_chinese": dict(tx - ty), "extra_in_chinese": dict(ty - tx), "english": x[:160], "chinese": y[:160]}
            (allowed if i + 1 in ALLOWED else diffs).append(d | ({"reason": ALLOWED[i + 1]} if i + 1 in ALLOWED else {}))
        if x.strip().startswith("|") and not re.fullmatch(r"\|[\s:|-]+\|", x.strip()):
            cx = [c.strip() for c in x.strip().strip("|").split("|")]; cy = [c.strip() for c in y.strip().strip("|").split("|")]
            if len(cx) != len(cy): cells.append({"line": i + 1, "problem": f"{len(cx)} cells vs {len(cy)}"})
            else:
                for k, (p, q) in enumerate(zip(cx, cy)):
                    if toks(p, True) != toks(q, False) and i + 1 not in ALLOWED: cells.append({"line": i + 1, "cell": k + 1, "english": p, "chinese": q})
    rep.update(numeric_tokens_english=n_en, lines_with_differences=diffs, table_cell_differences=cells, allowed_differences=allowed)
    rep["result"] = "PASS" if len(en) == len(zh) and not rep["line_kind_mismatches"] and not diffs and not cells else "REVIEW"
    out.write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    print(rep["result"], "tokens:", n_en, "line diffs:", len(diffs), "cell diffs:", len(cells), "kind mismatches:", rep["line_kind_mismatches"][:10])


if __name__ == "__main__":
    main()
