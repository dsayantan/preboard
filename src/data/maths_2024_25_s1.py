"""Heritage School Pre-Board 2024-25 (Set 1), Mathematics (Class XII).  Transcribed from the page images."""
from kit import Q, SEC
import maths_2024_25_s1_figs as F

REGR = ("Correlation and regression ({}) — dropped from ISC Mathematics; not in any of the seven ISC 2027 "
        "Class XII units.")

AR = r"""<p>(a) Both Assertion and Reason are true, and Reason is the correct explanation for Assertion.<br>
(b) Both Assertion and Reason are true, but Reason is not the correct explanation of the Assertion.<br>
(c) Assertion is true, but Reason is false.<br>
(d) Assertion is false, but Reason is true.</p>"""

ST = r"""<p>Which of the following is correct?<br>
(a) Statement 1 is true, but Statement 2 is false.<br>
(b) Statement 1 is false, but Statement 2 is true.<br>
(c) Both the statements are true.<br>
(d) Both the statements are false.</p>"""

PAPER = dict(
    subject="maths",
    year="2024-25",
    slug="2024-25-set-1",
    paper="Set 1",
    source="PreBoard-PYQ/2024-25/SET-1/MATHEMATICS.pdf",
    marks=80, time="3 hours",
    intro=r"""<p>Reading Time: An additional fifteen minutes.</p>
<ul><li>You are allowed an additional 15 minutes for only reading the paper.</li>
<li>You must NOT start writing during reading time.</li>
<li>The question paper has 8 printed pages.</li>
<li>The Question Paper is divided into three sections and has 22 questions in all.</li>
<li>Section A is compulsory and has fourteen questions.</li>
<li>You are required to attempt all questions either from Section B or Section C.</li>
<li>Section B and Section C have four questions each.</li>
<li>Internal choices have been provided in two questions of 2 marks, two questions of 4 marks and two
questions of 6 marks in Section A.</li>
<li>Internal choices have been provided in one question of 2 marks and one question of 4 marks each in Section
B and Section C.</li>
<li>While attempting Multiple Choice Questions in Section A, B and C, you are required to write only ONE
option as the answer.</li>
<li>The intended marks for questions or parts of questions are given in the brackets [ ].</li>
<li>All workings, including rough work, should be done on the same page as, and adjacent to, the rest of the
answer.</li>
<li>Mathematical tables and graph papers are provided.</li></ul>
<p class="note">In the ISC 2027 pattern there is no longer a choice between Sections B and C: Vectors and
3-D Geometry (this paper's Section B) and Linear Programming are compulsory. Of Section C, the items whose
mathematics is differentiation (MC = AC, maximum profit, maximum revenue) or solving a given revenue–cost equation
(break-even) are answered under Applications of Derivatives; the regression items have left the syllabus.</p>""",
    items=[
        SEC("Section A – 65 Marks",
            "Question 1 [15 × 1 = 15]. In subparts (i) to (x) choose the correct options and in subparts (xi) to (xv), "
            "answer the questions as instructed."),

        # ---------------------------------------------------------------- Question 1
        Q("1(i)", 1, r"""<p>If \(A=\begin{bmatrix}2&1\\7&5\end{bmatrix}\) then \(|A\,\operatorname{adj}A|\) is equal to:</p>
<p>(a) 3 &emsp; (b) 9 &emsp; (c) 27 &emsp; (d) 81</p>""",
          a=r"""<p>\(|A|=2(5)-1(7)=3\).</p>
<p>\(A(\operatorname{adj}A)=|A|\,I_2\), so \(|A\,\operatorname{adj}A|=\big||A|I_2\big|=|A|^2=3^2=9\).</p>
<p><span class="box">(b) 9</span></p>""",
          topic="Determinants",
          recall=r"""<ul><li>\(A(\operatorname{adj}A)=(\operatorname{adj}A)A=|A|I\).</li>
<li>\(|kI_n|=k^n\); hence \(|A\,\operatorname{adj}A|=|A|^n\) for order \(n\).</li></ul>"""),

        Q("1(ii)", 1, r"""<p>\(\displaystyle\int_0^{\pi/2}\sin2x\,\log(\tan x)\,dx\) is equal to:</p>
<p>(a) \(\pi\) &emsp; (b) \(\dfrac\pi2\) &emsp; (c) 0 &emsp; (d) \(2\pi\)</p>""",
          a=r"""<p>Let \(I=\displaystyle\int_0^{\pi/2}\sin2x\log(\tan x)\,dx\). Using \(\int_0^af(x)\,dx=\int_0^af(a-x)\,dx\):
\(\sin2(\tfrac\pi2-x)=\sin2x\) and \(\tan(\tfrac\pi2-x)=\cot x\), so</p>
<p>\(I=\displaystyle\int_0^{\pi/2}\sin2x\log(\cot x)\,dx=-\int_0^{\pi/2}\sin2x\log(\tan x)\,dx=-I\Rightarrow 2I=0\).</p>
<p><span class="box">(c) 0</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int_0^af(x)\,dx=\int_0^af(a-x)\,dx\).</li>
<li>\(\log\cot x=-\log\tan x\).</li></ul>"""),

        Q("1(iii)", 1, r"""<p>If \(f(x)=e^{\cos^{-1}\left(\sin\left(x+\frac\pi3\right)\right)}\) then \(f\left(\dfrac{8\pi}{9}\right)\) is equal to:</p>
<p>(a) \(e^{5\pi/18}\) &emsp; (b) \(e^{13\pi/18}\) &emsp; (c) \(e^{-5\pi/18}\) &emsp; (d) \(e^{-13\pi/18}\)</p>""",
          a=r"""<p>\(x+\dfrac\pi3=\dfrac{8\pi}9+\dfrac{3\pi}9=\dfrac{11\pi}9\), and \(\sin\dfrac{11\pi}9=-\sin\dfrac{2\pi}9=-\cos\left(\dfrac\pi2-\dfrac{2\pi}9\right)=-\cos\dfrac{5\pi}{18}\).</p>
<p>\(\cos^{-1}(-t)=\pi-\cos^{-1}t\), and \(\tfrac{5\pi}{18}\in[0,\pi]\): \(\cos^{-1}\left(-\cos\dfrac{5\pi}{18}\right)=\pi-\dfrac{5\pi}{18}=\dfrac{13\pi}{18}\).</p>
<p>\(f\left(\dfrac{8\pi}9\right)=e^{13\pi/18}\). <span class="box">(b)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>Principal range of \(\cos^{-1}\) is \([0,\pi]\); \(\cos^{-1}(\cos\theta)=\theta\) only for \(\theta\in[0,\pi]\).</li>
<li>\(\cos^{-1}(-x)=\pi-\cos^{-1}x\).</li></ul>"""),

        Q("1(iv)", 1, r"""<p><b>Assertion:</b> Degree of the differential equation \(\left\{1+\left(\dfrac{dy}{dx}\right)^2\right\}^{3/2}=\dfrac{d^2y}{dx^2}\) is not defined.<br>
<b>Reason:</b> If each term involving derivatives of the differential equation is a polynomial or can be expressed as a
polynomial then the highest exponent of the highest order derivative is known as degree of the differential equation.
Hence, or otherwise, the degree of the differential equation is not defined.</p>""" + AR,
          a=r"""<p>Squaring both sides makes the equation a polynomial in the derivatives:
\(\left\{1+\left(\dfrac{dy}{dx}\right)^2\right\}^{3}=\left(\dfrac{d^2y}{dx^2}\right)^2\).
Highest order derivative \(\dfrac{d^2y}{dx^2}\) occurs with power 2, so the order is 2 and the <b>degree is 2</b> — it is defined.
The Assertion is false.</p>
<p>The Reason states the definition of degree correctly (it is that definition which gives degree 2).</p>
<p><span class="box">(d)</span></p>
<p class="note">The last sentence of the printed Reason (“Hence … not defined”) contradicts its own definition; the
Reason is judged on the definition it states, which is true. Degree is undefined only when a derivative sits inside a
non-polynomial function such as \(\sin\left(\frac{dy}{dx}\right)\) or \(e^{y'}\).</p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Clear fractional powers of derivatives (raise both sides to a power) before reading the degree.</li>
<li>Degree is not defined when a derivative appears inside sin, log, exp, etc.</li></ul>"""),

        Q("1(v)", 1, r"""<p>A bag contains 19 tickets, numbered 1 to 19. Two tickets are drawn randomly in succession with replacement.
The probability that both the tickets are drawn are prime numbers are:</p>
<p>(a) \(\dfrac{81}{361}\) &emsp; (b) \(\dfrac{64}{361}\) &emsp; (c) \(\dfrac{121}{361}\) &emsp; (d) \(\dfrac{100}{361}\)</p>""",
          a=r"""<p>Primes from 1 to 19: 2, 3, 5, 7, 11, 13, 17, 19 — eight of them. With replacement the draws are independent:</p>
<p>\(P=\dfrac8{19}\times\dfrac8{19}=\dfrac{64}{361}\). <span class="box">(b)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>With replacement: draws are independent, \(P(A\cap B)=P(A)P(B)\).</li>
<li>1 is not a prime.</li></ul>"""),

        Q("1(vi)", 1, r"""<p>If \(f(x)=\begin{vmatrix}0&x-23&x-29\\x+23&0&x-31\\x+29&x+31&0\end{vmatrix}\) then \(f(0)\) is:</p>
<p>(a) 83 &emsp; (b) 1 &emsp; (c) 20677 &emsp; (d) 0</p>""",
          a=r"""<p>\(f(0)=\begin{vmatrix}0&-23&-29\\23&0&-31\\29&31&0\end{vmatrix}\). This matrix is skew-symmetric (\(a_{ji}=-a_{ij}\), zero diagonal) of odd order 3.</p>
<p>\(|A|=|A'|=|-A|=(-1)^3|A|=-|A|\Rightarrow|A|=0\).</p>
<p><span class="box">(d) 0</span></p>""",
          topic="Determinants",
          recall=r"""<ul><li>A skew-symmetric determinant of odd order is zero.</li>
<li>\(|kA|=k^n|A|\) and \(|A'|=|A|\).</li></ul>"""),

        Q("1(vii)", 1, r"""<p>The adjacent figure represents a graph of a real valued function. Which of the following is <b>not</b> true about the function.</p>
{{fig:0}}
<p>(a) The function is neither Injective nor Surjective.<br>
(b) The function possesses a local Minima at \(x=0\) but not differentiable at \(x=0\)<br>
(c) The function is continuous at \(x=0\) but not differentiable at \(x=0\).<br>
(d) The function possesses a stationary point at \(x=0\).</p>""",
          qfig=F.fig_q1vii_graph,
          a=r"""<p>The graph is \(f(x)=|x|\) (it passes through (±1, 1), (±2, 2) and (0, 0)).</p>
<p>(a) \(f(-1)=f(1)\): not one-one; the range \([0,\infty)\ne\mathbb R\): not onto. True.<br>
(b) \(f(0)=0\le f(x)\) near 0: local minimum; \(Lf'(0)=-1\ne Rf'(0)=1\): not differentiable. True.<br>
(c) \(\lim_{x\to0}|x|=0=f(0)\): continuous; not differentiable as in (b). True.<br>
(d) A stationary point needs \(f'(0)=0\); here \(f'(0)\) does not exist. <b>Not true.</b></p>
<p><span class="box">(d)</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Stationary point: \(f'(c)=0\) (the derivative must exist).</li>
<li>A corner (unequal left and right derivatives) can still be a local extremum — a critical point, not a stationary one.</li></ul>"""),

        Q("1(viii)", 1, r"""<p>If \(y=\log\sqrt{\tan x}\) then the value of \(\dfrac{dy}{dx}\) at \(x=\dfrac\pi4\) is given by</p>
<p>(a) \(\infty\) &emsp; (b) 1 &emsp; (c) 0 &emsp; (d) \(\dfrac12\)</p>""",
          a=r"""<p>\(y=\tfrac12\log\tan x\Rightarrow\dfrac{dy}{dx}=\dfrac12\cdot\dfrac{\sec^2x}{\tan x}=\dfrac{1}{2\sin x\cos x}=\dfrac1{\sin2x}\).</p>
<p>At \(x=\tfrac\pi4\): \(\dfrac{1}{\sin(\pi/2)}=1\). <span class="box">(b) 1</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>\(\log\sqrt u=\tfrac12\log u\).</li>
<li>\(\frac{d}{dx}\log\tan x=\frac{\sec^2x}{\tan x}=2\operatorname{cosec}2x\).</li></ul>"""),

        Q("1(ix)", 1, r"""<p><b>Statement 1:</b> If a function \(f:\{\alpha,\beta,\gamma,\delta\}\to\{\sigma,\tau\}\) then total number of possible surjections are 14.<br>
<b>Statement 2:</b> If a Relation \(R:\{\alpha,\beta,\gamma,\delta\}\to\{\alpha,\beta,\gamma,\delta\}\) then total number of possible reflexive relation is \(2^{12}\).</p>""" + ST,
          a=r"""<p>Statement 1: all functions from a 4-set to a 2-set: \(2^4=16\); the two constant functions are not onto, so onto functions \(=16-2=14\). True.</p>
<p>Statement 2: a relation on a set of \(n=4\) elements is a subset of the \(16\) ordered pairs. A reflexive relation must contain the 4 pairs \((a,a)\);
each of the other \(16-4=12\) pairs may be in or out: \(2^{12}\) reflexive relations. True.</p>
<p><span class="box">(c)</span></p>""",
          topic="Relations and Functions",
          recall=r"""<ul><li>Onto maps from an \(m\)-set to a 2-set: \(2^m-2\).</li>
<li>Reflexive relations on an \(n\)-set: \(2^{n^2-n}\).</li></ul>"""),

        Q("1(x)", 1, r"""<p><b>Assertion:</b> If \(|A|=-2\), then \(|-2A^{-1}|=4\) where A is a square matrix of order 3.<br>
<b>Reason:</b> In a square matrix of order \(n\) and for a scaler \(k\), \(|kA|=k^n|A|\) and \(|A^{-1}|=|A|^{-1}\)</p>
<p>(a) Both Assertion and Reason are true, and Reason is the correct explanation for Assertion.<br>
(b) Both Assertion and Reason are true, but Reason is the incorrect explanation for Assertion.<br>
(c) Assertion is true, and Reason is false.<br>
(d) Assertion is false, and Reason is true.</p>""",
          a=r"""<p>Using R: \(|-2A^{-1}|=(-2)^3|A^{-1}|=-8\cdot\dfrac{1}{|A|}=-8\cdot\left(-\dfrac12\right)=4\). A is true; R is true and is exactly the working.</p>
<p><span class="box">(a)</span></p>""",
          topic="Determinants",
          recall=r"""<ul><li>\(|kA|=k^n|A|\) (order \(n\)), \(|A^{-1}|=\dfrac1{|A|}\).</li></ul>"""),

        Q("1(xi)", 1, r"""<p>If A and B are independent events associated with a random experiment with sample space \(S\) such that
\(P(A\cup\bar B)=0.8\) and \(P(A)=0.3\) then find \(P(B)\).</p>""",
          a=r"""<p>A, B independent \(\Rightarrow\) A and \(\bar B\) independent. Let \(P(B)=p\), \(P(\bar B)=1-p\).</p>
<p>\(P(A\cup\bar B)=P(A)+P(\bar B)-P(A)P(\bar B)=0.3+0.7(1-p)=0.8\Rightarrow1-p=\dfrac57\).</p>
<p><span class="box">\(P(B)=\dfrac27\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>If A, B are independent, so are A and \(\bar B\).</li>
<li>\(P(A\cup B)=P(A)+P(B)-P(A\cap B)\).</li></ul>"""),

        Q("1(xii)", 1, r"""<p>If \(\begin{pmatrix}1&3&9\\1&x&x^2\\4&6&9\end{pmatrix}\) is a singular matrix then find the value(s) of \(x\).</p>""",
          a=r"""<p>Singular \(\Rightarrow\) determinant \(=0\):</p>
<p>\(1(9x-6x^2)-3(9-4x^2)+9(6-4x)=6x^2-27x+27=3(2x-3)(x-3)=0\).</p>
<p><span class="box">\(x=3\) or \(x=\dfrac32\)</span></p>
<p>(Check: \(x=3\) makes \(R_2=R_1\); \(x=\tfrac32\) makes \(R_2=\tfrac14R_3\).)</p>""",
          topic="Determinants",
          recall=r"""<ul><li>Singular matrix: \(|A|=0\).</li>
<li>Two proportional rows make a determinant zero — a quick check of the roots.</li></ul>"""),

        Q("1(xiii)", 1, r"""<p>If \(R\) is a relation on set \(A=\{a,b,c\}\) represented as \(R:A\to A\) defined as \(R=\{(b,c)\}\) then classify the relation on set \(A\).</p>""",
          a=r"""<p>Reflexive? \((a,a)\notin R\): <b>not reflexive</b>.<br>
Symmetric? \((b,c)\in R\) but \((c,b)\notin R\): <b>not symmetric</b>.<br>
Transitive? There is no pair \((b,c),(c,z)\) in R, so the condition is never violated: <b>transitive</b> (vacuously).</p>
<p><span class="box">R is transitive, but neither reflexive nor symmetric (so not an equivalence relation).</span></p>""",
          topic="Relations and Functions",
          recall=r"""<ul><li>Transitive: \((a,b),(b,c)\in R\Rightarrow(a,c)\in R\); with no such chain it holds vacuously.</li></ul>"""),

        Q("1(xiv)", 1, r"""{{fig:0}}
<p>Which of the above the graph does not represent a real valued function. Sketch the graph and confirm the result.</p>""",
          qfig=(F.fig_q1xiv_graphs, "The four printed graphs (numbered here (1)–(4) for reference)."),
          a=r"""<p>Vertical-line test: a curve is the graph of a function of \(x\) only if every vertical line meets it at most once
(each \(x\) has exactly one image).</p>
{{fig:0}}
<p>In graph (3) the vertical line \(x=k\) cuts the curve at three points, so one \(x\) would have three values of \(f(x)\).
Graphs (1), (2), (4) pass the test.</p>
<p><span class="box">Graph (3), the sideways S-shaped curve, is not a function.</span></p>""",
          afig=[(F.fig_q1xiv_ans, "The vertical line x = k meets graph (3) three times.")],
          topic="Relations and Functions",
          recall=r"""<ul><li>Vertical-line test → is it a function?</li>
<li>Horizontal-line test → is the function one-one?</li></ul>"""),

        Q("1(xv)", 1, r"""<p>A flashlight has 8 batteries out of which 3 are dead. If two batteries are selected without replacement and tested,
then find the probability that both the batteries are dead.</p>""",
          a=r"""<p>\(P(\text{both dead})=P(1\text{st dead})\,P(2\text{nd dead}\mid1\text{st dead})=\dfrac38\times\dfrac27=\dfrac6{56}\) = <span class="box">\(\dfrac3{28}\)</span></p>
<p>(Equivalently \(\dfrac{{}^3C_2}{{}^8C_2}=\dfrac3{28}\).)</p>""",
          topic="Probability",
          recall=r"""<ul><li>Without replacement: multiply conditional probabilities, \(P(A\cap B)=P(A)P(B|A)\).</li></ul>"""),

        # ---------------------------------------------------------------- Q2 – Q6 (2 marks)
        Q("2", 2, r"""<p>If \(y=e^{\sin^{-1}x}\) and \(z=e^{-\cos^{-1}x}\) where \(|x|\le1\) then find \(\dfrac{d^2y}{dx^2}\).</p>""",
          a=r"""<p>\(\dfrac{dy}{dx}=e^{\sin^{-1}x}\cdot\dfrac{1}{\sqrt{1-x^2}}=\dfrac{y}{\sqrt{1-x^2}}\), i.e. \(\sqrt{1-x^2}\,y_1=y\).</p>
<p>Differentiate again: \(\sqrt{1-x^2}\,y_2-\dfrac{x}{\sqrt{1-x^2}}y_1=y_1\Rightarrow(1-x^2)y_2-xy_1=\sqrt{1-x^2}\,y_1=y\).</p>
<p>So \((1-x^2)y_2=xy_1+y\) and</p>
<p><span class="box">\(\dfrac{d^2y}{dx^2}=\dfrac{e^{\sin^{-1}x}\left(x+\sqrt{1-x^2}\right)}{(1-x^2)^{3/2}}\)</span> &nbsp; (\(|x|\lt 1\)).</p>
<p class="note">z is not used in what is printed. The question was evidently meant to be about y and z together:
\(\dfrac yz=e^{\sin^{-1}x+\cos^{-1}x}=e^{\pi/2}\), so \(y=e^{\pi/2}z\), \(\dfrac{dy}{dz}=e^{\pi/2}\) and
\(\dfrac{d^2y}{dz^2}=0\).</p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>\(\frac{d}{dx}\sin^{-1}x=\frac1{\sqrt{1-x^2}}\).</li>
<li>Second derivative: clear the root first (\(\sqrt{1-x^2}\,y_1=y\)), then differentiate.</li>
<li>\(\sin^{-1}x+\cos^{-1}x=\frac\pi2\).</li></ul>"""),

        Q("2 (OR)", 2, r"""<p>The equation of the path traced by a roller coaster is given by the polynomial \(f(x)=a(x+9)(x+1)(x-3)\).
If the roller coaster crosses \(y\)-axis at a point, \((0,-1)\) then:</p>
{{fig:0}}
<p>(i) Find the value of \(a\).<br>(ii) Find \(f''(x)\) at \(x=1\).</p>""",
          qfig=(F.fig_q2or_coaster, "Redrawn from the printed picture of the roller-coaster track."),
          a=r"""<p>(i) \(f(0)=a(9)(1)(-3)=-27a=-1\Rightarrow\) <span class="box">\(a=\dfrac1{27}\)</span></p>
<p>(ii) \(f(x)=\dfrac1{27}(x+9)(x^2-2x-3)=\dfrac1{27}(x^3+7x^2-21x-27)\).</p>
<p>\(f'(x)=\dfrac1{27}(3x^2+14x-21)\), \(f''(x)=\dfrac1{27}(6x+14)\).</p>
<p>\(f''(1)=\dfrac{20}{27}\). <span class="box">\(f''(1)=\dfrac{20}{27}\)</span></p>
{{fig:0}}""",
          afig=[(F.fig_q2or_ans, "The track to scale: zeros at −9, −1, 3; it crosses the y-axis at (0, −1).")],
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>A curve crosses the y-axis where \(x=0\).</li>
<li>Expand the product before differentiating twice.</li></ul>"""),

        Q("3", 2, r"""<p>Evaluate: \(\displaystyle\int_0^{2\pi}|\sin x|\,dx\)</p>""",
          a=r"""<p>\(\sin x\ge0\) on \([0,\pi]\) and \(\le0\) on \([\pi,2\pi]\):</p>
<p>\(\displaystyle\int_0^{2\pi}|\sin x|\,dx=\int_0^{\pi}\sin x\,dx-\int_\pi^{2\pi}\sin x\,dx=[-\cos x]_0^\pi+[\cos x]_\pi^{2\pi}=2+2\)</p>
<p><span class="box">4</span></p>
{{fig:0}}""",
          afig=[(F.fig_q3_abssin, "Each arch of |sin x| has area 2.")],
          topic="Integrals",
          recall=r"""<ul><li>Split a modulus integral where the expression changes sign.</li>
<li>\(\int_0^\pi\sin x\,dx=2\).</li></ul>"""),

        Q("4", 2, r"""<p>Find the coordinates of the point on the curve \(\sqrt x+\sqrt y=4\) at which the tangent is equally inclined to the coordinate axes.</p>""",
          a=r"""<p>Differentiate: \(\dfrac1{2\sqrt x}+\dfrac1{2\sqrt y}\dfrac{dy}{dx}=0\Rightarrow\dfrac{dy}{dx}=-\dfrac{\sqrt y}{\sqrt x}\).</p>
<p>Equally inclined to the axes \(\Rightarrow\) slope \(=\pm1\). Since \(-\sqrt y/\sqrt x\le0\), only \(-1\) is possible:
\(\sqrt y=\sqrt x\Rightarrow y=x\).</p>
<p>Then \(2\sqrt x=4\Rightarrow x=4,\ y=4\).</p>
<p><span class="box">(4, 4)</span> (tangent there: \(x+y=8\)).</p>
{{fig:0}}""",
          afig=[(F.fig_q4_tangent, "The tangent at (4, 4) has slope −1: it makes 45° with both axes.")],
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Equally inclined to the axes: \(\tan\theta=\pm1\), slope \(\pm1\).</li>
<li>Slope of tangent \(=\dfrac{dy}{dx}\) at the point (implicit differentiation).</li></ul>"""),

        Q("5", 2, r"""<p>Evaluate: \(\displaystyle\int\frac{\sqrt{\tan x}}{\sin x\cos x}\,dx\)</p>""",
          a=r"""<p>Divide numerator and denominator by \(\cos^2x\): \(\dfrac{\sqrt{\tan x}}{\sin x\cos x}=\dfrac{\sqrt{\tan x}\sec^2x}{\tan x}=\dfrac{\sec^2x}{\sqrt{\tan x}}\).</p>
<p>Put \(\tan x=t\), \(\sec^2x\,dx=dt\): \(\displaystyle\int t^{-1/2}\,dt=2\sqrt t+C\).</p>
<p><span class="box">\(2\sqrt{\tan x}+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\sin x\cos x=\tan x\cos^2x\) — turn the integrand into \(\sec^2x\,g(\tan x)\).</li>
<li>\(\int t^n\,dt=\frac{t^{n+1}}{n+1}\).</li></ul>"""),

        Q("5 (OR)", 2, r"""<p>Evaluate: \(\displaystyle\int e^x\left(\frac{1-x}{1+x^2}\right)^2dx\)</p>""",
          a=r"""<p>\(\left(\dfrac{1-x}{1+x^2}\right)^2=\dfrac{1+x^2-2x}{(1+x^2)^2}=\dfrac1{1+x^2}-\dfrac{2x}{(1+x^2)^2}\).</p>
<p>With \(f(x)=\dfrac1{1+x^2}\), \(f'(x)=-\dfrac{2x}{(1+x^2)^2}\), the integrand is \(e^x[f(x)+f'(x)]\).</p>
<p><span class="box">\(\dfrac{e^x}{1+x^2}+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int e^x[f(x)+f'(x)]\,dx=e^xf(x)+C\).</li></ul>"""),

        Q("6", 2, r"""<p>Solve for \(x\): if \(\sin^{-1}\left(\dfrac3x\right)+\sin^{-1}\left(\dfrac4x\right)=\dfrac\pi2\).</p>""",
          a=r"""<p>\(\sin^{-1}\dfrac4x=\dfrac\pi2-\sin^{-1}\dfrac3x=\cos^{-1}\dfrac3x\).</p>
<p>Both angles must lie in \([0,\tfrac\pi2]\) (they add to \(\tfrac\pi2\) and \(\cos^{-1}\ge0\)), so \(x\gt 0\), and
\(\sin\left(\cos^{-1}\dfrac3x\right)=\sqrt{1-\dfrac9{x^2}}\).</p>
<p>\(\dfrac4x=\sqrt{1-\dfrac9{x^2}}\Rightarrow\dfrac{16}{x^2}=1-\dfrac9{x^2}\Rightarrow x^2=25\).</p>
<p>\(x=-5\) gives \(\sin^{-1}(-\tfrac35)+\sin^{-1}(-\tfrac45)=-\tfrac\pi2\), rejected.</p>
<p><span class="box">\(x=5\)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>\(\sin^{-1}u+\cos^{-1}u=\frac\pi2\).</li>
<li>\(\sin(\cos^{-1}u)=\sqrt{1-u^2}\) for \(u\in[-1,1]\).</li>
<li>Check each root in the original equation.</li></ul>"""),

        # ---------------------------------------------------------------- Q7 – Q10 (4 marks)
        Q("7", 4, r"""<p>If \(\cos^{-1}x+\cos^{-1}y+\cos^{-1}z=\pi\) then prove that \(x^2+y^2+z^2+2xyz=1\).</p>""",
          a=r"""<p>Let \(\cos^{-1}x=A,\ \cos^{-1}y=B,\ \cos^{-1}z=C\), each in \([0,\pi]\), so \(\cos A=x\), \(\sin A=\sqrt{1-x^2}\) (sine is \(\ge0\) on \([0,\pi]\)), and similarly for B, C.</p>
<p>Given \(A+B=\pi-C\Rightarrow\cos(A+B)=\cos(\pi-C)=-\cos C\).</p>
<p>\(\cos A\cos B-\sin A\sin B=-z\Rightarrow xy-\sqrt{1-x^2}\sqrt{1-y^2}=-z\)</p>
<p>\(\Rightarrow xy+z=\sqrt{(1-x^2)(1-y^2)}\).</p>
<p>Square: \(x^2y^2+2xyz+z^2=1-x^2-y^2+x^2y^2\)</p>
<p>\(\Rightarrow\) <span class="box">\(x^2+y^2+z^2+2xyz=1\)</span> &nbsp; Hence proved.</p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>\(\cos(A+B)=\cos A\cos B-\sin A\sin B\); \(\cos(\pi-C)=-\cos C\).</li>
<li>For \(A=\cos^{-1}x\in[0,\pi]\): \(\sin A=\sqrt{1-x^2}\).</li></ul>"""),

        Q("8", 4, r"""<p>Evaluate: \(\displaystyle\int\tan^{-1}\sqrt{\frac{1-x}{1+x}}\,dx\)</p>""",
          a=r"""<p>Put \(x=\cos2\theta\) (\(-1\lt x\le1\), \(0\le\theta\lt\tfrac\pi2\)), so \(\theta=\tfrac12\cos^{-1}x\):</p>
<p>\(\sqrt{\dfrac{1-\cos2\theta}{1+\cos2\theta}}=\sqrt{\dfrac{2\sin^2\theta}{2\cos^2\theta}}=\tan\theta\) (\(\tan\theta\ge0\)), hence
\(\tan^{-1}\sqrt{\dfrac{1-x}{1+x}}=\theta=\dfrac12\cos^{-1}x\).</p>
<p>\(I=\dfrac12\displaystyle\int\cos^{-1}x\cdot1\,dx\). By parts (first function \(\cos^{-1}x\)):</p>
<p>\(I=\dfrac12\left[x\cos^{-1}x-\displaystyle\int x\cdot\frac{-1}{\sqrt{1-x^2}}\,dx\right]=\dfrac12\left[x\cos^{-1}x+\int\frac{x}{\sqrt{1-x^2}}\,dx\right]\).</p>
<p>\(\displaystyle\int\frac{x\,dx}{\sqrt{1-x^2}}=-\sqrt{1-x^2}\) (put \(1-x^2=t\)).</p>
<p><span class="box">\(I=\dfrac12\left(x\cos^{-1}x-\sqrt{1-x^2}\right)+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\frac{1-\cos2\theta}{1+\cos2\theta}=\tan^2\theta\) — the substitution \(x=\cos2\theta\).</li>
<li>Integration by parts: \(\int u\,v\,dx=u\int v\,dx-\int\left(u'\int v\,dx\right)dx\).</li>
<li>\(\frac{d}{dx}\cos^{-1}x=-\frac1{\sqrt{1-x^2}}\).</li></ul>"""),

        Q("9", 4, r"""<p>Competitive examinations are considered an egalitarian way to select worthy candidates without risking influence peddling,
bias or other concerns. Self-motivated and hard-working students are very keen about to clear this type of competitive examination.
To clear one of these types of examination, Sana took admission in a highly reputed Institution of Kolkata where the academic growth
of a candidate in \(x\) months is represented by the polynomial function \(f(x)=2x^3-9x^2+12x+1\). From the first five months of the
year mention specifically the month or months in which the performance of Sana is (i) increasing (ii) decreasing.</p>""",
          a=r"""<p>\(f'(x)=6x^2-18x+12=6(x-1)(x-2)\). Critical points \(x=1,\ 2\) divide \([0,5]\):</p>
<table class="data"><tr><th>Interval</th><td>\((0,1)\)</td><td>\((1,2)\)</td><td>\((2,5)\)</td></tr>
<tr><th>Sign of \((x-1)(x-2)\)</th><td>\((-)(-)=+\)</td><td>\((+)(-)=-\)</td><td>\((+)(+)=+\)</td></tr>
<tr><th>f</th><td>increasing</td><td>decreasing</td><td>increasing</td></tr></table>
{{fig:0}}
<p>(i) <span class="box">Increasing in the 1st month (\(0\lt x\lt 1\)) and in the 3rd, 4th and 5th months (\(2\lt x\lt 5\))</span></p>
<p>(ii) <span class="box">Decreasing in the 2nd month (\(1\lt x\lt 2\))</span></p>
<p>(The growth score falls from \(f(1)=6\) to \(f(2)=5\) and then rises to \(f(5)=86\).)</p>""",
          afig=[(F.fig_q9_growth, "f(x) = 2x³ − 9x² + 12x + 1 on [0, 3.1]: falls only between the end of month 1 and the end of month 2.")],
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Increasing where \(f'(x)\gt 0\), decreasing where \(f'(x)\lt 0\).</li>
<li>Factorise \(f'\) and test the sign on each interval between critical points.</li></ul>"""),

        Q("9 (OR)", 4, r"""<p>If \(y=\sqrt{x+1}-\sqrt{x-1}\) then prove that \((x^2-1)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}-\dfrac y4=0\)</p>""",
          a=r"""<p>\(\dfrac{dy}{dx}=\dfrac1{2\sqrt{x+1}}-\dfrac1{2\sqrt{x-1}}=\dfrac{\sqrt{x-1}-\sqrt{x+1}}{2\sqrt{x^2-1}}=\dfrac{-y}{2\sqrt{x^2-1}}\).</p>
<p>So \(2\sqrt{x^2-1}\,y_1=-y\). Square: \(4(x^2-1)y_1^2=y^2\).</p>
<p>Differentiate w.r.t. \(x\): \(8xy_1^2+8(x^2-1)y_1y_2=2yy_1\).</p>
<p>Divide by \(8y_1\) (\(y_1\ne0\) for \(x\gt 1\)): \((x^2-1)y_2+xy_1=\dfrac y4\).</p>
<p><span class="box">\((x^2-1)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}-\dfrac y4=0\)</span> &nbsp; Hence proved.</p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Express \(y_1\) in terms of \(y\), square to remove the root, then differentiate again.</li>
<li>Divide by \(y_1\) only after noting it is non-zero.</li></ul>"""),

        Q("10", 4, r"""<p>From a medical survey it was found that chances of a patient having heart attack is 40%. The survey states that a meditation
and yoga course reduce the risk of heart attack by 30% while prescription of certain drug reduces it chances by 25%. At any given point
in time, a patient can choose any one of the two options with equal probabilities. It is given that after going through one of the two
options the patient selected at random suffers a heart attack. Find the probability that the patient followed a course of meditation and yoga.</p>""",
          a=r"""<p>Let \(E_1\): patient follows meditation and yoga, \(E_2\): patient takes the drug, H: patient has a heart attack.</p>
<p>\(P(E_1)=P(E_2)=\tfrac12\).</p>
<p>\(P(H|E_1)=0.40(1-0.30)=0.28\), &nbsp; \(P(H|E_2)=0.40(1-0.25)=0.30\).</p>
{{fig:0}}
<p>By Bayes' theorem,</p>
<p>\[P(E_1|H)=\frac{P(E_1)P(H|E_1)}{P(E_1)P(H|E_1)+P(E_2)P(H|E_2)}\]</p>
<p>\[=\frac{\frac12(0.28)}{\frac12(0.28)+\frac12(0.30)}=\frac{0.28}{0.58}=\frac{14}{29}.\]</p>
<p><span class="box">\(\dfrac{14}{29}\approx0.483\)</span></p>""",
          afig=[(F.fig_q10_tree, "Tree diagram: each option chosen with probability ½; risk reduced from 0.40.")],
          topic="Probability (Bayes' theorem)",
          recall=r"""<ul><li>“Reduces the risk by 30%” means the new risk is 70% of 0.40.</li>
<li>Bayes: \(P(E_i|H)=\dfrac{P(E_i)P(H|E_i)}{\sum_jP(E_j)P(H|E_j)}\).</li></ul>"""),

        Q("10 (OR)", 4, r"""<p>Border-Gavaskar Trophy is a test series which is played between India and Australia. The probability that India wins each of the
match in the series is 0.7, losing each of the match is 0.2 and having no result in each match is 0.1. If it is going to be a three match test
series find the probability India wins atleast two matches in the test series but does not lose in any one of the matches.</p>
<p class="note">[The printed photograph of the two captains with the trophy carries no data and is not reproduced.]</p>""",
          a=r"""<p>Matches are independent; per match P(win) = 0.7, P(no result) = 0.1. “At least two wins and no loss” in three matches means</p>
<p>(i) three wins: WWW, probability \(0.7^3=0.343\);<br>
(ii) two wins and one no-result: WWN in any of 3 orders, probability \(3\times0.7^2\times0.1=0.147\).</p>
<p>Required probability \(=0.343+0.147\) = <span class="box">0.49</span></p>""",
          topic="Probability (independent events)",
          recall=r"""<ul><li>Independent trials: multiply probabilities of the individual outcomes.</li>
<li>Count the arrangements of each pattern (here \({}^3C_1=3\) places for the no-result).</li></ul>"""),

        # ---------------------------------------------------------------- Q11 – Q14 (6 marks)
        Q("11", 6, r"""<p>The sum of the three number is 6. If we multiply the third number by 3 and add second number to it, we get 11.
By adding first and third numbers, we get twice of the second number. Answer the following questions:</p>
<p>(i) Translate the above-mentioned problem into a system of equation.<br>
(ii) Hence, solve the system of equation by using Matrix method.</p>""",
          a=r"""<p>(i) Let the numbers be \(x,y,z\):</p>
<p>\(x+y+z=6,\qquad y+3z=11,\qquad x+z=2y\ \text{ i.e. } x-2y+z=0.\)</p>
<p>(ii) \(AX=B\) with \(A=\begin{bmatrix}1&1&1\\0&1&3\\1&-2&1\end{bmatrix}\), \(X=\begin{bmatrix}x\\y\\z\end{bmatrix}\), \(B=\begin{bmatrix}6\\11\\0\end{bmatrix}\).</p>
<p>\(|A|=1(1+6)-1(0-3)+1(0-1)=7+3-1=9\ne0\), so \(A^{-1}\) exists and the solution is unique.</p>
<p>Cofactors: \(C_{11}=7,\ C_{12}=3,\ C_{13}=-1;\ C_{21}=-3,\ C_{22}=0,\ C_{23}=3;\ C_{31}=2,\ C_{32}=-3,\ C_{33}=1\).</p>
<p>\(\operatorname{adj}A=\begin{bmatrix}7&-3&2\\3&0&-3\\-1&3&1\end{bmatrix}\), \(A^{-1}=\dfrac19\begin{bmatrix}7&-3&2\\3&0&-3\\-1&3&1\end{bmatrix}\).</p>
<p>\(X=A^{-1}B=\dfrac19\begin{bmatrix}42-33+0\\18+0-0\\-6+33+0\end{bmatrix}=\dfrac19\begin{bmatrix}9\\18\\27\end{bmatrix}=\begin{bmatrix}1\\2\\3\end{bmatrix}\).</p>
<p><span class="box">\(x=1,\ y=2,\ z=3\)</span> (check: \(1+2+3=6\), \(2+9=11\), \(1+3=4=2\times2\)).</p>""",
          topic="Matrices and Determinants (system of equations)",
          recall=r"""<ul><li>\(AX=B\Rightarrow X=A^{-1}B\) when \(|A|\ne0\).</li>
<li>\(A^{-1}=\dfrac{\operatorname{adj}A}{|A|}\); adj A is the transpose of the cofactor matrix.</li></ul>"""),

        Q("12", 6, r"""<p>Find the general solution of the differential equation: \(\left[x\sin^2\left(\dfrac yx\right)-y\right]dx+x\,dy=0\)</p>
<p>Hence find the particular solution of the above differential equation when \(y\left(\dfrac\pi4\right)=1\).</p>""",
          a=r"""<p>\(\dfrac{dy}{dx}=\dfrac{y-x\sin^2(y/x)}{x}=\dfrac yx-\sin^2\dfrac yx\): homogeneous. Put \(y=vx\), \(\dfrac{dy}{dx}=v+x\dfrac{dv}{dx}\):</p>
<p>\(v+x\dfrac{dv}{dx}=v-\sin^2v\Rightarrow\dfrac{dv}{\sin^2v}=-\dfrac{dx}{x}\Rightarrow\displaystyle\int\operatorname{cosec}^2v\,dv=-\int\frac{dx}x\).</p>
<p>\(-\cot v=-\log|x|-C\Rightarrow\cot v=\log|x|+C\).</p>
<p>General solution: <span class="box">\(\cot\left(\dfrac yx\right)=\log|x|+C\)</span></p>
<p><b>Particular solution (as printed: \(y=1\) when \(x=\tfrac\pi4\)).</b> \(\dfrac yx=\dfrac4\pi\):
\(\cot\dfrac4\pi=\log\dfrac\pi4+C\Rightarrow C=\cot\dfrac4\pi-\log\dfrac\pi4\).</p>
<p><span class="box">\(\cot\left(\dfrac yx\right)=\log\left|\dfrac{4x}{\pi}\right|+\cot\left(\dfrac4\pi\right)\)</span></p>
<p class="note">The textbook version of this question gives \(y=\frac\pi4\) when \(x=1\), which is surely what was meant
(the printed condition leaves \(\cot\frac4\pi\), an angle of \(\frac4\pi\) radians, in the answer). Then
\(\cot\frac\pi4=1=\log1+C\Rightarrow C=1\), and the particular solution is \(\cot\left(\dfrac yx\right)=\log|ex|\).</p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Homogeneous equation \(\frac{dy}{dx}=F\left(\frac yx\right)\): substitute \(y=vx\).</li>
<li>\(\int\operatorname{cosec}^2v\,dv=-\cot v\).</li>
<li>Substitute the initial condition to fix C.</li></ul>"""),

        Q("12 (OR)", 6, r"""<p>Evaluate: \(\displaystyle\int_0^{\pi/2}\big(2\log(\sin x)-\log(\sin2x)\big)\,dx\)</p>""",
          a=r"""<p>\(\log\sin2x=\log(2\sin x\cos x)=\log2+\log\sin x+\log\cos x\), so the integrand is \(\log\sin x-\log\cos x-\log2\).</p>
<p>\(I=\displaystyle\int_0^{\pi/2}\log\sin x\,dx-\int_0^{\pi/2}\log\cos x\,dx-\frac\pi2\log2\).</p>
<p>By \(\int_0^af(x)\,dx=\int_0^af(a-x)\,dx\), \(\displaystyle\int_0^{\pi/2}\log\sin x\,dx=\int_0^{\pi/2}\log\cos x\,dx\), so the first two terms cancel
(each equals \(-\tfrac\pi2\log2\), finite).</p>
<p><span class="box">\(I=-\dfrac\pi2\log2=\dfrac\pi2\log\dfrac12\)</span></p>""",
          topic="Definite Integrals (properties)",
          recall=r"""<ul><li>\(\int_0^{\pi/2}f(\sin x)\,dx=\int_0^{\pi/2}f(\cos x)\,dx\).</li>
<li>\(\log(abc)=\log a+\log b+\log c\); \(\int_0^{\pi/2}\log\sin x\,dx=-\frac\pi2\log2\).</li></ul>"""),

        Q("13", 6, r"""<p>A swimmer is at a point \(S\) in the sea at a distance \(2\) km from the nearest point \(A\) on a straight shore. The House \(H\)
of the swimmer is on the shore at a distance of \(4\) km from point \(A\). If the swimmer can swim at the rate of \(4\) km/hr and walk at the
rate of \(6\) km/hr then using differentiation and from the given information answer the following question:</p>
{{fig:0}}
<p>(i) Find the distance of the point \(B\) on the shore from the point \(A\) where he should land so that he can reach his house \(H\) in
shortest possible time?<br>
(ii) The shortest time required to travel from point \(S\) to his house \(H\).</p>""",
          qfig=F.fig_q13_swim,
          a=r"""<p>Let \(AB=x\) km \((0\le x\le4)\). Then \(SB=\sqrt{4+x^2}\) (right angle at A) and \(BH=4-x\).</p>
{{fig:0}}
<p>Time \(T(x)=\dfrac{\sqrt{4+x^2}}{4}+\dfrac{4-x}{6}\) hours.</p>
<p>\(\dfrac{dT}{dx}=\dfrac{x}{4\sqrt{4+x^2}}-\dfrac16=0\Rightarrow3x=2\sqrt{4+x^2}\Rightarrow9x^2=16+4x^2\Rightarrow x^2=\dfrac{16}5\Rightarrow x=\dfrac4{\sqrt5}\).</p>
<p>\(\dfrac{d^2T}{dx^2}=\dfrac14\cdot\dfrac{4}{(4+x^2)^{3/2}}=\dfrac1{(4+x^2)^{3/2}}\gt 0\): minimum.</p>
<p>(i) <span class="box">\(AB=\dfrac4{\sqrt5}=\dfrac{4\sqrt5}5\approx1.79\) km</span></p>
<p>(ii) \(\sqrt{4+\tfrac{16}5}=\dfrac6{\sqrt5}\), so \(T_{\min}=\dfrac{6}{4\sqrt5}+\dfrac{4-\frac4{\sqrt5}}6=\dfrac{3}{2\sqrt5}-\dfrac{2}{3\sqrt5}+\dfrac23=\dfrac{5}{6\sqrt5}+\dfrac23=\dfrac{\sqrt5}6+\dfrac23\).</p>
<p><span class="box">\(T_{\min}=\dfrac{4+\sqrt5}{6}\) h \(\approx1.04\) h \(\approx\) 62 minutes</span></p>
<p>(Compare the ends: swimming straight to A takes \(\tfrac12+\tfrac23\approx1.17\) h, swimming straight to H takes \(\tfrac{\sqrt{20}}4\approx1.12\) h — both longer.)</p>""",
          afig=[(F.fig_q13_geometry, "Swim SB, then walk BH.")],
          topic="Applications of Derivatives (maxima and minima)",
          recall=r"""<ul><li>Time = distance ÷ speed; add the two legs.</li>
<li>Minimum: \(T'(x)=0\) and \(T''(x)\gt 0\); compare with the end points of the interval.</li></ul>"""),

        Q("13 (OR)", 6, r"""<p>A company is planning to launch a new product and decides to pack the new product in a closed right cylindrical can of volume
\(432\pi\) cm³. The cans are to be made from tin sheet. The company tried different options.</p>
{{fig:0}}
<p>Based on the above information, answer the following questions:</p>
<p>(i) If \(r\) cm is the radius of the base and \(h\) cm is the height of the cylinder then find the height of the cylindrical can in terms of the radius \(r\) cm.<br>
(ii) If \(S\) cm² is the total surface area of the cylindrical can then find \(S\) in terms of the radius \(r\) cm.<br>
(iii) Using differentiation find the radius of the cylindrical can when total surface area is minimum.<br>
(iv) Find the minimum total surface area of the cylindrical can. <b>(Keep your answer in terms of \(\pi\)).</b></p>""",
          qfig=F.fig_q13or_cans,
          a=r"""<p>(i) \(\pi r^2h=432\pi\Rightarrow\) <span class="box">\(h=\dfrac{432}{r^2}\) cm</span></p>
<p>(ii) \(S=2\pi r^2+2\pi rh=2\pi r^2+2\pi r\cdot\dfrac{432}{r^2}\Rightarrow\) <span class="box">\(S=2\pi r^2+\dfrac{864\pi}{r}\)</span></p>
<p>(iii) \(\dfrac{dS}{dr}=4\pi r-\dfrac{864\pi}{r^2}=0\Rightarrow r^3=216\Rightarrow r=6\).
\(\dfrac{d^2S}{dr^2}=4\pi+\dfrac{1728\pi}{r^3}\gt 0\): minimum. <span class="box">\(r=6\) cm</span> (then \(h=12\) cm \(=2r\)).</p>
<p>(iv) \(S_{\min}=2\pi(36)+\dfrac{864\pi}{6}=72\pi+144\pi\) = <span class="box">\(216\pi\) cm²</span></p>""",
          topic="Applications of Derivatives (maxima and minima)",
          recall=r"""<ul><li>Use the fixed quantity (volume) to write S in one variable.</li>
<li>Closed cylinder: \(S=2\pi r^2+2\pi rh\); minimum surface for given volume when \(h=2r\).</li></ul>"""),

        Q("14", 6, r"""<p>In a group activity class, there are <b>10</b> students whose ages are <b>16, 17, 15, 14, 19, 17, 16, 19, 16 and 15</b> years of age.
One student is selected at random such that each has equal chances of being chosen and the age of the student is recorded.</p>
<p>Based on the given information, answer the following questions:</p>
<p>(i) Find the probability that the age of the selected student is a composite number.<br>
(ii) If \(X\) represent the random variable of the age of the selected students then what can be the possible value(s) of \(X\).<br>
(iii) Find the probability distribution of the random variable \(X\).<br>
(iv) A student was selected at random, and his age was found to be more than 15 years old. Find the probability that his age is a prime number.<br>
(v) Find the mean age of the students from the probability distribution.</p>
<p class="note">[The printed illustration of children in a music class carries no data and is not reproduced.]</p>""",
          a=r"""<p>Frequencies: 14 → 1, 15 → 2, 16 → 3, 17 → 2, 19 → 2 (total 10).</p>
<p>(i) Composite ages: 14, 15, 16 → \(1+2+3=6\) students. \(P=\dfrac6{10}\) = <span class="box">\(\dfrac35\)</span></p>
<p>(ii) <span class="box">\(X\in\{14,15,16,17,19\}\)</span></p>
<p>(iii)</p>
<table class="data"><tr><th>X</th><td>14</td><td>15</td><td>16</td><td>17</td><td>19</td></tr>
<tr><th>P(X)</th><td>\(\frac1{10}\)</td><td>\(\frac2{10}\)</td><td>\(\frac3{10}\)</td><td>\(\frac2{10}\)</td><td>\(\frac2{10}\)</td></tr></table>
<p>(Total = 1 ✓.)</p>
<p>(iv) Let A: age is prime (17 or 19), B: age \(\gt 15\) (16, 17 or 19). \(P(B)=\tfrac7{10}\), \(P(A\cap B)=\tfrac4{10}\).</p>
<p>\(P(A|B)=\dfrac{P(A\cap B)}{P(B)}=\dfrac{4/10}{7/10}\) = <span class="box">\(\dfrac47\)</span></p>
<p>(v) \(E(X)=\sum x\,p(x)=\dfrac{14+30+48+34+38}{10}=\dfrac{164}{10}\) = <span class="box">16.4 years</span></p>""",
          topic="Probability (random variable and its distribution)",
          recall=r"""<ul><li>Probability distribution: each value of X with its probability; probabilities add to 1.</li>
<li>Conditional probability \(P(A|B)=\frac{P(A\cap B)}{P(B)}\).</li>
<li>Mean \(E(X)=\sum x_ip_i\).</li></ul>"""),

        # ---------------------------------------------------------------- Section B
        SEC("Section B – 15 Marks",
            "Question 15 [5 × 1 = 5]. In subparts (i) to (iii) choose the correct options and in subparts (iv) &amp; (v), "
            "answer the questions as instructed."),

        Q("15(i)", 1, r"""<p><b>Assertion:</b> If \(\vec a,\vec b\) and \(\vec c\) are three mutually perpendicular unit vectors then \(|\vec a+\vec b+\vec c|=\sqrt3\)<br>
<b>Reason:</b> \(|\vec a+\vec b+\vec c|^2=|\vec a|^2+|\vec b|^2+|\vec c|^2+2(\vec a\cdot\vec b+\vec b\cdot\vec c+\vec c\cdot\vec a)\)</p>""" + AR,
          a=r"""<p>R is the expansion of \((\vec a+\vec b+\vec c)\cdot(\vec a+\vec b+\vec c)\): true. With unit vectors and all dot products 0, it gives
\(|\vec a+\vec b+\vec c|^2=1+1+1+0=3\), so A is true, and R is what proves it.</p>
<p><span class="box">(a)</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(|\vec v|^2=\vec v\cdot\vec v\).</li>
<li>Perpendicular vectors: \(\vec a\cdot\vec b=0\).</li></ul>"""),

        Q("15(ii)", 1, r"""<p>If the direction angles of a straight line in space is \(\alpha,\beta\) and \(\gamma\) respectively then \(\cos2\alpha+\cos2\beta+\cos2\gamma\) is</p>
<p>(a) 1 &emsp; (b) −2 &emsp; (c) −1 &emsp; (d) 2</p>""",
          a=r"""<p>\(\cos2\theta=2\cos^2\theta-1\), so the sum \(=2(\cos^2\alpha+\cos^2\beta+\cos^2\gamma)-3=2(1)-3=-1\).</p>
<p><span class="box">(c) −1</span></p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Direction cosines: \(l^2+m^2+n^2=1\).</li></ul>"""),

        Q("15(iii)", 1, r"""<p>If the planes \(\vec r\cdot(2\hat i-\lambda\hat j+3\hat k)=0\) and \(\vec r\cdot(\lambda\hat i+5\hat j-\hat k)=0\) are perpendicular to each other then find the value of \(\lambda\) is:</p>
<p>(a) 0 &emsp; (b) 1 &emsp; (c) −1 &emsp; (d) −2</p>""",
          a=r"""<p>Planes are perpendicular when their normals are: \(\vec n_1\cdot\vec n_2=2\lambda-5\lambda-3=-3\lambda-3=0\Rightarrow\lambda=-1\).</p>
<p><span class="box">(c) −1</span></p>""",
          topic="Three-dimensional Geometry (planes)",
          recall=r"""<ul><li>\(\vec r\cdot\vec n=d\): \(\vec n\) is normal to the plane.</li>
<li>Perpendicular planes: \(\vec n_1\cdot\vec n_2=0\).</li></ul>"""),

        Q("15(iv)", 1, r"""<p>If \(\vec a=2\hat i+\hat j+2\hat k\) and \(\vec b=5\hat i-3\hat j+\hat k\) then find the projection of \(\vec b\) on \(\vec a\).</p>""",
          a=r"""<p>Projection of \(\vec b\) on \(\vec a=\dfrac{\vec a\cdot\vec b}{|\vec a|}=\dfrac{10-3+2}{\sqrt{4+1+4}}=\dfrac93\) = <span class="box">3</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>Projection of \(\vec b\) on \(\vec a\) is \(\vec b\cdot\hat a=\dfrac{\vec a\cdot\vec b}{|\vec a|}\).</li></ul>"""),

        Q("15(v)", 1, r"""<p>Find a vector of magnitude 20 units parallel to the vector \(2\hat i+5\hat j+4\hat k\).</p>""",
          a=r"""<p>\(|2\hat i+5\hat j+4\hat k|=\sqrt{4+25+16}=\sqrt{45}=3\sqrt5\). Required vector \(=20\cdot\dfrac{2\hat i+5\hat j+4\hat k}{3\sqrt5}\)</p>
<p><span class="box">\(\dfrac{4\sqrt5}{3}\left(2\hat i+5\hat j+4\hat k\right)=\dfrac{8\sqrt5}3\hat i+\dfrac{20\sqrt5}3\hat j+\dfrac{16\sqrt5}3\hat k\)</span></p>
<p>(The opposite vector \(-\dfrac{4\sqrt5}3(2\hat i+5\hat j+4\hat k)\) is also parallel, in the reverse sense.)</p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>Vector of magnitude \(k\) along \(\vec v\): \(k\,\hat v=k\dfrac{\vec v}{|\vec v|}\).</li></ul>"""),

        Q("16", 2, r"""<p>If the vectors \(\vec a\) and \(\vec b\) are such that \(|\vec a|=3\), \(|\vec b|=\dfrac{\sqrt2}3\) and \(\vec a\times\vec b\) is a unit vector, then find the angle(s) between the vectors \(\vec a\) and \(\vec b\).</p>""",
          a=r"""<p>\(|\vec a\times\vec b|=|\vec a||\vec b|\sin\theta\Rightarrow1=3\cdot\dfrac{\sqrt2}3\sin\theta=\sqrt2\sin\theta\Rightarrow\sin\theta=\dfrac1{\sqrt2}\).</p>
<p>With \(0\le\theta\le\pi\): <span class="box">\(\theta=\dfrac\pi4\) or \(\dfrac{3\pi}4\)</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(|\vec a\times\vec b|=|\vec a||\vec b|\sin\theta\), \(\theta\in[0,\pi]\).</li>
<li>\(\sin\theta=k\gt 0\) has two solutions in \([0,\pi]\).</li></ul>"""),

        Q("16 (OR)", 2, r"""<p>If the vectors \(\vec a\) and \(\vec b\) are inclined at an angle of 120°, \(|\vec a|=1\) and \(|\vec b|=2\) then find \(\left((\vec a+3\vec b)\times(3\vec a-\vec b)\right)^2\).</p>""",
          a=r"""<p>\((\vec a+3\vec b)\times(3\vec a-\vec b)=3\,\vec a\times\vec a-\vec a\times\vec b+9\,\vec b\times\vec a-3\,\vec b\times\vec b=-\vec a\times\vec b-9\,\vec a\times\vec b=-10\,(\vec a\times\vec b)\)</p>
<p>(using \(\vec a\times\vec a=\vec 0\), \(\vec b\times\vec a=-\vec a\times\vec b\)).</p>
<p>\(|\vec a\times\vec b|=1\cdot2\sin120^\circ=\sqrt3\). Hence \(\left(-10\,\vec a\times\vec b\right)^2=100\times3\).</p>
<p><span class="box">300</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>Cross product is distributive and anti-commutative; \(\vec a\times\vec a=\vec0\).</li>
<li>\((\vec v)^2=|\vec v|^2\).</li></ul>"""),

        Q("17", 4, r"""<p>Find the equation(s) of the plane parallel to the plane \(2x-4y+4z-7=0\) which are at a distance of 5 units from the point \((3,-1,2)\).</p>""",
          a=r"""<p>A plane parallel to the given one: \(2x-4y+4z+d=0\).</p>
<p>Distance from \((3,-1,2)\): \(\dfrac{|2(3)-4(-1)+4(2)+d|}{\sqrt{4+16+16}}=\dfrac{|18+d|}{6}=5\Rightarrow18+d=\pm30\Rightarrow d=12\) or \(d=-48\).</p>
<p><span class="box">\(2x-4y+4z+12=0\) i.e. \(x-2y+2z+6=0\), and \(2x-4y+4z-48=0\) i.e. \(x-2y+2z-24=0\)</span></p>""",
          topic="Three-dimensional Geometry (planes)",
          recall=r"""<ul><li>Parallel planes share the normal: only the constant changes.</li>
<li>Distance of \((x_1,y_1,z_1)\) from \(ax+by+cz+d=0\): \(\dfrac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}\).</li></ul>"""),

        Q("17 (OR)", 4, r"""<p>Find the equation of a straight line in space which passes through the point \((2,-1,3)\) and perpendicular the lines:
\(\vec r=(\hat i+\hat j-\hat k)+\lambda(2\hat i-2\hat j+\hat k)\) and \(\vec r=(2\hat i-\hat j-3\hat k)+\mu(\hat i+2\hat j+2\hat k)\).</p>""",
          a=r"""<p>The required line is perpendicular to both \(\vec b_1=2\hat i-2\hat j+\hat k\) and \(\vec b_2=\hat i+2\hat j+2\hat k\), so it is parallel to</p>
<p>\(\vec b_1\times\vec b_2=\begin{vmatrix}\hat i&\hat j&\hat k\\2&-2&1\\1&2&2\end{vmatrix}=\hat i(-4-2)-\hat j(4-1)+\hat k(4+2)=-6\hat i-3\hat j+6\hat k=-3(2\hat i+\hat j-2\hat k)\).</p>
<p>Line through \((2,-1,3)\) along \(2\hat i+\hat j-2\hat k\):</p>
<p><span class="box">\(\vec r=(2\hat i-\hat j+3\hat k)+t(2\hat i+\hat j-2\hat k)\)</span>, i.e. \(\dfrac{x-2}{2}=\dfrac{y+1}{1}=\dfrac{z-3}{-2}\).</p>""",
          topic="Three-dimensional Geometry (lines)",
          recall=r"""<ul><li>A direction perpendicular to two vectors is their cross product.</li>
<li>Line through \(\vec a\) parallel to \(\vec b\): \(\vec r=\vec a+t\vec b\).</li></ul>"""),

        Q("18", 4, r"""<p>Sketch the system of curve and straight lines \(y=x^2+2\), \(y=x\), \(x=0\) and \(x=3\).
Hence using integration find the area of the region bounded by the above system of curve and straight lines.</p>""",
          a=r"""<p>\(y=x^2+2\) is an upward parabola with vertex (0, 2); \(x^2+2-x=(x-\tfrac12)^2+\tfrac74\gt 0\), so the parabola lies above \(y=x\) everywhere and they never meet.
The region lies between them from \(x=0\) to \(x=3\).</p>
{{fig:0}}
<p>\[A=\int_0^3\left[(x^2+2)-x\right]dx=\left[\frac{x^3}{3}+2x-\frac{x^2}{2}\right]_0^3=9+6-\frac92=\frac{21}{2}.\]</p>
<p><span class="box">\(\dfrac{21}{2}\) sq units</span></p>""",
          afig=[(F.fig_q18_area, "Region between y = x² + 2 (above) and y = x (below), from x = 0 to x = 3.")],
          topic="Application of Integrals",
          recall=r"""<ul><li>Area between curves: \(\int_a^b(y_{\text{upper}}-y_{\text{lower}})\,dx\).</li>
<li>Check which curve is on top over the whole interval (here they never cross).</li></ul>"""),

        # ---------------------------------------------------------------- Section C
        SEC("Section C – 15 Marks",
            "Question 19 [5 × 1 = 5]. In subparts (i) to (iii) choose the correct options and in subparts (iii) &amp; (v), "
            "answer the questions as instructed. — In the ISC 2027 syllabus: 19(i) (MC = AC), 19(iii) (Linear "
            "Programming), 19(v) (break-even), Q20 and Q20 (OR) (maximum profit / revenue — Applications of "
            "Derivatives) and Q22 (Linear Programming). Excluded: 19(ii), 19(iv), Q21 and Q21 (OR) (regression)."),

        Q("19(i)", 1, r"""<p>If the total cost function for a production of \(x\) units of a commodity is given by \(x^2-7x+36\) then the total
number of units produced for which \(MC=AC\) is</p>
<p>(a) 4 &emsp; (b) 6 &emsp; (c) 9 &emsp; (d) 36</p>""",
          a=r"""<p>\(C=x^2-7x+36\): \(MC=\dfrac{dC}{dx}=2x-7\), \(AC=\dfrac Cx=x-7+\dfrac{36}x\).</p>
<p>\(2x-7=x-7+\dfrac{36}x\Rightarrow x^2=36\Rightarrow x=6\) (\(x\gt 0\)).</p>
<p><span class="box">(b) 6</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Marginal cost \(MC=\frac{dC}{dx}\); average cost \(AC=\frac{C}{x}\).</li>
<li>MC = AC exactly where AC is minimum.</li></ul>"""),

        Q("19(ii)", 1, r"""<p>If the coefficient of correlation \(r=0\) then which of the following is <b>not</b> true about the about the regression lines:</p>
<p>(a) the regression lines are parallel to each other.<br>(b) the regression lines are perpendicular to each other.<br>
(c) \(b_{yx}=b_{xy}=0\)<br>(d) The equation of regression line of \(x\) on \(y\) will parallel to \(y\)-axis.</p>""",
          excluded=REGR.format("regression lines when r = 0")),

        Q("19(iii)", 1, r"""<p><b>Statement 1:</b> Linear Programming Problem can be used only when the objective function and all the constraints are in the
form of equation or inequation.<br>
<b>Statement 2:</b> The coefficient of the constraints and the objective function must be known and remain unchanged during study time
of a given problem.</p>""" + ST,
          a=r"""<p>Statement 1: an LPP needs the objective function and every constraint expressed as linear equations or inequations
(linearity) — true. (The printed statement omits the word “linear”; it is the standard limitation of LPP that the
objective function and constraints be expressible as <i>linear</i> equations/inequations, and is read that way.)</p>
<p>Statement 2: the coefficients of the objective function and constraints are assumed known and constant over the period studied
(certainty) — true.</p>
<p><span class="box">(c)</span></p>""",
          topic="Linear Programming",
          recall=r"""<ul><li>LPP: optimise a linear objective function subject to linear constraints and non-negativity.</li>
<li>Assumptions: linearity, certainty (fixed known coefficients), divisibility, non-negativity.</li></ul>"""),

        Q("19(iv)", 1, r"""<p>If the coefficient of correlation is \(-0.6\), standard deviation of \(x\) is 5 and the variance of \(y\) is 16 then find the value of \(b_{yx}\).</p>""",
          excluded=REGR.format("regression coefficient")),

        Q("19(v)", 1, r"""<p>The fixed cost of a new product is Rs 30,000 and the variable cost per unit <b>is Rs 800.</b> If the demand function is
\(p(x)=4500-100x\), then find the breakeven values.</p>""",
          a=r"""<p>\(C(x)=30000+800x\); revenue \(R(x)=x\,p(x)=4500x-100x^2\).</p>
<p>Break-even: \(R=C\Rightarrow4500x-100x^2=30000+800x\Rightarrow100x^2-3700x+30000=0\Rightarrow x^2-37x+300=0\)</p>
<p>\(\Rightarrow(x-12)(x-25)=0\).</p>
<p><span class="box">Break-even at \(x=12\) units and \(x=25\) units</span> (profit is positive between them).</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Total cost = fixed cost + (variable cost per unit)·x; revenue \(R=p\cdot x\).</li>
<li>Break-even point: \(R(x)=C(x)\) (profit zero).</li></ul>"""),

        Q("20", 2, r"""<p>The activity department of The Heritage School of Kolkata is organising an Art and Craft exhibition cum sale to promote the
talented and gifted students at the school. The school want to charge a nominal amount as entry fee. Profit, in rupees, generated by
the entry tickets can be calculated using the function \(P(x)=-8x^3+29400x-60000\) where \(x\) is the price of each ticket. What is the
ideal price for each ticket that the department of the school set to maximise the profitability from the entry tickets.</p>""",
          a=r"""<p>\(P'(x)=-24x^2+29400=0\Rightarrow x^2=1225\Rightarrow x=35\) (\(x\gt 0\)).</p>
<p>\(P''(x)=-48x\); \(P''(35)=-1680\lt 0\): maximum.</p>
<p><span class="box">Ideal ticket price ₹35</span> (maximum profit \(P(35)=₹6{,}26{,}000\)).</p>""",
          topic="Applications of Derivatives (maxima and minima)",
          recall=r"""<ul><li>Maximum: \(P'(x)=0\) and \(P''(x)\lt 0\).</li></ul>"""),

        Q("20 (OR)", 2, r"""<p>A person runs a company that produces and sells a particular model of laptop. If demand function of the company is given by
\(x=80-4p\), where \(x\) is the number of units produced and sold and \(p\) is the price per unit then find the value of \(x\) for which the
revenue is maximum.</p>""",
          a=r"""<p>\(p=\dfrac{80-x}{4}\); revenue \(R=px=\dfrac{80x-x^2}{4}\).</p>
<p>\(\dfrac{dR}{dx}=\dfrac{80-2x}{4}=0\Rightarrow x=40\); \(\dfrac{d^2R}{dx^2}=-\dfrac12\lt 0\): maximum.</p>
<p><span class="box">\(x=40\) units</span> (at price \(p=10\), \(R_{\max}=400\)).</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Write p in terms of x, then \(R=px\).</li>
<li>Revenue is maximum where marginal revenue \(\frac{dR}{dx}=0\) and \(\frac{d^2R}{dx^2}\lt 0\).</li></ul>"""),

        Q("21", 4, r"""<p>A study was conducted to investigate the relationship between the number of hours \((X)\) that a student studies per week and their
scores of Mathematics \((Y)\) in Board examination by the evaluation department of Council for the Indian School Certificate Examination.
The following statistical data was collected from a sample of 50 students.</p>
<table class="data"><tr><th></th><th>X</th><th>Y</th></tr>
<tr><th>MEAN</th><td>15</td><td>75</td></tr><tr><th>STANDARD DEVIATION</th><td>4</td><td>10</td></tr></table>
<p>The correlation between X and Y is 0·65.</p>
<p>(a) Estimate the test scores for students who studies 20 hours per week.<br>
(b) If the pass marks in is 35 then how many hours must a student need to study to pass the Mathematics paper.</p>""",
          excluded=REGR.format("regression estimates")),

        Q("21 (OR)", 4, r"""<p>A renowned Multiplex in Kolkata conducts survey in which they need to significantly reduce the price of popcorn as they believe
their customers spend more time on aeriated drinks rather they buy popcorn. They recorded the following data of the daily revenue from
popcorn \(x\) and daily revenue from aeriated drinks \(y\) over 8 randomly selected days.</p>
<table class="data"><tr><th>Popcorn Revenue \(x\)</th><td>14</td><td>12</td><td>13</td><td>14</td><td>16</td><td>10</td><td>13</td><td>12</td></tr>
<tr><th>Aeriated Drinks revenue \(y\)</th><td>22</td><td>23</td><td>17</td><td>24</td><td>18</td><td>25</td><td>23</td><td>24</td></tr></table>
<p>(a) Find \(\bar x\) and \(\bar y\).<br>(b) Using \(\bar x\) and \(\bar y\) find the regression coefficient of \(y\) on \(x\).<br>
(c) Find the regression equation of \(y\) on \(x\) in the form \(y=a+bx\). Hence calculate the value of \(a\) and \(b\).</p>""",
          excluded=REGR.format("regression equation from data")),

        Q("22", 4, r"""<p>Indicate clearly on a graph the region satisfying the constraints \(x+y\le70\), \(x+2y\le100\), \(2x+y\le120\), \(x\le0\), \(y\le0\).
Hence Maximize the function \(5x+7y\).</p>
<p>[Use graph paper for the above question]</p>
<p class="note">[The non-negativity constraints are misprinted as \(x\le0,\ y\le0\); with them the region is the whole third quadrant and
\(5x+7y\) has its maximum 0 at the origin. The intended constraints \(x\ge0,\ y\ge0\) are solved below.]</p>""",
          a=r"""<p>Maximise \(Z=5x+7y\) subject to \(x+y\le70\), \(x+2y\le100\), \(2x+y\le120\), \(x\ge0,\ y\ge0\).</p>
<p>Lines: \(x+y=70\): (70, 0), (0, 70); \(x+2y=100\): (100, 0), (0, 50); \(2x+y=120\): (60, 0), (0, 120).
O satisfies all three inequalities, so the region is on the origin side of each line.</p>
<p>Corners: O(0, 0); A(60, 0); B: \(2x+y=120,\ x+y=70\Rightarrow x=50,\ y=20\); C: \(x+y=70,\ x+2y=100\Rightarrow y=30,\ x=40\); D(0, 50).</p>
{{fig:0}}
<table class="data"><tr><th>Corner</th><td>O(0, 0)</td><td>A(60, 0)</td><td>B(50, 20)</td><td>C(40, 30)</td><td>D(0, 50)</td></tr>
<tr><th>Z = 5x + 7y</th><td>0</td><td>300</td><td>390</td><td><b>410</b></td><td>350</td></tr></table>
<p>The feasible region is bounded, so the maximum is at a corner:</p>
<p><span class="box">\(Z_{\max}=410\) at \(x=40,\ y=30\)</span></p>""",
          afig=[(F.fig_q22_lpp, "Feasible region OABCD; the dashed line 5x + 7y = 410 touches it only at C(40, 30).")],
          topic="Linear Programming",
          recall=r"""<ul><li>Plot each line by its intercepts; shade the side containing O for “≤”.</li>
<li>Bounded region: evaluate Z at every corner point (corner-point method).</li></ul>"""),
    ])
