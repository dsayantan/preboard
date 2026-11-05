"""Figures for Chemistry pre-board 2016-17 (agent B)."""
from svg import Fig
from chemistry_1517_lib import (INK, ACC, WARM, MUTED, LIG, box_row, level, chem, F)


def _split(f, uid_title, lower_n, lower_fill, upper_n, upper_fill, lower_lab, upper_lab,
           delta_lab, title, notes, ion_parts):
    """Crystal-field splitting diagram: free-ion d level on the left, split levels on the right."""
    # free ion: five degenerate orbitals at the barycentre
    # octahedral: eg at +0.6 Δo, t2g at -0.4 Δo (Δo = 100 px);
    # tetrahedral: t2 at +0.4 Δt, e at -0.6 Δt (Δt = 4/9 Δo ≈ 55 px)
    yb, yl, yu = 150, 190, 90
    if lower_n == 2:
        yl, yu = 150 + 33, 150 - 22
    f.text(80, 108, "free ion", size=13, color=MUTED)
    chem(f, 80, 128, ion_parts, size=14)
    level(f, 22, yb, 5, [""] * 5, w=22, gap=8)
    # barycentre dashed
    f.line(160, yb, 400, yb, color=MUTED, w=1, dash="4 4")
    f.text(400, yb + 16, "barycentre", size=11, color=MUTED, anchor="end")
    # connectors
    f.line(160, yb, 205, yu, color=MUTED, w=1, dash="2 3")
    f.line(160, yb, 205, yl, color=MUTED, w=1, dash="2 3")
    xu = level(f, 210, yu, upper_n, upper_fill)
    xl = level(f, 210, yl, lower_n, lower_fill)
    f.text(xu + 12, yu + 5, upper_lab[0], size=15, italic=True, anchor="start", sub=upper_lab[1])
    f.text(xl + 12, yl + 5, lower_lab[0], size=15, italic=True, anchor="start", sub=lower_lab[1])
    # Delta arrow
    f.arrow(345, yl, 345, yu + 2, color=WARM, w=1.4)
    f.arrow(345, yu, 345, yl - 2, color=WARM, w=1.4)
    chem(f, 352, yu + 16, delta_lab, size=14, color=WARM, anchor="start")
    f.text(240, 24, title, size=14, bold=True)
    for k, n in enumerate(notes):
        if isinstance(n, str):
            n = [(n, "")]
        chem(f, 240, 232 + 22 * k, n, size=12.5, bold=(k == len(notes) - 1))


# ------------------------------------------------------------------ Q1(d)(i)
def fig_cof6_cft():
    f = Fig(480, 290, "fig_cof6_cft")
    _split(f, "cof6", 3, ["ud", "u", "u"], 2, ["u", "u"], ("t", "2g"), ("e", "g"),
           [("Δ", ""), ("o", "b"), (" small", "")],
           "[CoF₆]³⁻ : Co³⁺ (3d⁶) in an octahedral field",
           [[("weak-field F", ""), ("−", "p"), (": Δ", ""), ("o", "b"), (" < pairing energy, so high spin", "")],
            [("t", ""), ("2g", "b"), ("4", "p"), (" e", ""), ("g", "b"), ("2", "p"), ("  →  4 unpaired electrons", "")]],
           [("Co", ""), ("3+", "p"), ("  3d", ""), ("6", "p")])
    return f.svg()


# ------------------------------------------------------------------ Q5(b)
def fig_fecl4_cft():
    f = Fig(480, 290, "fig_fecl4_cft")
    _split(f, "fecl4", 2, ["u", "u"], 3, ["u", "u", "u"], ("e", ""), ("t", "2"),
           [("Δ", ""), ("t", "b"), (" ≈ 4/9 Δ", ""), ("o", "b")],
           "[FeCl₄]⁻ : Fe³⁺ (3d⁵) in a tetrahedral field",
           ["Cl⁻ is weak-field and Δt is small: always high spin",
            "e² t₂³  →  5 unpaired electrons (μ = 5.92 BM)"],
           [("Fe", ""), ("3+", "p"), ("  3d", ""), ("5", "p")])
    return f.svg()


# ------------------------------------------------------------------ Q5(c)
def fig_ni_vbt():
    f = Fig(470, 330, "fig_ni_vbt")
    x0 = 188
    for x, h in ((x0 + 55, "3d"), (x0 + 151, "4s"), (x0 + 210, "4p")):
        f.text(x, 22, h, size=13, italic=True)

    def row(y, label, d, s, p):
        chem(f, x0 - 12, y + 15, label, size=13, anchor="end")
        box_row(f, x0, y, d)
        box_row(f, x0 + 140, y, s)
        box_row(f, x0 + 177, y, p)

    row(34, [("Ni", ""), ("2+", "p"), ("  [Ar] 3d", ""), ("8", "p")], ["ud", "ud", "ud", "u", "u"], [""], ["", "", ""])
    # tetrahedral
    row(96, F("[NiCl4]^2−"), ["ud", "ud", "ud", "u", "u"], ["L"], ["L", "L", "L"])
    f.path(f"M {x0+140} 124 L {x0+140} 132 L {x0+243} 132 L {x0+243} 124", color=LIG, w=1.3)
    chem(f, x0 + 191, 148, [("sp", ""), ("3", "p"), (" → tetrahedral", "")], 13, color=LIG)
    f.text(235, 172, "weak-field Cl⁻: no pairing; 2 unpaired e⁻ → paramagnetic", size=12.5, bold=True)
    # square planar
    row(206, F("[Ni(CN)4]^2−"), ["ud", "ud", "ud", "ud", "L"], ["L"], ["L", "L", ""])
    f.path(f"M {x0+88} 234 L {x0+88} 242 L {x0+221} 242 L {x0+221} 234", color=LIG, w=1.3)
    chem(f, x0 + 155, 258, [("dsp", ""), ("2", "p"), (" → square planar", "")], 13, color=LIG)
    f.text(235, 282, "strong-field CN⁻ pairs the two odd electrons, freeing one 3d orbital;",
           size=12, color=MUTED)
    f.text(235, 302, "no unpaired electron → diamagnetic", size=12.5, bold=True)
    f.text(235, 324, "x x = electron pair donated by a ligand", size=11.5, color=LIG)
    return f.svg()


# ------------------------------------------------------------------ Q4(b)(i)
def fig_arrhenius_plot():
    f = Fig(440, 300, "fig_arrhenius_plot")
    ox, oy = 60, 260
    f.arrow(ox, oy, 420, oy)
    f.arrow(ox, oy, ox, 20)
    chem(f, 400, 288, [("1/T  (K", ""), ("−1", "p"), (")", "")], 13)
    f.text(18, 140, "log k", size=14, italic=True)
    # data line from (150, 70) to (380, 210) with points; dashed extrapolation to the y-axis
    x1, y1, x2, y2 = 150, 112, 380, 232
    m = (y2 - y1) / (x2 - x1)
    yA = y1 - m * (x1 - ox)
    f.line(ox, yA, x1, y1, color=ACC, w=1.4, dash="5 4")
    f.line(x1, y1, x2, y2, color=ACC, w=2.2)
    for k in range(5):
        x = x1 + 20 + k * 48
        y = y1 + m * (x - x1) + (3, -4, 2, -2, 3)[k]
        f.circle(x, y, 3.5, fill=INK)
    f.circle(ox, yA, 3.5, fill=WARM, color=WARM)
    f.text(ox + 8, yA - 6, "intercept = log A", size=12.5, color=WARM, anchor="start")
    # slope triangle
    xa, xb = 220, 320
    ya, yb = y1 + m * (xa - x1), y1 + m * (xb - x1)
    f.line(xa, ya, xb, ya, color=WARM, w=1.2)
    f.line(xb, ya, xb, yb, color=WARM, w=1.2)
    chem(f, (xa + xb) / 2, ya - 8, [("Δ(1/T)", "")], 12.5, color=WARM)
    chem(f, xb + 6, (ya + yb) / 2 + 4, [("Δ log k", "")], 12.5, color=WARM, anchor="start")
    chem(f, 290, 40, [("slope = −E", ""), ("a", "b"), (" / 2.303R", "")], 14, bold=True)
    chem(f, 290, 62, [("⇒  E", ""), ("a", "b"), (" = −2.303 R × slope", "")], 13)
    return f.svg()


# ------------------------------------------------------------------ Q10(b)
def fig_amino_acid_forms():
    f = Fig(660, 210, "fig_amino_acid_forms")
    cols = [(110, "in acid (low pH)", [("H", ""), ("3", "b"), ("N", ""), ("+", "p"), ("–CHR–COOH", "")],
             "cation", "→ moves to cathode (−)"),
            (330, "at the isoelectric point", [("H", ""), ("3", "b"), ("N", ""), ("+", "p"), ("–CHR–COO", ""), ("−", "p")],
             "zwitter ion (net charge 0)", "does not migrate"),
            (550, "in alkali (high pH)", [("H", ""), ("2", "b"), ("N–CHR–COO", ""), ("−", "p")],
             "anion", "→ moves to anode (+)")]
    for x, head, parts, kind, move in cols:
        f.rect(x - 98, 40, 196, 120, color=MUTED, w=1, rx=8)
        f.text(x, 30, head, size=12.5, color=MUTED)
        chem(f, x, 86, parts, 15)
        f.text(x, 116, kind, size=13, bold=True)
        f.text(x, 142, move, size=13, color=(WARM if "anode" in move or "cathode" in move else MUTED))
    for xm in (220, 440):
        f.arrow(xm - 8, 90, xm + 8, 90, color=ACC)
        f.arrow(xm + 8, 100, xm - 8, 100, color=ACC)
    chem(f, 220, 76, [("OH", ""), ("−", "p")], 12, color=ACC)
    chem(f, 220, 120, [("H", ""), ("+", "p")], 12, color=ACC)
    chem(f, 440, 76, [("OH", ""), ("−", "p")], 12, color=ACC)
    chem(f, 440, 120, [("H", ""), ("+", "p")], 12, color=ACC)
    f.text(330, 195, "The charge on the amino acid, and so its direction of migration, depends on the pH.",
           size=12.5)
    return f.svg()
