"""Checks for computers_2013_14_p1: every Boolean result over all rows, the K-map
groups against the reduced terms, the drawn circuits (simulated netlists), the MUX
data inputs, address, postfix, traversals, and every Java program run."""
from computers_a_checklib import *          # noqa
import infix, addr
import computers_2013_14_figs as F
from computers_2013_14_p1 import PAPER
ABC, ABCD = ["A", "B", "C"], ["A", "B", "C", "D"]

# Q1 idempotence
for a in (0, 1):
    ok((a | a) == a and (a & a) == a, "Q1 idempotent a=%d" % a)
# Q2 (P^Q^R)' == (P^Q) xnor R
for p, q, r in rows(3):
    ok(1 - (p ^ q ^ r) == 1 - ((p ^ q) ^ r), "Q2 row %d%d%d" % (p, q, r))
# Q3 [(p'+q)(q'+r)]' + (p'+r) == 1
for p, q, r in rows(3):
    ok((1 - (((1 - p) | q) & ((1 - q) | r))) | (1 - p) | r == 1, "Q3 tautology row %d%d%d" % (p, q, r))
# Q4 postfix
pf, _ = infix.to_postfix("(A-B)*(C/D)+E")
ok(pf == "AB-CD/*E+", "Q4 postfix " + pf)
in_page(PAPER, "4", "A B &minus; C D / * E +")
# Q5 canonical POS of (P+Q)(Q+R)
zeros = {k for k, (p, q, r) in enumerate(rows(3)) if not ((p | q) & (q | r))}
ok(zeros == {0, 1, 4}, "Q5 maxterms %s" % sorted(zeros))
equiv("(P+Q+R)(P+Q+R')(P'+Q+R)", "(P+Q)(Q+R)", ["P", "Q", "R"], "Q5")
# Q6 address
a6 = addr.addr("row", 10, 10, 1234, 0, 0, 4, 30, 40, 0, 0)
ok(a6 == 2874, "Q6 address %d" % a6)
ok(addr.addr("row", 10, 10, 1234, 1, 1, 4, 30, 40, 1, 1) == 2710, "Q6 1-based variant 2710")
in_page(PAPER, "6", "2874", "2710")
# Q7 complement of A'B' + A' + AB is AB'
equiv("(A'B'+A'+AB)'", "AB'", ["A", "B"], "Q7")
# Q8 NAND circuit computes AB' + A'(B+C')
want = on_set("AB'+A'(B+C')", ABC)
circuit_check(F.Q8_TERMS, "sop", "nand", ABC, want, "Q8 NAND-NAND")
equiv("AB'+A'B+A'C'", "AB'+A'(B+C')", ABC, "Q8 expansion")
# Q13
ok(on_set("AB+ACD", ABCD) == {11, 12, 13, 14, 15}, "Q13 X = AB + ACD on-set")
ok(on_set("AB'CD+ABC'D'+ABC'D+ABCD'+ABCD", ABCD) == {11, 12, 13, 14, 15}, "Q13 canonical SOP")
kmap_check("sop", [11, 12, 13, 14, 15], ABCD, [[12, 13, 14, 15], [11, 15]], F.Q13_TERMS, "AB+ACD", "Q13")
# Q14
kmap_check("sop", F.Q14A["cells"], ABCD, F.Q14A["groups"], F.Q14A["terms"], "BC+B'C'D+AB'D'", "Q14a")
kmap_check("pos", F.Q14B["cells"], ABCD, F.Q14B["groups"], F.Q14B["terms"], "(B'+C)(A+B+D)(B+C'+D')", "Q14b")
# Q15(a) 8:1 MUX with selects ABC and data D', D, D, D', 1, 0, 0, 1
mins = {0, 3, 5, 6, 8, 9, 14, 15}
for k, (a, b, c, d) in enumerate(rows(4)):
    s = F.Q15_DATA[4 * a + 2 * b + c]
    v = {"D": d, "D'": 1 - d, "1": 1, "0": 0}[s]
    ok(v == (1 if k in mins else 0), "Q15a MUX row %d" % k)
# Q15(b)
ok(set(range(8)) - {2, 3, 4, 7} == {0, 1, 5, 6}, "Q15b")
equiv("A'B'C'+A'B'C+AB'C+ABC'", "(A+B'+C)(A+B'+C')(A'+B+C)(A'+B'+C')", ABC, "Q15b expansion")
# Q16(a) full adder from two half adders
for a, b, c in rows(3):
    s1, c1 = a ^ b, a & b
    s, c2 = s1 ^ c, s1 & c
    ok(s == a ^ b ^ c and (c1 | c2) == int(a + b + c >= 2), "Q16a row %d%d%d" % (a, b, c))
# Q16(b) NAND identities
nand = lambda x, y: 1 - (x & y)
for a, b in rows(2):
    ok(nand(a, a) == 1 - a, "Q16b NOT")
    ok(nand(nand(a, b), nand(a, b)) == (a & b), "Q16b AND")
    ok(nand(nand(a, a), nand(b, b)) == (a | b), "Q16b OR")
# Q22(c) traversals
pre, ino, post = traversals(F.Q22_TREE)
ok(pre == "R A C D B 3 5 8 6 9", "Q22 preorder " + pre)
ok(ino == "C D A B R 8 5 3 6 9", "Q22 inorder " + ino)
ok(post == "D C B A 8 5 9 6 3 R", "Q22 postorder " + post)
in_page(PAPER, "22(c)", pre, ino, post)
# review: the 3-5 edge is printed (300 dpi); 5 is the LEFT child of 3, 8 the left child of 5
ok(F.Q22_TREE[2][1][0] == "5" and F.Q22_TREE[2][1][1][0] == "8" and F.Q22_TREE[2][1][2] is None, "Q22 3-5-8 shape")
q22 = [it for it in PAPER["items"] if it.get("num") == "22(c)"][0]
ok("not visible" not in q22["q"], "Q22 no stale 'edge not visible' note")
# review: K-map cell numbers are drawn after the group rings (on a white patch)
import re as _re
_svg = F.fig_q14a_kmap()
ok(_svg.rfind('stroke-width="1.7"') < _svg.find('>15</text>'), "K-map indices drawn over rings")
# BST in Q10 is a BST
def isbst(t, lo=-1e9, hi=1e9):
    return t is None or (lo < int(t[0]) < hi and isbst(t[1], lo, int(t[0])) and isbst(t[2], int(t[0]), hi))
ok(isbst(F.Q10_BST), "Q10 example is a BST")
# Java
run_java("computers_2013_14_p1")
done("computers_2013_14_p1")
