"""Computer Science pre-board 2015-16, Paper 1 (Theory).  Transcribed from the page images
(the PDF is a scan; its text layer is unusable).  Checks: src/checks/computers_2015_16_p1_check.py."""
from kit import Q, SEC
import computers_2015_16_figs as F
from cs_b_kit import jcode, jout, tbl

M = "computers_2015_16_p1"


def tt(header, rows):
    return tbl(header, [[str(c) for c in r] for r in rows])


ITEMS = [
    SEC("Part I", "(Compulsory) Answer all questions."),

    Q("1", 1, r"<p>State Absorption law and prove it using Truth Table.</p>",
      a=r"""<p><b>Absorption law:</b> \(A + A\cdot B = A\) and its dual \(A\cdot(A + B) = A\).</p>
<p>Proof of \(A + AB = A\) (the dual is proved the same way):</p>""" + tt(
        ["A", "B", "A·B", "A + A·B", "A + B", "A·(A + B)"],
        [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) +
      r"""<p>The column \(A + A\cdot B\) (and the column \(A\cdot(A+B)\)) is identical to column \(A\) in every row,
hence <span class="box">\(A + AB = A,\quad A(A+B) = A\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Absorption: \(A + AB = A\); dual \(A(A+B) = A\).</li><li>Two expressions are equal when their truth-table columns agree in every row.</li></ul>"),

    Q("2", 1, r"<p>Show the given statement is a tautology \([(P \Rightarrow Q) \uparrow P] \Rightarrow Q\)</p>",
      a=r"""<p class="note">[Unclear in the original: the connective inside the bracket is printed as ↑. Read as NAND the
statement is <i>not</i> a tautology (it is false for P = 0, Q = 0). The intended statement is clearly
\([(P\Rightarrow Q)\wedge P]\Rightarrow Q\) — the rule of <i>modus ponens</i> — and that is proved below.]</p>""" + tt(
        ["P", "Q", "P ⇒ Q", "(P ⇒ Q) ∧ P", "[(P ⇒ Q) ∧ P] ⇒ Q"],
        [[0, 0, 1, 0, 1], [0, 1, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) +
      r"""<p>The last column is 1 (true) for every combination of truth values, so the statement is
<span class="box">a tautology</span></p>""",
      topic="Boolean Algebra (propositional logic)",
      recall=r"<ul><li>\(P \Rightarrow Q\) is false only when P = 1 and Q = 0.</li><li>Tautology: true in every row of the truth table (valid formula).</li><li>Modus ponens: from \(P\Rightarrow Q\) and \(P\), infer \(Q\).</li></ul>"),

    Q("3", 1, r"<p>Simplify algebraically \(C\overline{D} + A + A + \overline{C}\cdot\overline{D} + A\cdot B\)</p>",
      a=r"""<p>\(= A + A + AB + C\overline{D} + \overline{C}\,\overline{D}\)</p>
<p>\(= A + AB + \overline{D}(C + \overline{C})\) &nbsp; (idempotence \(A + A = A\); factorise \(\overline{D}\))</p>
<p>\(= A + \overline{D}\cdot 1\) &nbsp; (absorption \(A + AB = A\); \(C + \overline{C} = 1\))</p>
<p><span class="box">\(= A + \overline{D}\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Idempotence \(A + A = A\); complement \(C + C' = 1\).</li><li>Absorption \(A + AB = A\).</li></ul>"),

    Q("4", 1, r"<p>Find the complement of \([\overline{(AB)}A][\overline{(AB)}B]\) and reduce to minimum literals.</p>",
      a=r"""<p>By De Morgan, the complement of a product is the sum of the complements:</p>
<p>\(\{[\overline{(AB)}A][\overline{(AB)}B]\}' = [\overline{(AB)}A]' + [\overline{(AB)}B]'\)</p>
<p>\(= (AB + A') + (AB + B')\) &nbsp; (De Morgan on each bracket, involution \((AB)'' = AB\))</p>
<p>\(= (A' + B) + (A + B')\) &nbsp; (\(A' + AB = A' + B\), \(B' + AB = B' + A\))</p>
<p>\(= (A + A') + (B + B') = 1\)</p>
<p><span class="box">Complement = 1</span> &nbsp; (the given expression itself is \(AB'\cdot A'B = 0\)).</p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>De Morgan: \((XY)' = X' + Y'\), \((X + Y)' = X'Y'\).</li><li>\(A' + AB = A' + B\) (redundant-literal rule).</li></ul>"),

    Q("5", 1, r"<p>Express in POS form: \(AB + \overline{C}\) &nbsp; Give the final answer in Cardinal form.</p>",
      a=r"""<p>F(A, B, C) is 1 when \(AB = 1\) (rows 110, 111) or \(C' = 1\) (rows 000, 010, 100, 110):</p>
<p>\(F = \Sigma(0, 2, 4, 6, 7)\), so F = 0 in rows 1 (001), 3 (011), 5 (101).</p>
<p>Canonical POS: \(F = (A + B + C')(A + B' + C')(A' + B + C')\)</p>
<p>Cardinal form: <span class="box">\(F(A,B,C) = \pi(1, 3, 5)\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Maxterm \(M_i\): the sum term that is 0 only in row i (a 0 bit gives the plain variable, a 1 bit its complement).</li><li>POS cardinal form lists the rows where F = 0.</li></ul>"),

    Q("6", 2, r"<p>Define Interface. How is it different from a Class?</p>",
      a=r"""<p><b>Interface:</b> an interface is a reference type in Java that declares a set of abstract methods
(and constants, i.e. <code>public static final</code> fields) which a class agrees to provide by
<code>implements</code>-ing it. It specifies <i>what</i> must be done, not <i>how</i>.</p>
<div class="tbl"><table><tr><th>Interface</th><th>Class</th></tr>
<tr><td>Methods are abstract (no body); fields are constants only.</td><td>Methods have bodies; can have instance variables.</td></tr>
<tr><td>Cannot be instantiated; has no constructor.</td><td>Objects can be created (unless abstract); has constructors.</td></tr>
<tr><td>A class can implement several interfaces (multiple inheritance of type).</td><td>A class can extend only one class.</td></tr>
<tr><td>Declared with <code>interface</code>, used with <code>implements</code>.</td><td>Declared with <code>class</code>, inherited with <code>extends</code>.</td></tr></table></div>""",
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li>Interface = contract: abstract methods + constants.</li><li>A class may implement many interfaces but extend only one class.</li></ul>"),

    Q("7", 2, r"<p>If A = 1, B = 0, C = 1 find X if \(X = \overline{A}BC + A\overline{B}C + \overline{A}B\overline{C}\)</p>",
      a=r"""<p>With A = 1, B = 0, C = 1: \(\overline{A} = 0,\ \overline{B} = 1,\ \overline{C} = 0\).</p>
<p>\(X = 0\cdot0\cdot1 + 1\cdot1\cdot1 + 0\cdot0\cdot0 = 0 + 1 + 0\)</p>
<p><span class="box">\(X = 1\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>Substitute, complement, then AND within each term and OR the terms.</li><li>A sum of products is 1 if any one term is 1.</li></ul>"),

    Q("8", 2, r"<p>Explain the use of 'super' and 'super( ) function'.</p>",
      a=r"""<p><b><code>super</code> (keyword as a reference):</b> inside a subclass it refers to the members of the
immediate superclass. It is used to reach a superclass variable or method that has been hidden or overridden
in the subclass, e.g. <code>super.display();</code> or <code>super.x</code>.</p>
<p><b><code>super( )</code> (constructor call):</b> calls the constructor of the immediate superclass from the
subclass constructor, passing it the arguments it needs, e.g. <code>super(name, basic);</code>. It must be the
<b>first statement</b> of the subclass constructor; if it is omitted, Java inserts a call to the superclass's
no-argument constructor.</p>""",
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li><code>super.member</code> reaches the parent's version of an overridden/hidden member.</li><li><code>super(args)</code> must be the first line of a subclass constructor.</li></ul>"),

    Q("9", 2, r"<p>Convert the following infix notation to postfix form: A*( B / C ) / E + F</p>",
      a=tt(["Symbol", "Stack", "Postfix"],
           [["A", "", "A"], ["*", "*", "A"], ["(", "*(", "A"], ["B", "*(", "AB"], ["/", "*(/", "AB"],
            ["C", "*(/", "ABC"], [")", "*", "ABC/"], ["/", "/", "ABC/*"], ["E", "/", "ABC/*E"],
            ["+", "+", "ABC/*E/"], ["F", "+", "ABC/*E/F"], ["end", "", "ABC/*E/F+"]]) +
      r"""<p>(* and / have equal precedence and associate left to right, so * is popped before / is pushed.)</p>
<p>Postfix: <span class="box">A B C / * E / F +</span></p>""",
      topic="Data Structures (infix to postfix)",
      recall=r"<ul><li>Operands go straight to output; an operator pops every stacked operator of higher or equal precedence first.</li><li>')' pops back to the matching '('.</li></ul>"),

    Q("10", 2, r"""<p>An array AR[15,20], stores elements in Row Major Wise, with the address AR[0][0] as 4000. If each
element requires 8 bytes of storage, find the base address.</p>""",
      a=r"""<p>Row major: \(\text{Address}(AR[i][j]) = B + W\,[\,(i - L_r)\times N_c + (j - L_c)\,]\), with
\(N_c = 20\) columns, \(W = 8\) bytes, lower bounds \(L_r = L_c = 0\).</p>
<p>The <b>base address</b> B is the address of the first element of the array, AR[0][0]. Putting i = j = 0:</p>
<p>\(4000 = B + 8[(0)(20) + 0] = B\) &nbsp;⇒&nbsp; <span class="box">Base address B = 4000</span></p>
<p class="note">[The question as printed gives the answer in its data — the address of AR[0][0] <i>is</i> the
base address. For practice with the same data: the last element AR[14][19] is at
\(4000 + 8(14\times20 + 19) = 4000 + 8\times299 = 6392\).]</p>""",
      topic="Arrays (address calculation)",
      recall=r"<ul><li>Row major: \(B + W[(i-L_r)N_c + (j-L_c)]\); column major: \(B + W[(i-L_r) + (j-L_c)N_r]\).</li><li>Base address = address of the first element.</li></ul>"),

    Q("11", 5, r"""<p>The following function ppp( ) is a function of some class. What will be the output of the function ppp( ) when
the value of begstr is "" and endstr is "ABCd".</p>
<pre class="code">public static void ppp(String begstr,String endstr)
{
    if(endstr.length()&lt;=2)
    {
        System.out.println(begstr+endstr);
    }
    else
    {
        for(int i=0;i&lt;endstr.length();i++)
        {
            String newendstr=endstr.substring(i+1)+endstr.substring(0,i);
            String newbegstr=endstr.charAt(i)+begstr;
            permute(newbegstr,newendstr);
        }
    }
}</pre>""",
      a=r"""<p class="note">[The recursive call is printed as <code>permute(…)</code>; it is evidently ppp( ) calling itself, and is
traced that way.]</p>
<p><b>Working.</b> While endstr has more than 2 characters, each character endstr[i] in turn is put in
<i>front</i> of begstr and the rest of endstr is <i>rotated</i> (the part after i, then the part before i).
With "ABCd" (4 chars) the first level makes 4 calls; each gets a 3-character endstr and makes 3 calls, which print.</p>""" +
      tt(["Level-1 call (i)", "begstr, endstr", "Level-2 calls → printed"],
         [["i = 0 ('A')", '"A", "BCd"', "BACd, CAdB, dABC"],
          ["i = 1 ('B')", '"B", "CdA"', "CBdA, dBAC, ABCd"],
          ["i = 2 ('C')", '"C", "dAB"', "dCAB, ACBd, BCdA"],
          ["i = 3 ('d')", '"d", "ABC"', "AdBC, BdCA, CdAB"]]) +
      r"""<p>e.g. for "A","BCd": i = 0 gives begstr "BA", endstr "Cd" → prints BACd; i = 1 gives "CA", "dB" → CAdB;
i = 2 gives "dA", "BC" → dABC.</p><p><b>Output</b> (confirmed by running it):</p>""" +
      jout(M, "ppp").split("<p><b>Output</b></p>")[1],
      topic="Recursion",
      recall=r"<ul><li><code>s.substring(k)</code> runs from index k to the end; <code>substring(0, i)</code> stops before i.</li><li><code>char + String</code> concatenates: the char goes in front.</li><li>Trace recursion level by level; output appears only at the base case.</li></ul>"),

    SEC("Part II — Section A", "Answer any two questions."),

    Q("12(a)", 5, r"""<p>Given the Boolean function F(A,B,C,D) = Σ(0,1,2,4,5,6,7,8,9,12,13,14).</p>
<p>Use Karnaugh's map to reduce the function F, using the SOP form. Draw a logic gate diagram for the reduced SOP form.
You may use gates with more than two inputs. Assume that the variables and their complements are available as inputs.</p>""",
      a=r"""<p>K-map (rows AB, columns CD in Gray-code order 00, 01, 11, 10; cell number in the corner):</p>{{fig:0}}
<ul><li>Octet (m0, m1, m4, m5, m8, m9, m12, m13) — columns C′D′ and C′D: \(C'\)</li>
<li>Quad (m4, m5, m6, m7) — row A′B: \(A'B\)</li>
<li>Quad (m0, m2, m4, m6) — rows A′B′, A′B with the two end columns (wrap round): \(A'D'\)</li>
<li>Quad (m4, m6, m12, m14) — rows A′B, AB with the two end columns: \(BD'\)</li></ul>
<p>Hence <span class="box">\(F(A,B,C,D) = C' + A'B + A'D' + BD'\)</span></p>
<p>Logic gate diagram (AND–OR):</p>{{fig:1}}""",
      afig=[F.fig_q12a_kmap, F.fig_q12a_circuit],
      topic="Boolean Algebra (Karnaugh maps)",
      recall=r"<ul><li>Gray order 00, 01, 11, 10 on both edges; the map wraps left–right and top–bottom.</li><li>Groups of 8/4/2/1, as large as possible, fewest groups covering every 1.</li><li>An octet drops 3 variables, a quad 2, a pair 1.</li></ul>"),

    Q("12(b)", 5, r"""<p>Given X(A,B,C,D) = π(0,1,2,5,8,9,10).</p>
<p>Use Karnaugh's map to reduce the function F, using the given POS form. Draw a logic gate diagram for the reduced POS
form. You may use gates with more than two inputs. Assume that the variables and their complements are available as
inputs.</p>""",
      a=r"""<p>K-map for the maxterms (rows A+B, columns C+D; a 0 in each listed cell):</p>{{fig:0}}
<ul><li>Quad (M0, M1, M8, M9) — top and bottom rows, columns C+D and C+D′: \((B + C)\)</li>
<li>Quad (M0, M2, M8, M10) — the four corners: \((B + D)\)</li>
<li>Pair (M1, M5) — column C+D′, rows A+B and A+B′: \((A + C + D')\)</li></ul>
<p>Hence <span class="box">\(X(A,B,C,D) = (B + C)(B + D)(A + C + D')\)</span></p>
<p>Logic gate diagram (OR–AND):</p>{{fig:1}}""",
      afig=[F.fig_q12b_kmap, F.fig_q12b_circuit],
      topic="Boolean Algebra (Karnaugh maps)",
      recall=r"<ul><li>For POS, group the 0s; a variable that is 0 in the group appears plain, 1 appears complemented.</li><li>The four corner cells form a quad.</li></ul>"),

    Q("13(a)", 3, r"<p>Briefly explain the working of 4:1 multiplexer and also draw a 4:1 multiplexer.</p>",
      a=r"""<p>A <b>multiplexer</b> (data selector) has many data inputs, one output and select lines; the binary number
on the select lines chooses which input is passed to the output. A 4:1 MUX has data inputs I0–I3, select lines S1 S0
and output Y:</p>{{fig:0}}
<p>\(Y = S_1'S_0'I_0 + S_1'S_0I_1 + S_1S_0'I_2 + S_1S_0I_3\). Each AND gate is enabled by one select
combination (S1′S0′, S1′S0, S1S0′, S1S0); only that gate passes its input, and the OR gate delivers it to Y.</p>{{fig:1}}""",
      afig=[F.fig_q13a_block, F.fig_q13a_mux4],
      topic="Computer Hardware (multiplexers)",
      recall=r"<ul><li>\(2^n\) data inputs need n select lines.</li><li>Each AND gate is a minterm of the select lines ANDed with one data input; the OR collects them.</li></ul>"),

    Q("13(b)", 4, r"<p>Draw a NOR – NOR circuit for the Boolean expression: \((A + \overline{D})\cdot(\overline{B} + A)\cdot(\overline{D} + C)\)</p>",
      a=r"""<p>The expression is in POS form, which maps directly to NOR–NOR:</p>
<p>\(F = (A + D')(B' + A)(D' + C) = \overline{\overline{(A + D')}\ +\ \overline{(B' + A)}\ +\ \overline{(D' + C)}}\)
&nbsp; (double complement, then De Morgan)</p>
<p>So each sum term is a NOR gate (giving the complemented sum), and a final 3-input NOR of these gives F:</p>{{fig:0}}""",
      afig=[F.fig_q13b_nornor],
      topic="Computer Hardware (NAND, NOR as universal gates)",
      recall=r"<ul><li>POS → NOR–NOR: replace every OR and the final AND by NOR.</li><li>SOP → NAND–NAND.</li><li>\(\overline{\overline{X}} = X\); \((X + Y)' = X'Y'\).</li></ul>"),

    Q("13(c)", 3, r"<p>Draw logic circuit of XNOR using NOR gate only.</p>",
      a=r"""<p>Four NOR gates:</p>
<ul><li>\(G_1 = (A + B)'\)</li>
<li>\(G_2 = (A + G_1)' = A'(A + B) = A'B\)</li>
<li>\(G_3 = (B + G_1)' = B'(A + B) = AB'\)</li>
<li>\(X = (G_2 + G_3)' = (A'B + AB')' = AB + A'B' = A \odot B\)</li></ul>{{fig:0}}""",
      afig=[F.fig_q13c_xnor_nor],
      topic="Computer Hardware (NAND, NOR as universal gates)",
      recall=r"<ul><li>XNOR: \(A \odot B = AB + A'B'\), 1 when inputs are equal.</li><li>NOR is universal: NOT = NOR with inputs tied; OR = NOR followed by NOT.</li></ul>"),

    Q("14(a)", 3, r"<p>Reduce the following Expression \(AB + \overline{AC} + A\overline{B}C(AB + C)\)</p>",
      a=r"""<p>\(A\overline{B}C(AB + C) = A\overline{B}C\cdot AB + A\overline{B}C\cdot C = 0 + A\overline{B}C\) &nbsp; (\(B\overline{B} = 0\), \(CC = C\))</p>
<p>\(\overline{AC} = A' + C'\) &nbsp; (De Morgan)</p>
<p>Expression \(= AB + A' + C' + AB'C\)</p>
<p>\(= (A' + AB) + C' + AB'C = A' + B + C' + AB'C\) &nbsp; (\(A' + AB = A' + B\))</p>
<p>\(= (A' + B + C') + (A' + B + C')' = 1\) &nbsp; since \(AB'C = (A' + B + C')'\) and \(X + X' = 1\)</p>
<p><span class="box">\(= 1\)</span></p>""",
      topic="Boolean Algebra",
      recall=r"<ul><li>\(X\cdot X' = 0\), \(X + X' = 1\).</li><li>De Morgan: \((AC)' = A' + C'\).</li><li>Look for a term that is the complement of the rest.</li></ul>"),

    Q("14(b)", 4, r"<p>With the help of a logic diagram and truth table explain a Octal to Binary Encoder.</p>",
      a=r"""<p>An <b>encoder</b> converts an active input line into a binary code. An octal-to-binary encoder has 8 inputs
D0–D7 (one active at a time) and 3 outputs A2 A1 A0 giving the binary code of the active input.</p>""" +
      tt(["Active input", "A2", "A1", "A0"],
         [["D0", 0, 0, 0], ["D1", 0, 0, 1], ["D2", 0, 1, 0], ["D3", 0, 1, 1],
          ["D4", 1, 0, 0], ["D5", 1, 0, 1], ["D6", 1, 1, 0], ["D7", 1, 1, 1]]) +
      r"""<p>Each output is 1 for the inputs whose code has a 1 in that position:</p>
<p>\(A_2 = D_4 + D_5 + D_6 + D_7,\quad A_1 = D_2 + D_3 + D_6 + D_7,\quad A_0 = D_1 + D_3 + D_5 + D_7\)</p>
{{fig:0}}<p>(D0 needs no connection: its code is 000, i.e. all outputs 0.)</p>""",
      afig=[F.fig_q14b_encoder],
      topic="Computer Hardware (encoders)",
      recall=r"<ul><li>Encoder: \(2^n\) inputs → n outputs, one OR gate per output bit.</li><li>Output bit k = OR of the inputs whose number has bit k = 1.</li></ul>"),

    Q("14(c)", 3, r"<p>Derive a Boolean expression for Out in the logic diagram given below and simplify it.</p>",
      qfig=F.fig_q14c_circuit,
      a=r"""<p>Output of each gate:</p>{{fig:0}}
<p>\(Out = (B + C + D')\,(A + C + D')\,(C' + D)\)</p>
<p>\(= (C + D' + AB)(C' + D)\) &nbsp; (distributive law: \((X + B)(X + A) = X + AB\) with \(X = C + D'\))</p>
<p>\(= CC' + CD + C'D' + DD' + ABC' + ABD = CD + C'D' + ABC' + ABD\)</p>
<p>\(ABD = ABCD + ABC'D\); \(ABCD\) is contained in \(CD\) and \(ABC'D\) in \(ABC'\), so \(ABD\) is redundant:</p>
<p><span class="box">\(Out = C'D' + CD + ABC'\)</span> &nbsp; i.e. \((C \odot D) + ABC'\)</p>""",
      afig=[F.fig_q14c_labelled],
      topic="Boolean Algebra / Computer Hardware",
      recall=r"<ul><li>Write each gate's output on the diagram, working from inputs to output.</li><li>\((X + A)(X + B) = X + AB\).</li><li>Consensus/absorption removes redundant terms.</li></ul>"),

    SEC("Part II — Section B", "Answer any two questions."),

    Q("15", 10, r"""<p>Write a program to pack an array which is already sorted. To pack means to remove all duplicates from the array
i.e. if the given array has the following numbers in order: 1,2,2,3,3,3,4,4,4,4,9,11,11,14,14,14<br>
The resultant array should have the following numbers: 1,2,3,4,9,11,14</p>
<p><b>CLASS NAME</b> : Pack<br><b>DATA MEMBERS</b><br>int size : to accept the size of the array<br>
int n[ ] : to accept the values<br><b>METHODS</b><br>
void packer(… ) : <u><b>using recursion</b></u> to pack the array n.<br>void printer( ) : Print the packed array n.</p>
<p>No need to write the main().</p>""",
      a=r"""<p><b>Logic.</b> Because the array is sorted, equal values are adjacent. Keep an index k of the last value kept;
compare each n[i] with n[k] — if different, copy it to n[k+1]. The recursion advances i by one each call; the base
case i = size sets size = k + 1. (An <code>accept()</code> method is added to read the data.)</p>""" +
      jcode(M, "PackRun.java") + r"<p>Test runs (a main() was used only for testing):</p>" +
      jout(M, "pack1") + jout(M, "pack2"),
      topic="Recursion / Arrays",
      recall=r"<ul><li>Every recursion needs a base case (here i == size) and a smaller sub-problem (i + 1).</li><li>Sorted ⇒ duplicates are adjacent, so one pass suffices.</li></ul>"),

    Q("16", 10, r"""<p>A class COMMON compares its own array of numbers with a parameterized object and prints the common numbers.
Some of the members of the class are given below.</p>
<p>class name : common<br>Data Members : arr[ ] – integer – stores elements or the array<br>
n - Integer - to store the size of the array<br>Member functions/Methods<br>
void common ( int nn ) : Constructor to assign n=nn, and declares the size of arr[ ] with n.<br>
void accept ( ) : to enter the elements of the array. (without duplicates)<br>
void display(Common A ) : to display the elements which are common to parameterized object array elements with
current object array elements (if found). If not found display message accordingly.</p>
<p>Define the main( ) function to create objects and call the methods accordingly to enable the task.</p>""",
      a=r"""<p class="note">[A constructor has no return type, so "void common(int nn)" is written as the constructor
<code>Common(int nn)</code>.]</p>""" + jcode(M, "Common.java") +
      jout(M, "common1") + jout(M, "common2"),
      topic="Objects / Arrays (object passing)",
      recall=r"<ul><li>An object passed as a parameter gives access to its members: <code>A.arr[j]</code>, <code>A.n</code>.</li><li>Nested loops compare every pair; use a flag for the 'not found' message.</li></ul>"),

    Q("17", 10, r"""<p>A class MIDSORT rearranges the alphabets of a word by keeping the smallest in the centre and then next bigger one
in left and then next bigger one in the right and so on. Members of the class are shown below.</p>
<p><b>Data members</b><br>String word – to accept a word from user.<br>int len – to accept size of the word.</p>
<p><b>Member function</b><br>void readdata( ) : to accept a word for sen.<br>void centre ( ) : to change the word as shown below.</p>
<p>Input : flower &nbsp; Output : wofelr<br>Input : trouble &nbsp; Output : toeblru</p>
<p>void print ( ) : to print the changed word</p><p>No need to write the main().</p>""",
      a=r"""<p><b>Logic.</b> Sort the letters (flower → e f l o r w). Put the smallest at the centre index len/2, then
place the rest alternately to the left and to the right of what is already placed:
e at 3, f at 2, l at 4, o at 1, r at 5, w at 0 → w o f e l r.</p>""" + jcode(M, "MidRun.java") +
      jout(M, "mid1") + jout(M, "mid2") + jout(M, "mid3"),
      topic="Arrays, Strings",
      recall=r"<ul><li><code>toCharArray()</code>, sort, then build a new char array.</li><li>Centre index len/2 works for both odd and even lengths (even: one more letter goes left).</li></ul>"),

    SEC("Part II — Section C", "Answer any two questions."),

    Q("18", 5, r"""<p>Write a program to create a node class of one data and one link only.
Then assume that a linked list already exists with data and create a llist class as following:</p>
{{fig:0}}
<p>Data members: Start : object of node type<br>Member functions :<br>
Displayfront_ from_pos( ) : This function accepts a position and displays the nodes from that position
e.g. if pos is 3 this function will display 44,55,66<br>
Displayback_ from_pos( ) : This function accepts a position and displays the nodes back from that position
e.g. if pos is 3 this function will display 44,33,22</p><p>No need to write the main function.</p>""",
      qfig=F.fig_q18_list,
      a=r"""<p><b>Logic.</b> Forward: walk pos − 1 links from Start, then print to the end. Backward: the links go only
forward, so walk from Start to the pos-th node, building the output string by putting each new value in
<i>front</i> — the string then reads from node pos back to node 1.</p>""" + jcode(M, "LListRun.java") +
      r"<p>Run on the list 22 → 33 → 44 → 55 → 66 with pos = 3, 3, 1, 5, 7 (forward, back, forward, back, forward):</p>" +
      jout(M, "llist"),
      topic="Data Structures (single linked list)",
      recall=r"<ul><li>Traverse with <code>p = p.link</code> until <code>p == null</code>.</li><li>A singly linked list cannot be walked backwards: reverse by collecting (or by recursion).</li></ul>"),

    Q("19(a)", 3, r"""<p>Write the outcome of traversing in fig 1. &nbsp;(i) Preorder (ii) Post-order (iii) In-order</p>""",
      qfig=(F.fig_q19_tree, "Fig 1"),
      a=r"""<p>(i) <b>Preorder</b> (root, left, right): <span class="box">2 7 2 6 5 11 5 9 4</span></p>
<p>(ii) <b>Post-order</b> (left, right, root): <span class="box">2 5 11 6 7 4 9 5 2</span></p>
<p>(iii) <b>In-order</b> (left, root, right): <span class="box">2 7 5 6 11 2 5 4 9</span></p>
<p>(Node 5 at level 1 has only a right child 9; 9 has only a left child 4.)</p>""",
      topic="Data Structures (binary trees)",
      recall=r"<ul><li>Pre: N L R; In: L N R; Post: L R N — applied recursively to every subtree.</li><li>A missing child is simply skipped.</li></ul>"),

    Q("19(b)", 1, r"""<p>What is the worst case complexity of the following program code.</p>
<pre class="code">for( int i=1; i&lt;N; i++)
{
  for( int j=1; j&lt;M; j++)
  {
   Statements;
  }
}</pre>""",
      a=r"""<p>The outer loop runs N − 1 times and, for each, the inner loop runs M − 1 times, so Statements execute
(N − 1)(M − 1) times. Dropping constants and lower-order terms: <span class="box">O(N × M)</span>
(O(N²) when M = N).</p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>Nested independent loops multiply.</li><li>Big O keeps only the dominant term, without constants.</li></ul>"),

    Q("19(c)", 1, r"<p>What is the Complexity of Quick Sort ?</p>",
      excluded="Quick sort — not in ISC 2027: the syllabus names only bubble, selection and insertion sort (Arrays, unit 10)."),

    Q("20", 5, r"""<p>A super class 'employee' has been defined to define the basic details of an employee. Define a subclass 'salary'
to compute the area of the gross pay of the employee and print the name and gross pay by using the required data
member of the super class.</p><p>The details of the members of the class are given below:</p>
<p>class name : employee<br>data members<br>name : to store the name of employee<br>basicpay : to store the basic pay of
the employee<br>DA : to store the DA<br>methods<br>employee(...) : parameterized constructor to assign values to data
members.<br>void calDA( ) : calculates DA at the rate of 35% of basicpay.</p>
<p>class name : salary<br>data members<br>grosspay : to calculate and store the gross pay of employee ( basicpay +DA)<br>
methods<br>salary(...) : parameterised constructor to assign values to data members.<br>void calGP() : compute the
grosspay<br>void show() : displays the name,basicpay,DA,Grosspay of employee</p>
<p>The main function and algorithm need not be written.</p>""",
      a=r"""<p>The superclass is shown for completeness (the question says it is already defined); the answer is the
subclass <code>salary</code>.</p>""" + jcode(M, "SalaryRun.java") +
      r"<p>Test (name Amit Sen, basic pay 20000):</p>" + jout(M, "salary"),
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li><code>class salary extends employee</code>; <code>super(n, b)</code> first in the constructor.</li><li>Inherited (non-private) fields are used directly in the subclass.</li></ul>"),
]

PAPER = dict(
    subject="computers",
    year="2015-16",
    slug="2015-16-paper-1",
    paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2015-16/Computer science paper 1.pdf",
    marks=70, time="3 hours",
    intro=r"""<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must not start writing during
this time.)</p>
<p>Answer <b>all</b> questions in part I (compulsory) and six questions from part II, choosing two questions from sec A,
two questions from sec B and two questions from sec C. All working, including rough work should be done on the same
sheet as the rest of the answer. The intended marks of the questions or parts of questions are given in brackets ( ).
<b>Full marks is 70.</b></p>""",
    items=ITEMS,
)
