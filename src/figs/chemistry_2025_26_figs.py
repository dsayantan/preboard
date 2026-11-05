"""Figures for Chemistry pre-board 2025-26, Set 1 and Set 2.

Helpers are copied (not imported) from chemistry_1517_lib so this module stands alone.
"""
import math
from html import escape
from svg import Fig

INK, ACC, WARM, MUTED, LIG, BLUE = "#111", "#0d6e6e", "#b5651d", "#777", "#c0392b", "#1f4e8c"


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
    """Benzene ring, a vertex at the top.  Returns vertex list: 0 top, 1 upper-right,
    2 lower-right, 3 bottom, 4 lower-left, 5 upper-left."""
    v = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
         for a in (-90, -30, 30, 90, 150, 210)]
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in v) + " Z"
    f.path(d, w=1.6)
    if circle:
        f.circle(cx, cy, r * 0.58, w=1.3)
    return v


def sub(f, cx, cy, v, k, label, L=16, size=14, color=INK, anchor=None):
    """Substituent bond from vertex k outward, with a formula label."""
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


def vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p", "4d"), counts=(5, 1, 3, 5), gap=14, w=24):
    """rows: list of (y, label, {shell: fills}) ; draws column headings above the first row."""
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
            if i == 0 or fills.get("_head"):
                f.text(xs[s] + n * w / 2, y - 6, s, size=12, color=MUTED)
    return xs


def _expand(code, n):
    """'2211.' style codes: 2 pair, 1 up, L ligand pair, . empty."""
    m = {"2": "ud", "1": "u", "L": "L", ".": ""}
    out = [m[c] for c in code]
    return out + [""] * (n - len(out))


def CF(t, e):
    """chem() parts for t2g^t eg^e."""
    return [("t", ""), ("2g", "b"), (t, "p"), (" e", ""), ("g", "b"), (e, "p")]


def brace(f, x1, x2, y, text, color=LIG, size=12):
    f.path(f"M {x1} {y} L {x1} {y+8} L {x2} {y+8} L {x2} {y}", color=color, w=1.2)
    f.text((x1 + x2) / 2, y + 24, text, size=size, color=color)


def level(f, x, y, n, fills, w=30, gap=8):
    for k in range(n):
        x0 = x + k * (w + gap)
        f.line(x0, y, x0 + w, y, w=2)
        fl = fills[k] if k < len(fills) else ""
        if fl in ("u", "ud"):
            xa = x0 + (w * 0.35 if fl == "ud" else w * 0.5)
            f.line(xa, y - 3, xa, y - 18, w=1.4)
            f.path(f"M {xa} {y-18} l 3.2 4.4", w=1.4)
            if fl == "ud":
                xb = x0 + w * 0.65
                f.line(xb, y - 18, xb, y - 3, w=1.4)
                f.path(f"M {xb} {y-3} l -3.2 -4.4", w=1.4)
    return x + n * (w + gap) - gap


def beaker(f, x, y, w, h, liquid_y, fill="#dceefb"):
    f.rect(x, liquid_y, w, y + h - liquid_y, color="none", w=0, fill=fill)
    f.path(f"M {x} {y} L {x} {y+h} L {x+w} {y+h} L {x+w} {y}", w=1.8)


def voltmeter(f, cx, cy, label="V"):
    f.circle(cx, cy, 14, fill="#fff")
    f.text(cx, cy + 5, label, size=14, bold=True)


# ================================================================== SET 1
def fig_s1_amine_bars():
    """Q1(B)(v) -- the four bar charts P, Q, R, S as printed (relative heights only)."""
    f = Fig(640, 210, "fig_s1_amine_bars")
    data = {"P": (8.5, 5, 7), "Q": (8.5, 5, 5), "R": (5, 7, 8.5), "S": (5, 8.5, 7)}
    opts = {"P": "a.", "Q": "b.", "R": "c.", "S": "d."}
    for i, (name, hs) in enumerate(data.items()):
        x0, yb, unit = 40 + i * 155, 160, 14
        for g in range(1, 10):
            f.line(x0, yb - g * unit, x0 + 112, yb - g * unit, color="#ccc", w=0.8)
        f.arrow(x0, yb, x0, yb - 140, w=1.3)
        f.line(x0, yb, x0 + 112, yb, w=1.3)
        f.raw(f'<text x="{x0-10}" y="{yb-60}" font-size="11" text-anchor="middle" fill="{INK}" '
              f'font-family="Arial,sans-serif" transform="rotate(-90 {x0-10} {yb-60})">Solubility</text>')
        for j, (h, lab) in enumerate(zip(hs, ("Amine I", "Amine J", "Amine K"))):
            bx = x0 + 10 + j * 35
            f.rect(bx, yb - h * unit, 20, h * unit, color=INK, w=1, fill="#222")
            f.text(bx + 10, yb + 13, lab, size=9.5)
        f.text(x0 + 56, yb + 30, name, size=14, bold=True)
        f.text(x0 - 10, yb + 46, opts[name], size=13, anchor="start")
    return f.svg()


def fig_s1_cu_conc_cell():
    """Q1(C) -- Cu | CuSO4(0.15) || CuSO4(1.0) | Cu with a voltmeter."""
    f = Fig(560, 230, "fig_s1_cu_conc_cell")
    beaker(f, 170, 90, 90, 90, 115)
    beaker(f, 330, 90, 90, 90, 115)
    for ex in (205, 385):
        f.rect(ex - 5, 70, 10, 85, color=INK, w=1.2, fill="#b87333")
    # salt bridge
    f.path("M 235 165 L 235 60 L 355 60 L 355 165", w=9, color="#999")
    f.path("M 235 165 L 235 60 L 355 60 L 355 165", w=6, color="#fff")
    # wires and voltmeter
    f.path("M 205 70 L 205 25 L 281 25", w=1.5)
    f.path("M 309 25 L 385 25 L 385 70", w=1.5)
    voltmeter(f, 295, 25)
    f.line(150, 95, 200, 95, w=1)
    f.text(145, 99, "Copper", size=13, anchor="end")
    f.line(390, 95, 440, 95, w=1)
    f.text(445, 99, "Copper", size=13, anchor="start")
    chem(f, 160, 150, [("0.15 mol dm", ""), ("−3", "p")], size=12, anchor="end")
    chem(f, 160, 166, F("CuSO4(aq)"), size=12, anchor="end")
    chem(f, 430, 150, [("1.0 mol dm", ""), ("−3", "p")], size=12, anchor="start")
    chem(f, 430, 166, F("CuSO4(aq)"), size=12, anchor="start")
    f.text(295, 54, "salt bridge", size=11, color=MUTED)
    f.text(215, 205, "left half-cell (dilute)", size=11, color=MUTED)
    f.text(375, 205, "right half-cell (1.0 M)", size=11, color=MUTED)
    return f.svg()


def fig_s1_q12_scheme():
    """Q12 OR -- reaction scheme as printed."""
    f = Fig(660, 250, "fig_s1_q12_scheme")
    f.text(30, 75, "[A]", size=16, bold=True)
    f.arrow(55, 70, 245, 70)
    chem(f, 150, 60, F("Conc. HNO3 /Conc. H2SO4"), size=12)
    f.text(150, 88, "Δ", size=13)
    mol(f, 290, 75, {0: "NO2"})
    f.arrow(325, 70, 405, 70)
    f.text(365, 60, "[B]", size=13, bold=True)
    mol(f, 450, 75, {0: "NH2"})
    f.arrow(485, 70, 575, 70)
    chem(f, 530, 60, F("Ac2O"), size=12)
    f.text(600, 75, "[C]", size=16, bold=True)
    f.arrow(600, 85, 600, 175)
    chem(f, 608, 135, F("HNO3"), size=12, anchor="start")
    f.text(600, 200, "[D]", size=16, bold=True)
    f.arrow(578, 195, 465, 195)
    chem(f, 521, 184, F("NaNO2/ HCl"), size=12)
    f.text(521, 213, "0–5 °C", size=12)
    f.text(445, 200, "[E]", size=16, bold=True)
    f.arrow(425, 195, 300, 195)
    chem(f, 362, 184, F("HBF4"), size=12)
    chem(f, 362, 213, F("NaNO2, Cu"), size=12)
    f.text(280, 200, "[F]", size=16, bold=True)
    return f.svg()


def fig_s1_q12_answer():
    """Q12 OR -- structures A to F."""
    f = Fig(720, 340, "fig_s1_q12_answer")
    mol(f, 60, 80, {}, "A  benzene")
    f.arrow(95, 75, 160, 75); f.text(128, 63, "nitration", size=11, color=MUTED)
    mol(f, 200, 80, {0: "NO2"}, "nitrobenzene")
    f.arrow(235, 75, 330, 75)
    T(f, 282, 63, "B: Sn/HCl", size=12, color=BLUE)
    f.text(282, 92, "(or Fe/HCl)", size=11, color=MUTED)
    mol(f, 370, 80, {0: "NH2"}, "aniline")
    f.arrow(405, 75, 480, 75); T(f, 442, 63, "Ac2O", size=12)
    mol(f, 540, 80, {0: "NHCOCH3"}, "C  acetanilide")
    f.path("M 575 80 L 625 80 L 625 235 L 578 235", arrow=True)
    T(f, 632, 150, "HNO3/", size=11, anchor="start")
    T(f, 632, 166, "H2SO4", size=11, anchor="start")
    y = 235
    mol(f, 540, y, {0: "NHCOCH3", 3: "NO2"}, "4-nitroacetanilide", namedy=78)
    f.arrow(500, y, 425, y)
    T(f, 462, y - 10, "H3O^+", size=11); f.text(462, y + 15, "hydrolysis", size=10, color=MUTED)
    mol(f, 380, y, {0: "NH2", 3: "NO2"}, "D  4-nitroaniline", namedy=78)
    f.arrow(345, y, 270, y)
    T(f, 307, y - 10, "NaNO2/HCl", size=11); f.text(307, y + 15, "0–5 °C", size=10)
    mol(f, 225, y, {0: "N2^+ Cl^−", 3: "NO2"}, "E  4-nitrobenzene-", namedy=78)
    f.text(225, y + 94, "diazonium chloride", size=12, color=MUTED)
    f.arrow(190, y, 115, y)
    T(f, 152, y - 10, "HBF4;", size=11); T(f, 152, y + 15, "NaNO2, Cu", size=11)
    mol(f, 70, y, {0: "NO2", 3: "NO2"}, "F  1,4-dinitrobenzene", namedy=78)
    return f.svg()


def fig_s1_q14_scheme():
    """Q14(i) -- scheme as printed."""
    f = Fig(560, 180, "fig_s1_q14_scheme")
    f.text(30, 85, "A", size=16, italic=True)
    f.arrow(45, 80, 165, 80)
    chem(f, 105, 70, F("NaNO2/HCl"), size=12)
    f.text(105, 98, "0°C–5°C", size=12)
    f.text(180, 85, "B", size=16, italic=True)
    f.arrow(195, 80, 285, 80)
    T(f, 240, 70, "CuCl/HCl", size=12)
    f.text(240, 98, "Δ", size=13)
    f.text(300, 85, "C", size=16, italic=True)
    f.arrow(315, 80, 420, 80)
    T(f, 368, 70, "Na/CH3Cl", size=12)
    mol(f, 460, 90, {0: "CH3"})
    f.path("M 300 95 L 300 150 L 420 150", arrow=True)
    f.text(360, 140, "Na/Ether", size=12)
    f.text(435, 155, "D", size=16, italic=True)
    return f.svg()


def _biphenyl(f, cx, cy, r=22):
    """Two rings joined by a C-C bond, rings with a vertex pointing at each other."""
    def hexa(x0):
        v = [(x0 + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
             for a in (0, 60, 120, 180, 240, 300)]
        f.path("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in v) + " Z", w=1.6)
        f.circle(x0, cy, r * 0.58, w=1.3)
        return v
    a = hexa(cx - r - 14)
    b = hexa(cx + r + 14)
    f.line(a[0][0], a[0][1], b[3][0], b[3][1], w=1.6)


def fig_s1_q14_answer():
    """Q14(i) -- A aniline, B benzenediazonium chloride, C chlorobenzene, D biphenyl."""
    f = Fig(680, 175, "fig_s1_q14_answer")
    mol(f, 50, 85, {0: "NH2"}, "A  aniline")
    f.arrow(82, 80, 128, 80)
    mol(f, 170, 85, {0: "N2^+ Cl^−"}, "B  benzenediazonium")
    f.text(170, 159, "chloride", size=12, color=MUTED)
    f.arrow(205, 80, 252, 80)
    mol(f, 290, 85, {0: "Cl"}, "C  chlorobenzene")
    f.arrow(322, 80, 372, 80)
    T(f, 347, 70, "Na/CH3Cl", size=10)
    mol(f, 410, 85, {0: "CH3"}, "toluene")
    f.line(460, 30, 460, 150, color="#ccc", dash="4 4")
    _biphenyl(f, 575, 85)
    f.text(575, 140, "D  biphenyl", size=12, color=MUTED)
    f.text(575, 156, "(C + Na/ether, Fittig)", size=11, color=MUTED)
    return f.svg()


def fig_s1_gly_ala():
    """Q15(i) -- glycine and alanine, skeletal as printed (alanine NH2 on a wedge)."""
    f = Fig(520, 190, "fig_s1_gly_ala")
    # glycine: N(60,70) - Ca(100,95) - C(140,70) ; C=O up ; C-OH down-right ; Ca-H down
    T(f, 48, 75, "H2N", size=16)
    f.line(70, 72, 100, 92); f.line(100, 92, 140, 68)
    f.line(140, 68, 140, 35); f.line(146, 68, 146, 35)
    f.text(143, 28, "O", size=16)
    f.line(140, 68, 172, 88)
    f.text(186, 95, "OH", size=16)
    f.line(100, 92, 100, 128)
    f.text(100, 145, "H", size=16)
    f.text(110, 180, "glycine", size=12, color=MUTED)
    # alanine: H3C(300,70)-Ca(340,95)-C(380,70)
    T(f, 290, 75, "H3C", size=16)
    f.line(312, 72, 340, 92); f.line(340, 92, 380, 68)
    f.line(380, 68, 380, 35); f.line(386, 68, 386, 35)
    f.text(383, 28, "O", size=16)
    f.line(380, 68, 412, 88)
    f.text(426, 95, "OH", size=16)
    f.path("M 340 92 L 335 128 L 345 128 Z", fill=INK, w=1)
    T(f, 341, 146, "NH2", size=16)
    f.text(350, 180, "alanine", size=12, color=MUTED)
    return f.svg()


def fig_s1_glyala():
    """Q15(i) answer -- glycylalanine with the peptide bond boxed."""
    f = Fig(640, 230, "fig_s1_glyala")
    # condensation equation (top) as text
    T(f, 320, 22, "H2N–CH2–COOH  +  H2N–CH(CH3)–COOH  →  H2N–CH2–CO–NH–CH(CH3)–COOH  +  H2O", size=13)
    f.text(320, 40, "(–COOH of glycine + –NH₂ of alanine, loss of H₂O)", size=11, color=MUTED)
    y = 130
    T(f, 40, y + 5, "H2N", size=16)
    f.line(60, y, 90, y)
    f.text(105, y + 5, "C", size=16)
    f.line(105, y - 12, 105, y - 32); f.text(105, y - 36, "H", size=14)
    f.line(105, y + 12, 105, y + 32); f.text(105, y + 46, "H", size=14)
    f.line(118, y, 150, y)
    f.text(165, y + 5, "C", size=16)
    f.line(161, y - 12, 161, y - 34); f.line(169, y - 12, 169, y - 34); f.text(165, y - 38, "O", size=16)
    f.line(178, y, 210, y)
    f.text(225, y + 5, "N", size=16)
    f.line(225, y + 12, 225, y + 32); f.text(225, y + 46, "H", size=14)
    f.line(240, y, 272, y)
    f.text(287, y + 5, "C", size=16)
    f.line(287, y - 12, 287, y - 32); f.text(287, y - 36, "H", size=14)
    f.line(287, y + 12, 287, y + 32); T(f, 287, y + 48, "CH3", size=14)
    f.line(300, y, 332, y)
    f.text(347, y + 5, "C", size=16)
    f.line(343, y - 12, 343, y - 34); f.line(351, y - 12, 351, y - 34); f.text(347, y - 38, "O", size=16)
    f.line(360, y, 392, y)
    f.text(412, y + 5, "OH", size=16)
    # peptide bond box
    f.rect(150, y - 58, 92, 112, color=LIG, w=1.6, rx=6, fill="none")
    f.text(196, y + 72, "peptide bond –CO–NH–", size=13, color=LIG, bold=True)
    f.text(105, y + 92, "glycine residue (N-terminal)", size=11, color=MUTED)
    f.text(320, y + 92, "alanine residue (C-terminal)", size=11, color=MUTED)
    f.text(530, y + 5, "Gly-Ala", size=15, bold=True, color=ACC)
    return f.svg()


def fig_s1_cu_ag_cell():
    """Q16(i)(b) -- the copper-silver cell as printed."""
    f = Fig(640, 300, "fig_s1_cu_ag_cell")
    beaker(f, 200, 120, 120, 130, 150, fill="#cfe8f7")
    beaker(f, 360, 120, 120, 130, 150, fill="#e3f1fa")
    f.rect(225, 95, 14, 120, color=INK, w=1.2, fill="#d98b6a")
    f.rect(440, 95, 14, 120, color=INK, w=1.2, fill="#ccc")
    # salt bridge
    f.path("M 280 210 L 280 85 L 400 85 L 400 210", w=12, color="#aaa")
    f.path("M 280 210 L 280 85 L 400 85 L 400 210", w=8, color="#f4f4f4")
    # wires + voltmeter
    f.path("M 232 95 L 232 45 L 312 45", w=1.6)
    f.path("M 368 45 L 447 45 L 447 95", w=1.6)
    f.rect(312, 32, 56, 26, color=INK, w=1.3, fill="#fff")
    f.text(340, 51, "0.422 V", size=13, bold=True)
    f.text(340, 70, "VOLTMETER", size=8, color=MUTED)
    f.arrow(250, 18, 430, 18, w=1.3)
    f.text(340, 13, "Flow of electrons", size=11)
    f.text(222, 92, "Cu anode  −", size=11, anchor="end")
    f.text(458, 92, "+  Ag cathode", size=11, anchor="start")
    f.text(340, 105, "Salt bridge (NaNO₃)", size=11)
    f.arrow(318, 125, 290, 125, w=1.1); f.text(312, 140, "anions", size=10)
    f.arrow(362, 125, 390, 125, w=1.1); f.text(370, 140, "cations", size=10)
    chem(f, 300, 180, [("NO", ""), ("3", "b"), ("−", "p")], size=11)
    chem(f, 380, 180, [("Na", ""), ("+", "p")], size=11)
    chem(f, 250, 235, [("Cu", ""), ("2+", "p")], size=11)
    chem(f, 425, 235, [("Ag", ""), ("+", "p")], size=11)
    chem(f, 260, 270, F("CuCl2 (0.10 M)"), size=13)
    chem(f, 420, 270, F("AgNO3"), size=13)
    chem(f, 190, 175, [("E", ""), ("o", "p"), (" (Cu", ""), ("2+", "p"), ("/Cu) = 0.34 V", "")], size=12, anchor="end")
    chem(f, 490, 175, [("E", ""), ("o", "p"), (" (Ag", ""), ("+", "p"), ("/Ag) = 0.80 V", "")], size=12, anchor="start")
    return f.svg()


def fig_s1_acylation():
    """Q19(ii) -- aniline + CH3COCl --pyridine--> acetanilide + HCl, as printed."""
    f = Fig(560, 165, "fig_s1_acylation")
    mol(f, 50, 90, {0: "NH2"})
    f.text(95, 95, "+", size=18)
    T(f, 160, 95, "CH3–CO–Cl", size=14)
    f.arrow(210, 90, 290, 90)
    f.text(250, 80, "pyridine", size=12)
    f.text(250, 106, "Δ", size=13)
    ring(f, 360, 110, 24)
    f.line(360, 86, 360, 74)
    f.text(360, 68, "N", size=15)
    f.circle(356, 50, 1.5, fill=INK); f.circle(364, 50, 1.5, fill=INK)
    f.line(352, 63, 336, 63); f.text(328, 68, "H", size=15)
    f.line(368, 63, 388, 63); f.text(396, 68, "C", size=15)
    f.line(393, 54, 393, 36); f.line(399, 54, 399, 36); f.text(396, 30, "O", size=15)
    f.line(404, 63, 420, 63); T(f, 422, 68, "CH3", size=15, anchor="start")
    f.text(360, 152, "Acetanilide", size=12)
    f.text(460, 95, "+ HCl", size=15, anchor="start")
    return f.svg()


def fig_s1_amine_flow():
    """Q19(iii) -- flow chart M, N, O as printed."""
    f = Fig(520, 470, "fig_s1_amine_flow")
    def box(cx, cy, s, w):
        f.rect(cx - w / 2, cy - 13, w, 26, w=1.3, fill="#fff")
        T(f, cx, cy + 5, s, size=13)
    def diamond(cx, cy, l1, l2):
        f.path(f"M {cx-90} {cy} L {cx} {cy-32} L {cx+90} {cy} L {cx} {cy+32} Z", w=1.3, fill="#fff")
        f.text(cx, cy - 3, l1, size=12); f.text(cx, cy + 13, l2, size=12)
    cx = 180
    box(cx, 20, "Three test tubes M, N and O are taken", 280)
    f.arrow(cx, 33, cx, 55)
    box(cx, 68, "Addition of CH3COCl", 170)
    f.arrow(cx, 81, cx, 103)
    diamond(cx, 136, "Is a product", "formed?")
    f.arrow(cx + 90, 136, cx + 190, 136); f.text(cx + 120, 128, "No", size=12)
    box(cx + 240, 136, "Test tube N", 100)
    f.arrow(cx, 168, cx, 198); f.text(cx + 8, 186, "Yes", size=12, anchor="start")
    box(cx, 211, "Test tubes M and O", 160)
    f.arrow(cx, 224, cx, 246)
    box(cx, 259, "Addition of CHCl3 and KOH", 210)
    f.arrow(cx, 272, cx, 294)
    diamond(cx, 327, "Is a foul-smelling", "product formed?")
    f.arrow(cx + 90, 327, cx + 190, 327); f.text(cx + 120, 319, "No", size=12)
    box(cx + 240, 327, "Test tube M", 100)
    f.arrow(cx, 359, cx, 389); f.text(cx + 8, 377, "Yes", size=12, anchor="start")
    box(cx, 402, "Test tube O", 100)
    f.text(10, 455, "(The printed chart reads “Is a product ormed?” — evidently “formed”.)", size=11,
           anchor="start", color=MUTED)
    return f.svg()


def fig_s1_nico4_vbt():
    """Q4 -- VBT for [Ni(CO)4]: Ni(0) 3d8 4s2 -> 3d10, sp3."""
    f = Fig(600, 200, "fig_s1_nico4_vbt")
    rows = [(30, "Ni (ground) 3d⁸4s²", {"3d": "22211", "4s": "2", "4p": "..."}),
            (85, "Ni in [Ni(CO)₄]", {"3d": "22222", "4s": ".", "4p": "..."}),
            (140, "[Ni(CO)₄]", {"3d": "22222", "4s": "L", "4p": "LLL"})]
    xs = vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p"), counts=(5, 1, 3))
    f.text(470, 100, "4s² paired into 3d", size=11, color=MUTED, anchor="start")
    f.text(470, 114, "(CO strong field)", size=11, color=MUTED, anchor="start")
    brace(f, xs["4s"], xs["4p"] + 72, 166, "sp³ — 4 pairs from 4 CO: tetrahedral, diamagnetic")
    return f.svg()


def fig_s1_salicylate():
    """Q18(i) -- intramolecular H-bond stabilising the o-hydroxybenzoate ion."""
    f = Fig(420, 190, "fig_s1_salicylate")
    v = ring(f, 120, 110, 30)
    # COO- at top vertex, OH at upper-right
    x0, y0 = v[0]
    f.line(x0, y0, x0, y0 - 22)
    f.text(x0, y0 - 27, "C", size=15)
    f.line(x0 - 6, y0 - 36, x0 - 26, y0 - 50); f.line(x0 - 10, y0 - 32, x0 - 30, y0 - 46)
    f.text(x0 - 36, y0 - 52, "O", size=15)
    f.line(x0 + 7, y0 - 36, x0 + 27, y0 - 50)
    chem(f, x0 + 36, y0 - 52, [("O", ""), ("−", "p")], size=15)
    x1, y1 = v[1]
    f.line(x1, y1, x1 + 22, y1 - 12)
    f.text(x1 + 30, y1 - 10, "O", size=15)
    f.line(x1 + 33, y1 - 22, x1 + 33, y1 - 38)
    f.text(x1 + 34, y1 - 42, "H", size=15)
    f.line(x1 + 28, y1 - 50, x0 + 42, y0 - 60, color=LIG, dash="3 3", w=1.4)
    f.text(240, 60, "intramolecular H-bond", size=12, color=LIG, anchor="start")
    f.text(240, 78, "stabilises the conjugate base", size=12, color=LIG, anchor="start")
    f.text(240, 96, "(ortho effect) → strongest acid", size=12, color=LIG, anchor="start")
    f.text(120, 175, "o-hydroxybenzoate (salicylate) ion", size=12, color=MUTED)
    return f.svg()


# ================================================================== SET 2
def fig_s2_daniell():
    """Q16(i) -- Daniell cell with salt bridge."""
    f = Fig(600, 280, "fig_s2_daniell")
    beaker(f, 140, 110, 120, 130, 140, fill="#eef3f6")
    beaker(f, 340, 110, 120, 130, 140, fill="#cfe5f7")
    f.rect(170, 85, 14, 120, color=INK, w=1.2, fill="#bbb")
    f.rect(415, 85, 14, 120, color=INK, w=1.2, fill="#d98b6a")
    f.path("M 225 200 L 225 75 L 375 75 L 375 200", w=12, color="#aaa")
    f.path("M 225 200 L 225 75 L 375 75 L 375 200", w=8, color="#f4f4f4")
    f.path("M 177 85 L 177 40 L 286 40", w=1.6)
    f.path("M 314 40 L 422 40 L 422 85", w=1.6)
    voltmeter(f, 300, 40)
    f.arrow(200, 22, 400, 22, w=1.2, color=BLUE)
    f.text(300, 15, "electrons (external circuit)", size=11, color=BLUE)
    f.text(165, 80, "Zn anode (−)", size=12, anchor="end")
    f.text(435, 80, "(+) Cu cathode", size=12, anchor="start")
    f.text(300, 68, "salt bridge (KCl / KNO₃ in agar)", size=11)
    f.arrow(268, 95, 238, 95, w=1.1, color=LIG); chem(f, 253, 112, [("Cl", ""), ("−", "p")], size=11, color=LIG)
    f.arrow(332, 95, 362, 95, w=1.1, color=LIG); chem(f, 347, 112, [("K", ""), ("+", "p")], size=11, color=LIG)
    chem(f, 200, 228, F("1 M ZnSO4"), size=12)
    chem(f, 400, 228, F("1 M CuSO4"), size=12)
    chem(f, 200, 262, [("Zn → Zn", ""), ("2+", "p"), (" + 2e", ""), ("−", "p")], size=12)
    chem(f, 400, 262, [("Cu", ""), ("2+", "p"), (" + 2e", ""), ("−", "p"), (" → Cu", "")], size=12)
    return f.svg()


def fig_s2_vbt_co_ni():
    """Q21(i)(a) -- [Co(NH3)6]3+ d2sp3 (inner) vs [Ni(NH3)6]2+ sp3d2 (outer)."""
    f = Fig(660, 270, "fig_s2_vbt_co_ni")
    rows = [(30, "Co³⁺ 3d⁶ (free)", {"3d": "21111", "4s": ".", "4p": "...", "4d": "....."}),
            (80, "[Co(NH₃)₆]³⁺", {"3d": "222LL", "4s": "L", "4p": "LLL", "4d": "....."}),
            (160, "Ni²⁺ 3d⁸ (free)", {"3d": "22211", "4s": ".", "4p": "...", "4d": "....."}),
            (210, "[Ni(NH₃)₆]²⁺", {"3d": "22211", "4s": "L", "4p": "LLL", "4d": "LL..."})]
    xs = vbt_rows(f, rows, x0=170)
    brace(f, xs["3d"] + 72, xs["4p"] + 72, 104, "d²sp³ (inner 3d): low spin, diamagnetic")
    brace(f, xs["4s"], xs["4d"] + 48, 234, "sp³d² (outer 4d): two unpaired e⁻, paramagnetic")
    return f.svg()


def fig_s2_fe_cft():
    """Q21(i)(b) -- Fe3+ d5 in a weak field (H2O) and a strong field (CN-)."""
    f = Fig(560, 230, "fig_s2_fe_cft")
    for x0, title, small, t2g, eg in ((60, "[Fe(H₂O)₆]³⁺  (weak field)", True, ["u", "u", "u"], ["u", "u"]),
                                      (320, "[Fe(CN)₆]³⁻  (strong field)", False, ["ud", "ud", "u"], ["", ""])):
        yt, ye = 160, (105 if small else 55)
        level(f, x0 + 20, yt, 3, t2g)
        level(f, x0 + 39, ye, 2, eg)
        chem(f, x0 + 150, yt + 4, [("t", ""), ("2g", "b")], size=13, anchor="start")
        chem(f, x0 + 150, ye + 4, [("e", ""), ("g", "b")], size=13, anchor="start")
        f.arrow(x0 + 5, yt, x0 + 5, ye, w=1.1, color=LIG)
        f.arrow(x0 + 5, ye, x0 + 5, yt, w=1.1, color=LIG)
        chem(f, x0 + 2, (yt + ye) / 2 + 4, [("Δ", ""), ("o", "b")], size=12, color=LIG, anchor="end")
        f.text(x0 + 85, 200, title, size=12)
    chem(f, 145, 222, CF("3", "2") + [(": 5 unpaired (≈5.92 BM)", "")], size=11, color=MUTED)
    chem(f, 405, 222, CF("5", "0") + [(": 1 unpaired (≈1.73 BM)", "")], size=11, color=MUTED)
    return f.svg()


def fig_s2_co_en3_optical():
    """Q21(ii)(b) -- d and l [Co(en)3]3+ as true mirror images."""
    f = Fig(600, 300, "fig_s2_co_en3_optical")

    def octa(cx, cy, s, title):
        P = {"U": (0, -85), "D": (0, 85), "L": (-85, 0), "R": (85, 0),
             "Fr": (-42, 36), "Bk": (42, -36)}
        P = {k: (cx + s * dx, cy + dy) for k, (dx, dy) in P.items()}
        for k, (x, y) in P.items():
            if k == "Bk":
                f.line(cx, cy, x, y, color=MUTED, w=1.4, dash="4 3")
            else:
                f.line(cx, cy, x, y, w=2.6 if k == "Fr" else 1.6)
        # three en chelates spanning cis pairs: U-R, L-Fr? use U-Bk, D-Fr? choose a propeller set
        pairs = (("U", "R"), ("L", "Fr"), ("D", "Bk"))
        for a, b in pairs:
            (x1, y1), (x2, y2) = P[a], P[b]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            vx, vy = mx - cx, my - cy
            L = math.hypot(vx, vy) or 1
            qx, qy = mx + vx / L * 42, my + vy / L * 42
            f.path(f"M {x1} {y1} Q {qx} {qy} {x2} {y2}", color=ACC, w=2.2)
            f.text(mx + vx / L * 30, my + vy / L * 30 + 4, "en", size=12, color=ACC, italic=True)
        f.circle(cx, cy, 15, fill="#fff")
        f.text(cx, cy + 5, "Co", size=13, bold=True)
        for k, (x, y) in P.items():
            f.circle(x, y, 9, fill="#fff", color=INK, w=1.2)
            f.text(x, y + 4, "N", size=11)
        f.text(cx, cy + 135, title, size=13)

    octa(150, 140, 1, "d-isomer")
    octa(450, 140, -1, "l-isomer (mirror image)")
    f.line(300, 20, 300, 260, color=MUTED, dash="6 4")
    f.text(300, 290, "mirror", size=11, color=MUTED)
    return f.svg()


def fig_s2_nicl4_vbt():
    """Q21(ii)(a) -- [NiCl4]2-: Ni2+ 3d8, sp3, 2 unpaired."""
    f = Fig(560, 150, "fig_s2_nicl4_vbt")
    rows = [(30, "Ni²⁺ 3d⁸ (free)", {"3d": "22211", "4s": ".", "4p": "..."}),
            (85, "[NiCl₄]²⁻", {"3d": "22211", "4s": "L", "4p": "LLL"})]
    xs = vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p"), counts=(5, 1, 3))
    brace(f, xs["4s"], xs["4p"] + 72, 110, "sp³ — tetrahedral, 2 unpaired e⁻ (high spin)")
    return f.svg()


def fig_s2_nicn4_vbt():
    """Q1(B)(i) -- [Ni(CN)4]2-: Ni2+ 3d8 paired, dsp2, square planar, diamagnetic."""
    f = Fig(560, 150, "fig_s2_nicn4_vbt")
    rows = [(30, "Ni²⁺ 3d⁸ (free)", {"3d": "22211", "4s": ".", "4p": "..."}),
            (85, "[Ni(CN)₄]²⁻", {"3d": "2222L", "4s": "L", "4p": "LL."})]
    xs = vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p"), counts=(5, 1, 3))
    brace(f, xs["3d"] + 96, xs["4p"] + 48, 110, "dsp² — square planar, no unpaired e⁻")
    return f.svg()


def fig_s2_cft_three():
    """Q21(ii)(c) -- CFT configurations of [CoF6]3-, [Cr(NH3)6]3+, [Cu(CN)6]5-."""
    f = Fig(660, 240, "fig_s2_cft_three")
    sets = ((20, "[CoF₆]³⁻", "Co³⁺ d⁶, F⁻ weak", ["ud", "u", "u"], ["u", "u"], True, ("4", "2", " — 4 unpaired")),
            (240, "[Cr(NH₃)₆]³⁺", "Cr³⁺ d³", ["u", "u", "u"], ["", ""], False, ("3", "0", " — 3 unpaired")),
            (460, "[Cu(CN)₆]⁵⁻", "Cu⁺ d¹⁰", ["ud", "ud", "ud"], ["ud", "ud"], False, ("6", "4", " — diamagnetic")))
    for x0, name, ion, t2g, eg, small, res in sets:
        yt, ye = 160, (110 if small else 70)
        level(f, x0 + 30, yt, 3, t2g)
        level(f, x0 + 49, ye, 2, eg)
        chem(f, x0 + 155, yt + 4, [("t", ""), ("2g", "b")], size=13, anchor="start")
        chem(f, x0 + 155, ye + 4, [("e", ""), ("g", "b")], size=13, anchor="start")
        f.arrow(x0 + 15, yt, x0 + 15, ye, w=1.1, color=LIG)
        f.arrow(x0 + 15, ye, x0 + 15, yt, w=1.1, color=LIG)
        f.text(x0 + 95, 25, name, size=14, bold=True)
        f.text(x0 + 95, 42, ion, size=11, color=MUTED)
        chem(f, x0 + 95, 190, CF(res[0], res[1]) + [(res[2], "")], size=11.5, color=(LIG if "dia" in res[2] else INK))
    f.text(330, 225, "(Δo not to a common scale; weak-field F⁻ gives the small Δo)", size=11, color=MUTED)
    return f.svg()
