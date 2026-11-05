"""Checks for Computer Science pre-board 2015-16 Paper 1: every Boolean result over
all rows, the K-map reductions, the postfix, the address, the traversals and the
dry-run; every Java answer compiled and run (outputs recorded for the page)."""
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
    print(("ok   " if c else "FAIL ") + msg)
    fails += 0 if c else 1
imp = lambda p, q: (not p) or q
# Q1 absorption
ok(all((a or (a and b)) == a and (a and (a or b)) == a for a, b in itertools.product([0, 1], repeat=2)), "Q1 absorption")
# Q2 [(P=>Q) AND P] => Q tautology ; with NAND reading it is not
ok(all(imp(imp(p, q) and p, q) for p, q in itertools.product([0, 1], repeat=2)), "Q2 tautology (AND)")
ok(not all(imp(not (imp(p, q) and p), q) for p, q in itertools.product([0, 1], repeat=2)), "Q2 NAND reading is not a tautology")
# Q3 CD' + A + A + C'D' + AB = A + D'
ok(truth(4, lambda A, B, C, D: (C and not D) or A or (not C and not D) or (A and B)) == truth(4, lambda A, B, C, D: A or not D), "Q3 = A + D'")
# Q4 complement of [(AB)'A][(AB)'B] is 1
ok(truth(2, lambda A, B: not ((not (A and B)) and A and (not (A and B)) and B)) == {0, 1, 2, 3}, "Q4 complement = 1")
# Q5 AB + C' = pi(1,3,5)
ok(set(range(8)) - truth(3, lambda A, B, C: (A and B) or not C) == {1, 3, 5}, "Q5 pi(1,3,5)")
# Q7
A, B, C = 1, 0, 1
X = ((not A) and B and C) or (A and (not B) and C) or ((not A) and B and (not C))
ok(bool(X) is True, "Q7 X = 1")
# Q9
ok(infix.to_postfix("A*(B/C)/E+F")[0] == "ABC/*E/F+", "Q9 postfix ABC/*E/F+")
# Q10 address of AR[0][0] with lower bounds 0 is the base; last element AR[14][19]
ok(4000 + 8 * (14 * 20 + 19) == 6392, "Q10 AR[14][19] = 6392")
# Q12
e, _ = KM.solve("sop", 4, [0, 1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14], list("ABCD"))
ok(e == "A'D' + C' + A'B + BD'", "Q12a " + e)
ok(KM.evaluate(e, 4) == {0, 1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14}, "Q12a evaluates back")
e, _ = KM.solve("pos", 4, [0, 1, 2, 5, 8, 9, 10], list("ABCD"))
ok(e == "(B+C)(B+D)(A+C+D')", "Q12b " + e)
ok(set(range(16)) - KM.evaluate(e, 4) == {0, 1, 2, 5, 8, 9, 10}, "Q12b evaluates back")
# Q13b NOR-NOR == expression
nor = lambda *x: not any(x)
ok(truth(4, lambda A, B, C, D: nor(nor(A, not D), nor(not B, A), nor(not D, C))) ==
   truth(4, lambda A, B, C, D: (A or not D) and (not B or A) and (not D or C)), "Q13b NOR-NOR")
# Q13c XNOR from 4 NOR
def xn(A, B):
    g1 = nor(A, B); return nor(nor(A, g1), nor(B, g1))
ok(truth(2, xn) == {0, 3}, "Q13c XNOR from NOR")
# Q14a AB + (AC)' + AB'C(AB+C) = 1
ok(truth(3, lambda A, B, C: (A and B) or not (A and C) or (A and not B and C and ((A and B) or C))) == set(range(8)), "Q14a = 1")
# Q14b octal->binary encoder
for d in range(8):
    a2 = d in (4, 5, 6, 7); a1 = d in (2, 3, 6, 7); a0 = d in (1, 3, 5, 7)
    ok(4 * a2 + 2 * a1 + a0 == d, "Q14b encodes D%d" % d)
# Q14c Out = (B+C+D')(A+C+D')(C'+D) = C'D' + CD + ABC'
on = truth(4, lambda A, B, C, D: (B or C or not D) and (A or C or not D) and (not C or D))
e, _ = KM.solve("sop", 4, sorted(on), list("ABCD"))
ok(e == "C'D' + CD + ABC'", "Q14c " + e)
ok(on == truth(4, lambda A, B, C, D: (C and D) or (not C and not D) or (A and B and D)), "Q14c also = CD + C'D' + ABD")
# Q19 traversals
T = ("2", ("7", ("2", None, None), ("6", ("5", None, None), ("11", None, None))), ("5", None, ("9", ("4", None, None), None)))
def pre(t): return [] if t is None else [t[0]] + pre(t[1]) + pre(t[2])
def ino(t): return [] if t is None else ino(t[1]) + [t[0]] + ino(t[2])
def post(t): return [] if t is None else post(t[1]) + post(t[2]) + [t[0]]
ok(" ".join(pre(T)) == "2 7 2 6 5 11 5 9 4", "Q19 preorder")
ok(" ".join(ino(T)) == "2 7 5 6 11 2 5 4 9", "Q19 inorder")
ok(" ".join(post(T)) == "2 5 11 6 7 4 9 5 2", "Q19 postorder")
# Q19b loop count
N, M = 7, 5
ok(sum(1 for i in range(1, N) for j in range(1, M)) == (N - 1) * (M - 1), "Q19b (N-1)(M-1)")
# Q11 dry run in Python
outp = []
def ppp(b, e):
    if len(e) <= 2: outp.append(b + e)
    else:
        for i in range(len(e)): ppp(e[i] + b, e[i + 1:] + e[:i])
ppp("", "ABCd")
M = "computers_2015_16_p1"
fails += run(M, [
    ("ppp", "Ppp.java", "", ["\n".join(outp)]),
    ("pack1", "PackRun.java", "16 1 2 2 3 3 3 4 4 4 4 9 11 11 14 14 14\n", ["1,2,3,4,9,11,14"]),
    ("pack2", "PackRun.java", "8 5 5 5 7 8 8 10 10\n", ["5,7,8,10"]),
    ("common1", "Common.java", "5\n12 7 9 12 3 25\n4\n25 6 9 1\n", ["Common elements: 9 25"]),
    ("common2", "Common.java", "3\n1 2 3\n3\n4 5 6\n", ["no common element"]),
    ("mid1", "MidRun.java", "flower\n", ["wofelr"]),
    ("mid2", "MidRun.java", "trouble\n", ["toeblru"]),
    ("mid3", "MidRun.java", "computer\n", ["uroecmpt"]),
    ("llist", "LListRun.java", "", ["44,55,66\n44,33,22\n22,33,44,55,66\n66,55,44,33,22\nInvalid position"]),
    ("salary", "SalaryRun.java", "", ["DA         : 7000.0", "Gross pay  : 27000.0"]),
])
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
