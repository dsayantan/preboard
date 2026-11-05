"""Computer Science pre-board 2024-25, Group 4 (Paper 1, Theory).
Transcribed from the page images (the PDF has a text layer, used only as a starting point).
Checks: src/checks/computers_2024_25_g4_check.py (Booleans over all rows, K-map covers, prefix,
tree, spiral order, every Java program compiled and run).
Figures: src/figs/computers_2024_25_figs.py."""
from kit import Q, SEC
import computers_2024_25_figs as F
from cs_b_kit import jcode, jout, tbl

M = "computers_2024_25_g4"


def code(s):
    return '<pre class="code">%s</pre>' % s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


AR = r"""<p>A) Both assertion and reasoning are true.<br>B) Both assertion and reasoning are false.<br>
C) The assertion is true, but the reasoning is false.<br>D) The assertion is false, but the reasoning is true.</p>"""

AR_RECALL = "<li>Judge the Assertion and the Reasoning separately, each as a statement on its own; then pick the option that matches the pair.</li>"

INTE = r"""public class preboard {
       static int Inte(String str)
    {
                if (str.length() == ____?1?___)
            return (str.charAt(0) - ___?2?___);
            double y = Inte(str.substring(1));
            double x = ?3?;
            x = x * ?4? + y;
            return (int)(x);
    }
    public static void main(String[] args)
    {
        String str = "1235";
        System.out.print(?5?);
    }
}"""

TRICK = r"""void trick(int a,int b)
{
        int p=1;
        for(int j=1;j<=b;j++,p*=a)
        System.out.println(p);
}"""

Q3A = r"""<p>Given the Boolean function: \(F(A,B,C,D) = \Sigma(5,6,7,8,9,10,11,14,15)\)</p>"""
Q3B = r"""<p>Given the Boolean function: \(F(A,B,C,D) = (A+B+C+D)(A+B+C+D')(A+B+C'+D')(A+B+C'+D)
(A+B'+C+D')(A+B'+C'+D)(A'+B+C+D)(A'+B+C'+D)\)</p>"""

KMAP_RECALL = r"""<ul><li>K-map rows and columns in Gray code: 00, 01, 11, 10 — cell numbers 0 1 3 2 / 4 5 7 6 / 12 13 15 14 / 8 9 11 10.</li>
<li>Group in powers of two (octet, quad, pair), as large as possible, wrapping round the edges; every 1 (SOP) or 0 (POS) covered, no group redundant.</li>
<li>In a group, a variable that changes is dropped; SOP: 1 → X, 0 → X′. POS: 0 → X, 1 → X′.</li></ul>"""

GATE_RECALL = r"""<ul><li>SOP → AND-OR: one AND gate per product term, all feeding one OR gate.</li>
<li>POS → OR-AND: one OR gate per sum term, all feeding one AND gate.</li>
<li>Complements are available as inputs, so no NOT gates are drawn.</li></ul>"""

Q5C = r"""<p>A sponsor partner intends to sponsor a music company to invite Bryan Adams for a live concert as per the
following criteria:</p>
<ul><li>The music company has organized live concerts earlier and is very creative<br><b>Or</b></li>
<li>The music company is very creative and is highly rated, but has not organized any live concerts earlier<br><b>Or</b></li>
<li>The music company is highly rated and has won prizes.</li></ul>
<p>The inputs are:</p>
<div class="tbl"><table><tr><th>Inputs</th><th></th></tr>
<tr><td>A</td><td>Organized live concerts earlier</td></tr>
<tr><td>B</td><td>Is very creative</td></tr>
<tr><td>C</td><td>Won prizes</td></tr>
<tr><td>D</td><td>Is highly rated</td></tr></table></div>
<p>(In all the above cases 1 indicates yes and 0 indicates no).<br>
Output: X [1 indicates yes and 0 indicates no for all cases].<br>
Draw the truth table for the inputs and outputs given above.</p>"""

Q6_TEXT = r"""<p>Design a class Duplicate to remove all duplicate characters from the string and find the resultant
string. The details of the members of the class are given below:</p>
<div class="tbl"><table>
<tr><td>Class name</td><td>Duplicate</td></tr>
<tr><th colspan="2">Data members/instance variables:</th></tr>
<tr><td>wrd</td><td>stores a String</td></tr>
<tr><td>nw</td><td>stores the modified string</td></tr>
<tr><td>len</td><td>to store the length of the word</td></tr>
<tr><th colspan="2">Methods/Member functions:</th></tr>
<tr><td>Duplicate( )</td><td>default constructor</td></tr>
<tr><td>void acceptword( )</td><td>to accept the string</td></tr>
<tr><td>String remvDup (String,String,int )</td><td>to remove all duplicate characters from the string and find the resultant string using recursion</td></tr>
<tr><td>void display( )</td><td>displays the modified string along with an appropriate message.</td></tr>
</table></div>
<p>Specify the class Duplicate giving details of the constructor, void acceptword( ), String remvDup( ) and void
display( ). Define the main( ) function to create an object and call the functions accordingly to enable the task.</p>"""

Q7_TEXT = r"""<p>A class Join has been defined to concat two numbers numerically (without using any string operations) and
produce a merged number.<br>Example: The two numbers 65 and 723 become 65723</p>
<p><b>Input :</b> 65 and 723<br><b>Output :</b> 65723<br>
<span style="margin-left:4.6em"><b>673</b></span></p>
<div class="tbl"><table>
<tr><td><b>Class Name</b></td><td><b>Join</b></td></tr>
<tr><th colspan="2">Data Members/Instance Variables</th></tr>
<tr><td>num</td><td>integer to store a number</td></tr>
<tr><th colspan="2">Member Functions/ Methods</th></tr>
<tr><td>Join()</td><td>constructor to initialize data member with legal initial value</td></tr>
<tr><td>void readNumber()</td><td>to accept the integer number in num</td></tr>
<tr><td>Join JoinNum(Join X, Join Y)</td><td>concat the numbers contained in parameterized objects X and Y numerically
(String operations are not allowed) and produces a merged number and returns the object containing the merged number.</td></tr>
<tr><td>void show()</td><td>to display the merged number and the odd positioned digit from the merged number with an appropriate message.</td></tr>
</table></div>
<p>Specify the class Join giving details of the constructor Join(), void readNumber( ), Join(Join X, Join Y ) and void
show( ). Define the main( ) function to create an object and call the functions accordingly to enable the task.</p>
<p class="note">[The second output line, 673, is printed at the top of the next page in the original. It is the
odd-positioned digits of 65723 (1st, 3rd and 5th: 6, 7, 3) — the second thing show() displays. The closing
instruction's “Join(Join X, Join Y)” means the method JoinNum(Join X, Join Y).]</p>"""

Q8_TEXT = r"""<p>A class Swirl contains a 2D Matrix of order NxM. It prints the K’th element in the spiral form of the matrix.</p>
<p>Input: arr[][] =<br>&nbsp;&nbsp;{{1, 2, 3, 4}<br>&nbsp;&nbsp;&nbsp;{5, 6, 7, 8}<br>&nbsp;&nbsp;&nbsp;{9, 10, 11, 12}<br>
&nbsp;&nbsp;&nbsp;{13, 14, 15, 16}}<br>&nbsp;k = 7<br>Output: 16<br>
Explanation: The elements in spiral order is<br>1, 2, 3, 4, 8, 12, 16, 15...so the 7th element is 16.</p>
<div class="tbl"><table>
<tr><td><b>Class Name</b></td><td><b>Swirl</b></td></tr>
<tr><th colspan="2">Data Members/Instance Variables</th></tr>
<tr><td>arr[][]</td><td>to store integer numbers</td></tr>
<tr><td>M</td><td>to store number of rows</td></tr>
<tr><td>N</td><td>to store number of columns</td></tr>
<tr><td>k</td><td>to store the K’th element</td></tr>
<tr><th colspan="2">Member Functions/ Methods</th></tr>
<tr><td>Swirl()</td><td>constructor to initialize data member with legal initial value</td></tr>
<tr><td>void read()</td><td>to accept the integer numbers and store in mat</td></tr>
<tr><td>void element_k()</td><td>returns the K’th element in the spiral form of the matrix.</td></tr>
<tr><td>void show()</td><td>to display the K’th element with an appropriate message.</td></tr>
</table></div>
<p>Specify the class Swirl giving details of the constructor, void read( ), int element_k() and void show( ). Define
the main( ) function to create an object and call the functions accordingly to enable the task.</p>
<p class="note">[As printed, the member table gives element_k() the return type void although it “returns” the
element, and the closing instruction says int element_k(); it is written here as int element_k(). “store in mat”
means the array arr[][]. The order is called N×M in the first line but M is the number of rows in the table; the
table is followed.]</p>"""

Q9_TEXT = r"""<p>A linked list is formed from the objects of the class Node. The details of the class Node is as follows:</p>
<pre class="code">Class Node
{
String str;
Node link;}</pre>
<p>Write an algorithm OR a Method to delete the start/first node containing str of an existing linked list. The
prototype of the method is : void deleteNode(Node first)</p>"""

Q10B = r"""<p>Write the Postorder traversal, depth of node 10 and size for the following binary tree.</p>"""

Q11_TEXT = r"""<p>An interface Staff is defined with a method void display( ) to print the required details of the incrementing
employee. Create the classes worker and wages which implement the interface Staff. The classes have attributes which
represent the name of the staff, basic salary for class Worker and working hours, rate per hour and total wages of
class Wages which are set by their constructor.</p>
<p><b>Interface Name : Staff</b><br><b>Member Methods</b><br>void display ( ) : to display the required details of the employee.</p>
<p><b>Class Name : Worker</b><br><b>Data members</b><br>name : to store the name of the worker<br>
basic : to store the basic pay in decimals<br><b>Member Methods</b><br>
Worker ( String ns, double bs): parameterized constructor to assign arguments to instance variables.<br>
void display ( ) : to display the worker details</p>
<p><b>Class Name : Wages</b><br><b>Data members</b><br>hours : to store hours work<br>rate : to store rate in decimals<br>
wage : to store the overall wages of the worker in decimals<br><b>Member Methods</b><br>
Wages(… ) parameterized constructor to assign values to the instance variables of the sub class and also the super class<br>
double overtime ( ) : calculates and returns the overtime amount as hours into rate<br>
void display ( ) : to calculate the wages using the formula ( wages = over-time amount + basic pay) and print all data members.</p>
<p>Specify the interface giving details of data members and method. Using the concept of inheritance, specify the
classes giving details of the methods. Define main( ) to create objects and call the methods accordingly to enable
the task.</p>"""

TREE_Q = (F.fig_q10_tree, "The binary tree as printed (redrawn)")

ITEMS = [
    SEC("Part I (20 Marks)", "(All questions are compulsory)"),

    Q("1(i)", 1, r"""<p>If a class implements an interface, what must it do?</p>
<p>A) Implement all methods of the interface<br>B) Extend the interface<br>C) Declare the interface as a variable<br>
D) Provide a constructor for the interface</p>""",
      a=r"""<p>An interface only declares method prototypes; a (non-abstract) class that implements it promises to
supply a body for every one of them. A class <i>implements</i> an interface (it does not extend it), and an interface
has no constructor.</p><p><span class="box">A) Implement all methods of the interface</span></p>""",
      topic="Inheritance, Interfaces and Polymorphism — interfaces",
      recall=r"<ul><li><code>class C implements I</code>: C must define every abstract method of I (or itself be declared abstract).</li><li>Interfaces cannot be instantiated and have no constructors.</li></ul>"),

    Q("1(ii)", 1, r"""<p><b>Assertion:</b> A class that implements an interface must implement all of its methods.<br>
<b>Reasoning:</b> If a class does not implement all methods, it can still be instantiated.</p>""" + AR,
      a=r"""<p><b>Assertion — true.</b> A concrete class implementing an interface must define all of its abstract methods,
or the compiler reports an error.<br><b>Reasoning — false.</b> A class that leaves any interface method undefined must
be declared <code>abstract</code>, and an abstract class <i>cannot</i> be instantiated.</p>
<p><span class="box">C) The assertion is true, but the reasoning is false.</span></p>""",
      topic="Inheritance, Interfaces and Polymorphism — interfaces",
      recall=r"<ul>" + AR_RECALL + r"<li>A class missing any abstract method must be <code>abstract</code>; <code>new</code> cannot create an object of an abstract class.</li></ul>"),

    Q("1(iii)", 1, r"""<p><b>Assertion:</b> The time complexity for inserting a node at the beginning of a linked list is O(1).<br>
<b>Reasoning:</b> This is because we only need to change a few pointers.</p>""" + AR,
      a=r"""<p>Insertion at the beginning needs only <code>temp.link = start; start = temp;</code> — a fixed number of
reference changes whatever the length n of the list, so the time is constant, O(1). Both statements are true (and the
reasoning is the reason for the assertion).</p>{{fig:0}}
<p><span class="box">A) Both assertion and reasoning are true.</span></p>""",
      afig=[(F.fig_q1iii_insert, "Inserting node 5 at the beginning: two assignments, independent of n")],
      topic="Data structures — single linked list; Complexity and Big O notation",
      recall=r"<ul>" + AR_RECALL + r"<li>Insert at beginning of a singly linked list: O(1); insert at end without a tail reference: O(n).</li></ul>"),

    Q("1(iv)", 1, r"""<p><b>Assertion:</b> Encoders can only work with binary inputs.<br>
<b>Reasoning:</b> This limitation makes them unsuitable for other number systems.</p>""" + AR,
      a=r"""<p><b>Assertion — false.</b> An encoder has 2<sup>n</sup> (or fewer) input lines, one per symbol, and
produces the n-bit binary code of the active line. Its inputs represent digits of other systems — the decimal-to-BCD
(10 → 4) encoder and the octal-to-binary (8 → 3) encoder are the standard examples.<br>
<b>Reasoning — false.</b> Encoders are used precisely to convert decimal, octal (or keyboard) inputs into binary,
so they are not unsuitable for other number systems.</p>
<p class="note">Each input <i>line</i> of an encoder carries a binary logic level (0 or 1), as in every digital
circuit; the assertion is about which number system the inputs represent, and there it is false.</p>
<p><span class="box">B) Both assertion and reasoning are false.</span></p>""",
      topic="Computer Hardware — encoders",
      recall=r"<ul>" + AR_RECALL + r"<li>Encoder: 2<sup>n</sup> inputs → n outputs (e.g. octal to binary 8:3, decimal to BCD 10:4). Decoder: n inputs → 2<sup>n</sup> outputs.</li></ul>"),

    Q("1(v)", 2, r"""<p>Write the difference<br>i) abstract class and interface.<br>ii) external and internal nodes of a binary tree.</p>""",
      a=r"""<p><b>i)</b></p>""" + tbl(["Abstract class", "Interface"], [
          ["Declared with <code>abstract class</code>; may have abstract methods <i>and</i> methods with bodies.",
           "Declared with <code>interface</code>; its methods are abstract (no bodies) by default."],
          ["Can have instance variables (any access) and constructors.",
           "Can have only <code>public static final</code> constants; no instance variables, no constructors."],
          ["A class can <code>extend</code> only one abstract class.",
           "A class can <code>implement</code> several interfaces."]]) +
      r"""<p><b>ii)</b></p>""" + tbl(["External node (leaf)", "Internal node"], [
          ["A node with no children (degree 0).", "A node with at least one child (degree 1 or 2)."],
          ["e.g. 1, 4, 7, 13 in the tree of Q10.", "e.g. 8, 3, 6, 10, 14 in the tree of Q10."]]),
      topic="Inheritance, Interfaces and Polymorphism; Data structures — binary trees",
      recall=r"<ul><li>Abstract class: partial implementation, single inheritance. Interface: a contract of method prototypes, multiple implementation.</li><li>Leaf = external node (no child); every other node, root included if it has a child, is internal.</li></ul>"),

    Q("1(vi)", 1, r"""<p>What is the Big O complexity for the following code segment?</p>""" +
      code("for(int k=0;k<n;k++)\n         s+=k;") +
      r"""<p>a) O(n) &nbsp; b) O(n*n) &nbsp; c) O(n<sup>2</sup>) &nbsp; d) O(1)</p>""",
      a=r"""<p>The loop body <code>s += k</code> is a constant-time statement and it executes once for each
k = 0, 1, …, n − 1, i.e. n times. Total work \(= c \cdot n\), so the complexity is linear.</p>
<p><span class="box">a) O(n)</span></p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>A single loop running n times with an O(1) body → O(n).</li><li>Nested loops each running n times → O(n<sup>2</sup>); drop constants and lower terms.</li></ul>"),

    Q("1(vii)", 1, r"""<p>With reference to the following program code answer the question</p>""" + code(TRICK) +
      r"""<p>What will be the value of method trick() when a=3 and b=4?</p>
<p>a) 12 &nbsp; b) 27 &nbsp; c) 81 &nbsp; d) 64</p>""",
      a=r"""<p>The loop prints p, <i>then</i> the update <code>j++, p*=a</code> runs.</p>""" +
      tbl(["j", "printed p", "p after p*=3"], [["1", "1", "3"], ["2", "3", "9"], ["3", "9", "27"], ["4", "27", "81"]]) +
      r"""<p>The loop stops at j = 5, so the values printed are 1, 3, 9, 27 (checked by running it). trick() is
<code>void</code> and returns nothing; the last value it displays is 27 (p becomes 81 but is never printed).</p>
<p><span class="box">b) 27</span></p>""",
      topic="Statements, Scope — looping; dry run",
      recall=r"<ul><li>In <code>for(init; cond; update)</code> the update part runs after the body, before the next test.</li><li>Trace in a table: loop variable, value used in the body, value after the update.</li></ul>"),

    Q("1(viii)", 1, r"""<p><b>Assertion:</b> A complete binary tree is a binary tree in which all levels are fully filled except
possibly the last level.<br><b>Reasoning:</b> The last level is filled from right to left.</p>""" + AR,
      a=r"""<p><b>Assertion — true:</b> that is the definition of a complete binary tree.<br>
<b>Reasoning — false:</b> the nodes of the last level are filled from <i>left to right</i> (as far left as
possible), not right to left.</p>
<p><span class="box">C) The assertion is true, but the reasoning is false.</span></p>""",
      topic="Data structures — binary trees (completeness)",
      recall=r"<ul>" + AR_RECALL + r"<li>Complete binary tree: every level full except perhaps the last, whose nodes are as far left as possible.</li></ul>"),

    Q("1(ix)", 1, r"<p>What is an exception?</p>",
      a=r"""<p>An <b>exception</b> is an abnormal condition (a run-time error) that occurs during the execution of a
program and disrupts its normal flow — e.g. dividing an integer by zero (<code>ArithmeticException</code>), an
array index out of range, or an input/output failure (<code>IOException</code>). Java represents it as an object
of a subclass of <code>Exception</code>, which is thrown and can be caught and handled with
<code>try … catch</code>.</p><p><span class="box">An exception is a run-time error event that interrupts the normal flow of a program.</span></p>""",
      topic="Objects — input/output exceptions",
      recall=r"<ul><li>Exception = run-time error object; handled with try–catch (or declared with throws).</li><li>Examples: ArithmeticException, ArrayIndexOutOfBoundsException, IOException, InputMismatchException.</li></ul>"),

    Q("2(i)", 2, r"""<p>Convert the following infix notation to prefix form.</p><p>\((A/B+C)/(D*(E-F))\)</p>""",
      a=r"""<p>Convert the innermost parts first, writing each operator before its two operands:</p>
<p><code>A/B</code> → <code>/AB</code>; &nbsp; <code>(/AB)+C</code> → <code>+/ABC</code> &nbsp; (left bracket)<br>
<code>E-F</code> → <code>-EF</code>; &nbsp; <code>D*(-EF)</code> → <code>*D-EF</code> &nbsp; (right bracket)<br>
<code>(+/ABC) / (*D-EF)</code> → <code>/ +/ABC *D-EF</code></p>
<p><span class="box">/+/ABC*D-EF</span></p>""",
      topic="Data structures — conversion of infix to prefix",
      recall=r"<ul><li>Prefix: operator before its operands; brackets disappear.</li><li>Work from the innermost bracket; / and * before + and −, left to right for equal precedence.</li></ul>"),

    Q("2(ii)", 2, r"<p>Differentiate between Direct Recursion and Indirect Recursion</p>",
      a=tbl(["Direct recursion", "Indirect recursion"], [
          ["A method calls <b>itself</b> within its own body.", "A method calls another method which in turn (directly or through others) calls the <b>first</b> method."],
          ["e.g. <code>int fact(int n){ return n==0 ? 1 : n*fact(n-1); }</code>",
           "e.g. <code>void A(int n){ if(n&gt;0) B(n-1); }</code> and <code>void B(int n){ if(n&gt;0) A(n-1); }</code>"]]),
      topic="Recursion",
      recall=r"<ul><li>Direct: f → f. Indirect (mutual): f → g → f.</li><li>Both need a base case to terminate.</li></ul>"),

    Q("2(iii)", 1, r"<p>Write the order of complexity for an if else statement.</p>",
      a=r"""<p>Only one of the two branches executes, so the cost is the test plus the larger branch. When the branches
are simple (constant-time) statements this does not depend on n:</p>
<p><span class="box">O(1)</span> (in general, O(max of the two branches)).</p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>Sequence: add the costs. if–else: cost of the condition + the costlier branch.</li><li>Constant amount of work → O(1).</li></ul>"),

    Q("2(iv)", 5, r"""<p>The following program converts string to Integer using recursion. Fill up the question marks with the
appropriate answer.</p>""" + code(INTE),
      a=r"""<p>For "1235": the last-but-first part "235" is converted recursively (y = 235), the first digit is
x = 1, and the number is x × 10<sup>length−1</sup> + y = 1000 + 235. A one-character string is the base case.</p>""" +
      tbl(["Blank", "Answer"], [["?1?", "<code>1</code>"], ["?2?", "<code>'0'</code>"],
                                ["?3?", "<code>str.charAt(0) - '0'</code>"],
                                ["?4?", "<code>Math.pow(10, str.length() - 1)</code>"],
                                ["?5?", "<code>Inte(str)</code>"]]) +
      r"""<p><b>Completed program</b> (compiled and run; it prints 1235):</p>""" + jcode(M, "Part1.java") +
      r"""<p><b>Trace</b>: Inte("5") = 5; Inte("35") = 3×10 + 5 = 35; Inte("235") = 2×100 + 35 = 235;
Inte("1235") = 1×1000 + 235 = <span class="box">1235</span></p>""",
      topic="Recursion; Strings",
      recall=r"<ul><li><code>ch - '0'</code> converts a digit character to its numeric value.</li><li>value(d<sub>1</sub>d<sub>2</sub>…d<sub>n</sub>) = d<sub>1</sub>×10<sup>n−1</sup> + value(d<sub>2</sub>…d<sub>n</sub>).</li><li><code>Math.pow</code> returns a double — hence the double variables and the final cast.</li></ul>"),

    SEC("Part II (50 Marks)"),
    SEC("Section A (20 Marks)", "(Answer any two questions)"),

    Q("3(a)(i)", 4, Q3A + r"""<p>i) Reduce the above expression by using 4-variable K map, showing the various groups (i.e., octet,
quads and pairs)</p>""",
      a=r"""<p>Place 1s in cells 5, 6, 7, 8, 9, 10, 11, 14, 15 (0s elsewhere):</p>{{fig:0}}
<p><b>Quad 1</b> (8, 9, 11, 10) — row AB′: \(AB'\)<br>
<b>Quad 2</b> (7, 6, 15, 14) — B = 1, C = 1 in all four: \(BC\)<br>
<b>Pair</b> (5, 7) — A′B with D = 1: \(A'BD\)<br>
Every 1 is covered and no group is redundant (cell 5 has no larger group: 13 and 4 are 0).</p>
<p><span class="box">\(F = AB' + BC + A'BD\)</span></p>""",
      afig=[(F.fig_q3a_kmap, "K-map: quads AB′ and BC (dashed), pair A′BD")],
      topic="Boolean Algebra — Karnaugh maps (SOP)",
      recall=KMAP_RECALL),

    Q("3(a)(ii)", 1, Q3A + r"""<p>ii) Draw the logic gate diagram for the reduced expression. Assume that the variables and their
complements are available as inputs.</p>""",
      a=r"""<p>\(F = AB' + BC + A'BD\): three AND gates feeding one OR gate.</p>""",
      afig=[(F.fig_q3a_circuit, "F = A′BD + BC + AB′ (AND-OR)")],
      topic="Computer Hardware — logic gates for an SOP expression",
      recall=GATE_RECALL),

    Q("3(b)(i)", 4, Q3B + r"""<p>i) Reduce the above expression by using 4 variable K-map showing the various groups (i.e., octet,
quads and pairs).</p>""",
      a=r"""<p>Each sum term is a maxterm (0 → X, 1 → X′): \(A+B+C+D = 0000 = M_0\), and likewise
\(M_1, M_3, M_2, M_5, M_6, M_8, M_{10}\), so \(F = \pi(0,1,2,3,5,6,8,10)\). Put 0s in these cells:</p>{{fig:0}}
<p><b>Quad 1</b> (0, 1, 3, 2) — row A + B: \((A+B)\)<br>
<b>Quad 2</b> (0, 2, 8, 10) — the four corners, B = 0 and D = 0: \((B+D)\)<br>
<b>Pair 1</b> (1, 5) — A = 0, C = 0, D = 1: \((A+C+D')\)<br>
<b>Pair 2</b> (2, 6) — A = 0, C = 1, D = 0: \((A+C'+D)\)<br>
Cells 5 and 6 have no larger group (their neighbours 4, 7, 13, 14 are 1s).</p>
<p><span class="box">\(F = (A+B)(B+D)(A+C+D')(A+C'+D)\)</span></p>""",
      afig=[(F.fig_q3b_kmap, "K-map of the 0s: quad (A+B), corner quad (B+D) (dashed), pairs (A+C+D′) and (A+C′+D)")],
      topic="Boolean Algebra — Karnaugh maps (POS)",
      recall=KMAP_RECALL),

    Q("3(b)(ii)", 1, Q3B + r"""<p>ii) Draw the logic gate diagram for the reduced expression. Assume that the variables and their
complements are available as inputs</p>""",
      a=r"""<p>\(F = (A+B)(B+D)(A+C+D')(A+C'+D)\): four OR gates feeding one AND gate.</p>""",
      afig=[(F.fig_q3b_circuit, "F = (A+B)(B+D)(A+C+D′)(A+C′+D) (OR-AND)")],
      topic="Computer Hardware — logic gates for a POS expression",
      recall=GATE_RECALL),

    Q("4(a)", 5, r"""<p>Draw the logic circuit to decode the binary numbers (0010, 0101, 0111, 1000, 1010, 1100, 1110, 1111).
Also state the hexadecimal equivalents of the given binary numbers.</p>""",
      a=r"""<p>Each number is detected by a 4-input AND gate fed with A, B, C, D (A the MSB): a bit 1 takes the
variable, a bit 0 its complement — so the gate outputs 1 for that input combination only.</p>""" +
      tbl(["Binary ABCD", "AND gate", "Hexadecimal"], [
          ["0010", "A′B′CD′", "2"], ["0101", "A′BC′D", "5"], ["0111", "A′BCD", "7"], ["1000", "AB′C′D′", "8"],
          ["1010", "AB′CD′", "A"], ["1100", "ABC′D′", "C"], ["1110", "ABCD′", "E"], ["1111", "ABCD", "F"]]) +
      r"""{{fig:0}}<p><span class="box">Hexadecimal: 2, 5, 7, 8, A, C, E, F</span></p>""",
      afig=[(F.fig_q4a_decoder, "Decoder: inputs A B C D and their complements (NOT gates), one AND gate per number")],
      topic="Computer Hardware — decoders",
      recall=r"<ul><li>A decoder output for a code word = AND of the inputs, complemented where the bit is 0.</li><li>Each group of 4 bits = one hexadecimal digit (1010 = A … 1111 = F).</li></ul>"),

    Q("4(b)", 3, r"""<p>Verify the following proposition is valid using truth table</p>
<p>\(A \Rightarrow (B \wedge C) = (A \Rightarrow B) \wedge (B \Rightarrow C)\)</p>""",
      a=r"""<p>Let L = \(A \Rightarrow (B\wedge C)\) and R = \((A\Rightarrow B)\wedge(B\Rightarrow C)\); the proposition
is valid only if L ⇔ R is true in every row.</p>""" +
      tbl(["A", "B", "C", "B∧C", "L = A⇒(B∧C)", "A⇒B", "B⇒C", "R", "L ⇔ R"], [
          ["0", "0", "0", "0", "1", "1", "1", "1", "1"],
          ["0", "0", "1", "0", "1", "1", "1", "1", "1"],
          ["0", "1", "0", "0", "<b>1</b>", "1", "0", "<b>0</b>", "<b>0</b>"],
          ["0", "1", "1", "1", "1", "1", "1", "1", "1"],
          ["1", "0", "0", "0", "0", "0", "1", "0", "1"],
          ["1", "0", "1", "0", "0", "0", "1", "0", "1"],
          ["1", "1", "0", "0", "0", "1", "0", "0", "1"],
          ["1", "1", "1", "1", "1", "1", "1", "1", "1"]]) +
      r"""<p>In the row A = 0, B = 1, C = 0 the left side is 1 but the right side is 0, so the two sides are not
equivalent.</p>
<p><span class="box">The proposition is <b>not valid</b> (L ⇔ R is a contingency, false for A = 0, B = 1, C = 0).</span></p>
<p class="note">The valid law is \(A \Rightarrow (B\wedge C) \equiv (A\Rightarrow B)\wedge(A\Rightarrow C)\) — with
A, not B, in the second implication its truth table matches column L in all eight rows. The question as printed
(B ⇒ C) is answered above.</p>""",
      topic="Boolean Algebra — propositional logic (validity, truth tables)",
      recall=r"<ul><li>p ⇒ q is false only when p = 1 and q = 0.</li><li>Two wffs are equivalent (the biconditional is valid) only if their columns agree in every row; one counter-example row disproves it.</li></ul>"),

    Q("4(c)(i)", 1, r"""<p>From the following diagram answer the following</p>{{fig:0}}
<p>i) Which relation in propositional logic is depicted by the above gate?</p>""",
      qfig=[(F.fig_q4c_xnor, "The gate as printed (redrawn)")],
      a=r"""<p>The gate is an XNOR (equivalence) gate: Y = 1 exactly when A and B are equal, which is the truth table of
the biconditional.</p><p><span class="box">Biconditional (equivalence), \(A \Leftrightarrow B\)</span></p>""",
      topic="Computer Hardware — logic gates; Propositional logic",
      recall=r"<ul><li>XNOR: output 1 when inputs are equal. XOR: output 1 when they differ.</li><li>p ⇔ q ≡ (p ⇒ q) ∧ (q ⇒ p): true when p and q have the same truth value.</li></ul>"),

    Q("4(c)(ii)", 1, r"""<p>(Refer to the gate in 4(c).)</p>{{fig:0}}
<p>ii) Write the boolean expression and draw the logic symbol for the above gate</p>""",
      qfig=[(F.fig_q4c_xnor, "The gate as printed (redrawn)")],
      a=r"""<p><span class="box">\(Y = A \odot B = \overline{A \oplus B} = A'B' + AB\)</span></p>
<p>Logic symbol (XNOR) and its realisation with basic gates:</p>""",
      afig=[(F.fig_q4c_xnor, "XNOR gate symbol"), (F.fig_q4c_xnor_gates, "Y = A′B′ + AB with AND-OR gates")],
      topic="Computer Hardware — logic gates (XNOR)",
      recall=r"<ul><li>XNOR = NOT(XOR): \(\overline{A\oplus B} = AB + A'B'\).</li><li>Symbol: OR body, extra curved line at the input side, bubble at the output.</li></ul>"),

    Q("5(a)", 3, r"""<p>A 4x1 MUX is shown in the figure below: Write the output of Z using exclusive gates.</p>""",
      qfig=[(F.fig_q5a_mux, "The multiplexer as printed (redrawn)")],
      a=r"""<p>Taking S1 = A as the more significant select bit and S2 = B as the less significant one, a 4 × 1 MUX gives</p>
<p>\(Z = A'B'I_0 + A'BI_1 + AB'I_2 + ABI_3\)</p>
<p>Substitute \(I_0 = I_1 = C\) and \(I_2 = I_3 = C'\):</p>
<p>\(Z = A'B'C + A'BC + AB'C' + ABC' = A'C(B' + B) + AC'(B' + B) = A'C + AC'\)</p>
<p><span class="box">\(Z = A'C + AC' = A \oplus C\)</span> — a single XOR gate of A and C; B has no effect.</p>{{fig:0}}
<p class="note">The figure numbers the select lines S1, S2 without saying which is the MSB. With the usual
convention (the first-listed line, S1 = A, is the MSB) A picks between the C pair (I0, I1) and the C′ pair (I2, I3),
giving A ⊕ C. If S2 = B were taken as the MSB, the same working gives \(Z = B \oplus C\); state the convention used.</p>""",
      afig=[(F.fig_q5a_xor, "Z = A ⊕ C")],
      topic="Computer Hardware — multiplexers",
      recall=r"<ul><li>4:1 MUX: \(Y = S_1'S_0'I_0 + S_1'S_0I_1 + S_1S_0'I_2 + S_1S_0I_3\) — the select lines pick one input.</li><li>\(X'Y + XY' = X \oplus Y\) (exclusive OR).</li></ul>"),

    Q("5(b)", 3, r"<p>Simplify the boolean expression \((A+B)(A+B')(A'+C)\)</p>",
      a=r"""<p>\((A+B)(A+B') = A + BB'\) &nbsp; (distributive law: \((X+Y)(X+Z) = X + YZ\))<br>
\(= A + 0 = A\) &nbsp; (complement law \(BB' = 0\), identity)<br>
So the expression is \(A(A'+C) = AA' + AC\) &nbsp; (distributive law)<br>
\(= 0 + AC = AC\) &nbsp; (complement law \(AA' = 0\))</p>
<p><span class="box">\(AC\)</span></p>""",
      topic="Boolean Algebra — laws and theorems",
      recall=r"<ul><li>Distributive: \((X+Y)(X+Z) = X + YZ\); \(X(Y+Z) = XY + XZ\).</li><li>Complement: \(XX' = 0\), \(X + X' = 1\); identity \(X + 0 = X\).</li></ul>"),

    Q("5(c)", 4, Q5C,
      a=r"""<p>From the three criteria: \(X = AB + A'BD + CD\) (A organised concerts, B creative, C won prizes,
D highly rated). X = 1 in a row if any criterion holds:</p>{{fig:0}}
<p><span class="box">X = 1 for rows 3, 5, 7, 11, 12, 13, 14, 15, i.e. \(X(A,B,C,D) = \Sigma(3,5,7,11,12,13,14,15)\)</span></p>
<p class="note">(Not asked: the expression reduces to \(X = AB + BD + CD\).)</p>""",
      afig=[(F.fig_q5c_truth, "Truth table: shaded rows have X = 1, with the criterion satisfied")],
      topic="Boolean Algebra — truth tables from a word problem",
      recall=r"<ul><li>Write each criterion as a product term (“not” → complemented variable); join the criteria with OR.</li><li>List all 2<sup>4</sup> = 16 rows in binary order with A as the MSB.</li></ul>"),

    SEC("Section B (20 Marks)", "(Answer any two questions)"),

    Q("6", 10, Q6_TEXT,
      a=r"""<p><b>Idea:</b> remvDup(s, r, i) examines character i of s; it is appended to the result r only if r does not
already contain it (so the first occurrence of each character is kept). The base case is i = len, when the whole
string has been examined and r is returned.</p>""" + jcode(M, "Duplicate.java") +
      r"<p><b>Sample runs</b></p>" + jout(M, "dup1") + jout(M, "dup2"),
      topic="Recursion; Strings",
      recall=r"<ul><li><code>r.indexOf(ch) == -1</code> means ch is not yet in r.</li><li>A recursive string method: base case at the end of the string; each call handles one character and recurses on i + 1.</li></ul>"),

    Q("7", 10, Q7_TEXT,
      a=r"""<p><b>Idea:</b> appending the digits of Y to X numerically means shifting X left by as many decimal places
as Y has digits: \(65 \times 10^3 + 723 = 65723\). The digits of Y are counted with a loop (a do–while, so that 0
counts as one digit). For the odd positions (counted from the left: 1st, 3rd, 5th …) the digits are peeled from
the right while the position is counted down from the total number of digits.</p>""" + jcode(M, "Join.java") +
      r"<p><b>Sample runs</b> (the paper's example, then 1203 and 0)</p>" + jout(M, "join1") + jout(M, "join2"),
      topic="Objects — passing and returning objects; Methods (number problems)",
      recall=r"<ul><li>Digits of n: count how many times n can be divided by 10 before it becomes 0.</li><li>Concatenate numerically: \(x \cdot 10^{d(y)} + y\).</li><li>A method can take objects as parameters, create a new object and return it.</li></ul>"),

    Q("8", 10, Q8_TEXT,
      a=r"""<p><b>Idea:</b> keep four boundaries — top, bottom, left, right. Go along the top row (left → right),
down the right column, back along the bottom row (right → left), up the left column; then move each boundary one
step inwards and repeat. Count elements as they are visited and return the one at count k.</p>{{fig:0}}""" +
      jcode(M, "Swirl.java") +
      r"<p><b>Sample runs</b> (the paper's example; a 3 × 4 matrix, whose spiral is 1 2 3 4 8 12 11 10 9 5 6 7; an invalid k)</p>" +
      jout(M, "swirl1") + jout(M, "swirl2") + jout(M, "swirl3"),
      afig=[(F.fig_q8_spiral, "Spiral order of the example: 1, 2, 3, 4, 8, 12, 16, … — the 7th is 16")],
      topic="Arrays — two-dimensional arrays",
      recall=r"<ul><li>Spiral traversal: four boundary variables; after each side, shrink that side's boundary.</li><li>Check top ≤ bottom and left ≤ right before the third and fourth sides, or a single remaining row/column is visited twice.</li></ul>"),

    SEC("Section C (10 Marks)", "(Answer any two questions)"),

    Q("9", 5, Q9_TEXT,
      a=r"""<p>“The start/first node” is the node <code>first</code> refers to. Java passes the reference
<code>first</code> by value, so the method cannot make the caller's start variable point to the second node.
Instead it removes the first node's <i>contents</i>: the second node's data is copied into the first node and the
second node is unlinked. The list seen from the caller's start reference is then the old list without its first
element.</p>
<p><b>Algorithm</b></p>
<ol><li>Start.</li>
<li>If first = null, display “List is empty” and stop.</li>
<li>If first.link = null (only one node), clear first.str and report that the caller must set start = null; stop.</li>
<li>second ← first.link.</li>
<li>first.str ← second.str.</li>
<li>first.link ← second.link.</li>
<li>second.link ← null.</li>
<li>Stop.</li></ol>{{fig:0}}
<p><b>Method</b></p>""" + jcode(M, "DeleteNode.java") +
      r"""<p><b>Test run</b> (list Red → Green → Blue → Pink; delete twice; then a one-node list and an empty list):</p>""" +
      jout(M, "delete") +
      r"""<p class="note">If the list's start is a data member of the list class (as in most ISC programs), the usual
answer is simply <code>if (start != null) start = start.link;</code> — the method here keeps to the printed
prototype.</p>""",
      afig=[(F.fig_q9_delete, "Deleting the start node through void deleteNode(Node first)")],
      topic="Data structures — single linked list (deletion)",
      recall=r"<ul><li>Deleting the first node of a list: start = start.link (O(1)).</li><li>Object references are passed by value: a method can change the object's fields but not the caller's variable.</li><li>Always handle the empty list and the one-node list.</li></ul>"),

    Q("10(a)", 2, r"<p>Is binary tree a recursive data structure? Justify your answer.</p>",
      a=r"""<p><b>Yes.</b> A binary tree is defined in terms of itself: it is either empty, or it consists of a root
node together with a <b>left subtree</b> and a <b>right subtree</b>, each of which is again a binary tree. Because
of this, operations on it (traversals, counting nodes, height) are written naturally as recursive methods —
e.g. size(T) = 1 + size(left) + size(right), with size(empty) = 0 as the base case.</p>""",
      afig=[(F.fig_q10_recursive, "A binary tree = root + left subtree + right subtree (each a binary tree)")],
      topic="Data structures — binary trees",
      recall=r"<ul><li>Recursive definition: empty, or root + left binary tree + right binary tree.</li><li>Pre/in/post-order traversals are recursive.</li></ul>"),

    Q("10(b)", 3, Q10B,
      qfig=TREE_Q,
      a=r"""<p><b>Postorder</b> (Left, Right, Root), applied to each subtree:<br>
left subtree of 8: 1, then (4, 7, 6), then 3 → 1 4 7 6 3;<br>
right subtree of 8: 10 has no left child; its right subtree is 13 14 → 13 14 10;<br>
then the root 8.</p>
<p><span class="box">Postorder: 1, 4, 7, 6, 3, 13, 14, 10, 8</span></p>
<p><b>Depth of node 10</b> = number of edges from the root to it = 1 (it is a child of the root; level 1 if the root is at level 0).</p>
<p><span class="box">Depth of 10 = 1</span></p>
<p><b>Size</b> = number of nodes (8, 3, 10, 1, 6, 14, 4, 7, 13):</p><p><span class="box">Size = 9</span></p>""",
      topic="Data structures — binary trees, traversals",
      recall=r"<ul><li>Postorder: left subtree, right subtree, root.</li><li>Depth of a node = edges on the path from the root (root has depth 0).</li><li>Size = total number of nodes.</li></ul>"),

    Q("11", 5, Q11_TEXT,
      a=r"""<p>The interface carries only the method prototype (an interface has no instance data members — any
variable in it is a <code>public static final</code> constant). Worker implements Staff; Wages extends Worker, so it
is also a Staff, and its constructor passes the name and basic pay to the superclass with
<code>super(…)</code>.</p>{{fig:0}}""" + jcode(M, "Staff.java") +
      jout(M, "staff"),
      afig=[(F.fig_q11_classes, "Staff ← Worker ← Wages")],
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li>Interface methods are implicitly public abstract — the implementing method must be declared <code>public</code>.</li><li><code>super(args)</code> must be the first statement of the subclass constructor; <code>super.display()</code> reuses the parent's method.</li><li>A Staff reference calling display() runs the object's own version (dynamic binding).</li></ul>"),
]

PAPER = dict(
    subject="computers",
    year="2024-25",
    slug="2024-25-group-4",
    paper="Paper 1 (Theory) — Group 4",
    source="PreBoard-PYQ/2024-25/SET-1/COMPUTER THEORY.pdf",
    marks=70, time="3 hours",
    practical=False,
    intro=r"""<p><b>The Heritage School — Pre Board Examination 2024-25 — Computer Science Theory Paper – Group 4 — Class XII</b></p>
<p>Full Marks: 70 &nbsp; Time: 3 hours</p>
<p>Part I (20 Marks): all questions are compulsory. Part II (50 Marks): Section A (20 marks), answer any two questions;
Section B (20 marks), answer any two questions; Section C (10 marks), answer any two questions.</p>
<p>This question paper consists of 9 printed pages.</p>""",
    items=ITEMS,
)
