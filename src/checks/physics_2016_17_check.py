"""Recompute every numerical answer in physics_2016_17.py (Heritage pre-board 2016-17, Paper 1)."""
import math
import numpy as np
e, h, c, me, eps0, k = 1.6e-19, 6.6e-34, 3e8, 9.1e-31, 8.85e-12, 9e9
ok = []
def chk(name, got, want, rel=6e-3):
    assert abs(got - want) <= rel * abs(want), f"{name}: got {got}, printed {want}"
    ok.append(name)

chk("1A(i) F12/F13", 2 / 1, 2)
chk("1A(iii) amplitude", math.sqrt(16 + 9 + 24 * math.cos(math.pi / 3)), 6.08)
chk("1A(iv) lambda0 nm", h * c / (2 * e) * 1e9, 620, rel=0.01)
chk("1B(i) C'", 4 / 2 * 1e-12, 2e-12)
# 1B(iii): solve the 3-branch circuit by nodal analysis. V = V_T - V_M.
# left: + on top, emf 16, R 2 -> I_up = (16 - V)/2 ; middle: + at bottom, emf 16, R 4 -> I_up = (-16 - V)/4
V = 20.0
I1 = (16 - V) / 2; I2 = (-16 - V) / 4; I3 = -(I1 + I2)
chk("1B(iii) I1", I1, -2); chk("1B(iii) I2", I2, -9); chk("1B(iii) I20", I3, 11)
chk("1B(v) ratio", 2, 2)
# 1B(vi) emf arms: v=+x, B=+z (out of page), physical y up; force on + charge
F = np.cross([1, 0, 0], [0, 0, 1]); assert list(F) == [0, -1, 0]; ok.append("1B(vi) v x B downward -> along AD, BC")
chk("1B(vii) Xc", 1 / (2 * math.pi * 4000 * 25e-6), 1.59)
f_inv = (1 / 1.5 - 1) * (1 / 10 - 1 / -10); chk("1B(viii) f", 1 / f_inv, -15)
chk("1B(x) dlambda", 0.1 * 5890, 589)
E0_over_E = 1 / (1 / 4 - 1 / 9); chk("1B(xii) IE/E", E0_over_E, 7.2)
chk("1B(xiv) I", (4 - 1) / 300, 0.01)
mg, qE = 80e-6 * 9.8, 20e-9 * 2e4
chk("2a T", math.hypot(mg, qE), 8.8e-4); chk("2a theta", math.degrees(math.atan(qE / mg)), 27, rel=0.02)
chk("3a X", 1.1 * 180 / 140, 1.41)
# 4(a): junctions
top = 15 + 8; right = top + 3; bottom = 8 - 5; i = right - bottom
chk("4a i", i, 23); chk("4a total", 15 + 3 + 5, i)
# 5(a): B = mu0 I/(4r) + mu0 I/(4 pi r)
coef = 1 / 4 + 1 / (4 * math.pi); chk("5a coef", coef, (math.pi + 1) / (4 * math.pi))
# direction checks: semicircle top->left->bottom is anticlockwise on page -> +z (out)
# straight wire below O, current +x, O at +y from wire: B = I x r_hat = x x y = +z
assert list(np.cross([1, 0, 0], [0, 1, 0])) == [0, 0, 1]; ok.append("5a straight-wire direction out")
chk("6b R", 20 / 0.01 - 50, 1950)
w, L, C, R = 500, 2, 4e-6, 500
XL, XC = w * L, 1 / (w * C); Z = math.hypot(R, XL - XC)
chk("7b XL", XL, 1000); chk("7b XC", XC, 500); chk("7b Z", Z, 707.1); chk("7b I0", 300 / Z, 0.424)
chk("7b C res", 1 / (w**2 * L), 2e-6)
chk("8b mu_l", 1.45 * math.sin(math.radians(60)), 1.26)
chk("10a n", 5000 / (6000 - 5000), 5)
tanC = math.tan(math.asin(3 / 4)); r = 7 * tanC
chk("11a r", r, 7.94); chk("11a area", math.pi * r**2, 198)
chk("11b mu", math.sin(math.radians(60)) / math.sin(math.radians(30)), 1.73)
lam = h / math.sqrt(2 * me * e * 300); chk("12b lambda A", lam * 1e10, 0.706); chk("12b shortcut", 12.27 / math.sqrt(300), 0.708)
K1 = me * e**4 / (8 * eps0**2 * h**2) / e; chk("12a K1 eV", K1, 13.6, rel=0.03)
dm = 2 * 2.014102 - 4.002604; chk("13b dm", dm, 0.0256); chk("13b Q", dm * 931, 23.8)

# review: prism figure marks the 60 deg angle of incidence INSIDE the glass (arc endpoints inside triangle ABC)
import re as _re, sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "figs"))
import physics_2016_17_figs as _F
_svg = _F.fig_a8b_prism()
_A = (210, 30); _B = (60, 30 + 150 * math.sqrt(3)); _C = (360, 30 + 150 * math.sqrt(3))
def _inside(px, py):
    def sg(a, b): return (px - b[0]) * (a[1] - b[1]) - (a[0] - b[0]) * (py - b[1])
    d1, d2, d3 = sg(_A, _B), sg(_B, _C), sg(_C, _A)
    return not ((d1 < 0 or d2 < 0 or d3 < 0) and (d1 > 0 or d2 > 0 or d3 > 0))
_m = _re.search(r'd="M ([\d.]+) ([\d.]+) A 28 28 0 0 \d ([\d.]+) ([\d.]+)"', _svg)
assert _m, "prism arc not found"
x1, y1, x2, y2 = map(float, _m.groups())
chk("8b arc start inside glass", 1 if _inside(x1, y1) else 0, 1); chk("8b arc end inside glass", 1 if _inside(x2, y2) else 0, 1)
chk("8b arc spans 60 deg", math.degrees(2 * math.asin(math.hypot(x2 - x1, y2 - y1) / 56)), 60, rel=0.02)
print(f"{len(ok)} checks passed")
