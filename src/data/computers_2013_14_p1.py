"""Computer Science Pre-Board 2013-14, Paper 1 (Theory) -- Heritage School."""
from kit import Q, SEC
import computers_2013_14_figs as F
from _computers_a_util import code, sample, pre, tt, table

M = "computers_2013_14_p1"
X = lambda a, b: a ^ b

INTRO = r"""<p><i>(Candidates are allowed additional 15 minutes for only reading the paper. They must not
start writing during this time.)</i></p>
<p>Answer <b>all</b> questions in Part I (compulsory) and seven questions from Part II, choosing three
questions from Sec A, two questions from Sec B and two questions from Sec C. All working, including
rough work, should be done on the same sheet as the rest of the answer. The intended marks of the
questions or parts of questions are given in brackets ( ). <b>Full marks is 100.</b></p>"""

ITEMS = [
    SEC("Part I", "(Compulsory)"),

    Q("1", 2, r"<p>State Idempotent law of Boolean Algebra and prove using truth table.</p>",
      a=r"""<p><b>Idempotent law:</b> a variable ORed or ANDed with itself gives the variable itself:</p>
<p style="text-align:center">(a) \(A + A = A\) &nbsp;&nbsp;&nbsp; (b) \(A \cdot A = A\)</p>
<p><b>Proof by truth table</b></p>""" + tt(["A"], [("A + A", lambda a: a | a), ("A&middot;A", lambda a: a & a)]) +
      r"""<p>The columns \(A+A\) and \(A\cdot A\) are identical to the column \(A\) in every row, hence
<span class="box">\(A+A=A\) and \(A\cdot A=A\)</span>.</p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Idempotence: \(A+A=A\), \(A\cdot A=A\).</li><li>A law is proved by a truth table when the two sides have identical columns for every input combination.</li></ul>"),

    Q("2", 2, r"""<p>Draw truth tables to verify the following:</p>
<p style="text-align:center">( P XOR Q XOR R )&prime; = P XOR Q XNOR R</p>""",
      a=r"""<p>Read the right-hand side left to right as \((P\oplus Q)\odot R\) (XNOR = complement of XOR).</p>""" +
      tt(["P", "Q", "R"], [
          (r"P&oplus;Q", lambda p, q, r: p ^ q),
          (r"P&oplus;Q&oplus;R", lambda p, q, r: p ^ q ^ r),
          (r"(P&oplus;Q&oplus;R)&prime;", lambda p, q, r: 1 - (p ^ q ^ r)),
          (r"(P&oplus;Q) XNOR R", lambda p, q, r: 1 - ((p ^ q) ^ r)),
      ], hl={2, 3}) +
      r"""<p>The last two columns are identical in all 8 rows, so
<span class="box">(P XOR Q XOR R)&prime; = P XOR Q XNOR R</span> is verified. (Reason: \(X \odot R = (X\oplus R)'\)
with \(X = P\oplus Q\).)</p>
<p>The two sides as circuits (not required, but they show why the identity holds):</p>{{fig:0}}""",
      afig=[(F.fig_q2_xor, "Both circuits give the same output for every input.")],
      topic="Computer Hardware (logic gates)",
      recall=r"<ul><li>XOR is 1 when an odd number of inputs are 1.</li><li>XNOR \(= (A\oplus B)'\): 1 when the inputs are equal.</li><li>XOR is associative, so \(P\oplus Q\oplus R\) needs no brackets.</li></ul>"),

    Q("3", 2, r"""<p>Simplify algebraically \(\;\overline{[(\bar p+q)\cdot(\bar q+r)]}+(\bar p+r)\)</p>""",
      a=r"""<p>\[
\begin{aligned}
F &= \overline{(\bar p+q)(\bar q+r)}+\bar p+r\\
  &= \overline{(\bar p+q)}+\overline{(\bar q+r)}+\bar p+r &&\text{(De Morgan)}\\
  &= p\bar q+q\bar r+\bar p+r &&\text{(De Morgan, involution)}\\
  &= (\bar p+p\bar q)+(r+q\bar r)&&\text{(regrouping)}\\
  &= (\bar p+\bar q)+(r+q) &&(x'+xy = x'+y,\; x+x'y=x+y)\\
  &= \bar p+(\bar q+q)+r = \bar p+1+r &&(\bar q+q=1)\\
  &= 1
\end{aligned}\]</p>
<p><span class="box">\(F = 1\)</span> &mdash; the expression is a tautology (true for every p, q, r).</p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>De Morgan: \((xy)'=x'+y'\), \((x+y)'=x'y'\).</li><li>Redundant literal: \(x'+xy=x'+y\).</li><li>Complement law \(x+x'=1\); \(1+x=1\).</li></ul>"),

    Q("4", 2, r"""<p>Convert the following infix expression to its postfix form</p>
<pre class="code">(A-B) * (C/D)+E</pre>""",
      a=r"""<p>Brackets first, then * before +, working left to right:</p>
<p><code>(A-B)*(C/D)+E &rarr; [AB-]*(C/D)+E &rarr; [AB-]*[CD/]+E &rarr; [AB-CD/*]+E &rarr; AB-CD/*E+</code></p>""" +
      table(["Symbol", "Stack", "Postfix"], [
          ["(", "(", ""], ["A", "(", "A"], ["-", "( -", "A"], ["B", "( -", "AB"], [")", "", "AB-"],
          ["*", "*", "AB-"], ["(", "* (", "AB-"], ["C", "* (", "AB-C"], ["/", "* ( /", "AB-C"],
          ["D", "* ( /", "AB-CD"], [")", "*", "AB-CD/"], ["+", "+", "AB-CD/*"], ["E", "+", "AB-CD/*E"],
          ["end", "", "AB-CD/*E+"]]) +
      r"""<p>Postfix: <span class="box">A B &minus; C D / * E +</span></p>""",
      topic="Data Structures (infix, prefix and postfix)",
      recall=r"<ul><li>Operand → output; '(' → push; ')' → pop to the matching '('.</li><li>An operator pops every operator of higher or equal precedence (left-associative) before it is pushed.</li><li>* and / bind tighter than + and −.</li></ul>"),

    Q("5", 2, r"""<p>Given F(P,Q,R) = (P+Q) . (Q+R). Convert it to its canonical POS form using Boolean Algebra.</p>""",
      a=r"""<p>Each sum term must contain all three variables; supply the missing one with \(XX'=0\):</p>
<p>\[\begin{aligned}
P+Q &= P+Q+RR' = (P+Q+R)(P+Q+R')\\
Q+R &= Q+R+PP' = (P+Q+R)(P'+Q+R)
\end{aligned}\]</p>
<p>\(F=(P+Q+R)(P+Q+R')(P+Q+R)(P'+Q+R)\). Removing the repeated factor (idempotence, \(X\cdot X=X\)):</p>
<p><span class="box">\(F(P,Q,R)=(P+Q+R)\,(P+Q+R')\,(P'+Q+R) = \prod(0,1,4)\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Canonical POS: every maxterm contains every variable once.</li><li>Missing variable X: add \(XX'\) and use \(A+BC=(A+B)(A+C)\).</li><li>Maxterm: variable 0 → uncomplemented, 1 → complemented.</li></ul>"),

    Q("6", 2, r"""<p>A two dimentional array defined as DATA [30][40] requires 4 bytes of storage space for each element.
If the array is stored in Row-major-Order, determine the address of DATA[10][10], given the base address as 1234.</p>""",
      a=r"""<p>Taking the Java/C convention of the declaration, indices start at 0 (so the base address 1234 is the
address of DATA[0][0]); number of columns \(N=40\), \(W=4\).</p>
<p>\[\text{Address}(\text{DATA}[I][J]) = B + W\,[\,N(I-L_r)+(J-L_c)\,]\]</p>
<p>\[= 1234 + 4\,[\,40(10-0)+(10-0)\,] = 1234 + 4\times 410 = 1234+1640\]</p>
<p><span class="box">Address of DATA[10][10] = 2874</span></p>
<p class="note">If the rows and columns were numbered from 1 instead, the same formula gives
\(1234+4[40(9)+9] = 2710\). State the lower bounds you assume.</p>""",
      topic="Arrays (address calculation)",
      recall=r"<ul><li>Row-major: \(B + W[N(I-L_r)+(J-L_c)]\), N = number of columns.</li><li>Column-major: \(B + W[(I-L_r)+M(J-L_c)]\), M = number of rows.</li><li>Base address = address of the first element.</li></ul>"),

    Q("7", 2, r"<p>Find the Complement of A&prime;B&prime; + A&prime; + A.B</p>",
      a=r"""<p>Simplify first: \(A'B'+A'=A'\) (absorption), so \(F=A'+AB=A'+B\) (redundant literal).</p>
<p>\[F' = (A'+B)' = A''\cdot B' = A\,B'\]</p>
<p>Check by De Morgan directly: \((A'B'+A'+AB)'=(A+B)\cdot A\cdot(A'+B') = A(A'+B') = AA'+AB' = AB'\).</p>
<p><span class="box">Complement = \(A\cdot B'\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>De Morgan: complement each literal and swap + and \(\cdot\).</li><li>Absorption \(X+XY=X\); \(X'+XY=X'+Y\).</li></ul>"),

    Q("8", 2, r"""<p>Draw circuit of the following expression using NAND gates only.</p>
<p style="text-align:center">AB&prime; + [A&prime;( B + C&prime; )]</p>""",
      a=r"""<p>Expand into sum-of-products: \(F = AB' + A'B + A'C'\).</p>
<p>A two-level AND-OR circuit becomes NAND-NAND: \(F = \overline{\overline{AB'}\cdot\overline{A'B}\cdot\overline{A'C'}}\)
(double complement and De Morgan). The complements \(A', B', C'\) are produced by NAND gates with
their inputs tied together \((\overline{X\cdot X} = X')\).</p>{{fig:0}}
<p>Gates: 3 NAND inverters + 3 two-input NANDs + 1 three-input NAND.</p>""",
      afig=[(F.fig_q8_nand, "NAND-only circuit for F = AB′ + A′B + A′C′")],
      topic="Computer Hardware (NAND as universal gate)",
      recall=r"<ul><li>SOP → NAND-NAND: replace both levels of AND-OR by NAND.</li><li>NOT from NAND: tie the inputs, \((XX)'=X'\).</li><li>\(\overline{\overline{P}\,\overline{Q}} = P+Q\).</li></ul>"),

    Q("9", 2, r"<p>What are the differences between Quick sort and Merge sort.</p>",
      excluded="Quick sort and merge sort are not in the ISC 2027 syllabus, which lists only bubble, selection and insertion sort (Unit 10, Arrays)."),

    Q("10", 2, r"<p>Define a Binary Search Tree</p>",
      a=r"""<p>A <b>binary search tree</b> is a binary tree in which, for every node,</p>
<ul><li>every value in its <b>left</b> subtree is <b>less</b> than the node's value, and</li>
<li>every value in its <b>right</b> subtree is <b>greater</b> than the node's value;</li>
<li>the left and right subtrees are themselves binary search trees.</li></ul>
<p>Example:</p>{{fig:0}}<p>Its inorder traversal (20 30 40 50 60 70 80) is in ascending order.</p>""",
      afig=[(F.fig_q10_bst, "A binary search tree")],
      topic="Data Structures (binary trees)",
      recall=r"<ul><li>Binary tree: each node has at most two children (left, right).</li><li>BST ordering: left &lt; root &lt; right at every node.</li><li>Inorder traversal of a BST gives sorted order.</li></ul>"),

    Q("11", 4, r"<p>Explain the use of super and this keyword in terms of Inheritance.</p>",
      a=r"""<p><b>this</b> &mdash; a reference to the <i>current object</i>.</p>
<ul><li>Separates an instance variable from a parameter/local of the same name: <code>this.roll = roll;</code></li>
<li>Calls another constructor of the same class: <code>this(…)</code>; or passes the current object as an argument.</li></ul>
<p><b>super</b> &mdash; a reference to the <i>superclass part</i> of the current object.</p>
<ul><li><code>super(…)</code> calls the superclass constructor; it must be the first statement of the subclass constructor.</li>
<li><code>super.method()</code> calls the superclass version of a method the subclass has overridden;
<code>super.x</code> reaches a superclass variable hidden by a subclass variable of the same name.</li></ul>
<p>Example:</p>""" + code(M, "Q11_SuperThis.java") + r"""<p><code>new Student("Ujaan", 12).show();</code> prints</p>""" +
      pre("Name : Ujaan\nRoll : 12"),
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li>this → current object; super → its superclass part.</li><li><code>super(...)</code> must be the first statement in a constructor.</li><li>Overriding: same signature in the subclass; <code>super.m()</code> reaches the hidden version.</li></ul>"),

    Q("12", 6, r"""<p>Read the program and find the output. Show dry run / working</p>
<pre class="code">public static void main( Strings args[])throws IOException
{
    int x=10,y=5,z;
    z=first(x,y);
    System.out.println("\n z=" + z);
}
int first (int x, int y)
{
    return(x + second (y));
}
int second (int y)
{
    Return(++y);
}</pre>""",
      a=r"""<p class="note">As printed the code has slips: <code>Strings</code> should be <code>String</code>,
<code>Return</code> should be <code>return</code>, and <code>first</code>/<code>second</code> must be
<code>static</code> to be called from <code>main</code>. The intended program is traced.</p>
<p><b>Dry run</b></p>""" + table(["Call", "Parameters", "Work", "Returns"], [
          ["main", "", "x = 10, y = 5; z = first(10, 5)", ""],
          ["first(10, 5)", "x = 10, y = 5", "x + second(5)", "10 + 6 = 16"],
          ["second(5)", "y = 5", "++y makes y = 6 (pre-increment: changed, then used)", "6"],
          ["main", "", "z = 16; prints \"\\n z=\" + 16", ""]]) +
      r"""<p>The string begins with <code>\n</code>, so a blank line is printed first, then the value:</p>""" +
      pre("(blank line)\n z=16") + r"""<p><span class="box">Output: a blank line, then &nbsp;z=16</span></p>
<p>The corrected program, which was run:</p>""" + code(M, "Q12_Output.java"),
      topic="Methods",
      recall=r"<ul><li>Primitive arguments are passed by value: <code>second</code> changes its own copy of y.</li><li>Pre-increment <code>++y</code> increments, then gives the new value.</li><li><code>\n</code> inside a string starts a new line.</li></ul>"),

    SEC("Part II &mdash; Sec A", "(Answer any three)"),

    Q("13", 10, r"""<p>The immigration rules of a country allow the issue of work-cum-stay permits to an applicant only if
the applicant satisfies any one of the following conditions:</p>
<ul><li>The spouse of the applicant is a permanent resident of that country, having lived there for at least 5 years.<br><b>OR</b></li>
<li>The applicant possesses certain special skills in the &ldquo;Skill Requirement List&rdquo; of the country and is sponsored by a permanent resident of that country.</li></ul>
<p>The inputs are:<br>A: The spouse or sponsor has permanent residence status.<br>
B: The spouse has lived in the country for 5 or more years.<br>
C: The applicant possesses the required special skills.<br>
D: Sponsorship by permanent resident.</p>
<p>Output:<br>X: Denotes eligible for permit issue. [1 indicates Yes and 0 indicates No in all]</p>
<p>a) Draw a truth table for the inputs and outputs given above and write SOP expression for X(A,B,C,D).</p>
<p>b) Reduce X(A,B,C,D) using Karnaugh&rsquo;s map. Now Draw Logic gate diagram for X using AND and OR gates.
You may use gates with more than two inputs. Assume that variables and their complements are available as inputs.</p>""",
      a=r"""<p><b>Conditions.</b> First: spouse is a permanent resident (A) <i>and</i> has lived 5+ years (B) &rarr; \(AB\).
Second: applicant has the skills (C) <i>and</i> is sponsored (D) by a permanent resident (A) &rarr; \(ACD\).
So X = 1 when \(AB\) or \(ACD\) is 1.</p>
<p><b>(a) Truth table</b></p>""" +
      tt(["A", "B", "C", "D"], [("X", lambda a, b, c, d: (a & b) | (a & c & d))], hl={0}) +
      r"""<p>\(X(A,B,C,D)=\sum(11,12,13,14,15)\)</p>
<p><span class="box">\(X = AB'CD + ABC'D' + ABC'D + ABCD' + ABCD\)</span></p>
<p><b>(b) Karnaugh map</b></p>{{fig:0}}
<ul><li>Quad (m12, m13, m14, m15) = \(AB\)</li><li>Pair (m11, m15) = \(ACD\)</li></ul>
<p><span class="box">\(X = AB + ACD\)</span></p>
<p><b>Logic gate diagram</b></p>{{fig:1}}""",
      afig=[(F.fig_q13_kmap, "K-map for X"), (F.fig_q13_circ, "X = AB + ACD with AND and OR gates")],
      topic="Boolean Algebra (K-maps)",
      recall=r"<ul><li>Turn each condition into an AND term; 'any one of' → OR them.</li><li>K-map rows/columns in Gray code: 00, 01, 11, 10.</li><li>Group 1s in 1, 2, 4, 8 cells; largest groups, fewest groups.</li></ul>"),

    Q("14(a)(i)", 4, r"""<p>a) Given F(A,B,C,D) = &Sigma; (1,6,7,8,9,10,14,15)</p>
<p>i. Reduce the above expression by using 4 &ndash; variable K-Map, showing the various groups ( i.e octal, quads and pairs ).</p>""",
      a=r"""{{fig:0}}
<ul><li>Quad (m6, m7, m14, m15) = \(BC\)</li>
<li>Pair (m1, m9) = \(B'C'D\) &nbsp;(top and bottom rows wrap)</li>
<li>Pair (m8, m10) = \(AB'D'\) &nbsp;(left and right columns wrap)</li></ul>
<p>No octet is possible. <span class="box">\(F = BC + B'C'D + AB'D'\)</span></p>""",
      afig=[(F.fig_q14a_kmap, "K-map for Σ(1,6,7,8,9,10,14,15)")],
      topic="Boolean Algebra (K-maps)",
      recall=r"<ul><li>Cell number = binary ABCD; Gray-code order 00, 01, 11, 10.</li><li>Opposite edges of the map are adjacent (wrap-around).</li><li>A quad drops 2 variables, a pair drops 1.</li></ul>"),

    Q("14(a)(ii)", 1, r"<p>ii. Draw the Logic gate diagram of the reduced expression.</p>",
      a=r"""{{fig:0}}""",
      afig=[(F.fig_q14a_circ, "F = BC + B′C′D + AB′D′ (complements taken as available inputs)")],
      topic="Computer Hardware (logic gates)",
      recall=r"<ul><li>SOP → one AND gate per product term, one OR gate to combine them.</li></ul>"),

    Q("14(b)(i)", 4, r"""<p>b) Given F(A,B,C,D) = &Pi; ( 0,2,3,4,5,11,12,13)</p>
<p>i. Reduce the above expression by using 4 &ndash; variable K-Map, showing the various groups ( i.e octal, quads and pairs ).</p>""",
      a=r"""<p>Place 0s in the maxterm cells and group the 0s. Row/column labels are sum terms.</p>{{fig:0}}
<ul><li>Quad (M4, M5, M12, M13) = \((B'+C)\)</li>
<li>Pair (M0, M2) = \((A+B+D)\) &nbsp;(left and right columns wrap)</li>
<li>Pair (M3, M11) = \((B+C'+D')\) &nbsp;(top and bottom rows wrap)</li></ul>
<p><span class="box">\(F = (B'+C)(A+B+D)(B+C'+D')\)</span></p>""",
      afig=[(F.fig_q14b_kmap, "POS K-map for Π(0,2,3,4,5,11,12,13)")],
      topic="Boolean Algebra (K-maps)",
      recall=r"<ul><li>POS map: group the 0s.</li><li>In a sum term a variable that is 0 appears uncomplemented, 1 complemented.</li><li>Product of the group sums gives F.</li></ul>"),

    Q("14(b)(ii)", 1, r"<p>ii. Draw the Logic gate diagram of the reduced expression.</p>",
      a=r"""{{fig:0}}""",
      afig=[(F.fig_q14b_circ, "F = (A+B+D)(B+C′+D′)(B′+C) with OR and AND gates")],
      topic="Computer Hardware (logic gates)",
      recall=r"<ul><li>POS → one OR gate per sum term, one AND gate to combine them.</li></ul>"),

    Q("15(a)", 7, r"""<p>15. a) Implement the following Boolean function with 8 X 1 multiplexer</p>
<p style="text-align:center">F(A,B,C,D) = &Sigma; ( 0,3,5,6,8,9,14,15)</p>""",
      a=r"""<p>Use A, B, C as the select lines \(S_2S_1S_0\) of the 8 : 1 MUX and feed each data input
\(I_k\) with 0, 1, D or D&prime;. For select value k the two minterms are \(2k\) (D = 0) and \(2k+1\) (D = 1):</p>""" +
      table(["A B C (select)", "minterms", "F when D=0", "F when D=1", "Input I<sub>k</sub>"], [
          ["0 0 0 (I<sub>0</sub>)", "0, 1", "1", "0", "D&prime;"],
          ["0 0 1 (I<sub>1</sub>)", "2, 3", "0", "1", "D"],
          ["0 1 0 (I<sub>2</sub>)", "4, 5", "0", "1", "D"],
          ["0 1 1 (I<sub>3</sub>)", "6, 7", "1", "0", "D&prime;"],
          ["1 0 0 (I<sub>4</sub>)", "8, 9", "1", "1", "1"],
          ["1 0 1 (I<sub>5</sub>)", "10, 11", "0", "0", "0"],
          ["1 1 0 (I<sub>6</sub>)", "12, 13", "0", "0", "0"],
          ["1 1 1 (I<sub>7</sub>)", "14, 15", "1", "1", "1"]]) +
      r"""<p><span class="box">I<sub>0</sub>=D&prime;, I<sub>1</sub>=D, I<sub>2</sub>=D, I<sub>3</sub>=D&prime;,
I<sub>4</sub>=1, I<sub>5</sub>=0, I<sub>6</sub>=0, I<sub>7</sub>=1; select lines A B C</span></p>{{fig:0}}
<p>For each select combination the MUX passes the one data line chosen, which equals F for that
combination; e.g. ABC = 011 selects I<sub>3</sub> = D&prime;, giving F = 1 for m6 (D = 0) and 0 for m7.</p>""",
      afig=[(F.fig_q15_mux, "F implemented with an 8 : 1 multiplexer")],
      topic="Computer Hardware (multiplexers)",
      recall=r"<ul><li>A \(2^n:1\) MUX has n select lines; output = the data input whose index is the select value.</li><li>For n+1 variables: n select lines, the last variable (or its complement, 0, 1) on the data inputs.</li></ul>"),

    Q("15(b)", 3, r"<p>b) Prove that F(A,B,C) = &Pi;(2,3,4,7) = &Sigma;(0,1,5,6)</p>",
      a=r"""<p>Write the truth table of \(F=\prod(2,3,4,7)\): F is 0 exactly in rows 2, 3, 4, 7 and 1 elsewhere.</p>""" +
      tt(["A", "B", "C"], [("row", lambda a, b, c: 4 * a + 2 * b + c),
                           ("F = &Pi;(2,3,4,7)", lambda a, b, c: 0 if 4 * a + 2 * b + c in (2, 3, 4, 7) else 1)], hl={1}) +
      r"""<p>The rows where F = 1 are 0, 1, 5, 6. Since a function's minterms are exactly the rows not among its
maxterms (the 8 rows split between them), F = m0 + m1 + m5 + m6:</p>
<p><span class="box">\(\prod(2,3,4,7)=\sum(0,1,5,6) = A'B'C' + A'B'C + AB'C + ABC'\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Minterm indices and maxterm indices of a function are complementary sets of rows.</li><li>\(M_i = m_i'\).</li></ul>"),

    Q("16(a)", 4, r"<p>16 a) Using two half adder and an OR gate construct a full adder.</p>",
      a=r"""<p>Half adder: \(S = a\oplus b\), \(C = ab\). Full adder: \(\text{SUM} = A\oplus B\oplus C\),
\(\text{CARRY} = AB + C(A\oplus B)\).</p>
<ul><li>Half adder 1 adds A and B: \(S_1 = A\oplus B\), \(C_1 = AB\).</li>
<li>Half adder 2 adds \(S_1\) and C: \(\text{SUM} = A\oplus B\oplus C\), \(C_2 = C(A\oplus B)\).</li>
<li>OR gate: \(\text{CARRY} = C_1 + C_2 = AB + C(A\oplus B)\).</li></ul>{{fig:0}}
<p>The same circuit drawn with gates (each half adder is one XOR and one AND):</p>{{fig:1}}""",
      afig=[(F.fig_q16a_block, "Full adder from two half adders and an OR gate"),
            (F.fig_q16a_gates, "Gate level: 2 XOR, 2 AND, 1 OR")],
      topic="Computer Hardware (adders)",
      recall=r"<ul><li>Half adder: SUM = A⊕B, CARRY = AB.</li><li>Full adder: SUM = A⊕B⊕C, CARRY = AB + C(A⊕B) (= AB + BC + CA).</li></ul>"),

    Q("16(b)", 6, r"<p>b) Show how NAND gates can be used to simulate function of NOT, AND &amp; OR gates.</p>",
      a=r"""<p><b>NOT:</b> tie both inputs together: \(\overline{A\cdot A} = A'\).</p>{{fig:0}}
<p><b>AND:</b> NAND followed by a NAND inverter: \(\overline{\overline{AB}} = AB\).</p>{{fig:1}}
<p><b>OR:</b> invert each input with a NAND, then NAND them: \(\overline{A'\cdot B'} = A'' + B'' = A+B\) (De Morgan).</p>{{fig:2}}
<p>Since NOT, AND and OR can all be built from NAND alone, NAND is a <b>universal gate</b>.</p>""",
      afig=[(F.fig_q16b_not, "NOT from one NAND"), (F.fig_q16b_and, "AND from two NANDs"),
            (F.fig_q16b_or, "OR from three NANDs")],
      topic="Computer Hardware (universal gates)",
      recall=r"<ul><li>NAND: \((AB)'\).</li><li>De Morgan: \((A'B')' = A+B\).</li><li>Universal gate: every Boolean function can be built from it alone.</li></ul>"),

    SEC("Part II &mdash; Sec B", "(Answer any two)"),

    Q("17", 10, r"""<p>Two different timings are added as :-<br>
Time1 - 6hrs &nbsp;35 mins<br>Time2 &nbsp;3hrs &nbsp;45 mins<br>Sum &nbsp;&nbsp;10hrs &nbsp;20 mins</p>
<p>To find the solution of above question a class <b>time</b> is declared:</p>
<p><b>Data members:</b><br>hrs,min : integer to store hours and minuties</p>
<p><b>Methods :</b><br>
time( ) : Consturctor to assign 0 to hrs and min<br>
void gettime( int h, int m ) : to assign h to hrs and m to min.<br>
void printTime( ) : to display values of hrs and min<br>
time sumtime (time t1,time t2 ) : to add the timings given in the time objects t1 , t2 and returns them.</p>
<p>Write a main function to ask the user to input the values for two timings. Invoke appropriate functions
to calculate sum of time. Print the given time and added time.</p>""",
      a=r"""<p><b>Logic:</b> convert both times to minutes, add, then split back: hours = total / 60,
minutes = total % 60 (35 + 45 = 80 min = 1 h 20 min carries one hour).</p>""" + code(M, "Q17_Time.java") +
      sample(M, "Q17_Time.java"),
      topic="Objects and classes",
      recall=r"<ul><li>A method can take objects as parameters and return a new object.</li><li>Normalise with / 60 and % 60.</li><li>Scanner: <code>nextInt()</code> reads the next integer token.</li></ul>"),

    Q("18", 10, r"""<p>It is assumed that the text files &ldquo;test1.txt&rdquo; is already created with names and &ldquo;test2.txt&rdquo;
contains pan numbers of various persons. Fields present in &ldquo;test1.txt&rdquo; are person&rsquo;s code and name only.
Fields present in &ldquo;test2.txt&rdquo; are person&rsquo;s code and pan only. The pan number is beginning with a capital
alphabet followed by numbers without space. Note that the number of records in both the files are same and
person&rsquo;s code is unique.</p>
<p>Write a program to merge the files &ldquo;test1.txt and &ldquo;test2.txt&rdquo; into a new file &ldquo; pan.txt&rdquo;
in such a way that name of person and its pan number should be stored as one string having only one space between name and pan numbers.</p>""",
      excluded="Data file handling (text files, FileReader/FileWriter) is a Class XI topic in the ISC 2027 syllabus (Class XI Unit 11(b)); the Class XII syllabus (Unit 5(c)) covers only Scanner/Printer input-output and tokens."),

    Q("19", 10, r"""<p>Class <b>checker</b> has been defined to check whether a number is palindrome or not. The details of the class are given below:</p>
<p><b>Data members:</b><br>num : long integer variable to store number<br>rev : long integer variable to store reverse of number</p>
<p>Methods :<br>Checker ( long z ) : constructor to assign &lsquo;z&rsquo; to num<br>
Long ReverseNum(long q): to reverse the number stored in num using Recursive Technique and store in &lsquo;rev&rsquo;. Return the reverse number.<br>
void display( ) : to invoke recursive function and decide whether num is a palindrome number or not.
Print the number along with suitable message in both cases.</p>
<p>Do not write the main function.</p>""",
      a=r"""<p><b>Recursion:</b> each call moves the last digit of q onto the end of rev
(\(rev = rev\times10 + q\%10\)) and recurses on \(q/10\); the base case \(q = 0\) returns rev.
A number is a palindrome when it equals its reverse.</p>""" + code(M, "Q19_Checker.java") +
      r"""<p class="note">The question prints the class name as <i>checker</i> and the constructor as <i>Checker</i>, and the return
type as <i>Long</i>; Java needs the constructor name to match the class, so <code>Checker</code> and the
primitive <code>long</code> are used.</p>""" +
      sample(M, "Q19_Checker.java", "<p>Tested with 12321, 12345 and 7 (main not required by the question):</p>"),
      topic="Recursion",
      recall=r"<ul><li>Every recursive method needs a base case.</li><li>Last digit: <code>q % 10</code>; drop it: <code>q / 10</code>.</li><li>Reset rev before reversing again.</li></ul>"),

    SEC("Part II &mdash; Sec C", "(Answer any two)"),

    Q("20", 10, r"""<p>Define class basepro and derived class dervpro to find the product of two numbers details of both the classes are given below:</p>
<p>Class name : basepro<br>Data members<br>n1,n2 : float variables whose product is to be determined.<br>
Methods<br>void enter( ) : to input values of n1 and n2<br>void show( ) : to display values of n1 and n2</p>
<p>Class name : dervpro<br>Data members<br>result : float variable to store product.<br>Methods<br>
void prod( ) : to accept values of n1 and n2 and to calculate their product using the concept of inheritance.<br>
void disp( ) : to display values of n1 and n2 and their product.</p>
<p>The main function need not to be written.</p>""",
      a=r"""<p>n1 and n2 are declared <code>protected</code> so the subclass can use them; dervpro reuses
<code>enter()</code> and <code>show()</code> through inheritance.</p>""" + code(M, "Q20_Product.java") +
      sample(M, "Q20_Product.java", "<p>Test: <code>dervpro d = new dervpro(); d.prod(); d.disp();</code></p>"),
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li><code>class B extends A</code>: B inherits A's non-private members.</li><li><code>protected</code>: visible in subclasses.</li><li>Inherited methods are called directly (or as <code>super.m()</code>).</li></ul>"),

    Q("21", 10, r"""<p>Some declarations in the memory are made in such a way that can store numbers having a decimal point
also and a number can be stored either at the front or at the back depending upon the availability of space.
There may be at the most hundred numbers that can be stored. A class someprocess is defined to perform such
kind of process as given above. The details of the class someprocess are as follows:</p>
<p><b>Class name</b> : someprocess<br><b>Data members</b><br>
line [ ] : double type array to hold numbers maximum size 100.<br>
capacity : integer as the maximum storage capacity of the Line [ ].<br>
front : integer to point to the index of front of the queue.<br>
rear : integer to point to the index of rear of the quque.<br>
num : double type variable to store a number.<br>
<b>Methods</b><br>
someprocess( ) : constructor to assign 100 to capacity,-1 to front and rear.<br>
int IsEmpty( ) : returns 1 if line is empty otherwise returns 0<br>
void InsertRear( ) : accepts num if line is empty and inserts at the rear of line, otherwise output &ldquo;line is full&rdquo;.<br>
void InsertFront( ) : accepts num if line is empty and inserts at the front of line, otherwise output &ldquo;line is full&rdquo;.<br>
double DeleteFront( ) : removes the number from the front of line if the line is not empty otherwise output message &ldquo;line is empty&rdquo; and returns -999.99.<br>
double DeleteRear( ) : removes the number from the rear of line if the line is not empty otherwise output message &ldquo;line is empty&rdquo; and returns -999.99.<br>
void LineDisplay( ) : to display the elements of line if line is not empty, otherwise display message &ldquo;line is empty&rdquo;.</p>""",
      a=r"""<p>This is a <b>double-ended queue (dequeue)</b> in an array. front = rear = &minus;1 means empty.
A number can go in at the rear while rear &lt; capacity&minus;1, and at the front while front &gt; 0
(or when the line is empty).</p>
<p class="note">&ldquo;accepts num if line is empty&rdquo; is evidently meant as &ldquo;if there is space&rdquo; (if line is not full),
which is what the methods below do.</p>""" + code(M, "Q21_Someprocess.java") +
      sample(M, "Q21_Someprocess.java",
             "<p>Test sequence: display, DeleteFront on empty, InsertRear 2.5, InsertRear 4.0, InsertFront (front = 0, so full at the front), "
             "display, DeleteFront, InsertFront 1.5, display, DeleteRear twice, IsEmpty, display.</p>"),
      topic="Data Structures (dequeue)",
      recall=r"<ul><li>Dequeue: insertion and deletion at both ends.</li><li>Linear array dequeue: front insertion needs front &gt; 0; rear insertion needs rear &lt; size−1.</li><li>Reset front = rear = −1 when the last element is removed.</li></ul>"),

    Q("22(a)", 5, r"<p>22 a) Write a program to create a small balanced binary tree ( till level 2) with integer elements.</p>",
      excluded="Binary trees are only 'Conceptual' in the ISC 2027 syllabus (Unit 13(b)); writing a program to build a tree is not required."),

    Q("22(b)", 2, r"<p>b) What is a Big O Notation ? Give the notation for a quadratic time.</p>",
      a=r"""<p><b>Big O notation</b> expresses the upper bound of an algorithm's running time (or space) as a function of
the input size n, keeping only the dominant term and ignoring constant factors: \(f(n)=O(g(n))\) if
\(f(n)\le c\,g(n)\) for some constant c and all large n. It describes how the time grows as n grows.</p>
<p>Quadratic time: <span class="box">\(O(n^2)\)</span> &mdash; e.g. two nested loops each running n times (bubble sort).</p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>Keep the dominant term, drop constants: \(3n^2+5n+7 = O(n^2)\).</li><li>Common orders: \(O(1) &lt; O(\log n) &lt; O(n) &lt; O(n\log n) &lt; O(n^2)\).</li></ul>"),

    Q("22(c)", 3, r"""<p>c) For the given Binary Tree in fig:1 write the<br>
1. Postorder Sequence.<br>2. Inorder Sequence.<br>3. Preorder Sequence.</p>{{fig:0}}""",
      a=r"""<p>From the figure: R has children A (left) and 3 (right); A has C (left) and B (right); C has only a right
child D; 3 has 5 (left) and 6 (right); 5 has a left child 8; 6 has a right child 9.</p>
<p>1. Postorder (Left, Right, Root): <span class="box">D C B A 8 5 9 6 3 R</span></p>
<p>2. Inorder (Left, Root, Right): <span class="box">C D A B R 8 5 3 6 9</span></p>
<p>3. Preorder (Root, Left, Right): <span class="box">R A C D B 3 5 8 6 9</span></p>""",
      qfig=[(F.fig_q22_tree, "FIG : 1")],
      topic="Data Structures (binary trees)",
      recall=r"<ul><li>Preorder: root, left, right. Inorder: left, root, right. Postorder: left, right, root.</li><li>A missing child is simply skipped.</li></ul>"),
]

PAPER = dict(
    subject="computers", year="2013-14", slug="2013-14-paper-1", paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2013-14/Computer Science Paper 1.pdf", marks=100, time="3 hours",
    intro=INTRO, items=ITEMS)
