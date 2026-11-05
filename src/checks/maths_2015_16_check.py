"""Recompute every answer in maths_2015_16.py (Heritage pre-board 2015-16)."""
from sympy import *
x, y, a, b, c, C, lam, t = symbols('x y a b c C lambda t')
ok = []
def zero(expr, pts=(0.3, 0.7, 0.55, 0.45)):
    if simplify(expr) == 0:
        return True
    fs = sorted(expr.free_symbols, key=str)
    for p in pts:
        sub = {s_: p + 0.11*i for i, s_ in enumerate(fs)}
        if abs(complex(N(expr.subs(sub), 30))) > 1e-15:
            return False
    return True
def chk(name, cond):
    assert cond, name
    ok.append(name)

# 1(i)
A = Matrix([[2, -3], [3, 4]])
chk("1(i) equation", A**2 - 6*A + 17*eye(2) == zeros(2))
chk("1(i) inverse", A.inv() == Matrix([[4, 3], [-3, 2]])/17 and (6*eye(2) - A)/17 == A.inv())
# 1(iii)
chk("1(iii)", solve(2*x/(1 + x**2) - 1, x) == [1] and sin(2*atan(1)) == 1)
# 1(v)
F = tan(x*exp(x)) - x*exp(x)
chk("1(v)", zero(diff(F, x) - (x + 1)*exp(x)/cot(x*exp(x))**2))
# 1(ix)
chk("1(ix)", Rational(2, 3) + Rational(4, 9) - Rational(4, 5) == Rational(14, 45))
# 1(x)  y = C(x+a)(1-ay)  ->  y/(1-ay) = C(x+a)
Y = C*(x + a)/(1 + a*C*(x + a))
chk("1(x)", zero(Y - x*diff(Y, x) - a*(Y**2 + diff(Y, x))))
chk("1(x) implicit form", zero(Y - C*(x + a)*(1 - a*Y)))
# 2(a) step by step
D0 = Matrix([[(b+c)**2, a**2, a**2], [b**2, (c+a)**2, b**2], [c**2, c**2, (a+b)**2]])
D1 = Matrix([[(b+c)**2, a-b-c, a-b-c], [b**2, c+a-b, 0], [c**2, 0, a+b-c]])
D2 = Matrix([[2*b*c, -2*c, -2*b], [b**2, c+a-b, 0], [c**2, 0, a+b-c]])
D3 = Matrix([[2*b*c, -2*b*c, -2*b*c], [b**2, b*(c+a-b), 0], [c**2, 0, c*(a+b-c)]])
D4 = Matrix([[2*b*c, 0, 0], [b**2, b*(c+a), b**2], [c**2, c**2, c*(a+b)]])
chk("2(a) C2-C1,C3-C1 and factor", expand(D0.det() - (a+b+c)**2*D1.det()) == 0)
chk("2(a) R1-R2-R3", expand(D1.det() - D2.det()) == 0)
chk("2(a) bC2, cC3", expand(D3.det() - b*c*D2.det()) == 0)
chk("2(a) C2+C1,C3+C1", expand(D3.det() - D4.det()) == 0)
chk("2(a) expand R1", expand(D4.det() - 2*a*b**2*c**2*(a+b+c)) == 0)
chk("2(a) result", expand(D0.det() - 2*a*b*c*(a+b+c)**3) == 0)
# 2(b)
A = Matrix([[0, 1, 2], [1, 2, 3], [3, 1, 1]])
chk("2(b) det/adj", A.det() == -2 and A.adjugate() == Matrix([[-1, 1, -1], [8, -6, 2], [-5, 3, -1]]))
chk("2(b) solution", A.inv()*Matrix([-8, -14, -8]) == Matrix([-1, -2, -3]))
# 3(a)
chk("3(a)", abs(N(asin(Rational(4, 5)) + acos(2/sqrt(5)) - acot(Rational(2, 11)), 30)) < 1e-25
    and Rational(4, 3)*Rational(1, 2) < 1)
# 5(a)
Y = acos(x)**2
y1 = diff(Y, x); y2 = diff(Y, x, 2)
chk("5(a)", zero((1 - x**2)*y2 - x*y1 - 2) and y2.subs(x, 0) == 2)
# 5(b)
s = symbols('s', positive=True); A2 = symbols('A2', positive=True)
V = (A2**2*s - s**3)/4
crit = solve(diff(V, s), s)
chk("5(b) crit", crit == [A2/sqrt(3)] and diff(V, s, 2).subs(s, A2/sqrt(3)) < 0)
chk("5(b) Vmax", simplify(V.subs(s, A2/sqrt(3)) - A2**3/(6*sqrt(3))) == 0)
# 6(a)
I = Integral(x*tan(x)/(1/cos(x) + tan(x)), (x, 0, pi))
chk("6(a) numeric", abs(N(I, 20) - N(pi*(pi - 2)/2, 20)) < 1e-12)
chk("6(a) aux", abs(N(Integral(1/(1 + sin(x)), (x, 0, pi))) - 2) < 1e-12)
# 6(b)
chk("6(b)", integrate(8 + 2*y - y**2, (y, -1, 3)) == Rational(92, 3)
    and all((8 + 2*v - v**2) > 0 for v in [-1, 0, 1, 2, 3]))
# 8(a)
p = Rational(1, 3); q = 1 - p
chk("8(a)", p/(1 - q**2) == Rational(3, 5) and q*p/(1 - q**2) == Rational(2, 5))
# 8(b)
w1, b1, w2, b2 = Rational(4, 6), Rational(2, 6), Rational(3, 8), Rational(5, 8)
chk("8(b)", (w1*w2, b1*b2, w1*b2 + b1*w2) == (Rational(1, 4), Rational(5, 24), Rational(13, 24)))
# 9(b)
Y = 3/sqrt(1 - x**2) - 1
chk("9(b)", zero((1 - x**2)*diff(Y, x) - x*Y - x) and Y.subs(x, 0) == 2)
# 11(a)
b1v, b2v = Matrix([1, -1, 1]), Matrix([2, 1, 1])
n = b1v.cross(b2v); d = Matrix([2, -1, -1]) - Matrix([1, 2, 1])
chk("11(a)", n == Matrix([-2, 1, 3]) and d.dot(n) == -11 and abs(d.dot(n))/sqrt(n.dot(n)) == 11/sqrt(14))
# 11(b)
L = Matrix([2, -1, 0]).cross(Matrix([0, -1, 3]))
N2 = L.cross(Matrix([4, 5, -3]))
chk("11(b)", L == Matrix([-3, -6, -2]) and N2 == Matrix([28, -17, 9])
    and N2.dot(Matrix([4, 5, -3])) == 0)
# family-of-planes cross-check
chk("11(b) family", solve(Matrix([2, -1 - lam, 3*lam]).dot(Matrix([4, 5, -3])), lam) == [Rational(3, 14)])
# 12(a)
chk("12(a)", Rational(1, 10)/Rational(2, 10) == Rational(1, 2) and Rational(3, 10) + Rational(2, 10) - Rational(1, 10) == Rational(2, 5))
# 12(b)
pb = [Rational(4, 10), Rational(6, 8), Rational(8, 9)]
PB = sum(pb)/3
chk("12(b)", PB == Rational(367, 540) and (pb[1] + pb[2])/3/PB == Rational(295, 367))
# 15(b): max 2.5x+y, x+3y<=12, 3x+y<=12
corners = [(0, 0), (4, 0), (3, 3), (0, 4)]
assert all(u + 3*w <= 12 and 3*u + w <= 12 for u, w in corners)
Z = {pt: Rational(5, 2)*pt[0] + pt[1] for pt in corners}
chk("15(b)", max(Z.values()) == Rational(21, 2) and Z[(3, 3)] == Rational(21, 2) and Z[(4, 0)] == 10)
from scipy.optimize import linprog
res = linprog([-2.5, -1], A_ub=[[1, 3], [3, 1]], b_ub=[12, 12], bounds=[(0, None)]*2)
chk("15(b) linprog", abs(-res.fun - 10.5) < 1e-6)
# 13(b) (restored by review): TC, MC, AC increasing
xp = symbols('xp', positive=True)
ACf = xp + 5 + 36/xp
TC = expand(xp*ACf)
chk("13(b) TC", TC == xp**2 + 5*xp + 36)
chk("13(b) MC", diff(TC, xp) == 2*xp + 5)
chk("13(b) AC increasing x>6", solve(diff(ACf, xp) > 0, xp).as_set() == Interval.open(6, oo))
chk("13(b) AC(6)=17", ACf.subs(xp, 6) == 17)
print(f"maths_2015_16: {len(ok)} checks passed")
