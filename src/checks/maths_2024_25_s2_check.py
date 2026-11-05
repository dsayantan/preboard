"""Recompute every answer in data/maths_2024_25_s2.py.   python3 src/checks/maths_2024_25_s2_check.py"""
from sympy import *
from fractions import Fraction as Fr
from itertools import combinations, product
x, y, z, a, m, k, t, r, h, V = symbols('x y z a m k t r h V', positive=True)
X = symbols('X', real=True)
ok = 0


def chk(name, cond):
    global ok
    assert cond, name
    ok += 1
    print("ok", name)


def num0(e, pts, var):
    return all(abs(N(e.subs(var, v))) < 1e-9 for v in pts)


# 1(i) perpendicular lines: model lines by slopes/directions (2D direction vectors)
dirs = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (-1, 2)]
perp = lambda u, v: u[0] * v[0] + u[1] * v[1] == 0
refl = all(perp(u, u) for u in dirs)
sym = all(perp(v, u) for u in dirs for v in dirs if perp(u, v))
tra = all(perp(u, w) for u in dirs for v in dirs for w in dirs if perp(u, v) and perp(v, w))
chk("1i symmetric only", (refl, sym, tra) == (False, True, False))
# 1(ii)
P = Matrix([[-1, 1], [3, 2]])
Qm = Matrix([[7, -8], [3, 0]]).T - P
chk("1ii", Qm == Matrix([[8, 2], [-11, -2]]))
# 1(iii)
chk("1iii", simplify(cot(pi / 2 + atan(1 / sqrt(2))) + 1 / sqrt(2)) == 0)
# 1(iv) brute force
tot = fav = 0
for c in combinations(range(1, 19), 5):
    tot += 1
    fav += (c[1] == 7 and c[3] == 11)
chk("1iv", Fr(fav, tot) == Fr(1, 68) and fav == 126 and tot == 8568)
# 1(vi)
chk("1vi", solve_univariate_inequality(diff(X**3 - 12 * X, X) > 0, X, relational=False) == Union(Interval.open(-oo, -2), Interval.open(2, oo)))
# 1(vii)
chk("1vii", simplify(integrate(1 / (1 + X**2), (X, 1, sqrt(3))) - pi / 12) == 0)
# 1(viii) numeric derivative at 3
yy = lambda u: abs(u - 1) + abs(u - 4)
chk("1viii", abs((yy(3 + 1e-6) - yy(3 - 1e-6)) / 2e-6) < 1e-6)
# 1(ix): 5x on N not onto (1 has no preimage)
chk("1ix", all(5 * n != 1 for n in range(1, 100)))
# 1(x)
A = Matrix([[-3, 2], [-5, 4]]); B = Matrix([[4, -2], [5, -3]])
chk("1x AB=BA", A * B == B * A == Matrix([[-2, 0], [0, -2]]))
chk("1x A^100 B = B A^100", A**100 * B == B * A**100)
# 1(xi) a p^2 + b/p = c  -> a p^3 - c p + b = 0, degree 3
p_, a_, b_, c_ = symbols('p a b c')
chk("1xi", Poly(expand((a_ * p_**2 + b_ / p_ - c_) * p_), p_).degree() == 3)
# 1(xii) random 3x3 with det 3
M = Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
M = M * diag(1, 1, Rational(3, M.det()))
chk("1xii det 3", M.det() == 3)
C = M.cofactor_matrix()
chk("1xii", (C**2).det() == 81)
# 1(xiii)
chk("1xiii", simplify(diff(log(X) + 1 / X, X) - (X - 1) / X**2) == 0)
# 1(xiv)
chk("1xiv", integrate(Abs(X + 3), (X, 0, 6)) == 36)
# 1(xv)
chk("1xv", abs(1 - 0.6 * 0.7 * 0.8 * 0.9 - 0.6976) < 1e-12)
# 2
chk("2", abs(N(5 * atan(1) + 3 * acot(1) - 2 * pi)) < 1e-12)
# 3
p, q, rr = symbols('p q r')
D = Matrix([[q * rr, rr * p, p * q], [5, 5, 5], [p * (q + rr), q * (rr + p), rr * (p + q)]])
chk("3", expand(D.det()) == 0)
# 3 OR
kk = symbols('kk')
chk("3OR", solve(Eq(Matrix([[0, kk], [-6, 0]]).T, -Matrix([[0, kk], [-6, 0]])), kk) == {kk: 6})
# 4
f4 = lambda u: (2 * u - 7) / 4
yv = symbols('yv')
chk("4 inverse", simplify(f4((4 * yv + 7) / 2) - yv) == 0)
# 5
cur = X**2 + 2 * X - 1
xs = solve(diff(cur, X), X)
chk("5", xs == [-1] and cur.subs(X, -1) == -2)
# 5 OR
F5 = -cot(X) - csc(X)
chk("5OR", simplify(diff(F5, X) - (1 + cos(X)) / sin(X)**2) == 0)
# 6
PB = Fr(5, 13); PA = PB / 2; PAB = Fr(2, 5) * PB
chk("6", PA + PB - PAB == Fr(11, 26))
# 7
Y = (X + sqrt(a**2 + X**2))**m
expr = (a**2 + X**2) * diff(Y, X, 2) + X * diff(Y, X) - m**2 * Y
chk("7", simplify(expr / Y) == 0)
# 7 OR: kx/|x| at x<0 = -k ; continuity -> -k = 3
chk("7OR", limit(-3 * X / Abs(X), X, 0, '-') == 3)
# 8: numerical check with x,y,z satisfying the condition
import random
random.seed(1)
cnt = 0
for _ in range(200):
    B_ = random.uniform(0.2, 1.4); C_ = random.uniform(0.2, 1.4)
    A_ = pi - B_ - C_
    if not (-pi / 2 <= N(A_) <= pi / 2):
        continue
    xv, yv_, zv = N(sin(A_)), N(sin(B_)), N(sin(C_))
    val = xv**2 - yv_**2 - zv**2 + 2 * yv_ * zv * sqrt(1 - xv**2)
    assert abs(val) < 1e-9, val
    cnt += 1
chk("8 (%d random triples)" % cnt, cnt > 20)
# 9
F9 = X**2 * sin(X) + 2 * X * cos(X) - 2 * sin(X)
chk("9", simplify(diff(F9, X) - X**2 * cos(X)) == 0)
# 10
outs = list(product("HT", repeat=3))
same = Fr(sum(1 for o in outs if len(set(o)) == 1), 8)
chk("10a", same == Fr(1, 4))
chk("10b", 1 - same == Fr(3, 4))
chk("10c", same**3 * (1 - same) == Fr(3, 256))
# 10 OR (enumerate ordered draws)


def pwr(w, rd):
    gems = ["W"] * w + ["R"] * rd
    n = 0; good = 0
    for i in range(len(gems)):
        for j in range(len(gems)):
            if i != j:
                n += 1
                good += {gems[i], gems[j]} == {"W", "R"}
    return Fr(good, n)


L = [pwr(1, 2), pwr(2, 3), pwr(3, 1)]
chk("10OR likelihoods", L == [Fr(2, 3), Fr(3, 5), Fr(1, 2)])
chk("10OR", L[1] / sum(L) == Fr(18, 53))
# 11
A11 = X * (12 - 3 * X) / 2 + sqrt(3) / 4 * X**2
crit = solve(diff(A11, X), X)
chk("11 x", len(crit) == 1 and simplify(crit[0] - 4 * (6 + sqrt(3)) / 11) == 0)
chk("11 max", N(diff(A11, X, 2)) < 0)
yw = (12 - 3 * crit[0]) / 2
chk("11 y", simplify(yw - (30 - 6 * sqrt(3)) / 11) == 0)
chk("11 approx", abs(N(crit[0]) - 2.812) < 1e-3 and abs(N(yw) - 1.782) < 1e-3)
# 11 OR
S = pi * r**2 + (pi + 2) * r * 2 * V / (pi * r**2)
rc = solve(diff(S, r), r)[0]
hc = 2 * V / (pi * rc**2)
chk("11OR ratio", simplify(hc / (2 * rc) - pi / (pi + 2)) == 0)
chk("11OR min", simplify(diff(S, r, 2).subs(r, rc)) .is_positive)
# 12
A12 = Matrix([[1, 1, 1], [1, -3, 0], [0, 1, -1]])
chk("12 det", A12.det() == 5)
chk("12 adj", A12.adjugate() == Matrix([[3, 2, 3], [1, -1, 1], [1, -1, -4]]))
chk("12 sol", A12.inv() * Matrix([100, 0, 10]) == Matrix([66, 22, 12]))
# 13: implicit solution 2 e^{x/y} + log y = 2  satisfies the DE
xs_, ys_ = symbols('xs ys', positive=True)
G = 2 * exp(xs_ / ys_) + log(ys_) - 2
dxdy = -diff(G, ys_) / diff(G, xs_)   # along G = const
de = 2 * ys_ * exp(xs_ / ys_) * dxdy + (ys_ - 2 * xs_ * exp(xs_ / ys_))
chk("13 DE", simplify(de) == 0)
chk("13 IC", G.subs({xs_: 0, ys_: 1}) == 0)
# 13 OR
I13 = Integral(cos(X)**2 / (1 + sin(X) * cos(X)), (X, 0, pi / 2))
chk("13OR", abs(N(I13) - N(pi / (3 * sqrt(3)))) < 1e-10)
# 14
sc = [abs(c1 - c2) for c1 in range(1, 5) for c2 in range(1, 5)]
chk("14 p,q", abs(2 - 1) == 1 and abs(1 - 3) == 2)
dist = {s: Fr(sc.count(s), 16) for s in range(4)}
chk("14 dist", dist == {0: Fr(1, 4), 1: Fr(3, 8), 2: Fr(1, 4), 3: Fr(1, 8)})
chk("14 iii", dist[0] + dist[1] + dist[2] == Fr(7, 8))
chk("14 iv", sum(s * pr for s, pr in dist.items()) == Fr(5, 4))
# 15(i)
av, bv = Matrix([3, 1, 0]), Matrix([1, 2, 0])     # sides p, q -> diagonals a=p+q, b=p-q
chk("15i", ((av + bv) + (av - bv)) / 2 == av)     # half-sum recovers the side (not double)
# 15(ii)
al = [0.3, 1.1]
l_, m_ = cos(al[0]), cos(al[1]); n_ = sqrt(1 - l_**2 - m_**2)
chk("15ii", abs(N((1 - l_**2) + (1 - m_**2) + (1 - n_**2)) - 2) < 1e-12)
# 15(iii)
a15 = Matrix([2, 1, 2]); b15 = Matrix([5, -3, 1])
chk("15iii", a15.dot(b15) / a15.norm() == 3)
# 15(iv)
n = Matrix([3, 0, 4]); d0 = -n.dot(Matrix([1, 1, 1]))
chk("15iv", Abs(d0) / n.norm() == Rational(7, 5))
# 15(v)
bb = symbols('bb', positive=True)
chk("15v", solve(3 - 2 * bb**2 + 5, bb) == [2])
# 16 OR
chk("16OR", solve_univariate_inequality(2 * X**2 - 6 * X + X**2 < 0, X, relational=False) == Interval.open(0, 2))
chk("16OR not antiparallel", all(v <= 0 for v in solve(2 * X**2 + Rational(3, 2) * X, X)))
# 17
d = Matrix([-2, 3, -1]); A17 = Matrix([0, 1, 1]); P17 = Matrix([-1, 0, 2])
n17 = d.cross(P17 - A17)
chk("17 normal", n17 == Matrix([2, 3, 5]))
chk("17 plane", n17.dot(A17) == 8 and n17.dot(P17) == 8 and n17.dot(A17 + 5 * d) == 8)
# 17 OR
Aa, Bb, Cc, Pp = Matrix([1, 0, 2]), Matrix([3, -1, 1]), Matrix([1, 2, 1]), Matrix([2, 3, 1])
nn = (Bb - Aa).cross(Cc - Aa)
chk("17OR normal", nn == Matrix([3, 2, 4]) and nn.dot(Aa) == nn.dot(Bb) == nn.dot(Cc) == 11)
foot = Pp - (nn.dot(Pp) - 11) / nn.dot(nn) * nn
chk("17OR foot", foot == Matrix([Rational(43, 29), Rational(77, 29), Rational(9, 29)]))
chk("17OR height", simplify((Pp - foot).norm() - 5 / sqrt(29)) == 0)
# 18
area = integrate(sqrt(X / a) - a * X**2, (X, 0, 1 / a))
chk("18 area", simplify(area - 1 / (3 * a**2)) == 0)
chk("18", solve(Eq(area, 27), a) == [Rational(1, 9)])
# 19(ii)
C19 = Rational(1, 10000) * X**3 - Rational(1, 100) * X**2 - 20 * X + 3500
mc200 = diff(C19, X).subs(X, 200)
chk("19ii MC(200)=-12", mc200 == -12)
chk("19ii C(201)-C(200)", abs(N(C19.subs(X, 201) - C19.subs(X, 200)) + 11.95) < 0.001)
# 19(v)
C195 = X + 2 * X**3 - Rational(7, 2) * X**2
chk("19v", simplify(diff(C195 / X, X) - (4 * X - Rational(7, 2))) == 0)
# 20
AC = X + 5 + 36 / X
chk("20a", expand(X * AC) == X**2 + 5 * X + 36)
chk("20b", solve_univariate_inequality(diff(AC, X) > 0, X, relational=False).intersect(Interval.open(0, oo)) == Interval.open(6, oo))
chk("20 min AC", AC.subs(X, 6) == 17)
# 20 OR
R20 = (100 * X - X**2) / 4
chk("20OR", solve(diff(R20, X), X) == [50])
# 22
verts = [(0, 0), (10, 0), (8, 2), (0, 6)]
for (u, v) in verts:
    assert u + 2 * v <= 12 and u + v <= 10
best = max(verts, key=lambda pt: 3000 * pt[0] + 4000 * pt[1])
chk("22", best == (8, 2) and 3000 * 8 + 4000 * 2 == 32000)
from scipy.optimize import linprog
res = linprog([-3000, -4000], A_ub=[[1, 2], [1, 1]], b_ub=[12, 10], bounds=[(0, None)] * 2)
chk("22 linprog", abs(-res.fun - 32000) < 1e-6 and abs(res.x[0] - 8) < 1e-6)

# Review: section totals justify the inferred marks on Q18, Q21, Q22 (none printed)
import sys as _sys, os as _os
_sys.path[:0] = [_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", d) for d in ("", "data", "figs")]
from maths_2024_25_s2 import PAPER as _P
_sec, _tot = None, {}
for _it in _P["items"]:
    if _it["kind"] == "sec":
        _sec = _it["title"].split()[1]
        continue
    if "(OR)" in _it["num"]:
        continue
    _tot[_sec] = _tot.get(_sec, 0) + _it["marks"]
chk("section totals A65 B15 C15", _tot == {"A": 65, "B": 15, "C": 15})
chk("paper total 80 (A + B or A + C)", _tot["A"] + _tot["B"] == 80 == _tot["A"] + _tot["C"])

print(f"\nALL {ok} CHECKS PASSED")
