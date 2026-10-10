"""SOLAR-001 V1.0 - redraw every report exhibit from the retained data tables in the report's visual system.

RENDERING ONLY. The plotting functions are the unchanged upstream code in build/upstream/ (render_all_figures.py,
render_panel_figures.py, chart_theme.py) plus the two finance exhibits whose plotting lines are copied verbatim from the
upstream integrate_finance.py. This script changes presentation only:
  * typeface Liberation Sans (the report's sans-serif), figure width matched to the 6.2 in text column;
  * R1 palette (option 1, navy + brick): the upstream amber is replaced by brick, so no yellow remains; colours only;
  * the in-image headline is removed (the report caption carries the figure number and title); the short in-image
    reading guide (subtitle) is kept;
  * output is vector SVG (text converted to outlines, no font dependency) plus a 200 dpi PNG preview.
No regression, simulation, decomposition, resampling or financial model is executed. Plotted values are recorded in
figures/Figure-Plot-Data.json and compared with the upstream snapshot by build/check_figures.py.

Usage:  python3 build/render_figures.py [--out DIR]      (default: <package>/figures)
"""
import argparse, json, re, sys, textwrap
from pathlib import Path

B = Path(__file__).resolve().parent
PKG = B.parent
sys.path.insert(0, str(B / "upstream"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import chart_theme as T

FONT_DIR = PKG / "assets" / "fonts"
for f in sorted(FONT_DIR.glob("LiberationSans-*.ttf")):
    font_manager.fontManager.addfont(str(f))

T.W = 6.2  # inches; equals the R1 PDF text column (8.5 in - 2 x 1.15 in margins)

# R1 palette (option 1, navy + brick). Colour constants only; every plotting call is the unchanged upstream code.
T.AMBER, T.AMBER_L = "#B4523A", "#E7B9A8"      # former amber -> accent brick
T.BRICK, T.BRICK_L = "#B4523A", "#E7B9A8"      # negative values keep brick
T.SLATE, T.SLATE_L = "#8A9BA8", "#C3CCD4"
T.SAGE = "#6F8A72"                               # fifth categorical colour, used where brick would otherwise appear twice
T.YEAR = {2023: dict(color=T.AMBER, marker="o", ls="-", lab="2023"), 2024: dict(color=T.TEAL, marker="s", ls="--", lab="2024"), 2025: dict(color=T.NAVY, marker="^", ls=":", lab="2025")}
T.ZONE = {"LZ_HOUSTON": (T.SAGE, "o"), "LZ_NORTH": (T.NAVY, "s"), "LZ_SOUTH": (T.AMBER, "^"), "LZ_WEST": (T.TEAL, "D")}
from matplotlib.colors import LinearSegmentedColormap
T.DIVERGING = LinearSegmentedColormap.from_list("brick_neutral_teal", [T.BRICK, "#E2B5A8", "#F4F4F2", "#BFE0E4", T.TEAL])
_apply = T.apply


def apply():
    _apply()
    plt.rcParams.update({"font.family": "Liberation Sans", "svg.fonttype": "path", "svg.hashsalt": "solar-001-v0999-r1",
                         "axes.titlesize": 8.2, "axes.titleweight": "semibold", "axes.labelsize": 7.6,
                         "xtick.labelsize": 7.2, "ytick.labelsize": 7.2, "legend.fontsize": 7.0})


T.apply = apply
OUT = PKG / "figures"
MAP = {}  # upstream png name -> v0999 svg path


def client_text(x):
    if not x: return x
    return (x.replace('empirical candidate', 'multi-year analysis').replace('retained', 'source').replace('first-round', '2025 cross-section')
             .replace('second-round', 'extended analysis').replace('non-DST dates', 'dates excluding DST transition days')
             .replace('node_base', 'Node base').replace('fixed_base', 'Fixed base')
             .replace('coloured', 'colored').replace('colour', 'color'))


def finish(fig, png, title, subtitle=None, note=None, top_pad=0.0, hspace=None, wspace=None, manual=None):
    """V0.999 replacement for chart_theme.finish: no in-image headline or source note (both live in the report caption)."""
    png = Path(png)
    for ax in fig.axes:  # same client-wording substitutions as upstream chart_theme.finish
        for title in (ax.title, ax._left_title, ax._right_title):
            title.set_text(client_text(title.get_text()))
        leg = ax.get_legend()
        if leg is not None:  # legibility only: opaque legend background so reference lines do not run through the text
            leg.set_frame_on(True); leg.get_frame().set_facecolor("white"); leg.get_frame().set_alpha(0.92); leg.get_frame().set_linewidth(0)
    stem = ("empirical_" if png.parent.name == "empirical" else "") + png.stem
    h = fig.get_figheight()
    subtitle = client_text(subtitle)
    sub = textwrap.wrap(subtitle, 120) if subtitle else []
    tl = (0.10 + 0.15 * len(sub) if sub else 0.04) + top_pad
    if sub:
        fig.text(0.006, 1 - 0.06 / h, "\n".join(sub), fontsize=7.4, color=T.MUTED, ha="left", va="top", linespacing=1.3)
    kw = {}
    if hspace is not None: kw["h_pad"] = hspace
    if wspace is not None: kw["w_pad"] = wspace
    if manual:
        tl += 0.30  # room for panel titles, which sit above the axes in manual layouts
        fig.subplots_adjust(left=manual.get("left", 0.09) + 0.02, right=manual.get("right", 0.98), top=1 - tl / h,
                            bottom=0.06 / h + manual.get("bottom_in", 0.55) / h, wspace=manual.get("wspace", 0.35), hspace=manual.get("hspace", 0.3))
    else:
        fig.tight_layout(rect=(0, 0.02, 1, 1 - tl / h), **kw)
    T.snapshot(fig, stem)
    OUT.mkdir(parents=True, exist_ok=True)
    svg = OUT / (stem + ".svg"); prev = OUT / "preview" / (stem + ".png"); prev.parent.mkdir(exist_ok=True)
    fig.savefig(svg, metadata={"Date": None, "Creator": "SOLAR-001 V1.0 render_figures.py"})
    fig.savefig(prev, dpi=200, metadata={"Software": None})
    plt.close(fig)
    MAP["figures/" + ("empirical/" if png.parent.name == "empirical" else "") + png.name] = svg.name
    return svg, prev


T.finish = finish


R1_COLOUR_SWAPS = [  # colour-only substitutions where the R1 palette would otherwise give two series the same hue
    ('color=T.AMBER, marker="o", ms=3.2, label="Mean node price (left)"', 'color=T.NAVY, marker="o", ms=3.2, label="Mean node price (left)"'),
    ('color=T.AMBER, label="FOM, replacement, decommissioning"', 'color=T.BRICK_L, label="FOM, replacement, decommissioning"'),
]


def run_upstream_all():
    import types
    src = (B / "upstream" / "render_all_figures.py").read_text()
    for a, b in R1_COLOUR_SWAPS:
        assert src.count(a) == 1, a
        src = src.replace(a, b)
    R = types.ModuleType("render_all_figures"); R.__file__ = str(B / "upstream" / "render_all_figures.py")
    exec(compile(src, R.__file__, "exec"), R.__dict__)
    R.PK = PKG; R.D = PKG / "data"; R.SUP = R.D / "supplement"; R.EMP = R.D / "empirical"; R.TAB = R.EMP / "tables"; R.OUT = OUT
    R.rec = lambda *a, **k: None  # upstream lineage writer not used; V0.999 lineage is written below
    for f in R.REG:
        f()


def run_upstream_panel():
    src = (B / "upstream" / "render_panel_figures.py").read_text()
    src = src.replace("D=Path(__file__).resolve().parents[1]", "D=PKG")
    # legibility only: white backing for total labels that otherwise sit on top of the stacked bars
    src = src.replace("textcoords='offset points',ha='center',fontsize=8,fontweight='bold')", "textcoords='offset points',ha='center',fontsize=8,fontweight='bold',zorder=9,bbox=dict(boxstyle='round,pad=0.15',fc='white',ec='none',alpha=0.9))")
    # R1 palette: solar (former amber) and net load (brick) would share a hue; net load uses slate
    src = src.replace("('net_load_mw','Load less wind and solar',T.BRICK,'--')", "('net_load_mw','Load less wind and solar',T.SLATE,'--')")
    src = src.replace("(D/'support/Panel-Figure-Lineage.json').write_text(json.dumps(lineage,indent=2))", "pass")
    src = src.replace(" lineage.append(dict(figure=str(png.relative_to(D)),vector=str(vec.relative_to(D)),inputs=inputs,columns=columns,operation=ops,input_sha256={i:hashlib.sha256((D/i).read_bytes()).hexdigest() for i in inputs},png_sha256=hashlib.sha256(png.read_bytes()).hexdigest()))", " lineage.append(name)")
    exec(compile(src, "render_panel_figures.py", "exec"), {"__name__": "panel", "PKG": PKG})


def run_finance():
    # Plotting lines copied verbatim from upstream scripts/integrate_finance.py (lines 23-24); inputs are the tables it wrote.
    import pandas as pd
    th = T; D = PKG
    g = pd.read_csv(PKG / "data/finance/EIA-2025-Tracking-Chart.csv")
    cost = pd.read_csv(PKG / "data/finance/Qualified-Investment-Comparisons.csv")
    th.apply();fig,ax=th.newfig(4.8);labels=[n.replace(' Energy Project','').replace(' Solar Project','')+(' *' if pid==63233 else '') for n,pid in zip(g.plant_name,g.plant_id)];ax.barh(labels,g.annual_capacity_factor_ac*100,color=th.TEAL);ax.axvline(33.38,color=th.AMBER,ls='--',label='Simulated potential 33.38%');ax.axvline(28.29,color=th.NAVY,ls=':',label='Simulated delivered 28.29%');ax.set_xlim(0,38);ax.set_xlabel('Annual AC capacity factor (%)');ax.legend(loc='lower right',fontsize=7);th.finish(fig,D/'figures/Finance_Operating_CF.png','Operating output provides a check on the simulated profile','2025 | EIA-record Pecos cohort | standalone PV, tracking Y | * county conflict')
    th.apply();fig,ax=th.newfig(3.3);c=cost.sort_values('result');ax.barh(c.project,c.result/1000,color=th.NAVY);ax.set_xlabel('Self-reported qualified investment / 2025 AC capacity ($/Wac)');ax.set_xlim(0,1.25);th.finish(fig,D/'figures/Finance_Qualified_Investment.png','Public investment filings cover a narrower scope than total project cost','Mid-2023 filings | nominal dollars | five selected plants | not IRR or all-in CAPEX')


def run_r1():
    """R1 addition: price ladder for Chapter 1. Values come from the V0.999 report and data/r1 (no model is run)."""
    import pandas as pd
    ptc = pd.read_csv(PKG / "data/r1/PTC-Illustration.csv")
    pt = ptc[ptc.variant.str.startswith("Full rate")].fixed_route_breakeven_usd_mwh
    lv = pd.read_csv(PKG / "data/r1/Market-References.csv")
    lv = lv[lv["item"] == "LevelTen solar PPA price index P25 ERCOT"].value.astype(float)
    rows = [  # (group, label, low, high, colour)
        ("paid", "West hub, solar-weighted, Jan–Sep 2026 (fixed 2025 profile)", 18.24, 18.24, T.SLATE),
        ("paid", "West hub, solar-weighted, 2025", 21.46, 21.46, T.SLATE),
        ("paid", "Reference node, gross value per delivered MWh, 2025", 26.4, 26.4, T.SLATE),
        ("offer", "ERCOT solar offers, LevelTen P25, 4Q24–4Q25", float(lv.iloc[:5].min()), float(lv.iloc[:5].max()), T.TEAL),
        ("need", "Node fixed price, production credit (illustration)", float(pt.min()), float(pt.max()), T.BRICK_L),
        ("need", "Node fixed price, illustrative 30% ITC", 53.51, 53.51, T.NAVY),
        ("need", "Node fixed price, no credit, all output paid", 55.91, 55.91, T.NAVY),
        ("need", "Node fixed price, no credit, 15.24% unpaid (base)", 65.97, 65.97, T.NAVY),
        ("need", "West hub hedge 10–15 yr + node tail, no credit", 60.6, 84.8, T.NAVY),
    ]
    T.apply(); fig, ax = T.newfig(3.55)
    y = list(range(len(rows)))[::-1]
    for yy, (g, lab, lo, hi, c) in zip(y, rows):
        if hi - lo > 0.05: ax.barh(yy, hi - lo, 0.5, left=lo, color=c)
        else: ax.plot([lo], [yy], marker="o", ms=6, color=c, ls="none")
        ax.text(hi + 2.4, yy, f"${lo:.1f}" + (f"–{hi:.1f}" if hi - lo > 0.05 else ""), va="center", fontsize=7, color=T.INK)
    ax.set_yticks(y); ax.set_yticklabels([r[1] for r in rows]); ax.set_xlim(0, 100); ax.set_xlabel("$/MWh; bases differ (see Table 1-2), so read as orders of magnitude")
    for yy in (5.5, 4.5): ax.axhline(yy, color=T.AXIS, lw=0.6, ls=(0, (2, 2)))
    T.hgrid(ax, "x")
    T.finish(fig, PKG / "figures/R1_price_ladder.png", "What solar output earned, what contracts offered and what this project needs",
             "Grey: market value of solar output; teal: public ERCOT offer index; navy: break-even prices from this report; light brick: production-credit illustration")


def main():
    global OUT
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=str(PKG / "figures")); a = ap.parse_args()
    OUT = Path(a.out).resolve()
    T.apply()
    run_upstream_all(); run_upstream_panel(); run_finance(); run_r1()
    (OUT / "Figure-Plot-Data.json").write_text(json.dumps(T.SNAP, indent=1, sort_keys=True))
    (OUT / "Figure-Map.json").write_text(json.dumps(MAP, indent=1, sort_keys=True))
    print(f"rendered {len(MAP)} exhibits to {OUT}")


if __name__ == "__main__":
    main()
