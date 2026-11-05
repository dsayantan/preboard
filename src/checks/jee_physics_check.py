"""Recompute every numerical answer of the Physics JEE mock tests (src/jee/physics_t{1,2,3}.py).

For each numerical MCQ: the value(s) printed in the correct option must equal the value computed
here from the question data (to 1 %), and no distractor may carry the same value(s).
For conceptual MCQs: the chosen option must be the expected one (matched by a key phrase).
For each integer (NUM) question: the computed value must round to the stated answer and lie within
0.05 of it (so "nearest integer" is unambiguous).

    python3 src/checks/jee_physics_check.py
"""
import os, re, sys, math

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
sys.path[:0] = [SRC]
import jee_kit  # noqa: E402  (sets up sys.path for data/, figs/, jee/)

pi, sqrt = math.pi, math.sqrt
k = 9e9
eps0 = 8.85e-12
mu0 = 4 * pi * 1e-7
e = 1.6e-19
hc_eVnm = 1240.0
deg = math.radians

FAILS = []


def nums(html):
    """All numbers printed in an option, with a x 10^{n} folded in; unit exponents dropped."""
    s = html.replace(r"\(", " ").replace(r"\)", " ")
    s = re.sub(r"(\d+(?:\.\d+)?)\s*\\times\s*10\^\{(-?\d+)\}", lambda m: f" {m.group(1)}e{m.group(2)} ", s)
    s = re.sub(r"(?<![\d.e])10\^\{(-?\d+)\}", lambda m: f" 1e{m.group(1)} ", s)
    s = re.sub(r"\^\{[^}]*\}|\^\d", " ", s)       # unit powers such as m^{-1}, m^2
    s = re.sub(r"\\sqrt\{?(\d+(?:\.\d+)?)\}?", lambda m: f" {sqrt(float(m.group(1)))} ", s)
    return [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?(?:e-?\d+)?", s)]


def close(a, b, rel=0.01):
    return abs(a - b) <= rel * max(abs(a), abs(b), 1e-300)


def same(t1, t2):
    return len(t1) == len(t2) and all(close(a, b) for a, b in zip(t1, t2))


def chk_value(tag, x, want, key=None):
    """want: a number or a tuple of numbers expected (in order) in the correct option.
    key: a phrase that must also be in the correct option (direction, nature); a distractor then
    equals the answer only if it has the same numbers AND the phrase."""
    if key is not None and key not in x["options"][x["answer"]]:
        FAILS.append(f"{tag}: correct option lacks {key!r}")
    want = tuple(want) if isinstance(want, (tuple, list)) else (want,)
    got = tuple(nums(x["options"][x["answer"]])[:len(want)])
    if not same(got, want):
        FAILS.append(f"{tag}: correct option shows {got}, computed {want}")
    for i, o in enumerate(x["options"]):
        if i != x["answer"] and same(tuple(nums(o)[:len(want)]), want) and (key is None or key in o):
            FAILS.append(f"{tag}: distractor {i} equals the answer {want}: {o}")
    return want


def chk_key(tag, x, key):
    if key not in x["options"][x["answer"]]:
        FAILS.append(f"{tag}: correct option {x['options'][x['answer']]!r} lacks {key!r}")
    for i, o in enumerate(x["options"]):
        if i != x["answer"] and o == x["options"][x["answer"]]:
            FAILS.append(f"{tag}: duplicate option")


def chk_num(tag, x, val):
    if x["kind"] != "num":
        FAILS.append(f"{tag}: expected an integer question")
    if round(val) != x["answer"] or abs(val - x["answer"]) > 0.05:
        FAILS.append(f"{tag}: computed {val}, answer {x['answer']}")


def lens_v(f, u):                       # 1/v - 1/u = 1/f
    return 1 / (1 / f + 1 / u)


# ---------------------------------------------------------------------------------- test 1
def t1():
    out = {}
    out[1] = ("v", (2 * 60) / (1 + 5))                                   # 20 V
    out[2] = ("v", math.hypot(40e-6 * 10, 15e-9 * 2e4))                  # 5e-4 N
    out[3] = ("k", "potential difference doubles, stored energy doubles")
    out[4] = ("v", 12 / (15 + 90 * 10 / 100))                            # 0.5 A
    out[5] = ("v", 2 * (1 / 0.5) ** 2)                                   # 8 (v)
    out[6] = ("k", "1:1")
    # r_alpha/r_p = sqrt(4)/2 = 1 : confirm
    assert close(sqrt(2 * 4 * 1) / 2 / (sqrt(2 * 1 * 1) / 1), 1)
    out[7] = ("k", r"(\pi+1)")
    out[8] = ("v", 4 * 0.02 / (5 - 1) * 1e3)                             # 20 mH
    Z = math.hypot(80, 100 - 40); I0 = 200 / Z
    assert close(Z, 100)
    out[9] = ("v", I0 * (80 + 100 + 40))                                 # 440 V
    out[10] = ("vk", (3e8 / 3e-2, "microwaves"))                         # 1e10 Hz, microwaves
    out[11] = ("v", 4 / 3 * 30)                                          # 40 cm
    # real image, m = v/u = -2
    u = -30.0; assert close(lens_v(20, u) / u, -2)
    out[12] = ("v", 30)
    A, dm = 60, 30
    out[13] = ("v", math.sin(deg((A + dm) / 2)) / math.sin(deg(A / 2)))  # sqrt2
    r = sqrt(9); a1 = (r + 1) / (r - 1)                                   # a1/a2
    out[14] = ("v", (a1 ** 2, 1))                                         # 4 : 1
    out[15] = ("v", hc_eVnm / 310 - 2.2)                                  # 1.8 V
    lam = 1 / (1.097e7 * (1 / 9 - 1 / 16)); assert 7e-7 < lam < 1e-5     # infrared
    out[16] = ("k", "Paschen")
    dm_ = 2 * 1.007276 + 2 * 1.008665 - 4.001506
    out[17] = ("v", dm_ * 931 / 4)                                        # 7.07 MeV
    assert 10 * 600 / 800 > 6
    out[18] = ("v", ((10 - 6) / 200 - 6 / 600) * 1e3)                     # 10 mA
    out[19] = ("k", "both decrease")
    B, l, v, R = 0.2, 0.5, 4, 2
    out[20] = ("v", B * (B * l * v / R) * l)                              # 0.02 N
    q2 = k * (10e-6) ** 2
    out[21] = ("n", q2 / 0.05 - q2 / 0.10)                                # 9 J
    out[22] = ("n", (100 * 4) / 4 / 4)                                    # 25 ohm
    out[23] = ("n", 10 / 5e-3 - 40)                                       # 1960 ohm
    out[24] = ("n", 1e-3 * 0.135e-3 / 0.25 * 1e9)                         # 540 nm
    out[25] = ("n", 4.14e-15 * 1.45e15)                                   # 6 eV
    return out


# ---------------------------------------------------------------------------------- test 2
def t2():
    out = {}
    out[1] = ("k", r"\sqrt3")
    assert close(sqrt(1 + 1 + 2 * math.cos(deg(60))), sqrt(3))
    C1, C2, V1 = 4e-6, 2e-6, 300
    Vc = C1 * V1 / (C1 + C2)
    out[2] = ("v", 0.5 * C1 * V1 ** 2 - 0.5 * (C1 + C2) * Vc ** 2)        # 0.06 J
    out[3] = ("v", 2e-6 / (6 * eps0))                                     # 3.77e4
    out[4] = ("v", 1.5 * 110 / 75)                                        # 2.2 V
    X = 3 * 40 / 60
    assert close(X, 2)
    out[5] = ("k", r"\(1\ \Omega\) in series")                            # need 3 - X = 1 ohm in series
    assert close(3 - X, 1)
    out[6] = ("k", r"\(4B\)")
    assert close((2 / (1 / 2)) / (1 / 1), 4)                              # N/R ratio
    Bsel = 5e4 / 2e6
    out[7] = ("vk", (Bsel, "into the page"))                              # 0.025 T, into
    out[8] = ("v", mu0 * 4000 * 2.5 * 1e3)                                # 12.6 mT
    Xc = 1 / (2 * pi * 50 * (100e-6 / pi))
    out[9] = ("v", 220 / Xc)                                              # 2.2 A
    out[10] = ("k", r"inductor and \(Y = P\)")
    out[11] = ("k", "X-rays, ultraviolet, infrared, microwaves")
    out[12] = ("vk", (1 / ((1 / 1.5 - 1) * (1 / 20 - 1 / -20)), "diverging"))  # -30 cm
    out[13] = ("v", (90 + 10, 90 / 10))                                   # 100 cm, 9
    out[14] = ("k", r"\(7I\)")
    assert close(1 + 4 + 2 * sqrt(4) * math.cos(pi / 3), 7)
    out[15] = ("v", 600e-9 / math.sin(deg(30)) * 1e6)                     # 1.2 um
    out[16] = ("v", (3e8 / 5e14 * 1e9, 6.6e-34 * 5e14 / e))               # 600 nm, 2.06 eV
    out[17] = ("v", (6.6e-34 * 3e8 / 660e-9, 6.6e-34 / 660e-9))           # 3e-19 J, 1e-27
    out[18] = ("k", r"\(4\pi a_0\)")
    assert close(2 * pi * (2 ** 2) / 2, 4 * pi)
    out[19] = ("k", "n-type, with electrons")
    out[20] = ("v", 2 * 50)                                               # 100 Hz
    C0 = eps0 * 100e-4 / 0.885e-3
    out[21] = ("n", 0.5 * 5 * C0 * 200 ** 2 * 1e6)                        # 10 uJ
    out[22] = ("n", 20 * (0.5 / 2) / 1)                                   # R/4 -> 5 min
    assert close(1 / (1 / 0.5 + 1 / 0.5), 0.25)
    out[23] = ("n", 220 ** 2 / 50)                                        # 968 W
    h = 2 * sqrt(7); C = math.asin(3 / 4)
    out[24] = ("n", h * math.tan(C))                                      # 6 cm
    out[25] = ("n", 2e-6 * (3e8) ** 2 / 1e10)                             # 18
    return out


# ---------------------------------------------------------------------------------- test 3
def t3():
    out = {}
    out[1] = ("k", r"\(n^2\)")
    n_ = 7; assert close((n_ * 1.0) / (1.0 / n_), n_ ** 2)
    Cs = 2 * 6 / 8
    out[2] = ("v", Cs * 160 / 2)                                          # 120 V
    pE = 2e-8 * 5e3
    out[3] = ("v", pE * (1 - math.cos(deg(120))))                         # 1.5e-4 J
    out[4] = ("v", 5 * 6 / (6 + 9))                                       # 2 A
    out[5] = ("k", "number density of free electrons")
    out[6] = ("k", r"\sqrt{m_e/m_p}")
    out[7] = ("v", (2 / 1 ** 3) / (1 / 2 ** 3))                           # 16
    Ig = 30 / 5
    out[8] = ("v", Ig * (1 + 45 / 5))                                     # 60 mA
    XL = 2 * pi * 50 * 2 / pi; XC = 1 / (2 * pi * 50 * 100e-6 / pi)
    assert close(math.degrees(math.atan((XL - XC) / 100)), 45) and XL > XC
    out[9] = ("k", r"lags the applied emf by \(45^\circ\)")
    out[10] = ("v", (5 * sqrt(2) / sqrt(2)) ** 2 * 20)                    # 500 W
    out[11] = ("k", "ultraviolet")
    out[12] = ("f", (1.5 / 1.25 - 1) / (1.5 - 1))                         # 2/5
    out[13] = ("vk", (1 / (1 / 20 + 1 / -30), "converging"))              # +60 cm, converging
    out[14] = ("v", 0.20 / (4 / 3))                                       # 0.15 deg
    out[15] = ("v", 2 * math.degrees(math.asin(500e-9 / 1e-6)))           # 60 deg
    out[16] = ("k", r"\(\lambda/2\)")
    assert close(1 / sqrt(4), 0.5)
    out[17] = ("v", hc_eVnm / 248 - 1.3)                                  # 3.7 eV
    out[18] = ("v", hc_eVnm / 0.511e6 * 1e3)                              # 2.43 pm
    out[19] = ("k", "indium")
    out[20] = ("k", "alternate half-cycles and the output pulses at 100 Hz")
    Cser = 1 / (1 / 8 + 1 / 16 + 1 / 24)
    out[21] = ("n", Cser * 110 / 24)                                      # 20 V
    out[22] = ("n", 8 * 2.5 + 3)                                          # 23 A
    out[23] = ("n", 0.2 * 0.5 * 10 / 4 * 1e3)                             # 250 mA
    v = lens_v(10, -15)
    out[24] = ("n", (v - 20) / 2)                                         # f = R/2, R = v - 20 = 10
    out[25] = ("n", (3 ** 2) / (1 ** 2))                                  # 9
    return out


# ------------------------------------------------------------------ review fixes (review_jee_physics.md)
POSITIONAL = re.compile(r"\b(first|second|third|fourth|last)\s+(option|sequence|choice|answer)\b"
                        r"|\boption\s*\(?[A-Da-d1-4]\)?(?![A-Za-z])|\(\s*[a-d]\s*\)\s*is", re.I)


def review_checks():
    """Pin the fixes made in the independent review.  Options are rotated at build time (_mcq),
    so a solution may name an option only by its content, never by position or letter."""
    from importlib import import_module
    Q = {t: import_module(f"physics_t{t}").QUESTIONS for t in (1, 2, 3)}
    for t in (1, 2, 3):
        for i, x in enumerate(Q[t], 1):
            m = POSITIONAL.search(re.sub(r"<[^>]+>", " ", x["sol"]))
            if m:
                FAILS.append(f"physics T{t} Q{i}: solution refers to an option by position: {m.group(0)!r}")

    def has(t, n, phrase):
        if phrase not in Q[t][n - 1]["sol"] + Q[t][n - 1]["q"]:
            FAILS.append(f"physics T{t} Q{n}: expected text {phrase!r}")

    def opt(t, n, val):
        if not any(any(close(v, val) for v in nums(o)) for o in Q[t][n - 1]["options"]):
            FAILS.append(f"physics T{t} Q{n}: no option carries slip value {val}")

    # T2 Q6: R doubled with N = 1 gives B/2; N and R both doubled gives B
    assert close((1 / 2) / 1, 0.5) and close((2 / 2) / 1, 1)
    has(2, 6, r"\(B/2\) doubles the radius and forgets the extra turn")
    # T3 Q7: inverse-square with the factor 2 gives 8 (the other distractor); without it, 4
    assert close((2 / 1 ** 2) / (1 / 2 ** 2), 8) and close((1 / 1 ** 2) / (1 / 2 ** 2), 4)
    has(3, 7, "inverse-square law and also drops the factor 2")
    # T3 Q16: lambda ~ 1/sqrt(H); 2H gives lambda/sqrt2
    assert close(1 / sqrt(2), 2 ** -0.5)
    has(3, 16, r"height of \(2H\)")
    # T3 Q8: 5 div per mA is a sensitivity; figure of merit is 0.2 mA/div; 30 x 5 = 150 slip
    has(3, 8, "figure of merit 0.2 mA per division")
    opt(3, 8, 30 * 5); opt(3, 8, 30 / 5 * (1 + 5 / 45))
    # T3 Q23 figure: field label must not read as the rail end "B"
    import physics_figs
    svg = physics_figs.fig_jp_t3_rails()
    if "B (into page)" in svg or "0.2 T" not in svg:
        FAILS.append("fig_jp_t3_rails: field label clashes with rail end B / lacks 0.2 T")


def main():
    from importlib import import_module
    total = 0
    for t, spec in ((1, t1()), (2, t2()), (3, t3())):
        Q = import_module(f"physics_t{t}").QUESTIONS
        assert len(spec) == 25 and sorted(spec) == list(range(1, 26)), f"T{t}: spec incomplete"
        for n in range(1, 26):
            x, (kind, val) = Q[n - 1], spec[n]
            tag = f"physics T{t} Q{n}"
            if kind == "n":
                chk_num(tag, x, val)
            elif kind == "k":
                if x["kind"] != "mcq":
                    FAILS.append(f"{tag}: expected an MCQ")
                chk_key(tag, x, val)
            else:
                if x["kind"] != "mcq":
                    FAILS.append(f"{tag}: expected an MCQ")
                opts = x["options"]
                if kind == "f":
                    # fractional options a/b: evaluate each
                    vals = []
                    for o in opts:
                        m = re.search(r"(\d+)\s*/\s*(\d+)", o)
                        vals.append(int(m.group(1)) / int(m.group(2)) if m else None)
                    want = val[0] if isinstance(val, tuple) else val
                    if vals[x["answer"]] is None or not close(vals[x["answer"]], want):
                        FAILS.append(f"{tag}: correct fraction {vals[x['answer']]} != {want}")
                    for i, w in enumerate(vals):
                        if i != x["answer"] and w is not None and close(w, want):
                            FAILS.append(f"{tag}: distractor {i} equals the answer")
                elif kind == "vk":
                    chk_value(tag, x, val[0], val[1])
                else:
                    chk_value(tag, x, val)
            total += 1
    review_checks()
    print("\n".join(FAILS) if FAILS else f"jee_physics_check: {total} questions checked, all pass")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
