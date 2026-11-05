"""Checks for computers_2014_15_p1: Boolean results over all rows, K-map groups
against reduced terms, simulated circuits, address, postfix, recursion outputs,
tree facts, and every Java program run."""
import os
from computers_a_checklib import *          # noqa
import infix, addr
import computers_2014_15_figs as F
from computers_2014_15_p1 import PAPER
XYZ, ABC, ABCD = ["X", "Y", "Z"], ["A", "B", "C"], ["A", "B", "C", "D"]

# 1(a) distributive
equiv("A+B'C", "(A+B')(A+C)", ABC, "1a")
# 1(c) OR from NAND
nand = lambda x, y: 1 - (x & y)
for a, b in rows(2):
    ok(nand(nand(a, a), nand(b, b)) == (a | b), "1c OR from NAND")
# 1(d) canonical SOP
ok(on_set("XY'+XZ+Z'", XYZ) == {0, 2, 4, 5, 6, 7}, "1d minterms")
equiv("X'Y'Z'+X'YZ'+XY'Z'+XY'Z+XYZ'+XYZ", "XY'+XZ+Z'", XYZ, "1d canonical")
in_page(PAPER, "1(d)", r"\sum(0,2,4,5,6,7)")
# 1(e) reduce and dual
kmap_check("sop", F.Q1E["cells"], XYZ, F.Q1E["groups"], ["Y", "XZ'"], "Y+XZ'", "1e")
equiv("Y(X+Z')", "Y(X+Z')", XYZ, "1e dual parses")
# 2(c) column-major: find X
d = 1060 - 1012
X = [x for x in range(10) if 2 * ((7 - x) + 10 * (3 - 1)) == d]
ok(X == [3], "2c X = %s" % X)
base = 1060 - 2 * (7 + 10 * 3)
ok(addr.addr("col", 3, 1, base, 0, 0, 2, 10, 7, 0, 0) == 1012, "2c check B[3][1]")
# 2(e) postfix with word operators
pf, _ = infix.to_postfix("NOT a AND b OR c AND d")
ok(pf == "aNOTbANDcdANDOR", "2e postfix " + pf)
in_page(PAPER, "2(e)", "a NOT b AND c d AND OR")
# 3(a)
def somefun(s, last):
    if last < 0: return 0
    return 2 * somefun(s, last - 1) if s[last] == "0" else 1 + 2 * somefun(s, last - 1)
ok(somefun("10011", 4) == 19 and somefun("001001101", 5) == 9, "3a values")
in_page(PAPER, "3(a)", "returns 19", "returns 9")
# 3(b)
ok("Hello World!"[::-1] == "!dlroW olleH", "3b reverse")
in_page(PAPER, "3(b)", "!dlroW olleH")
# 4
kmap_check("sop", F.Q4A["cells"], ABCD, F.Q4A["groups"], F.Q4A["terms"], "CD+BD'", "4a")
kmap_check("pos", F.Q4B["cells"], ABCD, F.Q4B["groups"], F.Q4B["terms"], "(A'+B')(A'+D)(B+C+D)", "4b")
# 5: S(G,T,A,B) = (G+T)AB
GTAB = F.Q5["names"]
ok(on_set("(G+T)AB", GTAB) == {7, 11, 15}, "5 minterms")
equiv("G'TAB+GT'AB+GTAB", "(G+T)AB", GTAB, "5 canonical")
kmap_check("sop", F.Q5["cells"], GTAB, F.Q5["groups"], F.Q5["terms"], "TAB+GAB", "5")
# 6(a) half subtractor
XY = ["X", "Y"]
ok(on_set("X'Y+XY'", XY) == {1, 2}, "6a D")
ok(on_set("(X+Y)(X'+Y)(X'+Y')", XY) == {1}, "6a B POS")
ok(on_set("X'Y", XY) == {1}, "6a B reduced")
circuit_check(F.Q6_TERMS, "sop", "nand", XY, {1, 2}, "6a NAND-NAND")
# 6(b)
for p, q in rows(2):
    lhs = (p | q) & p            # ~P => Q  ==  P v Q
    rhs = (p & (1 - q)) | (p & q)
    ok(lhs == rhs == p, "6b row %d%d" % (p, q))
# 6(c)
for a, b, c in rows(3):
    ok(((a & b) | (c & (a ^ b))) == int(a + b + c >= 2), "6c carry")
# 7(a) mux equation
for s1, s0 in rows(2):
    for I in itertools.product((0, 1), repeat=4):
        y = ((1-s1)&(1-s0)&I[0]) | ((1-s1)&s0&I[1]) | (s1&(1-s0)&I[2]) | (s1&s0&I[3])
        ok(y == I[2 * s1 + s0], "7a mux")
# 7(b)
ok(on_set("ABC+AB'C'+AB'C+ABC'+A'B'C", ABC) == {1, 4, 5, 6, 7}, "7b minterms")
equiv("(A+B+C)(A+B'+C)(A+B'+C')", "ABC+AB'C'+AB'C+ABC'+A'B'C", ABC, "7b POS")
equiv("A+B'C", "ABC+AB'C'+AB'C+ABC'+A'B'C", ABC, "7b simplified")
# 7(c) circuit as drawn: (1)=XY, (2)=(1)Z, (3)=(2)', F=(3)(1)
for x, y, z in rows(3):
    o1 = x & y; o2 = o1 & z; o3 = 1 - o2; f = o3 & o1
    ok(f == (x & y & (1 - z)), "7c row %d%d%d" % (x, y, z))
# 13(b)
def nodes(t):
    return [] if t is None else [t] + nodes(t[1]) + nodes(t[2])
allnodes = nodes(F.Q13_TREE)
internal = sorted(n[0] for n in allnodes if n[1] or n[2])
leaves = sorted(n[0] for n in allnodes if not (n[1] or n[2]))
ok(internal == sorted("ABCEGHJ"), "13b internal %s" % internal)
ok(leaves == sorted("DKFIL"), "13b leaves %s" % leaves)
pre, _, _ = traversals(F.Q13_TREE)
ok(pre == "A B D E H K C F G I J L", "13b preorder " + pre)
ok(F.Q13_TREE[2][2] == F.Q13_RIGHT_C, "13b right subtree of C")
in_page(PAPER, "13(b)", pre, "A, B, C, E, G, H, J", "D, K, F, I, L")
# 13(a) list sum
ok(sum(F.Q13_LIST) == 48, "13a sum")
# review: Q10 counts words with the same delimiters it fills rem[][] with (else words were dropped)
_j = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "java", "computers_2014_15_p1", "Q10_Maxword.java")).read()
ok(_j.count('" ,;:?"') == 2, "Q10 consistent delimiters")
# review: 4:1 MUX output wires use outer lanes for outer gates (no crossing near the OR)
import inspect as _insp
ok("lanes = [1, 0, 0, 1]" in _insp.getsource(F.fig_q7a_mux), "7a MUX lanes")
q13c = [it for it in PAPER["items"] if it.get("num") == "13(c)"][0]
ok("never terminates" in q13c["a"], "13c literal-behaviour note")
run_java("computers_2014_15_p1")
done("computers_2014_15_p1")
