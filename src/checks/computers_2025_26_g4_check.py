"""Checks for computers_2025_26_g4 (CS pre-board 2025-26, Group 4).
Every Boolean result over all 2^n rows, the address, the postfix, and every
Java program compiled and run (JDK 11 single-file launcher)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append(os.path.join(HERE, "..", "..", "..", "Computers", "src"))
from cs_b_java import run, truth
import kmapsolve as KM, addr as AD, infix as IX

bad = 0
def ok(c, msg):
    global bad
    print(("ok   " if c else "FAIL ") + msg)
    bad += not c

# Q1(viii) contrapositive of p' => q is q' => p ; equivalent to the original
imp = lambda a, b: (not a) or b
ok(all(imp(not p, q) == imp(not q, p) for p in (0, 1) for q in (0, 1)), "Q1(viii) q'=>p equivalent to p'=>q")
ok(any(imp(not p, q) != imp(q, not p) for p in (0, 1) for q in (0, 1)), "Q1(viii) option (b) is not equivalent")

# Q2(i)
ok(IX.to_postfix("((A-B)/(C*(D+E)))+F^(G-H)")[0] == "AB-CDE+*/FGH-^+", "Q2(i) postfix")
# Q2(ii) column major, rows -7..12 (20), cols 3..20 (18)
a = AD.addr("C", 5, 10, 2013, -7, 3, 6, 20, 18, -7, 3)
ok(a == 2925 and 2013 + 6 * ((10 - 3) * 20 + (5 + 7)) == 2925, "Q2(ii) address 2925 (addr.py gives %s)" % a)

# Q3 smart lighting: X = M'L + MLT' + M'L'S, rows MLTS
X = lambda M, L, T, S: ((not M) and L) or (M and L and not T) or ((not M) and (not L) and S)
on = truth(4, X)
ok(on == {1, 3, 4, 5, 6, 7, 12, 13}, "Q3 truth table minterms %s" % sorted(on))
red = lambda M, L, T, S: (L or S) and ((not M) or L) and ((not M) or (not T))
ok(truth(4, red) == on, "Q3 (L+S)(M'+L)(M'+T') equals X on all 16 rows")
ok(KM.solve("pos", 4, sorted(set(range(16)) - on), list("MLTS"))[0] == "(L+S)(M'+L)(M'+T')", "Q3 kmapsolve minimal POS")

# Q4(i)
F = lambda A, B, C, D: all([A or B or C or D, A or B or C or not D, A or B or (not C) or (not D),
                            A or B or (not C) or D, A or (not B) or C or (not D),
                            A or (not B) or (not C) or (not D), (not A) or B or C or D,
                            (not A) or B or (not C) or D])
on4 = truth(4, F)
ok(sorted(set(range(16)) - on4) == [0, 1, 2, 3, 5, 7, 8, 10], "Q4(i) maxterms pi(0,1,2,3,5,7,8,10)")
ok(truth(4, lambda A, B, C, D: (B or D) and (A or not D)) == on4, "Q4(i) (B+D)(A+D') equals F")
ok(KM.solve("pos", 4, [0, 1, 2, 3, 5, 7, 8, 10], list("ABCD"))[0] == "(B+D)(A+D')", "Q4(i) kmapsolve minimal POS")

# Q4(ii) circuit: (1)=X+Y', (2)=XZ, (3)=(1)(2), F=(3)+Z'
c = lambda x, y, z: ((x or not y) and (x and z)) or (not z)
ok(truth(3, c) == truth(3, lambda x, y, z: x or not z), "Q4(ii) F = X + Z'")
ok(0 < len(truth(3, c)) < 8, "Q4(ii) contingency (%d of 8 rows true)" % len(truth(3, c)))
ok(truth(3, lambda x, y, z: (x and z) == ((x or not y) and x and z)) == set(range(8)), "Q4(ii) (3) = XZ")

# Q5(i) hex
W = ["0001", "0101", "0111", "1000", "1010", "1100", "1110", "1111"]
ok(["%X" % int(w, 2) for w in W] == list("1578ACEF"), "Q5(i) hex equivalents")
# Q5(ii) F4 = NOR(A', A.B') = AB, not a contradiction
f4 = lambda A, B: not ((not A) or (A and not B))
ok(truth(2, f4) == {3}, "Q5(ii) F4 = AB, 1 only in row 11 -> not a contradiction")
# Q5(iii)
H = lambda p, q, r: (p and q and not r) or (not p and q and not r) or (p and not q and r) or (not p and q and r)
ok(truth(3, H) == {2, 3, 5, 6}, "Q5(iii) minterms 2,3,5,6 -> maxterms 0,1,4,7")

# Q11(ii) tree
T = ("A", ("B", ("D", ("H", None, None), ("I", None, None)), ("E", None, ("J", None, None))),
     ("C", ("F", None, None), ("G", None, None)))
def ino(t): return [] if t is None else ino(t[1]) + [t[0]] + ino(t[2])
def size(t): return 0 if t is None else 1 + size(t[1]) + size(t[2])
def ht(t): return -1 if t is None else 1 + max(ht(t[1]), ht(t[2]))
ok("".join(ino(T)) == "HDIBEJAFCG", "Q11(ii)(c) inorder HDIBEJAFCG")
ok(size(T[2]) == 3 and ht(T[2]) == 1, "Q11(ii)(b) right subtree size 3, depth 1 (edges)")
ok(T[1][2][1] is None and T[1][2][2][0] == "J", "Q11(ii) J is the RIGHT child of E (page image)")

# Java
M = "computers_2025_26_g4"
bad += run(M, [
    ("part1", "Part1.java", "", ["Q1vi -32", "Q1vii true false true", "Q2iii 7", "Q2iv 0 1 1 2 4 7 13 24"]),
    ("anagram1", "Anagram.java", "earth\nheart\n", ["earth and heart are anagram of each other"]),
    ("anagram2", "Anagram.java", "cat\ncut\n", ["cat and cut are not anagram of each other"]),
    ("sports1", "Sports.java", "Eagles 3\nHawks 4\n170 175 180\n172 168 181 183\n",
     ["Team with the higher average height : Hawks"]),
    ("sports2", "Sports.java", "Eagles 2\nHawks 2\n170 180\n175 175\n",
     ["Both teams have the same average height."]),
    ("mixsort", "Mix_sort.java", "3\n4\n1 2 3 4\n9 8 7 6\n4 5 6 7\n",
     ["After sort :\n4 3 2 1 \n6 7 8 9 \n7 6 5 4"]),
    ("repeat", "Repeat.java", "", ["10 20 30", "Overflow! Insertion not possible.", "popped 10",
                                   "Underflow! Deletion not possible.", "popped -9999", "50"]),
    ("volume", "Volume.java", "", ["Area of the circle = 153.938", "Volume of the cylinder = 1539.38"]),
    ("delete", "DeleteNode.java", "30\n10\n40\n99\n10\n",
     ["10 -> 20 -> 40 -> null", "20 -> 30 -> 40 -> null", "10 -> 20 -> 30 -> null", "99 not found",
      "List now empty: caller sets start = null"]),
])
print("ALL PASS" if not bad else "%d FAILURES" % bad)
sys.exit(1 if bad else 0)
