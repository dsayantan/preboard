"""Recompute every answer in data/maths_2025_26.py.   python3 src/checks/maths_2025_26_check.py"""
from sympy import *
from fractions import Fraction as Fr
from scipy.optimize import linprog
import itertools
x, y, t, r, p, a, m = symbols('x y t r p a m', real=True)
ok = 0
def chk(name, cond):
    global ok
    assert cond, name
    ok += 1; print("ok", name)
def num0(e, pts, var=x):
    return all(abs(N(e.subs(var, v))) < 1e-9 for v in pts)

# 1(i)
R = lambda a_, b_: a_ - b_ == 2
chk("1i", [R(2,4), R(10,8), R(6,8), R(8,7)] == [False, True, False, False])
# 1(ii)
A = diag(a, a, a); n = 5
chk("1ii", A**n == diag(a**n, a**n, a**n))
# 1(iii)  d/dx (y')^3 = 3 y'^2 y'' = 0 -> order 2 degree 1
f = Function('f')
e = diff(diff(f(x), x)**3, x)
chk("1iii", e == 3*diff(f(x), x)**2*diff(f(x), x, 2))  # highest y'' appears to power 1, order 2 -> m-n=1
# 1(iv)
chk("1iv", simplify(idiff(x**2 + y**3 - 42, y, x) - (-2*x/(3*y**2))) == 0)
# 1(v) skew 3x3 det 0
s1, s2, s3 = symbols('s1 s2 s3')
S = Matrix([[0, s1, s2], [-s1, 0, s3], [-s2, -s3, 0]])
chk("1v", S.det() == 0)
# 1(vi)
pp = solve(Rational(2, 5) + p - Rational(2, 5)*p - Rational(4, 5), p)
chk("1vi", pp == [Rational(2, 3)])
# 1(vii)
chk("1vii", num0(cos(atan(x)) - 1/sqrt(1 + x**2), [-3, -0.4, 0.2, 5]))
# 1(viii)
q, yy = symbols('q yy')
D = Matrix([[p, p, p], [p, p + x, p], [p, p, p + yy]]).det()
chk("1viii", expand(D - p*x*yy) == 0)
# 1(ix)
F_ = exp(x)/(1 - x)
chk("1ix", simplify(diff(F_, x) - (2 - x)/(x - 1)**2*exp(x)) == 0)
# 1(xi)
chk("1xi", solve_univariate_inequality(diff(7 + x - exp(x), x) > 0, x) == (x < 0))
# 1(xii) R={(b,b)} on {a,b,c}
Rel = {('b', 'b')}; Sset = ['a', 'b', 'c']
refl = all((u, u) in Rel for u in Sset)
sym = all((v, u) in Rel for (u, v) in Rel)
tra = all((u, w) in Rel for (u, v) in Rel for (v2, w) in Rel if v == v2)
chk("1xii", (refl, sym, tra) == (False, True, True))
# 1(xiii)
chk("1xiii", abs(N(acos(sin(10*pi/7)) - 13*pi/14)) < 1e-12)
# 1(xiv): [x]-x = 0 exactly at integers
chk("1xiv", all(floor(k) - k == 0 for k in range(-5, 6)) and all(floor(Rational(k, 3)) - Rational(k, 3) != 0 for k in (1, 2, 4, 5, -1)))
# 1(xv)
chk("1xv", 1 - Fr(2, 3)*Fr(3, 5)*Fr(1, 3) == Fr(13, 15))
# 2
g = y*log(x) - x*log(y)
d2 = idiff(g, y, x)
claim = y*(x*log(y) - y)/(x*(y*log(x) - x))
chk("2", simplify(d2 - claim) == 0)
# 2 OR: 1-... f' = -a + cos x >= 0 for all x iff a <= -1
chk("2or", all((-av + cos(v)) >= 0 for av in (-1, -2) for v in [k*0.1 for k in range(-70, 70)]) and N(-(-0.9) + cos(pi)) < 0)
# 3
chk("3", sorted(solve(-x**2 - (2*x - 15), x)) == [-5, 3])
# 4
s4 = atan(Rational(6, 10)) + atan(Rational(8, 10))
chk("4", abs(N(s4 - atan(Rational(35, 13)))) < 1e-12 and Rational(6, 10)*Rational(8, 10) < 1)
# 5: intended  sqrt x/(sqrt(5-x)+sqrt x)
I5 = Integral(sqrt(x)/(sqrt(5 - x) + sqrt(x)), (x, 0, 5)).evalf()
chk("5", abs(I5 - 2.5) < 1e-9)
# printed version has a zero of the denominator at x = 5/2 (non-integrable)
den = sqrt(5 - x) - sqrt(x)
chk("5 printed singular", den.subs(x, Rational(5, 2)) == 0 and diff(den, x).subs(x, Rational(5, 2)) != 0)
# 5 OR
chk("5or", simplify(diff(exp(x)/sin(x), x) - exp(x)/sin(x)*(1 - cot(x))) == 0)
# 6
yc = 4*x**2 - 2*x**3
chk("6", diff(yc, x).subs(x, 0) == 0 and yc.subs(x, 0) == 0)
# 7: holds for 0 < x <= 1, gives -x for -1 <= x < 0
L7 = lambda v: N(cos(atan(cot(asin(v)))))
chk("7", all(abs(L7(v) - v) < 1e-12 for v in (0.1, 0.5, 0.9, 1)) and abs(L7(-0.5) - 0.5) < 1e-12)
# 8
Y = (x + sqrt(a**2 + x**2))**m
chk("8", num0(((a**2 + x**2)*diff(Y, x, 2) + x*diff(Y, x) - m**2*Y).subs({a: 2, m: Rational(7, 3)}), [0.3, 1.7, -0.8]))
chk("8 y1", num0((diff(Y, x)*sqrt(a**2 + x**2) - m*Y).subs({a: 3, m: 2}), [0.5, 2]))
# 8 OR
P = 10 + 20*r - 10*r**2
chk("8or", P.subs(r, 0) == 10 and diff(P, r) == 20 - 20*r and solve(diff(P, r), r) == [1] and diff(P, r, 2) < 0 and P.subs(r, 1) == 20)
# 9
F9 = -acos(x)/x + log((1 + sqrt(1 - x**2))/Abs(x))
chk("9", num0(diff(F9, x) - acos(x)/x**2, [0.2, 0.5, 0.9, -0.3, -0.7]))
# 10
PE = Fr(40, 100)*Fr(20, 100) + Fr(35, 100)*Fr(30, 100) + Fr(25, 100)*Fr(50, 100)
chk("10", PE == Fr(31, 100) and Fr(25, 100)*Fr(50, 100)/PE == Fr(25, 62))
# 10 OR
pa = [Fr(1, 2), Fr(1, 3), Fr(1, 4)]
ex2 = sum((pa[i]*pa[j]*(1 - pa[k])) for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)))
chk("10or", ex2 == Fr(1, 4) and 1 - (1 - pa[0])*(1 - pa[1])*(1 - pa[2]) == Fr(3, 4))
# 11
M = Matrix([[2, 3, 4], [1, 1, 2], [3, 2, 1]]); B = Matrix([29, 13, 16])
chk("11 det", M.det() == 5)
chk("11 adj", M.adjugate() == Matrix([[-3, 5, 2], [5, -10, 0], [-1, 5, -1]]))
chk("11", M.inv()*B == Matrix([2, 3, 4]))
# 12
pi_ = Rational(22, 7)
h = Rational(539, 2)/(pi_*r**2)
S12 = 2*pi_*r**2 + 2*pi_*r*h
chk("12 S", simplify(S12 - (2*pi_*r**2 + 539/r)) == 0)
chk("12 r", solve(diff(S12, r), r) == [Rational(7, 2)] and diff(S12, r, 2).subs(r, Rational(7, 2)) > 0)
chk("12 h", h.subs(r, Rational(7, 2)) == 7)
# 12 OR
H = Rational(1, 2)*(-7*t**2 + 3*t + 2)
chk("12or b", diff(H, t).subs(t, Rational(1, 14)) == 1)
chk("12or d", solve(diff(H, t), t) == [Rational(3, 14)] and H.subs(t, Rational(3, 14)) == Rational(65, 56))
# 13
ps = [Fr(9, 10), Fr(8, 10), Fr(7, 10)]
dist = {k: Fr(0) for k in range(4)}
for bits in itertools.product((0, 1), repeat=3):
    pr = Fr(1)
    for b_, q_ in zip(bits, ps):
        pr *= q_ if b_ else 1 - q_
    dist[sum(bits)] += pr
chk("13", [dist[k] for k in range(4)] == [Fr(6, 1000), Fr(92, 1000), Fr(398, 1000), Fr(504, 1000)])
chk("13 mean", sum(k*v for k, v in dist.items()) == Fr(24, 10))
# 14: x y cos(y/x) = -pi
Fimp = x*y*cos(y/x)
dydx = -diff(Fimp, x)/diff(Fimp, y)
# DE: (x dy - y dx) y sin(y/x) = (y dx + x dy) x cos(y/x)  ->  dy/dx = (y^2 sin + x y cos)/(x y sin - x^2 cos)
de = (y**2*sin(y/x) + x*y*cos(y/x))/(x*y*sin(y/x) - x**2*cos(y/x))
chk("14", all(abs(N((dydx - de).subs({x: xv, y: yv}))) < 1e-10 for xv, yv in ((1.2, 0.7), (2, 3.1), (0.5, -1.3))))
chk("14 pc", Fimp.subs({x: 1, y: pi}) == -pi)
# 14 OR
chk("14or simplify", num0(x*tan(x)/(1/cos(x) + cos(x)) - x*sin(x)/(1 + cos(x)**2), [0.3, 1, 2, 2.9]))
I14 = Integral(x*sin(x)/(1 + cos(x)**2), (x, 0, pi)).evalf()
chk("14or", abs(I14 - N(pi**2/4)) < 1e-9)
# 15(ii)
chk("15ii", abs(N(3*sqrt(2)/3*sin(pi/4)) - 1) < 1e-12)
# 15(iii)
d1 = Matrix([1, -3, 1]); d2v = Matrix([1, 1, 1])
c = d1.cross(d2v)
chk("15iii", c == Matrix([-4, 0, 4]) and c.norm()/2 == 2*sqrt(2))
# 15(iv)
chk("15iv", Rational(abs(3*1 + 0*1 + 4*1), 5) == Rational(7, 5))
# 15(v)
c5 = Matrix([3, 2, 4]).cross(Matrix([1, -3, 1]))
chk("15v", c5 == Matrix([14, 1, -11]) and c5.norm() == sqrt(318))
# 16
Ap, Bp, Cp, Dp = Matrix([0, 1, 2]), Matrix([3, 0, 1]), Matrix([4, 3, 6]), Matrix([2, 3, 2])
G = (Bp + Cp + Dp)/3
chk("16a", G == Matrix([3, 2, 3]) and (G - Ap).norm() == sqrt(11))
cr = (Bp - Ap).cross(Cp - Ap)
chk("16b", cr == Matrix([-2, -16, 10]) and cr.norm()/2 == 3*sqrt(10))
# 16 OR
chk("16or", solve_univariate_inequality(expand(2*x**2*1 + 3*x*(-2) + 1*x**2) < 0, x, relational=False) == Interval.open(0, 2))
# 17
P0 = Matrix([-3, 1, -4]); dd = Matrix([5, 2, 3]); A17 = Matrix([0, 2, 3])
cc = (P0 - A17).cross(dd)
dist17 = sqrt(cc.dot(cc)/dd.dot(dd))
chk("17", cc == Matrix([11, -26, -1]) and simplify(dist17 - sqrt(21)) == 0)
# foot of perpendicular, as a cross-check
lam = symbols('lam')
Pt = P0 + lam*dd
lv = solve((Pt - A17).dot(dd), lam)[0]
chk("17 foot", simplify((Pt.subs(lam, lv) - A17).norm() - sqrt(21)) == 0)
chk("17 area", Rational(1, 2)*5*sqrt(21) == 5*sqrt(21)/2)
# 17 OR
d17 = Matrix([-2, 3, -1]); Pl = Matrix([0, 1, 1]); Qp = Matrix([-1, 0, 2])
nrm = d17.cross(Qp - Pl)
chk("17or", nrm == Matrix([2, 3, 5]) and nrm.dot(Pl) == 8 and nrm.dot(Qp) == 8 and nrm.dot(d17) == 0)
# 18
a1 = integrate(x*(4 - x), (x, 0, 4)); a2 = integrate(x*(4 - x), (x, 4, 5))
chk("18", a1 == Rational(32, 3) and a2 == Rational(-7, 3) and a1 - a2 == 13)
# 22
res = linprog([-1, -1], A_ub=[[6, 4], [1, 1.5]], b_ub=[96, 21], bounds=[(0, None), (0, None)])
chk("22 lp", abs(-res.fun - 18) < 1e-9 and abs(res.x[0] - 12) < 1e-9 and abs(res.x[1] - 6) < 1e-9)
corners = {(0, 0): 0, (16, 0): 16, (12, 6): 18, (0, 14): 14}
chk("22 corners", all(6*u + 4*v <= 96 and u + 1.5*v <= 21 and u + v == z for (u, v), z in corners.items()))
# 22 OR
chk("22or lines", 2*0 + 50 == 50 and 2*25 + 0 == 50 and 0 + 2*20 == 40 and 40 + 0 == 40)
Bsol = solve([2*x + y - 50, x + 2*y - 40], [x, y])
chk("22or B", Bsol == {x: 20, y: 10})
res = linprog([-1, -1], A_ub=[[2, 1], [1, 2]], b_ub=[50, 40], bounds=[(0, None), (0, None)])
chk("22or max", abs(-res.fun - 30) < 1e-9)
# ---- Section C items restored by review
X_ = symbols('X_', positive=True)
Rv = (1500 - 2*X_ - X_**2)*X_
chk("19i MR", diff(Rv, X_).subs(X_, 10) == 1160)
chk("19iii break-even", solve(Eq(280*X_, 210*X_ + 7000), X_) == [100] and 280*99 < 210*99 + 7000)
R20 = X_*(100 - X_)/4
chk("20 MR=0", solve(diff(R20, X_), X_) == [50] and diff(R20, X_, 2) < 0)
AC = (200 + 20*X_ - X_**2/2)/X_
dAC = simplify(diff(AC, X_))
chk("20or AC falls", simplify(dAC - (-Rational(1, 2) - 200/X_**2)) == 0 and all(dAC.subs(X_, v) < 0 for v in (0.1, 1, 10, 50, 1000)))
# 16 figure geometry: centroid G
chk("16 G", (Matrix([3,0,1]) + Matrix([4,3,6]) + Matrix([2,3,2]))/3 == Matrix([3,2,3]))
# 1(x) answer figure: dashed line meets the plotted curve in exactly four points
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "figs"))
import maths_2025_26_figs as FG
pts = FG._curve_pts()
chk("1x four crossings at k=0.6", sum((v1-0.6)*(v2-0.6) < 0 for (u1,v1),(u2,v2) in zip(pts, pts[1:])) == 4)
chk("1x three crossings at small k", sum((v1-0.1)*(v2-0.1) < 0 for (u1,v1),(u2,v2) in zip(pts, pts[1:])) == 3)
# 2 OR endpoint: a = -1 gives f' = 1 + cos x >= 0 with zeros only at odd multiples of pi
chk("2or a=-1", solve(Eq(1 + cos(x), 0), x) == [pi])
print(f"\nall {ok} checks passed")
