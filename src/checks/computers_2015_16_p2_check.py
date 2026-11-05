"""Checks for Computer Science pre-board 2015-16 Paper 2 (Practical): every program
compiled and run on the paper's own examples plus extra inputs; the paper's sample
outputs are asserted, and independently re-derived in Python (spiral, calendar, cipher)."""
import os, sys, calendar
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cs_b_java import run
fails = 0

def spiral(n):
    m = [[0] * n for _ in range(n)]; k = 1
    for r in range((n + 1) // 2):
        lo, hi = r, n - 1 - r
        if lo == hi: m[lo][lo] = k; break
        cells = ([(lo, j) for j in range(lo, hi + 1)] + [(i, hi) for i in range(lo + 1, hi + 1)] +
                 [(hi, j) for j in range(hi - 1, lo - 1, -1)] + [(i, lo) for i in range(hi - 1, lo, -1)])
        if r % 2: cells = [(c, r_) for r_, c in cells]     # transpose = reverse direction from top-left
        for i, j in cells: m[i][j] = k; k += 1
    return "\n".join("".join("%4d" % v for v in row) for row in m)

PAPER = {4: [[1,2,3,4],[12,13,16,5],[11,14,15,6],[10,9,8,7]],
         5: [[1,2,3,4,5],[16,17,24,23,6],[15,18,25,22,7],[14,19,20,21,8],[13,12,11,10,9]],
         6: [[1,2,3,4,5,6],[20,21,32,31,30,7],[19,22,33,34,29,8],[18,23,36,35,28,9],[17,24,25,26,27,10],[16,15,14,13,12,11]]}
for n, mat in PAPER.items():
    exp = "\n".join("".join("%4d" % v for v in row) for row in mat)
    if spiral(n) != exp: print("FAIL python spiral", n); fails += 1

def cal(month):
    import datetime
    first = datetime.date(2015, month, 1)
    assert month != 1 or first.weekday() == 3          # 1 Jan 2015 was a Thursday
    start = (first.weekday() + 1) % 7                 # Sunday = 0
    nd = calendar.monthrange(2015, month)[1]
    cells = [""] * start + [str(d) for d in range(1, nd + 1)]
    while len(cells) % 7: cells.append("*")
    rows = ["".join("%-7s" % h for h in ["Sun", "Mon", "Tues", "Wed", "Thrus", "Fri", "Sat"])]
    for i in range(0, len(cells), 7): rows.append("".join("%-7s" % c for c in cells[i:i + 7]))
    return "\n".join(rows)

def merge(a, b):
    L = max(len(a), len(b))
    return "".join((a[i] if i < len(a) else "*") + (b[i] if i < len(b) else "*") for i in range(L))
def enc(s):
    w = s.rstrip(".?!").split(); n = len(w)
    out = [merge(w[i], w[n - 1 - i]) for i in range(n // 2)]
    if n % 2: out.append("*" + w[n // 2][::-1] + "*")
    return " ".join(out)
assert enc("THE DOG JUMPS OVER THE BLACK CAT.") == "TCHAET DBOLGA*C*K JTUHMEP*S* *REVO*"
assert enc("ASHOK IS AN INDIAN") == "AISNHDOIKA*N IASN"

M = "computers_2015_16_p2"
fails += run(M, [
    ("spiral4", "CircularMatrix.java", "4\n", [spiral(4)]),
    ("spiral5", "CircularMatrix.java", "5\n", [spiral(5)]),
    ("spiral6", "CircularMatrix.java", "6\n", [spiral(6)]),
    ("spiral7", "CircularMatrix.java", "7\n", [spiral(7)]),
    ("cal_jan", "Calendar2015.java", "January\n", [cal(1)]),
    ("cal_mar", "Calendar2015.java", "March\n", [cal(3)]),
    ("cal_sep", "Calendar2015.java", "September\n", [cal(9)]),
    ("cal_feb", "Calendar2015.java", "February\n", [cal(2)]),
    ("cal_bad", "Calendar2015.java", "Smarch\n", ["INVALID MONTH NAME"]),
    ("enc1", "MergeCipher.java", "2\nTHE DOG JUMPS OVER THE BLACK CAT.\n", ["TCHAET DBOLGA*C*K JTUHMEP*S* *REVO*"]),
    ("dec1", "MergeCipher.java", "1\nTCHAET DBOLGA*C*K JTUHMEP*S* *REVO*\n", ["THE DOG JUMPS OVER THE BLACK CAT"]),
    ("enc2", "MergeCipher.java", "2\nASHOK IS AN INDIAN\n", ["AISNHDOIKA*N IASN"]),
    ("dec2", "MergeCipher.java", "1\nAISNHDOIKA*N IASN\n", ["ASHOK IS AN INDIAN"]),
    ("enc3", "MergeCipher.java", "2\nWE LOVE JAVA PROGRAMMING.\n", [enc("WE LOVE JAVA PROGRAMMING.")]),
    ("dec3", "MergeCipher.java", "1\n" + enc("WE LOVE JAVA PROGRAMMING.") + "\n", ["WE LOVE JAVA PROGRAMMING"]),
    ("enc4", "MergeCipher.java", "2\nCOMPUTER\n", ["*RETUPMOC*"]),
])
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
