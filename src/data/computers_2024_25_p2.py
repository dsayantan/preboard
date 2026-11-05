"""Computer Science pre-board 2024-25, Paper 2 (Practical).  Transcribed from the page images
(the PDF has a text layer, used only as a starting point).
Checks (every program compiled and run): src/checks/computers_2024_25_p2_check.py."""
from kit import Q, SEC
from cs_b_kit import jcode, jout, tbl

M = "computers_2024_25_p2"

PRAC_NOTE = r"""<p class="note">Answer as the practical expects it: the algorithm, then the documented Java program,
then the output for the paper's examples and for further inputs — every output below is from an actual run of this
program (JDK 11). The input given to each run is shown above its output.</p>"""


def mat(rows):
    b = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return '<div class="tbl"><table>%s</table></div>' % b


def pre(s):
    return '<pre class="code">%s</pre>' % s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


Q1 = r"""<p><b>QUESTION 1</b></p>
<p>A Prime-Adam integer is a positive integer (without leading zeros) which is a prime as well as an Adam number.</p>
<p><b>Prime number:</b> A number which has only two factors, i.e. 1 and the number itself.<br>Example: 2, 3, 5, 7 ... etc.</p>
<p><b>Adam number:</b> The square of a number and the square of its reverse are reverse to each other.<br>
Example: If n = 13 and reverse of 'n' = 31, then,<br>(13)<sup>2</sup> = 169<br>(31)<sup>2</sup> = 961 which is reverse of 169<br>
thus 13, is an Adam number.</p>
<p>Accept two positive integers m and n, where m is less than n as user input. Display all Prime-Adam integers that are
in the range between m and n (both inclusive) and output them along with the frequency, in the format given below:</p>
<p>Test your program with the following data and some random data:</p>
<p><b>Example 1</b><br>INPUT:<br>m = 5<br>n = 100<br>OUTPUT:<br>THE PRIME-ADAM INTEGERS ARE:<br>11 13 31<br>
FREQUENCY OF PRIME-ADAM INTEGERS IS: 3</p>
<p><b>Example 2</b><br>INPUT:<br>m = 100<br>n = 200<br>OUTPUT:<br>THE PRIME-ADAM INTEGERS ARE:<br>101 103 113<br>
FREQUENCY OF PRIME-ADAM INTEGERS IS: 3</p>
<p><b>Example 3</b><br>INPUT:<br>m = 50<br>n = 70<br>OUTPUT:<br>THE PRIME-ADAM INTEGERS ARE:<br>NIL<br>
FREQUENCY OF PRIME-ADAM INTEGERS IS: 0</p>
<p><b>Example 4</b><br>INPUT:<br>m = 700<br>n = 450<br>OUTPUT:<br>INVALID INPUT</p>"""

Q2 = (r"""<p><b>QUESTION 2</b></p>
<p>Write a program to declare a matrix A[][] of order MXN where M is the number of rows and N is the number of columns
such that M and N must be greater than 2 and less than 10. Allow the user to input integers into this matrix. Display
the appropriate error message for an invalid input.</p>
<p>Perform the following tasks on the matrix.</p>
<p>(a) Display the input matrix<br>
(b) Shift each column one step right so that the first column becomes the second column, the second column become the
third column and so on.<br>
(c) Display the shifted matrix along with the second smallest element and its location in the modified matrix.</p>
<p>Test your program for the following data and some random data.</p>
<p><b>Example 1:</b><br>INPUT: M=3<br>N=4<br>Enter the elements in the matrix:</p>"""
      + mat([[100, 90, 79, 56], [45, 64, 32, 99], [47, 89, 200, 15]])
      + r"""<p>OUTPUT:<br>Formed matrix after shifting</p>"""
      + mat([[56, 100, 90, 79], [99, 45, 64, 32], [15, 47, 89, 200]])
      + r"""<p>Second Smallest Element : 32 (Row: 1 and Column: 3)</p>
<p><b>Example 2:</b><br>INPUT: M=4<br>N=3<br>Enter the elements in the matrix:</p>"""
      + mat([[100, 90, 79], [45, 64, 32], [47, 89, 200], [89, 12, 30]])
      + r"""<p>OUTPUT:<br>Formed matrix after shifting</p>"""
      + mat([[79, 100, 90], [32, 45, 64], [200, 47, 89], [30, 89, 12]])
      + r"""<p>Second Smallest Element : 30 (Row: 3 and Column: 0)</p>
<p><b>Example 3:</b><br>INPUT: M=2<br>N=3<br>OUTPUT: Size is out of Range. Invalid Entry</p>""")

KEYPAD = ('<div class="tbl"><table>'
          '<tr><td>1</td><td>ABC<br>2</td><td>DEF<br>3</td></tr>'
          '<tr><td>GHI<br>4</td><td>JKL<br>5</td><td>MNO<br>6</td></tr>'
          '<tr><td>PQRS<br>7</td><td>TUV<br>8</td><td>WXYZ<br>9</td></tr>'
          '<tr><td></td><td>[SPACE]<br>0</td><td></td></tr></table></div>')

Q3 = (r"""<p><b>QUESTION 3</b></p>
<p>Most cell phone keypads look like the following arrangement (the letters are above the respective number)</p>"""
      + KEYPAD +
      r"""<p>For sending a message we generally need to press the individual keypad a number of times as per our requirement.
The task is to find out the frequency of each number being pressed to form a message. For this problem, accept a
sentence containing white spaces and print the frequency of each number being pressed to get each letter in each word.</p>
<p>Test your program with the sample data and some random data:</p>
<p><b>Example 1:</b><br>INPUT: DEAR ALL<br>OUTPUT:</p>"""
      + pre("DEAR\nNumber 3  is pressed 3 times\nNumber 2 is pressed 1 time\nNumber 7 is pressed 3 times\nWhite Space\n"
            "Number 0 is pressed 1 time.\nALL\nNumber 2 is pressed 1 time\nNumber 5 is pressed 6 times")
      + r"""<p><b>Example 2:</b><br>INPUT : THANK YOU<br>OUTPUT:</p>"""
      + pre("THANK\nNumber 8 is pressed 1 time\nNumber 4 is pressed 2 times\nNumber 2 is pressed 1 time\n"
            "Number 6 is pressed 2 times\nNumber 5 is pressed 2 times\nWhite Space\nNumber 0 is pressed 1 time.\nYOU\n"
            "Number 9 is pressed 3 times\nNumber 6 is pressed 3 times\nNumber 8 is pressed 2 times")
      + r"""<p><b>Example 3:</b> INPUT : GOOD-LUCK<br>OUTPUT: Invalid Entry</p>""")

ITEMS = [
    SEC("Problems", "This paper consists of three problems from which candidates are required to attempt any one problem."),

    Q("1", 15, Q1,
      a=PRAC_NOTE + r"""<p><b>Idea.</b> Test each i from m to n: i must be prime (no divisor from 2 to √i) and Adam
(reverse(i²) = (reverse(i))², e.g. 12: 144 reversed is 441 = 21²). The squares are held in <code>long</code> so
that large ranges do not overflow. m ≥ n (or a non-positive limit) is invalid.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Input m and n.</li>
<li>If m ≤ 0 or n ≤ 0 or m ≥ n, print “INVALID INPUT” and stop.</li>
<li>freq ← 0, list ← "".</li>
<li>For i = m to n: if isPrime(i) and isAdam(i), append i to list and freq ← freq + 1.</li>
<li>Print “THE PRIME-ADAM INTEGERS ARE:”; print “NIL” if freq = 0, else print list.</li>
<li>Print “FREQUENCY OF PRIME-ADAM INTEGERS IS: ” freq. Stop.</li></ol>
<p><i>isPrime(x)</i>: if x &lt; 2 return false; for d = 2 while d × d ≤ x: if x mod d = 0 return false; return true.<br>
<i>reverse(x)</i>: r ← 0; while x &gt; 0: r ← r × 10 + x mod 10, x ← x div 10; return r.<br>
<i>isAdam(x)</i>: return reverse(x × x) = reverse(x) × reverse(x).</p>
<p><b>Program</b></p>""" + jcode(M, "PrimeAdam.java") +
      r"<p><b>Output — the paper's four examples</b></p>" + jout(M, "adam1") + jout(M, "adam2") + jout(M, "adam3") + jout(M, "adam4") +
      r"<p><b>Output — random data</b> (m = 1, n = 1000)</p>" + jout(M, "adam5"),
      topic="Methods — number problems (prime, reverse)",
      recall=r"<ul><li>Prime test: try divisors 2 … √n only.</li><li>Reverse a number: r = r·10 + n%10, n = n/10.</li><li>Validate the input before any processing; print NIL when nothing is found.</li></ul>"),

    Q("2", 15, Q2,
      a=PRAC_NOTE + r"""<p><b>Idea.</b> Shifting every column one step right is a right rotation of each row: the last
element of a row is saved, the others move one place right, and the saved element goes into column 0 (as in both
examples, the last column comes round to the first). The second smallest element is the smallest value greater than
the minimum (a repeated minimum is not counted twice); its first position in the shifted matrix, row by row, is
reported with 0-based row and column numbers as in the examples.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Input M and N. If M ≤ 2 or M ≥ 10 or N ≤ 2 or N ≥ 10, print “Size is out of Range. Invalid Entry”
and stop.</li>
<li>Input the M × N elements into A[][]; display A.</li>
<li>For each row i: last ← A[i][N−1]; for j = N−1 down to 1: A[i][j] ← A[i][j−1]; A[i][0] ← last.</li>
<li>Display A with the heading “Formed matrix after shifting”.</li>
<li>min ← the smallest element of A.</li>
<li>sec ← the smallest element of A that is greater than min, scanning row by row; record its row r and column c.</li>
<li>If no element exceeds min, report that there is no second smallest element; otherwise print
“Second Smallest Element : sec (Row: r and Column: c)”. Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "ShiftMatrix.java") +
      r"<p><b>Output — the paper's three examples</b></p>" + jout(M, "shift1") + jout(M, "shift2") + jout(M, "shift3") +
      r"<p><b>Output — random data</b> (minimum 1 appears twice; the second smallest, 3, also twice — its first position is reported)</p>" +
      jout(M, "shift4"),
      topic="Arrays — two-dimensional arrays",
      recall=r"<ul><li>Right rotation of a row: save the last element, shift the rest right (from the end backwards), put the saved one at index 0.</li><li>Second smallest = smallest of the elements greater than the minimum.</li><li>Rows and columns are numbered from 0, as in the sample output.</li></ul>"),

    Q("3", 15, Q3,
      a=PRAC_NOTE + r"""<p><b>Idea.</b> A letter on key d needs as many presses as its position on that key (A = 1 press of
2, B = 2, C = 3; S = 4 presses of 7). For each word the presses are added per key, and the keys are listed in the
order in which they are first used in that word (this reproduces both sample outputs: in ALL the two Ls add 3 + 3 =
6 presses of key 5). Between two words the program prints “White Space” and one press of key 0. The sentence may
contain only letters and single spaces; anything else (such as the hyphen in GOOD-LUCK) is invalid. Lower-case input
is converted to capitals.</p>
<p><b>Algorithm</b></p>
<ol><li>Start. Input the sentence s; s ← s trimmed and in upper case.</li>
<li>If s is empty, or contains a character that is neither a letter nor a space, or two consecutive spaces, print
“Invalid Entry” and stop.</li>
<li>Split s into words at the spaces.</li>
<li>For each word w (index i): if i &gt; 0 print “White Space” and “Number 0 is pressed 1 time.”; print w.</li>
<li>&nbsp;&nbsp;Set count[0…9] ← 0 and an empty list order. For each letter ch of w: d ← the key carrying ch;
if count[d] = 0 add d to order; count[d] ← count[d] + (position of ch on key d).</li>
<li>&nbsp;&nbsp;For each d in order print “Number d is pressed count[d] time(s)”.</li>
<li>Stop.</li></ol>
<p><b>Program</b></p>""" + jcode(M, "Keypad.java") +
      r"<p><b>Output — the paper's three examples</b></p>" + jout(M, "key1") + jout(M, "key2") + jout(M, "key3") +
      r"<p><b>Output — random data</b> (lower-case input)</p>" + jout(M, "key4"),
      topic="Strings",
      recall=r"<ul><li><code>KEYS[d-2].indexOf(ch) + 1</code> gives the presses for ch on key d.</li><li>Use a count array indexed by key, plus an order array to keep first-use order.</li><li>Validate characters before processing; <code>split(&quot; &quot;)</code> separates the words.</li></ul>"),
]

PAPER = dict(
    subject="computers",
    year="2024-25",
    slug="2024-25-paper-2",
    paper="Paper 2 (Practical)",
    source="PreBoard-PYQ/2024-25/SET-1/COMPUTER PRACTICAL.pdf",
    marks=30, time="3 hours",
    practical=True,
    intro=r"""<p><b>THE HERITAGE SCHOOL — PRE BOARD EXAMINATION 2024-25 — COMPUTER SCIENCE PRACTICAL PAPER - 2</b></p>
<p>(Maximum Marks: 30) &nbsp; Time allowed: 3 Hours<br>
(Candidates are allowed additional 15 minutes for only reading the paper.)<br>(They must NOT start writing during this time.)</p>
<p>The total time to be spent on the Planning Session and the Examination Session is Three hours. After completing the
Planning Session, the candidate may begin with the Examination Session. A maximum of 90 minutes is permitted for the
Planning Session. However, if candidates finish earlier, they are to be permitted to begin the Examination Session.
This paper consists of three problems from which candidates are required to attempt any one problem.</p>
<p><b>Candidates are expected to do the following:</b></p>
<p><b>A. Planning Session:</b></p>
<ol><li>Write an algorithm for the selected problem. (Algorithm should be expressed clearly using any standard scheme
such as pseudo code or in steps which are simple enough to be obviously computable.) [3 marks]</li>
<li>Write a program in JAVA language. The program should follow the algorithm and should be logically and syntactically
correct. Document the program using mnemonic names /comments, identifying, and clearly describing the choice of data
types and meaning of variables. [7 marks]</li></ol>
<p><b>B. Examination Session:</b></p>
<ol><li>Code / Type the program on the computer and get a printout (hard copy). Typically, this should be a program
that compiles and runs correctly. [2 marks]</li>
<li>Test run the program on the computer using the given sample data and get a printout of the output in the format
specified in the problem. [3 marks]</li></ol>
<p><b>[Project - 15 marks]</b></p>
<p>This question paper consists of 4 printed pages.</p>
<p class="note">Each problem is worth the 15 marks of the planning and examination sessions; the other 15 are for the
project.</p>""",
    items=ITEMS,
)
