"""Practical 2013-14: regenerate the sample readings from the assumed apparatus and recompute every derived value."""
import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "figs"))
import numpy as np
import physics_2013_14_figs as F
ok = True
def chk(name, got, want, tol):
    global ok
    g = abs(got - want) <= tol; ok &= g
    print(f"{'ok ' if g else 'BAD'} {name}: {got:.5g} vs {want:.5g}")

# Q1: true f = 15.0 cm, F (approx) = 15.0 cm; v from the lens formula, readings within ±0.15 cm (bench LC 0.1 cm)
f, Fa = 15.0, 15.0
U = [70, 60, 50, 40, 30, 20]; V = [19.1, 20.1, 21.5, 24.1, 30.1, 60.1]
for u, v in zip(U, V):
    chk(f"Q1 v at u={u} vs lens formula", v, u*f/(u - f), 0.15)
X = [round(u - Fa, 1) for u in U]; Y = [round(100/(v - Fa), 1) for v in V]
print("Q1 x", X, "y", Y); ok &= X == F.PR_X1 and Y == F.PR_Y1
m, c = np.polyfit(X, Y, 1)
for p in ((4.0, 1.73), (56.0, 24.67)):
    chk(f"Q1 slope-point {p} on best-fit line", m*p[0] + c, p[1], 0.01)
mm = round((24.67 - 1.73)/(56.0 - 4.0), 3); chk("Q1 slope m", mm, 0.441, 1e-9)
chk("Q1 f = 10/sqrt(m)", round(10/math.sqrt(mm), 1), 15.1, 1e-9)
chk("Q1 f vs true f", 10/math.sqrt(mm), f, 0.2)

# Q2: R = 2.5 ohm; l = 100 x/(x + R), readings within ±0.2 cm (LC 0.1 cm)
R = 2.5; L = [28.6, 44.3, 54.7, 61.5, 66.8, 70.5]
for x, l in zip(range(1, 7), L):
    chk(f"Q2 l at x={x} vs balance condition", l, 100*x/(x + R), 0.2)
Y2 = [round(l/(100 - l), 2) for l in L]; print("Q2 y", Y2); ok &= Y2 == F.PR_Y2
m2, c2 = np.polyfit(range(1, 7), Y2, 1)
for p in ((0.5, 0.20), (6.5, 2.60)):
    chk(f"Q2 slope-point {p} on best-fit line", m2*p[0] + c2, p[1], 0.01)
S = round(2.40/6.00, 3); chk("Q2 S", S, 0.400, 1e-9); chk("Q2 R", round(1/S, 1), 2.5, 1e-9)

# Q3
d = round(np.mean([0.36, 0.35, 0.37]), 2); chk("Q3 d", d, 0.36, 1e-9)
K = math.pi*2.5*d**2/200; chk("Q3 K", K, 5.09e-3, 0.005e-3)
rho = 2.5*math.pi*(d*1e-3)**2/(4*0.5); chk("Q3 rho = K*1e-4", rho, K*1e-4, 1e-12)
print("ALL OK" if ok else "FAILURES")
