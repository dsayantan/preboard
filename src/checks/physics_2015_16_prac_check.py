"""Check the sample readings and results in physics_2015_16_prac.py (Heritage pre-board 2015-16, Paper 2)."""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, ".."), os.path.join(HERE, "..", "figs"), os.path.join(HERE, "..", "data")]
import physics_2015_16_figs as F
import physics_2015_16_prac as P
ok = []
def chk(name, cond):
    assert cond, name; ok.append(name)

# Q1: v readings consistent with a 15.0 cm lens within ~0.5 cm, recorded to 0.1 cm
for u, v in zip(F.P1_U, F.P1_V):
    vt = u * F.P1_F_TRUE / (u - F.P1_F_TRUE)
    chk(f"Q1 v({u}) realistic", abs(v - vt) <= 0.5 and abs(v * 10 - round(v * 10)) < 1e-9)
for u, v, x, y in zip(F.P1_U, F.P1_V, F.P1_X, F.P1_Y):
    chk(f"Q1 x,y({u})", x == round(u - F.P1_F_APPROX, 1) and y == round(100 / (v - F.P1_F_APPROX), 1))
# independent least-squares fit (numpy) and slope triangle
import numpy as np
m, c = np.polyfit(F.P1_X, F.P1_Y, 1)
chk("Q1 slope matches fit", abs(m - F.P1_M) < 1e-9)
chk("Q1 printed slope 3 s.f.", P.P1_SLOPE == 0.451)
chk("Q1 f = 10/sqrt(m)", round(10 / math.sqrt(P.P1_SLOPE), 1) == 14.9)
chk("Q1 f close to lens used", abs(10 / math.sqrt(P.P1_SLOPE) - F.P1_F_TRUE) < 0.3)
chk("Q1 slope points not data points", F.P1_XA not in F.P1_X and F.P1_XB not in F.P1_X)
chk("Q1 slope triangle > half the line", (F.P1_XB - F.P1_XA) > 0.5 * (max(F.P1_X) - min(F.P1_X)))
# Q2: meter readings on least counts and in range; consistent with the modelled circuit
for V, I in zip(F.P2_V, F.P2_I):
    chk(f"Q2 V {V} on LC 0.05", abs(V / 0.05 - round(V / 0.05)) < 1e-9 and 0 < V <= 3)
    chk(f"Q2 I {I} on LC 0.02", abs(I / 0.02 - round(I / 0.02)) < 1e-9 and 0 < I <= 1)
for R, V, I in zip(F.P2_R, F.P2_V, F.P2_I):
    It = 4 / (R + 100 * 0.039 + 0.25); Vt = It * 80 * 0.039
    chk(f"Q2 R={R} realistic", abs(I - It) <= 0.02 and abs(V - Vt) <= 0.05)
rs = [round(v / i, 2) for v, i in zip(F.P2_V, F.P2_I)]
chk("Q2 r values", rs == [3.08, 3.11, 3.12, 3.10, 3.07] or rs == [3.08, 3.11, 3.13, 3.10, 3.07])
chk("Q2 r0", P.R0 == round(sum(float(x) for x in P._r3) / 5, 2) and abs(P.R0 - 3.10) < 0.005)
chk("Q2 d", abs(P.D - 0.040) < 1e-12)
rho = math.pi * 0.040 ** 2 * 3.10 / 320
chk("Q2 rho", abs(P.RHO - rho) < 1e-12 and abs(rho - 4.87e-5) < 0.01e-5)
chk("Q2 formula 320 = 4 x 80", 4 * 80 == 320)
print(f"{len(ok)} checks passed;", "r =", P._r3, "r0 =", P.R0, "rho =", f"{P.RHO:.3e}")
