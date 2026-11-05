"""Checks for Computer Science pre-board 2016-17 Paper 2 (Practical): every program compiled
and run on the paper's examples plus extra inputs; day counts, calendars, bouncy tests and
closest pairs re-derived independently in Python."""
import os, sys, datetime, calendar, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cs_b_java import run
fails = 0
def ok(c, msg):
    global fails
    print(("ok   " if c else "FAIL ") + msg); fails += 0 if c else 1

d = lambda s: datetime.date(*reversed([int(x) for x in s.split("/")]))
ok((d("16/11/2016") - d("10/8/2016")).days == 98, "Q1 98 days (paper)")
ok((d("5/2/2024") - d("25/12/2023")).days == 42, "Q1 42 days (extra)")
ok(datetime.date(2016, 8, 1).strftime("%A") == "Monday" and datetime.date(2016, 11, 1).strftime("%A") == "Tuesday", "Q1 paper weekdays real")
ok(datetime.date(2023, 12, 1).strftime("%A") == "Friday" and datetime.date(2024, 2, 1).strftime("%A") == "Thursday", "Q1 extra weekdays real")

def calrows(y, m):
    start = (datetime.date(y, m, 1).weekday() + 1) % 7
    nd = calendar.monthrange(y, m)[1]
    cells = ["     "] * start + ["%-5d" % k for k in range(1, nd + 1)]
    return ["".join(cells[i:i + 7]) for i in range(0, len(cells), 7)]

def bouncy(n):
    s = str(n); inc = all(a <= b for a, b in zip(s, s[1:])); dec = all(a >= b for a, b in zip(s, s[1:]))
    return not inc and not dec
ok(bouncy(29748) and not bouncy(556778) and not bouncy(663320) and bouncy(101) and not bouncy(7777), "Q2 bouncy cases")
ok(not any(bouncy(n) for n in range(1, 100)), "Q2 no bouncy number below 100")
ok(min(n for n in range(1, 1000) if bouncy(n)) == 101, "Q2 smallest bouncy = 101")

def closest(a):
    best = None
    for i, j in itertools.combinations(range(len(a)), 2):
        k = (abs(a[i] - a[j]), i, j)
        if best is None or k < best: best = k
    return best[1], best[2]
ok(closest([5, 3, 21, 10, 12, 7]) == (0, 1), "Q3 sample 1")
ok(closest([19, 0, -5, 4, 7, 10]) == (3, 4), "Q3 sample 2")
ok(closest([40, 12, 31, 15, 29]) == (2, 4), "Q3 extra (all pairs)")
# reviewer: sample 1 has a second difference-2 pair (0,5) under the all-pairs reading; rule 3 decides it
ok(sorted((abs(a-b), i, j) for (i, a), (j, b) in itertools.combinations(enumerate([5, 3, 21, 10, 12, 7]), 2))[:3]
   == [(2, 0, 1), (2, 0, 5), (2, 3, 4)], "Q3 sample 1 exercises tie-break rule 3 (0,1) vs (0,5)")

M = "computers_2016_17_p2"
fails += run(M, [
    ("date1", "DateCalendar.java", "10/8/2016\n16/11/2016\nMonday\nTuesday\n",
     ["No of days between start date and end date: 98 days"] + calrows(2016, 8) + calrows(2016, 11)),
    ("date2", "DateCalendar.java", "25/12/2023\n5/2/2024\nFriday\nThursday\n",
     ["42 days"] + calrows(2023, 12) + calrows(2024, 2)),
    ("date3", "DateCalendar.java", "30/2/2016\n1/3/2016\n", ["INVALID DATE"]),
    ("bouncy1", "Bouncy.java", "29748\n", ["29748 is a Bouncy Number"]),
    ("bouncy2", "Bouncy.java", "556778\n", ["NOT a Bouncy Number (it is an increasing number)"]),
    ("bouncy3", "Bouncy.java", "663320\n", ["NOT a Bouncy Number (it is a decreasing number)"]),
    ("bouncy4", "Bouncy.java", "101\n", ["101 is a Bouncy Number"]),
    ("bouncy5", "Bouncy.java", "7777\n", ["all its digits are equal"]),
    ("pair1", "MinDiff.java", "6\n5 3 21 10 12 7\n", ["The indices are 0, 1."]),
    ("pair2", "MinDiff.java", "6\n19 0 -5 4 7 10\n", ["The indices are 3, 4."]),
    ("pair3", "MinDiff.java", "5\n40 12 31 15 29\n", ["The indices are 2, 4."]),
])
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
