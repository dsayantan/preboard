"""Computer Science pre-board 2025-26, Group 4 (Paper 1, Theory).
Transcribed from the page images (the PDF has a text layer, used only as a starting point).
Checks: src/checks/computers_2025_26_g4_check.py (Booleans over all rows, address, postfix,
every Java program compiled and run).  Figures: src/figs/computers_2025_26_figs.py."""
from kit import Q, SEC
import computers_2025_26_figs as F
from cs_b_kit import jcode, jout, tbl
import infix as IX

M = "computers_2025_26_g4"
TREE_Q = (F.fig_q11_tree, "The binary tree as printed (redrawn)")


def code(s):
    return '<pre class="code">%s</pre>' % s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


PF, PF_STEPS = IX.to_postfix("((A-B)/(C*(D+E)))+F^(G-H)")

INTRO = r"""<p>Candidates are allowed <b>additional 15 minutes</b> for <b>only</b> reading the paper.</p>
<p>Answer <b>all</b> questions in Part I (compulsory) and <b>six</b> questions from Part II, choosing <b>two</b>
questions from Section-A, <b>two</b> from Section B, and <b>two</b> from Section C.</p>
<p>All work, including rough work, should be done on the same sheet as <span class="note">[the line breaks off here in the original]</span></p>
<p>The intended marks for questions or parts of questions are given in brackets [ ].</p>
<p class="note">[As printed, Question 1 has no part (iii) — the numbering runs (i), (ii), (iv) … (x) — so
Part I adds up to 19 marks, not the 20 in its heading. Question 11 prints “(i)” twice; the second
(the binary tree) is shown here as 11(ii).]</p>"""

FINDPOS = r"""public int findPos(int arr[], int f, int l, int x)
{
  if (f > l)
     return -1;

  int m = (2 * f + l) / 3;

  if (arr[m] == x)
     return m;
  else if (arr[m] > x)
     return findPos(arr, f, m - 1, x);
  else
  {
     int k = findPos(arr, m + 1, l, x);
     if (k == -1)
        return -1;
     else
        return k + 1;
  }
}"""

TRIB = r"""public int tribonacci(int n)
{
   if (?1)
      return 0;
   else if (?2)
      return 1;
   else
      return tribonacci(n - 1) + tribonacci(n - 2) + ?3;
}"""

TRIB_Q = (r"""<p>The following is a function of class <b>Tribonacci</b>. This recursive function calculates and
returns the n<sup>th</sup> term of the <b>Tribonacci series</b>. The Tribonacci series is similar to the
Fibonacci series, but each term is the <b>sum of the previous three terms</b>.
<i>(Example: 0, 1, 1, 2, 4, 7, 13, 24, …)</i> Some statements or expressions are missing and are marked by
<b>?1</b>, <b>?2</b>, and <b>?3</b>. Replace each with suitable code so that the function works correctly.</p>"""
          + code(TRIB))

TRIB_RECALL = r"""<ul><li>A recursive method needs a base case for every starting term it cannot compute from earlier ones.</li>
<li>Tribonacci: \(T_n = T_{n-1} + T_{n-2} + T_{n-3}\), with three seed terms 0, 1, 1.</li>
<li>Test a filled-in method by tracing the first few terms against the given series.</li></ul>"""

Q3_TEXT = r"""<p>A student from the Computer Science department is tasked with designing a <b>smart lighting control
system</b> for a home. The system uses sensors to determine whether to automatically turn the lights on or off
in a specific room.</p>
<ul><li>If the motion is not detected in the room and the Ambient light is low<br><b>OR</b></li>
<li>If the motion is detected in the room and the ambient light is low but the current time is not between
6PM and 6AM.<br><b>OR</b></li>
<li>If the motion is not detected in the room and the ambient light is not low but the manual switch override
is turned on by the user</li></ul>
<p>The inputs are:</p>
<div class="tbl"><table><tr><th>INPUTS</th><th></th></tr>
<tr><td>M</td><td>Motion is detected in the room</td></tr>
<tr><td>L</td><td>Ambient light level is low</td></tr>
<tr><td>T</td><td>Current time is between 6 PM and 6 AM</td></tr>
<tr><td>S</td><td>Manual switch override is turned on by the user</td></tr></table></div>
<p>(In all the above cases 1 indicates yes and 0 indicates no.)</p>
<p>OUTPUT: X [1 indicates high power, 0 indicates low power for all cases]</p>"""

Q4_F = r"""<p>Given \(F(A, B, C, D) = (A + B + C + D)\cdot(A + B + C + D')\cdot(A + B + C' + D')\cdot
(A + B + C' + D)\cdot(A + B' + C + D')\cdot(A + B' + C' + D')\cdot(A' + B + C + D)\cdot(A' + B + C' + D)\).</p>"""

Q5II_Q = r"""<p>In the given logic gate diagram, F4 is a contradiction. State true or false. Justify your answer
using Truth table.</p>"""

Q9_CLASS = r"""<p>A class Repeat allows the user to insert integer elements from one end (rear) and delete elements
from the other end (front) only. This forms a restricted linear data structure. The details of the class
Repeat are given below:</p>
<div class="tbl"><table>
<tr><td>Class name</td><td>Repeat</td></tr>
<tr><th colspan="2">Data members / instance variables</th></tr>
<tr><td>st[]</td><td>an array to hold a maximum of 100 integer elements.</td></tr>
<tr><td>cap</td><td>stores the capacity of the array.</td></tr>
<tr><td>f</td><td>to point to the index of the front.</td></tr>
<tr><td>r</td><td>to point to the index of the rear.</td></tr>
<tr><th colspan="2">Member functions</th></tr>
<tr><td>Repeat(int m)</td><td>constructor to initialize data members cap = m, f = 0, r = -1 and to create the integer array st[].</td></tr>
<tr><td>void pushValue(int v)</td><td>to insert an element from the rear, if space is available; otherwise display the message “Overflow! Insertion not possible.”</td></tr>
<tr><td>int popValue()</td><td>to remove and return an element from the front, if the structure is not empty; otherwise return -9999 and display “Underflow! Deletion not possible.”</td></tr>
<tr><td>void disp()</td><td>to display the current elements in the queue from front to rear.</td></tr>
</table></div>"""

Q11T = r"""<p>Answer the following questions from the diagram of a Binary Tree given below:</p>"""

TREE_RECALL = r"""<ul><li>Root of a sub-tree = the child of the root on that side; siblings share a parent.</li>
<li>Size = number of nodes; depth/height = number of edges on the longest root-to-leaf path (levels − 1).</li>
<li>In-order: Left, Root, Right — applied recursively.</li></ul>"""

ITEMS = [
    SEC("Part I – 20 Marks", "Answer <b>all</b> questions. While answering questions in this Part, indicate "
        "briefly your working and reasoning, wherever required."),

    Q("1(i)", 1, r"""<p>Which statements are valid for static member methods?</p>
<p>I. Can access static &amp; non-static data members.<br>II. Can call non-static methods.<br>
III. Cannot refer to this or super.</p>
<p>(a) I &amp; II &nbsp; (b) II &amp; III &nbsp; (c) I &amp; III &nbsp; (d) Only III</p>""",
      a=r"""<p>A static method belongs to the class, not to any object, so it has no <code>this</code>; it cannot use
instance (non-static) data members or call non-static methods directly (I and II are false), and it cannot
refer to <code>this</code> or <code>super</code> (III is true).</p>
<p><span class="box">(d) Only III</span></p>""",
      topic="Objects — static methods and variables",
      recall=r"<ul><li>static = one copy per class, exists without any object.</li><li>A static method can directly use only static members; instance members need an object reference.</li><li><code>this</code>/<code>super</code> refer to the current object — none exists in a static context.</li></ul>"),

    Q("1(ii)", 1, r"""<p>If binary search uses recursion instead of iteration, which of the following is valid?</p>
<p>i. It will contain two base cases.<br>ii. It will contain two recursive cases.<br>
iii. When executed will lead to StackOverflow error.</p>
<p>(a) i &amp; ii &nbsp; (b) ii &amp; iii &nbsp; (c) i &amp; iii &nbsp; (d) Only iii</p>
<p class="note">[The paper prints the mark [1] twice against this part; it is a single 1-mark question.]</p>""",
      a=r"""<p>Recursive binary search stops in two cases — the range is empty (<code>low &gt; high</code>, not found)
or <code>a[mid] == key</code> (found): <b>two base cases</b>. Otherwise it recurses either on the left half or
on the right half: <b>two recursive cases</b>. The depth is only about \(\log_2 n\), so it does not overflow the
stack (iii is false).</p>
<p><span class="box">(a) i &amp; ii</span></p>""",
      topic="Recursion",
      recall=r"<ul><li>Base case: stops the recursion; recursive case: calls itself on a smaller problem.</li><li>Binary search halves the range each call — depth \(O(\log n)\).</li></ul>"),

    Q("1(iv)", 1, r"""<pre class="code">interface A { void abc(); }
interface B { void abc(); }
class Check implements A, B { ... }</pre>
<p>How many times abc() must be defined?</p>
<p>(a) Twice &nbsp; (b) Once &nbsp; (c) Compile time error &nbsp; (d) Runtime error</p>""",
      a=r"""<p>Both interfaces declare the same signature <code>void abc()</code>. Interface methods carry no body, so
there is no conflict: one <code>public void abc() { … }</code> in <code>Check</code> implements the method of
both A and B. (Defining it twice would itself be a compile error — a duplicate method.)</p>
<p><span class="box">(b) Once</span></p>""",
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li>A class can implement several interfaces.</li><li>Identical abstract signatures from two interfaces are satisfied by one method.</li><li>Implementing methods must be <code>public</code>.</li></ul>"),

    Q("1(v)", 1, r"""<p>Find the time complexity of:</p>
<pre class="code">for(i=0;i&lt;x;i++)
   m *= Math.random();
for(j=0;j&lt;y;j++)
   n *= Math.random();</pre>
<p>(a) O(x) &nbsp; (b) O(y) &nbsp; (c) O(x+y) &nbsp; (d) O(xy)</p>""",
      a=r"""<p>The two loops are <b>sequential</b>, not nested: the first runs x times, the second y times, each body
\(O(1)\). Total work \(\propto x + y\); neither term dominates since x and y are independent.</p>
<p><span class="box">(c) O(x+y)</span></p>""",
      topic="Complexity and Big O notation",
      recall=r"<ul><li>Sequential blocks: add the complexities; nested loops: multiply.</li><li>Keep every term that depends on a different input size.</li></ul>"),

    Q("1(vi)", 1, r"""<pre class="code">System.out.println("RocKet".substring(0,4).compareTo("Rock".replace('m','o')));</pre>
<p>(a) 0 &nbsp; (b) -32 &nbsp; (c) +32 &nbsp; (d) Error</p>""",
      a=r"""<p><code>"RocKet".substring(0,4)</code> = <code>"RocK"</code> (indices 0–3).</p>
<p><code>"Rock".replace('m','o')</code> = <code>"Rock"</code> (there is no 'm', so nothing changes).</p>
<p><code>"RocK".compareTo("Rock")</code>: the first difference is at index 3, 'K' (75) vs 'k' (107), so the
result is 75 − 107 = −32. (Checked by running it.)</p>
<p><span class="box">(b) -32</span></p>""",
      topic="Strings",
      recall=r"<ul><li><code>substring(a, b)</code> takes indices a to b − 1.</li><li><code>compareTo</code> returns the difference of the first unequal characters' codes (or of the lengths).</li><li>'A'–'Z' = 65–90, 'a'–'z' = 97–122; upper/lower differ by 32.</li></ul>"),

    Q("1(vii)", 1, r"""<p>What gets printed?</p>
<pre class="code">char[] set = {'*','D','5'};
System.out.print(Character.isDigit(set[2])+" ");
System.out.print(Character.isWhitespace(set[0])+" ");
System.out.print(Character.isLetterOrDigit(set[1]));</pre>
<p>(a) true false true &nbsp; (b) false false true &nbsp; (c) true true false &nbsp; (d) false true false</p>""",
      a=r"""<p><code>isDigit('5')</code> → true; <code>isWhitespace('*')</code> → false;
<code>isLetterOrDigit('D')</code> → true. Output: <code>true false true</code> (checked by running it).</p>
<p><span class="box">(a) true false true</span></p>""",
      topic="Primitive values, Wrapper classes — Character",
      recall=r"<ul><li><code>Character.isDigit</code>, <code>isLetter</code>, <code>isLetterOrDigit</code>, <code>isWhitespace</code>, <code>isUpperCase</code> all return boolean.</li><li>Whitespace = space, tab, newline etc.; '*' is a symbol.</li></ul>"),

    Q("1(viii)", 1, r"""<p>The contrapositive of \(p' \Rightarrow q\) is:</p>
<p>(a) \(q' \Rightarrow p\) &nbsp; (b) \(q \Rightarrow p'\) &nbsp; (c) \(p \Rightarrow q'\) &nbsp; (d) \(q \Rightarrow p\)</p>""",
      a=r"""<p>Contrapositive of \(a \Rightarrow b\) is \(b' \Rightarrow a'\). With \(a = p'\), \(b = q\):
\(q' \Rightarrow (p')' = q' \Rightarrow p\). (It is logically equivalent to the original — checked over all four rows.)</p>
<p><span class="box">(a) \(q' \Rightarrow p\)</span></p>""",
      topic="Propositional logic",
      recall=r"<ul><li>Converse \(b\Rightarrow a\); inverse \(a'\Rightarrow b'\); contrapositive \(b'\Rightarrow a'\).</li><li>Only the contrapositive is equivalent to the original statement.</li><li>Involution: \((p')' = p\).</li></ul>"),

    Q("1(ix)", 1, r"<p>What is the space complexity of the recursive Fibonacci function?</p>",
      a=r"""<p>For <code>fib(n) = fib(n−1) + fib(n−2)</code> the calls are made one branch at a time, so at most
n frames are on the call stack together (the chain n, n−1, …, 1). The extra memory grows linearly with n.</p>
<p><span class="box">O(n)</span> &nbsp; (its time complexity, by contrast, is \(O(2^n)\)).</p>""",
      topic="Complexity and Big O notation; Recursion",
      recall=r"<ul><li>Space of a recursive method = maximum depth of the call stack × space per frame.</li><li>Do not confuse with the number of calls (time).</li></ul>"),

    Q("1(x)", 1, r"<p>Define abstraction in object-oriented programming.</p>",
      a=r"""<p><b>Abstraction</b> is the act of representing only the <b>essential features</b> of an object while
<b>hiding the background details</b> (the implementation). E.g. a user calls <code>list.add(x)</code> without
knowing how the list stores x. In Java it is achieved through classes, abstract classes and interfaces.</p>""",
      topic="Objects — OOP principles",
      recall=r"<ul><li>Abstraction: show what, hide how.</li><li>Encapsulation: wrap data and methods together and restrict access.</li></ul>"),

    Q("2(i)", 2, r"""<p>Convert the following <i>infix notation</i> to <i>postfix</i> form.</p>
<p style="text-align:center"><b>((A - B) / (C * (D + E))) + F ^ (G - H)</b></p>""",
      a=r"""<p>Working bracket by bracket (innermost first):</p>
<p><code>(A-B)</code> → <code>AB-</code>; <code>(D+E)</code> → <code>DE+</code>; <code>C*(D+E)</code> → <code>CDE+*</code>;
<code>(A-B)/(C*(D+E))</code> → <code>AB-CDE+*/</code></p>
<p><code>(G-H)</code> → <code>GH-</code>; <code>F^(G-H)</code> → <code>FGH-^</code> (^ binds tighter than +)</p>
<p>Join with the last operator +:</p>
<p><span class="box">A B − C D E + * / F G H − ^ +</span></p>
<p>Stack trace (scan left to right):</p>""" + tbl(["Symbol", "Stack", "Postfix"],
                                                 [[s, st or "—", o] for s, st, o, _ in PF_STEPS]),
      topic="Data structures — infix to postfix conversion",
      recall=r"<ul><li>Precedence: ^ &gt; * / &gt; + −; ^ is right-associative.</li><li>Operands go straight to output; ')' pops to the matching '('.</li></ul>"),

    Q("2(ii)", 2, r"""<p>A matrix \(M[-7 \ldots 12,\ 3 \ldots 20]\) is stored in memory. Each element requires
<b>6 bytes</b> of storage. If the base address of \(M[-7][3]\) is <b>2013</b>, find the memory address of
\(M[5][10]\) when the matrix is stored <b>column-major</b>.</p>""",
      a=r"""<p>Rows \(L_r = -7\) to \(U_r = 12\): number of rows \(N_r = 12 - (-7) + 1 = 20\). Columns \(L_c = 3\) to 20.</p>
<p>Column-major: \(\text{Address}(M[i][j]) = B + W\,[(j - L_c)\,N_r + (i - L_r)]\)</p>
<p>\(= 2013 + 6\,[(10 - 3)\times 20 + (5 - (-7))]\)</p>
<p>\(= 2013 + 6\,[140 + 12] = 2013 + 6 \times 152 = 2013 + 912\)</p>
<p><span class="box">Address of M[5][10] = 2925</span></p>""",
      topic="Arrays — address calculation",
      recall=r"<ul><li>Column-major: \(B + W[(j-L_c)N_r + (i-L_r)]\); row-major: \(B + W[(i-L_r)N_c + (j-L_c)]\).</li><li>Count with \(U - L + 1\) when the lower bound is negative.</li></ul>"),

    Q("2(iii)(a)", 2, r"""<p>The following function findPos() is a part of a class. Assume arr[] is a sorted array of
positive integers. Answer the questions given below <b>along with dry run / working</b>.</p>""" + code(FINDPOS) +
      r"""<p>(a) Trace the recursive calls and find the output when arr[] = {3, 7, 12, 18, 25, 31, 42, 53} and x = 31.</p>""",
      a=r"""<p>Indices: 0:3, 1:7, 2:12, 3:18, 4:25, 5:31, 6:42, 7:53.</p>""" + tbl(
          ["Call", "f", "l", "m = (2f + l)/3", "arr[m]", "Action"],
          [["findPos(arr,0,7,31)", 0, 7, "7/3 = 2", 12, "12 &lt; 31 → k = findPos(arr,3,7,31)"],
           ["findPos(arr,3,7,31)", 3, 7, "13/3 = 4", 25, "25 &lt; 31 → k = findPos(arr,5,7,31)"],
           ["findPos(arr,5,7,31)", 5, 7, "17/3 = 5", 31, "found → return 5"]]) +
      r"""<p>Unwinding: the second call receives k = 5 → returns 5 + 1 = <b>6</b>; the first call receives k = 6 →
returns 6 + 1 = <b>7</b>.</p>
<p><span class="box">Output: 7</span></p>
<p class="note">31 is actually at index 5. The <code>k + 1</code> adds one for every move to the right part,
so the method does not return the true index — confirmed by running it.</p>""",
      topic="Recursion",
      recall=r"<ul><li>Dry-run recursion with a table of parameters per call, then unwind returns in reverse order.</li><li>Integer division truncates: 17/3 = 5.</li></ul>"),

    Q("2(iii)(b)", 1, r"""<p>(Refer to findPos() in 2(iii).)</p>""" + code(FINDPOS) +
      r"""<p>(b) What additional concept (apart from recursion) is used in the above function logic?</p>""",
      a=r"""<p><span class="box">Binary search (divide and conquer)</span> — searching a sorted array by comparing x with
one element and discarding the part that cannot contain it. Here the split point is the one-third point
\(m = (2f + l)/3\) instead of the middle, so it is a modified (ternary-split) binary search; naming binary search /
divide and conquer on a sorted array is what earns the mark.</p>""",
      topic="Recursion; Searching",
      recall=r"<ul><li>Binary search: compare with a middle element, discard the part that cannot hold the key (needs sorted data).</li><li>Divide and conquer: split, solve the part, combine.</li></ul>"),

    Q("2(iv)(a)", 1, TRIB_Q + r"<p>(a) What condition should replace <b>?1</b>?</p>",
      a=r"""<p>The 0th term is 0: <span class="box">?1 : n == 0</span></p>
<p class="note">If the terms are counted from n = 1 (first term 0), the answers shift by one: n == 1, then
n == 2 || n == 3.</p>""" + jcode(M, "Part1.java") +
      r"<p>Run for n = 0 … 7 gives <code>0 1 1 2 4 7 13 24</code>, the given series.</p>",
      topic="Recursion", recall=TRIB_RECALL),

    Q("2(iv)(b)", 1, TRIB_Q + r"<p>(b) What condition should replace <b>?2</b>?</p>",
      a=r"""<p>The 1st and 2nd terms are both 1: <span class="box">?2 : n == 1 || n == 2</span></p>""",
      topic="Recursion", recall=TRIB_RECALL),

    Q("2(iv)(c)", 1, TRIB_Q + r"<p>(c) What recursive call or expression should replace <b>?3</b>?</p>",
      a=r"""<p>Each term is the sum of the previous <b>three</b>: <span class="box">?3 : tribonacci(n - 3)</span></p>""",
      topic="Recursion", recall=TRIB_RECALL),

    # one heading: the kit shows only the last of two consecutive SECs
    SEC("Part II – 50 Marks · Section A", "Answer <b>six</b> questions in Part II, choosing <b>two</b> questions "
        "from Section A, <b>two</b> from Section B and <b>two</b> from Section C. Section A: answer <b>any two</b> "
        "questions."),

    Q("3(i)", 5, Q3_TEXT + r"""<p>Draw the truth table for the inputs and outputs given above and write the POS
expression for X(M,L,T,S).</p>""",
      a=r"""<p>From the three conditions: \(X = M'L + MLT' + M'L'S\), i.e. X = 1 in rows
\(M'L\): 4, 5, 6, 7; \(MLT'\): 12, 13; \(M'L'S\): 1, 3. X = 0 in every other row.</p>
{{fig:0}}
<p>POS (product of the maxterms of the rows where X = 0):</p>
<p>\(X(M,L,T,S) = (M+L+T+S)(M+L+T'+S)(M'+L+T+S)(M'+L+T+S')(M'+L+T'+S)(M'+L+T'+S')(M'+L'+T'+S)(M'+L'+T'+S')\)</p>
<p><span class="box">\(X(M,L,T,S) = \pi(0, 2, 8, 9, 10, 11, 14, 15)\)</span></p>""",
      afig=[(F.fig_q3_truth, "Truth table; shaded rows (X = 0) give the maxterms")],
      topic="Boolean Algebra — truth tables, canonical POS",
      recall=r"<ul><li>Translate each condition into a product term; X is their sum.</li><li>Maxterm: 0 bit → variable, 1 bit → complement; POS = product over rows with X = 0.</li></ul>"),

    Q("3(ii)", 5, r"""<p>Reduce the above expression X(M,L,T,S) by using 4-variable Karnaugh map, showing the various
groups (i.e. octal, quads and pairs).</p>
<p>Draw the logic gate diagram for the reduced expression. Assume that the variables and their complements are
available as inputs.</p>
<p class="note">[“The above expression” is the POS expression of 3(i): \(X = \pi(0, 2, 8, 9, 10, 11, 14, 15)\).]</p>""",
      a=r"""<p>Place 0s in cells 0, 2, 8, 9, 10, 11, 14, 15 (rows M L in Gray order, columns T S in Gray order) and group
the 0s:</p>
{{fig:0}}
<div class="tbl"><table><tr><th>Group</th><th>Cells</th><th>Sum term</th></tr>
<tr><td>Quad 1 (four corners)</td><td>0, 2, 8, 10</td><td>\(L + S\)</td></tr>
<tr><td>Quad 2 (row M=1, L=0)</td><td>8, 9, 10, 11</td><td>\(M' + L\)</td></tr>
<tr><td>Quad 3 (M=1, T=1)</td><td>10, 11, 14, 15</td><td>\(M' + T'\)</td></tr></table></div>
<p>No octet is possible; all eight 0s are covered by the three quads.</p>
<p><span class="box">\(X = (L + S)\cdot(M' + L)\cdot(M' + T')\)</span></p>
<p>Logic gate diagram (three OR gates feeding one AND gate):</p>
{{fig:1}}""",
      afig=[(F.fig_q3_kmap, "K-map of the 0s (POS)"), (F.fig_q3_circuit, "X = (L+S)(M′+L)(M′+T′)")],
      topic="Boolean Algebra — Karnaugh maps",
      recall=r"<ul><li>POS K-map: group the 0s; a variable constant at 0 in the group appears plain, at 1 complemented.</li><li>Corners are adjacent (wrap-around).</li><li>Use the largest groups and the fewest of them.</li></ul>"),

    Q("4(i)(a)", 4, Q4_F + r"""<p>(a) Reduce the above expression by using 4-variable Karnaugh map, showing the various groups.</p>""",
      a=r"""<p>Maxterms: \(A+B+C+D = M_0\), \(A+B+C+D' = M_1\), \(A+B+C'+D' = M_3\), \(A+B+C'+D = M_2\),
\(A+B'+C+D' = M_5\), \(A+B'+C'+D' = M_7\), \(A'+B+C+D = M_8\), \(A'+B+C'+D = M_{10}\).</p>
<p>\(F = \pi(0, 1, 2, 3, 5, 7, 8, 10)\)</p>
{{fig:0}}
<div class="tbl"><table><tr><th>Group</th><th>Cells</th><th>Sum term</th></tr>
<tr><td>Quad 1 (four corners)</td><td>0, 2, 8, 10</td><td>\(B + D\)</td></tr>
<tr><td>Quad 2 (A = 0, D = 1)</td><td>1, 3, 5, 7</td><td>\(A + D'\)</td></tr></table></div>
<p>The quad 0, 1, 2, 3 is <b>redundant</b>: its cells are already in the two quads above.</p>
<p><span class="box">\(F = (B + D)\cdot(A + D')\)</span></p>""",
      afig=[(F.fig_q4i_kmap, "K-map of F (0s grouped)")],
      topic="Boolean Algebra — Karnaugh maps",
      recall=r"<ul><li>Each sum term with all four literals is one maxterm; write its number from the bits (plain = 0, complement = 1).</li><li>Drop any group whose cells are all covered by other groups.</li></ul>"),

    Q("4(i)(b)", 1, Q4_F + r"""<p>(b) Draw the logic gate diagram for the reduced expression. Assume that the variables and their
complements are available as inputs.</p>""",
      a=r"""<p>Reduced expression from 4(i)(a): \(F = (B + D)(A + D')\) — two OR gates feeding a 2-input AND gate.</p>""",
      afig=[(F.fig_q4i_circuit, "F = (B+D)(A+D′)")],
      topic="Boolean Algebra — logic gates",
      recall=r"<ul><li>POS → OR gates for the sum terms, then one AND gate.</li></ul>"),

    Q("4(ii)(a)", 4, r"""<p>(a) From the logic circuit diagram given below, name the outputs (1), (2) and (3) and finally
derive the Boolean expression (F) and simplify it. State whether it is a tautology, contradiction or
contingency.</p>""",
      qfig=F.fig_q4ii_circuit,
      a=r"""<p>(1) = OR of X and Y′: \(X + Y'\)<br>(2) = AND of X and Z: \(X\cdot Z\)<br>
(3) = AND of (1) and (2): \((X + Y')\cdot XZ\)</p>
<p>\(F = (X + Y')XZ + Z'\)</p>
<p>\(= XXZ + XY'Z + Z'\) &nbsp; (distributive)</p>
<p>\(= XZ + XY'Z + Z'\) &nbsp; (idempotence \(XX = X\))</p>
<p>\(= XZ(1 + Y') + Z' = XZ + Z'\) &nbsp; (absorption)</p>
<p>\(= (X + Z')(Z + Z') = X + Z'\) &nbsp; (distributive; \(Z + Z' = 1\))</p>
<p><span class="box">\(F = X + Z'\)</span></p>
<p>F is 0 when X = 0, Z = 1 and 1 otherwise — it is neither always 1 nor always 0, so F is a
<span class="box">contingency</span>.</p>""",
      topic="Boolean Algebra — logic circuits; Propositional logic",
      recall=r"<ul><li>Write each gate's output from its inputs, left to right.</li><li>\(A + A'B = A + B\); \(A(1 + B) = A\).</li><li>Tautology: always 1; contradiction: always 0; contingency: both occur.</li></ul>"),

    Q("4(ii)(b)", 1, r"<p>(b) Write the dual of the expression \((A'+1)\cdot B\)</p>",
      a=r"""<p>Dual: interchange + and ·, and 0 and 1 (variables and complements unchanged).</p>
<p><span class="box">\((A'\cdot 0) + B\)</span> &nbsp; (which simplifies to B, as does the original).</p>""",
      topic="Boolean Algebra — duality",
      recall=r"<ul><li>Duality: + ↔ ·, 0 ↔ 1; do not complement the variables.</li></ul>"),

    Q("5(i)", 5, r"""<p>Draw the logic circuit to decode the following binary number (0001, 0101, 0111, 1000, 1010, 1100,
1110, 1111) to its hexadecimal equivalents. Also state the Hexadecimal equivalents of the given binary numbers.</p>""",
      a=r"""<div class="tbl"><table><tr><th>Binary ABCD</th><th>Minterm</th><th>Hex</th></tr>
<tr><td>0001</td><td>\(A'B'C'D\)</td><td>1</td></tr><tr><td>0101</td><td>\(A'BC'D\)</td><td>5</td></tr>
<tr><td>0111</td><td>\(A'BCD\)</td><td>7</td></tr><tr><td>1000</td><td>\(AB'C'D'\)</td><td>8</td></tr>
<tr><td>1010</td><td>\(AB'CD'\)</td><td>A</td></tr><tr><td>1100</td><td>\(ABC'D'\)</td><td>C</td></tr>
<tr><td>1110</td><td>\(ABCD'\)</td><td>E</td></tr><tr><td>1111</td><td>\(ABCD\)</td><td>F</td></tr></table></div>
<p>Each output is a 4-input AND gate of its minterm: a 1 bit takes the variable, a 0 bit its complement (from
the NOT gates). Exactly one output is high for each listed input.</p>
{{fig:0}}""",
      afig=[(F.fig_q5i_decoder, "Decoder: A, B, C, D and their complements; one AND gate per code")],
      topic="Elementary digital electronics — decoders",
      recall=r"<ul><li>Decoder: n inputs, one AND gate per output, each gate = the minterm of its code.</li><li>Hex digits: 10–15 = A–F.</li></ul>"),

    Q("5(ii)", 3, Q5II_Q, qfig=F.fig_q5ii_circuit,
      a=r"""<p>Output of the AND gate: \(A\cdot B'\). The NOR gate: \(F4 = (A' + AB')'\).</p>""" + tbl(
          ["A", "B", "A′", "B′", "A·B′", "A′ + A·B′", "F4 = (A′ + A·B′)′"],
          [[0, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0, "<b>1</b>"]]) +
      r"""<p>F4 = 1 when A = 1, B = 1, so it is not always 0. (Algebraically \(A' + AB' = A' + B'\), so
\(F4 = (A' + B')' = AB\).)</p>
<p><span class="box">False — F4 = AB is a contingency, not a contradiction.</span></p>""",
      topic="Boolean Algebra — logic circuits; Propositional logic",
      recall=r"<ul><li>NOR output = complement of the OR of its inputs.</li><li>Contradiction: 0 in every row of the truth table.</li><li>\(A' + AB' = A' + B'\) (redundant literal); De Morgan \((A'+B')' = AB\).</li></ul>"),

    Q("5(iii)", 2, r"""<p>Represent the given expression in canonical and cardinal POS form.</p>
<p>\(H5 = p\cdot q\cdot r' + p'\cdot q\cdot r' + p\cdot q'\cdot r + p'\cdot q\cdot r\)</p>""",
      a=r"""<p>Minterms present: \(pqr' = 110 = 6\), \(p'qr' = 010 = 2\), \(pq'r = 101 = 5\), \(p'qr = 011 = 3\):
\(H5 = \Sigma(2, 3, 5, 6)\). The remaining rows 0, 1, 4, 7 are the maxterms.</p>
<p>Canonical POS: <span class="box">\(H5 = (p + q + r)(p + q + r')(p' + q + r)(p' + q' + r')\)</span></p>
<p>Cardinal POS: <span class="box">\(H5 = \pi(0, 1, 4, 7)\)</span></p>""",
      topic="Boolean Algebra — canonical and cardinal forms",
      recall=r"<ul><li>POS rows = rows missing from the SOP list.</li><li>Maxterm: 0 → plain variable, 1 → complemented.</li></ul>"),

    SEC("Section B", "Answer <b>any two</b> questions. Each program should be written in such a way that it "
        "clearly depicts the logic of the problem. This can be achieved by using mnemonic names and comments "
        "in the program. (Flowcharts and Algorithms are not required.) The programs must be written in Java."),

    Q("6", 10, r"""<p>Two words are called anagram of each other if both the words contain the same letters but they
are arranged in different order. Following are the three pairs of the words which are anagrams of each other.</p>
<p style="text-align:center">cat, act &nbsp;&nbsp; heart, earth &nbsp;&nbsp; silent, listen</p>
<p>Design the class Anagram to input two words in lower case and check if they are anagram of each other. The
member functions and data members of the class are given below:</p>
<div class="tbl"><table>
<tr><td>Class Name</td><td>Anagram</td></tr>
<tr><th colspan="2">Data members / instance variables</th></tr>
<tr><td>s1, s2</td><td>stores the two words in lower case</td></tr>
<tr><td>l1, l2</td><td>number of character in s1 and s2 respectively</td></tr>
<tr><th colspan="2">Member functions</th></tr>
<tr><td>Anagram(String s1, String s2)</td><td>parameterised constructor to assign the accepted values of s1 and s2 to data member</td></tr>
<tr><td>void sort(char c[])</td><td>to sort the characters in array c[] in ascending order using any sorting technique</td></tr>
<tr><td>boolean areAnagram(char[] str1, char[] str2)</td><td>to check if str1 and str2 are anagrams of each other and to return true or false accordingly</td></tr>
<tr><td>void check()</td><td>to convert the two strings into two character arrays and to display the appropriate message as shown in the sample output by calling the method areAnagram(char[] str1, char[] str2)</td></tr>
</table></div>
<p>Specify the class Anagram giving details of the parameterised constructor, void sort(char c[]), boolean
areAnagram(char[] str1, char[] str2) and void check(). Create one object in the main() method and call all the
methods appropriately.</p>
<p>Sample Input:<br>Enter first word -&gt; earth<br>Enter second word -&gt; heart</p>
<p>Output:<br>earth and heart are anagram of each other</p>""",
      a=r"""<p><b>Idea:</b> two words are anagrams exactly when their letters, sorted, give the same sequence. Equal
lengths are checked first; then both arrays are sorted (bubble sort) and compared position by position.</p>"""
      + jcode(M, "Anagram.java") + jout(M, "anagram1") + jout(M, "anagram2"),
      topic="Strings; Arrays — sorting",
      recall=r"<ul><li><code>toCharArray()</code> converts a String to char[].</li><li>Bubble sort: compare neighbours, swap if out of order, n − 1 passes.</li><li>Anagram test: equal length and equal sorted letters.</li></ul>"),

    Q("7", 10, r"""<p>A sports academy wants to conduct a friendly match between two teams with maximum fifteen players.
A class Sports contains three data members, to store the name of the team with ‘n’ number of players and a
one-dimensional array to store height of each player. Design a class Sports to compare average height of both
the teams. The details of the members of the class are given below:</p>
<div class="tbl"><table>
<tr><td>Class Name</td><td>Sports</td></tr>
<tr><th colspan="2">Data Members / Instance Variables</th></tr>
<tr><td>height[]</td><td>to store the height of each player</td></tr>
<tr><td>name</td><td>to store the name of the team</td></tr>
<tr><td>n</td><td>to store total number of players</td></tr>
<tr><th colspan="2">Member methods</th></tr>
<tr><td>Sports()</td><td>default constructor</td></tr>
<tr><td>Sports(int n, String name)</td><td>to initialize the number of players and name of the team</td></tr>
<tr><td>void fillHeight()</td><td>to enter the height of all the players</td></tr>
<tr><td>double averageHeight</td><td>to calculate average height of the team</td></tr>
<tr><td>String compare(Sports s1, Sports s2)</td><td>to compare average height of both the teams and return the name of the team with the higher average height</td></tr>
<tr><td>void display(String msg)</td><td>to display the name of the team with the higher average height stored in msg. If both the teams have the same average height, then msg should be “Both teams have the same average height.”</td></tr>
</table></div>
<p>Specify the class Sports giving the details of constructors, void fillHeight(), double averageHeight(),
String compare(Sports, Sports), void display(String). Write the main() method to call methods defined in an
appropriate manner.</p>""",
      a=r"""<p><b>Idea:</b> each team is one Sports object. <code>compare()</code> is called on a third object (made
with the default constructor) and receives both teams; it returns the winning team's name, or the
“same average” message, which <code>display()</code> then prints. The parameterised constructor caps n at 15.</p>"""
      + jcode(M, "Sports.java") + jout(M, "sports1") + jout(M, "sports2"),
      topic="Objects — passing objects to methods; Arrays",
      recall=r"<ul><li>Objects can be passed as arguments; the method reads their members through the reference.</li><li>Average = sum / count (use double).</li><li>Constructors: default (no arguments) and parameterised.</li></ul>"),

    Q("8", 10, r"""<p>Given below is an example of a double dimensional array with unequal number of rows and columns.
It must be arranged in such a way that the elements in the even rows are in ascending order and the elements in
the odd rows are in descending order, using Insertion sort technique.</p>
<p>Sample Input :<br>Row = 3<br>Column = 4</p>
<p>Enter the array elements</p><pre class="code">1 2 3 4
9 8 7 6
4 5 6 7</pre>
<p>Before sort :</p><pre class="code">1 2 3 4
9 8 7 6
4 5 6 7</pre>
<p>After sort :</p><pre class="code">4 3 2 1
6 7 8 9
7 6 5 4</pre>
<p>The members of the class are given below :</p>
<div class="tbl"><table>
<tr><td>Class name</td><td>Mix_sort</td></tr>
<tr><th colspan="2">Data members / instance variables</th></tr>
<tr><td>a[][]</td><td>to store integers in the double dimensional array</td></tr>
<tr><td>m</td><td>to store the number of rows</td></tr>
<tr><td>n</td><td>to store the number of columns</td></tr>
<tr><th colspan="2">Methods / Member functions</th></tr>
<tr><td>Mix_sort(int row, int col)</td><td>parameterised constructor to initialise m = row, n = col and allocate memory for a[][]</td></tr>
<tr><td>void input()</td><td>to enter the integer elements in a[][]</td></tr>
<tr><td>void ascEven(int x[])</td><td>arrange the elements of x[] in ascending order using Insertion sort technique</td></tr>
<tr><td>void dscOdd(int x[])</td><td>arrange the elements of x[] in descending order using Insertion sort technique</td></tr>
<tr><td>void arrange()</td><td>to arrange the rows in even position in Ascending order using ascEven(..) method and rows in odd position in descending order using dscOdd(..) method. Finally store the sorted elements into a[][]</td></tr>
<tr><td>void display()</td><td>display the original a[][] and sorted a[][]</td></tr>
</table></div>
<p>Define the class <b>Mix_sort</b> with details of the constructor, void input(), void arrange(), void
ascEven(int []), void dscOdd(int []) and void display(). Define a main() function to create an object and call
the functions accordingly to enable the task.</p>""",
      a=r"""<p><b>Reading the sample:</b> the 1st and 3rd rows come out descending and the 2nd ascending, so “even” and
“odd” are row <i>positions counted from 1</i> (index 0 is position 1, odd). The program follows the sample.
An extra array <code>orig[][]</code> keeps the original matrix, because <code>display()</code> must print both.</p>
<p><b>Insertion sort:</b> take each element in turn as the key and shift the larger (for ascending) or smaller
(for descending) elements before it one place right, then drop the key into the gap.</p>"""
      + jcode(M, "Mix_sort.java") + jout(M, "mixsort") +
      r"<p>The output matches the sample in the question.</p>",
      topic="Arrays — double dimensional; Sorting (insertion)",
      recall=r"<ul><li>Insertion sort: <code>while (j &gt;= 0 &amp;&amp; x[j] &gt; key) { x[j+1] = x[j]; j--; } x[j+1] = key;</code> — flip &gt; to &lt; for descending.</li><li>Copy a row into a 1-D array, sort it, copy it back.</li></ul>"),

    SEC("Section C", "Answer <b>any two</b> questions. Each program should be written in such a way that it clearly "
        "depicts the logic of the problem stepwise. This can be achieved by using comments in the program and "
        "mnemonic names or pseudo codes for algorithms. The programs must be written in Java and the algorithms "
        "must be written in general / standard form, wherever required / specified. (Flowcharts are not required.)"),

    Q("9(a)", 3, Q9_CLASS + r"<p>(a) Write the member functions void pushValue(int) and int popValue().</p>",
      a=r"""<p>Insert at the rear (r moves forward), delete from the front (f moves forward). The structure is
empty when f &gt; r and full when r = cap − 1.</p>""" + jcode(M, "Repeat.java") +
      r"""{{fig:0}}<p>Test run (cap = 3): push 10, 20, 30, push 40, then four pops and a push 50:</p>"""
      + jout(M, "repeat"),
      afig=[(F.fig_q9_queue, "cap = 5 after pushValue(10), (20), (30) and one popValue(): f = 1, r = 2")],
      topic="Data structures — queue",
      recall=r"<ul><li>Linear queue: insert at rear (<code>st[++r] = v</code>), delete at front (<code>st[f++]</code>).</li><li>Overflow: r == cap − 1; underflow: f &gt; r.</li></ul>"),

    Q("9(b)", 1, Q9_CLASS + r"<p>(b) What is the common name of the entity described above?</p>",
      a=r"<p>Insertion at one end (rear) and deletion at the other (front): <span class='box'>a Queue</span> (linear queue).</p>",
      topic="Data structures — queue",
      recall=r"<ul><li>Stack: one end for both operations; queue: insert at rear, delete at front; dequeue: both ends.</li></ul>"),

    Q("9(c)", 1, Q9_CLASS + r"<p>(c) On what principle does this entity work?</p>",
      a=r"<p><span class='box'>FIFO — First In, First Out</span>: the element inserted first is the first to be removed.</p>",
      topic="Data structures — queue",
      recall=r"<ul><li>Queue: FIFO; stack: LIFO.</li></ul>"),

    Q("10", 5, r"""<p>A super class Circle has been defined to calculate the area of a circle. Define a subclass Volume to
calculate the volume of a cylinder. The details of the members of both the classes are given below:</p>
<div class="tbl"><table>
<tr><td>Class name</td><td>Circle</td></tr>
<tr><th colspan="2">Data members/instance variables</th></tr>
<tr><td>radius</td><td>to store the radius in decimals</td></tr>
<tr><td>area</td><td>to store the area of a circle</td></tr>
<tr><th colspan="2">Methods / Member functions</th></tr>
<tr><td>Circle( ... )</td><td>parameterized constructor to assign values to the data members</td></tr>
<tr><td>void cal_area()</td><td>calculates the area of a circle (πr<sup>2</sup>)</td></tr>
<tr><td>void display( )</td><td>to display the area of the circle</td></tr>
<tr><td>Class name</td><td>Volume</td></tr>
<tr><th colspan="2">Data members/instance variables</th></tr>
<tr><td>height</td><td>to store the height of the cylinder in decimals</td></tr>
<tr><td>volume</td><td>to store the volume of the cylinder in decimals</td></tr>
<tr><th colspan="2">Methods / Member functions</th></tr>
<tr><td>Volume( ... )</td><td>parameterized constructor to assign values to the data members of both the classes</td></tr>
<tr><td>double calculate()</td><td>to calculate and return the volume of the cylinder using the formula (πr<sup>2</sup>h) where, r is the radius and h is the height</td></tr>
<tr><td>void display( )</td><td>to display the area of a circle and volume of a cylinder.</td></tr>
</table></div>
<p>Assume that the super class Circle has been defined. Using the concept of inheritance, specify the class Volume
giving the details of the <b>constructor(...), double calculate() and void display().</b></p>
<p>The super class, main function and algorithm need NOT be written</p>""",
      a=r"""<p>The super class, as assumed (shown only so the answer can be read; <i>not part of the answer</i>):</p>
<pre class="code" style="border-style:dashed">class Circle
{
    double radius, area;
    Circle(double r)  { radius = r; area = 0.0; }
    void cal_area()   { area = Math.PI * radius * radius; }
    void display()    { System.out.println("Area of the circle = " + area); }
}</pre>
<p><b>Answer:</b></p>""" + jcode(M, "Volume.java") +
      r"""<p><code>display()</code> overrides the super-class method, so the super-class version is reached with
<code>super.display()</code>; <code>cal_area()</code> is called first, otherwise the area would print as 0.0.
Run with r = 7, h = 10:</p>""" + jout(M, "volume"),
      topic="Inheritance, Interfaces and Polymorphism",
      recall=r"<ul><li><code>super(…)</code> must be the first statement of the subclass constructor.</li><li>An overriding method calls the parent version with <code>super.method()</code>.</li><li>Cylinder volume \(= \pi r^2 h\) = base area × height.</li></ul>"),

    Q("11(i)", 2, r"""<p>A linked list is formed from the objects of the class</p>
<pre class="code">class Node
{
   int info;
   Node link;
}</pre>
<p>Write an <b>algorithm or a method</b> to <b>delete a node</b> from the linked list. The method declaration is
given below:</p><p><b>void deleteNode(Node start)</b></p>""",
      a=r"""<p>The node to delete is taken to be the one whose <code>info</code> equals a value read from the user.</p>
<p><b>Algorithm</b></p>
<ol><li>Read val. If start = null, print “List is empty” and stop.</li>
<li>If start.info = val: if start.link = null (the only node) the list becomes empty — the caller sets
start = null; otherwise copy start.link's info into start and set start.link = start.link.link
(start itself cannot be re-pointed inside the method, as Java passes the reference by value). Stop.</li>
<li>Set prev = start, ptr = start.link.</li>
<li>While ptr ≠ null and ptr.info ≠ val: prev = ptr, ptr = ptr.link.</li>
<li>If ptr = null, print “not found”; else set prev.link = ptr.link. Stop.</li></ol>
{{fig:0}}
<p><b>Method</b></p>""" + jcode(M, "DeleteNode.java") +
      r"""<p class="note">In algorithm form ISC answers often write “start = start.link” for the first node; that is the
right idea and earns the step, but inside a <code>void</code> method taking <code>start</code> as a parameter it would
change only the local copy, which is why the method above copies the second node forward instead.</p>
<p>Run on 10 → 20 → 30 → 40 deleting 30, 10, 40 and 99 in turn (each on a fresh list), then on a one-node list:</p>"""
      + jout(M, "delete"),
      afig=[(F.fig_q11i_delete, "Deleting a middle node: prev.link = ptr.link")],
      topic="Data structures — linked list",
      recall=r"<ul><li>To delete, keep a pointer to the node <i>before</i> the one removed and bypass it.</li><li>Handle the empty list and the first node separately.</li><li>Traversal: <code>ptr = ptr.link</code> until null.</li></ul>"),

    Q("11(ii)(a)", 1, Q11T + r"<p>(a) Name the root of the left sub tree and its siblings</p>"
      r"<p class='note'>[The paper numbers this part “(i)” a second time; it is 11(ii).]</p>",
      qfig=TREE_Q,
      a=r"""<p>The left sub-tree of A is rooted at <span class="box">B</span>; its sibling (the other child of A) is
<span class="box">C</span>.</p>""",
      topic="Data structures — binary trees", recall=TREE_RECALL),

    Q("11(ii)(b)", 1, Q11T + r"<p>(b) State the size and depth of the right sub tree.</p>", qfig=TREE_Q,
      a=r"""<p>Right sub-tree = C with children F and G.</p>
<p><span class="box">Size = 3</span> (nodes C, F, G); <span class="box">Depth = 1</span> (one edge from C to a
leaf, the sub-tree's root C taken at level 0 — the convention of CISCE's own key for this question type in the
2025 specimen paper; counted in levels from 1 it would be 2).</p>""",
      topic="Data structures — binary trees", recall=TREE_RECALL),

    Q("11(ii)(c)", 1, Q11T + r"<p>(c) Write the in-order traversal of the above tree structure</p>", qfig=TREE_Q,
      a=r"""<p>In-order (Left, Root, Right): left sub-tree of A → H D I B E J (E has only a right child J, so E
comes before J), then A, then the right sub-tree F C G.</p>
<p><span class="box">H, D, I, B, E, J, A, F, C, G</span></p>""",
      topic="Data structures — binary trees", recall=TREE_RECALL),
]

PAPER = dict(
    subject="computers",
    year="2025-26",
    slug="2025-26-group-4",
    paper="Paper 1 (Theory) — Group 4",
    source="PreBoard-PYQ/2025-26/SET-1/COMPUTER SCIENCE Group 4.pdf",
    marks=70, time="3 hours",
    intro=INTRO,
    items=ITEMS,
)
