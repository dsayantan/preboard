"""Figures for Chemistry pre-board 2024-25, Set 1 (prefix s1_) and the Practical (prefix prac_).

Helpers are copied (not imported) from chemistry_2025_26_figs so this module stands alone.
"""
import math
from html import escape
from svg import Fig

INK, ACC, WARM, MUTED, LIG, BLUE, RED = "#111", "#0d6e6e", "#b5651d", "#777", "#1f4fa8", "#1f4e8c", "#c0392b"


# ================================================================== helpers
def chem(f, x, y, parts, size=14, anchor="middle", color=INK, bold=False):
    st = ' font-weight="bold"' if bold else ""
    out = []
    for s, kind in parts:
        s = escape(s)
        if kind == "b":
            out.append(f'<tspan baseline-shift="sub" font-size="{size*0.72:.1f}">{s}</tspan>')
        elif kind == "p":
            out.append(f'<tspan baseline-shift="super" font-size="{size*0.72:.1f}">{s}</tspan>')
        else:
            out.append(f"<tspan>{s}</tspan>")
    f.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
          f'font-family="Times New Roman,serif"{st}>{"".join(out)}</text>')


def F(s):
    """'CH3COOH' -> parts; digits after a letter or ')' ']' are subscripts; '^..' (to a space) superscript."""
    parts, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "^":
            j = i + 1
            while j < len(s) and s[j] != " ":
                j += 1
            parts.append((s[i + 1:j], "p")); i = j; continue
        if c.isdigit() and i > 0 and (s[i - 1].isalpha() or s[i - 1] in ")]"):
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            parts.append((s[i:j], "b")); i = j; continue
        parts.append((c, "")); i += 1
    out = []
    for p in parts:
        if out and out[-1][1] == p[1] == "":
            out[-1] = (out[-1][0] + p[0], "")
        else:
            out.append(p)
    return out


def T(f, x, y, s, size=14, anchor="middle", color=INK, bold=False):
    chem(f, x, y, F(s), size=size, anchor=anchor, color=color, bold=bold)


def ring(f, cx, cy, r=24, circle=True):
    """Benzene ring, a vertex at the top. Vertices: 0 top, 1 upper-right, 2 lower-right,
    3 bottom, 4 lower-left, 5 upper-left."""
    v = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
         for a in (-90, -30, 30, 90, 150, 210)]
    f.path("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in v) + " Z", w=1.6)
    if circle:
        f.circle(cx, cy, r * 0.58, w=1.3)
    return v


def sub(f, cx, cy, v, k, label, L=16, size=14, color=INK, anchor=None):
    x, y = v[k]
    dx, dy = x - cx, y - cy
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    x2, y2 = x + ux * L, y + uy * L
    f.line(x, y, x2, y2, w=1.6)
    if anchor is None:
        anchor = "middle" if abs(ux) < 0.3 else ("start" if ux > 0 else "end")
    tx = x2 + ux * 4
    ty = y2 + uy * 4 + (5 if abs(ux) >= 0.3 else (-4 if uy < 0 else 13))
    T(f, tx, ty, label, size=size, anchor=anchor, color=color)


def mol(f, cx, cy, subs, name=None, r=24, size=14, namecol=MUTED, namedy=None):
    v = ring(f, cx, cy, r)
    for k, lab in subs.items():
        sub(f, cx, cy, v, k, lab, size=size)
    if name:
        f.text(cx, cy + (namedy if namedy else r + 34), name, size=12, color=namecol)
    return v


def spin_box(f, x, y, fill, w=24, h=22):
    f.rect(x, y, w, h, color=MUTED, w=1.1)
    if fill in ("u", "ud"):
        xa = x + (w * 0.33 if fill == "ud" else w * 0.5)
        f.line(xa, y + h - 3, xa, y + 4, w=1.4)
        f.path(f"M {xa} {y+4} l 3.2 4.4", w=1.4)
        if fill == "ud":
            xb = x + w * 0.67
            f.line(xb, y + 4, xb, y + h - 3, w=1.4)
            f.path(f"M {xb} {y+h-3} l -3.2 -4.4", w=1.4)
    elif fill == "L":
        for xc in (x + w * 0.32, x + w * 0.68):
            f.text(xc, y + h * 0.72, "x", size=12, color=LIG, bold=True)


def boxes(f, x, y, fills, w=24, h=22):
    for k, fl in enumerate(fills):
        spin_box(f, x + k * w, y, fl, w, h)
    return x + len(fills) * w


def _expand(code, n):
    """'2211.' style codes: 2 pair, 1 up, L ligand pair, . empty."""
    m = {"2": "ud", "1": "u", "L": "L", ".": ""}
    out = [m[c] for c in code]
    return out + [""] * (n - len(out))


def vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p"), counts=(5, 1, 3), gap=14, w=24):
    xs, x = {}, x0
    for s, n in zip(shells, counts):
        xs[s] = x; x += n * w + gap
    for i, (y, label, fills) in enumerate(rows):
        f.text(10, y + 16, label, size=13, anchor="start")
        for s, n in zip(shells, counts):
            fl = fills.get(s)
            if fl is None:
                continue
            boxes(f, xs[s], y, _expand(fl, n), w)
            if i == 0:
                f.text(xs[s] + n * w / 2, y - 6, s, size=12, color=MUTED)
    return xs


def brace(f, x1, x2, y, text, color=LIG, size=12):
    f.path(f"M {x1} {y} L {x1} {y+8} L {x2} {y+8} L {x2} {y}", color=color, w=1.2)
    f.text((x1 + x2) / 2, y + 24, text, size=size, color=color)


def label_arrow(f, x1, x2, y, top=None, bot=None, size=12):
    f.arrow(x1, y, x2, y)
    if top:
        T(f, (x1 + x2) / 2, y - 8, top, size=size)
    if bot:
        T(f, (x1 + x2) / 2, y + 17, bot, size=size)


# ================================================================== SET 1
def fig_s1_q8_scheme():
    """Q8 -- 2-chloropropane (skeletal, as printed) -> A -> B -> C -> D."""
    f = Fig(640, 150, "fig_s1_q8_scheme")
    cx, cy = 60, 95
    f.line(cx, cy, cx - 34, cy + 20)
    f.line(cx, cy, cx + 34, cy + 20)
    f.line(cx, cy, cx, cy - 46)
    f.text(cx, cy - 52, "Cl", size=15)
    label_arrow(f, 120, 200, 90, "alc", "KOH")
    f.text(215, 95, "A", size=16)
    label_arrow(f, 232, 300, 90, "HBr")
    f.text(315, 95, "B", size=16)
    label_arrow(f, 332, 430, 90, "NaI", "Dry ether")
    f.text(445, 95, "C", size=16)
    label_arrow(f, 462, 560, 90, "Mg", "Dry ether")
    f.text(575, 95, "D", size=16)
    return f.svg()


def fig_s1_q8_answer():
    """Q8 answer -- condensed structures of A to D."""
    f = Fig(700, 120, "fig_s1_q8_answer")
    T(f, 50, 55, "CH3–CHCl–CH3", size=13)
    f.text(50, 78, "2-chloropropane", size=11, color=MUTED)
    label_arrow(f, 105, 150, 50, "alc KOH", None, size=10)
    T(f, 205, 55, "CH3–CH=CH2", size=13)
    f.text(205, 78, "A  propene", size=11, color=MUTED)
    label_arrow(f, 255, 295, 50, "HBr", None, size=10)
    T(f, 350, 55, "CH3–CHBr–CH3", size=13)
    f.text(350, 78, "B  2-bromopropane", size=11, color=MUTED)
    label_arrow(f, 405, 445, 50, "NaI", None, size=10)
    T(f, 495, 55, "CH3–CHI–CH3", size=13)
    f.text(495, 78, "C  2-iodopropane", size=11, color=MUTED)
    label_arrow(f, 545, 580, 50, "Mg", None, size=10)
    T(f, 640, 55, "(CH3)2CH–MgI", size=13)
    f.text(640, 78, "D  isopropylmagnesium", size=11, color=MUTED)
    f.text(640, 93, "iodide", size=11, color=MUTED)
    return f.svg()


def fig_s1_q3_answer():
    """Q3 -- acetophenone (A) + I2/NaOH -> iodoform (B) + benzoate -> benzoic acid (C); CHI3 + Ag -> C2H2 (D)."""
    f = Fig(660, 200, "fig_s1_q3_answer")
    mol(f, 60, 80, {0: "COCH3"}, "A  acetophenone")
    f.arrow(105, 80, 215, 80)
    T(f, 160, 70, "I2 / NaOH", size=12)
    f.text(160, 98, "(iodoform reaction)", size=10, color=MUTED)
    mol(f, 260, 80, {0: "COO^− Na^+"}, "sodium benzoate", namedy=58)
    f.text(345, 85, "+", size=18)
    T(f, 390, 86, "CHI3", size=16)
    f.text(390, 106, "B  iodoform (yellow)", size=11, color=MUTED)
    f.arrow(260, 145, 260, 172)
    T(f, 270, 162, "H3O^+", size=11, anchor="start")
    f.text(260, 192, "C  benzoic acid, C₆H₅COOH (also from KMnO₄ oxidation of A)", size=11, color=MUTED)
    f.arrow(390, 118, 470, 150)
    T(f, 445, 128, "Ag, Δ", size=11, anchor="start")
    T(f, 560, 160, "HC≡CH", size=16)
    f.text(560, 180, "D  ethyne (decolourises Br₂/CCl₄)", size=11, color=MUTED)
    return f.svg()


def fig_s1_q12_scheme():
    """Q12(iii) -- aniline -> A -> B as printed."""
    f = Fig(560, 130, "fig_s1_q12_scheme")
    mol(f, 60, 80, {0: "NH2"})
    label_arrow(f, 110, 270, 78, "conc. H2SO4")
    f.text(290, 84, "A", size=17, italic=True, bold=True)
    label_arrow(f, 310, 490, 78, "heat, 453–473 K")
    f.text(510, 84, "B", size=17, italic=True, bold=True)
    return f.svg()


def fig_s1_q12_answer():
    """Q12(iii) answer -- anilinium hydrogensulphate -> sulphanilic acid (zwitterion)."""
    f = Fig(660, 190, "fig_s1_q12_answer")
    mol(f, 55, 95, {0: "NH2"}, "aniline")
    label_arrow(f, 100, 165, 92, "H2SO4", None, size=11)
    mol(f, 230, 95, {0: "NH3^+ HSO4^−"}, "A  anilinium", namedy=50)
    f.text(230, 162, "hydrogensulphate", size=12, color=MUTED)
    label_arrow(f, 300, 380, 92, "453–473 K", "−H2O", size=11)
    mol(f, 450, 95, {0: "NH2", 3: "SO3H"}, None)
    f.text(450, 178, "B  sulphanilic acid", size=12, color=MUTED)
    f.text(520, 100, "≡", size=18)
    mol(f, 590, 95, {0: "NH3^+", 3: "SO3^−"}, None)
    f.text(590, 178, "zwitterion", size=12, color=MUTED)
    return f.svg()


def fig_s1_q13_graph():
    """Q13 -- melting point against mass of NaCl, both sets; the anomalous Set-2 point ringed."""
    f = Fig(560, 330, "fig_s1_q13_graph")
    x0, y0, W, H = 70, 40, 440, 240          # plot box: x 0..1.2 g, y 0..-7 C
    X = lambda m: x0 + m / 1.2 * W
    Y = lambda t: y0 + (-t) / 7 * H
    for k in range(0, 7):
        m = k * 0.2
        f.line(X(m), y0, X(m), y0 + H, color="#ddd", w=0.8)
        f.text(X(m), y0 + H + 18, f"{m:.1f}", size=11)
    for t in range(0, 8):
        f.line(x0, Y(-t), x0 + W, Y(-t), color="#ddd", w=0.8)
        f.text(x0 - 8, Y(-t) + 4, f"{-t}" if t else "0", size=11, anchor="end")
    f.line(x0, y0, x0, y0 + H, w=1.4)
    f.line(x0, y0, x0 + W, y0, w=1.4)
    f.text(x0 + W / 2, y0 + H + 40, "mass of NaCl in 10 mL water / g", size=12)
    f.raw(f'<text x="22" y="{y0+H/2}" font-size="12" text-anchor="middle" fill="{INK}" '
          f'font-family="Times New Roman,serif" transform="rotate(-90 22 {y0+H/2})">melting point / °C</text>')
    s1 = [(0.3, -1.9), (0.4, -2.5), (0.5, -3.0), (0.6, -3.8), (0.8, -5.1), (1.0, -6.4)]
    s2 = [(0.3, -1.9), (0.4, -2.6), (0.5, -5.5), (0.6, -3.8), (0.8, -5.0), (1.0, -6.3)]
    # best-fit line through the origin from the 11 good points: slope b = sum(m t)/sum(m^2)
    pts = s1 + [p for p in s2 if p != (0.5, -5.5)]
    b = sum(m * t for m, t in pts) / sum(m * m for m, t in pts)
    f.line(X(0), Y(0), X(1.1), Y(b * 1.1), color=ACC, w=1.4, dash="6 4")
    f.text(X(0.17), Y(-0.55), "best-fit line (11 points)", size=11, color=ACC, anchor="start")
    for m, t in s1:
        f.circle(X(m), Y(t), 4, color=BLUE, fill=BLUE)
    for m, t in s2:
        f.rect(X(m) - 4, Y(t) - 4, 8, 8, color=WARM, fill="none", w=1.6)
    f.circle(X(0.5), Y(-5.5), 12, color=RED, w=1.8)
    f.text(X(0.5) + 16, Y(-5.5) + 4, "−5.5 °C: anomalous", size=12, color=RED, anchor="start")
    f.circle(x0 + 20, y0 + H - 40, 4, color=BLUE, fill=BLUE)
    f.text(x0 + 30, y0 + H - 36, "Set 1", size=11, anchor="start")
    f.rect(x0 + 16, y0 + H - 24, 8, 8, color=WARM, w=1.6)
    f.text(x0 + 30, y0 + H - 16, "Set 2", size=11, anchor="start")
    return f.svg()


def fig_s1_q15_vbt():
    """Q15 -- VBT for Cr(III) in [Cr(NH3)4Cl2]+ / [Cr(NH3)4ClBr]+: d2sp3, 3 unpaired."""
    f = Fig(620, 210, "fig_s1_q15_vbt")
    rows = [(30, "Cr (ground) 3d⁵4s¹", {"3d": "11111", "4s": "1", "4p": "..."}),
            (85, "Cr³⁺  3d³", {"3d": "111..", "4s": ".", "4p": "..."}),
            (140, "Cr³⁺ in the complex", {"3d": "111LL", "4s": "L", "4p": "LLL"})]
    xs = vbt_rows(f, rows, x0=200)
    brace(f, xs["3d"] + 72, xs["4p"] + 72, 166, "d²sp³ — six pairs from 4 NH₃ + 2 halide: octahedral, inner orbital")
    f.text(xs["3d"] + 36, 132, "3 unpaired", size=11, color=RED)
    return f.svg()


def fig_s1_q15_isomers():
    """Q15 -- octahedral cations of A and B (trans arrangement drawn; both are octahedral)."""
    f = Fig(560, 210, "fig_s1_q15_isomers")
    def octa(cx, cy, top, bot, lab):
        L = 52
        pos = {"t": (cx, cy - L), "b": (cx, cy + L), "l": (cx - 60, cy + 6), "r": (cx + 60, cy - 6),
               "fl": (cx - 36, cy + 32), "br": (cx + 36, cy - 32)}
        for k, (x, y) in pos.items():
            d = math.hypot(x - cx, y - cy)
            sx, sy = cx + (x - cx) * 13 / d, cy + (y - cy) * 13 / d
            f.line(sx, sy, x, y, w=1.5, dash=("4 3" if k == "br" else None))
        T(f, cx, cy + 5, "Cr", size=14, bold=True)
        T(f, cx, cy - L - 6, top, size=13)
        T(f, cx, cy + L + 16, bot, size=13)
        for k, dx, dy, an in (("l", -5, 5, "end"), ("r", 5, 5, "start"), ("fl", -5, 12, "end"), ("br", 5, -3, "start")):
            x, y = pos[k]
            T(f, x + dx, y + dy, "NH3", size=12, anchor=an)
        f.text(cx, cy + L + 40, lab, size=12, color=MUTED)
    octa(140, 95, "Br", "Cl", "A: [Cr(NH₃)₄BrCl]⁺ Cl⁻")
    octa(420, 95, "Cl", "Cl", "B: [Cr(NH₃)₄Cl₂]⁺ Br⁻")
    return f.svg()


def fig_s1_q19_azo():
    """Q19(i)a -- coupling of benzenediazonium chloride with phenol (alkaline, 0 C) -> p-hydroxyazobenzene."""
    f = Fig(680, 170, "fig_s1_q19_azo")
    v = ring(f, 50, 80)
    sub(f, 50, 80, v, 1, "N2^+ Cl^−", size=12)
    f.text(150, 85, "+", size=18)
    v = ring(f, 205, 80)
    sub(f, 205, 80, v, 1, "OH", size=13)
    f.arrow(265, 80, 355, 80)
    T(f, 310, 70, "OH^− , 0 °C", size=11)
    f.text(310, 100, "pH 9–10", size=10, color=MUTED)
    # product: ring1 - N=N - ring2 - OH, rings with vertices pointing along the axis
    def hexa(cx, cy, r=22):
        pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
               for a in (0, 60, 120, 180, 240, 300)]
        f.path("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z", w=1.6)
        f.circle(cx, cy, r * 0.58, w=1.3)
        return pts
    a = hexa(395, 80)
    f.line(a[0][0], 80, a[0][0] + 16, 80)
    T(f, a[0][0] + 20, 85, "N", size=13, anchor="start")
    f.line(a[0][0] + 32, 77, a[0][0] + 50, 77); f.line(a[0][0] + 32, 83, a[0][0] + 50, 83)
    T(f, a[0][0] + 52, 85, "N", size=13, anchor="start")
    b = hexa(a[0][0] + 100, 80)
    f.line(a[0][0] + 64, 80, b[3][0], 80)
    f.line(b[0][0], 80, b[0][0] + 14, 80)
    T(f, b[0][0] + 16, 85, "OH", size=13, anchor="start")
    f.text(500, 140, "p-hydroxyazobenzene (orange dye) + NaCl + H₂O", size=12, color=MUTED)
    return f.svg()


def _vp_axes(f, x0, y0, W, H):
    f.line(x0, y0, x0, y0 + H, w=1.8)
    f.line(x0 + W, y0, x0 + W, y0 + H, w=1.8)
    f.line(x0, y0 + H, x0 + W, y0 + H, w=1.8)


def fig_s1_q21_vp_printed():
    """Q21 I(i) -- the printed vapour-pressure diagram for an ideal solution (as printed, unscaled)."""
    f = Fig(600, 300, "fig_s1_q21_vp_printed")
    x0, y0, W, H = 110, 30, 400, 190
    _vp_axes(f, x0, y0, W, H)
    yA, yB, yb = y0 + 55, y0 + 18, y0 + H
    f.line(x0, yA, x0 + W, yB, w=1.6)
    f.line(x0, yA, x0 + W, yb, w=1.2, dash="3 3")
    f.line(x0, yb, x0 + W, yB, w=1.2, dash="3 3")
    chem(f, x0 - 10, yA + 4, [("P", ""), ("o", "p"), ("A", "b")], size=14, anchor="end")
    chem(f, x0 + W + 10, yB + 4, [("P", ""), ("o", "p"), ("B", "b")], size=14, anchor="start")
    chem(f, x0 + 200, y0 + 22, [("P", ""), ("T", "b"), (" = P", ""), ("A", "b"), (" + P", ""), ("B", "b")], size=14)
    chem(f, x0 + 250, y0 + 115, [("P", ""), ("B", "b"), (" = P", ""), ("o", "p"), ("B", "b"), ("·X", ""), ("B", "b")], size=13)
    chem(f, x0 + 290, y0 + 178, [("P", ""), ("A", "b"), (" = P", ""), ("o", "p"), ("A", "b"), ("·X", ""), ("A", "b")], size=13)
    f.arrow(60, y0 + H - 10, 60, y0 + 10)
    f.raw(f'<text x="45" y="{y0+H/2+20}" font-size="13" text-anchor="middle" fill="{INK}" '
          f'font-family="Arial,sans-serif" transform="rotate(-90 45 {y0+H/2+20})">Vapour Pressure</text>')
    T(f, x0, yb + 20, "XA = 1", size=12); T(f, x0, yb + 36, "XB = 0", size=12)
    T(f, x0 + W, yb + 20, "XA = 0", size=12); T(f, x0 + W, yb + 36, "XB = 1", size=12)
    f.arrow(x0 + 130, yb + 26, x0 + 270, yb + 26, w=1.2)
    f.text(x0 + 200, yb + 18, "Mole Fraction", size=12)
    f.text(x0 + W / 2, yb + 68, "Vapour Pressure Diagram for Ideal Solution", size=13)
    return f.svg()


def fig_s1_q21_vp_answer():
    """Q21 I(i) answer -- to scale: P°A 450, P°B 700 mm Hg; P = 600 at xB = 0.6 (xA = 0.4)."""
    f = Fig(600, 320, "fig_s1_q21_vp_answer")
    x0, y0, W, H = 90, 20, 420, 240           # y: 0..800 mm Hg
    X = lambda xB: x0 + xB * W
    Y = lambda p: y0 + H - p / 800 * H
    for p in range(0, 801, 100):
        f.line(x0, Y(p), x0 + W, Y(p), color="#e3e3e3", w=0.8)
        f.text(x0 - 8, Y(p) + 4, str(p), size=11, anchor="end")
    for k in range(0, 11, 2):
        f.text(X(k / 10), Y(0) + 18, f"{k/10:.1f}", size=11)
    _vp_axes(f, x0, y0, W, H)
    f.line(X(0), Y(450), X(1), Y(700), w=1.8)
    f.line(X(0), Y(450), X(1), Y(0), w=1.2, dash="4 3", color=BLUE)
    f.line(X(0), Y(0), X(1), Y(700), w=1.2, dash="4 3", color=WARM)
    f.line(x0, Y(600), X(0.6), Y(600), color=RED, w=1.3, dash="6 3")
    f.line(X(0.6), Y(600), X(0.6), Y(0), color=RED, w=1.3, dash="6 3")
    f.circle(X(0.6), Y(600), 4, color=RED, fill=RED)
    f.text(X(0.6) + 6, Y(600) - 10, "P = 600", size=12, color=RED, anchor="start")
    f.text(X(0.6) + 5, Y(0) - 6, "xB = 0.6 (xA = 0.4)", size=11, color=RED, anchor="start")
    f.text(x0 + 6, Y(450) - 8, "P°A = 450", size=12, anchor="start")
    f.text(x0 + W - 6, Y(700) - 10, "P°B = 700", size=12, anchor="end")
    f.text(X(0.2), Y(330) + 4, "pA", size=12, color=BLUE, italic=True)
    f.text(X(0.85), Y(560) + 22, "pB", size=12, color=WARM, italic=True)
    f.text(x0 + W / 2, Y(0) + 38, "mole fraction of B in the liquid, xB", size=12)
    f.raw(f'<text x="30" y="{y0+H/2}" font-size="12" text-anchor="middle" fill="{INK}" '
          f'font-family="Times New Roman,serif" transform="rotate(-90 30 {y0+H/2})">vapour pressure / mm Hg</text>')
    return f.svg()


def fig_s1_q21_osmotic():
    """Q21 I(ii) -- printed straight-line plot of pi against the x-variable (labelled C on the paper)."""
    f = Fig(320, 250, "fig_s1_q21_osmotic")
    x0, y0 = 60, 200
    f.arrow(x0, y0, x0, 20, w=1.8)
    f.arrow(x0, y0, 290, y0, w=1.8)
    f.line(x0, y0, 240, 40, w=1.8)
    f.arrow(30, 120, 30, 80, w=1.3)
    f.text(30, 140, "π", size=18, italic=True)
    f.text(90, 230, "C", size=18, bold=True)
    f.arrow(105, 225, 150, 225, w=1.3)
    return f.svg()
