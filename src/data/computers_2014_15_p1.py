"""Computer Science Pre-Board 2014-15, Paper 1 (Theory) -- Heritage School."""
from kit import Q, SEC
import computers_2014_15_figs as F
from _computers_a_util import code, sample, pre, tt, table

M = "computers_2014_15_p1"

INTRO = r"""<p><i>(Candidates are allowed additional 15 minutes for only reading the paper.
They must NOT start writing during this time)</i></p>
<p><i>Answer all questions in Part I (compulsory) and seven questions from Part-II, choosing three questions
from Section-A, two from Section-B and two from Section-C. All working, including rough work, should be done
on the same sheet as the rest of the answer. The intended marks for questions or parts of questions are given
in brackets [ ].</i></p>"""

SECB = r"""Answer any two questions. Each program should be written in such a way that it clearly depicts the logic of
the problem. This can be achieved by using mnemonic names and comments in the program. (Flowcharts and
Algorithms are not required.) <b>The Programs must be written in Java.</b>"""
SECC = r"""Answer any two questions. Each program/ Algorithm should be written in such a way that it clearly depicts
the logic of the problem step wise. This can also be achieved by using pseudo codes. (Flowcharts are not
required.) <b>The Programs must be written in Java. The Algorithm must be written in general/standard form,
wherever required.</b>"""

ITEMS = [
    SEC("Part I", "Answer all questions. While answering questions in this Part, indicate briefly your working and reasoning, wherever required."),

    Q("1(a)", 2, r"<p>Verify using the truth table, A+B&prime;C= (A+B&prime;).(A+C). Also, state the law.</p>",
      a=tt(["A", "B", "C"], [
          ("B&prime;C", lambda a, b, c: (1 - b) & c),
          ("A+B&prime;C", lambda a, b, c: a | ((1 - b) & c)),
          ("A+B&prime;", lambda a, b, c: a | (1 - b)),
          ("A+C", lambda a, b, c: a | c),
          ("(A+B&prime;)(A+C)", lambda a, b, c: (a | (1 - b)) & (a | c))], hl={1, 4}) +
      r"""<p>The columns \(A+B'C\) and \((A+B')(A+C)\) agree in all 8 rows, so the identity holds.</p>
<p><b>Law:</b> <span class="box">Distributive law &mdash; OR distributes over AND: \(X + YZ = (X+Y)(X+Z)\)</span>
(here with \(Y = B'\), \(Z = C\)).</p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Distributive laws: \(X(Y+Z)=XY+XZ\) and \(X+YZ=(X+Y)(X+Z)\).</li><li>Verify a law by giving both sides their own column.</li></ul>"),

    Q("1(b)", 2, r"""<p>If \(X \Rightarrow Y\) then write its<br>i. Converse<br>ii. Contra positive</p>""",
      a=r"""<p>i. Converse (swap the two parts): <span class="box">\(Y \Rightarrow X\)</span></p>
<p>ii. Contrapositive (swap and negate both): <span class="box">\(\sim Y \Rightarrow \sim X\)</span>
(i.e. \(Y' \Rightarrow X'\)), which is logically equivalent to \(X \Rightarrow Y\).</p>""",
      topic="Boolean Algebra (propositional logic)",
      recall=r"<ul><li>Converse: \(q\Rightarrow p\). Inverse: \(\sim p\Rightarrow\sim q\). Contrapositive: \(\sim q\Rightarrow\sim p\).</li><li>Only the contrapositive is equivalent to the original.</li></ul>"),

    Q("1(c)", 2, r"<p>Show how NAND gates can be used to construct an OR gate.</p>",
      a=r"""<p>Invert A and B with NAND gates whose inputs are tied, then NAND the results:</p>
<p>\(\overline{A\cdot A} = A'\), \(\overline{B\cdot B}=B'\), and \(\overline{A'\cdot B'} = A'' + B'' = A + B\) (De Morgan).</p>{{fig:0}}""",
      afig=[(F.fig_q1c_or, "OR gate from three NAND gates")],
      topic="Computer Hardware (universal gates)",
      recall=r"<ul><li>NOT from NAND: tie the inputs.</li><li>De Morgan: \((A'B')' = A+B\).</li></ul>"),

    Q("1(d)", 2, r"<p>Given \(F(X,Y,Z)=X.Y'+XZ+Z'\) write the function is canonical sum- of &ndash; product form.</p>",
      a=r"""<p>Multiply each term by \((V+V')\) for every missing variable V:</p>
<p>\[\begin{aligned}
XY' &= XY'(Z+Z') = XY'Z + XY'Z'\\
XZ &= XZ(Y+Y') = XYZ + XY'Z\\
Z' &= Z'(X+X')(Y+Y') = XYZ' + XY'Z' + X'YZ' + X'Y'Z'
\end{aligned}\]</p>
<p>Removing repeated terms (\(P+P=P\)):</p>
<p><span class="box">\(F = X'Y'Z' + X'YZ' + XY'Z' + XY'Z + XYZ' + XYZ = \sum(0,2,4,5,6,7)\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Canonical SOP: every term contains every variable.</li><li>Expand with \(V+V'=1\); drop duplicates (idempotence).</li></ul>"),

    Q("1(e)", 2, r"""<p>Given the Boolean function \(F(X,Y,Z)=\sum(2,3,4,6,7)\). Reduce it using Karnaugh&rsquo;s map.
And also find the dual of its answer.</p>""",
      a=r"""{{fig:0}}
<ul><li>Quad (m2, m3, m6, m7) = \(Y\)</li><li>Pair (m4, m6) = \(XZ'\) (end columns wrap)</li></ul>
<p>\(F = Y + XZ'\). <b>Dual</b>: interchange + and \(\cdot\) (and 0 and 1), keep the literals:</p>
<p><span class="box">\(F = Y + XZ'\); &nbsp; dual \(= Y\cdot(X+Z')\)</span></p>""",
      afig=[(F.fig_q1e_kmap, "3-variable K-map")],
      topic="Boolean Algebra (K-maps)",
      recall=r"<ul><li>3-variable map: X down the side, YZ across in Gray code 00, 01, 11, 10.</li><li>Dual: swap + ↔ · and 0 ↔ 1; literals unchanged.</li></ul>"),

    Q("2(a)", 2, r"<p>State the difference between linear and non-linear data structures.</p>",
      a=table(["Linear data structure", "Non-linear data structure"], [
          ["Elements form a sequence; each element has at most one predecessor and one successor.",
           "Elements form a hierarchy or network; an element may have several successors."],
          ["Can be traversed in a single run from first to last.", "Cannot be traversed in one linear run; needs tree/graph traversals."],
          ["e.g. array, stack, queue, linked list.", "e.g. tree, graph."]]),
      topic="Data Structures",
      recall=r"<ul><li>Linear: one-after-another (array, stack, queue, list).</li><li>Non-linear: branching (binary tree).</li></ul>"),

    Q("2(b)", 2, r"""<p>With respect to file handling in Java, answer the following questions:<br>
i. Name the class that allows reading of binary representations of Java primitives from an input byte stream.<br>
ii. Which abstract class is the super class of all classes used for reading Bytes?</p>""",
      excluded="Data file handling (byte streams, DataInputStream, InputStream) is a Class XI topic in the ISC 2027 syllabus (Class XI Unit 11(b)); the Class XII syllabus (Unit 5(c)) covers only Scanner/Printer input-output."),

    Q("2(c)", 2, r"""<p>A matrix B[10][7] is stored in the memory with each element requiring 2 bytes of storage. If the base
address at B[X][1] is 1012 and the base address at B[7][3] is 1060, determine the value &lsquo;X&rsquo; where the
matrix is stored in column major form.</p>""",
      a=r"""<p>Column-major, number of rows \(M = 10\), \(W = 2\):
\(\text{Address}(B[I][J]) = B_0 + W[(I-L_r) + M(J-L_c)]\). Subtracting the two given addresses removes the
unknown base and lower bounds:</p>
<p>\[1060 - 1012 = 2\,[\,(7 - X) + 10(3 - 1)\,]\]</p>
<p>\[48 = 2\,[\,27 - X\,] \;\Rightarrow\; 27 - X = 24 \;\Rightarrow\; X = 3\]</p>
<p><span class="box">X = 3</span></p>
<p>Check (indices from 0): \(B_0 = 1060 - 2(7+30) = 986\), and \(B[3][1] = 986 + 2(3+10) = 1012\). &#10003;</p>""",
      topic="Arrays (address calculation)",
      recall=r"<ul><li>Column-major: \(B + W[(I-L_r)+M(J-L_c)]\), M = number of rows.</li><li>Two known addresses: subtract to eliminate the base.</li></ul>"),

    Q("2(d)", 2, r"<p>What do you mean by dominant term in Complexity? Support with an example.</p>",
      a=r"""<p>The <b>dominant term</b> is the term in the expression for an algorithm's running time that grows fastest
as the input size n increases; for large n it decides the time, so the complexity is written using that term
alone (constant factors dropped).</p>
<p>Example: a method performs \(T(n) = 3n^2 + 5n + 20\) steps (a nested loop plus a single loop).
For \(n = 1000\): \(3n^2 = 3\,000\,000\) while \(5n + 20 = 5020\). The dominant term is \(3n^2\), so
<span class="box">\(T(n) = O(n^2)\)</span>.</p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>Growth order: \(1 &lt; \log n &lt; n &lt; n\log n &lt; n^2 &lt; 2^n\).</li><li>Big O keeps only the dominant term, without its constant.</li></ul>"),

    Q("2(e)", 2, r"""<p>Convert the following infix notation to its postfix notation:<br>(NOT) a (AND) b (OR) c (AND) d</p>""",
      a=r"""<p>Precedence: NOT (highest, unary) &gt; AND &gt; OR, so the expression is \(((\text{NOT } a)\text{ AND } b)\text{ OR }(c \text{ AND } d)\).</p>
<p><code>[a NOT] AND b OR [c d AND] &rarr; [a NOT b AND] OR [c d AND] &rarr; a NOT b AND c d AND OR</code></p>""" +
      table(["Symbol", "Stack", "Postfix"], [
          ["NOT", "NOT", ""], ["a", "NOT", "a"], ["AND", "AND", "a NOT"], ["b", "AND", "a NOT b"],
          ["OR", "OR", "a NOT b AND"], ["c", "OR", "a NOT b AND c"], ["AND", "OR AND", "a NOT b AND c"],
          ["d", "OR AND", "a NOT b AND c d"], ["end", "", "a NOT b AND c d AND OR"]]) +
      r"""<p><span class="box">a NOT b AND c d AND OR</span> &nbsp;(i.e. \(a \sim b \wedge c\, d \wedge \vee\))</p>""",
      topic="Data Structures (infix, prefix and postfix)",
      recall=r"<ul><li>NOT &gt; AND &gt; OR, like unary minus &gt; * &gt; +.</li><li>A unary operator in postfix follows its single operand.</li></ul>"),

    Q("3(a)", 4, r"""<p>Give the output of the following function: Show the dry run / working.</p>
<pre class="code">int somefun(String s,int last)
{
    if(last &lt; 0)
        return 0;
    if(s.charAt(last) == '0')
        return 2*somefun(s,last-1);
    else
        return 1+2*somefun(s, last-1);
}</pre>
<p>i. What will the function somefun(&ldquo; 10011&rdquo;,4) return?<br>
ii. What will the function somefun(&ldquo;001001101&rdquo;,5,)return?</p>""",
      a=r"""<p>The function reads the characters s[0..last] as a binary number (each step doubles the value of the
prefix and adds the current bit).</p>
<p><b>i.</b> s = "10011", last = 4</p>""" + table(["Call", "s.charAt(last)", "Returns"], [
          ["somefun(s,4)", "'1'", "1 + 2&times;9 = <b>19</b>"],
          ["somefun(s,3)", "'1'", "1 + 2&times;4 = 9"],
          ["somefun(s,2)", "'0'", "2&times;2 = 4"],
          ["somefun(s,1)", "'0'", "2&times;1 = 2"],
          ["somefun(s,0)", "'1'", "1 + 2&times;0 = 1"],
          ["somefun(s,&minus;1)", "&mdash;", "0"]]) +
      r"""<p><span class="box">somefun("10011",4) returns 19</span> (\(10011_2 = 19\))</p>
<p><b>ii.</b> last = 5 uses s[0..5] = "001001": bits 0,0,1,0,0,1 give
\(0\to0\to1\to2\to4\to9\).</p>
<p><span class="box">somefun("001001101",5) returns 9</span> (\(001001_2 = 9\))</p>
<p class="note">The paper prints the call as <code>somefun("001001101",5,)</code>; the stray comma is a misprint.
The first string is taken as "10011" (the space after the opening quote is typographic; with a leading space
last = 4 would index "1001" plus the space and the call would not mean a binary number).</p>
<p>Checked by running the method:</p>""" + code(M, "Q3a_Somefun.java") + sample(M, "Q3a_Somefun.java"),
      topic="Recursion",
      recall=r"<ul><li>Unwind the recursion to the base case, then substitute the returned values back up.</li><li>value = 2 × (value of prefix) + bit: binary to decimal.</li></ul>"),

    Q("3(b)", 3, r"""<p>Give the output of the following function: Show the dry run / working.</p>
<pre class="code">public static String fun_with_recursion(String str)
{
    if(str.length()&lt;2)
    {
        return str;
    }
    return fun_with_recursion(str.substring(1))+str.charAt(0);
}</pre>
<p>What will the function fun_with_recursion(&ldquo; Hello World!&rdquo;) return?</p>""",
      a=r"""<p>Each call removes the first character and appends it <i>after</i> the reversed rest, so the string is
reversed.</p>
<p>f("Hello World!") = f("ello World!") + 'H'<br>
&nbsp;&nbsp;= f("llo World!") + 'e' + 'H'<br>
&nbsp;&nbsp;= &hellip; = f("!") + 'd' + 'l' + 'r' + 'o' + 'W' + ' ' + 'o' + 'l' + 'l' + 'e' + 'H'<br>
&nbsp;&nbsp;= "!" + "dlroW olleH" (base case: length 1 returns itself)</p>
<p><span class="box">!dlroW olleH</span></p>
<p class="note">If the space printed after the opening quote is part of the string (" Hello World!"),
the result is the same followed by a trailing space: "!dlroW olleH ".</p>""" + sample(M, "Q3b_Rec.java",
          "<p>Run with both readings (brackets mark the ends of the string):</p>"),
      topic="Recursion",
      recall=r"<ul><li><code>substring(1)</code>: everything after the first character.</li><li>Recursive call first, then append: the first character ends up last → reversal.</li></ul>"),

    Q("3(c)", 3, r"""<p>Give the output of the following function:</p>
<pre class="code">class Counter
{
    static int c=10;
    Counter()
    {
        c++;
        System.out.println("THE VALUE IS - "+c);
    }
    public static void main(String args[])
    {
        Counter c1=new Counter();
        Counter c2=new Counter();
        Counter c3=new Counter();
    }
}</pre>""",
      a=r"""<p><code>c</code> is <b>static</b>: one copy shared by all objects, starting at 10. Each <code>new Counter()</code> runs the
constructor once, incrementing the same c.</p>""" + table(["Object created", "c after c++", "Printed"], [
          ["c1", "11", "THE VALUE IS - 11"], ["c2", "12", "THE VALUE IS - 12"], ["c3", "13", "THE VALUE IS - 13"]]) +
      r"""<p><b>Output</b></p>""" + pre("THE VALUE IS - 11\nTHE VALUE IS - 12\nTHE VALUE IS - 13") +
      r"""<p class="note">Verified by running the class exactly as printed.</p>""",
      topic="Methods (static variables)",
      recall=r"<ul><li>A static variable belongs to the class: one copy shared by every object.</li><li>A constructor runs once per <code>new</code>.</li></ul>"),

    SEC("Part II &mdash; Section A", "Answer any three questions."),

    Q("4(a)", 5, r"""<p>a) Given the boolean function: \(F(A,B,C,D)=\Sigma(3,4,6,7,11,12,14,15)\)</p>
<p>Use Karnaugh&rsquo;s map to reduce the function F, using the SOP form. Draw a logic gate diagram for the
reduced SOP form. You may use gates more than two inputs. Assume that the variables and their complements
are available as inputs.</p>""",
      a=r"""{{fig:0}}
<ul><li>Quad (m3, m7, m11, m15) = \(CD\) (the whole CD column)</li>
<li>Quad (m4, m6, m12, m14) = \(BD'\) (rows A&prime;B and AB, end columns wrap)</li></ul>
<p><span class="box">\(F = CD + BD'\)</span></p>{{fig:1}}""",
      afig=[(F.fig_q4a_kmap, "K-map for Σ(3,4,6,7,11,12,14,15)"), (F.fig_q4a_circ, "Logic diagram of F = CD + BD′")],
      topic="Boolean Algebra (K-maps)",
      recall=r"<ul><li>Gray-code order 00, 01, 11, 10 on both sides.</li><li>A full column/row of 4 is a quad; corners and edges wrap.</li><li>SOP → AND gates into an OR gate.</li></ul>"),

    Q("4(b)", 5, r"""<p>b) Given the boolean function: \(F(A,B,C,D)=\pi(0,8,10,12,13,14,15)\)</p>
<p>Use Karnaugh&rsquo;s map to reduce the function F, using the POS form. Draw a logic gate diagram for the
reduced POS form. You may use gates more than two inputs. Assume that the variables and their complements
are available as inputs.</p>""",
      a=r"""<p>Mark 0s at the maxterms and group the 0s:</p>{{fig:0}}
<ul><li>Quad (M12, M13, M14, M15) = \((A'+B')\)</li>
<li>Quad (M8, M10, M12, M14) = \((A'+D)\) (rows AB and AB&prime;, end columns wrap)</li>
<li>Pair (M0, M8) = \((B+C+D)\) (top and bottom rows wrap)</li></ul>
<p><span class="box">\(F = (A'+B')(A'+D)(B+C+D)\)</span></p>{{fig:1}}""",
      afig=[(F.fig_q4b_kmap, "POS K-map for π(0,8,10,12,13,14,15)"), (F.fig_q4b_circ, "Logic diagram of the reduced POS")],
      topic="Boolean Algebra (K-maps)",
      recall=r"<ul><li>POS: group the 0s; a variable that is 0 in the group appears uncomplemented.</li><li>POS → OR gates into an AND gate.</li></ul>"),

    Q("5", 10, r"""<p>A man goes to a matrimonial office to search for a bride. The office has information about 10,000 girls.
The man gives two conditions:</p>
<ul><li>The girl must be a teacher or a graduate.</li><li>The girl must be 25 years or less and beautiful.</li></ul>
<p>The inputs are:</p>
<ul><li>G &ndash; The girl is a graduate</li><li>T &ndash; The girl is a teacher</li>
<li>A &ndash; The girl is 25 years or less</li><li>B &ndash; The girl is beautiful</li></ul>
<p>(For all the cases- 1 indicates yes and 0 indicates no)</p>
<p>The output is:</p><ul><li>S &ndash; The girl is selected. [1 indicates she is selected and 0 indicates that she is rejected]</li></ul>
<p>Draw the truth table for inputs and outputs given below and write the SOP expression for X (A, B, C, D).
Reduce X (A, B, C, D) using Karnaugh&rsquo;s map.</p>
<p>Draw the logic gate diagram for the reduced SOP expression for X (A, B, C, D) using AND &amp; OR gates.
You may use the gates with two or more inputs. Assume that the variables and their complements are available as inputs.</p>""",
      a=r"""<p class="note">The question names the output X(A, B, C, D), but its own inputs are G, T, A, B and its output is S;
the function is S(G, T, A, B).</p>
<p>Both conditions must hold: \((G + T)\) <i>and</i> \(A\) <i>and</i> \(B\), so S = 1 only when A = B = 1 and at
least one of G, T is 1.</p>""" +
      tt(["G", "T", "A", "B"], [("S", lambda g, t, a, b: (g | t) & a & b)], hl={0}) +
      r"""<p>\(S(G,T,A,B) = \sum(7, 11, 15)\)</p>
<p><span class="box">\(S = G'TAB + GT'AB + GTAB\)</span></p>{{fig:0}}
<ul><li>Pair (m7, m15) = \(TAB\)</li><li>Pair (m11, m15) = \(GAB\)</li></ul>
<p><span class="box">\(S = TAB + GAB\) &nbsp;(\(= AB(G+T)\))</span></p>{{fig:1}}""",
      afig=[(F.fig_q5_kmap, "K-map for S(G,T,A,B)"), (F.fig_q5_circ, "S = TAB + GAB with AND and OR gates")],
      topic="Boolean Algebra (K-maps)",
      recall=r"<ul><li>'or' between conditions → +, 'and' → product.</li><li>m15 may be used in two groups (overlap is allowed).</li></ul>"),

    Q("6(a)", 3, r"""<p>a) In the following truth table X and Y are the input and B and D are the outputs:</p>""" +
      table(["X", "Y", "D", "B"], [["0", "0", "0", "0"], ["0", "1", "1", "1"], ["1", "0", "1", "0"], ["1", "1", "0", "0"]]) +
      r"""<p>Answer the following questions:<br>i. Write the SOP expression for D.<br>ii. Write the POS expression for B.<br>
iii. Draw the Logic diagram for SOP expression derived for D, using only NAND gates.</p>""",
      a=r"""<p>(This is a half subtractor: D = difference, B = borrow.)</p>
<p><b>i.</b> D = 1 in rows 01 and 10: <span class="box">\(D = X'Y + XY'\)</span> \((= X\oplus Y)\)</p>
<p><b>ii.</b> B = 0 in rows 00, 10, 11: <span class="box">\(B = (X+Y)(X'+Y)(X'+Y')\)</span>
(which reduces to \(B = X'Y\)).</p>
<p><b>iii.</b> \(D = \overline{\overline{X'Y}\cdot\overline{XY'}}\): NAND-NAND, with X&prime; and Y&prime; from NAND gates with tied inputs.</p>{{fig:0}}""",
      afig=[(F.fig_q6_nand, "D = X′Y + XY′ using only NAND gates")],
      topic="Boolean Algebra / Computer Hardware",
      recall=r"<ul><li>SOP: one minterm per 1-row; POS: one maxterm per 0-row (0 → plain, 1 → complemented).</li><li>Half subtractor: D = X⊕Y, B = X′Y.</li><li>SOP to NAND-NAND: replace AND and OR by NAND.</li></ul>"),

    Q("6(b)", 3, r"<p>b) Using the truth table verify: (~P =&gt; Q) ^ P = (P ^ ~Q) v (P ^ Q)</p>",
      a=tt(["P", "Q"], [
          ("~P", lambda p, q: 1 - p),
          ("~P &rArr; Q", lambda p, q: p | q),
          ("(~P&rArr;Q) &and; P", lambda p, q: (p | q) & p),
          ("P &and; ~Q", lambda p, q: p & (1 - q)),
          ("P &and; Q", lambda p, q: p & q),
          ("(P&and;~Q) &or; (P&and;Q)", lambda p, q: (p & (1 - q)) | (p & q))], hl={2, 5}) +
      r"""<p>(\(\sim P\Rightarrow Q\) is false only when \(\sim P\) is true and Q false, i.e. P = 0, Q = 0.)</p>
<p>The two highlighted columns are identical (both equal P), so
<span class="box">\((\sim P \Rightarrow Q)\wedge P \;\equiv\; (P\wedge\sim Q)\vee(P\wedge Q)\)</span> is verified.</p>""",
      topic="Boolean Algebra (propositional logic)",
      recall=r"<ul><li>\(p\Rightarrow q\) is false only for p true, q false; \(p\Rightarrow q \equiv \sim p\vee q\).</li><li>Equivalent wffs have identical truth-table columns.</li></ul>"),

    Q("6(c)", 4, r"<p>c) Draw the logic gate diagram and give the truth table for a full adder circuit.</p>",
      a=r"""<p>A full adder adds three bits A, B and C (carry in):
\(\text{SUM} = A\oplus B\oplus C\), \(\text{CARRY} = AB + C(A\oplus B)\) \((= AB+BC+CA)\).</p>""" +
      tt(["A", "B", "C"], [("SUM", lambda a, b, c: a ^ b ^ c), ("CARRY", lambda a, b, c: (a & b) | (b & c) | (c & a))]) +
      r"""{{fig:0}}""",
      afig=[(F.fig_q6c_fa, "Full adder: 2 XOR, 2 AND, 1 OR")],
      topic="Computer Hardware (adders)",
      recall=r"<ul><li>SUM is 1 for an odd number of 1s.</li><li>CARRY is 1 when at least two inputs are 1 (majority).</li></ul>"),

    Q("7(a)", 4, r"<p>a) Draw the truth table and a logic gate diagram for a 4:1 multiplexer and briefly explain its working.</p>",
      a=r"""<p>A 4 : 1 multiplexer has four data inputs \(I_0\)&ndash;\(I_3\), two select lines \(S_1S_0\) and one output Y.
The select lines choose which data input is passed to the output.</p>""" +
      table(["S<sub>1</sub>", "S<sub>0</sub>", "Y"], [["0", "0", "I<sub>0</sub>"], ["0", "1", "I<sub>1</sub>"],
                                                      ["1", "0", "I<sub>2</sub>"], ["1", "1", "I<sub>3</sub>"]]) +
      r"""<p>\(Y = S_1'S_0'I_0 + S_1'S_0I_1 + S_1S_0'I_2 + S_1S_0I_3\)</p>{{fig:0}}
<p><b>Working:</b> for each select combination exactly one of the four AND gates has both its select inputs
at 1; that gate passes its data input, the other three output 0, and the OR gate delivers the selected input
to Y. E.g. \(S_1S_0 = 10\) enables only the third gate, so \(Y = I_2\).</p>""",
      afig=[(F.fig_q7a_mux, "4 : 1 multiplexer at gate level")],
      topic="Computer Hardware (multiplexers)",
      recall=r"<ul><li>\(2^n\) inputs need n select lines.</li><li>Each AND gate decodes one select combination.</li></ul>"),

    Q("7(b)", 2, r"""<p>b) Convert the following SOP expression to an equivalent POS expression.</p>
<p style="text-align:center">\(ABC + AB'C' + AB'C + ABC' + A'B'C\)</p>""",
      a=r"""<p>Minterms: \(ABC = m_7\), \(AB'C' = m_4\), \(AB'C = m_5\), \(ABC' = m_6\), \(A'B'C = m_1\).
So \(F = \sum(1,4,5,6,7)\); the missing rows 0, 2, 3 are the maxterms:</p>
<p><span class="box">\(F = \prod(0,2,3) = (A+B+C)(A+B'+C)(A+B'+C')\)</span></p>
<p>(It simplifies to \(F = A + B'C\).)</p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>SOP ↔ POS: the maxterm indices are the rows not among the minterms.</li><li>Maxterm: 0 → variable, 1 → complement.</li></ul>"),

    Q("7(c)", 4, r"""<p>c) From the Logic circuit diagram given below, name the outputs (1), (2) and (3). Finally derive the Boolean
expression and simplify it to show that it represents a logic gate. Name and draw the logic gate.</p>{{fig:0}}""",
      a=r"""<p>(1) = \(X\cdot Y\) &nbsp; (2) = \((XY)\cdot Z = XYZ\) &nbsp; (3) = \((XYZ)'\)</p>
<p>The last AND gate takes (3) and (1):</p>
<p>\[\begin{aligned}
F &= XY\cdot(XYZ)' = XY\,(X'+Y'+Z') &&\text{(De Morgan)}\\
  &= XYX' + XYY' + XYZ' = 0 + 0 + XYZ'
\end{aligned}\]</p>
<p><span class="box">\(F = X\cdot Y\cdot Z'\)</span> &mdash; an <b>AND gate</b> (three inputs) with the Z input inverted:</p>{{fig:0}}
<p class="note">As drawn, the circuit reduces to \(XYZ'\), a three-input AND with an inverted input, rather than to one of the
basic two-input gates. If the last gate were meant to take only (3) and Z the answer would differ; the circuit is solved as printed.</p>""",
      qfig=[(F.fig_q7c_given, "Circuit as printed")],
      afig=[(F.fig_q7c_answer, "F = XYZ′")],
      topic="Computer Hardware (logic gates)",
      recall=r"<ul><li>Label each gate's output in terms of the inputs, left to right.</li><li>\(XX' = 0\); De Morgan \((XYZ)' = X'+Y'+Z'\).</li></ul>"),

    SEC("Part II &mdash; Section B", SECB),

    Q("8", 10, r"""<p>A class called <b>DigiNumber</b> has been defined to find the frequency of each digit present in a number and the
sum of the digits. Some of the members of the class <b>DigiNumber</b> are given below:</p>
<p><b>Class name</b> : DigiNumber<br><b>Data members/instance variables</b> :<br>num : long integer for storing the number<br>
<b>Member functions :</b><br>
DigiNumber ( ) : constructor to assign <b>0</b> to <b>num</b><br>
DigiNumber (long n) : parameterised constructor to assign <b>n</b> to <b>num</b><br>
void digitfrequency( ) : find the frequency of each digit present in <b>num</b> and to display it<br>
long sumDigits(long N) : to return the sum of the digits of the number stored in <b>num</b> using <b>Recursive Technique</b><br>
void printsum( ) : print sum of digits of num by invoking sumDigits(&hellip;)</p>
<p>Specify the class <b>DigiNumber</b>, giving details of the <b>two Constructor</b> and functions <b>void digitfrequency( ),
long sumDigits(long) and void printsum( )</b>. Also write the <b>main( )</b> function to create an object and call the member function accordingly.</p>""",
      a=r"""<p><b>Logic:</b> a frequency array <code>freq[10]</code> is filled by peeling digits with % 10 and / 10;
<code>sumDigits(N) = N%10 + sumDigits(N/10)</code> with base case N = 0.</p>""" + code(M, "Q8_DigiNumber.java") +
      sample(M, "Q8_DigiNumber.java"),
      topic="Recursion",
      recall=r"<ul><li>Last digit <code>n % 10</code>, remove it <code>n / 10</code>.</li><li>Recursive sum: \(s(N) = N\%10 + s(N/10)\), \(s(0)=0\).</li><li>Overloaded constructors differ in their parameter lists.</li></ul>"),

    Q("9", 10, r"""<p>Following is the description of class Collection:</p>
<p><b>Class name</b> : Collection<br><b>Data members/ instance variables:</b><br>arr[] : an array of 100 integers.<br>len : length of the array<br>
<b>Member functions/methods:</b><br>Collection( ) : default constructor<br>
Collection(int) : parameterised constructor to define the length of the array.<br>
void readArray( ) : to accept array elements.<br>
Collection common(Collection) : this function will receive an object of Collection. Then, it will find the common elements in its
own array and in the array of the object received. Finally it will return the common elements as an array of the Collection object.<br>
void displayArray( ) : to display the array elements .</p>
<p>Specify the class Collection giving the details of the constructors and the given methods. You need not write the main() method.</p>""",
      a=r"""<p><b>Logic:</b> for each element of this array, search the other object's array; if found and not already in the
result, append it to a new Collection whose <code>len</code> counts the elements added. The result object is returned.</p>""" +
      code(M, "Q9_Collection.java") +
      sample(M, "Q9_Collection.java", "<p>Test: x has 6 elements, y has 5; <code>x.common(y).displayArray()</code>:</p>"),
      topic="Objects (passing and returning objects)",
      recall=r"<ul><li>An object passed as an argument is accessed through its reference: <code>ob.arr[j]</code>.</li><li>A method may create and return a new object of its own class.</li></ul>"),

    Q("10", 10, r"""<p>Write a java program to input a paragraph from the user and then follow the class definition as given below.</p>
<p><b>Class name</b> : Maxword_paragraph<br><b>Data members/ instance variables:</b><br>
sent : stores the paragraph. The paragraph should consist of 5-sentences only, and Should either end with a full stop (.) or an exclamation mark ( ! ).<br>
rem [5][n] : to store the each of the sentences in the paragraph in each of the rows. Extract each word and place it in each of the cells for a
particular row, for each of the sentence. When n represents the number of words of the longest sentence.<br>
<b>Member functions/methods:</b><br>void readparagraph( ) : to accept the paragraph with the given constraints in <b>sent</b>.<br>
void para_to_array( ) : extract each word of a sentence and store it in rem[][]. And each row of rem[][] represents a sentence. Fill the blank cells of rem[][]with &ldquo;Q&rdquo;. Display the array.<br>
void word_max() : to find and print the word with the maximum length and print its position as stored in the rem[][].</p>
<p>Specify the class Maxword_paragraph giving details of all the methods and the constructor. Create an object in main () and call the above methods.</p>""",
      a=r"""<p><b>Logic:</b> validate that the paragraph has exactly five terminators ('.' or '!') and ends with one;
split it into sentences with a StringTokenizer on ".!"; n = the largest word count; fill each row of
<code>rem</code> with that sentence's words and pad with "Q"; then scan the array for the longest word
(the first one found wins a tie).</p>""" + code(M, "Q10_Maxword.java") + sample(M, "Q10_Maxword.java"),
      topic="Strings and arrays",
      recall=r"<ul><li><code>StringTokenizer(s, delims)</code> and <code>countTokens()</code>.</li><li>A 2-D array can be created after its size is known: <code>new String[5][n]</code>.</li><li>Track the row and column of the current maximum.</li></ul>"),

    SEC("Part II &mdash; Section C", SECC),

    Q("11", 10, r"""<p>A class salesman defines the personal data of a salesman, while another class Sales defines the bill number, name of the item,
and number of items sold and the price of the item. The details of the classes are as follows:</p>
<p><b>Class name</b> : Salesman<br><b>Data members/ instance variables</b> :<br>name : String variable to store the name of the salesman<br>
address : String variable to store the address<br><b>Member functions/methods</b> :<br>
Salesman(String n, String ad ) : parameterised constructor to assign &lsquo;n&rsquo; and &lsquo;a&rsquo; to name and address respectively.<br>
void show( ) : to print the values of name and address using suitable headings</p>
<p><b>Class name</b> : Sales<br><b>Data members/ instance variables:</b><br>billno, qty : Integer to store bill number and quantity<br>
price, psales : Double type to store price and previous sales amount<br>pname : String variable to store name of product<br>
<b>Member functions/methods:</b><br>
Sales( &hellip;.. ) : parameterised constructor to call the constructor of the base class and to assign &lsquo;b&rsquo; to billno,&lsquo;q&rsquo; to qty,&lsquo;p&rsquo; to price, &lsquo;s&rsquo; to psales and &lsquo;pr&rsquo; to pname of the derived class.<br>
double calculate( ) : to calculate and return the total sales using the formula: price*qty + psales<br>
void show( ) : to display values of pname, billno, qty, psales and the total sales made by invoking suitable functions and also call the display( ) method of the super class.</p>
<p>Specify the class Salesman giving the details of the constructor and the functions. Using the concept of Inheritance specify the class
Sales giving the details of the functions. You do not need to write the main( ) method.</p>""",
      a=r"""<p class="note">The superclass method is named <code>show()</code> in its description, so &ldquo;the display( ) method of the
super class&rdquo; is <code>super.show()</code>.</p>
<p>Sales <code>extends</code> Salesman; its constructor passes n and ad to <code>super(n, ad)</code> as its first statement,
and its <code>show()</code> overrides the superclass one and calls it through <code>super</code>.</p>""" + code(M, "Q11_Sales.java") +
      sample(M, "Q11_Sales.java",
             '<p>Test: <code>new Sales("R. Sen", "Kolkata", 101, 5, 250.0, 1200.0, "Pen drive").show();</code> (total = 250&times;5 + 1200 = 2450)</p>'),
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li><code>super(args)</code> must be the first statement of the subclass constructor.</li><li>An overriding method calls the parent version with <code>super.show()</code>.</li></ul>"),

    Q("12", 10, r"""<p>A special type of queue enables the user to add integers from either ends, i.e. from front and rear, but allows removal only from the front end.
Define the class Squeue with the following details:</p>
<p><b>Class name</b> : Squeue<br><b>Data members/ instance variables:</b><br>que[] : array to hold up to 100 integers<br>
lim : stores the limit of the circular queue.<br>front : integer to point to the front end index number<br>rear : integer to point to the rear end index number<br>
<b>Member functions/methods:</b><br>Squeue (int l) : constructor to initialize the data members lim=l, front=rear=0<br>
void insert(int val ) : to add integers to the special queue from both the ends &ndash;</p>
<ul><li>Firstly ask the user to choose , at which end the user wants to enter the data</li>
<li>If the user chooses front and queue is not full then shift the elements to the right by one place and then enter the element at the front.
If front &ndash; most position is empty then insert the data there and point it as front.</li>
<li>Now, if the user wants to enter the data at the rear position then follow the same algorithm as a normal queue.</li>
<li>If the array is filled up and you cannot enter any more data then print &ldquo;OVERFLOW&rdquo;.</li></ul>
<p>int delete( ) : returns element from front, if possible, otherwise returns the value -9999.</p>
<p>Specify the class <b>Squeue</b> giving the details of the constructor and the functions. Using the concept of Inheritance specify the class
Sales giving the details of the functions. You do not need to write the main( ) method.</p>""",
      a=r"""<p class="note">The last sentence (&ldquo;Using the concept of Inheritance specify the class Sales&rdquo;) is carried over from
Question 11 by mistake; only class Squeue is asked for.</p>
<p><b>Representation:</b> the elements are <code>que[front] &hellip; que[rear-1]</code>; front = rear means empty.
Insertion at the rear needs <code>rear &lt; lim</code>. Insertion at the front uses the free cell before front if there is one;
otherwise, if the array is not full, every element is shifted one place right and the new value goes in at front.</p>""" +
      code(M, "Q12_Squeue.java") +
      sample(M, "Q12_Squeue.java",
             "<p>Test with lim = 4: insert 10 (R), 20 (R), 5 (F, shifts), delete, 1 (F, free slot), 30 (R), 40 (R) and 50 (F) overflow, then five deletions:</p>"),
      topic="Data Structures (queue, dequeue)",
      recall=r"<ul><li>Queue: insert at rear, delete at front (FIFO).</li><li>Input-restricted variant here: insert at both ends, delete at one.</li><li>Shift right from the rear end backwards so nothing is overwritten.</li></ul>"),

    Q("13(a)", 4, r"""<p>a) A linked list is formed from the objects of the class,</p>
<pre class="code">class Node
{
    int item;
    Node ptr;
}</pre>
<p>Write an <b>Algorithm</b> or a <b>Method</b> to find the sum of the values of all the elements in the linked list. The method declaration is given below:<br>
<b>int sum(Node ptr_start)</b></p>""",
      a=r"""{{fig:0}}
<p><b>Algorithm</b></p>
<ol><li>Start. Set S = 0 and TEMP = ptr_start.</li>
<li>Repeat steps 3&ndash;4 while TEMP &ne; null.</li>
<li>S = S + TEMP.item.</li>
<li>TEMP = TEMP.ptr (move to the next node).</li>
<li>Return S. Stop.</li></ol>
<p><b>Method</b></p>""" + code(M, "Q13a_LinkedSum.java") +
      r"""<p>For the list shown, sum = 12 + 7 + 25 + 4 = 48 (run output: <code>sum = 48</code>; an empty list gives 0).</p>""",
      afig=[(F.fig_q13a_list, "Traversal from ptr_start to null")],
      topic="Data Structures (linked list)",
      recall=r"<ul><li>Traverse with a temporary reference; never move the start reference.</li><li>Stop when the reference becomes null.</li></ul>"),

    Q("13(b)", 4, r"""<p>b) Answer the questions below for the given binary tree:</p>{{fig:0}}
<p>i. List the internal nodes of the binary tree<br>ii. List the leaf nodes of the binary tree<br>
iii. Draw the right subtree of node C<br>iv. Write preorder traversal of the Binary tree</p>""",
      a=r"""<p>From the figure: A(B, C); B(D, E); E has left child H; H has right child K; C(F, G); G(I, J); J has left child L.</p>
<p>i. Internal nodes (at least one child): <span class="box">A, B, C, E, G, H, J</span></p>
<p>ii. Leaf nodes (no children): <span class="box">D, K, F, I, L</span></p>
<p>iii. Right subtree of C (rooted at G):</p>{{fig:0}}
<p>iv. Preorder (Root, Left, Right): <span class="box">A B D E H K C F G I J L</span></p>""",
      qfig=[(F.fig_q13b_tree, "")],
      afig=[(F.fig_q13b_right, "Right subtree of C")],
      topic="Data Structures (binary trees)",
      recall=r"<ul><li>Leaf: no children; internal node: at least one child.</li><li>Right subtree of a node: its right child and all that child's descendants.</li><li>Preorder: root, left subtree, right subtree.</li></ul>"),

    Q("13(c)", 2, r"""<p>c) What is the worst case complexity of the following code segment:</p>
<pre class="code">a = a + 1
for (i = 1 ; i &lt;= N ; i++)  {
        m = m + 2;
}
for (i = 1 ; i&lt;= M ; i++)  {
    for (i = 1 ; i &lt;= N ; i++)
    {
        k = k +1;
    }
}</pre>""",
      a=r"""<p>Statement counts: \(a=a+1\) once \(\to O(1)\); first loop N times \(\to O(N)\); nested loops
\(M\times N\) times \(\to O(MN)\).</p>
<p>Total \(= O(1) + O(N) + O(MN)\); the dominant term is \(MN\):</p>
<p><span class="box">\(O(M\times N)\)</span> (\(= O(N^2)\) if M = N).</p>
<p class="note">The inner loop reuses <code>i</code> as printed; this is evidently a slip for a separate counter j, and the
intended nested-loop analysis is given. (Taken literally, the inner loop leaves i = N+1 and the outer i++ makes it N+2: if
M &le; N+1 the outer loop runs only once, giving O(N) overall; if M &ge; N+2 the inner loop resets i to 1 every time and the
segment never terminates.)</p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>Sequential blocks: add complexities, keep the largest.</li><li>Nested loops: multiply the iteration counts.</li></ul>"),
]

PAPER = dict(
    subject="computers", year="2014-15", slug="2014-15-paper-1", paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2014-15/Computer Science.pdf", marks=100, time="3 hours",
    intro=INTRO, items=ITEMS)
