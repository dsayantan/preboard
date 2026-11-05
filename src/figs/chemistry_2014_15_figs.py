"""Figures for Chemistry pre-board 2014-15 (chemistry_2014_15, chemistry_2014_15_prac)."""
import math
from svg import Fig


def _ring(f, cx, cy, r=26):
    v = [(cx + r * math.cos(math.radians(-90 + 60 * k)), cy + r * math.sin(math.radians(-90 + 60 * k)))
         for k in range(6)]
    for k in range(6):
        a, b = v[k], v[(k + 1) % 6]
        f.line(f"{a[0]:.1f}", f"{a[1]:.1f}", f"{b[0]:.1f}", f"{b[1]:.1f}")
    for k in (0, 2, 4):
        a, b = v[k], v[(k + 1) % 6]
        ax = cx + .78 * (a[0] - cx); ay = cy + .78 * (a[1] - cy)
        bx = cx + .78 * (b[0] - cx); by = cy + .78 * (b[1] - cy)
        mx, my = (ax + bx) / 2, (ay + by) / 2
        f.line(f"{mx+.8*(ax-mx):.1f}", f"{my+.8*(ay-my):.1f}", f"{mx+.8*(bx-mx):.1f}", f"{my+.8*(by-my):.1f}", w=1.4)
    return v


def _top(f, v, label, L=20, size=14):
    x, y = v[0]
    f.line(f"{x:.1f}", f"{y:.1f}", f"{x:.1f}", f"{y-L:.1f}")
    f.text(f"{x:.1f}", f"{y-L-4:.1f}", label, size=size)


def _octa(f, cx, cy, lig, L=58, metal="Co", size=14):
    """Octahedron. lig = dict(up, down, fl, fr, br, bl) of labels.
    Each label is (text, anchor_offset) or text. Bonds solid, equatorial plane dashed."""
    pos = dict(up=(0, -L), down=(0, L), fl=(-L, .28 * L), fr=(.55 * L, .5 * L),
               br=(L, -.28 * L), bl=(-.55 * L, -.5 * L))
    eq = ["fl", "fr", "br", "bl"]
    pts = [(cx + pos[k][0], cy + pos[k][1]) for k in eq]
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts) + " Z", w=1, dash="4 3", color="#888")
    for k, (dx, dy) in pos.items():
        n = math.hypot(dx, dy)
        sx, sy = cx + 12 * dx / n, cy + 12 * dy / n
        ex, ey = cx + dx, cy + dy
        f.line(f"{sx:.1f}", f"{sy:.1f}", f"{ex:.1f}", f"{ey:.1f}", w=1.8)
    f.text(cx, cy + 5, metal, size=size, bold=True)
    for k, lab in lig.items():
        dx, dy = pos[k]
        ex, ey = cx + dx, cy + dy
        anchor = "middle"
        if k == "up":
            ty, tx = ey - 6, ex
        elif k == "down":
            ty, tx = ey + 16, ex
        elif dx < 0:
            tx, ty, anchor = ex - 3, ey + 5, "end"
        else:
            tx, ty, anchor = ex + 3, ey + 5, "start"
        if isinstance(lab, tuple):          # (text, anchor) override
            lab, anchor = lab
            if anchor == "start" and k in ("up", "down"):
                tx = ex - 5
        col = "#c0392b" if lab in ("Cl", "NO₂", "ONO") else "#111"
        f.text(f"{tx:.1f}", f"{ty:.1f}", lab, size=size - 1, anchor=anchor, color=col)


def _bracket(f, x1, y1, x2, y2, charge=""):
    f.path(f"M {x1+8} {y1} L {x1} {y1} L {x1} {y2} L {x1+8} {y2}", w=1.4)
    f.path(f"M {x2-8} {y1} L {x2} {y1} L {x2} {y2} L {x2-8} {y2}", w=1.4)
    if charge:
        f.text(x2 + 4, y1 + 10, charge, size=13, anchor="start")


# --------------------------------------------------------------- Q1(c)(ii)
def fig_q1c2_pt():
    """[Pt(NH3)4Cl2]2+ : trans and cis forms (octahedral, Pt(IV), d2sp3)."""
    f = Fig(560, 250, "fig_q1c2_pt")
    a = "NH₃"
    _octa(f, 140, 115, dict(up="Cl", down="Cl", fl=a, fr=a, br=a, bl=a), metal="Pt")
    _bracket(f, 50, 30, 235, 200, "2+")
    f.text(140, 238, "trans-[Pt(NH₃)₄Cl₂]²⁺", size=13)
    _octa(f, 410, 115, dict(up="Cl", down=a, fl=a, fr="Cl", br=a, bl=a), metal="Pt")
    _bracket(f, 320, 30, 505, 200, "2+")
    f.text(410, 238, "cis-[Pt(NH₃)₄Cl₂]²⁺", size=13)
    return f.svg()


# --------------------------------------------------------------- Q3(a)
T = [0, 75, 119, 193]
V = [9.62, 12.10, 13.10, 14.75]
VINF = 21.05


def fig_q3a_graph():
    """log10(Vinf - Vt) against t: a straight line => first order. Best fit + slope triangle."""
    f = Fig(520, 360, "fig_q3a_graph")
    x0, y0, W, H = 80, 300, 400, 250
    X = lambda t: x0 + W * t / 220
    Y = lambda v: y0 - H * (v - 0.75) / 0.35
    for t in range(0, 221, 20):
        f.line(X(t), Y(0.75), X(t), Y(1.10), color="#e3e8ef", w=0.8)
    for k in range(0, 8):
        v = 0.75 + 0.05 * k
        f.line(X(0), Y(v), X(220), Y(v), color="#e3e8ef", w=0.8)
        f.text(X(0) - 6, Y(v) + 4, f"{v:.2f}", size=11, anchor="end")
    for t in range(0, 221, 40):
        f.text(X(t), y0 + 16, str(t), size=11)
    f.line(X(0), Y(0.75), X(220), Y(0.75), w=1.3)
    f.line(X(0), Y(0.75), X(0), Y(1.10), w=1.3)
    f.text(X(110), y0 + 36, "time t / min", size=13)
    f.raw(f'<text x="22" y="{Y(0.925):.1f}" font-size="13" text-anchor="middle" font-family="Times New Roman,serif" '
          f'transform="rotate(-90 22 {Y(0.925):.1f})">log₁₀(V∞ − Vt)</text>')
    f.text(X(0) + 4, Y(1.10) - 6, "origin shifted: y-axis starts at 0.75", size=10, anchor="start", color="#666")
    y = [math.log10(VINF - v) for v in V]
    n = 4; sx = sum(T); sy = sum(y); sxx = sum(t * t for t in T); sxy = sum(a * b for a, b in zip(T, y))
    m = (n * sxy - sx * sy) / (n * sxx - sx * sx); c = (sy - m * sx) / n
    f.line(X(0), Y(c), X(215), Y(c + m * 215), color="#1f4e8c", w=1.8)
    for t, v in zip(T, y):
        f.circle(f"{X(t):.1f}", f"{Y(v):.1f}", 4, color="#c0392b", fill="#c0392b")
    # slope triangle between t = 30 and t = 180 on the line
    ta, tb = 30, 180
    ya, yb = c + m * ta, c + m * tb
    f.line(X(ta), Y(ya), X(tb), Y(ya), color="#2e7d32", w=1.3, dash="5 3")
    f.line(X(tb), Y(ya), X(tb), Y(yb), color="#2e7d32", w=1.3, dash="5 3")
    f.text(X((ta + tb) / 2), Y(ya) - 6, "Δt = 150 min", size=12, color="#2e7d32")
    f.text(X(tb) + 6, Y((ya + yb) / 2) + 4, f"Δy = {yb-ya:.3f}", size=12, color="#2e7d32", anchor="start")
    return f.svg()


# --------------------------------------------------------------- Q4(b)
def fig_q4b_cell():
    """Daniell cell with a salt bridge."""
    f = Fig(540, 330, "fig_q4b_cell")
    # beakers
    for x in (60, 320):
        f.path(f"M {x} 150 L {x} 300 L {x+140} 300 L {x+140} 150", w=1.8)
        f.rect(x + 2, 190, 136, 108, color="none", fill="#dbe9f7")
    f.text(130, 290, "ZnSO₄(aq)", size=13)
    f.text(390, 290, "CuSO₄(aq)", size=13)
    # electrodes
    f.rect(95, 110, 16, 160, fill="#9aa5b1")
    f.rect(410, 110, 16, 160, fill="#c97b4a")
    f.text(85, 230, "Zn", size=14, bold=True, anchor="end")
    f.text(436, 230, "Cu", size=14, bold=True, anchor="start")
    f.text(40, 128, "anode (−)", size=12, anchor="start")
    f.text(432, 128, "cathode (+)", size=12, anchor="start")
    # salt bridge
    f.path("M 165 270 L 165 140 Q 165 125 180 125 L 340 125 Q 355 125 355 140 L 355 270", w=14, color="#b9b9b9")
    f.path("M 165 270 L 165 140 Q 165 125 180 125 L 340 125 Q 355 125 355 140 L 355 270", w=10, color="#f3f3f3")
    f.text(260, 108, "salt bridge (KNO₃ or KCl in agar)", size=11)
    f.arrow(285, 165, 185, 165, color="#7d3c98", w=1.3); f.text(292, 169, "NO₃⁻", size=12, anchor="start", color="#7d3c98")
    f.arrow(235, 200, 335, 200, color="#c0392b", w=1.3); f.text(228, 204, "K⁺", size=12, anchor="end", color="#c0392b")
    # external circuit
    f.line(103, 110, 103, 40); f.line(103, 40, 230, 40)
    f.line(290, 40, 418, 40); f.line(418, 40, 418, 110)
    f.circle(260, 40, 22, fill="#fff"); f.text(260, 46, "V", size=16, bold=True)
    f.arrow(140, 28, 200, 28, color="#1f4e8c", w=1.5); f.text(170, 20, "e⁻ flow", size=12, color="#1f4e8c")
    return f.svg()


# --------------------------------------------------------------- Q7(b)
def fig_q7b_vbt():
    """VBT: Fe3+ free ion, and [Fe(CN)6]3- with d2sp3 (inner-orbital) hybridisation."""
    f = Fig(600, 230, "fig_q7b_vbt")
    bw = 30
    def boxes(x, y, n):
        for i in range(n):
            f.rect(x + i * bw, y, bw, 30, w=1.3)
    def e(x, y, i, s):  # s: 'u' up, 'p' pair, 'L' ligand pair
        cx = x + i * bw + bw / 2
        if s == "u":
            f.text(cx, y + 22, "↑", size=18)
        elif s == "p":
            f.text(cx, y + 22, "↑↓", size=16)
        elif s == "L":
            f.text(cx, y + 22, "××", size=14, color="#c0392b")
    xs = dict(d=150, s=330, p=380)
    for row, (y, title, dd, ss, pp) in enumerate((
            (40, "Fe³⁺ (free ion)  3d⁵", "uuuuu", "", ""),
            (130, "[Fe(CN)₆]³⁻", "ppuLL", "L", "LLL"))):
        f.text(10, y + 20, title, size=13, anchor="start")
        boxes(xs["d"], y, 5); boxes(xs["s"], y, 1); boxes(xs["p"], y, 3)
        for i, s in enumerate(dd): e(xs["d"], y, i, s)
        for i, s in enumerate(ss): e(xs["s"], y, i, s)
        for i, s in enumerate(pp): e(xs["p"], y, i, s)
        if row == 0:
            f.text(xs["d"] + 75, y - 8, "3d", size=13); f.text(xs["s"] + 15, y - 8, "4s", size=13)
            f.text(xs["p"] + 45, y - 8, "4p", size=13)
    f.path(f"M {xs['d']+60} 168 L {xs['d']+60} 178 L {xs['p']+90} 178 L {xs['p']+90} 168", w=1.2, color="#c0392b")
    f.text((xs['d'] + 60 + xs['p'] + 90) / 2, 196, "d²sp³ hybrid orbitals ← 6 electron pairs from 6 CN⁻", size=12, color="#c0392b")
    f.text(xs["d"] + 75, 218, "CN⁻ (strong field) pairs up 3d electrons: 1 unpaired e⁻", size=12)
    return f.svg()


# --------------------------------------------------------------- Q7(c)
def fig_q7c_linkage():
    """Linkage isomers: nitro (Co–NO2) and nitrito (Co–ONO)."""
    f = Fig(600, 260, "fig_q7c_linkage")
    a = "NH₃"
    _octa(f, 140, 125, dict(up=("NO₂", "start"), down=a, fl=a, fr=a, br=a, bl=a))
    _bracket(f, 50, 40, 235, 205, "2+")
    f.text(268, 128, "Cl₂", size=14, anchor="start")
    f.text(150, 238, "[Co(NH₃)₅(NO₂)]Cl₂ — bonded through N", size=12)
    f.text(150, 254, "pentaamminenitrito-N-cobalt(III) chloride", size=11, color="#555")
    _octa(f, 430, 125, dict(up=("ONO", "start"), down=a, fl=a, fr=a, br=a, bl=a))
    _bracket(f, 340, 40, 525, 205, "2+")
    f.text(558, 128, "Cl₂", size=14, anchor="start")
    f.text(440, 238, "[Co(NH₃)₅(ONO)]Cl₂ — bonded through O", size=12)
    f.text(440, 254, "pentaamminenitrito-O-cobalt(III) chloride", size=11, color="#555")
    return f.svg()


# --------------------------------------------------------------- Q9(a)  (redrawn from the question)
def fig_q9a_scheme():
    f = Fig(640, 170, "fig_q9a_scheme")
    xs = [40, 190, 320, 460, 590]
    labs = ["HCOOH", "[A]", "[B]", "[C]", "[D]"]
    reag = ["LiAlH₄", "P/I₂", "KCN", "H₃O⁺"]
    for x, l in zip(xs, labs):
        f.text(x, 50, l, size=15)
    for i in range(4):
        x1 = xs[i] + (38 if i == 0 else 22); x2 = xs[i + 1] - 22
        f.arrow(x1, 45, x2, 45)
        f.text((x1 + x2) / 2, 35, reag[i], size=12)
    f.arrow(590, 60, 590, 120)
    f.text(584, 95, "NH₃", size=12, anchor="end"); f.text(596, 95, "Heat", size=12, anchor="start")
    f.text(590, 140, "[E]", size=15)
    f.arrow(568, 135, 482, 135)
    f.text(525, 125, "Ni/H₂", size=12)
    f.text(460, 140, "[F]", size=15)
    return f.svg()


# --------------------------------------------------------------- Q10(a)
def fig_q10a_scheme():
    """Benzaldehyde (A): Cannizzaro -> B + C; B -> A by oxidation; A, C with PCl5 -> D, E."""
    f = Fig(640, 360, "fig_q10a_scheme")
    def mol(cx, cy, grp, name):
        v = _ring(f, cx, cy); _top(f, v, grp); f.text(cx, cy + 46, name, size=12)
    mol(70, 110, "CHO", "A  benzaldehyde")
    f.arrow(120, 105, 255, 105)
    f.text(188, 92, "1. conc. NaOH", size=12); f.text(188, 124, "2. H₃O⁺", size=12)
    mol(320, 110, "CH₂OH", "B  benzyl alcohol")
    f.text(395, 110, "+", size=20)
    mol(470, 110, "COOH", "C  benzoic acid")
    f.path("M 320 165 Q 200 200 80 165", arrow=True, color="#1f4e8c")
    f.text(200, 205, "B, mild oxidation [O] → A", size=12, color="#1f4e8c")
    # second row
    mol(70, 290, "CHO", "A")
    f.arrow(110, 285, 190, 285); f.text(150, 275, "PCl₅", size=12)
    mol(240, 290, "CHCl₂", "D  benzal chloride")
    mol(400, 290, "COOH", "C")
    f.arrow(440, 285, 520, 285); f.text(480, 275, "PCl₅", size=12)
    mol(575, 290, "COCl", "E  benzoyl chloride")
    return f.svg()
