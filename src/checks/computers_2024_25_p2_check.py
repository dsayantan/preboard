"""Checks for computers_2024_25_p2 (CS pre-board 2024-25, Paper 2, Practical):
every program compiled and run on the paper's examples plus extra inputs, and the
expected answers re-derived independently in Python."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cs_b_java import run
bad = 0
def ok(c, msg):
    global bad
    print(("ok   " if c else "FAIL ") + msg); bad += not c

# Q1 Prime-Adam
isp = lambda n: n > 1 and all(n % i for i in range(2, int(n ** .5) + 1))
rev = lambda n: int(str(n)[::-1])
adam = lambda n: rev(n * n) == rev(n) ** 2
pa = lambda m, n: [i for i in range(m, n + 1) if isp(i) and adam(i)]
ok(pa(5, 100) == [11, 13, 31], "Q1 5..100")
ok(pa(100, 200) == [101, 103, 113], "Q1 100..200")
ok(pa(50, 70) == [], "Q1 50..70 NIL")
ok(pa(1, 1000) == [2, 3, 11, 13, 31, 101, 103, 113, 211, 311], "Q1 1..1000 (extra run)")

# Q2 shift + second smallest
def q2(m):
    s = [[r[-1]] + r[:-1] for r in m]
    v = sorted(set(x for r in s for x in r))[1]
    loc = next((i, j) for i, r in enumerate(s) for j, x in enumerate(r) if x == v)
    return s, v, loc
s, v, loc = q2([[100, 90, 79, 56], [45, 64, 32, 99], [47, 89, 200, 15]])
ok(s[0] == [56, 100, 90, 79] and (v, loc) == (32, (1, 3)), "Q2 example 1")
s, v, loc = q2([[100, 90, 79], [45, 64, 32], [47, 89, 200], [89, 12, 30]])
ok(s[3] == [30, 89, 12] and (v, loc) == (30, (3, 0)), "Q2 example 2")
s, v, loc = q2([[5, 1, 9], [1, 7, 3], [8, 3, 6]])
ok((v, loc) == (3, (1, 0)), "Q2 extra (repeated minimum 1, second smallest 3) -> %s %s" % (v, loc))

# Q3 keypad
K = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
def kp(w):
    out = {}
    for ch in w:
        d = next(i for i, k in enumerate(K) if ch in k)
        out[d] = out.get(d, 0) + K[d].index(ch) + 1
    return list(out.items())
ok(kp("DEAR") == [(3, 3), (2, 1), (7, 3)] and kp("ALL") == [(2, 1), (5, 6)], "Q3 DEAR ALL")
ok(kp("THANK") == [(8, 1), (4, 2), (2, 1), (6, 2), (5, 2)] and kp("YOU") == [(9, 3), (6, 3), (8, 2)], "Q3 THANK YOU")
ok(kp("SOON") == [(7, 4), (6, 8)], "Q3 SOON (extra)")

M = "computers_2024_25_p2"
bad += run(M, [
    ("adam1", "PrimeAdam.java", "5\n100\n", ["THE PRIME-ADAM INTEGERS ARE:\n11 13 31\nFREQUENCY OF PRIME-ADAM INTEGERS IS: 3"]),
    ("adam2", "PrimeAdam.java", "100\n200\n", ["101 103 113\nFREQUENCY OF PRIME-ADAM INTEGERS IS: 3"]),
    ("adam3", "PrimeAdam.java", "50\n70\n", ["NIL\nFREQUENCY OF PRIME-ADAM INTEGERS IS: 0"]),
    ("adam4", "PrimeAdam.java", "700\n450\n", ["INVALID INPUT"]),
    ("adam5", "PrimeAdam.java", "1\n1000\n", ["2 3 11 13 31 101 103 113 211 311", "IS: 10"]),
    ("shift1", "ShiftMatrix.java", "3\n4\n100 90 79 56\n45 64 32 99\n47 89 200 15\n",
     ["    56   100    90    79", "Second Smallest Element : 32 (Row: 1 and Column: 3)"]),
    ("shift2", "ShiftMatrix.java", "4\n3\n100 90 79\n45 64 32\n47 89 200\n89 12 30\n",
     ["    30    89    12", "Second Smallest Element : 30 (Row: 3 and Column: 0)"]),
    ("shift3", "ShiftMatrix.java", "2\n3\n", ["Size is out of Range. Invalid Entry"]),
    ("shift4", "ShiftMatrix.java", "3\n3\n9 5 1\n7 1 3\n6 8 3\n", ["Second Smallest Element : 3 (Row: 1 and Column: 0)"]),
    ("key1", "Keypad.java", "DEAR ALL\n", ["DEAR\nNumber 3 is pressed 3 times\nNumber 2 is pressed 1 time\nNumber 7 is pressed 3 times\nWhite Space\nNumber 0 is pressed 1 time.\nALL\nNumber 2 is pressed 1 time\nNumber 5 is pressed 6 times"]),
    ("key2", "Keypad.java", "THANK YOU\n", ["THANK\nNumber 8 is pressed 1 time\nNumber 4 is pressed 2 times\nNumber 2 is pressed 1 time\nNumber 6 is pressed 2 times\nNumber 5 is pressed 2 times\nWhite Space\nNumber 0 is pressed 1 time.\nYOU\nNumber 9 is pressed 3 times\nNumber 6 is pressed 3 times\nNumber 8 is pressed 2 times"]),
    ("key3", "Keypad.java", "GOOD-LUCK\n", ["Invalid Entry"]),
    ("key4", "Keypad.java", "see you soon\n", ["SOON\nNumber 7 is pressed 4 times\nNumber 6 is pressed 8 times"]),
])
print("ALL PASS" if not bad else "%d FAILURES" % bad)
sys.exit(1 if bad else 0)
