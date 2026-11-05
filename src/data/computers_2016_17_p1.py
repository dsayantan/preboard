"""Computer Science pre-board 2016-17, Paper 1 (Theory).  Transcribed from the page images
(scanned, no text layer).  Checks: src/checks/computers_2016_17_p1_check.py."""
from kit import Q, SEC
import computers_2016_17_figs as F
from cs_b_kit import jcode, jout, tbl
import infix

M = "computers_2016_17_p1"


def tt(header, rows):
    return tbl(header, [[str(c) for c in r] for r in rows])


_pf, _trace = infix.to_postfix("P+T/Q*(G*(R+K)/M*(N-J)/S)+L")
RPN_TABLE = tbl(["Symbol", "Stack", "Postfix", "Action"], [list(r) for r in _trace])

ITEMS = [
    SEC("Part I", "Answer all questions. While answering questions in this Part, indicate briefly your working and "
                  "reasoning, wherever required."),

    Q("1(a)", 1, r"<p>Find the complement of the expression: \(S' + ST'\).</p>",
      a=r"""<p>\((S' + ST')' = (S')'\cdot(ST')'\) &nbsp; (De Morgan)</p>
<p>\(= S\cdot(S' + T) = SS' + ST = 0 + ST\)</p>
<p><span class="box">\(ST\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>De Morgan: \((X + Y)' = X'Y'\), \((XY)' = X' + Y'\).</li><li>\(SS' = 0\).</li></ul>"),

    Q("1(b)", 1, r"<p>State the two absorption laws. Verify one of them using a truth table.</p>",
      a=r"""<p><b>Absorption laws:</b> (i) \(X + XY = X\) &nbsp; (ii) \(X(X + Y) = X\)</p>
<p>Verifying (i):</p>""" + tt(["X", "Y", "XY", "X + XY"], [[0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]) +
      r"<p>Column \(X + XY\) equals column X in every row, so <span class=\"box\">\(X + XY = X\)</span></p>",
      topic="Boolean Algebra",
      recall=r"<ul><li>Absorption \(X + XY = X\) and its dual \(X(X+Y) = X\).</li></ul>"),

    Q("1(c)", 1, r"<p>Given, \(F(A,B,C) = (A' + B')\cdot(B + C')\), write the function in canonical product of sum form.</p>",
      a=r"""<p>A sum term with a variable missing is expanded by adding \(XX' = 0\):</p>
<p>\(A' + B' = A' + B' + CC' = (A' + B' + C)(A' + B' + C')\)</p>
<p>\(B + C' = B + C' + AA' = (A + B + C')(A' + B + C')\)</p>
<p><span class="box">\(F = (A + B + C')(A' + B + C')(A' + B' + C)(A' + B' + C')\)</span> &nbsp; \(= \pi(1, 5, 6, 7)\)</p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>\(X + YY' = (X + Y)(X + Y')\) — distributive law for sums.</li><li>Canonical POS: every sum term contains every variable.</li></ul>"),

    Q("1(d)", 1, r"<p>Draw the truth table and logic circuit for a 2-input XNOR gate.</p>",
      a=tt(["A", "B", "X = A ⊙ B"], [[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]) +
      r"""<p>\(X = A \odot B = AB + A'B'\) — the output is 1 when both inputs are equal.</p>
<p>Gate symbol:</p>{{fig:0}}<p>Using basic gates:</p>{{fig:1}}""",
      afig=[F.fig_q1d_gate, F.fig_q1d_basic],
      topic="Computer Hardware (logic gates)",
      recall=r"<ul><li>XNOR = complement of XOR = \(AB + A'B'\) (equality detector).</li><li>Symbol: XOR shape with an output bubble.</li></ul>"),

    Q("1(e)", 1, r"<p>If x→y and x = Beth is a good girl and y = Beth submits her work on time then write the contrapositive of x→y.</p>",
      a=r"""<p>Contrapositive of \(x \Rightarrow y\) is \(\sim y \Rightarrow\ \sim x\):</p>
<p><span class="box">If Beth does not submit her work on time, then Beth is not a good girl.</span></p>""",
      topic="Boolean Algebra (propositional logic)",
      recall=r"<ul><li>Converse \(y\Rightarrow x\); inverse \(\sim x\Rightarrow\sim y\); contrapositive \(\sim y\Rightarrow\sim x\).</li><li>A statement and its contrapositive are equivalent.</li></ul>"),

    Q("2(a)", 2, r"<p>How is final different from finally with respect to java?</p>",
      a=r"""<p><b><code>final</code></b> is a modifier: a final variable is a constant (cannot be reassigned), a final
method cannot be overridden, a final class cannot be extended. e.g. <code>final double PI = 3.14159;</code></p>
<p><b><code>finally</code></b> is a block used with <code>try</code>–<code>catch</code> in exception handling; the
code in it is executed whether or not an exception occurs (used to release resources, close files etc.).</p>""",
      topic="Variables, Expressions (final) / exceptions",
      recall=r"<ul><li><code>final</code>: constant / no override / no subclass.</li><li><code>finally</code>: always-executed block after try–catch.</li></ul>"),

    Q("2(b)", 2, r"<p>Write the difference between an abstract class and an interface.</p>",
      a=tbl(["Abstract class", "Interface"],
            [["May have both abstract and concrete (defined) methods.", "Methods are abstract (only declared)."],
             ["May have instance variables of any kind.", "Variables are implicitly public static final (constants)."],
             ["A class extends only one abstract class (<code>extends</code>).", "A class can implement many interfaces (<code>implements</code>)."],
             ["Can have constructors.", "Cannot have constructors."]]),
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li>Neither can be instantiated.</li><li>Interface = pure contract; abstract class = partial implementation.</li></ul>"),

    Q("2(c)", 2, r"""<p>Each element of an array arr[15][20] requires 'W' bytes of storage. If the address of arr[6][8] is 4550 and
the base address at arr[1][1] is 4000, find the width 'W' of each cell in the array arr[][] when the array is stored in
<b>Column Major Order</b>.</p>""",
      a=r"""<p>Column major: \(\text{Address}(arr[i][j]) = B + W[(i - L_r) + (j - L_c)\times N_r]\),
with \(B = 4000\) at \(arr[1][1]\) (so \(L_r = L_c = 1\)) and \(N_r = 15\) rows.</p>
<p>\(4550 = 4000 + W[(6 - 1) + (8 - 1)\times 15]\)</p>
<p>\(550 = W[5 + 105] = 110\,W\)</p>
<p><span class="box">\(W = 5\) bytes</span></p>""",
      topic="Arrays (address calculation)",
      recall=r"<ul><li>Column major: \(B + W[(i-L_r) + (j-L_c)N_r]\) — multiply by the number of <i>rows</i>.</li><li>Measure i and j from the element whose address is the base.</li></ul>"),

    Q("2(d)", 2, r"<p>Differentiate between worst and average case complexity.</p>",
      a=r"""<p><b>Worst case:</b> the maximum time (number of basic operations) an algorithm takes over all inputs of
size n — an upper bound. e.g. linear search when the item is last or absent: n comparisons, O(n).</p>
<p><b>Average case:</b> the expected time over all inputs of size n, assuming a distribution of inputs (usually
all equally likely). e.g. linear search for an item present at a random position: about n/2 comparisons — still
O(n).</p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>Best ≤ average ≤ worst.</li><li>Big O drops constants: n/2 and n are both O(n).</li></ul>"),

    Q("2(e)", 2, r"<p>Write the RPN for the infix expression P+T/Q*(G*(R+K)/M*(N-J)/S)+L</p>",
      a=r"<p>RPN = Reverse Polish (postfix) notation. Scanning left to right with an operator stack:</p>" + RPN_TABLE +
      r"<p>RPN: <span class=\"box\">P T Q / G R K + * M / N J − * S / * + L +</span></p>",
      topic="Data Structures (infix to postfix)",
      recall=r"<ul><li>Operands to output; on an operator, pop stacked operators of higher or equal precedence (left-associative).</li><li>'(' is pushed; ')' pops back to it.</li></ul>"),

    Q("3", 5, r"""<p>Predict the output of the following code with n = 8. Show the dry run/working</p>
<pre class="code">public static void mystery (int n) {
       if (n &lt;= 1) {
           System.out.print(": ");}
       else {
           System.out.print((n % 2) + " ");
           mystery (n/2);
           System.out.print(n + " ");
       }
}</pre>""",
      a=r"""<p>Each call prints n % 2 <i>before</i> recursing (on the way down) and n <i>after</i> (on the way back).</p>""" +
      tt(["Call", "Prints before the call", "Recursive call", "Prints after it returns"],
         [["mystery(8)", "8 % 2 = 0 → '0 '", "mystery(4)", "'8 '"],
          ["mystery(4)", "4 % 2 = 0 → '0 '", "mystery(2)", "'4 '"],
          ["mystery(2)", "2 % 2 = 0 → '0 '", "mystery(1)", "'2 '"],
          ["mystery(1)", "n ≤ 1 → ': '", "—", "—"]]) +
      r"""<p>Unwinding prints 2, then 4, then 8. Output:</p><p><span class="box"><code>0 0 0 : 2 4 8</code></span></p>
<p>(Confirmed by running the method.)</p>""",
      topic="Recursion",
      recall=r"<ul><li>Statements before the recursive call run top-down; those after it run in reverse (stack unwinding).</li><li>Integer division: 8/2 = 4, 4/2 = 2, 2/2 = 1.</li></ul>"),

    SEC("Part II — Section A", "Answer any two questions."),

    Q("4(a)(i)", 4, r"""<p>Given the Boolean function \(F(A,B,C,D) = \Sigma(0,1,2,3,5,8,9,10,11,13,14,15)\)</p>
<p>i) Reduce the above expression by using 4-variable Karnaugh map, showing the various groups (i.e. octal, quads and pairs).</p>""",
      a=r"""{{fig:0}}<ul><li>Octet (m0, m1, m2, m3, m8, m9, m10, m11) — rows A′B′ and AB′: \(B'\)</li>
<li>Quad (m1, m5, m9, m13) — column C′D: \(C'D\)</li>
<li>Quad (m10, m11, m14, m15) — rows AB, AB′ × columns CD, CD′: \(AC\)</li></ul>
<p><span class="box">\(F(A,B,C,D) = B' + C'D + AC\)</span></p>""",
      afig=[F.fig_q4a_kmap],
      topic="Boolean Algebra (Karnaugh maps)",
      recall=r"<ul><li>Gray order 00, 01, 11, 10; top and bottom rows are adjacent.</li><li>Octet → 1 literal, quad → 2, pair → 3.</li></ul>"),

    Q("4(a)(ii)", 1, r"<p>ii) Draw the logic diagram for the reduced expression using basic gates. Assume that the variables and their complements are available as inputs.</p>",
      a=r"<p>\(F = B' + C'D + AC\): two AND gates and a 3-input OR gate.</p>{{fig:0}}",
      afig=[F.fig_q4a_circuit],
      topic="Boolean Algebra (logic diagrams)",
      recall=r"<ul><li>SOP → AND gates feeding one OR gate; a single literal goes straight to the OR.</li></ul>"),

    Q("4(b)(i)", 4, r"""<p>Given the Boolean function \(F(A,B,C,D) = \pi(3,4,5,6,7,9,11,13)\)</p>
<p>i) Reduce the above expression by using 4-variable Karnaugh map, showing the various groups (i.e. octal, quads and pairs).</p>""",
      a=r"""{{fig:0}}<ul><li>Quad (M4, M5, M6, M7) — row A+B′: \((A + B')\)</li>
<li>Pair (M3, M11) — column C′+D′, rows A+B and A′+B: \((B + C' + D')\)</li>
<li>Pair (M9, M13) — column C+D′, rows A′+B′ and A′+B: \((A' + C + D')\)</li></ul>
<p><span class="box">\(F(A,B,C,D) = (A + B')(B + C' + D')(A' + C + D')\)</span></p>""",
      afig=[F.fig_q4b_kmap],
      topic="Boolean Algebra (Karnaugh maps)",
      recall=r"<ul><li>POS: group the 0s; a variable that is 0 throughout the group appears plain, 1 appears complemented.</li><li>No octet exists here: cover with the largest groups available.</li></ul>"),

    Q("4(b)(ii)", 1, r"<p>ii) Draw the logic diagram for the reduced expression using basic gates. Assume that the variables and their complements are available as inputs.</p>",
      a=r"<p>\(F = (A + B')(B + C' + D')(A' + C + D')\): three OR gates feeding a 3-input AND gate.</p>{{fig:0}}",
      afig=[F.fig_q4b_circuit],
      topic="Boolean Algebra (logic diagrams)",
      recall=r"<ul><li>POS → OR gates feeding one AND gate.</li></ul>"),

    Q("5(a)", 5, r"""<p>The computer department of a school has organized an IT fest which will be held at the school campus.
An invitation is issued to an ex-student if</p>
<p>The person is an ex-student of the department and had passed out in 2015.<br><b>OR</b><br>
The person is not an ex-student of the same department but passed out from school in 2015 and is a member of the school
alumni.</p>
<p>The <b>inputs</b> are:<br>E: The person is an ex-student of the department.<br>
F: The person is not an ex-student of the department, but a student of the same school.<br>
G: The person passed out in 2015<br>H: The person is a member of the school alumni.<br>
[1 indicates yes and 0 indicates no in all cases]</p>
<p><b>Output</b><br>I (Denotes the invitation card is issued.) [1 indicates yes and 0 indicates no]</p>
<p>(a) Draw the truth table for the inputs and outputs given above and write the <b>POS</b> expression for I(E,F,G,H).<br>
(b) Reduce I(E,F,G,H) using karnaugh map.</p>""",
      a=r"""<p>From the conditions: \(I = E\cdot G\ +\ F\cdot G\cdot H\). I = 1 in rows 7 (0111), 10 (1010), 11 (1011),
14 (1110), 15 (1111).</p>""" +
      tt(["E", "F", "G", "H", "I"],
         [[(r >> 3) & 1, (r >> 2) & 1, (r >> 1) & 1, r & 1, 1 if r in (7, 10, 11, 14, 15) else 0] for r in range(16)]) +
      r"""<p>POS expression (the rows where I = 0):</p>
<p><span class="box">\(I(E,F,G,H) = \pi(0,1,2,3,4,5,6,8,9,12,13)\)</span></p>
<p>i.e. \(I = (E+F+G+H)(E+F+G+H')(E+F+G'+H)(E+F+G'+H')(E+F'+G+H)(E+F'+G+H')(E+F'+G'+H)(E'+F+G+H)(E'+F+G+H')(E'+F'+G+H)(E'+F'+G+H')\)</p>
<p><b>(b) Reduction</b> — K-map of the 0s:</p>{{fig:0}}
<ul><li>Octet (M0, M1, M4, M5, M8, M9, M12, M13) — columns G+H and G+H′: \((G)\)</li>
<li>Quad (M0, M1, M2, M3) — row E+F: \((E + F)\)</li>
<li>Quad (M0, M2, M4, M6) — rows E+F, E+F′ with the two end columns: \((E + H)\)</li></ul>
<p><span class="box">\(I(E,F,G,H) = G\,(E + F)(E + H)\)</span> &nbsp; (= \(EG + FGH\), as the conditions say)</p>
<p class="note">E = 1 with F = 1 cannot actually occur (F says "not an ex-student of the department"); treating
those four rows as don't-cares would not change this result.</p>{{fig:1}}""",
      afig=[F.fig_q5a_kmap, F.fig_q5a_circuit],
      topic="Boolean Algebra (word problems, Karnaugh maps)",
      recall=r"<ul><li>Turn each condition into a product term, then OR them.</li><li>POS cardinal form lists the rows where the output is 0.</li><li>Group the 0s for a POS reduction.</li></ul>"),

    Q("5(b)", 5, r"""<p>Using the following truth table design a circuit with a decoder and external gates. Also write the SOP expression
for the functions F<sub>1</sub>, F<sub>2</sub>, F<sub>3</sub>.</p><p><b>Truth Table</b></p>""" +
      tt(["x", "y", "z", "x′", "xy", "xz", "x′y", "F1", "F2", "F3"],
         [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
          [1, 1, 0, 0, 1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1]]),
      a=r"""<p>Reading the 1s of each output (row number = xyz in binary):</p>
<p>\(F_1 = \Sigma(0, 5, 7) = x'y'z' + xy'z + xyz = x'y'z' + xz\)</p>
<p>\(F_2 = \Sigma(2, 3, 5) = x'yz' + x'yz + xy'z = x'y + xy'z\)</p>
<p>\(F_3 = \Sigma(1, 6, 7) = x'y'z + xyz' + xyz = xy + x'y'z\)</p>
<p>(The helper columns x′y, xz, xy are exactly the terms that appear in the simplified forms.)</p>
<p><b>Circuit:</b> a 3-to-8 decoder with x, y, z as inputs (x the most significant) makes every minterm
D0 … D7 available; each function is the OR of its minterm lines.</p>{{fig:0}}""",
      afig=[F.fig_q5b_decoder],
      topic="Computer Hardware (decoders)",
      recall=r"<ul><li>An n-to-2ⁿ decoder outputs every minterm: \(D_i\) = 1 only for input i.</li><li>Any function = OR of the decoder outputs for its minterms.</li></ul>"),

    Q("6(a)", 2, r"<p>Verify the following law by using the truth table. \((A \oplus B \oplus C)' = A \odot B \oplus C\)</p>",
      a=tt(["A", "B", "C", "A ⊕ B ⊕ C", "(A ⊕ B ⊕ C)′", "A ⊙ B", "(A ⊙ B) ⊕ C"],
           [[a, b, c, a ^ b ^ c, 1 - (a ^ b ^ c), 1 - (a ^ b), (1 - (a ^ b)) ^ c]
            for a in (0, 1) for b in (0, 1) for c in (0, 1)]) +
      r"""<p>(⊙ and ⊕ are taken left to right: \(A\odot B\) first, then \(\oplus\,C\).)</p>
<p>The columns \((A\oplus B\oplus C)'\) and \(A\odot B\oplus C\) are identical in all eight rows, hence
<span class="box">\((A\oplus B\oplus C)' = A\odot B\oplus C\)</span> &nbsp; — the law is verified.</p>
<p>(Reason: \(A\odot B = (A\oplus B)'\), and complementing one input of an XOR complements its output, so
\((A\oplus B)'\oplus C = (A\oplus B\oplus C)'\).)</p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>XOR of several bits is 1 when an odd number of them are 1.</li><li>\(X\odot Y = (X\oplus Y)' = XY + X'Y'\).</li><li>\(X'\oplus Y = (X\oplus Y)'\): complementing one XOR input complements the output.</li></ul>"),

    Q("6(b)", 3, r"""<p>Analyze the combinational circuit and find the Boolean expression for the two outputs F<sub>1</sub> and
F<sub>2</sub> as a function of the three inputs and then simplify.</p>""",
      qfig=F.fig_q6b_circuit,
      a=r"""<p>Writing each gate's output on the diagram:</p>{{fig:0}}
<p>\(F_2 = AB + (A + B)C = AB + AC + BC\) — the <b>carry</b> (majority) function.</p>
<p>\(F_1 = F_2'\,(A + B + C) + ABC\)</p>
<p>\(F_2' = (AB + BC + CA)' = (A' + B')(B' + C')(C' + A') = A'B' + B'C' + C'A'\)</p>
<p>\(F_2'(A + B + C) = AB'C' + A'BC' + A'B'C\)</p>
<p><span class="box">\(F_1 = A'B'C + A'BC' + AB'C' + ABC = A \oplus B \oplus C\)</span> — the <b>sum</b>;</p>
<p><span class="box">\(F_2 = AB + BC + CA\)</span> — the <b>carry</b>. The circuit is a <b>full adder</b>.</p>""",
      afig=[F.fig_q6b_labelled],
      topic="Computer Hardware (full adder)",
      recall=r"<ul><li>Full adder: SUM = \(A\oplus B\oplus C\), CARRY = \(AB + BC + CA\).</li><li>Label every gate's output, then simplify.</li></ul>"),

    Q("6(c)", 2, r"<p>Draw the logic diagram of a Decimal to Binary encoder.</p>",
      a=r"""<p>Ten inputs D0–D9 (one active at a time), four outputs A3 A2 A1 A0 giving the BCD code:</p>
<p>\(A_3 = D_8 + D_9,\ A_2 = D_4 + D_5 + D_6 + D_7,\ A_1 = D_2 + D_3 + D_6 + D_7,\ A_0 = D_1 + D_3 + D_5 + D_7 + D_9\)</p>{{fig:0}}
<p>(D0 → 0000 needs no connection.)</p>""",
      afig=[F.fig_q6c_encoder],
      topic="Computer Hardware (encoders)",
      recall=r"<ul><li>Output bit k = OR of the inputs whose number has bit k set.</li><li>Decimal → 4-bit code: 10 inputs, 4 outputs.</li></ul>"),

    Q("6(d)", 3, r"""<p>Write two applications of a multiplexer and write down the simplified SOP expression for the following block diagram.</p>
{{fig:0}}<p>where P is the select line, a+b is I<sub>0</sub> and ab is I<sub>1</sub> (I<sub>n</sub> stands for input).</p>""",
      qfig=F.fig_q6d_mux,
      a=r"""<p><b>Applications:</b> (i) data routing / selecting one of many data sources onto a single line (e.g. in
communication systems and CPU data paths); (ii) parallel-to-serial conversion; also implementing any Boolean function
without separate gates.</p>
<p><b>Expression.</b> A 2:1 MUX gives \(F = P'I_0 + PI_1\):</p>
<p>\(F = P'(a + b) + P\,ab = P'a + P'b + Pab\)</p>
<p>\(P'ab\) is already covered by \(P'a\), so it may be added without changing F:
\(Pab + P'ab = ab(P + P') = ab\). Hence</p>
<p><span class="box">\(F = P'a + P'b + ab\)</span></p>
<p class="note">[The output is labelled F(P, x, y) but the inputs are written in a and b; the answer is in a and b
(read x = a, y = b).]</p>{{fig:0}}""",
      afig=[F.fig_q6d_gates],
      topic="Computer Hardware (multiplexers)",
      recall=r"<ul><li>2:1 MUX: \(Y = S'I_0 + SI_1\).</li><li>A term already covered may be added: \(X + XY = X\), then combine \(Pab + P'ab = ab\).</li></ul>"),

    SEC("Part II — Section B", "Answer any two questions. Each program should be written in such a way that it clearly "
        "depicts the logic of the problem. This can be achieved by using mnemonic names and comments in the program. "
        "(Flowcharts and Algorithms are not required.) The programs must be written in Java."),

    Q("7", 10, r"""<p>Design a class SeriesSum to compute the sum of the following series. Some of the data members and member
functions are given below:</p>
\[\text{Sum} = 1 + \frac{x}{1!} + \frac{x^3}{2!} + \frac{x^5}{3!} + \dots + \frac{x^{2n-1}}{n!}\]
<p>Class Name : SeriesSum<br>Data Members<br>n : integer number<br>x : integer number<br>sum : double type to store the sum.<br>
Member Functions<br>SeriesSum(int,int) : to initialize the data member n = nn and x = xx.<br>
void calcSeries() : to calculate the sum of the series<br>
int power(int,int) : calculate the result when a number is raised to a power using recursion<br>
int factorial(int) : to calculate the factorial of a number using recursion<br>void display() : to show the result</p>
<p>Specify the class <b>SeriesSum</b> giving the details of the constructor and member functions
<b>SeriesSum(int,int), void calcSeries(), int power(int,int), int factorial(int), void display()</b> with the
<b>main()</b> function to create an object and call the member function accordingly to enable the task.</p>""",
      a=r"""<p>The i-th term (i = 1 … n) is \(x^{2i-1}/i!\); the cast to double stops integer division.</p>""" +
      jcode(M, "SeriesSum.java") + r"<p>Runs (n = 3, x = 2: \(1 + 2 + 8/2 + 32/6 = 12.33\dots\); n = 4, x = 1):</p>" +
      jout(M, "series1") + jout(M, "series2"),
      topic="Recursion / Methods",
      recall=r"<ul><li>Recursive power: \(x^p = x\cdot x^{p-1}\), \(x^0 = 1\); factorial: \(m! = m(m-1)!\), \(0! = 1\).</li><li>Cast to double before dividing ints.</li></ul>"),

    Q("8", 10, r"""<p>Design a class ParagraphSort to arrange the sentences in a paragraph in decreasing order of their number of
words. The sentences in the paragraph is terminated by either a full stop '.', question mark '?' or an exclamation mark
'!'. Some of the data members and member functions are given below:</p>
<p>Class Name : ParagraphSort<br>Data Members :<br>str : to store the paragraph.<br>lines[] : array to store the sentences
separately<br>wrds[] : array to store number of words in each sentence</p>
<p>Member Functions :<br>void print(String lines[],int wrds[]) : to print the result along with the number of words in each sentence.<br>
int countWords(String str) : to count the number of words in each sentence.<br>
void sort(String lines[],int wrds[]) : to sort the paragraph in decreasing order of the number of words in each
sentence.<b>(largest sentence should be the first to appear)</b></p>
<p>Specify the class <b>ParagraphSort</b> giving details of all the member functions. Also write the main method to call
the functions accordingly.</p>""",
      a=r"""<p>A constructor and a <code>split()</code> method (to fill <code>lines[]</code> and <code>wrds[]</code>) are
added; the sort swaps a sentence together with its word count.</p>""" + jcode(M, "ParagraphSort.java") +
      jout(M, "para1") + jout(M, "para2"),
      topic="Arrays, Strings",
      recall=r"<ul><li>Sentence ends: '.', '?', '!'; words = blank-separated tokens.</li><li>Parallel arrays: swap both together while sorting.</li></ul>"),

    Q("9", 10, r"""<p>The sum of angles is calculated as :<br>Let the first angle = 15 degrees 45 minutes<br>
Let the second angle = 12 degrees 40 minutes<br>The sum of angles will be 28 degrees 25 minutes. (where 60 minutes = 1 degree)</p>
<p>Design a class Angle with the following details:<br>Class name : Angle<br>Data members/instance variables :<br>
deg : integer to store degrees.<br>min : integer to store minutes.<br>Member functions/methods<br>
Angle( ) : constructor to assign 0 to deg and min<br>void inputAngle() : to input values of deg and min.<br>
void dispAngle() : to print the values of deg and min with proper message.<br>
Angle sumAngle(Angle A, Angle B) : to find and return the sum of angles from objects A and B by using the above
technique of adding angles</p>
<p>Specify the class <b>Angle</b> giving the details of the constructors and all the functions. You need not write the main function.</p>""",
      a=jcode(M, "AngleRun.java") +
      r"<p>Test (main used only for testing): the paper's example, and one where the minutes carry exactly 1°:</p>" +
      jout(M, "angle1") + jout(M, "angle2"),
      topic="Objects (objects as parameters and return values)",
      recall=r"<ul><li>minutes = (m₁ + m₂) % 60; carry = (m₁ + m₂) / 60.</li><li>A method can create and return a new object.</li></ul>"),

    SEC("Part II — Section C", "Answer any two questions. The programs must be written in Java and the algorithms must be "
        "written in general / standard form, wherever required / specified. (Flowcharts are not required.)"),

    Q("10", 5, r"""<p>A class <b>Personal</b> contains employee details and another class <b>Retire</b> calculates the employee's
provident fund and gratuity. The details of the two classes are given below:</p>
<p>Class Name : Personal<br>Data Members :<br>empName : stores the employee name<br>Pan : stores the employee pan number<br>
basic-pay : stores the employee basic salary(in decimals)<br>acc_no : stores the employee bank account number<br>
Member functions<br>Personal(…) : parameterised constructor to assign values to data members<br>
void display() : to display the employee details</p>
<p>Class Name : Retire<br>Data Members :<br>yrs : stores the employee's years of service<br>
pf : stores the employee's provident fund amount (in decimals)<br>grat : stores the employees's gratuity amount (in decimals)<br>
Member Functions :<br>Retire(…) : parameterized constructor to assign values to data members<br>
void provident() : calculates the PF as (2% of the basic pay)*years of service<br>
void gratuity() : calculates the gratuity as 12 months' salary, if the years of service is more than or equal to 10
years else the gratuity amount is nil.<br>void display1() : displays the employee details along with the pf and gratuity amount.</p>
<p>Specify the class <b>Personal</b> giving details of the constructor and the member function <b>void display()</b>.
Using the concept of <b>inheritance</b> specify the class <b>Retire</b> giving details of constructor and the member
function <b>void provident(), void gratuity()</b> and <b>void display1()</b>. The main function needs to be written.</p>""",
      a=r"""<p class="note">["basic-pay" is not a legal Java identifier (the hyphen is the minus operator); it is written
<code>basicPay</code>. "12 months' salary" is taken as 12 × basic pay.]</p>""" + jcode(M, "Retire.java") +
      r"<p>Runs (12 years: PF = 0.02 × 30000 × 12 = 7200, gratuity = 12 × 30000; 7 years: gratuity nil):</p>" +
      jout(M, "retire1") + jout(M, "retire2"),
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li><code>class Retire extends Personal</code>; <code>super(…)</code> passes the personal details up.</li><li>The subclass calls the inherited <code>display()</code> inside <code>display1()</code>.</li></ul>"),

    Q("11", 5, r"""<p>Pipe is an entity which can hold at the most 50 integers. The pipe enables the user to add and remove integers.
Define a class Pipe with the following details.</p>
<p>Class Name : Pipe<br>Data Members<br>item[] : the array to hold the integer elements<br>cap : stores the maximum capacity of the array<br>
front : to point to the index of the front<br>rear : to point to the index of the rear.</p>
<p>Member Functions<br>Pipe(int max) : constructor to initialize the data member cap=max, front =rear=-1 and to create the integer array.<br>
void pushrear(int v) : to add integers from the rear index if possible else display the message ("Rear full")<br>
int popfront() : to remove the elements from front. If array is empty then return -999.<br>
int poprear() : to remove elements from the rear. If the array is empty then return -999.<br>
void display() : to display the array.</p>
<p>Specify the class Pipe giving details of the constructor and the member function <b>void pushrear(int), int popfront(),
int poprear()</b> and <b>void display()</b>. The main method need not be written.</p>""",
      a=r"""<p>This is an <b>input-restricted dequeue</b>: insertion only at the rear, deletion at both ends. When the last
element is removed, front and rear are reset to −1.</p>""" + jcode(M, "PipeRun.java") +
      r"<p>Test with capacity 3 (main used only for testing): push 10, 20, 30, 40 (full), then pops from both ends:</p>" +
      jout(M, "pipe"),
      topic="Data Structures (queue / dequeue)",
      recall=r"<ul><li>Empty: front = rear = −1; full (linear): rear = cap − 1.</li><li>Removing the only element resets both pointers.</li></ul>"),

    Q("12(a)", 3, r"<p>Write down the postorder, inorder and preorder traversal of the following binary tree.</p>",
      qfig=F.fig_q12a_tree,
      a=r"""<p>(E has only a right child I; F has only a right child J.)</p>
<p><b>Postorder</b> (L R N): <span class="box">I E J F C G K L H D B M A</span></p>
<p><b>Inorder</b> (L N R): <span class="box">E I C F J B G D K H L A M</span></p>
<p><b>Preorder</b> (N L R): <span class="box">A B C E I F J D G H K L M</span></p>""",
      topic="Data Structures (binary trees)",
      recall=r"<ul><li>Pre N-L-R, In L-N-R, Post L-R-N, recursively.</li><li>A node with only a right child: in inorder it comes <i>before</i> that child.</li></ul>"),

    Q("12(b)", 2, r"""<p>A linked list is formed from the objects of the class,</p>
<pre class="code">class ListNode
{
  float data;
  ListNode ptr;
}</pre>
<p>Write a method Or an algorithm to compute and return the sum of all float data stored in the linked list. The method
declaration is specified below:<br><b>float addList(ListNode head)</b></p>""",
      a=r"""<p><b>Algorithm:</b> 1. sum ← 0, temp ← head. 2. While temp ≠ null: sum ← sum + temp.data; temp ← temp.ptr.
3. Return sum.</p>{{fig:0}}<p><b>Method:</b></p>""" + jcode(M, "AddList.java") +
      r"<p>Test on 2.5 → 4.0 → 1.25 → 3.75 and on an empty list:</p>" + jout(M, "addlist"),
      afig=[F.fig_q12b_list],
      topic="Data Structures (single linked list)",
      recall=r"<ul><li>Traverse with a temporary reference; never move head.</li><li>Stop when the reference becomes null (handles an empty list too).</li></ul>"),
]

PAPER = dict(
    subject="computers",
    year="2016-17",
    slug="2016-17-paper-1",
    paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2016-17/COMPUTER SCIENCE PAPER I.pdf",
    marks=70, time="3 hours",
    intro=r"""<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start writing during
this time).</p>
<p><i>Answer <b>all</b> questions in Part I (compulsory) and <b>six</b> questions from Part II, choosing <b>two</b>
questions from Section - A, <b>two</b> from Section - B and <b>two</b> from Section - C. All working, including rough
work should be done on the same sheet as the rest of the answer. The intended marks for questions or parts of questions
are given in the brackets [].</i></p><p>This question paper consists of 8 printed pages.</p>""",
    items=ITEMS,
)
