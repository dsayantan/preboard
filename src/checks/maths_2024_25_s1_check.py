"""Recompute every answer in data/maths_2024_25_s1.py.   python3 src/checks/maths_2024_25_s1_check.py"""
from sympy import *
from fractions import Fraction as Fr
from itertools import product
from scipy.optimize import linprog
x, y, z, t, p, v, r, lam, d = symbols('x y z t p v r lam d', real=True)
ok = 0
def chk(name, cond):
    global ok
    assert cond, name
    ok += 1; print("ok", name)
def num0(e, pts, var=x):
    return all(abs(N(e.subs(var, w))) < 1e-9 for w in pts)

# 1(i)
A = Matrix([[2, 1], [7, 5]])
chk("1i", (A*A.adjugate()).det() == 9)
# 1(ii)
chk("1ii", abs(N(Integral(sin(2*x)*log(tan(x)), (x, 0, pi/2)))) < 1e-9)
# 1(iii)
chk("1iii", simplify(acos(sin(Rational(8, 9)*pi + pi/3)) - 13*pi/18) == 0)
# 1(iv): squared form has y'' to power 2
yp, ypp = symbols('yp ypp')
chk("1iv", degree(expand((1 + yp**2)**3 - ypp**2), ypp) == 2)
# 1(v)
pr = [k for k in range(1, 20) if isprime(k)]
chk("1v", Fr(len(pr), 19)**2 == Fr(64, 361))
# 1(vi)
M = Matrix([[0, x-23, x-29], [x+23, 0, x-31], [x+29, x+31, 0]])
chk("1vi", M.det().subs(x, 0) == 0)
# 1(vii) |x|: left and right derivatives -1, 1
chk("1vii", limit((Abs(t)-0)/t, t, 0, '+') == 1 and limit(Abs(t)/t, t, 0, '-') == -1)
# 1(viii)
chk("1viii", simplify(diff(log(sqrt(tan(x))), x).subs(x, pi/4)) == 1)
# 1(ix)
dom, cod = range(4), range(2)
onto = sum(1 for f in product(cod, repeat=4) if set(f) == set(cod))
chk("1ix-a", onto == 14)
pairs = [(i, j) for i in dom for j in dom]
offdiag = [q for q in pairs if q[0] != q[1]]
chk("1ix-b", 2**len(offdiag) == 2**12)
# 1(x)
B3 = Matrix([[-2, 0, 0], [0, 1, 0], [0, 0, 1]])   # |B| = -2
chk("1x", (-2*B3.inv()).det() == 4)
# 1(xi)
chk("1xi", solve(Rational(3, 10) + (1-p) - Rational(3, 10)*(1-p) - Rational(4, 5), p) == [Rational(2, 7)])
# 1(xii)
D = Matrix([[1, 3, 9], [1, x, x**2], [4, 6, 9]]).det()
chk("1xii", set(solve(D, x)) == {3, Rational(3, 2)} and expand(D - 3*(2*x-3)*(x-3)) == 0)
# 1(xiii)
S_ = ['a', 'b', 'c']; R = {('b', 'c')}
refl = all((u, u) in R for u in S_)
sym = all((w, u) in R for (u, w) in R)
tra = all((u, w2) in R for (u, w) in R for (w1, w2) in R if w == w1)
chk("1xiii", (refl, sym, tra) == (False, False, True))
# 1(xv)
chk("1xv", Fr(3, 8)*Fr(2, 7) == Fr(3, 28) and Fr(binomial(3, 2), binomial(8, 2)) == Fr(3, 28))
# 2
Y = exp(asin(x))
claim = exp(asin(x))*(x + sqrt(1-x**2))/(1-x**2)**Rational(3, 2)
chk("2", num0(diff(Y, x, 2) - claim, [-0.7, -0.2, 0.3, 0.9]))
chk("2-note", num0(exp(asin(x))/exp(-acos(x)) - exp(pi/2), [-0.9, 0.1, 0.6]))
# 2 OR
a_ = symbols('a_')
f2 = a_*(x+9)*(x+1)*(x-3)
asol = solve(f2.subs(x, 0) + 1, a_)[0]
chk("2or-a", asol == Rational(1, 27))
chk("2or-b", diff(f2.subs(a_, asol), x, 2).subs(x, 1) == Rational(20, 27))
# 3
chk("3", integrate(sin(x), (x, 0, pi)) - integrate(sin(x), (x, pi, 2*pi)) == 4)
chk("3n", abs(N(Integral(Abs(sin(x)), (x, 0, 2*pi))) - 4) < 1e-8)
# 4
slope = -sqrt(y)/sqrt(x)
chk("4", slope.subs({x: 4, y: 4}) == -1 and sqrt(4) + sqrt(4) == 4)
# 5
F5 = 2*sqrt(tan(x))
chk("5", num0(diff(F5, x) - sqrt(tan(x))/(sin(x)*cos(x)), [0.2, 0.7, 1.3]))
# 5 OR
F5o = exp(x)/(1+x**2)
chk("5or", simplify(diff(F5o, x) - exp(x)*((1-x)/(1+x**2))**2) == 0)
# 6
chk("6", abs(N(asin(Rational(3, 5)) + asin(Rational(4, 5)) - pi/2)) < 1e-12
    and abs(N(asin(-Rational(3, 5)) + asin(-Rational(4, 5)) + pi/2)) < 1e-12
    and set(solve(16/x**2 - (1 - 9/x**2), x)) == {5, -5})
# 7 numeric: pick x, y, then z = cos(pi - acos x - acos y)
import random
for _ in range(5):
    xa, ya = random.uniform(-1, 1), random.uniform(-1, 1)
    C = float(pi) - float(acos(xa)) - float(acos(ya))
    if 0 <= C <= float(pi):
        za = float(cos(C))
        assert abs(xa**2 + ya**2 + za**2 + 2*xa*ya*za - 1) < 1e-9
chk("7", True)
# 8
F8 = Rational(1, 2)*(x*acos(x) - sqrt(1-x**2))
chk("8", num0(diff(F8, x) - atan(sqrt((1-x)/(1+x))), [-0.8, -0.1, 0.4, 0.95]))
# 9
f9 = 2*x**3 - 9*x**2 + 12*x + 1
chk("9", expand(diff(f9, x) - 6*(x-1)*(x-2)) == 0 and f9.subs(x, 1) == 6 and f9.subs(x, 2) == 5 and f9.subs(x, 5) == 86)
chk("9-sign", solve_univariate_inequality(diff(f9, x) < 0, x, relational=False) == Interval.open(1, 2))
# 9 OR
Y9 = sqrt(x+1) - sqrt(x-1)
chk("9or", num0((x**2-1)*diff(Y9, x, 2) + x*diff(Y9, x) - Y9/4, [1.5, 2, 7]))
# 10
pE = Fr(1, 2)*Fr(28, 100) / (Fr(1, 2)*Fr(28, 100) + Fr(1, 2)*Fr(30, 100))
chk("10", pE == Fr(14, 29))
# 10 OR (enumerate)
P = {'W': Fr(7, 10), 'L': Fr(2, 10), 'N': Fr(1, 10)}
tot = sum(P[a]*P[b]*P[c] for a, b, c in product('WLN', repeat=3)
          if (a+b+c).count('W') >= 2 and 'L' not in (a+b+c))
chk("10or", tot == Fr(49, 100))
# 11
A11 = Matrix([[1, 1, 1], [0, 1, 3], [1, -2, 1]]); B11 = Matrix([6, 11, 0])
chk("11-det", A11.det() == 9)
chk("11-adj", A11.adjugate() == Matrix([[7, -3, 2], [3, 0, -3], [-1, 3, 1]]))
chk("11", A11.inv()*B11 == Matrix([1, 2, 3]))
# 12: cot(y/x) = log x + C satisfies the ODE
C12 = symbols('C12')
ysol = x*acot(log(x) + C12)
chk("12", all(num0(((x*sin(ysol/x)**2 - ysol) + x*diff(ysol, x)).subs(C12, cv), [0.5, 1.3, 2.7]) for cv in (-1, 0.4, 2)))
Cp = cot(4/pi) - log(pi/4)
chk("12-pc", abs(N((x*acot(log(x)+Cp)).subs(x, pi/4)) - 1) < 1e-12)
chk("12-textbook", abs(N((x*acot(log(x)+1)).subs(x, 1)) - N(pi/4)) < 1e-12)
# 12 OR
val = N(Integral(2*log(sin(x)) - log(sin(2*x)), (x, 0, pi/2)))
chk("12or", abs(val - N(-pi/2*log(2))) < 1e-8)
# 13
T = sqrt(4 + x**2)/4 + (4 - x)/6
crit = [s for s in solve(diff(T, x), x) if s.is_real and 0 <= s <= 4]
chk("13-x", crit == [4/sqrt(5)])
Tm = simplify(T.subs(x, crit[0]))
chk("13-T", simplify(Tm - (4 + sqrt(5))/6) == 0 and Tm < T.subs(x, 0) and Tm < T.subs(x, 4))
chk("13-T2", diff(T, x, 2).subs(x, crit[0]) > 0)
# 13 OR
h = 432/r**2; S = 2*pi*r**2 + 2*pi*r*h
rc = [s for s in solve(diff(S, r), r) if s.is_real and s > 0]
chk("13or", rc == [6] and simplify(S.subs(r, 6)) == 216*pi and h.subs(r, 6) == 12)
# 14
ages = [16, 17, 15, 14, 19, 17, 16, 19, 16, 15]
comp = [a for a in ages if not isprime(a)]
chk("14i", Fr(len(comp), 10) == Fr(3, 5))
dist = {a: Fr(ages.count(a), 10) for a in sorted(set(ages))}
chk("14iii", dist == {14: Fr(1, 10), 15: Fr(2, 10), 16: Fr(3, 10), 17: Fr(2, 10), 19: Fr(2, 10)} and sum(dist.values()) == 1)
gt = [a for a in ages if a > 15]
chk("14iv", Fr(sum(1 for a in gt if isprime(a)), len(gt)) == Fr(4, 7))
chk("14v", sum(k*w for k, w in dist.items()) == Fr(164, 10))
# 15
chk("15i", Matrix([1, 1, 1]).norm() == sqrt(3))
al, be = symbols('al be')
gam_c2 = 1 - cos(al)**2 - cos(be)**2
chk("15ii", simplify(cos(2*al) + cos(2*be) + (2*gam_c2 - 1)) == -1)
chk("15iii", solve(Matrix([2, -lam, 3]).dot(Matrix([lam, 5, -1])), lam) == [-1])
a15 = Matrix([2, 1, 2]); b15 = Matrix([5, -3, 1])
chk("15iv", a15.dot(b15)/a15.norm() == 3)
v15 = 20*Matrix([2, 5, 4])/Matrix([2, 5, 4]).norm()
chk("15v", simplify(v15 - 4*sqrt(5)/3*Matrix([2, 5, 4])) == zeros(3, 1) and simplify(v15.norm()) == 20)
# 16
chk("16", set(solve(Eq(3*sqrt(2)/3*sin(t), 1), t)) == {pi/4, 3*pi/4})
# 16 OR: a=(1,0,0), b at 120 deg length 2
a3 = Matrix([1, 0, 0]); b3 = Matrix([2*cos(2*pi/3), 2*sin(2*pi/3), 0])
w = (a3 + 3*b3).cross(3*a3 - b3)
chk("16or", simplify(w.dot(w)) == 300)
# 17
ds = solve(Abs(2*3 - 4*(-1) + 4*2 + d)/6 - 5, d)
chk("17", set(ds) == {12, -48})
# 17 OR
dvec = Matrix([2, -2, 1]).cross(Matrix([1, 2, 2]))
chk("17or", dvec == Matrix([-6, -3, 6]) and dvec.dot(Matrix([2, -2, 1])) == 0 and dvec.dot(Matrix([1, 2, 2])) == 0)
# 18
chk("18", integrate(x**2 + 2 - x, (x, 0, 3)) == Rational(21, 2) and discriminant(x**2 - x + 2, x) < 0)
# 19(i)
C19 = x**2 - 7*x + 36
chk("19i", [s for s in solve(diff(C19, x) - C19/x, x) if s > 0] == [6])
# 19(v)
chk("19v", set(solve(x*(4500 - 100*x) - (30000 + 800*x), x)) == {12, 25})
# 20
P20 = -8*x**3 + 29400*x - 60000
chk("20", [s for s in solve(diff(P20, x), x) if s > 0] == [35] and diff(P20, x, 2).subs(x, 35) < 0 and P20.subs(x, 35) == 626000)
# 20 OR
R20 = x*(80 - x)/4
chk("20or", solve(diff(R20, x), x) == [40] and R20.subs(x, 40) == 400)
# 22 (intended x,y >= 0)
res = linprog([-5, -7], A_ub=[[1, 1], [1, 2], [2, 1]], b_ub=[70, 100, 120], bounds=[(0, None), (0, None)])
chk("22", abs(-res.fun - 410) < 1e-6 and abs(res.x[0] - 40) < 1e-6 and abs(res.x[1] - 30) < 1e-6)
corners = {(0, 0): 0, (60, 0): 300, (50, 20): 390, (40, 30): 410, (0, 50): 350}
for (u, w_), zv in corners.items():
    assert u + w_ <= 70 and u + 2*w_ <= 100 and 2*u + w_ <= 120 and 5*u + 7*w_ == zv
chk("22-corners", True)
# 22 as printed (x<=0, y<=0): max 0 at origin
res2 = linprog([-5, -7], A_ub=[[1, 1], [1, 2], [2, 1]], b_ub=[70, 100, 120], bounds=[(None, 0), (None, 0)])
chk("22-printed", abs(res2.fun) < 1e-9)
# review: Q10 Bayes display split in two (one line overflowed the answer column)
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs"))
import maths_2024_25_s1 as D
q10 = [q for q in D.PAPER["items"] if q.get("num") == "10"][0]
chk("10-display-split", not any("P(E_2)P(H|E_2)}" in blk and "14}{29}" in blk for blk in re.findall(r"\\\[(.*?)\\\]", q10["a"], re.S)))
chk("10-bayes", Fr(1,2)*Fr(28,100) / (Fr(1,2)*Fr(28,100) + Fr(1,2)*Fr(30,100)) == Fr(14,29))
print(f"\nall {ok} checks passed")
