"""Checks for computers_2024_25_g4 (CS pre-board 2024-25, Group 4, Paper 1).
Booleans over all 2^n rows, K-map covers, prefix form, tree traversal, the
spiral order, and every Java program compiled and run (JDK 11 single-file launcher)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append(os.path.join(HERE, "..", "..", "..", "Computers", "src"))
from cs_b_java import run, truth
import kmapsolve as KM, infix as IX

bad = 0
def ok(c, msg):
    global bad
    print(("ok   " if c else "FAIL ") + msg)
    bad += not c

imp = lambda a, b: (not a) or b

# Q1(vii) trick(3,4) prints 1 3 9 27 (checked again by Part1.java)
p, seen = 1, []
for j in range(1, 5):
    seen.append(p); p *= 3
ok(seen == [1, 3, 9, 27], "Q1(vii) printed values 1 3 9 27, last printed 27")

# Q2(i)
ok(IX.to_prefix("(A/B+C)/(D*(E-F))")[0] == "/+/ABC*D-EF", "Q2(i) prefix /+/ABC*D-EF")

# Q3(a) SOP
e, g = KM.solve("sop", 4, [5, 6, 7, 8, 9, 10, 11, 14, 15], list("ABCD"))
ok(e == "A'BD + BC + AB'", "Q3(a) minimal SOP %s" % e)
f3a = lambda A, B, C, D: (not A and B and D) or (B and C) or (A and not B)
ok(truth(4, f3a) == {5, 6, 7, 8, 9, 10, 11, 14, 15}, "Q3(a) A'BD + BC + AB' has the given minterms")

# Q3(b) POS: maxterm rows read from the printed sum terms
terms = ["A+B+C+D", "A+B+C+D'", "A+B+C'+D'", "A+B+C'+D", "A+B'+C+D'", "A+B'+C'+D", "A'+B+C+D", "A'+B+C'+D"]
rows = sorted(int("".join("1" if "'" in t else "0" for t in s.replace("'", "'").split("+")), 2) for s in terms)
ok(rows == [0, 1, 2, 3, 5, 6, 8, 10], "Q3(b) maxterms pi(0,1,2,3,5,6,8,10)")
e, g = KM.solve("pos", 4, rows, list("ABCD"))
ok(e == "(A+B)(B+D)(A+C+D')(A+C'+D)", "Q3(b) minimal POS %s" % e)
f3b = lambda A, B, C, D: (A or B) and (B or D) and (A or C or not D) and (A or not C or D)
ok(set(range(16)) - truth(4, f3b) == set(rows), "Q3(b) reduced POS is 0 exactly on the maxterms")

# Q4(a)
W = ["0010", "0101", "0111", "1000", "1010", "1100", "1110", "1111"]
ok(["%X" % int(w, 2) for w in W] == list("2578ACEF"), "Q4(a) hex 2 5 7 8 A C E F")

# Q4(b) A=>(B^C) vs (A=>B)^(B=>C): not valid
L = lambda A, B, C: imp(A, B and C)
R = lambda A, B, C: imp(A, B) and imp(B, C)
diff = sorted(r for r in range(8) if L(*[(r >> (2 - i)) & 1 for i in range(3)]) != R(*[(r >> (2 - i)) & 1 for i in range(3)]))
ok(diff == [2], "Q4(b) the two sides differ only in row A=0,B=1,C=0 (rows %s)" % diff)
R2 = lambda A, B, C: imp(A, B) and imp(A, C)
ok(truth(3, L) == truth(3, R2), "Q4(b) note: A=>(B^C) == (A=>B)^(A=>C) is valid")

# Q4(c) XNOR == biconditional
ok(all((a == b) == (not (a ^ b)) for a in (0, 1) for b in (0, 1)), "Q4(c) XNOR = A<=>B")

# Q5(a) MUX: S1=A (MSB), S2=B; I0=I1=C, I2=I3=C'
def mux(A, B, C):
    I = [C, C, 1 - C, 1 - C]
    return I[2 * A + B]
ok(all(mux(A, B, C) == (A ^ C) for A in (0, 1) for B in (0, 1) for C in (0, 1)), "Q5(a) Z = A xor C")
# review note: with S2 = B taken as the MSB instead, Z = B xor C
ok(all([C, C, 1 - C, 1 - C][2 * B + A] == (B ^ C) for A in (0, 1) for B in (0, 1) for C in (0, 1)), "Q5(a) note: S2 as MSB gives Z = B xor C")

# Q5(b)
ok(truth(3, lambda A, B, C: (A or B) and (A or not B) and (not A or C)) == truth(3, lambda A, B, C: A and C), "Q5(b) = AC")

# Q5(c) X = AB + A'BD + DC  (A concerts, B creative, C prizes, D highly rated)
X = lambda A, B, C, D: (A and B) or (B and D and not A) or (D and C)
on = truth(4, X)
ok(on == {3, 5, 7, 11, 12, 13, 14, 15}, "Q5(c) X = 1 in rows %s" % sorted(on))
e, _ = KM.solve("sop", 4, sorted(on), list("ABCD"))
ok(e == "CD + BD + AB", "Q5(c) reduces to %s (shown as a remark)" % e)

# Q10(b) tree
T = (8, (3, (1, None, None), (6, (4, None, None), (7, None, None))), (10, None, (14, (13, None, None), None)))
def post(t): return [] if t is None else post(t[1]) + post(t[2]) + [t[0]]
def size(t): return 0 if t is None else 1 + size(t[1]) + size(t[2])
ok(post(T) == [1, 4, 7, 6, 3, 13, 14, 10, 8], "Q10(b) postorder 1 4 7 6 3 13 14 10 8")
ok(size(T) == 9 and T[2][0] == 10, "Q10(b) size 9; node 10 is the root's child -> depth 1")

# Q8 spiral, independently
def spiral(a):
    out = []
    while a:
        out += a.pop(0)
        a = [list(r) for r in zip(*a)][::-1]
    return out
ok(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])[6] == 16, "Q8 4x4 k=7 -> 16")
ok(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])[9] == 5, "Q8 3x4 k=10 -> 5")

# Q7 join / odd positions
ok(65 * 1000 + 723 == 65723 and "65723"[0::2] == "673", "Q7 65723, odd positions 673")
ok("12030"[0::2] == "100" and "84507"[0::2] == "857", "Q7 extra cases")

# Q6 remove duplicates (first occurrence kept)
dd = lambda s: "".join(c for i, c in enumerate(s) if c not in s[:i])
ok(dd("programming") == "progamin" and dd("MISSISSIPPI RIVER") == "MISP RVE", "Q6 duplicate removal")

M = "computers_2024_25_g4"
bad += run(M, [
    ("part1", "Part1.java", "", ["1\n3\n9\n27\n", "Q2iv 1235", "Inte(\"40096\") = 40096"]),
    ("dup1", "Duplicate.java", "programming\n", ["String after removing duplicate characters : progamin"]),
    ("dup2", "Duplicate.java", "MISSISSIPPI RIVER\n", ["String after removing duplicate characters : MISP RVE"]),
    ("join1", "Join.java", "65\n723\n", ["Merged number : 65723", "Odd positioned digits : 673"]),
    ("join2", "Join.java", "1203\n0\n", ["Merged number : 12030", "Odd positioned digits : 100"]),
    ("swirl1", "Swirl.java", "4 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n7\n", ["Element number 7 in spiral order = 16"]),
    ("swirl2", "Swirl.java", "3 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n10\n", ["Element number 10 in spiral order = 5"]),
    ("swirl3", "Swirl.java", "2 2\n1 2\n3 4\n5\n", ["Invalid k"]),
    ("delete", "DeleteNode.java", "", ["Red -> Green -> Blue -> Pink -> null\nGreen -> Blue -> Pink -> null\nBlue -> Pink -> null",
                                      "Only node removed", "List is empty"]),
    ("staff", "Staff.java", "", ["Overtime    : 3000.0", "Total wages : 18000.0", "Name        : Ravi Kumar"]),
])
print("ALL PASS" if not bad else "%d FAILURES" % bad)
sys.exit(1 if bad else 0)
