"""Recompute every Mathematics answer in the JEE mock tests (src/jee/maths_t{1,2,3}.py) with sympy.

For each MCQ: the value of every option is written out here (in the order printed), the true value
is computed independently, and the check asserts that the option the module marks correct carries
the true value and that no other option does.  Indefinite integrals are checked by differentiating
each option; equation-solving questions by comparing solution sets.  Conceptual MCQs assert the
chosen index (the reasoning is in the solution).  NUM answers are recomputed and compared.

    python3 src/checks/jee_maths_check.py
"""
import os, sys, itertools
from fractions import Fraction
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
sys.path[:0] = [SRC, os.path.join(SRC, "jee"), os.path.join(SRC, "data"), os.path.join(SRC, "figs")]
import jee_kit

x, y, z, t, a, b, c, m, p, X, Y, r, h, k, lam = sp.symbols("x y z t a b c m p X Y r h k lambda", real=True)
pi, I, sqrt, log = sp.pi, sp.Integral, sp.sqrt, sp.log
R = sp.Rational
fails, n_ok = [], 0
Q = {T: jee_kit.load("maths", T) for T in (1, 2, 3)}


def _same(u, v):
    if isinstance(u, (set, frozenset, tuple, str)) or isinstance(v, (set, frozenset, tuple, str)):
        return u == v
    if isinstance(u, sp.MatrixBase) or isinstance(v, sp.MatrixBase):
        return isinstance(u, sp.MatrixBase) and isinstance(v, sp.MatrixBase) and \
            u.shape == v.shape and sp.simplify(u - v) == sp.zeros(*u.shape)
    d = sp.simplify(sp.sympify(u) - sp.sympify(v))
    if d == 0:
        return True
    try:
        return abs(complex(sp.N(d, 30))) < 1e-12
    except TypeError:
        return False


def mcq(T, n, true, opts, same=_same, note=""):
    """n is the printed question number 51..70."""
    global n_ok
    it = Q[T][n - 51]
    tag = f"T{T} Q{n}"
    if it["kind"] != "mcq":
        fails.append(f"{tag}: not an MCQ"); return
    ans = it["answer"]
    hits = [i for i, o in enumerate(opts) if same(true, o)]
    if hits != [ans]:
        fails.append(f"{tag}: true value matches options {hits}, module marks {ans}  {note}")
    else:
        n_ok += 1


def concept(T, n, idx):
    global n_ok
    it = Q[T][n - 51]
    if it["answer"] != idx:
        fails.append(f"T{T} Q{n}: conceptual answer is {idx}, module marks {it['answer']}")
    else:
        n_ok += 1


def num(T, n, true):
    global n_ok
    it = Q[T][n - 51]
    tv = sp.nsimplify(true)
    if not (tv.is_integer and int(tv) == it["answer"]):
        fails.append(f"T{T} Q{n}: computed {true}, module says {it['answer']}")
    else:
        n_ok += 1


def antideriv(integrand, var=x):
    """same() for indefinite integrals: option differentiates back to the integrand."""
    def s(_true, opt):
        d = sp.simplify(sp.diff(opt, var) - integrand)
        if d == 0:
            return True
        # numeric spot checks on the domain of interest
        for v in (R(3, 10), R(7, 10), R(11, 10), R(13, 10)):
            try:
                if abs(complex(sp.N(d.subs(var, v)))) > 1e-9:
                    return False
            except Exception:
                return False
        return True
    return s


def M(*rows):
    return sp.Matrix(rows)


# ============================================================================ TEST 1
T = 1
# 51 onto functions 5 -> 2 (inclusion-exclusion, and brute force)
cnt = sum(1 for f in itertools.product((0, 1), repeat=5) if set(f) == {0, 1})
assert cnt == 2**5 - 2
mcq(T, 51, cnt, [30, 32, 25, 31])
# 52 perpendicularity: symmetric only (index 2)
concept(T, 52, 2)
# 53 tan^-1 2x + tan^-1 3x = pi/4 : keep roots of the tan-equation that satisfy the original
cand = sp.solve(sp.Eq(5 * x, 1 - 6 * x**2), x)
sols = frozenset(s for s in cand if _same(sp.atan(2 * s) + sp.atan(3 * s), pi / 4))
mcq(T, 53, sols, [frozenset({-1, R(1, 6)}), frozenset({R(1, 6)}), frozenset({-1}), frozenset({1, R(-1, 6)})])
# 54 skew part of A
A = M([2, 5], [-1, 3])
mcq(T, 54, (A - A.T) / 2, [M([0, 6], [-6, 0]), M([0, -3], [3, 0]), M([2, 2], [2, 3]), M([0, 3], [-3, 0])])
assert (A + A.T) / 2 + (A - A.T) / 2 == A
# 55 |A adj A|
A = M([3, 1], [4, 2])
mcq(T, 55, (A * A.adjugate()).det(), [2, 4, 8, 16])
# 56 determinant
D = M([p, p, p], [p, p + x, p], [p, p, p + y]).det()
mcq(T, 56, D, [p * x * y, p**2 * x * y, p * x * y * (p + x + y), 0])
# 57 derivative of |x-2|+|x-5| at 6 (two-sided difference quotient)
f = sp.Abs(x - 2) + sp.Abs(x - 5)
hh = sp.Symbol("hh", positive=True)
dl = sp.limit((f.subs(x, 6) - f.subs(x, 6 - hh)) / hh, hh, 0)
dr = sp.limit((f.subs(x, 6 + hh) - f.subs(x, 6)) / hh, hh, 0)
assert dl == dr
mcq(T, 57, dr, [0, -2, 1, 2])
# 58 discontinuities of 1/(x-[x]) in (-2,3): where frac part is 0 = integers strictly inside
pts = [n for n in range(-5, 6) if -2 < n < 3]
# the stem counts undefined points as discontinuities; option "0" is the domain-only convention
assert "not defined is to be counted" in Q[1][58 - 51]["q"]
mcq(T, 58, len(pts), [5, 0, 4, "inf"], same=lambda u, v: u == v)
# 59 increasing interval of x^3 - 27x + 5
f = x**3 - 27 * x + 5
inc = sp.solve_univariate_inequality(sp.diff(f, x) > 0, x, relational=False)
mcq(T, 59, inc, [sp.Union(sp.Interval.open(-sp.oo, -3), sp.Interval.open(3, sp.oo)), sp.Interval.open(-3, 3),
                 sp.Interval.open(-sp.oo, 3), sp.Interval.open(-3, sp.oo)], same=lambda u, v: u == v)
# not increasing on the union itself, so the correct option must name the two intervals separately
assert f.subs(x, -4) > f.subs(x, 4) and r"\cup" not in Q[1][59 - 51]["options"][0]
# 60 point on sqrt x + sqrt y = 6 with slope -1 (curve check + slope)
def on_curve_slope(P):
    px, py = P
    if not _same(sqrt(px) + sqrt(py), 6):
        return None
    return -sqrt(py) / sqrt(px)
truth = [P for P in [(3, 3), (9, 9), (6, 6), (16, 4)] if on_curve_slope(P) is not None and _same(on_curve_slope(P), -1)]
mcq(T, 60, tuple(truth[0]), [(3, 3), (9, 9), (6, 6), (16, 4)])
# 61 indefinite integral
ig = sp.exp(x) * (1 + sp.sin(x)) / (1 + sp.cos(x))
mcq(T, 61, None, [sp.exp(x) * sp.cot(x / 2), -sp.exp(x) * sp.tan(x / 2), sp.exp(x) * sp.tan(x / 2),
                  sp.exp(x) * sp.sec(x / 2)**2 / 2], same=antideriv(ig))
# 62 definite integral (numeric)
val = sp.Integral(1 / (1 + sqrt(sp.tan(x))), (x, pi / 6, pi / 3)).evalf(30)
mcq(T, 62, val, [pi / 6, pi / 4, pi / 3, pi / 12])
# 63
val = sp.integrate(sp.cos(x), (x, 0, pi / 2)) - sp.integrate(sp.cos(x), (x, pi / 2, 3 * pi / 2))
assert abs(sp.Integral(sp.Abs(sp.cos(x)), (x, 0, 3 * pi / 2)).evalf(20) - val) < 1e-12
mcq(T, 63, val, [3, -1, 1, 2])
# 64 area between x = y^2 and x = y + 2
ys = sorted(sp.solve(sp.Eq(y**2, y + 2), y))
val = sp.integrate((y + 2) - y**2, (y, ys[0], ys[1]))
mcq(T, 64, val, [R(10, 3), 9, R(9, 2), R(7, 6)])
# 65 linear DE (1-x^2)y' - xy = x, y(0)=1 -> y(sqrt3/2)
Yf = sp.Function("Y")
sol = sp.dsolve(sp.Eq((1 - x**2) * Yf(x).diff(x) - x * Yf(x), x), Yf(x), ics={Yf(0): 1}).rhs
assert sp.simplify((1 - x**2) * sp.diff(sol, x) - x * sol - x) == 0
mcq(T, 65, sol.subs(x, sqrt(3) / 2), [4, 3, 1, 5])
# 66 d/dx[(y')^4] = 4 (y')^3 y'' -> order 2, degree 1
mcq(T, 66, 2 + 1, [5, 6, 2, 3])
# 67 sin(theta) = 1/(|a||b|), theta in [0, pi]
th = sp.Symbol("th")
angs = frozenset(sp.solveset(sp.Eq(2 / sqrt(3) * sp.sin(th), 1), th, sp.Interval(0, pi)))
mcq(T, 67, angs, [frozenset({pi / 3}), frozenset({pi / 3, 2 * pi / 3}), frozenset({pi / 6, 5 * pi / 6}),
                  frozenset({pi / 6})])
# 68 sum cos 2alpha for a random direction
l_, m_, n_ = sp.Matrix([1, 2, 2]) / 3
val = sp.simplify(sum(2 * u**2 - 1 for u in (l_, m_, n_)))
mcq(T, 68, val, [-1, 1, 2, -2])
# 69 perpendicular planes
lv = sp.solve(sp.Matrix([3, -lam, 2]).dot(sp.Matrix([lam, 4, -1])), lam)
mcq(T, 69, lv[0], [2, R(1, 2), -2, R(-2, 7)])
# 70 Bayes
pr = [R(30, 100), R(30, 100), R(40, 100)]; dq = [R(2, 100), R(3, 100), R(4, 100)]
PD = sum(u * v for u, v in zip(pr, dq))
mcq(T, 70, pr[2] * dq[2] / PD, [R(6, 31), R(9, 31), R(2, 5), R(16, 31)])
# 71 cone in sphere r=9
V = sp.pi / 3 * (18 * h - h**2) * h
crit = [s for s in sp.solve(sp.diff(V, h), h) if s > 0 and sp.diff(V, h, 2).subs(h, s) < 0]
num(T, 71, crit[0])
# 72 LPP by enumerating all vertices
def lpp(obj, cons):
    """cons: list of (coef_x, coef_y, rhs) meaning cx*x + cy*y <= rhs ; includes x>=0, y>=0."""
    lines = cons + [(-1, 0, 0), (0, -1, 0)]
    best = None
    for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(lines, 2):
        d = a1 * b2 - a2 * b1
        if d == 0:
            continue
        px = Fraction(c1 * b2 - c2 * b1, d); py = Fraction(a1 * c2 - a2 * c1, d)
        if all(u * px + v * py <= w for u, v, w in lines):
            val = obj[0] * px + obj[1] * py
            if best is None or val > best[0]:
                best = (val, (px, py))
    return best
best = lpp((3, 5), [(1, 1, 70), (1, 2, 100), (2, 1, 120)])
assert best[1] == (40, 30)
num(T, 72, best[0])
# 73 16 Var, X ~ B(4, 1/4) from the distribution
pmf = {kk: sp.binomial(4, kk) * R(1, 4)**kk * R(3, 4)**(4 - kk) for kk in range(5)}
E = sum(kk * v for kk, v in pmf.items()); E2 = sum(kk**2 * v for kk, v in pmf.items())
num(T, 73, 16 * (E2 - E**2))
# 74 linear system
A = M([4, 2, 3], [1, 1, 1], [3, 1, -2]); B = sp.Matrix([5, 2, 7])
assert A.det() == -8 and A.adjugate() == M([-3, 7, -1], [5, -17, -1], [-2, 2, 2])
S = A.inv() * B
assert list(S) == [1, 2, -1]
num(T, 74, sum(u**2 for u in S))
# 75
Ks = sp.solve(sp.Eq(sp.integrate(1 / (9 + x**2), (x, 0, k)), pi / 12), k)
num(T, 75, [s for s in Ks if s > 0][0])

# ============================================================================ TEST 2
T = 2
# 51 R = {(c,a)} on {a,b,c}
Aset = "abc"; Rel = {("c", "a")}
refl = all((u, u) in Rel for u in Aset)
sym = all((v, u) in Rel for u, v in Rel)
trans = all((u, w) in Rel for u, v in Rel for v2, w in Rel if v == v2)
assert (refl, sym, trans) == (False, False, True)
concept(T, 51, 3)
# 52 inverse function
f = (3 * x - 5) / 2
inv = sp.solve(sp.Eq(f, y), x)[0].subs(y, x)
mcq(T, 52, inv, [(2 * x + 5) / 3, (2 * x - 5) / 3, 2 / (3 * x - 5), (3 * x + 5) / 2])
# 53
mcq(T, 53, sp.cot(pi / 2 + sp.atan(R(1, 3))), [R(1, 3), -3, R(-1, 3), 3])
# 54 principal value
mcq(T, 54, sp.acos(sp.sin(9 * pi / 7)), [3 * pi / 14, 11 * pi / 14, -3 * pi / 14, 9 * pi / 7])
# 55
A = M([3, -2], [4, 1])
assert A**2 - 4 * A + 11 * sp.eye(2) == sp.zeros(2)
mcq(T, 55, A.inv(), [M([3, 2], [-4, 1]) / 11, M([-1, -2], [4, -3]) / 11, M([1, -2], [4, 3]) / 11,
                     M([1, 2], [-4, 3]) / 11])
# 56 |C^2| for |A| = 2, order 3 — use a concrete matrix with det 2
A = M([2, 0, 0], [0, 1, 1], [0, 0, 1]); assert A.det() == 2
C = A.adjugate().T
assert (A.cofactor_matrix() - C) == sp.zeros(3)
A2 = M([1, 2, 0], [0, 1, 3], [1, 0, 1]); A2 = A2 * sp.diag(1, 1, sp.Rational(2, 1) / A2.det())
assert A2.det() == 2 and (A2.cofactor_matrix()**2).det() == 16
mcq(T, 56, (C**2).det(), [16, 4, 64, 256])
# 57 singular values of x
roots = sp.solve(M([1, 2, 4], [1, x, x**2], [1, 5, 25]).det(), x)
mcq(T, 57, sum(roots), [3, 10, 7, -7])
# 58
yv = log(sqrt(sp.tan(x)))
mcq(T, 58, sp.diff(yv, x).subs(x, pi / 6), [1 / sqrt(3), 2 / sqrt(3), 4 / sqrt(3), sqrt(3) / 2])
# 59 continuity: left limit of kx/|x| is -k
kk = sp.Symbol("kk")
left = sp.limit(kk * x / sp.Abs(x), x, 0, "-")
ks = sp.solve(sp.Eq(left, 2), kk)
mcq(T, 59, ks[0], [2, 1, -2, "none"])
# 60 LPP
best = lpp((3, 2), [(2, 1, 50), (1, 2, 40)])
assert best[1] == (20, 10)
mcq(T, 60, best[0], [75, 70, 80, 40])
# 61
inc = sp.solve_univariate_inequality(sp.diff(3 + 2 * x - sp.exp(x), x) > 0, x, relational=False)
mcq(T, 61, inc, [sp.Interval.open(log(2), sp.oo), sp.Interval.open(-sp.oo, log(2)),
                 sp.Interval.open(-sp.oo, 0), sp.Interval.open(0, sp.oo)], same=lambda u, v: u == v)
# (-oo, 0) is a sub-interval of increase, so the stem must ask for the LARGEST interval
assert sp.Interval.open(-sp.oo, 0).is_subset(inc) and "largest interval" in Q[2][61 - 51]["q"]
# 62 a - 3 sin x >= 0 for all x  <=>  a >= max(3 sin x) = 3 ; test sample values of a
def ok_a(av):
    return sp.minimum(av - 3 * sp.sin(x), x, sp.Interval(0, 2 * pi)) >= 0
opts = [lambda av: av >= 3, lambda av: av <= -3, lambda av: av >= -3, lambda av: abs(av) <= 3]
samples = [-4, -3, 0, 2, 3, 4]
truth_set = tuple(ok_a(s) for s in samples)
mcq(T, 62, truth_set, [tuple(bool(o(s)) for s in samples) for o in opts])
# 63
mcq(T, 63, None, [-x**2 * sp.cos(x) + 2 * x * sp.sin(x) - 2 * sp.cos(x),
                  x**2 * sp.cos(x) - 2 * x * sp.sin(x) - 2 * sp.cos(x),
                  -x**2 * sp.cos(x) + 2 * x * sp.sin(x) + 2 * sp.cos(x),
                  -x**2 * sp.cos(x) - 2 * x * sp.sin(x) + 2 * sp.cos(x)], same=antideriv(x**2 * sp.sin(x)))
# 64
ig = sp.exp(x) * (x**2 + 1) / (x + 1)**2
mcq(T, 64, None, [sp.exp(x) * (x + 1) / (x - 1), sp.exp(x) / (x + 1)**2, sp.exp(x) * (x - 1) / (x + 1),
                  sp.exp(x) / (x + 1)], same=antideriv(ig))
# 65
val = sp.Integral(sp.cos(x)**2 / (1 + sp.sin(x) * sp.cos(x)), (x, 0, pi / 2)).evalf(30)
mcq(T, 65, val, [2 * pi / (3 * sqrt(3)), pi / (3 * sqrt(3)), pi / sqrt(3), pi / 4])
# 66
g = 3 + 2 * y - y**2
assert sp.solve_univariate_inequality(g >= 0, y, relational=False) == sp.Interval(-1, 3)
mcq(T, 66, sp.integrate(g, (y, -1, 3)), [R(28, 3), R(16, 3), 9, R(32, 3)])
# 67 homogeneous DE: check the candidate satisfies DE and IC; options as implicit F(x,y)=0
cands = [sp.cot(y / x) - log(x) - 1, sp.tan(y / x) - log(x) - 1, sp.cot(y / x) - 1 + log(x), sp.cot(y / x) - log(x)]
def solves(Fxy):
    # implicit slope -F_x/F_y must equal y/x - sin^2(y/x); IC y(1)=pi/4
    slope = -sp.diff(Fxy, x) / sp.diff(Fxy, y)
    dexp = slope - (y / x - sp.sin(y / x)**2)
    pts = [(R(13, 10), None), (R(17, 10), None)]
    good = _same(Fxy.subs({x: 1, y: pi / 4}), 0)
    for px, _ in pts:
        # find y on the curve near the solution branch, then test the slope
        yy = sp.nsolve(Fxy.subs(x, px), y, 0.6)
        good = good and abs(sp.N(dexp.subs({x: px, y: yy}))) < 1e-9
    return good
mcq(T, 67, True, [solves(F) for F in cands], same=lambda u, v: u == v)
# 68 |b|
bb = sp.Symbol("bb", positive=True)
# (3a+b).(a-2b) with |a|=1, a.b=0
mcq(T, 68, sp.solve(sp.Eq(3 * 1 - 2 * bb**2, -15), bb)[0], [9, sqrt(6), 2, 3])
# 69 skew lines
a1, b1 = sp.Matrix([1, 2, 1]), sp.Matrix([1, -1, 1]); a2, b2 = sp.Matrix([2, 1, -1]), sp.Matrix([2, 1, 1])
nn = b1.cross(b2)
mcq(T, 69, abs((a2 - a1).dot(nn)) / nn.norm(), [11 / sqrt(14), 9 / sqrt(14), 3 / sqrt(14), 9 / sqrt(6)])
# 70 series: enumerate outcomes
pw, pl, pd = R(6, 10), R(3, 10), R(1, 10)
tot = 0
for o in itertools.product("WLD", repeat=3):
    if o.count("W") >= 2 and o.count("L") == 0:
        tot += sp.prod([{"W": pw, "L": pl, "D": pd}[s] for s in o])
mcq(T, 70, tot, [R(324, 1000), R(648, 1000), R(216, 1000), R(432, 1000)])
# 71 100 Var(X), X = number of tests: full distribution
ps = [R(9, 10), R(7, 10), R(4, 10)]
dist = {}
for o in itertools.product((0, 1), repeat=3):
    pr_ = sp.prod([pi_ if s else 1 - pi_ for pi_, s in zip(ps, o)])
    dist[sum(o)] = dist.get(sum(o), 0) + pr_
E = sum(kk * v for kk, v in dist.items()); E2 = sum(kk**2 * v for kk, v in dist.items())
assert E == 2
num(T, 71, 100 * (E2 - E**2))
# 72 can of volume 128 pi
rp = sp.Symbol("rp", positive=True)
S = 2 * pi * rp**2 + 2 * pi * rp * (128 / rp**2)
r0 = sp.solve(sp.diff(S, rp), rp)[0]
assert sp.diff(S, rp, 2).subs(rp, r0) > 0
num(T, 72, sp.simplify(S.subs(rp, r0) / pi))
# 73 triangle area
Ap, Bp, Cp = sp.Matrix([1, 1, 1]), sp.Matrix([1, 2, 3]), sp.Matrix([2, 3, 1])
Dl = (Bp - Ap).cross(Cp - Ap).norm() / 2
num(T, 73, 4 * Dl**2)
# 74 area between y = a x^2 and x = a y^2 equals 12
ap = sp.Symbol("ap", positive=True)
area = sp.integrate(sqrt(x / ap) - ap * x**2, (x, 0, 1 / ap))
asol = sp.solve(sp.Eq(area, 12), ap)
num(T, 74, 1 / asol[0])
# 75 (x^2 - y^2)dx + 2xy dy = 0 through (2,4): x^2 + y^2 = C x
Cc = sp.Symbol("Cc")
Fxy = x**2 + y**2 - Cc * x
Cv = sp.solve(Fxy.subs({x: 2, y: 4}), Cc)[0]
slope = -sp.diff(Fxy, x) / sp.diff(Fxy, y)
assert sp.simplify((slope - (y**2 - x**2) / (2 * x * y)).subs(Cc, (x**2 + y**2) / x)) == 0
yv = [s for s in sp.solve(Fxy.subs({Cc: Cv, x: 5}), y) if s > 0]
num(T, 75, yv[0])

# ============================================================================ TEST 3
T = 3
# 51 R = {(b,b)}
Rel = {("b", "b")}
refl = all((u, u) in Rel for u in "abc")
sym = all((v, u) in Rel for u, v in Rel)
trans = all((u, w) in Rel for u, v in Rel for v2, w in Rel if v == v2)
assert (refl, sym, trans) == (False, True, True)
concept(T, 51, 1)
# 52 onto Z->Z fails (0 has no preimage), onto R->R holds
assert sp.solve(sp.Eq(2 * x + 3, 0), x)[0] == R(-3, 2)
concept(T, 52, 3)
# 53
expr = sp.sin(sp.acot(sp.tan(sp.acos(x))))
mcq(T, 53, None, [sqrt(1 - x**2), 1 / x, x, x / sqrt(1 - x**2)],
    same=lambda _u, v: all(abs(sp.N(expr.subs(x, s) - v.subs(x, s))) < 1e-12 for s in (R(1, 5), R(1, 2), R(9, 10))))
# 54 solve cos(2 atan x) = 1/2
sols = frozenset(sp.solve(sp.Eq(sp.cos(2 * sp.atan(x)), R(1, 2)), x))
mcq(T, 54, sols, [frozenset({1 / sqrt(3), -1 / sqrt(3)}), frozenset({1 / sqrt(3)}), frozenset({sqrt(3), -sqrt(3)}),
                  frozenset({1, -1})], same=lambda u, v: u == frozenset(sp.nsimplify(s) for s in v) or u == v)
# 55
sols = frozenset(sp.solve(sp.Eq(x**2, 2 * x + 8), x))
mcq(T, 55, sols, [frozenset({-4, 2}), frozenset({4}), frozenset({4, -2}), frozenset({2, -2})])
# 56
D = M([a - b - c, 2 * a, 2 * a], [2 * b, b - c - a, 2 * b], [2 * c, 2 * c, c - a - b]).det()
mcq(T, 56, D, [-(a + b + c)**3, (a + b + c)**3, 2 * (a + b + c)**3, (a + b + c) * (a**2 + b**2 + c**2)])
# 57 |2 A^-1| with |A| = -3, order 3 (concrete matrix)
A = sp.diag(-3, 1, 1)
mcq(T, 57, (2 * A.inv()).det(), [R(8, 3), R(-2, 3), R(-3, 8), R(-8, 3)])
# 58
yv = sp.exp(2 * sp.asin(x))
mcq(T, 58, sp.diff(yv, x, 2).subs(x, 0), [4, 2, 0, 8])
# 59
yv = (x + sqrt(x**2 - 1))**m
lhs = (x**2 - 1) * sp.diff(yv, x, 2) + x * sp.diff(yv, x)
def same59(_u, v):
    return all(abs(sp.N((lhs - v.subs(y, yv) if isinstance(v, sp.Expr) else lhs - v).subs({x: xv, m: mv}))) < 1e-9
               for xv, mv in ((R(3, 2), 2), (R(5, 2), R(1, 3)), (3, -1)))
mcq(T, 59, None, [-m**2 * y, m * y, m**2 * y, m**2], same=same59)
# 60
hf = -5 * t**2 + 4 * t + 1
t0 = sp.solve(sp.diff(hf, t), t)[0]
mcq(T, 60, hf.subs(t, t0), [1, R(9, 5), R(13, 5), R(2, 5)])
# 61
rr = sp.Symbol("rr", positive=True)
V = pi * rr**2 * (6 - 2 * pi * rr)
r0 = sp.solve(sp.diff(V, rr), rr)[0]
assert sp.diff(V, rr, 2).subs(rr, r0) < 0
mcq(T, 61, V.subs(rr, r0), [4 / pi, 16 / pi, 8 * pi, 8 / pi])
# 62
xp = sp.Symbol("xp", positive=True)
ig = (1 + log(xp)) * sp.tan(xp * log(xp))**2
mcq(T, 62, None, [sp.tan(xp * log(xp)) - xp * log(xp), sp.tan(xp * log(xp)) + xp * log(xp),
                  sp.sec(xp * log(xp))**2, sp.tan(xp * log(xp)) - xp], same=antideriv(ig, xp))
# 63 on (0, pi/2)
ig = sqrt(sp.tan(x)) + sqrt(sp.cot(x))
mcq(T, 63, None, [sqrt(2) * sp.asin(sp.sin(x) + sp.cos(x)), sp.asin(sp.sin(x) - sp.cos(x)) / sqrt(2),
                  sqrt(2) * sp.asin(sp.sin(x) - sp.cos(x)), sqrt(2) * sp.acos(sp.sin(x) + sp.cos(x))],
    same=antideriv(ig))
# 64
val = sp.Integral(x * sp.sin(x) / (1 + sp.cos(x)**2), (x, 0, pi)).evalf(30)
mcq(T, 64, val, [pi**2 / 2, pi / 2, pi**2 / 8, pi**2 / 4])
# 65 area |y| from 0 to 4
fy = x * (3 - x)
val = sp.integrate(fy, (x, 0, 3)) - sp.integrate(fy, (x, 3, 4))
import mpmath
assert abs(mpmath.quad(lambda u: abs(u * (3 - u)), [0, 3, 4]) - float(val)) < 1e-10
mcq(T, 65, val, [R(19, 3), R(8, 3), R(9, 2), R(11, 3)])
# 66 linear DE: option F(x,y)=C  ->  y = (rhs + C)/IF ; test that y satisfies DE for C = 1
xp = sp.Symbol("xp", positive=True)
def de66(yexpr):
    return sp.simplify(sp.diff(yexpr, xp) + yexpr / (2 * sqrt(xp)) - sp.exp(-sqrt(xp)) / (2 * sqrt(xp)))
cands = [(2 * sqrt(xp) + 1) * sp.exp(-2 * sqrt(xp)), (2 * sqrt(xp) + 1) * sp.exp(-sqrt(xp)),
         (sqrt(xp) + 1) * sp.exp(sqrt(xp)), (sqrt(xp) + 1) * sp.exp(-sqrt(xp))]
mcq(T, 66, 0, [de66(cnd) for cnd in cands])
# 67 degree: multiply by y' -> a y'^3 - c y' + b = 0
yp = sp.Symbol("yp")
poly = sp.Poly(sp.expand((a * yp**2 + b / yp - c) * yp), yp)
mcq(T, 67, poly.degree(), [2, 3, 1, "nd"], same=lambda u, v: u == v)
# 68 area from diagonals
d1, d2 = sp.Matrix([3, 1, -2]), sp.Matrix([1, -3, 4])
mcq(T, 68, d1.cross(d2).norm() / 2, [10 * sqrt(3), 5 * sqrt(3) / 2, 5 * sqrt(3), 20 * sqrt(3)])
# 69 plane: a candidate is right iff it contains P and two points of the line
P0 = (1, 0, 0); L0 = (0, 1, 2); L1 = (2, 0, 3)
def plane(cx, cy, cz, d):
    return lambda q: cx * q[0] + cy * q[1] + cz * q[2] == d
opts = [plane(3, 5, 1, 3), plane(3, 5, -1, 3), plane(3, -5, -1, 3), plane(1, 5, -3, 1)]
mcq(T, 69, True, [all(o(q) for q in (P0, L0, L1)) for o in opts], same=lambda u, v: u == v)
# 70 sum 9 with two dice, alternate throws
pp = R(sum(1 for i in range(1, 7) for j in range(1, 7) if i + j == 9), 36)
mcq(T, 70, pp / (1 - (1 - pp)**2), [R(8, 17), R(1, 2), R(9, 17), R(9, 16)])
# 71
xs = [s for s in sp.solve(sp.Eq(25 + 144, x**2), x) if s > 0]
assert _same(sp.asin(R(5, xs[0])) + sp.asin(R(12, xs[0])), pi / 2)
num(T, 71, xs[0])
# 72
P = sp.Rational(sp.binomial(3, 3) + sp.binomial(4, 3) + sp.binomial(5, 3), sp.binomial(12, 3))
num(T, 72, P.p + P.q)
# 73
kvals = sp.solve(sp.Eq(sp.Abs(1 - 4 + 6 - k) / 3, 4), k)
assert len(kvals) == 2
num(T, 73, sum(kvals))
# 74
best = lpp((5, 4), [(1, 3, 12), (3, 1, 12)])
assert best[1] == (3, 3)
num(T, 74, best[0])
# 75
A = M([2, 3, 4], [1, 1, 2], [3, 2, 1]); B = sp.Matrix([25, 12, 15])
assert A.det() == 5 and A.adjugate() == M([-3, 5, 2], [5, -10, 0], [-1, 5, -1])
S = A.inv() * B
assert list(S) == [3, 1, 4]
num(T, 75, sum(S))

# ---------------------------------------------------------------- structure: every item checked
total = sum(len(v) for v in Q.values())
errs = jee_kit.check_all()
errs = [e for e in errs if e.startswith("maths")]
print(f"jee_maths_check: {n_ok}/{total} answers recomputed and confirmed")
for e in errs:
    print("KIT:", e)
for f_ in fails:
    print("FAIL:", f_)
if n_ok != total:
    print(f"FAIL: {total - n_ok} items not confirmed")
sys.exit(1 if (fails or errs or n_ok != total) else 0)
