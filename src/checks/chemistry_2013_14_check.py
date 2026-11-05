"""Recompute every numerical answer in chemistry_2013_14 (theory) and chemistry_2013_14_prac."""
import math
ok = True
def chk(name, got, want, tol=5e-3):
    global ok
    good = abs(got - want) <= tol * max(1, abs(want))
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: computed {got:.6g}, printed {want}")

# 1(c)(iv): Faraday II -- Cu+ needs 1 e, Cu2+ needs 2 e; same charge => ratio of masses 2:1
chk("1(c)(iv) mass ratio Cu(I):Cu(II)", (63.5 / 1) / (63.5 / 2), 2)

# 2(c) molar conductivity of CuSO4
G = 2.768e-3 * 250.2                      # cell constant, cm^-1
chk("2(c) cell constant", G, 0.6925)
kap = G / 8331
chk("2(c) kappa CuSO4 (S cm^-1)", kap, 8.313e-5)
Lm = kap * 1000 / 0.01
chk("2(c) Lambda_m (S cm2 mol-1)", Lm, 8.313)

# 2(d) benzene/toluene equal masses (take 100 g each)
nb, nt = 100 / 78, 100 / 92
xb = nb / (nb + nt)
chk("2(d) x_benzene", xb, 0.5412)
P = 150 * xb + 45 * (1 - xb)
chk("2(d) P total (mm Hg)", P, 101.8)

# 2(e) glycerine isotonic with 2 % glucose
c = (2 / 180) / 0.100                     # mol L-1
chk("2(e) conc glucose", c, 0.1111)
M = 10.2 / c
chk("2(e) M glycerine", M, 91.8)

# 3(c) Kohlrausch
L = 2.8e-2 + 2 * 2.481e-2 - 2 * 1.265e-2
chk("3(c) Lambda0 Ba(OH)2 (S m2 mol-1)", L, 5.232e-2)

# 3(d) cane sugar / glucose
Kf = (273.15 - 271) / 0.1539
chk("3(d) Kf implied", Kf, 13.97)
chk("3(d) 5 % sugar molality check", (5 / 342) / 0.095, 0.1539)
mg = (5 / 180) / 0.095
chk("3(d) molality glucose", mg, 0.2924)
dT = Kf * mg
chk("3(d) dTf glucose", dT, 4.08)
chk("3(d) Tf glucose solution (K)", 273.15 - dT, 269.07)

# 4(b) 0.5 % KCl freezes at -0.24 C, Kf(water) = 1.86 assumed
m = (0.5 / 74.5) / 0.0995
chk("4(b) molality KCl", m, 0.06745)
dTc = 1.86 * m
chk("4(b) dTf calc", dTc, 0.1255)
chk("4(b) i", 0.24 / dTc, 1.91)

# ---------------- practical (chemistry_2013_14_prac): titration KMnO4 / oxalic acid
Mk = 1.1 / 158
chk("P1(i) M KMnO4", Mk, 0.006962, 1e-4)
V_ox, titre = 20.0, 24.60
Mox = 2.5 * Mk * titre / V_ox
chk("P1(ii) M oxalic", Mox, 0.02141, 1e-3)
s = Mox * 126
chk("P1(iii) g/L", s, 2.697, 1e-3)
chk("P1(iv) purity %", s / 3.0 * 100, 89.9, 1e-3)
print("expected titre at 100 % purity (mL):", round(0.4 * (3.0 / 126) * 20 / Mk, 2))
# review: unconfirmed practical observations must not be asserted as fact
import os
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "chemistry_2013_14_prac.py")).read()
_good = 'becomes blue/dull' not in _src and "could not be confirmed" in _src
ok &= _good
print(("ok " if _good else "BAD") + " chemistry_2013_14_prac: unconfirmed observation flagged, not asserted")
print("ALL OK" if ok else "FAILURES")
