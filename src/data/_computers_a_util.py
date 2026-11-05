"""Helpers for computers_2013_14_p1.py and computers_2014_15_p1.py (agent A).

Java listings are not typed into the data modules: `code(mod, file)` reads the file in
src/checks/java/<mod>/ that the check script compiles and runs, and shows only its
`// ANSWER-START` ... `// ANSWER-END` segments (the test harness class is left out).
`RUNS` holds the stdin and the exact expected output of each program; the page shows
them as the sample run, and src/checks/computers_a_check.py re-runs every program and
fails if the output differs.
"""
import html
import os
import re

JAVA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checks", "java")


def segments(mod, fname):
    src = open(os.path.join(JAVA, mod, fname)).read()
    parts = re.findall(r"// ANSWER-START\n(.*?)\n[ \t]*// ANSWER-END", src, re.S)
    if not parts:
        return src.strip("\n")
    out = "\n\n".join(p.rstrip() for p in parts)
    lines = out.split("\n")                 # remove common indentation
    ind = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    return "\n".join(l[ind:] for l in lines)


def code(mod, fname):
    return '<pre class="code">' + html.escape(segments(mod, fname), quote=False) + "</pre>"


def pre(s):
    return '<pre class="code">' + html.escape(s, quote=False) + "</pre>"


# (module, file) -> list of (stdin, expected stdout)
RUNS = {
    ("computers_2013_14_p1", "Q11_SuperThis.java"): [("", "Name : Ujaan\nRoll : 12\n")],
    ("computers_2013_14_p1", "Q12_Output.java"): [("", "\n z=16\n")],
    ("computers_2013_14_p1", "Q17_Time.java"): [(
        "6 35\n3 45\n",
        "Enter hours and minutes of Time1: Enter hours and minutes of Time2: \n"
        "Time1 : 6 hrs 35 mins\nTime2 : 3 hrs 45 mins\nSum   : 10 hrs 20 mins\n")],
    ("computers_2013_14_p1", "Q19_Checker.java"): [(
        "", "12321 is a palindrome number\n12345 is not a palindrome number\n"
            "7 is a palindrome number\n")],
    ("computers_2013_14_p1", "Q20_Product.java"): [(
        "2.5 4\n", "Enter two numbers: n1 = 2.5, n2 = 4.0\nProduct = 10.0\n")],
    ("computers_2013_14_p1", "Q21_Someprocess.java"): [(
        "2.5\n4.0\n1.5\n",
        "line is empty\nline is empty\n-999.99\nEnter number: Enter number: line is full\n"
        "2.5  4.0  \nDeleted from front: 2.5\nEnter number: 1.5  4.0  \n"
        "Deleted from rear: 4.0\nDeleted from rear: 1.5\nIsEmpty = 1\nline is empty\n")],
    ("computers_2014_15_p1", "Q3a_Somefun.java"): [(
        "", '19\n9\nsomefun("10011",0) = 1\nsomefun("10011",1) = 2\nsomefun("10011",2) = 4\n'
            'somefun("10011",3) = 9\nsomefun("10011",4) = 19\n')],
    ("computers_2014_15_p1", "Q3b_Rec.java"): [("", "[!dlroW olleH]\n[!dlroW olleH ]\n")],
    ("computers_2014_15_p1", "Q3c_Counter.java"): [(
        "", "THE VALUE IS - 11\nTHE VALUE IS - 12\nTHE VALUE IS - 13\n")],
    ("computers_2014_15_p1", "Q8_DigiNumber.java"): [(
        "1225532\n", "Enter a number: Digit\tFrequency\n1\t1\n2\t3\n3\t1\n5\t2\n"
                     "Sum of digits of 1225532 = 20\n")],
    ("computers_2014_15_p1", "Q9_Collection.java"): [(
        "4 7 9 7 12 3\n9 1 7 20 7\n", "Enter 6 integers:\nEnter 5 integers:\n7 9 \n")],
    ("computers_2014_15_p1", "Q10_Maxword.java"): [(
        "Hello there.\nThe cat sat on the mat. I love Java! It is a programming language. "
        "Hello world! Computers are wonderful machines.\n",
        "Enter 5 sentences, each ending in . or !\nINVALID INPUT\n"
        "Enter 5 sentences, each ending in . or !\n"
        "The\tcat\tsat\ton\tthe\tmat\t\nI\tlove\tJava\tQ\tQ\tQ\t\n"
        "It\tis\ta\tprogramming\tlanguage\tQ\t\nHello\tworld\tQ\tQ\tQ\tQ\t\n"
        "Computers\tare\twonderful\tmachines\tQ\tQ\t\n"
        "Longest word: programming at rem[2][3]\n")],
    ("computers_2014_15_p1", "Q11_Sales.java"): [(
        "", "Name of salesman : R. Sen\nAddress          : Kolkata\nProduct          : Pen drive\n"
            "Bill number      : 101\nQuantity         : 5\nPrevious sales   : 1200.0\n"
            "Total sales      : 2450.0\n")],
    ("computers_2014_15_p1", "Q12_Squeue.java"): [(
        "R R F F R R F\n",
        'Insert 10 at Front or Rear (F/R)?\nInsert 20 at Front or Rear (F/R)?\nInsert 5 at Front or Rear (F/R)?\nQueue: 5 10 20\ndelete -> 5\nInsert 1 at Front or Rear (F/R)?\nQueue: 1 10 20\nInsert 30 at Front or Rear (F/R)?\nQueue: 1 10 20 30\nInsert 40 at Front or Rear (F/R)?\nOVERFLOW\nInsert 50 at Front or Rear (F/R)?\nOVERFLOW\ndelete -> 1\ndelete -> 10\ndelete -> 20\ndelete -> 30\ndelete -> -9999\n')],
    ("computers_2014_15_p1", "Q13a_LinkedSum.java"): [("", "sum = 48\nsum(empty) = 0\n")],
}


def sample(mod, fname, note=""):
    """'Sample run' block: the input typed and the output printed (both from RUNS)."""
    out = []
    for stdin, expect in RUNS[(mod, fname)]:
        s = ""
        if stdin:
            s += "<p><b>Sample input</b></p>" + pre(stdin.rstrip("\n"))
        s += ("<p><b>Output</b>" + (" (the typed input is not echoed)" if stdin else "")
              + "</p>" + pre(expect.rstrip("\n") if expect.strip() else expect))
        out.append(s)
    return (note or "") + "".join(out)


def tt(names, cols, hl=None):
    """Truth table computed here: names = input variables (MSB first);
    cols = [(header_html, fn(*bits) -> 0/1), ...]; hl = set of header indices to bold."""
    n = len(names)
    head = "".join("<th>%s</th>" % h for h in names) + "".join(
        "<th>%s</th>" % h for h, _ in cols)
    rows = []
    for k in range(2 ** n):
        bits = [(k >> (n - 1 - i)) & 1 for i in range(n)]
        vals = [int(fn(*bits)) for _, fn in cols]
        rows.append("<tr>" + "".join("<td>%d</td>" % b for b in bits) + "".join(
            ("<td><b>%d</b></td>" if hl and j in hl else "<td>%d</td>") % v
            for j, v in enumerate(vals)) + "</tr>")
    return '<table class="tt"><tr>%s</tr>%s</table>' % (head, "".join(rows))


def table(header, rows):
    h = "".join("<th>%s</th>" % x for x in header)
    b = "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows)
    return "<table><tr>%s</tr>%s</table>" % (h, b)
