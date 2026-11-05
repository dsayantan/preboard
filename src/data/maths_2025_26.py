"""Heritage School Pre-Board 2025-26, Mathematics (Class XII).  Transcribed from the page images."""
from kit import Q, SEC
import maths_2025_26_figs as F

COMMERCE = ("Commerce application without calculus ({}) — not in the ISC 2027 Class XII syllabus; of the old "
            "Section C only Linear Programming (and calculus applications) remain.")
REGR = ("Correlation and regression ({}) — dropped from ISC Mathematics; not in any of the seven ISC 2027 "
        "Class XII units.")

AR = r"""<p>(a) Both Assertion (A) &amp; Reason (R) are true &amp; Reason (R) is the correct explanation for Assertion (A).<br>
(b) Both Assertion (A) &amp; Reason (R) are true but Reason (R) is not the correct explanation for Assertion (A).<br>
(c) Assertion is true and Reason is false.<br>
(d) Assertion is false and Reason is true.</p>"""

PAPER = dict(
    subject="maths",
    year="2025-26",
    slug="2025-26",
    paper="Mathematics (Class XII)",
    source="PreBoard-PYQ/2025-26/SET-1/MATHEMATICS.pdf",
    marks=80, time="3 hours",
    intro=r"""<p>You are allowed an additional 15 minutes for only reading the paper.</p>
<ul><li>You must NOT start writing during reading time.</li>
<li>The question paper has 7 printed pages.</li>
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
3-D Geometry (this paper's Section B) and Linear Programming (Q22 here) are compulsory. Of the rest of
Section C, the questions whose mathematics is differentiation (marginal revenue, average cost) or solving a
given function equation (break-even) are answered as Applications of Derivatives / functions; regression and the
non-calculus cost-function item have left the syllabus.</p>""",
    items=[
        SEC("Section A – 65 Marks [Compulsory Section]",
            "1. In subparts (i) to (xi) choose the correct options and in subparts (xii) to (xv), answer the questions as instructed. [15]"),

        # ---------------------------------------------------------------- Question 1
        Q("1(i)", 1, r"""<p>Let R be a relation on N, set of all natural given by R = {(a, b): a – b = 2} then</p>
<p>(a) (2, 4) ∈ R &emsp; (b) (10, 8) ∈ R &emsp; (c) (6, 8) ∈ R &emsp; (d) (8, 7) ∈ R</p>""",
          a=r"""<p>Test \(a-b=2\) for each pair: \(2-4=-2\), \(10-8=2\) ✓, \(6-8=-2\), \(8-7=1\).</p>
<p><span class="box">(b) \((10, 8)\in R\)</span></p>""",
          topic="Relations and Functions",
          recall=r"""<ul><li>\((a,b)\in R\) means the pair satisfies the defining rule, in that order.</li></ul>"""),

        Q("1(ii)", 1, r"""<p>If \(A=\begin{bmatrix}a&0&0\\0&a&0\\0&0&a\end{bmatrix}\) then \(A^n\) equals to</p>
<p>(a) \(\begin{bmatrix}a^n&0&0\\0&a^n&0\\0&0&a^n\end{bmatrix}\) &emsp;
(b) \(\begin{bmatrix}a&0&0\\0&a^n&0\\0&0&a\end{bmatrix}\) &emsp;
(c) \(\begin{bmatrix}a^n&0&0\\0&a&0\\0&0&a^n\end{bmatrix}\) &emsp;
(d) \(\begin{bmatrix}na&0&0\\0&na&0\\0&0&a^n\end{bmatrix}\)</p>""",
          a=r"""<p>\(A=aI\) is a scalar matrix, so \(A^n=a^nI^n=a^nI\).</p>
<p><span class="box">(a) \(\begin{bmatrix}a^n&0&0\\0&a^n&0\\0&0&a^n\end{bmatrix}\)</span></p>""",
          topic="Matrices",
          recall=r"""<ul><li>Powers of a diagonal matrix: raise each diagonal entry to that power.</li>
<li>\(I^n=I\).</li></ul>"""),

        Q("1(iii)", 1, r"""<p>If m and n are respectively the order and degree of the differential equation
\(\dfrac{d}{dx}\left(\dfrac{dy}{dx}\right)^3=0\), then the value of \((m-n)\) is</p>
<p>(a) 0 &emsp; (b) 1 &emsp; (c) 2 &emsp; (d) 3</p>""",
          a=r"""<p>Carry out the differentiation first: \(\dfrac{d}{dx}\left(\dfrac{dy}{dx}\right)^3=3\left(\dfrac{dy}{dx}\right)^2\dfrac{d^2y}{dx^2}=0\).</p>
<p>Highest derivative \(\dfrac{d^2y}{dx^2}\): order \(m=2\); its power is 1: degree \(n=1\). So \(m-n=1\).</p>
<p><span class="box">(b) 1</span></p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Order = order of the highest derivative; degree = its power once the equation is a polynomial in the derivatives.</li>
<li>Write the equation out (perform the indicated differentiation) before reading off order and degree.</li></ul>"""),

        Q("1(iv)", 1, r"""<p>If \(x^2+y^3=42\) then \(\dfrac{dy}{dx}\) is</p>
<p>(a) \(\dfrac{dy}{dx}=\dfrac{-3y^2}{2x}\) &emsp; (b) \(\dfrac{dy}{dx}=\dfrac{3y^2}{2x}\) &emsp;
(c) \(\dfrac{dy}{dx}=\dfrac{2x}{3y^2}\) &emsp; (d) \(\dfrac{dy}{dx}=\dfrac{-2x}{3y^2}\)</p>""",
          a=r"""<p>Differentiate implicitly: \(2x+3y^2\dfrac{dy}{dx}=0\Rightarrow\dfrac{dy}{dx}=-\dfrac{2x}{3y^2}\).</p>
<p><span class="box">(d)</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Implicit differentiation: \(\frac{d}{dx}(y^n)=ny^{n-1}\frac{dy}{dx}\).</li></ul>"""),

        Q("1(v)", 1, r"""<p><b>Assertion (A)</b>: If A is a skew symmetric matrix of order 3×3, then \(|A|=0\)<br>
<b>Reason (R)</b>: If A is a square matrix then \(|A|=|A'|\)</p>""" + AR,
          a=r"""<p>For skew-symmetric \(A\), \(A'=-A\). Using R: \(|A|=|A'|=|-A|=(-1)^3|A|=-|A|\), so \(2|A|=0\), \(|A|=0\).
A is true, R is true, and R is exactly the property that proves A.</p>
<p><span class="box">(a)</span></p>""",
          topic="Determinants",
          recall=r"""<ul><li>\(|A'|=|A|\); \(|kA|=k^n|A|\) for order \(n\).</li>
<li>A skew-symmetric matrix of odd order has determinant 0.</li></ul>"""),

        Q("1(vi)", 1, r"""<p><b>Statement I</b>: If A and B are independent events such that P(A) = 0.4, P(B) = p and
P(A ∪ B) = 0.8 then \(p=\tfrac23\).<br>
<b>Statement II</b>: For two independent events A and B, P(A ∪ B) = P(A) + P(B)</p>
<p>(a) Both the statements are true.<br>(b) Both the statements are false.<br>
(c) Statement I is true, and Statement II is false.<br>(d) Statement I is false, and Statement II is true.</p>""",
          a=r"""<p>\(P(A\cup B)=P(A)+P(B)-P(A)P(B)\Rightarrow 0.8=0.4+p-0.4p\Rightarrow0.6p=0.4\Rightarrow p=\tfrac23\). Statement I is true.</p>
<p>Statement II drops the term \(P(A)P(B)\); it holds only for mutually exclusive events. False.</p>
<p><span class="box">(c)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Independent: \(P(A\cap B)=P(A)P(B)\).</li>
<li>Addition theorem: \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\).</li></ul>"""),

        Q("1(vii)", 1, r"""<p>The expression for \(\cos(\tan^{-1}x)\) is equal to</p>
<p>(a) \(\dfrac{1}{\sqrt{1-x^2}}\) &emsp; (b) \(\dfrac{1}{\sqrt{1+x^2}}\) &emsp; (c) \(\dfrac{\sqrt{1-x^2}}{2}\) &emsp; (d) \(\sqrt{1-x^2}\)</p>""",
          a=r"""<p>Let \(\theta=\tan^{-1}x\in(-\tfrac\pi2,\tfrac\pi2)\), so \(\cos\theta\gt 0\) and \(\sec^2\theta=1+x^2\). Hence \(\cos\theta=\dfrac{1}{\sqrt{1+x^2}}\).</p>
<p><span class="box">(b)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>Range of \(\tan^{-1}\) is \((-\frac\pi2,\frac\pi2)\), where cosine is positive.</li>
<li>Right triangle with opposite \(x\), adjacent 1, hypotenuse \(\sqrt{1+x^2}\).</li></ul>"""),

        Q("1(viii)", 1, r"""<p>If \(D=\begin{vmatrix}p&p&p\\p&p+x&p\\p&p&p+y\end{vmatrix}\) for \(p\ne0,\ x\ne0,\ y\ne0\) then D is divisible by</p>
<p>(a) only p &emsp; (b) p &amp; x but not y &emsp; (c) p &amp; y but not x &emsp; (d) p, x &amp; y</p>""",
          a=r"""<p>\(R_2\to R_2-R_1,\ R_3\to R_3-R_1\): \(D=\begin{vmatrix}p&p&p\\0&x&0\\0&0&y\end{vmatrix}=pxy\) (upper triangular).</p>
<p><span class="box">(d) p, x &amp; y</span></p>""",
          topic="Determinants",
          recall=r"""<ul><li>Subtracting a multiple of one row from another leaves the determinant unchanged.</li>
<li>Triangular determinant = product of the diagonal entries.</li></ul>"""),

        Q("1(ix)", 1, r"""<p>If \(\displaystyle\int\frac{2-x}{(x-1)^2}e^x\,dx=e^xf(x)+C\), then f(x) will be</p>
<p>(a) \(\dfrac{1}{x-1}\) &emsp; (b) \(\dfrac{1}{2-x}\) &emsp; (c) \(\dfrac{1}{3-x}\) &emsp; (d) \(\dfrac{1}{1-x}\)</p>
<p class="note">[The paper prints “If f(x) = ∫ …”; the leading “f(x) =” is a misprint and is ignored.]</p>""",
          a=r"""<p>Split: \(\dfrac{2-x}{(x-1)^2}=\dfrac{1-(x-1)}{(x-1)^2}=\dfrac{1}{1-x}+\dfrac{1}{(1-x)^2}\).</p>
<p>With \(f(x)=\dfrac1{1-x}\), \(f'(x)=\dfrac1{(1-x)^2}\), so the integrand is \(e^x[f(x)+f'(x)]\) and
\(\int e^x[f+f']\,dx=e^xf(x)+C\).</p>
<p><span class="box">(d) \(\dfrac{1}{1-x}\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int e^x[f(x)+f'(x)]\,dx=e^xf(x)+C\).</li>
<li>Rewrite the numerator in terms of the bracket in the denominator.</li></ul>"""),

        Q("1(x)", 1, r"""<p><b>Assertion (A)</b>: The curve in the graph below is not a one-one function</p>
{{fig:0}}
<p><b>Reason (R)</b>: If any straight line parallel to y-axis does not cut the curve at more than one point, then
that curve represents a function.</p>""" + AR,
          qfig=F.fig_q1x_curve,
          a=r"""<p>A: a horizontal line \(y=k\) with \(k\) between the height of the right-hand dip and the lower hump cuts the curve at four points
(even a line just above the x-axis cuts it at three, on both sides of the cusp at O), so different \(x\) give the
same value — the function is not one-one. A is true. {{fig:0}}</p>
<p>R is the vertical-line test for a <em>function</em>; it is true, but it tells us the curve is a function,
not whether it is one-one (that is the horizontal-line test).</p>
<p><span class="box">(b)</span></p>""",
          afig=[(F.fig_q1x_ans, "A horizontal line meets the graph in four points.")],
          topic="Relations and Functions",
          recall=r"""<ul><li>Vertical-line test: a graph is a function.</li>
<li>Horizontal-line test: a function is one-one.</li></ul>"""),

        Q("1(xi)", 1, r"""<p>The function \(f(x)=7+x-e^x\) is strictly increasing in the interval</p>
<p>(a) \((1,\infty)\) &emsp; (b) \((-\infty,1)\) &emsp; (c) \((0,\infty)\) &emsp; (d) \((-\infty,0)\)</p>""",
          a=r"""<p>\(f'(x)=1-e^x\gt 0\iff e^x\lt 1\iff x\lt 0\).</p>
<p><span class="box">(d) \((-\infty,0)\)</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Strictly increasing where \(f'(x)\gt 0\).</li><li>\(e^x\) is increasing, \(e^0=1\).</li></ul>"""),

        Q("1(xii)", 1, r"""<p>If a relation R on the set \(\{a,b,c\}\) defined by R = {(b, b)}, then classify the relation.</p>""",
          a=r"""<p><b>Reflexive?</b> No: \((a,a)\notin R\) (and \((c,c)\notin R\)).</p>
<p><b>Symmetric?</b> Yes: the only pair \((b,b)\) is its own reverse.</p>
<p><b>Transitive?</b> Yes: the only chain is \((b,b),(b,b)\Rightarrow(b,b)\in R\).</p>
<p><span class="box">R is symmetric and transitive but not reflexive (so not an equivalence relation).</span></p>""",
          topic="Relations and Functions",
          recall=r"""<ul><li>Reflexive needs \((x,x)\) for <em>every</em> element of the set.</li>
<li>Symmetric/transitive are “if … then” conditions — satisfied vacuously when no pair breaks them.</li></ul>"""),

        Q("1(xiii)", 1, r"""<p>Find the principal values of \(\cos^{-1}\left(\sin\dfrac{10\pi}{7}\right)\)</p>""",
          a=r"""<p>\(\sin\dfrac{10\pi}{7}=\sin\left(\pi+\dfrac{3\pi}{7}\right)=-\sin\dfrac{3\pi}{7}=-\cos\left(\dfrac\pi2-\dfrac{3\pi}{7}\right)=-\cos\dfrac{\pi}{14}=\cos\left(\pi-\dfrac{\pi}{14}\right)=\cos\dfrac{13\pi}{14}.\)</p>
<p>Since \(\dfrac{13\pi}{14}\in[0,\pi]\), the principal value branch of \(\cos^{-1}\):</p>
<p><span class="box">\(\cos^{-1}\left(\sin\dfrac{10\pi}{7}\right)=\dfrac{13\pi}{14}\)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>Principal range of \(\cos^{-1}\): \([0,\pi]\).</li>
<li>\(\cos^{-1}(\cos\theta)=\theta\) only when \(\theta\in[0,\pi]\); first rewrite the sine as a cosine of an angle in that range.</li></ul>"""),

        Q("1(xiv)", 1, r"""<p>Find the number of point(s) at which the function \(f(x)=\dfrac{1}{[x]-x}\) is discontinuous.</p>""",
          a=r"""<p>\([x]-x=-\{x\}\), which is 0 exactly when \(x\) is an integer. So \(f\) is not defined — hence
discontinuous — at every integer; between consecutive integers \([x]\) is constant and \(f(x)=\dfrac{1}{k-x}\) is continuous.</p>
<p class="note">The question intends the usual answer “at every integer”. (Under the strict NCERT convention, continuity is
judged only at points of the domain, \(\mathbb R\setminus\mathbb Z\), where f is continuous; the integers are then points
where f is not defined. Either way the trouble points are exactly the integers.)</p>
<p><span class="box">Infinitely many points: every integer \(x\in\mathbb Z\).</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>\([x]\) is constant on \([k,k+1)\) and jumps at each integer.</li>
<li>A quotient is discontinuous where its denominator vanishes.</li></ul>"""),

        Q("1(xv)", 1, r"""<p>A company has estimated that the probabilities of success for three products introduced in the market
are 1/3, 2/5 and 2/3 respectively. Assuming independence, find the probability that at least one product is
successful.</p>""",
          a=r"""<p>P(none succeeds) \(=\left(1-\tfrac13\right)\left(1-\tfrac25\right)\left(1-\tfrac23\right)=\tfrac23\cdot\tfrac35\cdot\tfrac13=\tfrac{2}{15}\).</p>
<p>P(at least one) \(=1-\tfrac2{15}\) = <span class="box">\(\dfrac{13}{15}\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>P(at least one) = 1 − P(none).</li>
<li>Complements of independent events are independent.</li></ul>"""),

        # ---------------------------------------------------------------- 2–6 (2 marks)
        Q("2", 2, r"""<p>If \(x^y=y^x\), find \(\dfrac{dy}{dx}\)</p>""",
          a=r"""<p>Take logs: \(y\log x=x\log y\).</p>
<p>Differentiate w.r.t. \(x\): \(\dfrac{dy}{dx}\log x+\dfrac yx=\log y+\dfrac xy\dfrac{dy}{dx}\).</p>
<p>\(\dfrac{dy}{dx}\left(\log x-\dfrac xy\right)=\log y-\dfrac yx\)</p>
<p><span class="box">\(\dfrac{dy}{dx}=\dfrac{\log y-\frac yx}{\log x-\frac xy}=\dfrac{y(x\log y-y)}{x(y\log x-x)}\)</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Logarithmic differentiation for variable powers \(u^v\).</li>
<li>Product rule on \(y\log x\).</li></ul>"""),

        Q("2 (OR)", 2, r"""<p>Find the values of a for which \(f(x)=b-ax+\sin x\) is increasing on R.</p>""",
          a=r"""<p>\(f'(x)=-a+\cos x\). For \(f\) increasing on R we need \(f'(x)\ge0\) for all \(x\), i.e.
\(\cos x\ge a\) for all \(x\).</p>
<p>The least value of \(\cos x\) is \(-1\), so \(a\le-1\). (At \(a=-1\), \(f'(x)=1+\cos x\ge0\) and vanishes only at
isolated points \(x=(2k+1)\pi\), so \(f\) is still strictly increasing; some keys print \(a\lt -1\), which omits this valid endpoint.)</p>
<p><span class="box">\(a\le-1\), i.e. \(a\in(-\infty,-1]\)</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Increasing on R: \(f'(x)\ge0\) for all \(x\), zero only at isolated points.</li>
<li>\(-1\le\cos x\le1\).</li></ul>"""),

        Q("3", 2, r"""<p>If the matrix \(\begin{bmatrix}6&-x^2\\2x-15&10\end{bmatrix}\) is symmetric, find the value(s) of x.</p>""",
          a=r"""<p>Symmetric \(\Rightarrow A'=A\Rightarrow a_{12}=a_{21}\): \(-x^2=2x-15\Rightarrow x^2+2x-15=0\Rightarrow(x+5)(x-3)=0\).</p>
<p><span class="box">\(x=3\) or \(x=-5\)</span></p>""",
          topic="Matrices",
          recall=r"""<ul><li>Symmetric: \(a_{ij}=a_{ji}\) for all \(i,j\).</li></ul>"""),

        Q("4", 2, r"""<p>During the annual science fair, students create an online poster presentation. The number of views
increases with time and the popularity of the poster is modelled by \(P(t)=\tan^{-1}\dfrac{t}{10}\) where t is the number of
hours since the poster was uploaded. If one student checks the poster after 6 hours and another after 8
hours, find the sum of the popularity scores.</p>""",
          a=r"""<p>\(P(6)+P(8)=\tan^{-1}\dfrac{6}{10}+\tan^{-1}\dfrac{8}{10}=\tan^{-1}\dfrac35+\tan^{-1}\dfrac45\).</p>
<p>Since \(\dfrac35\cdot\dfrac45=\dfrac{12}{25}\lt 1\):</p>
<p>\[\tan^{-1}\frac35+\tan^{-1}\frac45=\tan^{-1}\frac{\frac35+\frac45}{1-\frac{12}{25}}=\tan^{-1}\frac{\frac75}{\frac{13}{25}}=\tan^{-1}\frac{35}{13}.\]</p>
<p><span class="box">Sum of popularity scores \(=\tan^{-1}\dfrac{35}{13}\)</span> (≈ 1.215 rad)</p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>\(\tan^{-1}x+\tan^{-1}y=\tan^{-1}\dfrac{x+y}{1-xy}\) when \(xy\lt 1\).</li></ul>"""),

        Q("5", 2, r"""<p>Evaluate: \(\displaystyle\int_0^5\frac{\sqrt x}{\sqrt{5-x}-\sqrt x}\,dx\)</p>
<p class="note">[As printed (confirmed at 400 dpi) the denominator has a minus sign; it vanishes at \(x=\tfrac52\) and the integral diverges.
The intended integrand is evidently \(\dfrac{\sqrt x}{\sqrt{5-x}+\sqrt x}\), the standard \(\int_0^af(a-x)\) question; that is solved.]</p>""",
          a=r"""<p>Let \(I=\displaystyle\int_0^5\frac{\sqrt x}{\sqrt{5-x}+\sqrt x}\,dx\). (1)</p>
<p>Using \(\int_0^af(x)\,dx=\int_0^af(a-x)\,dx\) with \(a=5\):
\(I=\displaystyle\int_0^5\frac{\sqrt{5-x}}{\sqrt x+\sqrt{5-x}}\,dx\). (2)</p>
<p>Adding (1) and (2): \(2I=\displaystyle\int_0^5 1\,dx=5\).</p>
<p><span class="box">\(I=\dfrac52\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int_0^af(x)\,dx=\int_0^af(a-x)\,dx\).</li>
<li>Add the two forms so the numerators combine into the denominator.</li></ul>"""),

        Q("5 (OR)", 2, r"""<p>Evaluate: \(\displaystyle\int e^x\operatorname{cosec}x(1-\cot x)\,dx\)</p>""",
          a=r"""<p>\(I=\int e^x(\operatorname{cosec}x-\operatorname{cosec}x\cot x)\,dx\).</p>
<p>With \(f(x)=\operatorname{cosec}x\), \(f'(x)=-\operatorname{cosec}x\cot x\), so the integrand is \(e^x[f(x)+f'(x)]\).</p>
<p><span class="box">\(I=e^x\operatorname{cosec}x+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int e^x[f(x)+f'(x)]\,dx=e^xf(x)+C\).</li>
<li>\(\frac{d}{dx}\operatorname{cosec}x=-\operatorname{cosec}x\cot x\).</li></ul>"""),

        Q("6", 2, r"""<p>Find the equation of the tangent at (0, 0) to the curve \(y=4x^2-2x^3\)</p>""",
          a=r"""<p>\(\dfrac{dy}{dx}=8x-6x^2\); at \((0,0)\) the slope is \(0\).</p>
<p>Tangent: \(y-0=0(x-0)\) — <span class="box">\(y=0\)</span> (the x-axis).</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Tangent at \((x_1,y_1)\): \(y-y_1=\left(\frac{dy}{dx}\right)_{(x_1,y_1)}(x-x_1)\).</li></ul>"""),

        # ---------------------------------------------------------------- 7–10 (4 marks)
        Q("7", 4, r"""<p>Prove that \(\cos[\tan^{-1}\{\cot(\sin^{-1}x)\}]=x\).</p>""",
          a=r"""<p>Let \(\sin^{-1}x=\theta\), so \(x=\sin\theta\). For the identity take \(0\lt x\le1\), i.e. \(\theta\in(0,\tfrac\pi2]\)
(see the note below).</p>
<p>Then \(\cot\theta=\tan\left(\dfrac\pi2-\theta\right)\), and \(\dfrac\pi2-\theta\in[0,\tfrac\pi2)\) lies in the principal range of \(\tan^{-1}\):</p>
<p>\[\tan^{-1}\{\cot(\sin^{-1}x)\}=\tan^{-1}\left\{\tan\left(\frac\pi2-\theta\right)\right\}=\frac\pi2-\theta.\]</p>
<p>\[\therefore\ \cos[\tan^{-1}\{\cot(\sin^{-1}x)\}]=\cos\left(\frac\pi2-\theta\right)=\sin\theta=x.\]</p>
<p><span class="box">\(\cos[\tan^{-1}\{\cot(\sin^{-1}x)\}]=x\)</span> &nbsp;Hence proved.</p>
<p><b>Alternative (triangle):</b> \(\cot\theta=\dfrac{\sqrt{1-x^2}}{x}\); \(\tan^{-1}\dfrac{\sqrt{1-x^2}}{x}=\phi\) gives
\(\tan\phi=\dfrac{\sqrt{1-x^2}}{x}\), hypotenuse 1, so \(\cos\phi=x\).</p>
<p class="note">Note: the identity holds for \(0&lt;x\le1\). For \(-1\le x&lt;0\) the left side equals \(-x\)
(e.g. \(x=-\tfrac12\): \(\cot(-\tfrac\pi6)=-\sqrt3\), \(\tan^{-1}(-\sqrt3)=-\tfrac\pi3\), \(\cos(-\tfrac\pi3)=\tfrac12\)), and at \(x=0\) cot is undefined.</p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>\(\cot\theta=\tan(\frac\pi2-\theta)\).</li>
<li>\(\tan^{-1}(\tan\alpha)=\alpha\) only for \(\alpha\in(-\frac\pi2,\frac\pi2)\).</li>
<li>\(\cos(\frac\pi2-\theta)=\sin\theta\).</li></ul>"""),

        Q("8", 4, r"""<p>If \(y=\left(x+\sqrt{a^2+x^2}\right)^m\), prove that \((a^2+x^2)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}-m^2y=0\)</p>""",
          a=r"""<p>\[\frac{dy}{dx}=m\left(x+\sqrt{a^2+x^2}\right)^{m-1}\left(1+\frac{x}{\sqrt{a^2+x^2}}\right)
=m\left(x+\sqrt{a^2+x^2}\right)^{m-1}\cdot\frac{\sqrt{a^2+x^2}+x}{\sqrt{a^2+x^2}}=\frac{my}{\sqrt{a^2+x^2}}.\]</p>
<p>So \(\sqrt{a^2+x^2}\,y_1=my\). Squaring: \((a^2+x^2)y_1^2=m^2y^2\).</p>
<p>Differentiate w.r.t. \(x\): \(2xy_1^2+(a^2+x^2)\cdot2y_1y_2=m^2\cdot2yy_1\).</p>
<p>Divide by \(2y_1\) (\(y_1\ne0\)): \((a^2+x^2)y_2+xy_1=m^2y\).</p>
<p><span class="box">\((a^2+x^2)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}-m^2y=0\)</span> &nbsp;Hence proved.</p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Chain rule; \(\frac{d}{dx}\sqrt{a^2+x^2}=\frac{x}{\sqrt{a^2+x^2}}\).</li>
<li>Square to remove the root before differentiating a second time.</li></ul>"""),

        Q("8 (OR)", 4, r"""<p>In a particular forest, the population density (P) of wild animals (in thousands of animals per sq km)
at a distance of ‘r’ km from the centre of the forest is approximately given by \(P=10+20r-10r^2\).</p>
<p>a) What is the population density in the centre of the forest?<br>
b) Calculate the rate of change of population density.<br>
c) For what value of r, is the population density maximum?</p>""",
          a=r"""<p>(a) Centre: \(r=0\Rightarrow P=10\). <span class="box">10 thousand animals per sq km</span></p>
<p>(b) <span class="box">\(\dfrac{dP}{dr}=20-20r\)</span> thousand animals per sq km per km.</p>
<p>(c) \(\dfrac{dP}{dr}=0\Rightarrow r=1\). \(\dfrac{d^2P}{dr^2}=-20\lt 0\), so P is maximum at \(r=1\).</p>
<p><span class="box">\(r=1\) km</span>, where \(P_{\max}=10+20-10=20\) thousand per sq km.</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Rate of change of P with respect to r is \(dP/dr\).</li>
<li>Second-derivative test: \(f'(c)=0,\ f''(c)\lt 0\Rightarrow\) local maximum.</li></ul>"""),

        Q("9", 4, r"""<p>Evaluate: \(\displaystyle\int\frac{\cos^{-1}x}{x^2}\,dx\)</p>""",
          a=r"""<p>By parts with \(u=\cos^{-1}x\), \(dv=x^{-2}dx\): \(du=-\dfrac{dx}{\sqrt{1-x^2}}\), \(v=-\dfrac1x\).</p>
<p>\[I=-\frac{\cos^{-1}x}{x}-\int\left(-\frac1x\right)\left(-\frac{1}{\sqrt{1-x^2}}\right)dx=-\frac{\cos^{-1}x}{x}-\int\frac{dx}{x\sqrt{1-x^2}}.\]</p>
<p>For \(J=\int\dfrac{dx}{x\sqrt{1-x^2}}\) put \(1-x^2=t^2\): \(x\,dx=-t\,dt\), so
\(J=\int\dfrac{x\,dx}{x^2\sqrt{1-x^2}}=\int\dfrac{-t\,dt}{(1-t^2)t}=-\int\dfrac{dt}{1-t^2}=-\dfrac12\log\left|\dfrac{1+t}{1-t}\right|\).</p>
<p>Since \(\dfrac{1+t}{1-t}=\dfrac{(1+t)^2}{1-t^2}=\dfrac{(1+t)^2}{x^2}\), \(J=-\log\left|\dfrac{1+\sqrt{1-x^2}}{x}\right|\).</p>
<p><span class="box">\(\displaystyle\int\frac{\cos^{-1}x}{x^2}\,dx=-\frac{\cos^{-1}x}{x}+\log\left|\frac{1+\sqrt{1-x^2}}{x}\right|+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>By parts \(\int u\,dv=uv-\int v\,du\); take the inverse-trig function as \(u\) (ILATE).</li>
<li>\(\frac{d}{dx}\cos^{-1}x=-\frac{1}{\sqrt{1-x^2}}\).</li>
<li>\(\int\frac{dt}{1-t^2}=\frac12\log\left|\frac{1+t}{1-t}\right|\).</li></ul>"""),

        Q("10", 4, r"""<p>A school offers its students, three modes for attending classes:</p>
<ul><li>Mode A: Offline (in-person) – 40% of students</li><li>Mode B: Online (live virtual classes) – 35% of students</li>
<li>Mode C: Recorded lectures – 25% of students</li></ul>
<p>After a feedback survey: • 20% of students from Mode A reported the class as “Excellent” • 30% from Mode B rated it
as “Excellent” • 50% from Mode C rated it as “Excellent”</p>
<p>A student is selected at random, and it is found that he rated the class as “Excellent.” Using Bayes’
Theorem, find the probability that the student attended the Recorded lectures (Mode C).</p>""",
          a=r"""<p>Let \(E_1,E_2,E_3\): student attended Mode A, B, C; \(E\): rated “Excellent”.</p>
<p>\(P(E_1)=0.40,\ P(E_2)=0.35,\ P(E_3)=0.25\); \(P(E|E_1)=0.20,\ P(E|E_2)=0.30,\ P(E|E_3)=0.50\).</p>
{{fig:0}}
<p>By the theorem of total probability, \(P(E)=0.40(0.20)+0.35(0.30)+0.25(0.50)=0.08+0.105+0.125=0.31\).</p>
<p>By Bayes’ theorem:</p>
<p>\[P(E_3|E)=\frac{P(E_3)P(E|E_3)}{\sum P(E_i)P(E|E_i)}=\frac{0.125}{0.31}=\frac{25}{62}.\]</p>
<p><span class="box">\(P(\text{Mode C}\mid\text{Excellent})=\dfrac{25}{62}\approx0.403\)</span></p>""",
          afig=[F.fig_q10_tree],
          topic="Probability",
          recall=r"""<ul><li>Total probability: \(P(E)=\sum P(E_i)P(E|E_i)\) over a partition.</li>
<li>Bayes: \(P(E_k|E)=\dfrac{P(E_k)P(E|E_k)}{\sum P(E_i)P(E|E_i)}\).</li></ul>"""),

        Q("10 (OR)", 4, r"""<p>A problem in mathematics is given to three students A, B and C. Their chances of solving the problem
are \(\tfrac12,\tfrac13\) and \(\tfrac14\) respectively. Find the probability that</p>
<p>i) Exactly two of them can solve the problem.<br>ii) the problem is solved</p>""",
          a=r"""<p>\(P(A)=\tfrac12,\ P(B)=\tfrac13,\ P(C)=\tfrac14\); \(P(\bar A)=\tfrac12,\ P(\bar B)=\tfrac23,\ P(\bar C)=\tfrac34\); independent.</p>
<p>(i) \(P(AB\bar C)+P(A\bar BC)+P(\bar ABC)=\tfrac12\cdot\tfrac13\cdot\tfrac34+\tfrac12\cdot\tfrac23\cdot\tfrac14+\tfrac12\cdot\tfrac13\cdot\tfrac14
=\tfrac{3}{24}+\tfrac{2}{24}+\tfrac{1}{24}=\tfrac{6}{24}\) = <span class="box">\(\dfrac14\)</span></p>
<p>(ii) Solved \(=1-P(\bar A\bar B\bar C)=1-\tfrac12\cdot\tfrac23\cdot\tfrac34=1-\tfrac14\) = <span class="box">\(\dfrac34\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Multiplication theorem for independent events.</li>
<li>“Exactly two” = sum of three mutually exclusive cases; “solved” = 1 − nobody solves.</li></ul>"""),

        # ---------------------------------------------------------------- 11–14 (6 marks)
        Q("11", 6, r"""<p>A furniture factory uses three types of wood namely, teakwood, rosewood and satinwood for
manufacturing three types of furniture, that are, table, chair and cot. The wood requirements (in tonnes) for
each type of furniture are given below:</p>
<table class="data"><tr><th></th><th>TABLE</th><th>CHAIR</th><th>COT</th></tr>
<tr><td>TEAKWOOD</td><td>2</td><td>3</td><td>4</td></tr>
<tr><td>ROSEWOOD</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>SATINWOOD</td><td>3</td><td>2</td><td>1</td></tr></table>
<p>It is found that 29 tonnes of teakwood, 13 tonnes of rosewood and 16 tonnes of satinwood are available
to make all the three types of furniture.</p>
<p>i) Translate the problem into a system of equations.<br>
ii) Solve the system of equations by using matrix method.<br>
iii) Hence find the number of table(s), chair(s) and cot(s) produced.</p>""",
          a=r"""<p>(i) Let \(x,y,z\) be the numbers of tables, chairs and cots.</p>
<p>\(2x+3y+4z=29,\quad x+y+2z=13,\quad 3x+2y+z=16.\)</p>
<p>(ii) \(AX=B\) with \(A=\begin{bmatrix}2&3&4\\1&1&2\\3&2&1\end{bmatrix},\ X=\begin{bmatrix}x\\y\\z\end{bmatrix},\ B=\begin{bmatrix}29\\13\\16\end{bmatrix}\).</p>
<p>\(|A|=2(1-4)-3(1-6)+4(2-3)=-6+15-4=5\ne0\), so \(A^{-1}\) exists and the solution is unique.</p>
<p>Cofactors: \(C_{11}=-3,\ C_{12}=5,\ C_{13}=-1;\ C_{21}=5,\ C_{22}=-10,\ C_{23}=5;\ C_{31}=2,\ C_{32}=0,\ C_{33}=-1\).</p>
<p>\[\operatorname{adj}A=\begin{bmatrix}-3&5&2\\5&-10&0\\-1&5&-1\end{bmatrix},\qquad A^{-1}=\frac15\begin{bmatrix}-3&5&2\\5&-10&0\\-1&5&-1\end{bmatrix}.\]</p>
<p>\[X=A^{-1}B=\frac15\begin{bmatrix}-87+65+32\\145-130+0\\-29+65-16\end{bmatrix}=\frac15\begin{bmatrix}10\\15\\20\end{bmatrix}=\begin{bmatrix}2\\3\\4\end{bmatrix}.\]</p>
<p>(iii) <span class="box">2 tables, 3 chairs and 4 cots</span></p>
<p>Check: teak \(4+9+16=29\), rose \(2+3+8=13\), satin \(6+6+4=16\). ✓</p>""",
          topic="Matrices and Determinants (system of equations)",
          recall=r"""<ul><li>\(AX=B\Rightarrow X=A^{-1}B\) when \(|A|\ne0\).</li>
<li>\(A^{-1}=\dfrac{\operatorname{adj}A}{|A|}\); adj A is the transpose of the cofactor matrix.</li></ul>"""),

        Q("12", 6, r"""<p>A person has manufactured a water tank in the shape of a closed right circular cylinder. The volume of
the cylinder is \(\dfrac{539}{2}\) cubic units. If the height and radius of the cylinder be h and r</p>
{{fig:0}}
<p>(a) Express h in terms of radius r and given volume.<br>
(b) Let the total surface area of the tank be S, express S in terms of r.<br>
(c) If the total surface area of the tank is minimum, prove that radius \(r=\tfrac72\) units.<br>
(d) Find the height of the tank.</p>""",
          qfig=F.fig_q12_cylinder,
          a=r"""<p>(a) \(\pi r^2h=\dfrac{539}{2}\Rightarrow\) <span class="box">\(h=\dfrac{539}{2\pi r^2}\)</span></p>
<p>(b) \(S=2\pi r^2+2\pi rh=2\pi r^2+2\pi r\cdot\dfrac{539}{2\pi r^2}\Rightarrow\) <span class="box">\(S=2\pi r^2+\dfrac{539}{r}\)</span></p>
<p>(c) \(\dfrac{dS}{dr}=4\pi r-\dfrac{539}{r^2}=0\Rightarrow r^3=\dfrac{539}{4\pi}=\dfrac{539\times7}{4\times22}=\dfrac{343}{8}\) (taking \(\pi=\tfrac{22}{7}\)),
so \(r=\dfrac72\).</p>
<p>\(\dfrac{d^2S}{dr^2}=4\pi+\dfrac{1078}{r^3}\gt 0\), so S is minimum at <span class="box">\(r=\dfrac72\) units</span>.</p>
<p>(d) \(h=\dfrac{539}{2\cdot\frac{22}{7}\cdot\frac{49}{4}}=\dfrac{539}{77}\) = <span class="box">\(7\) units</span> (\(h=2r\): height equals diameter).</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Closed cylinder: \(V=\pi r^2h\), \(S=2\pi r^2+2\pi rh\).</li>
<li>Use the constraint to write S in one variable, then \(S'=0\), \(S''\gt 0\) for a minimum.</li></ul>"""),

        Q("12 (OR)", 6, r"""<p>A dolphin jumps and its path is given by the function \(h(t)=\tfrac12(-7t^2+3t+2)\), \((t\ge0)\), h(t) is the height
of the dolphin at any point of time.</p>
<p class="note">[The question is accompanied by a picture of a leaping dolphin; it carries no data.]</p>
<p>(a) Is the function differentiable for \(t\ge0\)? Justify.<br>
(b) Find the instantaneous rate of change of height at \(t=\tfrac1{14}\).<br>
(c) \(h(t)\) is increasing in \(\left(-\infty,\tfrac{3}{14}\right)\). Is this true or false? Justify.<br>
(d) Find the time at which the dolphin will attain the maximum height. Also find the maximum height.</p>""",
          a=r"""<p>(a) <b>Yes.</b> \(h\) is a polynomial, and \(h'(t)=\tfrac12(-14t+3)\) exists for every \(t\ge0\); so \(h\) is differentiable for \(t\ge0\).</p>
<p>(b) \(h'\left(\tfrac1{14}\right)=\tfrac12(-1+3)\) = <span class="box">1 unit of height per unit time</span>.</p>
<p>(c) \(h'(t)\gt 0\iff t\lt \tfrac3{14}\). The function is defined only for \(t\ge0\) (time cannot be negative), so h is
increasing on \(\left[0,\tfrac3{14}\right)\), not on \(\left(-\infty,\tfrac3{14}\right)\).
<span class="box">False</span> — the correct interval is \(\left[0,\tfrac{3}{14}\right)\).
(The bare quadratic would increase on \((-\infty,\tfrac3{14})\), but negative \(t\) is outside the domain.)</p>
<p>(d) \(h'(t)=0\Rightarrow t=\tfrac3{14}\); \(h''(t)=-7\lt 0\), so a maximum.</p>
<p>\(h\left(\tfrac3{14}\right)=\tfrac12\left(-\tfrac{9}{28}+\tfrac{9}{14}+2\right)=\tfrac12\cdot\tfrac{65}{28}\).</p>
<p><span class="box">Maximum height \(\dfrac{65}{56}\) units at \(t=\dfrac{3}{14}\)</span></p>
{{fig:0}}""",
          afig=[(F.fig_q12or_path, "Height against time: rising on [0, 3/14), falling after.")],
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Polynomials are differentiable everywhere.</li>
<li>Instantaneous rate of change = \(h'(t)\).</li>
<li>Increasing where \(h'\gt 0\), restricted to the domain; max where \(h'=0,\ h''\lt 0\).</li></ul>"""),

        Q("13", 6, r"""<p>The Economics, Mathematics and Commerce teachers of a school sometimes give surprise tests on the
same day. The Economics teacher give a test 90% of the time, the Mathematics teacher give a test 80% of
the time, while the Commerce teacher gives a test 70% of the time. Each teacher decides independently.</p>
<p>Let X be the number of surprise tests a student gets on a given day.</p>
<p>(i) Find the probability for each possible number of surprise tests.<br>
(ii) Use the probabilities to build a distribution table.<br>
(iii) Calculate the average number of surprise tests per day.</p>""",
          a=r"""<p>Test probabilities 0.9, 0.8, 0.7; no-test probabilities 0.1, 0.2, 0.3; independent. \(X\in\{0,1,2,3\}\).</p>
<p>(i) \(P(X=0)=0.1\times0.2\times0.3=0.006\)</p>
<p>\(P(X=1)=0.9(0.2)(0.3)+0.1(0.8)(0.3)+0.1(0.2)(0.7)=0.054+0.024+0.014=0.092\)</p>
<p>\(P(X=2)=0.9(0.8)(0.3)+0.9(0.2)(0.7)+0.1(0.8)(0.7)=0.216+0.126+0.056=0.398\)</p>
<p>\(P(X=3)=0.9\times0.8\times0.7=0.504\)</p>
<p>(ii)</p>
<table class="data"><tr><th>X</th><td>0</td><td>1</td><td>2</td><td>3</td></tr>
<tr><th>P(X)</th><td>0.006</td><td>0.092</td><td>0.398</td><td>0.504</td></tr></table>
<p>(Total \(=1\) ✓.)</p>
<p>(iii) \(E(X)=\sum xP(x)=0+0.092+0.796+1.512\) = <span class="box">2.4 tests per day</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Probability distribution: list every value of X with its probability; they sum to 1.</li>
<li>Mean \(E(X)=\sum x_ip_i\).</li></ul>"""),

        Q("14", 6, r"""<p>Solve the differential equation: \((x\,dy-y\,dx)\,y\sin\left(\dfrac yx\right)=(y\,dx+x\,dy)\,x\cos\left(\dfrac yx\right)\).
Find the particular solution satisfying the condition that \(y=\pi\) when \(x=1\).</p>""",
          a=r"""<p>Rearrange: \(\dfrac{dy}{dx}\left[xy\sin\tfrac yx-x^2\cos\tfrac yx\right]=y^2\sin\tfrac yx+xy\cos\tfrac yx\), so</p>
<p>\[\frac{dy}{dx}=\frac{y^2\sin\frac yx+xy\cos\frac yx}{xy\sin\frac yx-x^2\cos\frac yx}=\frac{\frac yx\left(\frac yx\sin\frac yx+\cos\frac yx\right)}{\frac yx\sin\frac yx-\cos\frac yx},\]</p>
<p>a homogeneous equation. Put \(y=vx\), \(\dfrac{dy}{dx}=v+x\dfrac{dv}{dx}\):</p>
<p>\[x\frac{dv}{dx}=\frac{v(v\sin v+\cos v)}{v\sin v-\cos v}-v=\frac{2v\cos v}{v\sin v-\cos v}.\]</p>
<p>Separate: \(\displaystyle\int\frac{v\sin v-\cos v}{v\cos v}\,dv=\int\frac{2\,dx}{x}\Rightarrow\int\left(\tan v-\frac1v\right)dv=2\log|x|+\log|C_1|.\)</p>
<p>\(-\log|\cos v|-\log|v|=\log|C_1x^2|\Rightarrow\log\left|\dfrac{1}{v\cos v}\right|=\log|C_1x^2|\Rightarrow v\cos v\cdot x^2=C\).</p>
<p>With \(v=\tfrac yx\): general solution <span class="box">\(xy\cos\dfrac yx=C\)</span></p>
<p>At \(x=1,\ y=\pi\): \(C=1\cdot\pi\cos\pi=-\pi\).</p>
<p>Particular solution: <span class="box">\(xy\cos\left(\dfrac yx\right)=-\pi\)</span></p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Homogeneous equation: \(\frac{dy}{dx}=F(\frac yx)\); substitute \(y=vx\).</li>
<li>\(\int\tan v\,dv=-\log|\cos v|\).</li>
<li>Use the initial condition to fix the constant.</li></ul>"""),

        Q("14 (OR)", 6, r"""<p>Evaluate: \(\displaystyle\int_0^\pi\frac{x\tan x}{\sec x+\cos x}\,dx\)</p>""",
          a=r"""<p>Simplify: \(\dfrac{\tan x}{\sec x+\cos x}=\dfrac{\sin x/\cos x}{(1+\cos^2x)/\cos x}=\dfrac{\sin x}{1+\cos^2x}\) (the point \(x=\tfrac\pi2\) is a removable gap).</p>
<p>\(I=\displaystyle\int_0^\pi\frac{x\sin x}{1+\cos^2x}\,dx\). (1)</p>
<p>Using \(\int_0^af(x)\,dx=\int_0^af(a-x)\,dx\): \(\sin(\pi-x)=\sin x,\ \cos(\pi-x)=-\cos x\), so</p>
<p>\(I=\displaystyle\int_0^\pi\frac{(\pi-x)\sin x}{1+\cos^2x}\,dx\). (2)</p>
<p>Adding: \(2I=\pi\displaystyle\int_0^\pi\frac{\sin x}{1+\cos^2x}\,dx\). Put \(\cos x=t\), \(-\sin x\,dx=dt\); \(x=0\to t=1,\ x=\pi\to t=-1\):</p>
<p>\[2I=\pi\int_{-1}^{1}\frac{dt}{1+t^2}=\pi\left[\tan^{-1}t\right]_{-1}^{1}=\pi\left(\frac\pi4+\frac\pi4\right)=\frac{\pi^2}{2}.\]</p>
<p><span class="box">\(I=\dfrac{\pi^2}{4}\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int_0^af(x)\,dx=\int_0^af(a-x)\,dx\) removes the factor \(x\).</li>
<li>\(\int\frac{dt}{1+t^2}=\tan^{-1}t\).</li></ul>"""),

        # ---------------------------------------------------------------- Section B
        SEC("Section B – 15 Marks",
            "15. In subparts (i) and (ii) choose the correct options and in subparts (iii) to (v), answer the questions as instructed. [5]"),

        Q("15(i)", 1, r"""<p>If L is the foot of the perpendicular drawn from a point P (a, b, c) on the XY-plane, what is the co-ordinate of L?</p>
<p>a) (a, b, 0) &emsp; b) (0, 0, c) &emsp; c) (0, b, 0) &emsp; d) (a, 0, 0)</p>""",
          a=r"""<p>On the XY-plane \(z=0\); the perpendicular from P is parallel to the z-axis, so x and y are unchanged.</p>
<p><span class="box">a) (a, b, 0)</span></p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>XY-plane: \(z=0\); its normal is the z-axis.</li></ul>"""),

        Q("15(ii)", 1, r"""<p>If \(|\vec a|=3\), \(|\vec b|=\dfrac{\sqrt2}{3}\) and \(\vec a\times\vec b\) is a unit vector, then the angle between \(\vec a\) and \(\vec b\) will be</p>
<p>a) \(\tfrac\pi6\) &emsp; b) \(\tfrac\pi4\) &emsp; c) \(\tfrac\pi3\) &emsp; d) \(\tfrac\pi2\)</p>""",
          a=r"""<p>\(|\vec a\times\vec b|=|\vec a||\vec b|\sin\theta=3\cdot\dfrac{\sqrt2}{3}\sin\theta=\sqrt2\sin\theta=1\Rightarrow\sin\theta=\dfrac1{\sqrt2}\Rightarrow\theta=\dfrac\pi4\) (θ ∈ [0, π]; π/4 is the listed option).</p>
<p><span class="box">b) \(\dfrac\pi4\)</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(|\vec a\times\vec b|=|\vec a||\vec b|\sin\theta\).</li></ul>"""),

        Q("15(iii)", 1, r"""<p>Find the area of the parallelogram whose diagonals are \(\hat i-3\hat j+\hat k\) and \(\hat i+\hat j+\hat k\).</p>""",
          a=r"""<p>\(\vec d_1\times\vec d_2=\begin{vmatrix}\hat i&\hat j&\hat k\\1&-3&1\\1&1&1\end{vmatrix}=\hat i(-3-1)-\hat j(1-1)+\hat k(1+3)=-4\hat i+4\hat k\).</p>
<p>Area \(=\tfrac12|\vec d_1\times\vec d_2|=\tfrac12\sqrt{16+16}=\tfrac12\cdot4\sqrt2\) = <span class="box">\(2\sqrt2\) sq units</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>Area of parallelogram from diagonals: \(\tfrac12|\vec d_1\times\vec d_2|\) (from adjacent sides: \(|\vec a\times\vec b|\)).</li></ul>"""),

        Q("15(iv)", 1, r"""<p>Find the distance of the plane through (1, 1, 1) and perpendicular to the line
\(\dfrac{x-1}{3}=\dfrac{y-1}{0}=\dfrac{z-1}{4}\) from the origin.</p>""",
          a=r"""<p>Normal = direction of the line \((3,0,4)\). Plane: \(3(x-1)+0(y-1)+4(z-1)=0\Rightarrow3x+4z=7\).</p>
<p>Distance from O \(=\dfrac{|0+0-7|}{\sqrt{9+0+16}}\) = <span class="box">\(\dfrac75\) units</span></p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Plane through \((x_1,y_1,z_1)\) with normal \((a,b,c)\): \(a(x-x_1)+b(y-y_1)+c(z-z_1)=0\).</li>
<li>Distance of a point from \(ax+by+cz+d=0\): \(\frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}\).</li></ul>"""),

        Q("15(v)", 1, r"""<p>Find the unit vector perpendicular to both \(\vec a=3\hat i+2\hat j+4\hat k\) and \(\vec b=\hat i-3\hat j+\hat k\).</p>""",
          a=r"""<p>\(\vec a\times\vec b=\begin{vmatrix}\hat i&\hat j&\hat k\\3&2&4\\1&-3&1\end{vmatrix}=\hat i(2+12)-\hat j(3-4)+\hat k(-9-2)=14\hat i+\hat j-11\hat k\),
\(|\vec a\times\vec b|=\sqrt{196+1+121}=\sqrt{318}\).</p>
<p><span class="box">\(\pm\dfrac{1}{\sqrt{318}}\left(14\hat i+\hat j-11\hat k\right)\)</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(\vec a\times\vec b\) is perpendicular to both; divide by its magnitude; ± for both senses.</li></ul>"""),

        Q("16", 2, r"""{{fig:0}}
<p>A building is to be constructed in the form of a triangular pyramid ABCD as shown in the figure. Let the
angular points be A (0,1,2), B (3,0,1), C (4,3,6) and D (2,3,2) and let G be the point of intersection of the
medians of ΔBCD. Using the above information, answer the following</p>
<p>a) What will be the length of the vector \(\overrightarrow{AG}\)?<br>b) Find the area of ΔABC.</p>""",
          qfig=F.fig_q16_pyramid,
          a=r"""<p>(a) G is the centroid of ΔBCD: \(G=\left(\dfrac{3+4+2}{3},\dfrac{0+3+3}{3},\dfrac{1+6+2}{3}\right)=(3,2,3)\).</p>
<p>\(\overrightarrow{AG}=3\hat i+\hat j+\hat k\), \(|\overrightarrow{AG}|=\sqrt{9+1+1}\) = <span class="box">\(\sqrt{11}\) units</span></p>
<p>(b) \(\overrightarrow{AB}=3\hat i-\hat j-\hat k,\ \overrightarrow{AC}=4\hat i+2\hat j+4\hat k\).</p>
<p>\(\overrightarrow{AB}\times\overrightarrow{AC}=\begin{vmatrix}\hat i&\hat j&\hat k\\3&-1&-1\\4&2&4\end{vmatrix}=\hat i(-4+2)-\hat j(12+4)+\hat k(6+4)=-2\hat i-16\hat j+10\hat k\).</p>
<p>Area \(=\tfrac12\sqrt{4+256+100}=\tfrac12\sqrt{360}=\tfrac12\cdot6\sqrt{10}\) = <span class="box">\(3\sqrt{10}\) sq units</span></p>""",
          afig=[(F.fig_q16_centroid, "G is the centroid of face BCD; AG joins the apex to it.")],
          topic="Vector Algebra",
          recall=r"""<ul><li>Centroid = average of the three vertices.</li>
<li>Area of triangle = \(\tfrac12|\overrightarrow{AB}\times\overrightarrow{AC}|\).</li></ul>"""),

        Q("16 (OR)", 2, r"""<p>What are the values of x for which the angle between the vectors, \(2x^2\hat i+3x\hat j+\hat k\) and
\(\hat i-2\hat j+x^2\hat k\), is obtuse?</p>
<p class="note">[The paper prints the hat over “3x” instead of over j (\(\widehat{3x}j\)); the term is \(3x\hat j\).]</p>""",
          a=r"""<p>The angle is obtuse iff the dot product is negative (and the vectors are not antiparallel):</p>
<p>\(\vec a\cdot\vec b=2x^2-6x+x^2=3x^2-6x=3x(x-2)\lt 0\iff0\lt x\lt 2\).</p>
<p>For \(0\lt x\lt 2\) the vectors cannot be antiparallel (that would need \(2x^2=\lambda,\ 3x=-2\lambda\) with \(\lambda\lt 0\), impossible for \(x\gt 0\)).</p>
<p><span class="box">\(0\lt x\lt 2\)</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}\); obtuse ⇔ \(\vec a\cdot\vec b\lt 0\) (θ ≠ π).</li></ul>"""),

        Q("17", 4, r"""<p>Given B and C lie on the line \(\dfrac{x+3}{5}=\dfrac{y-1}{2}=\dfrac{z+4}{3}\) and BC = 5 units. Given A (0,2,3).
Find the area of ΔABC.</p>
{{fig:0}}""",
          qfig=F.fig_q17_triangle,
          a=r"""<p>The height of ΔABC on base BC is the perpendicular distance AD of A from the line.</p>
<p>Line: through \(P(-3,1,-4)\), direction \(\vec d=5\hat i+2\hat j+3\hat k\), \(|\vec d|=\sqrt{38}\).</p>
<p>A general point is \(D(5\lambda-3,\ 2\lambda+1,\ 3\lambda-4)\); \(\overrightarrow{AD}=(5\lambda-3)\hat i+(2\lambda-1)\hat j+(3\lambda-7)\hat k\).</p>
<p>\(\overrightarrow{AD}\perp\vec d\): \(5(5\lambda-3)+2(2\lambda-1)+3(3\lambda-7)=0\Rightarrow38\lambda=38\Rightarrow\lambda=1\).</p>
<p>So \(D=(2,3,-1)\) and \(AD=\sqrt{4+1+16}=\sqrt{21}\).</p>
<p>(Check by the cross product: \(\overrightarrow{AP}\times\vec d=(11,-26,-1)\), \(\dfrac{|\overrightarrow{AP}\times\vec d|}{|\vec d|}=\sqrt{\tfrac{798}{38}}=\sqrt{21}\), as before.)</p>
<p>Area \(=\tfrac12\times BC\times AD=\tfrac12\times5\times\sqrt{21}\) = <span class="box">\(\dfrac{5\sqrt{21}}{2}\) sq units</span> (≈ 11.46)</p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Foot of perpendicular: take a general point on the line and make \(\overrightarrow{AD}\cdot\vec d=0\).</li>
<li>Distance from a point to a line: \(\dfrac{|\overrightarrow{AP}\times\vec d|}{|\vec d|}\).</li></ul>"""),

        Q("17 (OR)", 4, r"""<p>Find the equation of the plane containing the line \(\dfrac{x}{-2}=\dfrac{y-1}{3}=\dfrac{1-z}{1}\) and the point (−1, 0, 2).</p>""",
          a=r"""<p>Standard form of the line: \(\dfrac{x-0}{-2}=\dfrac{y-1}{3}=\dfrac{z-1}{-1}\): point \(P(0,1,1)\), direction \(\vec d=(-2,3,-1)\).</p>
<p>With \(Q(-1,0,2)\): \(\overrightarrow{PQ}=(-1,-1,1)\). Normal \(\vec n=\vec d\times\overrightarrow{PQ}=\begin{vmatrix}\hat i&\hat j&\hat k\\-2&3&-1\\-1&-1&1\end{vmatrix}=\hat i(3-1)-\hat j(-2-1)+\hat k(2+3)=2\hat i+3\hat j+5\hat k\).</p>
<p>Plane through P: \(2(x-0)+3(y-1)+5(z-1)=0\).</p>
<p><span class="box">\(2x+3y+5z=8\)</span></p>
<p>Check: Q gives \(-2+0+10=8\) ✓; \(\vec n\cdot\vec d=-4+9-5=0\) ✓.</p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Rewrite \(\frac{1-z}{1}\) as \(\frac{z-1}{-1}\) before reading the direction ratios.</li>
<li>Normal to a plane containing a line and a point: \(\vec d\times\overrightarrow{PQ}\).</li></ul>"""),

        Q("18", 4, r"""<p>Find the area bounded by the curve, \(y=x(4-x)\) and the x-axis from \(x=0\) to \(x=5\) as shown in the
figure given below.</p>
{{fig:0}}""",
          qfig=F.fig_q18_area,
          a=r"""<p>The curve cuts the x-axis at \(x=0\) and \(x=4\); it is above the axis on \((0,4)\) and below it on \((4,5)\), so
the area is split there.</p>
<p>\(A_1=\displaystyle\int_0^4(4x-x^2)\,dx=\left[2x^2-\frac{x^3}{3}\right]_0^4=32-\frac{64}{3}=\frac{32}{3}.\)</p>
<p>\(\displaystyle\int_4^5(4x-x^2)\,dx=\left[2x^2-\frac{x^3}{3}\right]_4^5=\left(50-\frac{125}{3}\right)-\left(32-\frac{64}{3}\right)=\frac{25}{3}-\frac{32}{3}=-\frac73\), so \(A_2=\dfrac73\).</p>
<p>Area \(=A_1+A_2=\dfrac{32}{3}+\dfrac73=\dfrac{39}{3}\) = <span class="box">13 sq units</span></p>
<p>(Integrating straight from 0 to 5 would give \(\tfrac{32}{3}-\tfrac73=\tfrac{25}{3}\), which is wrong: the part below the axis would cancel area.)</p>""",
          topic="Application of Integrals",
          recall=r"""<ul><li>Area = \(\int|y|\,dx\): split at the x-intercepts and take the modulus of each part.</li></ul>"""),

        # ---------------------------------------------------------------- Section C
        SEC("Section C – 15 Marks",
            "In the ISC 2027 syllabus: 19(i), Q20 and Q20 (OR) (marginal revenue and average cost — differentiation, Applications of Derivatives), 19(iii) (break-even — solving a given cost equation) and Q22 (Linear Programming). Excluded: 19(ii), 19(v), Q21 (regression) and 19(iv) (cost function from fixed and variable costs — no calculus)."),

        Q("19(i)", 1, r"""<p><b>19. In subparts (i) and (ii) choose the correct options and in subpart (iii), answer the questions as
instructed. [5]</b></p>
<p>If the demand function is given by \(p=1500-2x-x^2\) then find the marginal revenue when x = 10</p>
<p>a) 1160 &emsp; b) 1600 &emsp; c) 1100 &emsp; d) 1200</p>""",
          a=r"""<p>Revenue \(R=px=1500x-2x^2-x^3\).</p>
<p>Marginal revenue \(MR=\dfrac{dR}{dx}=1500-4x-3x^2\); at \(x=10\): \(1500-40-300=1160\).</p>
<p><span class="box">a) 1160</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Revenue \(R(x)=p\cdot x\); marginal revenue \(MR=\dfrac{dR}{dx}\) (rate of change of revenue).</li>
<li>Differentiate R, not p.</li></ul>"""),

        Q("19(ii)", 1, r"""<p>Read the following statements and choose the correct option:<br>
I) If r = 0, then regression lines are not defined.<br>II) If r = 0, then regression lines are parallel.<br>
III) If r = 0, then regression lines are perpendicular<br>IV) If r = ±1, then regression lines coincide.</p>
<p>Which of the following is correct?<br>a) Only IV is correct &emsp; b) Only I and II are correct &emsp;
c) Only I and IV are correct &emsp; d) Only III and IV are correct</p>""",
          excluded=REGR.format("regression lines")),

        Q("19(iii)", 1, r"""<p>A manufacturing company finds that the daily cost of producing x items of a product is given by
C(x) = 210x + 7000. Find the minimum number that must be produced and sold daily, if each item is sold
for ₹280.</p>""",
          a=r"""<p>Revenue from \(x\) items: \(R(x)=280x\). Profit \(P(x)=R(x)-C(x)=280x-210x-7000=70x-7000\).</p>
<p>There is no loss when \(P(x)\ge0\): \(70x\ge7000\Rightarrow x\ge100\) (break-even where \(R(x)=C(x)\), i.e. \(x=100\)).</p>
<p><span class="box">At least 100 items must be produced and sold daily</span></p>""",
          topic="Relations and Functions (application of a linear function)",
          recall=r"""<ul><li>Revenue = selling price × quantity; profit \(P=R-C\).</li>
<li>Break-even: \(R(x)=C(x)\); no loss for \(x\) at or beyond it.</li></ul>"""),

        Q("19(iv)", 1, r"""<p>A company sells its product @₹10 per unit. The variable costs are estimated to be estimated to be
25% of the total revenue received. If the fixed cost for the product is ₹4500, then find the cost function.</p>""",
          excluded=COMMERCE.format("forming a cost function from fixed and variable costs")),

        Q("19(v)", 1, r"""<p>If the coefficient of correlation is 0.66, the variance of x is 121 and the standard deviation of y is 8, find
the regression coefficient of x on y.</p>""",
          excluded=REGR.format("regression coefficient")),

        Q("20", 2, r"""<p>A demand function of a monopoly is given by x = 100 − 4p. Find the quantity at which the marginal
revenue will be zero.</p>""",
          a=r"""<p>From \(x=100-4p\): \(p=\dfrac{100-x}{4}\).</p>
<p>Revenue \(R=px=\dfrac{100x-x^2}{4}\); marginal revenue \(MR=\dfrac{dR}{dx}=\dfrac{100-2x}{4}\).</p>
<p>\(MR=0\Rightarrow100-2x=0\Rightarrow\) <span class="box">\(x=50\) units</span> (where \(p=12.5\); R is then maximum since \(\frac{d^2R}{dx^2}=-\frac12\lt 0\)).</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Express p in terms of x first; \(R=px\).</li>
<li>\(MR=\dfrac{dR}{dx}\).</li></ul>"""),

        Q("20 (OR)", 2, r"""<p>The cost function of a commodity is \(C(x)=200+20x-\tfrac12x^2\) (in rupees). Find the range where AC falls.</p>""",
          a=r"""<p>Average cost \(AC=\dfrac{C(x)}{x}=\dfrac{200}{x}+20-\dfrac x2\), \(x\gt 0\).</p>
<p>\(\dfrac{d(AC)}{dx}=-\dfrac{200}{x^2}-\dfrac12\).</p>
<p>Both terms are negative, so \(\dfrac{d(AC)}{dx}\lt 0\) for every \(x\gt 0\): AC is strictly decreasing.</p>
<p><span class="box">AC falls for all output levels \(x\gt 0\)</span></p>
<p class="note">(The cost function itself is realistic only while \(MC=20-x\gt 0\), i.e. \(0\lt x\lt 20\); AC falls throughout.)</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>\(AC=\dfrac{C(x)}{x}\).</li>
<li>A function falls (decreases) where its derivative is negative.</li></ul>"""),

        Q("21", 4, r"""<p>A company plans to advertise some vacancies. The Manager is asked to suggest the monthly salary for
these vacancies based on the years of experience. To do so, the Manager studies the years of service and
the monthly salary drawn by the existing employees in the company.
Following is the data that the Manager refers to:</p>
<table class="data"><tr><th>Years of service (X)</th><td>11</td><td>7</td><td>9</td><td>5</td><td>8</td><td>6</td><td></td><td>10</td></tr>
<tr><th>Monthly salary (in ₹ 1000) (Y)</th><td>10</td><td>8</td><td>6</td><td>5</td><td>9</td><td>7</td><td></td><td>11</td></tr></table>
<p class="note">[The seventh column is printed empty in the original.]</p>
<p>a) Find the regression equation of monthly salary on the years of service.<br>
b) If a person with 13 years of experience applies for a job in this company, what monthly salary will be
suggested by the Manager?</p>""",
          excluded=REGR.format("regression equation")),

        Q("22", 4, r"""<p>Two different types of books have to be stacked in the shelf of a library. The first type of book weighs
1 kg and has a thickness of 6 cm. The second type of book weighs 1.5 kg and has a thickness of 4 cm. The
shelf is 96 cm long and can support a maximum weight of 21 kg. How should both the types of books be
placed in the shelf to include the maximum number of books? Formulate a Linear Programming Problem
and solve it graphically.</p>""",
          a=r"""<p>Let \(x\) books of the first type and \(y\) of the second be placed.</p>
<p><b>Maximise</b> \(Z=x+y\) subject to</p>
<p>\(6x+4y\le96\) i.e. \(3x+2y\le48\) (shelf length), &nbsp; \(x+1.5y\le21\) i.e. \(2x+3y\le42\) (weight), &nbsp; \(x\ge0,\ y\ge0\).</p>
<p>Lines: \(3x+2y=48\) through \((16,0),(0,24)\); \(2x+3y=42\) through \((21,0),(0,14)\). Both inequalities are satisfied
by O, so the feasible region lies on the origin side of each line.</p>
<p>Intersection: \(9x+6y=144,\ 4x+6y=84\Rightarrow5x=60\Rightarrow x=12,\ y=6\).</p>
{{fig:0}}
<table class="data"><tr><th>Corner</th><td>O(0, 0)</td><td>(16, 0)</td><td>P(12, 6)</td><td>(0, 14)</td></tr>
<tr><th>Z = x + y</th><td>0</td><td>16</td><td><b>18</b></td><td>14</td></tr></table>
<p>The region is bounded, so the maximum is at a corner: \(Z_{\max}=18\) at \((12,6)\).</p>
<p><span class="box">12 books of the first type and 6 of the second: 18 books in all</span></p>""",
          afig=[(F.fig_q22_lpp, "Feasible region OAPC; the dashed line x + y = 18 touches it only at P(12, 6).")],
          topic="Linear Programming",
          recall=r"""<ul><li>Define the variables, write the objective and every constraint (including non-negativity).</li>
<li>Bounded feasible region: optimum at a corner point — evaluate Z at each.</li></ul>"""),

        Q("22 (OR)", 4, r"""<p>The feasible region for an L.P.P. is shown in the adjoining figure. From on the given graph,</p>
{{fig:0}}
<p>a) Write the constraints for the L.P.P.<br>b) Find the co-ordinates of the point B.<br>
c) Find the maximum value of the objective function, z = x + y.</p>""",
          qfig=F.fig_q22or_region,
          a=r"""<p>(a) Line DA through \((0,50),(25,0)\): \(\dfrac x{25}+\dfrac y{50}=1\Rightarrow2x+y=50\).
Line CE through \((0,20),(40,0)\): \(\dfrac x{40}+\dfrac y{20}=1\Rightarrow x+2y=40\).
The shaded region contains O, so</p>
<p><span class="box">\(2x+y\le50,\quad x+2y\le40,\quad x\ge0,\quad y\ge0\)</span></p>
<p>(b) Solve \(2x+y=50,\ x+2y=40\): \(4x+2y=100\Rightarrow3x=60\Rightarrow x=20,\ y=10\). <span class="box">B(20, 10)</span></p>
<p>(c) Corners O(0,0), A(25,0), B(20,10), C(0,20):</p>
<table class="data"><tr><th>Corner</th><td>O</td><td>A(25, 0)</td><td>B(20, 10)</td><td>C(0, 20)</td></tr>
<tr><th>z = x + y</th><td>0</td><td>25</td><td><b>30</b></td><td>20</td></tr></table>
<p><span class="box">\(z_{\max}=30\) at B(20, 10)</span></p>
{{fig:0}}""",
          afig=[(F.fig_q22or_ans, "Region OABC with B(20, 10); the dashed line z = 30 touches it only at B.")],
          topic="Linear Programming",
          recall=r"""<ul><li>Intercept form \(\frac xa+\frac yb=1\) from the two axis points of each line.</li>
<li>The side containing O gives “≤” when the region includes the origin.</li>
<li>Corner-point method for a bounded region.</li></ul>"""),
    ])
