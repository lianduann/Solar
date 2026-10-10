"""Unified chart theme for the SOLAR-001 Integrated Research Release Candidate v0.4. Rendering only; see support/Visual-Style-Guide.md."""
import textwrap
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

SNAP = {}                      # plotted-data snapshots per exhibit (for the rendering-fidelity check)
W = 7.05                      # inches: matches the 508 pt text column of the PDF, so font sizes below are the final printed sizes
NAVY, TEAL, AMBER, SLATE, BRICK = "#17324D", "#167D8D", "#C58A36", "#718096", "#B35B54"
NAVY_L, TEAL_L, AMBER_L, SLATE_L, BRICK_L = "#8FA3B8", "#8CC3CB", "#E3C28F", "#B9C2CE", "#DDB1AC"
INK, MUTED, GRID, AXIS = "#1F2933", "#5F6B76", "#E6EAEE", "#A9B3BC"
# explicit semantic mappings (same entity -> same colour/marker in every exhibit)
YEAR = {2023: dict(color=AMBER, marker="o", ls="-", lab="2023"), 2024: dict(color=TEAL, marker="s", ls="--", lab="2024"), 2025: dict(color=NAVY, marker="^", ls=":", lab="2025")}
ZONE = {"LZ_HOUSTON": (BRICK, "o"), "LZ_NORTH": (NAVY, "s"), "LZ_SOUTH": (AMBER, "^"), "LZ_WEST": (TEAL, "D")}
# separate palettes for quantitative scales
DIVERGING = LinearSegmentedColormap.from_list("brick_neutral_teal", [BRICK, "#E9C9C4", "#F6F3EE", "#BFE0E4", TEAL])   # lightness varies monotonically on each side, interpretable in grayscale
SEQ_NAVY = ["#17324D", "#3B5A78", "#6B88A3", "#A1B5C7", "#D2DDE6"]

def apply():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.titlesize": 8.6, "axes.titleweight": "bold", "axes.titlelocation": "left", "axes.labelsize": 7.8, "axes.labelcolor": MUTED,
        "xtick.labelsize": 7.4, "ytick.labelsize": 7.4, "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK, "axes.edgecolor": AXIS, "axes.linewidth": 0.7, "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True, "legend.fontsize": 7, "legend.frameon": False, "figure.dpi": 100, "savefig.dpi": 250, "axes.unicode_minus": True,
        "lines.linewidth": 1.6, "xtick.major.size": 2.5, "ytick.major.size": 2.5, "pdf.fonttype": 42, "svg.fonttype": "none", "text.parse_math": False})

def fmt(v, d=1, pct=False, plus=False):
    s = f"{abs(v):,.{d}f}"; sign = "−" if v < 0 else ("+" if plus and v > 0 else "")
    return f"{sign}{s}{'%' if pct else ''}"

def newfig(h, ncols=1, nrows=1, **kw):
    fig, ax = plt.subplots(nrows, ncols, figsize=(W, h), **kw); return fig, ax

def finish(fig, png, title, subtitle=None, note=None, top_pad=0.0, hspace=None, wspace=None, manual=None):
    # Client edition: neutral source language; plot data and qualifications unchanged.
    import re
    def client_text(x):
        if x is None: return x
        return x.replace('empirical candidate', 'multi-year analysis').replace('retained', 'source').replace('first-round', '2025 cross-section').replace('second-round', 'extended analysis').replace('non-DST dates', 'dates excluding DST transition days').replace('node_base', 'Node base').replace('fixed_base', 'Fixed base')
    title = client_text(title)
    subtitle = client_text(subtitle)
    note = None  # Source and interpretation notes live once in the manuscript captions.
    for ax in fig.axes:
        ax.set_title(client_text(ax.get_title()))
    """Title (left-aligned, bold, wrapped), optional subtitle, source note at the bottom (wrapped), tight layout between them; writes PNG + vector PDF master."""
    h = fig.get_figheight(); tlines = textwrap.wrap(title, 80); sub = textwrap.wrap(subtitle, 118) if subtitle else []
    tl = 0.12 + 0.185 * len(tlines) + (0.04 + 0.15 * len(sub) if sub else 0) + 0.16 + top_pad
    lines = textwrap.wrap(note, 122) if note else []; nh = (0.105 * len(lines) + 0.16) if lines else 0.06
    fig.text(0.006, 1 - 0.08 / h, "\n".join(tlines), fontsize=9.6, fontweight="bold", color=INK, ha="left", va="top", linespacing=1.25)
    if sub: fig.text(0.006, 1 - (0.08 + 0.185 * len(tlines) + 0.03) / h, "\n".join(sub), fontsize=7.6, color=MUTED, ha="left", va="top")
    if lines: fig.text(0.006, 0.05 / h, "\n".join(lines), fontsize=6.5, color=MUTED, ha="left", va="bottom", linespacing=1.3)
    kw = {}
    if hspace is not None: kw["h_pad"] = hspace
    if wspace is not None: kw["w_pad"] = wspace
    if manual: fig.subplots_adjust(left=manual.get('left', 0.09), right=manual.get('right', 0.98), top=1 - tl / h, bottom=nh / h + manual.get('bottom_in', 0.55) / h, wspace=manual.get('wspace', 0.35), hspace=manual.get('hspace', 0.3))
    else: fig.tight_layout(rect=(0, nh / h, 1, 1 - tl / h), **kw)
    png = Path(png); png.parent.mkdir(parents=True, exist_ok=True); snapshot(fig, ('empirical/' if png.parent.name == 'empirical' else '') + png.stem)
    fig.savefig(png, metadata={"Software": None}); vec = png.parent / "vector" / (png.stem + ".pdf") if png.parent.name != "empirical" else png.parent.parent / "vector" / ("empirical_" + png.stem + ".pdf")
    vec.parent.mkdir(parents=True, exist_ok=True); fig.savefig(vec, metadata={"CreationDate": None, "Creator": "SOLAR-001 render_all_figures.py"}); plt.close(fig); return png, vec


def snapshot(fig, name):
    """Record what was actually drawn (line data, bar/histogram rectangles, scatter offsets, image arrays) so that scripts/verify_figure_fidelity.py can compare it with the retained tables."""
    import numpy as np
    from matplotlib.lines import Line2D
    from matplotlib.patches import Rectangle
    out = []
    for i, ax in enumerate(fig.axes):
        d = {"axes": i, "title": ax.get_title(), "xlabel": ax.get_xlabel(), "ylabel": ax.get_ylabel(), "lines": [], "rects": [], "scatter": [], "images": [], "xscale": ax.get_xscale(), "xlim": [float(v) for v in ax.get_xlim()], "ylim": [float(v) for v in ax.get_ylim()]}
        for ln in ax.lines:
            x, y = np.asarray(ln.get_xdata(), dtype=float), np.asarray(ln.get_ydata(), dtype=float)
            if len(x) == 0 or len(x) != len(y): continue
            rec = {"label": ln.get_label(), "n": int(len(x))}
            if len(x) <= 400: rec.update(x=[round(float(v), 6) for v in x], y=[round(float(v), 6) for v in y])
            else: rec.update(x_sum=float(np.nansum(x)), y_sum=float(np.nansum(y)), x_min=float(np.nanmin(x)), x_max=float(np.nanmax(x)), y_min=float(np.nanmin(y)), y_max=float(np.nanmax(y)), y_first=[round(float(v), 6) for v in y[:5]], y_last=[round(float(v), 6) for v in y[-5:]])
            d["lines"].append(rec)
        for p in ax.patches:
            if isinstance(p, Rectangle) and p.get_width() != 0 or isinstance(p, Rectangle) and p.get_height() != 0: d["rects"].append([round(float(v), 6) for v in (p.get_x(), p.get_y(), p.get_width(), p.get_height())])
        for c in ax.collections:
            off = getattr(c, "get_offsets", lambda: None)()
            if off is not None and len(off): d["scatter"].append([[round(float(a), 6), round(float(b), 6)] for a, b in np.asarray(off)[:2000]])
        for im in ax.images: d["images"].append([[round(float(v), 6) for v in row] for row in np.asarray(im.get_array())])
        out.append(d)
    SNAP[name] = out

def hgrid(ax, which="y"):
    ax.grid(False); ax.grid(True, axis=which, color=GRID, linewidth=0.6)
