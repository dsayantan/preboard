"""Figures for Chemistry pre-board 2013-14 (chemistry_2013_14, chemistry_2013_14_prac)."""
import math
from svg import Fig


def _ring(f, cx, cy, r=28):
    """Benzene ring (Kekule), pointy top. Returns the six vertices, clockwise from the top."""
    v = [(cx + r * math.cos(math.radians(-90 + 60 * k)), cy + r * math.sin(math.radians(-90 + 60 * k)))
         for k in range(6)]
    for k in range(6):
        a, b = v[k], v[(k + 1) % 6]
        f.line(f"{a[0]:.1f}", f"{a[1]:.1f}", f"{b[0]:.1f}", f"{b[1]:.1f}", w=1.6)
    for k in (0, 2, 4):                       # inner lines of the three C=C
        a, b = v[k], v[(k + 1) % 6]
        s = 0.78
        ax = cx + s * (a[0] - cx); ay = cy + s * (a[1] - cy)
        bx = cx + s * (b[0] - cx); by = cy + s * (b[1] - cy)
        mx, my = (ax + bx) / 2, (ay + by) / 2
        ax, ay = mx + 0.8 * (ax - mx), my + 0.8 * (ay - my)
        bx, by = mx + 0.8 * (bx - mx), my + 0.8 * (by - my)
        f.line(f"{ax:.1f}", f"{ay:.1f}", f"{bx:.1f}", f"{by:.1f}", w=1.4)
    return v


def _sub(f, v, cx, cy, k, label, L=22, size=14):
    """Bond from ring vertex k outward and a group label at its end."""
    x, y = v[k]
    dx, dy = x - cx, y - cy
    n = math.hypot(dx, dy)
    ex, ey = x + L * dx / n, y + L * dy / n
    f.line(f"{x:.1f}", f"{y:.1f}", f"{ex:.1f}", f"{ey:.1f}")
    tx, ty = ex + 4 * dx / n, ey + 4 * dy / n
    anchor = "middle" if abs(dx) < 1 else ("start" if dx > 0 else "end")
    if anchor == "middle":
        ty += -4 if dy < 0 else 14
    else:
        ty += 5
    f.text(f"{tx:.1f}", f"{ty:.1f}", label, size=size, anchor=anchor)


def fig_q1b3_salicylic():
    """Phenol + CCl4 / NaOH, then H3O+ -> salicylic acid (2-hydroxybenzoic acid)."""
    f = Fig(520, 170, "fig_q1b3_salicylic")
    v = _ring(f, 80, 105); _sub(f, v, 80, 105, 0, "OH")
    f.text(80, 162, "phenol", size=13)
    f.arrow(140, 105, 300, 105)
    f.text(220, 95, "CCl₄, NaOH (aq), heat", size=13)
    f.text(220, 125, "then H₃O⁺", size=13)
    v = _ring(f, 380, 105); _sub(f, v, 380, 105, 0, "OH"); _sub(f, v, 380, 105, 1, "COOH")
    f.text(380, 162, "salicylic acid", size=13)
    return f.svg()


def fig_q2b_conductance():
    """kappa falls with dilution, Lambda_m rises (strong electrolyte; weak one sharply)."""
    f = Fig(560, 250, "fig_q2b_conductance")
    for i, (x0, ylab, title) in enumerate(((60, "κ", "specific conductance"),
                                            (340, "Λ", "molar conductivity"))):
        X = lambda u, x0=x0: x0 + 200 * u
        Y = lambda w: 200 - 160 * w
        f.arrow(X(0), Y(0), X(1.05), Y(0), w=1.2)
        f.arrow(X(0), Y(0), X(0), Y(1.05), w=1.2)
        f.text(X(1.05), Y(0) + 20, "dilution (1/C) →", size=12, anchor="end")
        f.text(X(0) - 8, Y(1.0), ylab, italic=True, size=15, anchor="end", sub=("m" if i else None))
        f.text(X(0.5), 235, title, size=13)
        us = [0.03 + k * 0.97 / 60 for k in range(61)]
        if i == 0:
            pts = [(X(u), Y(0.08 + 0.85 * math.exp(-4.5 * u))) for u in us]
            f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color="#c0392b", w=2)
        else:
            pts = [(X(u), Y(0.62 + 0.25 * (1 - math.exp(-5 * u)))) for u in us]
            f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color="#1f4e8c", w=2)
            f.text(X(1.0), Y(0.92), "strong (KCl)", size=12, anchor="end", color="#1f4e8c")
            pts = [(X(u), Y(0.05 + 0.75 * u ** 2.2)) for u in us]
            f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color="#7d3c98", w=2)
            f.text(X(0.08), Y(0.45), "weak (CH₃COOH)", size=12, anchor="start", color="#7d3c98")
    return f.svg()


def fig_q1a5_aminoacid():
    """Glycine: cation in acid, zwitterion, anion in alkali."""
    f = Fig(600, 120, "fig_q1a5_aminoacid")
    f.text(95, 55, "H₃N⁺–CH₂–COOH", size=15)
    f.text(95, 80, "cation (pH < pI)", size=12, color="#c0392b")
    f.text(95, 100, "moves to cathode", size=12, color="#c0392b")
    f.arrow(205, 50, 245, 50); f.arrow(245, 62, 205, 62)
    f.text(225, 40, "OH⁻", size=11); f.text(225, 78, "H⁺", size=11)
    f.text(330, 55, "H₃N⁺–CH₂–COO⁻", size=15)
    f.text(330, 80, "zwitterion (pH = pI)", size=12)
    f.arrow(435, 50, 475, 50); f.arrow(475, 62, 435, 62)
    f.text(455, 40, "OH⁻", size=11); f.text(455, 78, "H⁺", size=11)
    f.text(550, 55, "H₂N–CH₂–COO⁻", size=15)
    f.text(550, 80, "anion (pH > pI)", size=12, color="#1f4e8c")
    f.text(550, 100, "moves to anode", size=12, color="#1f4e8c")
    return f.svg()
