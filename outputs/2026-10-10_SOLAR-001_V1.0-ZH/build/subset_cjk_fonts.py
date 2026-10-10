"""SOLAR-001 V1.0 Chinese edition - make the embedded Noto CJK SC subsets in assets/fonts/.

The full Noto Serif CJK SC / Noto Sans CJK SC OTFs (SIL OFL 1.1, https://github.com/notofonts/noto-cjk) are ~16-25 MB
each, so the package ships subsets covering: all GB 2312 characters, CJK and full-width punctuation, general punctuation,
Latin-1, and every character of the Chinese Markdown source. The subsets are converted from CID-keyed CFF outlines to
TrueType (quadratic) outlines, because WeasyPrint 70 does not draw the CID-keyed CFF glyphs. Only needed when the text gains
a character outside that set (build/check_fonts.py reports this).
Usage: python3 build/subset_cjk_fonts.py FULL_FONT_DIR
"""
import sys
from pathlib import Path
from fontTools import subset
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import newTable

PKG = Path(__file__).resolve().parents[1]
SRC = PKG / "source" / "SOLAR-001_V1.0_Report-ZH.md"
FONTS = {"NotoSerifCJKsc-Regular.otf": "NotoSerifSC-Regular-subset.ttf", "NotoSerifCJKsc-Bold.otf": "NotoSerifSC-Bold-subset.ttf",
         "NotoSansCJKsc-Regular.otf": "NotoSansSC-Regular-subset.ttf", "NotoSansCJKsc-Medium.otf": "NotoSansSC-Medium-subset.ttf",
         "NotoSansCJKsc-Bold.otf": "NotoSansSC-Bold-subset.ttf"}


def cff_to_glyf(font, max_err=1.0):
    """CFF -> TrueType outlines (after fontTools' Snippets/otf2ttf.py)."""
    font.recalcBBoxes = True  # glyf/maxp/head bounds and point counts are computed on compile
    order = font.getGlyphOrder(); gs = font.getGlyphSet(); quad = {}
    for g in order:
        pen = TTGlyphPen(gs); gs[g].draw(Cu2QuPen(pen, max_err, reverse_direction=True)); quad[g] = pen.glyph()
    font["loca"] = newTable("loca"); font["glyf"] = glyf = newTable("glyf"); glyf.glyphOrder = order; glyf.glyphs = quad
    del font["CFF "]
    if "VORG" in font: del font["VORG"]
    for gl in quad.values(): gl.recalcBounds(glyf)
    glyf.compile(font)
    hmtx = font["hmtx"]
    for g, gl in glyf.glyphs.items():
        if hasattr(gl, "xMin"): hmtx[g] = (hmtx[g][0], gl.xMin)
    font["maxp"] = maxp = newTable("maxp")
    maxp.tableVersion = 0x00010000
    for k in ("maxZones",): setattr(maxp, k, 1)
    for k in ("maxTwilightPoints", "maxStorage", "maxFunctionDefs", "maxInstructionDefs", "maxStackElements", "maxSizeOfInstructions", "maxComponentElements"):
        setattr(maxp, k, 0)
    post = font["post"]; post.formatType = 3.0; post.extraNames = []; post.mapping = {}
    font.sfntVersion = "\000\001\000\000"


def charset():
    cps = set(range(0x20, 0x7F)) | set(range(0xA0, 0x180)) | set(range(0x2000, 0x2070)) | set(range(0x2100, 0x2200))
    cps |= set(range(0x3000, 0x3040)) | set(range(0xFF00, 0xFFF0)) | set(range(0x2460, 0x24FF))
    for hi in range(0xA1, 0xF8):  # GB 2312 rows
        for lo in range(0xA1, 0xFF):
            try: cps.add(ord(bytes([hi, lo]).decode("gb2312")))
            except UnicodeDecodeError: pass
    if SRC.exists(): cps |= {ord(c) for c in SRC.read_text(encoding="utf-8")}
    return sorted(cps)


def main():
    full = Path(sys.argv[1]); cps = charset()
    for src, dst in FONTS.items():
        opts = subset.Options(); opts.layout_features = ["*"]; opts.name_IDs = ["*"]; opts.notdef_outline = True; opts.drop_tables += ["DSIG"]
        f = subset.load_font(str(full / src), opts); s = subset.Subsetter(opts); s.populate(unicodes=cps); s.subset(f)
        cff_to_glyf(f)
        out = PKG / "assets" / "fonts" / dst; f.save(str(out))
        print(dst, out.stat().st_size)


if __name__ == "__main__":
    main()
