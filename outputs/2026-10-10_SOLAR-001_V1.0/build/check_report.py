"""SOLAR-001 V1.0 - structural checks of the Markdown source and the built PDF.

Checks: figure/table numbering order and uniqueness; every in-text Table/Figure/Section/Appendix reference has a target;
required qualifiers are present; PDF page count, bookmarks, contents page numbers, internal link targets, external
links and links to accompanying research files.
Usage: python3 build/check_report.py SOURCE.md REPORT.pdf OUT.json
"""
import json, os, re, sys
from pathlib import Path

import pymupdf

PKG = Path(__file__).resolve().parents[1]

# Qualifiers that must stay next to the results they qualify (wording as in the V0.999 source).
QUALIFIERS = {
    "Figure 8-4 left panel: thin dotted lines with crosses are medians": "thin dotted lines with crosses are medians",
    "$26.4/MWh is modeled gross energy value, not net revenue": "not net revenue",
    "30-year node fixed price and 10-15-year hub hedge are separate calculation versions": "Separately versioned hub-hedge calculation",
    "Pre-tax NPV plus illustrative credit is not a complete after-tax valuation": "not an after-tax value",
    "Pre-tax NPV plus illustrative credit is not a complete after-tax valuation (Section 10.8)": "does not claim the illustration is a complete after-tax NPV",
    "Historical scenarios are not an ERCOT market-wide conclusion": "they do not show that ERCOT solar projects are generally uneconomic",
    "Historical shortfall is not a market-wide finding": "It is not a market-wide finding",
    "Industry-line and product-line margins are not a ranking": "they are not a matched product ranking",
    "2026 fixed-profile diagnostic is not a realized 2026 capture price": "This is a fixed-profile price diagnostic, not realized 2026 capture",
    "Production-credit illustration is pre-tax NPV plus a credit, not an after-tax valuation": "the result is pre-tax NPV plus a credit, not an after-tax valuation",
    "Storage result is a screen, not a valuation": "the storage result is a screen, not a valuation",
    "Market offer index is not an executed contract": "not an executed contract",
}


def numbering(md):
    res = {}
    for kind, pat in (("Table", r"^\*\*Table ([0-9A-D]+)-(\d+)([AB]?)\."), ("Figure", r"^!\[Figure ([0-9A-D]+)-(\d+)\.")):
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
    tables = set(re.findall(r"^\*\*Table ([0-9A-D]+-\d+[AB]?)\.", md, re.M))
    figures = set(re.findall(r"^!\[Figure ([0-9A-D]+-\d+)\.", md, re.M))
    secs = set(re.findall(r"^## (\d+\.\d+|[A-D]\.\d+)\b", md, re.M))
    body = re.sub(r"^\*\*Table [^\n]*|^!\[Figure [^\n]*", "", md, flags=re.M)
    missing = []
    for m in re.finditer(r"\bTables? ([0-9A-D]+-\d+[AB]?)(?:(?: and |, |–)([0-9A-D]+-\d+[AB]?))?", body):
        missing += [x for x in m.groups() if x and x not in tables]
    missing += [x for x in re.findall(r"\bFigures? ([0-9A-D]+-\d+)", body) if x not in figures]
    # "filing Section 2.7" refers to a section of an external filing, not of this report
    missing += [x for x in re.findall(r"(?<!filing )\b(?:Sections?|Appendix) ((?:\d+|[A-D])\.\d+)", body) if x not in secs]
    return {"tables": len(tables), "figures": len(figures), "sections": len(secs), "unresolved": sorted(set(missing))}


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
    ci = next(i for i, (_, t, _) in enumerate(toc) if t == "Contents")  # contents run from its bookmark to the next one
    text = "\n".join(d[i].get_text() for i in range(toc[ci][2] - 1, toc[ci + 1][2] - 1))
    shown = [int(x) for x in re.findall(r"\.{3,}\s*(\d+)\s*$", text, re.M)]
    zero = [n for n in shown if n == 0]
    out.update(contents_entries=len(shown), contents_zero_page_numbers=len(zero))
    listed = [pg for _, t, pg in toc if t not in ("Cover", "Contents", "Back cover")]
    out["contents_numbers_differ_from_bookmarks"] = [(i, a, b) for i, (a, b) in enumerate(zip(shown, listed)) if a != b] + ([("count", len(shown), len(listed))] if len(shown) != len(listed) else [])
    mism = []
    # compare: for each level-2 bookmark, its title text appears on the page it points to
    for lvl, t, p in toc:
        title = re.sub(r"^(Chapter \d+|Appendix [A-D]) —\s*", "", t).strip()
        key = re.sub(r"\s+", " ", title)[:40]
        pg = re.sub(r"\s+", " ", d[p - 1].get_text().replace("­", "").replace("‐", "-"))
        pg = re.sub(r"(\w)- (\w)", r"\1\2", pg)
        if lvl > 1 and key.split(" ", 1)[-1][:25] not in pg: mism.append((t, p))
    out["bookmarks_title_not_on_target_page"] = mism
    return out


def main():
    md_p, pdf_p, out_p = map(Path, sys.argv[1:4])
    md = md_p.read_text()
    rep = {"source": md_p.name, "pdf": pdf_p.name, "numbering": numbering(md), "references": references(md),
           "qualifiers": {k: (v in md) for k, v in QUALIFIERS.items()}, "pdf": pdf_checks(pdf_p)}
    p = rep["pdf"]
    ok = (not rep["numbering"]["Table"]["problems"] and not rep["numbering"]["Figure"]["problems"] and not rep["references"]["unresolved"]
          and all(rep["qualifiers"].values()) and not p["bookmarks_bad_page"] and not p["internal_links_unresolved"]
          and not p["file_links_missing_or_absolute"] and not p["external_non_https"] and p["contents_zero_page_numbers"] == 0 and not p["contents_numbers_differ_from_bookmarks"]
          and not p["bookmarks_title_not_on_target_page"])
    rep["result"] = "PASS" if ok else "REVIEW"
    out_p.write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    print(rep["result"], json.dumps({k: v for k, v in p.items() if k != "metadata"}, ensure_ascii=False)[:1500])
    print("numbering", {k: v["problems"] for k, v in rep["numbering"].items()}, "refs", rep["references"], "qual", all(rep["qualifiers"].values()))


if __name__ == "__main__":
    main()
