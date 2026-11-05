"""Recompute every numerical result in the JEE Chemistry mock tests (src/jee/chemistry_t{1,2,3}.py).

    python3 src/checks/jee_chemistry_check.py

* MCQ with a numerical answer: the value is recomputed from the question data; the number printed in
  the option marked correct must agree with it (within half a unit of its last printed digit, or 0.6%),
  and no distractor may agree with it (each must differ by more than 2%).
* NUM: the recomputed value must round to the stored integer and be at least 0.1 away from a .5 tie.
* Conceptual MCQ: the stored index is asserted (and the supporting data, e.g. pKa/pKb orders, checked).
* Every \\ce{} equation in the questions/solutions that is written as a balanced equation is checked
  for atom and charge balance (schemes with reagents/[O]/[H] or lettered unknowns are listed in SKIP).
* Each solution's closing "Answer: (n)" must name the stored option.
"""
import os, re, sys, math
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
for p in (SRC, os.path.join(SRC, "jee"), os.path.join(SRC, "data"), os.path.join(SRC, "figs"), HERE):
    if p not in sys.path:
        sys.path.insert(0, p)

import jee_kit
from chem_balance_1517 import _ce_blocks, ARROW, _side

FAIL = []
T = {t: jee_kit.load("chemistry", t) for t in (1, 2, 3)}
F, R = 96500.0, 8.314
log = math.log10


def say(ok, msg):
    print(("ok  " if ok else "BAD ") + msg)
    if not ok:
        FAIL.append(msg)


# ------------------------------------------------------------------ option parsing
def nums(s):
    """All numbers in an option, in order; a×10^{b} read as one number; '19\\,040' as 19040."""
    s = s.replace(r"\,", "").replace("&minus;", "-").replace("−", "-")
    out = []
    for m in re.finditer(r"([+-]?\d+(?:\.\d+)?)(\s*\\times\s*10\^\{?([+-]?\d+)\}?)?", s):
        v = float(m.group(1))
        if m.group(3):
            v *= 10 ** int(m.group(3))
        out.append((v, m.group(1)))
    return out


def agrees(printed, txt, val):
    d = len(txt.split(".")[1]) if "." in txt else 0
    half = 0.5 * 10 ** (-d)
    # scale half-unit by the power of ten when the option is written a×10^b
    if printed != 0 and float(txt) != 0:
        half *= abs(printed / float(txt))
    return abs(printed - val) <= half * 1.01 or abs(printed - val) <= 0.006 * abs(val)


def mcq_value(t, n, val, k=0, label=""):
    """Question n (1-based within the test) — option values compared at number position k."""
    x = T[t][n - 1]
    assert x["kind"] == "mcq"
    for i, o in enumerate(x["options"]):
        v, txt = nums(o)[k]
        if i == x["answer"]:
            say(agrees(v, txt, val), f"T{t} Q{n} {label}: computed {val:.6g}, correct option prints {v:.6g}")
        else:
            say(abs(v - val) > 0.02 * abs(val), f"T{t} Q{n}: distractor {v:.6g} differs from {val:.6g}")


def mcq_index(t, n, idx, why=""):
    x = T[t][n - 1]
    say(x["kind"] == "mcq" and x["answer"] == idx, f"T{t} Q{n} conceptual: answer index {x['answer']} == {idx} {why}")


def num_ans(t, n, val, label=""):
    x = T[t][n - 1]
    r = round(val)
    say(x["kind"] == "num" and x["answer"] == r and abs(val - r) < 0.4,
        f"T{t} Q{n} NUM {label}: computed {val:.5g} -> {r}, stored {x['answer']}")


def balanced(eq):
    parts = [x for i, x in enumerate(ARROW.split(eq)) if i % 4 == 0]
    L, ql = _side(parts[0]); Rr, qr = _side(parts[-1])
    return L == Rr and ql == qr


# ================================================================== Test 1
t = 1
xB = (1 / 78) / (1 / 78 + 1 / 92)
mcq_value(t, 1, 45 + (150 - 45) * xB, label="VP equal masses benzene/toluene")
mcq_index(t, 2, 2, "(i rises towards 3 on dilution)")
mcq_value(t, 3, 1.52 - 0.0591 / 6 * log(0.1 ** 2 / 0.001 ** 3), label="emf Al/Sn")
mcq_value(t, 4, 9.65 * 1000 / F / 2 * 137, label="mass Ba")
k = 0.693 / 20
mcq_value(t, 5, 2.303 / k * log(100 / 0.1), label="t99.9%")
# E/500 = (E-20)/400  ->  E = 20*500/(500-400)
mcq_value(t, 6, 20 * 500 / (500 - 400), label="Ea uncatalysed")
mcq_index(t, 7, 1); mcq_index(t, 8, 3)
mcq_value(t, 9, math.sqrt(4 * 6), label="mu [CoF6]3- (d6 high spin, n=4)")
mcq_index(t, 10, 2); mcq_index(t, 11, 3); mcq_index(t, 12, 1)
pKa = {"p-cresol": 10.26, "phenol": 9.99, "m-nitrophenol": 8.36, "p-nitrophenol": 7.15}
say(sorted(pKa, key=pKa.get, reverse=True) == ["p-cresol", "phenol", "m-nitrophenol", "p-nitrophenol"],
    "T1 Q13 increasing acidity = decreasing pKa order")
mcq_index(t, 13, 0); mcq_index(t, 14, 2); mcq_index(t, 15, 3)
pKa2 = {"o": 2.98, "m": 4.08, "benzoic": 4.20, "p": 4.58}
say(sorted(pKa2, key=pKa2.get) == ["o", "m", "benzoic", "p"], "T1 Q16 decreasing acidity order from pKa")
mcq_index(t, 16, 1); mcq_index(t, 17, 0)
pKb = {"m": 11.55, "p": 13.0, "o": 14.28}
say(sorted(pKb, key=pKb.get) == ["m", "p", "o"], "T1 Q18 basicity order from pKb")
mcq_index(t, 18, 2); mcq_index(t, 19, 3); mcq_index(t, 20, 1)
i = 1.88 / (0.52 * 2)
num_ans(t, 21, (i - 1) * 100, "alpha% NaCl")
Lm = 1000 * 7.896e-5 / 0.00241; a = Lm / 390
num_ans(t, 22, 0.00241 * a * a / (1 - a) * 1e7, "Ka x1e7")
num_ans(t, 23, 2.303 * R * 350 * 410 * log(6) / 60 / 1000, "Ea kJ")
eq = "MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O"
say(balanced(eq), f"T1 Q24 balanced: {eq}")
num_ans(t, 24, 1 + 5 + 8 + 1 + 5 + 4, "sum of coefficients")
num_ans(t, 25, 250 * 0.02 * 1, "mmol AgCl ([CrCl2(H2O)4]Cl, 1 ionisable Cl)")

# ================================================================== Test 2
t = 2
mcq_value(t, 1, 10.2 * 180 / 20, label="M glycerine")
mcq_index(t, 2, 2)
mcq_value(t, 3, -2 * F * (0.80 - (-0.25)) / 1000, label="dG Ni/Ag kJ")
mcq_value(t, 4, (2.800 + 2 * 2.481 - 2 * 1.265) * 1e-2, label="Lambda Ba(OH)2")
# rate data: orders from the table, then k for each option's rate law
r1, r2, r3 = 6.0e-3, 1.2e-2, 4.8e-2
x = math.log(r2 / r1, 2); y = math.log(r3 / r2 / 2 ** x, 2)
kk = r1 / (0.20 * 0.05)
say(abs(x - 1) < 1e-9 and abs(y - 1) < 1e-9 and abs(kk - 0.6) < 1e-9, f"T2 Q5 orders {x:.3g},{y:.3g}; k = {kk:.3g}")
opts = T[2][4]["options"]
say(T[2][4]["answer"] == 0 and "0.6" in opts[0], "T2 Q5 correct option carries rate = k[NO2][F2], k = 0.6")
for o, kv in zip(opts[1:], (r1 / (0.2 ** 2 * 0.05), r1 / 0.2, r1 / (0.2 * 0.05 ** 2))):
    say(abs(float(re.search(r"k = ([\d.]+)", o).group(1)) - kv) < 1e-6 * kv and abs(kv - kk) > 0.02 * kk, f"T2 Q5 distractor k {kv:.3g} matches its law and differs from 0.6")
mcq_value(t, 6, 2.303 / (0.693 / 5730) * log(10), label="age 14C")
mcq_index(t, 7, 3); mcq_index(t, 8, 2)
say(abs(4 * -0.4 - (-1.6)) < 1e-12, "T2 Q9 CFSE t2g4 = -1.6 Do (+P)")
mcq_index(t, 9, 1); mcq_index(t, 10, 0); mcq_index(t, 11, 2); mcq_index(t, 12, 3)
mcq_index(t, 13, 2); mcq_index(t, 14, 3); mcq_index(t, 15, 0)
mcq_value(t, 16, 2 * 2, label="aldols: 2 enolisable donors x 2 acceptors")
mcq_index(t, 17, 0); mcq_index(t, 18, 3)
pKb2 = {"(CH3)2NH": 3.27, "CH3NH2": 3.38, "(CH3)3N": 4.22, "NH3": 4.75}
say(sorted(pKb2, key=pKb2.get) == ["(CH3)2NH", "CH3NH2", "(CH3)3N", "NH3"], "T2 Q19 aqueous basicity order from pKb")
mcq_index(t, 19, 1)
mcq_value(t, 20, (52.5 + (-92.4)) / 2, label="[alpha] invert sugar")
i = 7 / (14 * 75.2 / 94)
num_ans(t, 21, (1 - i) * 2 * 100, "% phenol dimerised")
num_ans(t, 22, 5 * 7200 / (2 * F) * 58.7, "g Ni")
num_ans(t, 23, 3500 * 2.303 * R / 1000, "Ea kJ from slope")
eq = "2KMnO4 + 5H2C2O4 + 3H2SO4 -> K2SO4 + 2MnSO4 + 10CO2 + 8H2O"
say(balanced(eq), f"T2 Q24 balanced: {eq}")
num_ans(t, 24, 50 * 0.05 * 2 / 5 / 0.02, "mL KMnO4")
unp = {"Cr3+": 3, "Fe2+": 4, "Cu2+": 1, "Zn2+": 0}
d = {"Cr3+": 3, "Fe2+": 6, "Cu2+": 9, "Zn2+": 10}
hs = lambda n: n if n <= 5 else 10 - n          # high-spin octahedral unpaired count
say(all(hs(d[k]) == v for k, v in unp.items()), "T2 Q25 high-spin unpaired counts")
num_ans(t, 25, sum(unp.values()), "total unpaired")

# ================================================================== Test 3
t = 3
mcq_value(t, 1, 1000 * 3.63 * 6.21 / ((68.04 - 61.70) * 24.0), label="M from bp elevation")
mcq_index(t, 2, 1)
E = 0.059 * log(0.1 / 0.001)
x = T[3][2]
say(agrees(nums(x["options"][x["answer"]])[0][0], nums(x["options"][x["answer"]])[0][1], E)
    and "0.001 M side to the 0.1 M side" in x["options"][x["answer"]],
    f"T3 Q3 conc cell: {E:.3f} V, electrons dilute -> concentrated")
for i_, o in enumerate(x["options"]):
    if i_ != x["answer"]:
        v = nums(o)[0][0]
        say(abs(v - E) > 0.02 * E or "0.1 M side to the 0.001 M side" in o,
            f"T3 Q3 distractor '{o[:40]}' differs in value or direction")
z = (4.0 * 45 * 60 / F) / (2.977 / 106.4)
mcq_value(t, 4, z, label="charge on metal ion")
kq = 0.10 / (0.20 * 0.05)
X, Y = 0.40 / (kq * 0.05), 0.80 / (kq * 0.40)
mcq_value(t, 5, X, k=0, label="X");
xo = T[3][4]
say(abs(nums(xo["options"][xo["answer"]])[1][0] - Y) < 1e-9, f"T3 Q5 Y = {Y:.3g} in the correct option")
say(all((abs(nums(o)[0][0] - X) > 1e-9 or abs(nums(o)[1][0] - Y) > 1e-9) for j, o in enumerate(xo["options"]) if j != xo["answer"]),
    "T3 Q5 no distractor has both X and Y right")
n_order = 1 - (-2)          # units (mol L-1)^(1-n) s-1 with exponent -2
mcq_value(t, 6, 2 ** n_order, label="rate factor (third order)")
mcq_index(t, 7, 0)
eq = "2MnO4- + 10I- + 16H+ -> 2Mn^2+ + 5I2 + 8H2O"
say(balanced(eq), f"T3 Q8 balanced: {eq}")
mcq_value(t, 8, 5 / 2, label="mol I2 per mol KMnO4")
for n_, idx in ((9, 1), (10, 0), (11, 2), (12, 3), (13, 1), (14, 1), (15, 3), (16, 1), (17, 0), (18, 3), (19, 3), (20, 2)):
    mcq_index(t, n_, idx)
i = 0.320 / (1.86 * 0.0711)
num_ans(t, 21, (i - 1) / 2 * 100, "alpha% Na2SO4")
num_ans(t, 22, 1000 * 1.65e-4 / 0.01 / (349.1 + 40.9) * 100, "alpha% acetic acid")
num_ans(t, 23, 2.303 * R * 298 * 308 / 10 * log(1.75) / 1000, "Ea from temperature coefficient")
eq = "K2Cr2O7 + 6FeSO4 + 7H2SO4 -> K2SO4 + Cr2(SO4)3 + 3Fe2(SO4)3 + 7H2O"
say(balanced(eq), f"T3 Q24 balanced: {eq}")
num_ans(t, 24, 25 * 0.12 / 6 / 0.05, "mL dichromate")
num_ans(t, 25, 5 * (5 + 2), "mu^2 [FeCl4]- (d5, 5 unpaired)")

# ================================================================== every \ce equation shown
SKIP = {
    # schemes / unbalanced-by-design (reagents on the arrow, [O]/[H], conversion chains)
    r"(CH3)2CHOH ->[P/I2] (CH3)2CHI ->[Mg] (CH3)2CHMgI": "conversion chain (reagents on arrows)",
    r"(CH3)2CHMgI + HCHO -> (CH3)2CHCH2OMgI ->[H3O+] (CH3)2CHCH2OH": "Grignard chain; second step is hydrolysis (H2O on arrow)",
    r"CH3CH2CN ->[H3O+] CH3CH2COOH": "hydrolysis written as a conversion",
    r"C6H5CH3 ->[CrO2Cl2/CCl4][H3O+] C6H5CHO": "Etard reaction written as a conversion",
    r"C6H5COOH + NH3 -> C6H5COONH4 ->[\Delta] C6H5CONH2 + H2O": None,   # balanced: checked
    r"CH3CH2CH2NC + 4[H] -> CH3CH2CH2NHCH3": None,
    r"MnO4- + Fe^2+ + H+ -> Mn^2+ + Fe^3+ + H2O": "skeleton printed in the question for the student to balance (balanced form checked above)",
    r"A + B -> products": "rate-law prompt, not an equation",
    r"R-NH2 -> R-N#C": "schematic (R group) in prose",
}
eqs_ok, eqs_skip = 0, []
for t in (1, 2, 3):
    for n_, x in enumerate(T[t], 1):
        for txt in [x["q"], x["sol"]] + x["options"]:
            for ce in _ce_blocks(txt):
                if not ARROW.search(ce):
                    continue
                parts = [p_ for j, p_ in enumerate(ARROW.split(ce)) if j % 4 == 0]
                if not parts[-1].strip() or any(re.fullmatch(r"\s*[A-E]\s*", p_) for p_ in parts):
                    eqs_skip.append((t, n_, ce, "prompt / lettered unknowns")); continue
                if SKIP.get(ce):
                    eqs_skip.append((t, n_, ce, SKIP[ce])); continue
                bad = []
                for lhs, rhs in zip(parts, parts[1:]):
                    try:
                        L, ql = _side(lhs); Rr, qr = _side(rhs)
                    except Exception as e:
                        bad.append(f"parse {e}"); continue
                    if not (L == Rr and ql == qr):
                        bad.append(f"{lhs.strip()} -> {rhs.strip()}: {dict(L - Rr)} | {dict(Rr - L)} q {ql}/{qr}")
                if bad:
                    say(False, f"T{t} Q{n_} equation not balanced: {ce}  [{'; '.join(bad)}]")
                else:
                    eqs_ok += 1
print(f"ok  {eqs_ok} \\ce equations atom- and charge-balanced; {len(eqs_skip)} skipped:")
for s in eqs_skip:
    print(f"      T{s[0]} Q{s[1]}: {s[2]}  ({s[3]})")

# ================================================================== reviewer additions (review_jee_chemistry.md)
def opt_vals(t, n, k=0):
    return [nums(o)[k][0] for o in T[t][n - 1]["options"]]


def slips(t, n, claimed, k=0, tol=0.006):
    """Each distractor value must be the slip the solution names for it (index -> value)."""
    v = opt_vals(t, n, k)
    for j, val in claimed.items():
        say(abs(v[j] - val) <= tol * abs(val), f"T{t} Q{n} distractor ({j+1}) {v[j]:.4g} = named slip {val:.4g}")

slips(1, 1, {0: 45 + 105 * 78 / 170, 2: 45 + 105 * 0.5, 3: 150 * xB})
slips(1, 3, {2: 1.52 - 0.0591 / 2 * 7, 3: 1.52 + 0.0591 / 6 * 7})
slips(1, 4, {0: 0.1 * 137, 1: 0.1 / 4 * 137, 2: 0.2 * 137})
slips(2, 3, {1: -96500 * 1.05 / 1000, 2: -2 * 96500 * 0.55 / 1000, 3: -2 * 96500 * 2.10 / 1000})
slips(2, 4, {0: 2.800e-2 + 2.481e-2 - 1.265e-2, 2: 2.800e-2 + 2 * 2.481e-2 - 1.265e-2, 3: 2.800e-2 - 2 * 2.481e-2 + 2 * 1.265e-2}, tol=0.002)
slips(2, 6, {0: 2.303 / (0.693 / 5730) * log(100 / 90)}, tol=0.01)
slips(3, 1, {3: 1000 * 3.63 * 6.21 / (68.04 * 24.0)}, tol=0.01)
xo = T[3][4]["options"][3]
say(abs(nums(xo)[0][0] - 2 * X) < 1e-9 and abs(nums(xo)[1][0] - 2 * Y) < 1e-9 and "doubles both" in T[3][4]["sol"],
    "T3 Q5 option (4) is both correct values doubled, and the solution says so")
say("one-half" not in T[3][4]["sol"], "T3 Q5 no wrong 'half order' explanation for X = 1.60")
# T1 Q22: the c*alpha^2 approximation gives a different integer, so the stem must fix the formula
Lm = 1000 * 7.896e-5 / 0.00241; a_ = Lm / 390
say(round(0.00241 * a_ ** 2 * 1e7) != T[1][21]["answer"] and r"(1-\alpha)" in T[1][21]["q"],
    "T1 Q22 stem prescribes Ka = c*alpha^2/(1-alpha) (approximation would give " + str(round(0.00241 * a_ ** 2 * 1e7)) + ")")
# T1 Q15: the reused 2024-25 figure carried that paper's A-D lettering and an ethyne step not in this question
say(all(fn.__name__ != "fig_s1_q3_answer" for fn, _ in T[1][14]["sfig"]), "T1 Q15 does not reuse the lettered 2024-25 scheme")
say(any(fn.__name__ == "fig_jc_acetophenone_tests" for fn, _ in T[1][14]["sfig"]), "T1 Q15 uses fig_jc_acetophenone_tests")
# T3 Q7: actinoid ions are not smaller than lanthanoid ions
say("ions are also smaller" not in T[3][6]["sol"], "T3 Q7 no claim that actinoid ions are smaller")
# T2 Q16: the four aldols are four distinct structures
ald = {"CH3CH2CH(OH)CH(CH3)CHO", "(CH3)2CHCH(OH)C(CH3)2CHO", "(CH3)2CHCH(OH)CH(CH3)CHO", "CH3CH2CH(OH)C(CH3)2CHO"}
say(len(ald) == 4 and all(s_ in T[2][15]["sol"] for s_ in ald), "T2 Q16 four distinct aldols listed")

# ================================================================== answer line names the stored option
for t in (1, 2, 3):
    for n_, x in enumerate(T[t], 1):
        if x["kind"] == "mcq":
            m = re.search(r"Answer: \((\d)\)", x["sol"])
            say(bool(m) and int(m.group(1)) == x["answer"] + 1, f"T{t} Q{n_} 'Answer: (n)' matches stored index")
        else:
            m = re.search(r"Answer: (\d+)</b>", x["sol"])
            say(bool(m) and int(m.group(1)) == x["answer"], f"T{t} Q{n_} NUM answer line matches")

print("\nFAILED:" if FAIL else "\njee_chemistry_check: all checks pass", *FAIL, sep="\n  ")
sys.exit(1 if FAIL else 0)
