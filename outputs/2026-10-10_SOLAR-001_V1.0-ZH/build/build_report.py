"""SOLAR-001 V1.0 Chinese edition - convert the Chinese Markdown source into the designed HTML and render the PDF with WeasyPrint.

Adapted from the English V1.0 build: Chinese structural labels (表 / 图 / 第 X.Y 节 / 附录 / 第 N 章 / 方框 1 / 本章限制 / 示意),
Chinese page furniture, and Noto CJK fonts. Figures are shared with the English edition.

The Markdown file is the single content source; this script only adds structure and styling:
cover, back cover, contents, chapter openers, key-number tiles, boxes, tables, figures, notes,
internal cross-reference links, PDF bookmarks and document metadata.

Usage:
  python3 build/build_report.py --figures DIR --out PDF [--html HTML]
Defaults: figures = <package>/figures, out = <package>/SOLAR-001_V1.0_Integrated-Market-Research-Report-ZH.pdf
"""
import argparse, html, json, re
from pathlib import Path

B = Path(__file__).resolve().parent
PKG = B.parent
SRC = PKG / "source" / "SOLAR-001_V1.0_Report-ZH.md"
ASSETS = PKG / "assets"
COMPANION = "research-companion"

# ----------------------------------------------------------------------------- inline formatting

SECTION_IDS, TABLE_IDS, FIGURE_IDS, APPENDIX_IDS, CHAPTER_IDS = set(), set(), set(), set(), set()


def smart(s):
    """Typographic quotes and apostrophes in plain text."""
    s = re.sub(r"(?<=\w)'(?=\w)", "’", s)
    s = re.sub(r"(?<=[\w.,;:!?)%])'", "’", s)
    s = re.sub(r"'(?=\w)", "‘", s)
    s = re.sub(r'"(?=\w|\$)', "“", s)
    s = s.replace('"', "”")
    return s


def xref(s):
    """Link cross-references to sections, tables, figures, appendices and chapters (plain-text segments only)."""
    def sec(m):
        k = m[2]; i = "sec-" + k.replace(".", "-")
        return f'<a class="xref" href="#{i}">{m[1]}{k}{m[3]}</a>' if i in SECTION_IDS else m[0]
    # 第 10.3 节 / 第 10.3–10.5 节 / 第 8.1、10.3 节 (first number linked) / 附录 B.2
    s = re.sub(r"(第 )([A-D]\.\d|\d{1,2}\.\d{1,2})((?:[–、]\d{1,2}\.\d{1,2})*(?: 节)?)(?![\d.])", sec, s)
    s = re.sub(r"(附录 )([A-D]\.\d)()(?![\d])", sec, s)
    def tab(m):
        i = "tbl-" + m[2].lower()
        return f'<a class="xref" href="#{i}">{m[1]}{m[2]}</a>' if i in TABLE_IDS else m[0]
    s = re.sub(r"(表 ?)([0-9A-D]+-\d+[AB]?)", tab, s)
    def fig(m):
        i = "fig-" + m[2].lower()
        return f'<a class="xref" href="#{i}">{m[1]}{m[2]}</a>' if i in FIGURE_IDS else m[0]
    s = re.sub(r"(图 ?)([0-9A-D]+-\d+)", fig, s)
    def app(m):
        i = "app-" + m[1].lower()
        return f'<a class="xref" href="#{i}">附录 {m[1]}</a>' if i in APPENDIX_IDS else m[0]
    s = re.sub(r"附录 ([A-D])(?![.\w])", app, s)
    def chap(m):
        i = "ch-" + m[2]
        return f'<a class="xref" href="#{i}">{m[1]}{m[2]}{m[3]}</a>' if i in CHAPTER_IDS else m[0]
    s = re.sub(r"(第 )(\d{1,2})((?:[–、]\d{1,2})* 章)", chap, s)
    s = s.replace("方框 1", '<a class="xref" href="#box-1">方框 1</a>')
    return s


def title_html(t):
    """Chapter titles longer than one line break after the colon, so the second line is a whole phrase."""
    h = inline(t, False)
    return h.replace("：", "：<br/>", 1) if len(t) > 22 and "：" in t else h


def local_link(href):
    target = PKG / COMPANION / href
    return f"{COMPANION}/{href}" if target.exists() else None


def inline(t, links=True):
    """Markdown inline -> HTML. Protects code spans and links, then applies emphasis, quotes and cross-references."""
    out, pos = [], 0
    token = re.compile(r"`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)")
    for m in token.finditer(t):
        out.append(("text", t[pos:m.start()]))
        if m[1] is not None:
            out.append(("raw", f'<code>{html.escape(m[1]).replace("/", "/<wbr>").replace("_", "_<wbr>")}</code>'))
        else:
            label, href = m[2], m[3]
            lab = emph(smart(html.escape(label, quote=False)))
            if href.startswith("http"):
                out.append(("raw", f'<a class="ext" href="{html.escape(href)}">{lab}</a>'))
            elif href.startswith("#"):
                out.append(("raw", f'<a class="xref" href="{html.escape(href)}">{lab}</a>'))
            else:
                h = local_link(href)
                out.append(("raw", f'<a class="file" href="{html.escape(h)}">{lab}</a>' if h else lab))
        pos = m.end()
    out.append(("text", t[pos:]))
    res = []
    for kind, s in out:
        if kind == "raw": res.append(s); continue
        s = emph(nobreak(smart(html.escape(s, quote=False))))
        if links: s = xref(s)
        res.append(s)
    return "".join(res)


NUM = re.compile(r"(?<![A-Za-z0-9_/.])((?:[−+±~≈]\s?)?\$?\d[\d,]*(?:\.\d+)?(?:%|m|bn)?(?:/[A-Za-z]+(?:-year)?|\s(?:MWh|MW|GW|TWh|GWh|kWac|MWac|MWdc))?)(?![A-Za-z0-9_])")


def nobreak(s):
    """Keep signed values and value/unit expressions on one line (e.g. −$103.3m, $48.9/MWh); render ^n as a superscript."""
    s = re.sub(r"\^(\d+)", r"<sup>\1</sup>", s)
    def w(m):
        v = m[1]
        return f'<span class="nw">{v}</span>' if (v[0] in "−+±~≈" or "/" in v or " " in v) else v
    return NUM.sub(w, s)


def emph(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![A-Za-z0-9_*])\*(?!\s)(.+?)(?<!\s)\*(?![A-Za-z0-9_*])", r"<em>\1</em>", s)
    return s


def strip_italic(t):
    t = t.strip()
    if t.startswith("*") and not t.startswith("**") and t.endswith("*") and not t.endswith("**"):
        inner = t[1:-1]
        if "*" not in inner.replace("**", ""): return inner
    # paragraph that mixes an italic sentence group with roman text: drop the italic markers
    return re.sub(r"(?<!\*)\*(?!\*)([^*]+)\*(?!\*)", r"\1", t)

# ----------------------------------------------------------------------------- block parsing


def parse_front(lines):
    meta = {}
    if lines and lines[0].strip() == "---":
        j = lines.index("---", 1)
        for l in lines[1:j]:
            k, v = l.split(":", 1); meta[k.strip()] = v.strip()
        lines = lines[j + 1:]
    return meta, lines


def table_html(rows, aligns, cls=""):
    head, body = rows[0], rows[1:]
    num = []
    for c in range(len(head)):
        vals = [r[c] for r in body if c < len(r) and r[c].strip() not in ("", "—", "-", "n/a", "n/d")]
        isnum = bool(vals) and all(re.fullmatch(r"[−+\-]?[$]?[\d,.]+[%¹²³⁴⁵]?( ?[+/] ?[−\-]?[\d,.]+[%¹²³⁴⁵]?)*|none⁵|of which [\d.]+|\+[\d.]+ restricted cash", v.strip()) for v in vals)
        num.append(aligns[c] == "R" or isnum)
    h = [f'<table class="{cls}"><thead><tr>']
    for c, x in enumerate(head):
        h.append(f'<th class="{"num" if num[c] else ""}">{inline(x)}</th>')
    h.append("</tr></thead><tbody>")
    for r in body:
        h.append("<tr>" + "".join(f'<td class="{"num" if c < len(num) and num[c] else ""}">{inline(x)}</td>' for c, x in enumerate(r)) + "</tr>")
    h.append("</tbody></table>")
    return "".join(h)


def build_html(md, figmap, figdir):
    meta, lines = parse_front(md.splitlines())
    # pass 1: collect anchors so cross-references only link to targets that exist
    for l in lines:
        m = re.match(r"^## (\d{1,2}\.\d{1,2}|[A-D]\.\d) ", l)
        if m: SECTION_IDS.add("sec-" + m[1].replace(".", "-"))
        m = re.match(r"^\*\*表 ([0-9A-D]+-\d+[AB]?)\.", l)
        if m: TABLE_IDS.add("tbl-" + m[1].lower())
        m = re.match(r"^!\[图 ([0-9A-D]+-\d+)\.", l)
        if m: FIGURE_IDS.add("fig-" + m[1].lower())
        m = re.match(r"^# 附录 ([A-D])\.", l)
        if m: APPENDIX_IDS.add("app-" + m[1].lower())
        m = re.match(r"^# (\d{1,2})\. ", l)
        if m: CHAPTER_IDS.add("ch-" + m[1])
    out, toc = [], []
    i, n = 0, len(lines)
    in_section = False

    def peek_notes(j):
        """Collect note paragraphs / note lists directly following a table or figure."""
        notes = []
        while j < n:
            while j < n and not lines[j].strip(): j += 1
            if j >= n: break
            s = lines[j].strip()
            if s.startswith("*") and not s.startswith("**"):
                para = [s]; j += 1
                while j < n and lines[j].strip() and not lines[j].strip().startswith(("#", "|", "!", "- ", ">", ":::")) and not re.match(r"^\d+\. ", lines[j].strip()) and not lines[j].strip().startswith("*"):
                    para.append(lines[j].strip()); j += 1
                notes.append(f'<p>{inline(strip_italic(" ".join(para)))}</p>')
                # a "Notes:" heading followed by a numbered list of italic notes
                if strip_italic(s).rstrip(":：") in ("Notes", "注", "注释", "附注"):
                    items = []
                    while j < n and re.match(r"^\d+\. ", lines[j].strip()):
                        items.append(f'<li>{inline(strip_italic(re.sub(r"^\d+\. ", "", lines[j].strip())))}</li>'); j += 1
                    notes[-1] = f'<p class="notes-h">注</p><ol class="notes">{"".join(items)}</ol>'
                continue
            break
        return notes, j

    while i < n:
        raw = lines[i]; s = raw.strip()
        if not s or s == "---": i += 1; continue
        # chapter / appendix / front headings
        if s.startswith("# "):
            title = s[2:]
            if in_section: out.append("</section>")
            in_section = True
            if title.endswith("{.front}"):
                t = title.replace("{.front}", "").strip(); hid = "about"
                out.append(f'<section class="front" id="{hid}"><h1 class="front-h"><span class="chap-title">{inline(t, False)}</span></h1>')
                toc.append((1, hid, "", t))
            else:
                m = re.match(r"^(\d{1,2})\. (.*)$", title) or re.match(r"^附录 ([A-D])\. (.*)$", title)
                num, t = m[1], m[2]
                is_app = title.startswith("附录")
                hid = ("app-" + num.lower()) if is_app else ("ch-" + num)
                label = f"附录 {num}" if is_app else f"第 {int(num)} 章"
                big = num if is_app else f"{int(num):02d}"
                out.append(f'<section class="chapter{" appendix" if is_app else ""}" id="{hid}"><header class="opener"><div class="chap-num">{big}</div>'
                           f'<h1 data-label="{label}" data-title="{html.escape(smart(re.sub(r"[*`]", "", t)))}"><span class="chap-label">{label}</span><span class="chap-title">{title_html(t)}</span></h1><div class="opener-rule"></div></header>')
                toc.append((1, hid, num, t))
            i += 1; continue
        if s.startswith("## "):
            t = s[3:]; m = re.match(r"^(\d{1,2}\.\d{1,2}|[A-D]\.\d) (.*)$", t)
            if m:
                hid = "sec-" + m[1].replace(".", "-")
                out.append(f'<h2 id="{hid}"><span class="sec-num">{m[1]}</span> {inline(m[2], False)}</h2>')
                toc.append((2, hid, m[1], m[2]))
            else:
                out.append(f"<h2>{inline(t, False)}</h2>")
            i += 1; continue
        if s.startswith("### "):
            out.append(f"<h3>{inline(s[4:], False)}</h3>"); i += 1; continue
        # fenced blocks
        if s.startswith("::: "):
            kind = s[4:].strip(); body = []; i += 1
            while i < n and lines[i].strip() != ":::": body.append(lines[i]); i += 1
            i += 1
            if kind == "lead":
                out.append(f'<div class="lead"><p>{inline(" ".join(x.strip() for x in body if x.strip()))}</p></div>')
            elif kind == "kpis":
                tiles = []
                for row in [x for x in body if x.strip()]:
                    v, lab, q = [c.strip() for c in row.split("|")]
                    tiles.append(f'<div class="kpi"><div class="kpi-v">{inline(v, False)}</div><div class="kpi-l">{inline(lab, False)}</div><div class="kpi-q">{inline(q, False)}</div></div>')
                out.append(f'<div class="kpis">{"".join(tiles)}</div>')
            elif kind == "uses":
                cols, cur = [], None
                for x in body:
                    x = x.strip()
                    if not x: continue
                    if x.startswith("**"): cur = [x.strip("*"), []]; cols.append(cur)
                    elif x.startswith("- "): cur[1].append(x[2:])
                html_cols = "".join(f'<div class="use-col {"yes" if k == 0 else "no"}"><p class="use-h">{html.escape(h)}</p><ul>{"".join(f"<li>{inline(it, False)}</li>" for it in items)}</ul></div>' for k, (h, items) in enumerate(cols))
                out.append(f'<div class="uses">{html_cols}</div>')
            continue
        # table title (+ table + notes)
        mt = re.match(r"^\*\*表 ([0-9A-D]+-\d+[AB]?)\. (.*?)\*\*$", s)
        if mt or s.startswith("|"):
            cap = ""; tid = ""
            if mt:
                tid = "tbl-" + mt[1].lower()
                cap = f'<p class="tcap"><span class="lab">表 {mt[1]}</span> {inline(mt[2], False)}</p>'
                i += 1
                while i < n and not lines[i].strip(): i += 1
                if i >= n or not lines[i].strip().startswith("|"):
                    out.append(cap); continue
            rows, aligns = [], []
            while i < n and lines[i].strip().startswith("|"):
                row = [x.strip() for x in lines[i].strip().strip("|").split("|")]
                if all(re.fullmatch(r":?-{2,}:?", x.replace(" ", "")) for x in row):
                    aligns = ["R" if x.strip().endswith(":") and not x.strip().startswith(":") else "L" for x in row]
                else: rows.append(row)
                i += 1
            aligns = aligns or ["L"] * len(rows[0])
            notes, i = peek_notes(i)
            ncols = len(rows[0]); nrows = len(rows)
            cls = f"cols-{ncols}" + (" long" if nrows > 14 else "")
            if tid == "tbl-0-1": cls += " nav"
            if tid == "tbl-d-1": cls += " glossary"
            note_html = f'<div class="tnote">{"".join(notes)}</div>' if notes else ""
            out.append(f'<div class="tblock {"long" if nrows > 14 else "mid" if nrows > 8 else ""}" id="{tid}">{cap}{table_html(rows, aligns, cls)}{note_html}</div>' if tid else f'<div class="tblock">{table_html(rows, aligns, cls)}{note_html}</div>')
            continue
        # figure
        if s.startswith("!["):
            m = re.match(r"!\[图 ([0-9A-D]+-\d+)\. ([^\]]*)\]\(([^)]+)\)", s)
            fid = "fig-" + m[1].lower(); src = figmap[m[3]]
            notes, i = peek_notes(i + 1)
            out.append(f'<figure id="{fid}"><figcaption><span class="lab">图 {m[1]}</span> {inline(m[2], False)}</figcaption>'
                       f'<img src="{(Path(figdir) / src).as_uri()}" alt="图 {m[1]}. {html.escape(m[2])}"/>'
                       f'<div class="fnote">{"".join(notes)}</div></figure>')
            continue
        # boxes
        if s.startswith(">"):
            body = []
            while i < n and lines[i].strip().startswith(">"): body.append(lines[i].strip()[1:].strip()); i += 1
            t = " ".join(body)
            if t.startswith("**本章限制。**"):
                rest = t[len("**本章限制。**"):].strip()
                items = [x.strip() for x in re.split(r"\(\d\)", rest) if x.strip()]
                out.append('<aside class="limits"><p class="box-h">本章限制</p><ol>' + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol></aside>")
            elif t.startswith("**方框 1."):
                m = re.match(r"\*\*(方框 1\. .*?)。?\*\*(.*)", t)
                out.append(f'<aside class="box" id="box-1"><p class="box-h">{inline(m[1], False)}</p><p>{inline(m[2].strip())}</p></aside>')
            elif t.startswith("**示意："):
                m = re.match(r"\*\*(示意：.*?)。?\*\*(.*)", t)
                out.append(f'<aside class="box r1"><p class="box-h">{inline(m[1], False)}</p><p>{inline(m[2].strip())}</p></aside>')
            else:
                out.append(f'<aside class="box"><p>{inline(t)}</p></aside>')
            continue
        # lists
        if re.match(r"^\d+\. ", s) or s.startswith("- "):
            ordered = bool(re.match(r"^\d+\. ", s)); items = []
            while i < n and (re.match(r"^\d+\. ", lines[i].strip()) if ordered else lines[i].strip().startswith("- ")):
                items.append(re.sub(r"^(\d+\. |- )", "", lines[i].strip())); i += 1
            tag = "ol" if ordered else "ul"
            cls = ' class="findings"' if ordered and any(x.startswith("**") for x in items) else ""
            out.append(f"<{tag}{cls}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        # paragraph
        para = [s]; i += 1
        while i < n and lines[i].strip() and not lines[i].strip().startswith(("#", "|", "![", "- ", ">", ":::")) and not re.match(r"^\d+\. ", lines[i].strip()) and not re.match(r"^\*\*表 ", lines[i].strip()):
            para.append(lines[i].strip()); i += 1
        t = " ".join(para)
        if t.startswith("*") and not t.startswith("**"):
            out.append(f'<p class="pnote">{inline(strip_italic(t))}</p>')
        else:
            h = inline(t)
            h = re.sub(r"^<strong>(.*?)</strong>", r'<strong class="runin">\1</strong>', h)
            out.append(f"<p>{h}</p>")
    if in_section: out.append("</section>")
    return meta, "\n".join(out), toc

# ----------------------------------------------------------------------------- page furniture


def cover_art(w=612, h=792, back=False):
    """Original abstract artwork: a sun arc, a field of module cells and grid lines to settlement nodes. Decorative only."""
    g = []
    cx, cy = (w + 40, -60) if not back else (w * 0.5, h + 140)
    for k, r in enumerate(range(150, 520, 46)):
        op = 0.55 - k * 0.055
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#B4523A" stroke-opacity="{op:.2f}" stroke-width="{1.4 if k % 2 else 0.8}"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="112" fill="#B4523A" fill-opacity="0.9"/>')
    if back:
        return "".join(g)
    # module field: skewed rows of cells, fading with distance
    ox, oy, cw, ch, skew = 36, 560, 30, 15, 9
    for row in range(7):
        for col in range(19):
            x = ox + col * (cw + 4) + row * skew; y = oy + row * (ch + 4)
            if x > w - 20: continue
            op = max(0.05, 0.62 - 0.028 * col - 0.03 * row)
            pts = f"{x},{y} {x + cw},{y} {x + cw + skew * 0.6},{y + ch} {x + skew * 0.6},{y + ch}"
            g.append(f'<polygon points="{pts}" fill="#167D8D" fill-opacity="{op * 0.45:.3f}" stroke="#8CC3CB" stroke-opacity="{op:.3f}" stroke-width="0.6"/>')
    # grid lines and settlement nodes
    for k, y in enumerate([512, 528, 544]):
        g.append(f'<line x1="300" y1="{y}" x2="{w}" y2="{y}" stroke="#8CC3CB" stroke-opacity="{0.35 - k * 0.08:.2f}" stroke-width="0.8"/>')
    for x, y in [(330, 512), (402, 528), (468, 512), (540, 544), (588, 528)]:
        g.append(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#0E2338" stroke="#E7B9A8" stroke-width="1.1"/>')
    return "".join(g)


WORDMARK = ('<svg class="mark" viewBox="0 0 24 24" width="22" height="22"><rect x="1" y="1" width="10" height="10" fill="#B4523A"/>'
            '<rect x="13" y="1" width="10" height="10" fill="none" stroke="#8CC3CB" stroke-width="1.6"/>'
            '<rect x="1" y="13" width="10" height="10" fill="none" stroke="#8CC3CB" stroke-width="1.6"/>'
            '<rect x="13" y="13" width="10" height="10" fill="#167D8D"/></svg>')


def cover(meta):
    t = html.escape(meta["title"], quote=False).replace("到", "<br/>到", 1)
    return f'''<section class="cover">
<svg class="art" viewBox="0 0 612 792" width="612" height="792" xmlns="http://www.w3.org/2000/svg">{cover_art()}</svg>
<div class="brand">{WORDMARK}<span>{html.escape(meta["organization"].replace(" LLC", ""))}</span></div>
<div class="cover-main">
<p class="kicker">行业与市场研究</p>
<h1 class="cover-title">{t}</h1>
<p class="cover-sub">{smart(html.escape(meta["subtitle"], quote=False))}</p>
</div>
<div class="cover-foot"><div><span class="k">项目</span><span class="v">{meta["project"]}</span></div><div><span class="k">版本</span><span class="v">{meta["version"]}</span></div><div><span class="k">日期</span><span class="v">{meta["date"]}</span></div><div class="org">{html.escape(meta["organization"])}</div></div>
</section>'''


def back_cover(meta):
    return f'''<section class="backcover">
<svg class="art" viewBox="0 0 612 792" width="612" height="792" xmlns="http://www.w3.org/2000/svg">{cover_art(back=True)}</svg>
<div class="back-main">
<div class="brand">{WORDMARK}<span>{html.escape(meta["organization"].replace(" LLC", ""))}</span></div>
<p class="back-title">{smart(html.escape(meta["title"], quote=False))}</p>
<p class="back-sub">{smart(html.escape(meta["subtitle"], quote=False))}</p>
<p class="back-meta">{meta["project"]} &#183; {meta["version"].lstrip("V")} 版 &#183; {meta["date"]}</p>
<p class="back-note">本报告提供有条件的情景分析，用于市场筛查、采购尽职调查、合同比较和资本回收分析。它不是投资建议、实际资产估值、融资或可融资性意见、税收抵免资格认定，也不是价格预测。本中文版译自英文版 1.0 版；如有歧义，以英文版为准。</p>
<p class="back-org">{html.escape(meta["organization"])}</p>
</div>
</section>'''


def contents(toc):
    rows = []
    for lvl, hid, num, t in toc:
        if lvl == 1:
            lab = num
            rows.append(f'<li class="toc1"><a href="#{hid}"><span class="tn">{lab}</span><span class="tt">{smart(html.escape(t, quote=False))}</span></a></li>')
        else:
            rows.append(f'<li class="toc2"><a href="#{hid}"><span class="tn">{num}</span><span class="tt">{smart(html.escape(t, quote=False))}</span></a></li>')
    return f'<section class="contents"><h1 class="contents-h"><span class="chap-title">目录</span></h1><ul class="toc">{"".join(rows)}</ul></section>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--figures", default=str(PKG / "figures"))
    ap.add_argument("--out", default=str(PKG / "SOLAR-001_V1.0_Integrated-Market-Research-Report-ZH.pdf"))
    ap.add_argument("--html")
    a = ap.parse_args()
    figdir = Path(a.figures).resolve()
    figmap = json.loads((figdir / "Figure-Map.json").read_text())
    meta, body, toc = build_html(SRC.read_text(encoding="utf-8"), figmap, figdir)
    css = (ASSETS / "report.css").read_text(encoding="utf-8").replace("url(fonts/", f"url({(ASSETS / 'fonts').as_uri()}/")
    css = css.replace("RUNNING_TEXT", meta["running"])
    # contents: About page first, then the contents list
    doc = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"/>
<title>{html.escape(meta["title"])}：{html.escape(meta["subtitle"])}</title>
<meta name="author" content="{html.escape(meta["organization"])}"/>
<meta name="description" content="SOLAR-001 行业与市场研究报告，{meta["version"].lstrip("V")} 版（中文版），{meta["date"]}"/>
<meta name="keywords" content="光伏供应链; ERCOT; 大型地面光伏; 价值捕获; 采购; SOLAR-001; {meta["version"]}; 中文版"/>
<meta name="dcterms.created" content="2026-10-10T00:00:00-04:00"/><meta name="dcterms.modified" content="2026-10-10T00:00:00-04:00"/>
<style>{css}</style></head><body>
{cover(meta)}
{contents(toc)}
{body}
{back_cover(meta)}
</body></html>'''
    if a.html: Path(a.html).write_text(doc, encoding="utf-8")
    from weasyprint import HTML
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=doc, base_url=str(PKG)).write_pdf(str(out), uncompressed_pdf=False)
    relative_file_links(out)
    print(out)


def relative_file_links(pdf):
    """WeasyPrint writes links to accompanying research files as absolute paths; rewrite them relative to the package
    root so they resolve wherever the package is extracted (the PDF sits in the package root)."""
    import os, pymupdf
    d = pymupdf.open(str(pdf)); n = 0
    for page in d:
        for l in page.get_links():
            if l["kind"] == pymupdf.LINK_LAUNCH and os.path.isabs(l.get("file", "")):
                rel = os.path.relpath(l["file"], PKG).replace("\\", "/")
                spec = "<</Type/Filespec/F" + pymupdf.get_pdf_str(rel) + "/UF" + pymupdf.get_pdf_str(rel) + ">>"
                d.xref_set_key(l["xref"], "A", "<</S/Launch/F" + spec + ">>"); n += 1
    tmp = Path(str(pdf) + ".tmp")
    d.save(str(tmp), garbage=3, deflate=True); d.close(); tmp.replace(pdf)
    return n


if __name__ == "__main__":
    main()
