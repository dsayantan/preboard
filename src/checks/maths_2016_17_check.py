"""Recompute every answer in data/maths_2016_17.py with sympy.  python3 src/checks/maths_2016_17_check.py"""
from sympy import *
from fractions import Fraction as F
from math import comb
x, y, a, b, c, m, r, t, lam = symbols('x y a b c m r t lambda', real=True)
ok = 0
def chk(name, cond):
    global ok
    assert cond, name
    ok += 1; print("ok", name)

# 1(a)
A = Matrix([[3, -4], [1, -1]])
P = (A + A.T) / 2; Qm = (A - A.T) / 2
chk("1a sym", P == Matrix([[3, Rational(-3, 2)], [Rational(-3, 2), -1]]) and P == P.T)
chk("1a skew", Qm == Matrix([[0, Rational(-5, 2)], [Rational(5, 2), 0]]) and Qm == -Qm.T and P + Qm == A)
# 1(b)
s = asin(Rational(4, 5)) + acos(2 / sqrt(5))
chk("1b", abs(N(s - acot(Rational(2, 11)))) < 1e-12 and (Rational(4,3)+Rational(1,2))/(1-Rational(4,3)*Rational(1,2)) == Rational(11, 2) and N(s) < N(pi/2))
# 1(e)
I = -x * cot(x / 2)
for v in (0.4, 1.3, 2.5, -1.1):
    chk(f"1e at {v}", abs(N((diff(I, x) - (x - sin(x)) / (1 - cos(x))).subs(x, v))) < 1e-12)
# 1(f)
chk("1f", abs(N(Integral(1 / (1 + tan(x)), (x, 0, pi / 2))) - N(pi / 4)) < 1e-10)
# 1(i)
chk("1i", F(comb(36, 2), comb(52, 2)) == F(105, 221) and 52 - 13 - 3 == 36)
# 1(j): sin y + sin x - sin^3 x /3 = C  => implicit derivative satisfies sec^3x dy + sec y dx = 0
G = sin(y) + sin(x) - sin(x)**3 / 3
dydx = -diff(G, x) / diff(G, y)
chk("1j", simplify(dydx - (-cos(x)**3 / cos(y))) == 0)
# 2(a)
D = Matrix([[a - b - c, 2*a, 2*a], [2*b, b - c - a, 2*b], [2*c, 2*c, c - a - b]])
chk("2a", expand(D.det() - (a + b + c)**3) == 0)
# check the intermediate matrix after R1->R1+R2+R3, taking (a+b+c) out, C2->C2-C1, C3->C3-C1
S = a + b + c
M2 = Matrix([[1, 0, 0], [2*b, -S, 0], [2*c, 0, -S]])
chk("2a steps", expand(S * M2.det() - D.det()) == 0)
# 2(b)
A = Matrix([[5, 3, 1], [2, 1, 3], [1, 2, 4]])
chk("2b det", A.det() == -22)
chk("2b adj", A.adjugate() == Matrix([[-2, -10, 8], [-5, 19, -13], [3, -7, -1]]))
X = A.inv() * Matrix([16, 19, 25])
chk("2b sol", list(X) == [1, 2, 5])
# 3(b): only x = 2
f = lambda v: asin(v / sqrt(1 + v**2)) - asin(1 / sqrt(1 + v**2)) - asin((1 + v) / (1 + v**2))
chk("3b x=2", abs(N(f(2))) < 1e-12)
chk("3b x=-1 rejected", abs(N(f(-1))) > 1)
# scan for other roots on domain x<=0 or x>=1
import numpy as np
vals = [float(N(f(v))) for v in np.linspace(-20, 0, 401)] + []
chk("3b no root x<=0", min(abs(v) for v in vals) > 0.5)
vals = [(v, float(N(f(v)))) for v in np.linspace(1, 30, 2901)]
roots = [v for (v, w), (v2, w2) in zip(vals, vals[1:]) if w * w2 <= 0]
chk("3b single root x>=1", len(roots) == 1 and abs(roots[0] - 2) < 0.02)
# 5(a)
Y = (x + sqrt(x**2 - 1))**m
E5 = (x**2 - 1) * diff(Y, x, 2) + x * diff(Y, x) - m**2 * Y
for xv, mv in ((1.5, 2), (3.2, 0.7), (2.0, -1.3)):
    chk(f"5a at x={xv},m={mv}", abs(N(E5.subs({x: xv, m: mv}))) < 1e-9)
# 5(b)
V = pi * r**2 * (10 - 2 * pi * r)
rs = [s_ for s_ in solve(diff(V, r), r) if s_ != 0][0]
chk("5b r", simplify(rs - 10 / (3 * pi)) == 0 and diff(V, r, 2).subs(r, rs) < 0)
chk("5b h", simplify(10 - 2 * pi * rs - Rational(10, 3)) == 0)
chk("5b V", simplify(V.subs(r, rs) - 1000 / (27 * pi)) == 0)
# 6(a)
Fx = sqrt(2) * asin(sin(x) - cos(x))
for v in (0.3, 0.7, 1.2):
    d = N(diff(Fx, x).subs(x, v)); g = N((sqrt(tan(x)) + sqrt(cot(x))).subs(x, v))
    chk(f"6a at {v}", abs(d - g) < 1e-10)
# 6(b): main reading y^2 = 2x - x^2 ; alternative y = 2x - x^2
A1 = integrate(sqrt(2*x - x**2) - x, (x, 0, 1))
chk("6b circle", simplify(A1 - (pi / 4 - Rational(1, 2))) == 0)
chk("6b quarter", simplify(integrate(sqrt(2*x - x**2), (x, 0, 1)) - pi / 4) == 0)
chk("6b parabola alt", integrate(2*x - x**2 - x, (x, 0, 1)) == Rational(1, 6))
chk("6b intersections", set(solve([x**2 + y**2 - 2*x, y - x], [x, y])) == {(0, 0), (1, 1)})
# 8(a)
n = comb(52, 2)
chk("8a(i)", F(comb(26, 2) + comb(4, 2) - 1, n) == F(55, 221))
chk("8a(ii)", F(2 * 13, n) == F(1, 51))
# 8(b)
tr = {(2, 0): F(comb(4, 2), 21), (1, 1): F(12, 21), (0, 2): F(comb(3, 2), 21)}
p = sum(pr * F((2 + w) * (2 + bk), comb(6, 2)) for (w, bk), pr in tr.items())
chk("8b", p == F(4, 7) and sum(tr.values()) == 1)
# 9(b)
Y = sqrt(2 * x - x**2)
chk("9b", simplify((x**2 - Y**2) + 2 * x * Y * diff(Y, x)) == 0 and Y.subs(x, 1) == 1)
# 11(a)
a1, b1 = Matrix([3, 8, 3]), Matrix([3, -1, 1]); a2, b2 = Matrix([-3, -7, 6]), Matrix([3, -2, -4])
nn = b1.cross(b2)
chk("11a cross", nn == Matrix([6, 15, -3]))
d = abs((a2 - a1).dot(nn)) / nn.norm()
chk("11a", simplify(d - 3 * sqrt(30)) == 0 and (a2 - a1).dot(nn) == -270 and a2 - a1 == Matrix([-6, -15, 3]))
# 11(b)
lv = Rational(9, 2)
nrm = Matrix([4, -1, 1]) + lv * Matrix([3, 1, -1])
chk("11b perp", nrm.dot(Matrix([1, -2, 3])) == 0)
chk("11b eq", 2 * nrm == Matrix([35, 7, -7]))
# plane contains intersection line: point on both planes satisfies 35x+7y-7z=45
sol = solve([4*x - y + symbols('z'), 3*x + y - symbols('z') - 5], [x, y], dict=True)[0]
z = symbols('z')
chk("11b contains line", simplify(35 * sol[x] + 7 * sol[y] - 7 * z - 45) == 0)
# 12(a)
pI, pII, pIII = F(1 * 3, comb(6, 2)), F(2 * 1, comb(4, 2)), F(4 * 3, comb(12, 2))
chk("12a likelihoods", (pI, pII, pIII) == (F(1, 5), F(1, 3), F(2, 11)))
chk("12a", pII / (pI + pII + pIII) == F(55, 118))
# 12(b)
dist = [F(comb(3, k)) * F(1, 4)**k * F(3, 4)**(3 - k) for k in range(4)]
chk("12b dist", dist == [F(27, 64), F(27, 64), F(9, 64), F(1, 64)])
mu = sum(k * pk for k, pk in enumerate(dist)); var = sum(k * k * pk for k, pk in enumerate(dist)) - mu**2
chk("12b mean var", mu == F(3, 4) and var == F(9, 16) and sum(k*k*pk for k, pk in enumerate(dist)) == F(18, 16))
# 13(b) LPP: 2x+y>=1000, x+2y>=800, Z = 0.005x + 0.02y (Rs, x,y in grams)
X0 = solve([2*x + y - 1000, x + 2*y - 800], [x, y])
chk("13b B", X0 == {x: 400, y: 200})
Z = lambda u, v: Rational(5, 1000) * u + Rational(20, 1000) * v
corners = {(0, 1000): Z(0, 1000), (400, 200): Z(400, 200), (800, 0): Z(800, 0)}
chk("13b Z", corners == {(0, 1000): 20, (400, 200): 6, (800, 0): 4})
# the open half-plane Z < 4 does not meet the region: 0.005x+0.02y<4 ⇒ x+4y<800 ⇒ with x+2y>=800 needs y<0
chk("13b min", all(Z(u, v) >= 4 for u in range(0, 1601, 10) for v in range(0, 1601, 10)
                   if 2*u + v >= 1000 and u + 2*v >= 800))
# 13(b) note: with wheat Rs 4/kg, rice Rs 6/kg the optimum is the mixed corner B at Rs 2.80
Zt = lambda u, v: Rational(4, 1000) * u + Rational(6, 1000) * v
chk("13b textbook prices", (Zt(0, 1000), Zt(400, 200), Zt(800, 0)) == (6, Rational(14, 5), Rational(16, 5)))
chk("13b textbook min", all(Zt(u, v) >= Rational(14, 5) for u in range(0, 1601, 10) for v in range(0, 1601, 10)
                   if 2*u + v >= 1000 and u + 2*v >= 800))
# 3(b) domain: RHS defined only for x<=0 or x>=1; x=2 inside
chk("3b domain", solve_univariate_inequality(Abs((1 + x) / (1 + x**2)) <= 1, x, relational=False) == Union(Interval(-oo, 0), Interval(1, oo)))
print(ok, "checks passed")

# 14(b) restored (calculus application): MC and marginal average cost identity
import sympy as _s
_x = _s.symbols('x', positive=True)
_AC = _x**2/3 + 3*_x - 7 + 16/_x
_C = _s.expand(_x*_AC)
_MC = _s.diff(_C, _x)
assert _s.simplify(_MC - (_x**2 + 6*_x - 7)) == 0
assert _s.simplify(_s.diff(_AC, _x) - (_x*_MC - _C)/_x**2) == 0
print("14(b) MC and MAC identity: ok")
