"""Export the report's figures (SVG) to 300-dpi PNG files named by figure number and title."""
import json, re, sys
from pathlib import Path
import pymupdf

src, figdir, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
figmap = json.loads((figdir / "Figure-Map.json").read_text())
rows = []
STOP = {"and", "the", "to", "for", "of", "in", "a", "at", "across", "from", "with"}
for m in re.finditer(r"!\[Figure ([0-9A-Z]+)-(\d+)\. ([^\]]+)\]\((figures/[^)]+)\)", src.read_text(encoding="utf-8")):
    ch, n, title, ref = m.groups()
    ch = ch.zfill(2) if ch.isdigit() else ch
    words = re.sub(r"[^A-Za-z0-9 ]+", " ", title.replace("U.S.", "US").replace("–", " to ").replace("&", "and")).split()
    slug, k = "", 0
    for w in words:
        if len(slug) + len(w) + 1 > 48: break
        slug = f"{slug}-{w}" if slug else w
    while slug.rsplit("-", 1)[-1].lower() in STOP: slug = slug.rsplit("-", 1)[0]
    name = f"Figure-{ch}-{n}_{slug}.png"
    svg = figdir / figmap[ref]
    doc = pymupdf.open(str(svg)); pix = doc[0].get_pixmap(dpi=300, alpha=False); pix.save(str(out / name))
    rows.append((f"Figure {m[1]}-{n}", title, name, pix.width, pix.height))
for r in rows: print(*r, sep=" | ")
print(len(rows), "figures")
