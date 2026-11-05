"""Figures for Chemistry pre-board 2024-25, Set 2 (chemistry_2024_25_s2).

Helpers copied (not imported) from chemistry_2025_26_figs so this module stands alone.
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




def ring_h(f, cx, cy, r=24, circle=True):
    """Benzene ring with vertices at left and right.  0 right, 1 lower-right, 2 lower-left,
    3 left, 4 upper-left, 5 upper-right."""
    v = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
         for a in (0, 60, 120, 180, 240, 300)]
    f.path("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in v) + " Z", w=1.6)
    if circle:
        f.circle(cx, cy, r * 0.58, w=1.3)
    return v


def rxn_arrow(f, x1, x2, y, above="", below="", size=11):
    f.arrow(x1, y, x2, y, w=1.4)
    if above:
        T(f, (x1 + x2) / 2, y - 10, above, size=size)
    if below:
        T(f, (x1 + x2) / 2, y + 15, below, size=size)


# ================================================================== VBT
def fig_b_cucl4_vbt():
    """1(A)(iv) -- [CuCl4]2-: Cu2+ 3d9, sp3, tetrahedral, 1 unpaired e-."""
    f = Fig(560, 150, "fig_b_cucl4_vbt")
    rows = [(30, "Cu²⁺ 3d⁹ (free)", {"3d": "22221", "4s": ".", "4p": "..."}),
            (85, "[CuCl₄]²⁻", {"3d": "22221", "4s": "L", "4p": "LLL"})]
    xs = vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p"), counts=(5, 1, 3))
    brace(f, xs["4s"], xs["4p"] + 72, 110, "sp³ — tetrahedral, 1 unpaired e⁻")
    return f.svg()


def fig_b_fecn6_vbt():
    """Q7 -- [Fe(CN)6]3-: Fe3+ 3d5, CN- pairs four electrons, d2sp3, 1 unpaired e-."""
    f = Fig(560, 150, "fig_b_fecn6_vbt")
    rows = [(30, "Fe³⁺ 3d⁵ (free)", {"3d": "11111", "4s": ".", "4p": "..."}),
            (85, "[Fe(CN)₆]³⁻", {"3d": "221LL", "4s": "L", "4p": "LLL"})]
    xs = vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p"), counts=(5, 1, 3))
    brace(f, xs["3d"] + 72, xs["4p"] + 72, 110, "d²sp³ (inner orbital) — 1 unpaired e⁻, paramagnetic")
    return f.svg()


def fig_b_conh36_vbt():
    """Q20(iii) -- [Co(NH3)6]3+: Co3+ 3d6 paired, d2sp3, diamagnetic."""
    f = Fig(560, 150, "fig_b_conh36_vbt")
    rows = [(30, "Co³⁺ 3d⁶ (free)", {"3d": "21111", "4s": ".", "4p": "..."}),
            (85, "[Co(NH₃)₆]³⁺", {"3d": "222LL", "4s": "L", "4p": "LLL"})]
    xs = vbt_rows(f, rows, x0=190, shells=("3d", "4s", "4p"), counts=(5, 1, 3))
    brace(f, xs["3d"] + 72, xs["4p"] + 72, 110, "d²sp³ (inner orbital) — no unpaired e⁻, diamagnetic")
    return f.svg()


# ================================================================== CFT
def _split(f, x0, title, sub_, t2g, eg, small, res):
    yt, ye = 160, (110 if small else 65)
    level(f, x0 + 30, yt, 3, t2g)
    level(f, x0 + 49, ye, 2, eg)
    chem(f, x0 + 155, yt + 4, [("t", ""), ("2g", "b")], size=13, anchor="start")
    chem(f, x0 + 155, ye + 4, [("e", ""), ("g", "b")], size=13, anchor="start")
    f.arrow(x0 + 15, yt, x0 + 15, ye, w=1.1, color=LIG)
    f.arrow(x0 + 15, ye, x0 + 15, yt, w=1.1, color=LIG)
    chem(f, x0 + 11, (yt + ye) / 2 + 4, [("Δ", ""), ("o", "b")], size=12, color=LIG, anchor="end")
    f.text(x0 + 95, 22, title, size=14, bold=True)
    f.text(x0 + 95, 40, sub_, size=11, color=MUTED)
    chem(f, x0 + 95, 192, res, size=11.5)


def fig_b_mn_cft():
    """Q15(ii) -- Mn3+ d4: low spin in CN- (t2g4 eg0), high spin in Cl- (t2g3 eg1)."""
    f = Fig(560, 230, "fig_b_mn_cft")
    _split(f, 30, "[Mn(CN)₆]³⁻", "strong field, Δo > P: low spin", ["ud", "u", "u"], ["", ""], False,
           CF("4", "0") + [(": CFSE = −1.6 Δ", ""), ("o", "b"), (" + P", "")])
    _split(f, 300, "[MnCl₆]³⁻", "weak field, Δo < P: high spin", ["u", "u", "u"], ["u", ""], True,
           CF("3", "1") + [(": CFSE = −0.6 Δ", ""), ("o", "b")])
    f.text(280, 222, "(Δo not to a common scale)", size=11, color=MUTED)
    return f.svg()


def fig_b_cu_dd():
    """Q15(i) -- Cu2+ d9 in [Cu(H2O)4]2+ (octahedral field shown): d-d transition t2g -> eg."""
    f = Fig(580, 220, "fig_b_cu_dd")
    # free ion: five degenerate d orbitals (one half-filled)
    level(f, 20, 120, 5, ["ud", "ud", "ud", "ud", "u"], w=24, gap=6)
    f.text(84, 150, "Cu²⁺ 3d⁹, no ligands:", size=11, color=MUTED)
    f.text(84, 165, "d orbitals not split,", size=11, color=MUTED)
    f.text(84, 180, "no d–d absorption: white", size=11, color=MUTED)
    x0 = 270
    yt, ye = 160, 70
    level(f, x0 + 30, yt, 3, ["ud", "ud", "ud"])
    level(f, x0 + 49, ye, 2, ["ud", "u"])
    chem(f, x0 + 155, yt + 4, [("t", ""), ("2g", "b")], size=13, anchor="start")
    chem(f, x0 + 155, ye + 4, [("e", ""), ("g", "b")], size=13, anchor="start")
    f.arrow(x0 + 15, yt, x0 + 15, ye, w=1.1, color=LIG)
    f.arrow(x0 + 15, ye, x0 + 15, yt, w=1.1, color=LIG)
    chem(f, x0 + 11, (yt + ye) / 2 + 4, [("Δ", ""), ("o", "b")], size=12, color=LIG, anchor="end")
    f.path(f"M {x0+120} {yt-22} C {x0+150} {yt-50} {x0+150} {ye+30} {x0+132} {ye+8}", color=BLUE, w=1.6, arrow=True)
    f.text(x0 + 185, (yt + ye) / 2 + 4, "hν absorbed", size=11, color=BLUE, anchor="start")
    f.text(x0 + 185, (yt + ye) / 2 + 18, "(red-orange)", size=11, color=BLUE, anchor="start")
    f.text(x0 + 95, 25, "water ligands split the d set", size=12)
    f.text(x0 + 95, 195, "d–d transition: blue colour seen", size=11, color=MUTED)
    f.line(250, 20, 250, 200, color="#ccc", dash="4 3")
    return f.svg()


# ================================================================== cell
def fig_b_daniell():
    """Q16(i) -- Daniell cell with salt bridge."""
    f = Fig(600, 280, "fig_b_daniell")
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


# ================================================================== isomers
def fig_b_cocl2en2_optical():
    """Q20(iv) -- cis-[CoCl2(en)2]+ : the two enantiomers (mirror images).
    Cl at U and L (cis); en spans R-Bk and D-Fr (both cis pairs)."""
    f = Fig(620, 310, "fig_b_cocl2en2_optical")

    def octa(cx, cy, s, title):
        P = {"U": (0, -85), "D": (0, 85), "L": (-85, 0), "R": (85, 0), "Fr": (-42, 36), "Bk": (42, -36)}
        P = {k: (cx + s * dx, cy + dy) for k, (dx, dy) in P.items()}
        for k, (x, y) in P.items():
            if k == "Bk":
                f.line(cx, cy, x, y, color=MUTED, w=1.4, dash="4 3")
            else:
                f.line(cx, cy, x, y, w=2.6 if k == "Fr" else 1.6)
        for a, b in (("R", "Bk"), ("D", "Fr")):
            (x1, y1), (x2, y2) = P[a], P[b]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            vx, vy = mx - cx, my - cy
            L = math.hypot(vx, vy) or 1
            qx, qy = mx + vx / L * 40, my + vy / L * 40
            f.path(f"M {x1} {y1} Q {qx} {qy} {x2} {y2}", color=ACC, w=2.2)
            f.text(mx + vx / L * 30, my + vy / L * 30 + 4, "en", size=12, color=ACC, italic=True)
        f.circle(cx, cy, 15, fill="#fff")
        f.text(cx, cy + 5, "Co", size=13, bold=True)
        for k, (x, y) in P.items():
            if k in ("U", "L"):
                f.circle(x, y, 12, fill="#e8f5e9", color="#2e7d32", w=1.2)
                f.text(x, y + 4, "Cl", size=11, color="#2e7d32", bold=True)
            else:
                f.circle(x, y, 9, fill="#fff", color=INK, w=1.2)
                f.text(x, y + 4, "N", size=11)
        f.text(cx, cy + 140, title, size=13)

    octa(155, 140, 1, "cis-[CoCl₂(en)₂]⁺ : enantiomer I")
    octa(465, 140, -1, "enantiomer II (mirror image)")
    f.line(310, 20, 310, 260, color=MUTED, dash="6 4")
    f.text(310, 300, "mirror", size=11, color=MUTED)
    return f.svg()


def fig_b_trans_cocl2en2():
    """Q20(iv) -- trans isomer: has a mirror plane, optically inactive."""
    f = Fig(560, 250, "fig_b_trans_cocl2en2")
    cx, cy = 280, 120
    P = {"U": (0, -85), "D": (0, 85), "L": (-85, 0), "R": (85, 0), "Fr": (-42, 36), "Bk": (42, -36)}
    P = {k: (cx + dx, cy + dy) for k, (dx, dy) in P.items()}
    for k, (x, y) in P.items():
        if k == "Bk":
            f.line(cx, cy, x, y, color=MUTED, w=1.4, dash="4 3")
        else:
            f.line(cx, cy, x, y, w=2.6 if k == "Fr" else 1.6)
    for a, b in (("L", "Fr"), ("R", "Bk")):
        (x1, y1), (x2, y2) = P[a], P[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        vx, vy = mx - cx, my - cy
        L = math.hypot(vx, vy) or 1
        f.path(f"M {x1} {y1} Q {mx + vx/L*40} {my + vy/L*40} {x2} {y2}", color=ACC, w=2.2)
        f.text(mx + vx / L * 30, my + vy / L * 30 + 4, "en", size=12, color=ACC, italic=True)
    f.circle(cx, cy, 15, fill="#fff"); f.text(cx, cy + 5, "Co", size=13, bold=True)
    for k, (x, y) in P.items():
        if k in ("U", "D"):
            f.circle(x, y, 12, fill="#e8f5e9", color="#2e7d32", w=1.2)
            f.text(x, y + 4, "Cl", size=11, color="#2e7d32", bold=True)
        else:
            f.circle(x, y, 9, fill="#fff", color=INK, w=1.2); f.text(x, y + 4, "N", size=11)
    f.text(cx, 240, "trans: plane of symmetry — optically inactive", size=12, color=MUTED)
    return f.svg()


# ================================================================== phenol (Q19)
def fig_b_picric():
    """Q19(b) -- phenol -> phenol-2,4-disulphonic acid (Y) -> 2,4,6-trinitrophenol (Z)."""
    f = Fig(640, 190, "fig_b_picric")
    mol(f, 70, 95, {0: "OH"}, name="phenol", r=26, namedy=72)
    rxn_arrow(f, 120, 200, 95, "conc. H2SO4")
    mol(f, 290, 95, {0: "OH", 1: "SO3H", 3: "SO3H"}, r=26)
    f.text(290, 180, "Y: phenol-2,4-disulphonic acid", size=12, color=MUTED)
    rxn_arrow(f, 380, 460, 95, "conc. HNO3")
    mol(f, 545, 95, {0: "OH", 1: "NO2", 3: "NO2", 5: "NO2"}, r=26)
    f.text(545, 180, "Z: 2,4,6-trinitrophenol (picric acid)", size=12, color=MUTED)
    return f.svg()


def fig_b_azo():
    """Q19(c) -- benzenediazonium chloride + phenol (OH-) -> p-hydroxyazobenzene (orange)."""
    f = Fig(640, 150, "fig_b_azo")
    v = ring_h(f, 60, 70, r=24)
    f.line(v[0][0], v[0][1], v[0][0] + 14, v[0][1])
    chem(f, v[0][0] + 16, v[0][1] + 5, [("N", ""), ("2", "b"), ("+", "p"), ("Cl", ""), ("−", "p")], size=13, anchor="start")
    f.text(160, 75, "+", size=18)
    v = ring_h(f, 210, 70, r=24)
    f.line(v[0][0], v[0][1], v[0][0] + 14, v[0][1])
    T(f, v[0][0] + 16, v[0][1] + 5, "OH", size=13, anchor="start")
    rxn_arrow(f, 270, 345, 70, "OH^−", "273–278 K")
    a = ring_h(f, 385, 70, r=24)
    x1 = a[0][0]
    f.line(x1, 70, x1 + 12, 70)
    f.text(x1 + 20, 75, "N", size=13)
    f.line(x1 + 27, 67, x1 + 43, 67); f.line(x1 + 27, 73, x1 + 43, 73)
    f.text(x1 + 50, 75, "N", size=13)
    b = ring_h(f, x1 + 58 + 24 + 12, 70, r=24)
    f.line(x1 + 57, 70, b[3][0], 70)
    f.line(b[0][0], 70, b[0][0] + 14, 70)
    T(f, b[0][0] + 16, 75, "OH", size=13, anchor="start")
    f.text(465, 130, "p-hydroxyazobenzene (orange dye)  + Cl⁻ + H₂O", size=12, color=MUTED)
    return f.svg()


def fig_b_kolbe():
    """Q19(d) -- Kolbe's reaction: phenol -> sodium phenoxide -> sodium salicylate -> salicylic acid."""
    f = Fig(700, 170, "fig_b_kolbe")
    mol(f, 50, 95, {0: "OH"}, r=24, name="phenol", namedy=62)
    rxn_arrow(f, 90, 145, 95, "NaOH")
    mol(f, 195, 95, {0: "O^− Na^+"}, r=24, name="sodium phenoxide", namedy=62)
    rxn_arrow(f, 240, 340, 95, "CO2, 400 K", "4–7 atm")
    mol(f, 395, 95, {0: "OH", 1: "COO^− Na^+"}, r=24, name="sodium salicylate", namedy=62)
    rxn_arrow(f, 495, 560, 95, "H3O^+")
    mol(f, 610, 95, {0: "OH", 1: "COOH"}, r=24, name="salicylic acid", namedy=62)
    return f.svg()
