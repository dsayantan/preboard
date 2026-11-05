"""Checks for Computer Science pre-board 2016-17 Paper 1: Boolean results over all rows,
K-maps, address, RPN, traversals, dry run; every Java answer compiled and run."""
import os, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(os.path.dirname(HERE), "figs")]
from cs_b_java import run, truth
import cs_b_kit as K
import infix
KM = K.KM
fails = 0
def ok(c, msg):
    global fails
    print(("ok   " if c else "FAIL ") + msg); fails += 0 if c else 1
N = lambda x: 1 - x
# Q1(a) complement of S' + ST' is ST
ok(truth(2, lambda S, T: not (N(S) or (S and N(T)))) == truth(2, lambda S, T: S and T), "Q1a (S'+ST')' = ST")
# Q1(c) (A'+B')(B+C') = pi(1,5,6,7)
ok(set(range(8)) - truth(3, lambda A, B, C: (N(A) or N(B)) and (B or N(C))) == {1, 5, 6, 7}, "Q1c pi(1,5,6,7)")
# Q1(d) XNOR = AB + A'B'
ok(truth(2, lambda A, B: A == B) == truth(2, lambda A, B: (A and B) or (N(A) and N(B))) == {0, 3}, "Q1d XNOR")
# Q2(c) column major, arr[15][20], base arr[1][1] = 4000, arr[6][8] = 4550
W = (4550 - 4000) / ((6 - 1) + 15 * (8 - 1))
ok(W == 5, "Q2c W = %s" % W)
# Q2(e)
pf = infix.to_postfix("P+T/Q*(G*(R+K)/M*(N-J)/S)+L")[0]
ok(pf == "PTQ/GRK+*M/NJ-*S/*+L+", "Q2e " + pf)
# Q4
e, _ = KM.solve("sop", 4, [0, 1, 2, 3, 5, 8, 9, 10, 11, 13, 14, 15], list("ABCD"))
ok(e == "B' + C'D + AC", "Q4a " + e)
e, _ = KM.solve("pos", 4, [3, 4, 5, 6, 7, 9, 11, 13], list("ABCD"))
ok(e == "(B+C'+D')(A+B')(A'+C+D')", "Q4b " + e)
ok(set(range(16)) - KM.evaluate(e, 4) == {3, 4, 5, 6, 7, 9, 11, 13}, "Q4b evaluates back")
# Q5(a) I = EG + FGH  (rows E F G H)
I = truth(4, lambda E, F, G, H: (E and G) or (F and G and H))
ok(I == {7, 10, 11, 14, 15}, "Q5a minterms %s" % sorted(I))
e, _ = KM.solve("pos", 4, sorted(set(range(16)) - I), list("EFGH"))
ok(set(range(16)) - KM.evaluate(e, 4, list("EFGH")) == set(range(16)) - I, "Q5a POS " + e)
ok(truth(4, lambda E, F, G, H: G and (E or F) and (E or H)) == I, "Q5a = G(E+F)(E+H)")
# Q5(b) table columns
x_ = [0,0,0,0,1,1,1,1]; y_ = [0,0,1,1,0,0,1,1]; z_ = [0,1,0,1,0,1,0,1]
F1 = [1,0,0,0,0,1,0,1]; F2 = [0,0,1,1,0,1,0,0]; F3 = [0,1,0,0,0,0,1,1]
ok([i for i in range(8) if F1[i]] == [0, 5, 7], "Q5b F1 = sum(0,5,7)")
ok([i for i in range(8) if F2[i]] == [2, 3, 5], "Q5b F2 = sum(2,3,5)")
ok([i for i in range(8) if F3[i]] == [1, 6, 7], "Q5b F3 = sum(1,6,7)")
ok(all(F1[i] == ((not x_[i] and not y_[i] and not z_[i]) or (x_[i] and z_[i])) for i in range(8)), "Q5b F1 = x'y'z' + xz")
ok(all(F2[i] == ((not x_[i] and y_[i]) or (x_[i] and not y_[i] and z_[i])) for i in range(8)), "Q5b F2 = x'y + xy'z")
ok(all(F3[i] == ((x_[i] and y_[i]) or (not x_[i] and not y_[i] and z_[i])) for i in range(8)), "Q5b F3 = xy + x'y'z")
# Q6(a): printed as (A xor B xor C)' = A xnor B xor C   (re-read from the 600-dpi image by the reviewer)
lhs = truth(3, lambda A, B, C: 1 - (A ^ B ^ C))
rhs = truth(3, lambda A, B, C: (1 - (A ^ B)) ^ C)             # (A xnor B) xor C
ok(lhs == rhs, "Q6a law as printed holds: (A^B^C)' = (A xnor B) ^ C")
ok(truth(3, lambda A, B, C: 1 - ((1 - (A ^ B)) ^ C)) != lhs, "Q6a (the xnor-xnor misreading would NOT hold)")
ok(truth(2, lambda A, B: not (A ^ B)) == truth(2, lambda A, B: A == B), "Q6a holds for 2 variables")
# Q6(b)
def q6b(A, B, C):
    ab = A and B; apb = A or B
    F2 = ab or (apb and C)
    F1 = ((not F2) and (apb or C)) or (ab and C)
    return F1, F2
ok(all(bool(q6b(*r)[0]) == bool(r[0] ^ r[1] ^ r[2]) for r in itertools.product([0, 1], repeat=3)), "Q6b F1 = A xor B xor C")
ok(all(bool(q6b(*r)[1]) == (sum(r) >= 2) for r in itertools.product([0, 1], repeat=3)), "Q6b F2 = AB+BC+CA")
# Q6(c) decimal -> BCD
for d in range(10):
    a3 = d in (8, 9); a2 = d in (4, 5, 6, 7); a1 = d in (2, 3, 6, 7); a0 = d in (1, 3, 5, 7, 9)
    ok(8 * a3 + 4 * a2 + 2 * a1 + a0 == d, "Q6c D%d" % d)
# Q6(d) F = P'(a+b) + P(ab) = P'a + P'b + ab
mux = truth(3, lambda P, a, b: (not P and (a or b)) or (P and a and b))
e, _ = KM.solve("sop", 3, sorted(mux), list("Pab"))
ok(mux == truth(3, lambda P, a, b: (not P and a) or (not P and b) or (a and b)), "Q6d = P'a + P'b + ab (" + e + ")")
# Q12(a)
T = ("A", ("B", ("C", ("E", None, ("I", None, None)), ("F", None, ("J", None, None))),
           ("D", ("G", None, None), ("H", ("K", None, None), ("L", None, None)))), ("M", None, None))
def pre(t): return "" if t is None else t[0] + pre(t[1]) + pre(t[2])
def ino(t): return "" if t is None else ino(t[1]) + t[0] + ino(t[2])
def post(t): return "" if t is None else post(t[1]) + post(t[2]) + t[0]
ok(pre(T) == "ABCEIFJDGHKLM", "Q12a pre " + pre(T))
ok(ino(T) == "EICFJBGDKHLAM", "Q12a in " + ino(T))
ok(post(T) == "IEJFCGKLHDBMA", "Q12a post " + post(T))
# Q3 dry run in Python
out = []
def mystery(n):
    if n <= 1: out.append(": ")
    else:
        out.append("%d " % (n % 2)); mystery(n // 2); out.append("%d " % n)
mystery(8)
M = "computers_2016_17_p1"
fails += run(M, [
    ("mystery", "Mystery.java", "", ["".join(out)]),
    ("series1", "SeriesSum.java", "3\n2\n", ["12.33333"]),
    ("series2", "SeriesSum.java", "4\n1\n", ["2.70833"]),
    ("para1", "ParagraphSort.java", "The sun rises in the east. Do you know why? It is because the earth spins from west to east! Amazing.\n",
     ["It is because the earth spins from west to east!   [words = 10]\nThe sun rises in the east.   [words = 6]\nDo you know why?   [words = 4]\nAmazing.   [words = 1]"]),
    ("para2", "ParagraphSort.java", "Where are you going? Stop. I am going to the market to buy some fruit.\n",
     ["I am going to the market to buy some fruit.   [words = 10]\nWhere are you going?   [words = 4]\nStop.   [words = 1]"]),
    ("angle1", "AngleRun.java", "15\n45\n12\n40\n", ["Angle = 28 degrees 25 minutes"]),
    ("angle2", "AngleRun.java", "30\n50\n29\n10\n", ["Angle = 60 degrees 0 minutes"]),
    ("retire1", "Retire.java", "Rina ABCDE1234F 30000 SB1029 12\n", ["Provident fund   : 7200.0", "Gratuity         : 360000.0"]),
    ("retire2", "Retire.java", "Arun PQRST9876K 25000 SB2201 7\n", ["Provident fund   : 3500.0", "Gratuity         : 0.0"]),
    ("pipe", "PipeRun.java", "", ["Rear full\n10 20 30 \npopfront -> 10\npoprear  -> 30\n20 \npoprear  -> 20\npopfront -> -999\nPipe is empty\n50"]),
    ("addlist", "AddList.java", "", ["Sum = 11.5", "Sum of empty list = 0.0"]),
])
ok(abs(1 + 2 + 8 / 2 + 32 / 6 - 12.333333) < 1e-5 and abs(1 + 1 + 1 / 2 + 1 / 6 + 1 / 24 - 2.708333) < 1e-5, "Q7 series values")
ok(0.02 * 30000 * 12 == 7200 and 0.02 * 25000 * 7 == 3500, "Q10 pf values")
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
