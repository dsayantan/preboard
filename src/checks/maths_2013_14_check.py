"""Recompute every answer in maths_2013_14.py (Heritage pre-board 2013-14)."""
from sympy import *
x, y, t, K, a, b, c, r, h, C = symbols('x y t K a b c r h C')
ok = []
def zero(expr, var=None, pts=(0.3, 0.7, 1.1, 0.45)):
    """expr == 0 identically: sympy simplify, else numeric at several points."""
    if simplify(expr) == 0:
        return True
    fs = sorted(expr.free_symbols, key=str)
    import random
    random.seed(1)
    for p in pts:
        sub = {s_: p + 0.13*i for i, s_ in enumerate(fs)}
        if abs(complex(N(expr.subs(sub), 30))) > 1e-15:
            return False
    return True
def chk(name, cond):
    assert cond, name
    ok.append(name)

# 1(i)
A = Matrix([[3, -4], [1, -1]])
P = (A + A.T) / 2; Q = (A - A.T) / 2
chk("1(i) P", P == Matrix([[3, Rational(-3, 2)], [Rational(-3, 2), -1]]))
chk("1(i) Q", Q == Matrix([[0, Rational(-5, 2)], [Rational(5, 2), 0]]) and P + Q == A and P.T == P and Q.T == -Q)
# 1(iii)
sols = solve(6*x**2 + 5*x - 1, x)
chk("1(iii) quadratic", set(sols) == {Rational(1, 6), -1})
chk("1(iii) x=1/6 works", abs(N(atan(Rational(1, 3)) + atan(Rational(1, 2)) - pi/4, 30)) < 1e-25)
chk("1(iii) x=-1 rejected", N(atan(-2) + atan(-3)) < 0)
# 1(v)
F = exp(x)*tan(x/2)
chk("1(v)", zero(diff(F, x) - exp(x)*(1 + sin(x))/(1 + cos(x))))
# 1(vi)
I = integrate(1/(2 + 8*x**2), (x, 0, K))
chk("1(vi)", simplify(I.subs(K, Rational(1, 2)) - pi/16) == 0)
# 1(ix): (1-x^2)(1-y^2)=C ; y=1 constant solution
G = (1 - x**2)*(1 - y**2)
# implicit derivative of G=C must satisfy y(1-x^2)dy + x(1-y^2)dx = 0
dydx = -diff(G, x)/diff(G, y)
chk("1(ix) general", simplify(y*(1 - x**2)*dydx + x*(1 - y**2)) == 0)
chk("1(ix) y=1 satisfies", (y*(1 - x**2)*0 + x*(1 - y**2)).subs(y, 1) == 0)
# intended (1+x^2)(1+y^2)=2
G2 = (1 + x**2)*(1 + y**2); d2 = -diff(G2, x)/diff(G2, y)
chk("1(ix) intended", simplify(y*(1 + x**2)*d2 + x*(1 + y**2)) == 0 and G2.subs({x: 0, y: 1}) == 2)
# 1(x)
p = Rational(5, 8)*Rational(4, 8) + Rational(3, 8)*Rational(5, 8)
chk("1(x)", p == Rational(35, 64))
# 2(a) step by step
D0 = Matrix([[b+c, c+a, a+b], [c+a, a+b, b+c], [a+b, b+c, c+a]])
D1 = Matrix([[1, c+a, a+b], [1, a+b, b+c], [1, b+c, c+a]])
D2 = Matrix([[1, c+a, a+b], [0, b-c, c-a], [0, b-a, c-b]])
chk("2(a) step1", expand(D0.det() - 2*(a+b+c)*D1.det()) == 0)
chk("2(a) step2", expand(D1.det() - D2.det()) == 0)
chk("2(a) step3", expand(D2.det() + (a**2+b**2+c**2-a*b-b*c-c*a)) == 0)
chk("2(a) result", expand(D0.det() + 2*(a**3+b**3+c**3-3*a*b*c)) == 0)
# 2(b)
A = Matrix([[4, 2, 3], [1, 1, 1], [3, 1, -2]])
chk("2(b) det", A.det() == -8)
chk("2(b) adj", A.adjugate() == Matrix([[-3, 7, -1], [5, -17, -1], [-2, 2, 2]]))
X = A.inv()*Matrix([2, 1, 5])
chk("2(b) solution", X == Matrix([Rational(1, 2), Rational(3, 2), -1]))
# 3(b)
v = sin(2*atan(Rational(3, 5)) - asin(Rational(7, 25)))
chk("3(b)", simplify(expand_trig(v) - Rational(304, 425)) == 0 or abs(N(v) - 304/425) < 1e-12)
# 5(a)
phi, lam = symbols('phi lambda')
X_ = sin(phi); Y_ = sin(lam*phi)
y1 = diff(Y_, phi)/diff(X_, phi)
y2 = diff(y1, phi)/diff(X_, phi)
chk("5(a)", zero((1 - X_**2)*y2 - X_*y1 + lam**2*Y_))
# 5(b)
V = pi/3*(2*r*h**2 - h**3)
hs = solve(diff(V, h), h)
chk("5(b) h", Rational(4, 3)*r in hs and simplify(diff(V, h, 2).subs(h, 4*r/3)) == -4*pi*r/3)
chk("5(b) Vmax", simplify(V.subs(h, 4*r/3) - Rational(32, 81)*pi*r**3) == 0)
# 6(a)
F = log((1 + sin(x))/(2 + sin(x)))
chk("6(a)", zero(diff(F, x) - cos(x)/((1 + sin(x))*(2 + sin(x)))))
# 6(b)
chk("6(b) pts", set(solve(y**2 - 2*(y + 4), y)) == {4, -2})
chk("6(b) area", integrate((y + 4)/2 - y**2/4, (y, -2, 4)) == 9)
# 8(a)
tot = binomial(9, 3)
chk("8(a)", (Rational(2*3*4, tot), Rational(binomial(2,2)*7 + binomial(3,2)*6 + binomial(4,2)*5, tot), Rational(binomial(3,3) + binomial(4,3), tot)) == (Rational(2, 7), Rational(55, 84), Rational(5, 84)))
# 8(b)
pp = Rational(1, 4); q = 1 - pp
chk("8(b)", q*pp/(1 - q**2) == Rational(3, 7))
# 9(b)
Y = (2*sqrt(x) + C)*exp(-2*sqrt(x))
chk("9(b)", zero(diff(Y, x) + Y/sqrt(x) - exp(-2*sqrt(x))/sqrt(x)))
# 11(a)
n = Matrix([2, 3, -2]).cross(Matrix([0, 6, 0]) - Matrix([-2, -3, 4]))
chk("11(a) normal", n == Matrix([6, 4, 12]))
chk("11(a) plane", Matrix([3, 2, 6]).dot(Matrix([0, 6, 0])) == 12 and Matrix([3, 2, 6]).dot(Matrix([-2, -3, 4])) == 12
    and Matrix([3, 2, 6]).dot(Matrix([2, 3, -2])) == 0)
# 11(b)
bb = Matrix([2, -3, 6]); cr = (Matrix([2, 3, 2]) - Matrix([-2, 3, 0])).cross(bb)
chk("11(b)", cr == Matrix([6, -20, -12]) and sqrt(cr.dot(cr))/sqrt(bb.dot(bb)) == 2*sqrt(145)/7)
# 12(a)
PD = Rational(25, 100)*Rational(5, 100) + Rational(35, 100)*Rational(4, 100) + Rational(40, 100)*Rational(2, 100)
chk("12(a)", PD == Rational(345, 10000) and Rational(35, 100)*Rational(4, 100)/PD == Rational(28, 69))
# 12(b)
dist = [Rational(binomial(4, k)*binomial(16, 3 - k), binomial(20, 3)) for k in range(4)]
chk("12(b)", dist == [Rational(28, 57), Rational(8, 19), Rational(8, 95), Rational(1, 285)] and sum(dist) == 1
    and sum(k*dist[k] for k in range(4)) == Rational(3, 5))
# 14(a) LPP: min 10x+4y, 4x+y>=80, 2x+y>=60
corners = [(0, 80), (10, 40), (30, 0)]
for (u, w) in corners:
    assert 4*u + w >= 80 and 2*u + w >= 60
Z = {pt: 10*pt[0] + 4*pt[1] for pt in corners}
chk("14(a) values", Z == {(0, 80): 320, (10, 40): 260, (30, 0): 300})
from scipy.optimize import linprog
res = linprog([10, 4], A_ub=[[-4, -1], [-2, -1]], b_ub=[-80, -60], bounds=[(0, None)]*2)
chk("14(a) linprog", abs(res.fun - 260) < 1e-6 and abs(res.x[0] - 10) < 1e-6)
# 14(b) (restored by review): minimum average cost with Rs 2/unit tax
xp = symbols('xp', positive=True)
Ct = 5*xp**2 + 28*xp + 5 + 2*xp
ACt = expand(Ct/xp)
chk("14(b) AC", simplify(ACt - (5*xp + 30 + 5/xp)) == 0)
chk("14(b) stationary", solve(diff(ACt, xp), xp) == [1] and diff(ACt, xp, 2).subs(xp, 1) > 0)
chk("14(b) min AC", ACt.subs(xp, 1) == 40)
print(f"maths_2013_14: {len(ok)} checks passed")
