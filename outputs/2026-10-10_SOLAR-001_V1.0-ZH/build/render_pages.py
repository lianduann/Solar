"""Render every PDF page to PNG and build contact sheets for visual inspection.
Usage: python3 build/render_pages.py PDF OUTDIR [--dpi 110] [--per 6]"""
import sys, argparse
from pathlib import Path
import pymupdf
from PIL import Image
ap = argparse.ArgumentParser(); ap.add_argument("pdf"); ap.add_argument("out"); ap.add_argument("--dpi", type=int, default=110); ap.add_argument("--per", type=int, default=6); a = ap.parse_args()
out = Path(a.out); (out / "pages").mkdir(parents=True, exist_ok=True); (out / "sheets").mkdir(exist_ok=True)
doc = pymupdf.open(a.pdf); files = []
for i, p in enumerate(doc):
    f = out / "pages" / f"page-{i + 1:03d}.png"; p.get_pixmap(dpi=a.dpi).save(f); files.append(f)
for k in range(0, len(files), a.per):
    ims = [Image.open(f) for f in files[k:k + a.per]]; w, h = ims[0].size; cols = 3; rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols + 1) * 12, rows * h + (rows + 1) * 12), (120, 120, 120))
    for j, im in enumerate(ims): sheet.paste(im, (12 + (j % cols) * (w + 12), 12 + (j // cols) * (h + 12)))
    sheet.save(out / "sheets" / f"sheet-{k // a.per + 1:02d}_pages-{k + 1:03d}-{k + len(ims):03d}.png")
print(len(files), "pages")
