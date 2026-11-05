"""Sample readings for physics_2025_26_prac: generated from plausible apparatus, rounded to the least count,
then every derived column, slope and result recomputed."""
import math
ok = True
def chk(name, got, want, tol):
    global ok
    good = abs(got - want) <= tol
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: computed {got:.6g}, printed {want:.6g}")

# ---------------- Q1: convex lens f_true = 15.0 cm, v read to 0.1 cm with ~0.3 cm parallax scatter
U = [20, 25, 30, 35, 40, 45]
V = [60.4, 37.3, 30.2, 26.1, 24.1, 22.4]          # printed readings
for u, v in zip(U, V):
    vt = u*15/(u - 15)
    print(f"u={u} v_true={vt:.2f} printed={v} diff={v - vt:+.2f}")
    ok &= abs(v - vt) < 0.6
X = [round(u*v, 2) for u, v in zip(U, V)]
Y = [round(u + v, 2) for u, v in zip(U, V)]
PX = [1208.00, 932.50, 906.00, 913.50, 964.00, 1008.00]
PY = [80.40, 62.30, 60.20, 61.10, 64.10, 67.40]
for i in range(6):
    chk(f"x{i+1}", X[i], PX[i], 0.005); chk(f"y{i+1}", Y[i], PY[i], 0.005)
n = 6; mx = sum(X)/n; my = sum(Y)/n
S_ls = sum((x - mx)*(y - my) for x, y in zip(X, Y))/sum((x - mx)**2 for x in X)
c_ls = my - S_ls*mx
print(f"least-squares slope {S_ls:.5f}, intercept {c_ls:.3f}")
# best-fit line drawn on the graph: through the mean point with the LS slope (rounded line used in the figure)
LINE_S, LINE_C = 0.06620, 0.47     # the line drawn in fig_p1_graph:  y = LINE_S x + LINE_C
chk("drawn line close to LS slope", LINE_S, S_ls, 0.0006)
P1 = (920.0, round(LINE_S*920 + LINE_C, 2)); P2 = (1200.0, round(LINE_S*1200 + LINE_C, 2))
print("slope-triangle points", P1, P2)
chk("P1 y", P1[1], 61.37, 0.005); chk("P2 y", P2[1], 79.91, 0.005)
chk("line through mean point", LINE_S*mx + LINE_C, my, 0.02)
S = (P2[1] - P1[1])/(P2[0] - P1[0]); chk("S", round(S, 5), 0.0662, 0.00005)
chk("S 3 s.f.", float(f"{S:.3g}"), 0.0662, 1e-9)
F = 1/0.0662; chk("F cm (1 dp)", round(F, 1), 15.1, 1e-9)
chk("F vs true lens", F, 15.0, 0.3)
# lens position: object at 0.0 cm, u = 20 cm -> lens at 20.0 cm; image pin at 20 + v
for u, v in zip(U, V):
    ok &= u + v <= 100; 
print("all image-pin positions on the 100 cm bench:", [round(u + v, 1) for u, v in zip(U, V)])

# ---------------- Q2: 100 cm wire, 0.04 ohm/cm -> R_AB = 4.0 ohm; AC = 80 cm -> r = 3.2 ohm
E, rint, RAB, r_true = 3.0, 0.2, 4.0, 3.2
LCV, LCI = 0.05, 0.02
def rnd(x, lc): return round(round(x/lc)*lc, 2)
PV = [1.85, 1.55, 1.35, 1.15, 1.05, 0.95]
PI = [0.58, 0.48, 0.42, 0.36, 0.32, 0.30]
PR = [3.2, 3.2, 3.2, 3.2, 3.3, 3.2]
rs = []
for k, R in enumerate(range(1, 7)):
    I = E/(R + RAB + rint); V = I*r_true
    Ir, Vr = rnd(I, LCI), rnd(V, LCV)
    chk(f"R={R} I", Ir, PI[k], 1e-9); chk(f"R={R} V", Vr, PV[k], 1e-9)
    ok &= Vr <= 3 and Ir <= 1
    ok &= abs(Vr/LCV - round(Vr/LCV)) < 1e-6 and abs(Ir/LCI - round(Ir/LCI)) < 1e-6
    r = Vr/Ir; rs.append(r)
    print(f"   r = {Vr}/{Ir} = {r:.3f}")
    chk(f"R={R} r (1 dp)", round(r, 1), PR[k], 1e-9)
r0 = sum(PR)/6; chk("r0 mean of printed r", round(r0, 2), 3.22, 1e-9)
chk("r0 (1 dp)", round(r0, 1), 3.2, 1e-9)
chk("r per cm", 3.2/80, 0.04, 1e-9)
print("ALL OK" if ok else "FAILURES")
