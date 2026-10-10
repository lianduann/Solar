"""SOLAR-001 V1.0 Chinese edition - structural checks of the Chinese Markdown source and the built PDF.

Checks: figure/table numbering order and uniqueness; every in-text 表/图/第 X.Y 节/附录 X.Y reference has a target;
required qualifiers are present; PDF page count, bookmarks, contents page numbers, internal link targets, external
links and links to accompanying research files.
Usage: python3 build/check_report.py SOURCE.md REPORT.pdf OUT.json
"""
import json, os, re, sys
from pathlib import Path

import pymupdf

PKG = Path(__file__).resolve().parents[1]

# Qualifiers that must stay next to the results they qualify: the English wording (V1.0 source) and its Chinese rendering.
QUALIFIERS = {
    "Figure 8-4 left panel: thin dotted lines with crosses are medians": "带叉号的细虚线为中位数",
    "$26.4/MWh is modeled gross energy value, not net revenue": "非净收入",
    "30-year node fixed price and 10-15-year hub hedge are separate calculation versions": "单独版本的枢纽对冲计算",
    "Pre-tax NPV plus illustrative credit is not a complete after-tax valuation": "而非税后价值",
    "Pre-tax NPV plus illustrative credit is not a complete after-tax valuation (Section 10.8)": "本版并不声称该示意是完整的税后 NPV",
    "Historical scenarios are not an ERCOT market-wide conclusion": "它们并不表明 ERCOT 光伏项目总体上不经济",
    "Historical shortfall is not a market-wide finding": "这并非关于光伏开发的全市场结论",
    "Industry-line and product-line margins are not a ranking": "并非匹配的产品排名",
    "2026 fixed-profile diagnostic is not a realized 2026 capture price": "这是固定曲线价格诊断，而非 2026 年已实现的捕获",
    "Production-credit illustration is pre-tax NPV plus a credit, not an after-tax valuation": "该结果为税前 NPV 加上一项抵免，而非税后估值",
    "Storage result is a screen, not a valuation": "储能结果是筛查，而非估值",
    "Market offer index is not an executed contract": "非已签署合同",
}


def numbering(md):
    res = {}
    for kind, pat in (("Table", r"^\*\*表 ([0-9A-D]+)-(\d+)([AB]?)\."), ("Figure", r"^!\[图 ([0-9A-D]+)-(\d+)\.")):
        seen, problems = [], []
        for m in re.finditer(pat, md, re.M):
            seen.append(m.group(0).split()[1].rstrip("."))
        by = {}
        for s in seen:
            ch, n = s.split("-")[0], re.match(r"\d+", s.split("-")[1])[0]
            by.setdefault(ch, []).append((int(n), s))
        for ch, lst in by.items():
            nums = sorted(set(n for n, _ in lst))
            if nums != list(range(nums[0], nums[0] + len(nums))): problems.append(f"{kind} {ch}: gap in {nums}")
            if [n for n, _ in lst] != sorted(n for n, _ in lst): problems.append(f"{kind} {ch}: out of order {[s for _, s in lst]}")
        if len(seen) != len(set(seen)): problems.append(f"duplicate {kind} numbers")
        res[kind] = {"count": len(seen), "labels": seen, "problems": problems}
    return res


def references(md):
    tables = set(re.findall(r"^\*\*表 ([0-9A-D]+-\d+[AB]?)\.", md, re.M))
    figures = set(re.findall(r"^!\[图 ([0-9A-D]+-\d+)\.", md, re.M))
    secs = set(re.findall(r"^## (\d+\.\d+|[A-D]\.\d+)\b", md, re.M))
    body = re.sub(r"^\*\*表 [^\n]*|^!\[图 [^\n]*", "", md, flags=re.M)
    body = re.sub(r"\]\([^)]*\)", "]", body)
    missing = []
    for m in re.finditer(r"表 ?([0-9A-D]+-\d+[AB]?)(?:(?: ?和表 ?|、表 ?|、|–)([0-9A-D]+-\d+[AB]?))?", body):
        missing += [x for x in m.groups() if x and x not in tables]
    missing += [x for x in re.findall(r"图 ?([0-9A-D]+-\d+)", body) if x not in figures]
    # "申报文件第 2.7 节" (filing Section 2.7) refers to a section of an external filing, not of this report
    for m in re.finditer(r"(?<!申报文件)(?<!文件)第 ((?:\d+|[A-D])\.\d+)((?:[–、](?:\d+|[A-D])\.\d+)*)(?: 节)", body):
        missing += [x for x in [m[1]] + re.findall(r"(?:\d+|[A-D])\.\d+", m[2]) if x not in secs]
    missing += [x for x in re.findall(r"附录 ([A-D]\.\d+)", body) if x not in secs]
    # English labels left in the text ("Electric Power Monthly Table 6.1" is the title of an external EIA table)
    english_left = sorted(set(re.findall(r"(?<!Monthly )\b(?:Table|Figure|Section|Appendix|Chapter) [0-9A-D]", body)))
    return {"tables": len(tables), "figures": len(figures), "sections": len(secs), "unresolved": sorted(set(missing)),
            "untranslated_reference_labels": english_left}


def pdf_checks(pdf):
    d = pymupdf.open(str(pdf))
    toc = d.get_toc()
    out = {"pages": len(d), "bookmarks": len(toc), "bookmark_levels": sorted(set(l for l, _, _ in toc)),
           "bookmarks_bad_page": [t for _, t, p in toc if not 1 <= p <= len(d)], "metadata": d.metadata}
    names = d.resolve_names()
    internal = external = files = 0; bad_internal, bad_files, urls = [], [], set()
    for page in d:
        for l in page.get_links():
            if l["kind"] in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED):
                internal += 1
                tgt = l.get("page", -1) if l["kind"] == pymupdf.LINK_GOTO else names.get(l.get("nameddest") or l.get("name"), {}).get("page", -1)
                if tgt is None or not 0 <= tgt < len(d): bad_internal.append((page.number + 1, l.get("nameddest") or l.get("name")))
            elif l["kind"] == pymupdf.LINK_URI:
                external += 1; urls.add(l["uri"])
            else:
                a = d.xref_get_key(l["xref"], "A")[1]
                m = re.search(r"/F\(([^)]*)\)", a)
                f = m[1] if m else l.get("file", "")
                files += 1
                if os.path.isabs(f) or not (PKG / f).exists(): bad_files.append(f)  # links are relative to the package root
    out.update(internal_links=internal, internal_links_unresolved=bad_internal, external_links=external,
               external_unique=len(urls), external_non_https=sorted(u for u in urls if not u.startswith("https://")),
               file_links=files, file_links_missing_or_absolute=sorted(set(bad_files)))
    # contents pages: every entry must show a page number equal to the bookmark page
    ci = next(i for i, (_, t, _) in enumerate(toc) if t == "目录")  # contents run from its bookmark to the next one
    text = "\n".join(d[i].get_text() for i in range(toc[ci][2] - 1, toc[ci + 1][2] - 1))
    shown = [int(x) for x in re.findall(r"\.{3,}\s*(\d+)\s*$", text, re.M)]
    zero = [n for n in shown if n == 0]
    out.update(contents_entries=len(shown), contents_zero_page_numbers=len(zero))
    listed = [pg for _, t, pg in toc if t not in ("封面", "目录", "封底")]
    out["contents_numbers_differ_from_bookmarks"] = [(i, a, b) for i, (a, b) in enumerate(zip(shown, listed)) if a != b] + ([("count", len(shown), len(listed))] if len(shown) != len(listed) else [])
    mism = []
    # compare: for each level-2 bookmark, its title text appears on the page it points to
    for lvl, t, p in toc:
        # Chinese lines break between any two characters, so compare with all whitespace removed
        key = re.sub(r"\s+", "", t.split(" ", 1)[-1])[:20]
        pg = re.sub(r"\s+", "", d[p - 1].get_text().replace("­", "").replace("‐", "-"))
        if lvl > 1 and key not in pg: mism.append((t, p))
    out["bookmarks_title_not_on_target_page"] = mism
    return out


def main():
    md_p, pdf_p, out_p = map(Path, sys.argv[1:4])
    md = md_p.read_text()
    rep = {"source": md_p.name, "pdf": pdf_p.name, "numbering": numbering(md), "references": references(md),
           "qualifiers": {k: (v in md) for k, v in QUALIFIERS.items()}, "pdf": pdf_checks(pdf_p)}
    p = rep["pdf"]
    ok = (not rep["numbering"]["Table"]["problems"] and not rep["numbering"]["Figure"]["problems"] and not rep["references"]["unresolved"]
          and not rep["references"]["untranslated_reference_labels"]
          and all(rep["qualifiers"].values()) and not p["bookmarks_bad_page"] and not p["internal_links_unresolved"]
          and not p["file_links_missing_or_absolute"] and not p["external_non_https"] and p["contents_zero_page_numbers"] == 0 and not p["contents_numbers_differ_from_bookmarks"]
          and not p["bookmarks_title_not_on_target_page"])
    rep["result"] = "PASS" if ok else "REVIEW"
    out_p.write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    print(rep["result"], json.dumps({k: v for k, v in p.items() if k != "metadata"}, ensure_ascii=False)[:1500])
    print("numbering", {k: v["problems"] for k, v in rep["numbering"].items()}, "refs", rep["references"], "qual", all(rep["qualifiers"].values()))


if __name__ == "__main__":
    main()
