"""Computer Science pre-board 2015-16, Paper 2 (Practical).  Transcribed from the page images.
Checks (every program compiled and run): src/checks/computers_2015_16_p2_check.py."""
from kit import Q, SEC
from cs_b_kit import jcode, jout, tbl

M = "computers_2015_16_p2"


def grid(rows):
    return tbl(rows[0], rows[1:])


def mat(rows):
    return '<div class="tbl"><table>%s</table></div>' % "".join(
        "<tr>%s</tr>" % "".join("<td>%d</td>" % v for v in r) for r in rows)


PRAC_NOTE = r"""<p class="note">Answer as the practical expects it: the algorithm, then the documented Java program,
then the output for the paper's sample data and for further inputs — every output below is from an actual run of
this program (JDK 11).</p>"""

ITEMS = [
    SEC("Problems", "This paper consists of three problems from which candidates are required to attempt any one problem."),

    Q("1", 20, r"""<p><b>Question 1:</b> Write a program to accept the size (n) of a square matrix then create the matrix with values 1
to n<sup>2</sup> in a circular fashion as shown below.</p>
<p>Sample output : when n = 4</p>""" + mat([[1, 2, 3, 4], [12, 13, 16, 5], [11, 14, 15, 6], [10, 9, 8, 7]]) +
      r"<p>Sample output : when n=5</p>" +
      mat([[1, 2, 3, 4, 5], [16, 17, 24, 23, 6], [15, 18, 25, 22, 7], [14, 19, 20, 21, 8], [13, 12, 11, 10, 9]]) +
      r"<p>Sample output : when n=6</p>" +
      mat([[1, 2, 3, 4, 5, 6], [20, 21, 32, 31, 30, 7], [19, 22, 33, 34, 29, 8], [18, 23, 36, 35, 28, 9],
           [17, 24, 25, 26, 27, 10], [16, 15, 14, 13, 12, 11]]),
      a=PRAC_NOTE + r"""<p><b>Reading the samples.</b> The outer ring is filled clockwise (1 → 12 for n = 4). The next ring
starts at its top-left corner but goes <i>down</i> first — anticlockwise (13 at [1][1], 14 below it, 15, 16). For
n = 6 the third ring (33–36) is clockwise again. So the rings alternate: even-numbered rings (0, 2, …) clockwise,
odd-numbered rings anticlockwise, always starting at the ring's top-left corner. An ordinary one-way spiral would
give the wrong matrix for every sample.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Input n; if n &lt; 1 print "INVALID SIZE" and stop. Create m[n][n]; k ← 1.</li>
<li>For ring r = 0 to (n+1)/2 − 1: lo ← r, hi ← n−1−r.</li>
<li>If lo = hi (centre cell of odd n): m[lo][lo] ← k; go to step 7.</li>
<li>If r is even (clockwise): fill the top row m[lo][lo..hi] left to right, the right column m[lo+1..hi][hi]
downwards, the bottom row m[hi][hi−1..lo] right to left, the left column m[hi−1..lo+1][lo] upwards, putting k
and incrementing it each time.</li>
<li>If r is odd (anticlockwise): fill the left column m[lo..hi][lo] downwards, the bottom row m[hi][lo+1..hi]
left to right, the right column m[hi−1..lo][hi] upwards, the top row m[lo][hi−1..lo+1] right to left.</li>
<li>Next r.</li><li>Print the matrix row by row. Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "CircularMatrix.java") +
      r"<p><b>Output — the paper's samples</b></p>" + jout(M, "spiral4") + jout(M, "spiral5") + jout(M, "spiral6") +
      r"<p><b>Output — a further input</b> (n = 7: three alternating rings and a centre cell)</p>" + jout(M, "spiral7"),
      topic="Arrays (double-dimensional)",
      recall=r"<ul><li>Ring r occupies rows/columns r … n−1−r; there are ⌈n/2⌉ rings.</li><li>Fill each side once, stopping one short of the corner the next side starts from.</li><li>Check the direction against <i>every</i> sample before coding.</li></ul>"),

    Q("2", 20, r"""<p><b>Question 2:</b> 1<sup>st</sup> January 2015 was Thursday.<br>
Design a program which inputs the name of a month of 2015 and print the calendar of the month.</p>
<p>Sample input: January &nbsp; Sample output :</p>""" +
      grid([["Sun", "Mon", "Tues", "Wed", "Thrus", "Fri", "Sat"], ["", "", "", "", "1", "2", "3"],
            ["4", "5", "6", "7", "8", "9", "10"], ["11", "12", "13", "14", "15", "16", "17"],
            ["18", "19", "20", "21", "22", "23", "24"], ["25", "26", "27", "28", "29", "30", "31"]]) +
      r"<p>Sample input: March &nbsp; Sample output :</p>" +
      grid([["Sun", "Mon", "Tues", "Wed", "Thrus", "Fri", "Sat"], ["1", "2", "3", "4", "5", "6", "7"],
            ["8", "9", "10", "11", "12", "13", "14"], ["15", "16", "17", "18", "19", "20", "21"],
            ["22", "23", "24", "25", "26", "27", "28"], ["29", "30", "31", "*", "*", "*", "*"]]) +
      r"<p>Sample input: September &nbsp; Sample output :</p>" +
      grid([["Sun", "Mon", "Tues", "Wed", "Thrus", "Fri", "Sat"], ["", "", "1", "2", "3", "4", "5"],
            ["6", "7", "8", "9", "10", "11", "12"], ["13", "14", "15", "16", "17", "18", "19"],
            ["20", "21", "22", "23", "24", "25", "26"], ["27", "28", "29", "30", "*", "*", "*"]]),
      a=PRAC_NOTE + r"""<p><b>Idea.</b> Number the weekdays Sunday = 0 … Saturday = 6; 1 January is Thursday = 4. The 1st of
any month falls on (4 + number of days in all earlier months) mod 7 — e.g. March: (4 + 31 + 28) mod 7 = 63 mod 7 = 0,
Sunday. 2015 is not a leap year, so February has 28 days. As in the samples, cells before the 1st are blank and
cells after the last day up to Saturday hold '*'.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Store month names and days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}.</li>
<li>Input the month name; find its index m (0–11) ignoring case. If not found, print "INVALID MONTH NAME" and stop.</li>
<li>total ← sum of days[0..m−1]; start ← (4 + total) mod 7.</li>
<li>Print the heading Sun … Sat. col ← 0.</li>
<li>Print start blank cells, col ← start.</li>
<li>For d = 1 to days[m]: print d in a cell; col ← col + 1; if col = 7, go to a new line and col ← 0.</li>
<li>If col ≠ 0, print '*' cells until col = 7. Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "Calendar2015.java") +
      r"<p><b>Output — the paper's samples</b></p>" + jout(M, "cal_jan") + jout(M, "cal_mar") + jout(M, "cal_sep") +
      r"<p><b>Output — further inputs</b> (February: starts on a Sunday and fills exactly four weeks; an invalid name)</p>" +
      jout(M, "cal_feb") + jout(M, "cal_bad"),
      topic="Arrays, Strings (date / calendar programs)",
      recall=r"<ul><li>Day of week of the 1st = (day of week of 1 Jan + days before the month) mod 7.</li><li>Leap year: divisible by 400, or by 4 and not by 100.</li><li>Use a column counter to break lines after Saturday.</li></ul>"),

    Q("3", 20, r"""<p><b>Question 3:</b> A new type of encryption system was made to keep the alphabetic sentence a bit more secure by
merging the word of a sentence. The system is categorized in two categories:</p>
<p><b>Category 1 : If the number of words in the sentence is of odd numbers.</b></p>
<p>Sample input/output:<br>Original Sentence : THE DOG JUMPS OVER THE BLACK CAT.<br>
Encrypted Sentence : TCHAET &nbsp; DBOLGA*C*K &nbsp; JTUHMEP*S* &nbsp; *REVO*</p>
<p>The Encryption system will merge in the following way-</p>""" +
      tbl(["Words", "", "Merged", ""],
          [["'THE' and 'CAT'", "→", "TCHAET", "(If the words are of same length)"],
           ["'DOG' and 'BLACK'", "→", "DBOLGA*C*K", "(If the second word is lengthier than the first)"],
           ["'JUMPS' and 'THE'", "→", "JTUHMEP*S*", "(If the first word is lengthier than the Second)"],
           ["'OVER'", "→", "*REVO*", ""]]) +
      r"""<p>(the extra word which do not has a pair is reversed and then prefixed and suffixed with '*')</p>
<p><b>Category 2 : If the number of words in the sentence is of even numbers.</b></p>
<p>Sample input/output:<br>Original Sentence : ASHOK IS AN INDIAN<br>Encrypted Sentence : AISNHDOIKA*N &nbsp; IASN</p>
<p>The Encryption system will merge in the following way-</p>""" +
      tbl(["Words", "", "Merged", ""],
          [["'ASHOK' and 'INDIAN'", "→", "AISNHDOIKA*N", "(If the second word is lengthier than the first)"],
           ["'IS' and 'AN'", "→", "IASN", "(If the words are of same length)"]]) +
      r"""<p>Write a program</p><p>i) to accept an Encrypted word/ sentence and display the original word/sentence.<br>
ii) to accept an the original word/sentence and display Encrypted word/ sentence.</p>""",
      a=PRAC_NOTE + r"""<p><b>Reading the samples.</b> Word 1 is paired with the last word, word 2 with the last-but-one, and
so on. A pair is merged letter by letter — first word's letter, then second word's — and where the shorter word has
run out its turn is filled with '*' (DOG + BLACK: D B O L G A * C * K). With an odd number of words the middle word is
left over and written reversed between two '*'. The full stop is not part of the encrypted text.</p>
<p><b>Decrypting</b> reverses this: a token that begins with '*' is the middle word (a merged token always begins
with a letter of the first word); in every other token the characters at even positions (0, 2, 4, …) form the first
word and those at odd positions the second, ignoring '*'. The k-th token gives word k and word n−1−k.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Input the choice (1 = decrypt, 2 = encrypt) and the sentence; convert to upper case; drop a final
'.', '?' or '!'. Split into words w[0..n−1].</li>
<li><b>Encrypt:</b> for i = 0 to n/2 − 1: t ← "" ; for j = 0 to max(len(w[i]), len(w[n−1−i])) − 1: append
w[i][j] (or '*' if j ≥ its length), then w[n−1−i][j] (or '*'). Output t.</li>
<li>If n is odd, output "*" + reverse(w[n/2]) + "*".</li>
<li><b>Decrypt:</b> tokens t[0..p−1]. If the last token starts with '*', it is the middle word: mid ← reverse of it
without the two stars, pairs ← p − 1, n ← 2·pairs + 1; else pairs ← p, n ← 2·pairs.</li>
<li>For k = 0 to pairs − 1: a ← characters of t[k] at even positions, b ← those at odd positions, skipping '*';
w[k] ← a, w[n−1−k] ← b.</li>
<li>If n is odd, w[n/2] ← mid. Output w[0..n−1] separated by spaces. Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "MergeCipher.java") +
      r"<p><b>Output — the paper's samples</b> (both directions)</p>" + jout(M, "enc1") + jout(M, "dec1") +
      jout(M, "enc2") + jout(M, "dec2") +
      r"<p><b>Output — further inputs</b> (a sentence whose first word is much shorter than its partner, decrypted back; a single word)</p>" +
      jout(M, "enc3") + jout(M, "dec3") + jout(M, "enc4"),
      topic="Arrays, Strings",
      recall=r"<ul><li><code>StringTokenizer</code> / <code>split</code> to get words; <code>charAt</code>, <code>length</code>.</li><li>Pair index i with n−1−i.</li><li>To undo an interleave, take even and odd positions separately.</li></ul>"),
]

PAPER = dict(
    subject="computers",
    year="2015-16",
    slug="2015-16-paper-2",
    paper="Paper 2 (Practical)",
    source="PreBoard-PYQ/2015-16/Computer Science Paper II.pdf",
    marks=30, time="3 hours",
    practical=True,
    intro=r"""<p>The total time to be spent on the Planning session and the Examination session is Three hours.<br>
Planning session: 90 minutes<br>Examination session: 90 minutes<br>
Candidates are to be permitted to proceed to the Examination session only after the 90 minutes of the planning
session are over.</p>
<p><i>(This paper consists of three problems from which candidates are required to attempt any one problem)</i></p>
<ol><li>Write an algorithm for the selected problem. (Algorithm should be expressed clearly using any standard scheme
such as pseudo code or in steps which are simple enough to be obviously computable.) [3]</li>
<li>Write a program in JAVA language. The program should follow the algorithm and should be logically and
syntactically correct. [5]</li>
<li>Document the program using mnemonic names/ comments, identifying and clearly describing the choice of data types
and meaning of variables. [2]</li>
<li>Code/Type the program on the computer and get a printout (Hard Copy). Typically, this should be a program that
compiles and runs correctly. [2]</li>
<li>Test run the program on the computer using the given sample data and get a printout of the output in the format
specified in the problem. [5]</li>
<li>Viva-Voce on the Selected Problem. [3]</li>
<li>Programming Assignment File. [10]</li></ol>
<p>This question paper consists of four printed pages.</p>
<p class="note">Each problem is worth the 20 marks of items 1–6; the remaining 10 are for the assignment file.</p>""",
    items=ITEMS,
)
