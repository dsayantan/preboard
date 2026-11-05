"""Heritage School Pre-Board 2024-25 (second set), Mathematics (Class XII).  Transcribed from the page images."""
from kit import Q, SEC
import maths_2024_25_s2_figs as F

REGR = ("Correlation and regression ({}) — dropped from ISC Mathematics; not in any of the seven ISC 2027 "
        "Class XII units.")

AR = r"""<p>Which of the following is correct?<br>
(a) Both Assertion and Reason are true &amp; Reason is the correct explanation for Assertion.<br>
(b) Both Assertion and Reason are true &amp; Reason is not the correct explanation for Assertion.<br>
(c) Assertion is true and Reason is false.<br>
(d) Assertion is false and Reason is true.</p>"""

PAPER = dict(
    subject="maths",
    year="2024-25",
    slug="2024-25-set-2",
    paper="Set 2",
    source="PreBoard-PYQ/2024-25/SET-2/MATHEMATICS.pdf",
    marks=80, time="3 hours",
    intro=r"""<p>You are allowed an additional 15 minutes for only reading the paper.</p>
<ul><li>You must NOT start writing during reading time.</li>
<li>The question paper has 8 printed pages.</li>
<li>The Question Paper is divided into three sections and has 22 questions in all.</li>
<li>Section A is compulsory and has fourteen questions.</li>
<li>You are required to attempt all questions either from Section B or Section C.</li>
<li>Section B and Section C have four questions each.</li>
<li>Internal choices have been provided in two questions of 2 marks, two questions of 4 marks and two questions
of 6 marks in Section A.</li>
<li>Internal choices have been provided in one question of 2 marks and one question of 4 marks each in Section
B and Section C.</li>
<li>While attempting Multiple Choice Questions in Section A, B and C, you are required to write only ONE
option as the answer.</li>
<li>The intended marks for questions or parts of questions are given in the brackets [].</li>
<li>All workings, including rough work, should be done on the same page as, and adjacent to, the rest of the
answer.</li>
<li>Mathematical tables and graph papers are provided.</li></ul>
<p class="note">In the ISC 2027 pattern there is no longer a choice between Sections B and C: Vectors and
3-D Geometry (this paper's Section B) and Linear Programming (Q22 here) are compulsory. Of the rest of
Section C, the questions whose mathematics is differentiation (marginal cost, marginal average cost, average cost,
marginal revenue) are answered as Applications of Derivatives; regression and the price-from-revenue item
(no calculus) have left the syllabus.</p>""",
    items=[
        SEC("Section A – 65 Marks [Compulsory Section]",
            "Question 1 [15]. In subparts (i) to (xi) choose the correct options and in subparts (xii) to (xv), "
            "answer the questions as instructed."),

        # ---------------------------------------------------------------- Question 1
        Q("1(i)", 1, r"""<p>Let L be a set of all straight lines in a plane. The relation R on L defined as ‘perpendicular to’ is:</p>
<p>(a) Symmetric and Transitive &emsp; (b) Transitive &emsp; (c) Symmetric &emsp; (d) Equivalence</p>""",
          a=r"""<p><b>Reflexive?</b> No line is perpendicular to itself, so \((L_1,L_1)\notin R\).</p>
<p><b>Symmetric?</b> \(L_1\perp L_2\Rightarrow L_2\perp L_1\). Yes.</p>
<p><b>Transitive?</b> \(L_1\perp L_2\) and \(L_2\perp L_3\) make \(L_1\parallel L_3\), not perpendicular. No.</p>
<p><span class="box">(c) Symmetric</span></p>""",
          topic="Relations and Functions",
          recall=r"""<ul><li>Reflexive: \((a,a)\in R\ \forall a\); symmetric: \((a,b)\in R\Rightarrow(b,a)\in R\); transitive: \((a,b),(b,c)\in R\Rightarrow(a,c)\in R\).</li>
<li>In a plane, two lines perpendicular to the same line are parallel.</li></ul>"""),

        Q("1(ii)", 1, r"""<p>P and Q are two matrices such that \([P+Q]^T=\begin{bmatrix}7&-8\\3&0\end{bmatrix}\). If
\(P=\begin{bmatrix}-1&1\\3&2\end{bmatrix}\), which one of the following is Q?</p>
<p>(a) \(\begin{bmatrix}8&-9\\0&2\end{bmatrix}\) &emsp; (b) \(\begin{bmatrix}-8&-2\\11&2\end{bmatrix}\) &emsp;
(c) \(\begin{bmatrix}8&2\\-11&-2\end{bmatrix}\) &emsp; (d) \(\begin{bmatrix}8&-11\\2&-2\end{bmatrix}\)</p>""",
          a=r"""<p>Transpose both sides: \(P+Q=\begin{bmatrix}7&3\\-8&0\end{bmatrix}\).</p>
<p>\(Q=\begin{bmatrix}7&3\\-8&0\end{bmatrix}-\begin{bmatrix}-1&1\\3&2\end{bmatrix}=\begin{bmatrix}8&2\\-11&-2\end{bmatrix}\).</p>
<p><span class="box">(c)</span></p>""",
          topic="Matrices",
          recall=r"""<ul><li>\((A^T)^T=A\): transpose the given sum before subtracting.</li>
<li>Matrices are added/subtracted entry by entry.</li></ul>"""),

        Q("1(iii)", 1, r"""<p>What is the value of \(\cot\left(\dfrac{\pi}{2}+\tan^{-1}\dfrac{1}{\sqrt2}\right)\)?</p>
<p>(a) \(\dfrac{1}{\sqrt2}\) &emsp; (b) \(\dfrac{\pi}{2}\) &emsp; (c) −1 &emsp; (d) \(\dfrac{-1}{\sqrt2}\)</p>""",
          a=r"""<p>Let \(\theta=\tan^{-1}\dfrac1{\sqrt2}\), so \(\tan\theta=\dfrac1{\sqrt2}\).</p>
<p>\(\cot\left(\dfrac\pi2+\theta\right)=-\tan\theta=-\dfrac1{\sqrt2}\).</p>
<p><span class="box">(d) \(-\dfrac{1}{\sqrt2}\)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>Allied angles: \(\cot\left(\frac\pi2+\theta\right)=-\tan\theta\).</li>
<li>\(\tan(\tan^{-1}x)=x\) for every real \(x\).</li></ul>"""),

        Q("1(iv)", 1, r"""<p>Five numbers \(x_1, x_2, x_3, x_4, x_5\) are randomly selected from the numbers 1, 2, 3, ……., 18 and are
arranged in the increasing order such that \(x_1\lt x_2\lt x_3\lt x_4\lt x_5\). What is the probability that
\(x_2=7\) and \(x_4=11\)?</p>
<p>(a) \(\dfrac{26}{51}\) &emsp; (b) \(\dfrac{3}{104}\) &emsp; (c) \(\dfrac{1}{68}\) &emsp; (d) \(\dfrac{1}{34}\)</p>""",
          a=r"""<p>Total ways to choose 5 numbers: \(n(S)=\binom{18}{5}=8568\).</p>
<p>Favourable: \(x_2=7,\ x_4=11\) fixed; \(x_1\) from \(\{1,\dots,6\}\) (6 ways), \(x_3\) from \(\{8,9,10\}\) (3 ways),
\(x_5\) from \(\{12,\dots,18\}\) (7 ways): \(6\times3\times7=126\).</p>
<p>\(P=\dfrac{126}{8568}=\dfrac1{68}\).</p>
<p><span class="box">(c) \(\dfrac{1}{68}\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Classical probability \(P(E)=\dfrac{n(E)}{n(S)}\).</li>
<li>Once a set is chosen its increasing arrangement is unique, so count selections, not arrangements.</li></ul>"""),

        Q("1(v)", 1, r"""<p>Given below are the graphs of f(x) along with the statements. Which one of the following statements is
NOT correct about the graphs?</p>
{{fig:0}}""",
          qfig=F.fig_q1v_graphs,
          a=r"""<p>(a) There is a jump at \(x_0\): the left and right limits differ. Correct.</p>
<p>(b) The curve has a hole at \(x_0\): \(f(x_0)\) is not defined. Correct.</p>
<p>(c) \(f(x)\to-\infty\) on the left of \(x_0\) and \(+\infty\) on the right: not continuous. Correct.</p>
<p>(d) \(f(x)\to-\infty\) from both sides of \(x_0\): the limit is not finite and \(f(x_0)\) is not defined, so f is
<b>not</b> continuous at \(x_0\). The statement “f(x) is continuous at \(x=x_0\)” is wrong.</p>
<p><span class="box">(d)</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>f is continuous at \(a\) iff \(\lim_{x\to a^-}f=\lim_{x\to a^+}f=f(a)\), all finite.</li>
<li>A vertical asymptote (infinite limit) is always a discontinuity.</li></ul>"""),

        Q("1(vi)", 1, r"""<p>In which one of the following intervals is the function \(f(x)=x^3-12x\) increasing?</p>
<p>(a) (– 2, 2) &emsp; (b) \((-\infty,-2)\cup(2,\infty)\) &emsp; (c) \((-2,\infty)\) &emsp; (d) \((-\infty,2)\)</p>""",
          a=r"""<p>\(f'(x)=3x^2-12=3(x-2)(x+2)\gt 0\iff x\lt -2\) or \(x\gt 2\).</p>
<p><span class="box">(b) \((-\infty,-2)\cup(2,\infty)\)</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>f is increasing where \(f'(x)\gt 0\).</li>
<li>Sign of a quadratic: positive outside its roots when the leading coefficient is positive.</li></ul>"""),

        Q("1(vii)", 1, r"""<p>The value of \(\displaystyle\int_1^{\sqrt3}\frac{dx}{1+x^2}\) is</p>
<p>(a) \(\dfrac{\pi}{2}\) &emsp; (b) \(\dfrac{2\pi}{3}\) &emsp; (c) \(\dfrac{\pi}{6}\) &emsp; (d) \(\dfrac{\pi}{12}\)</p>""",
          a=r"""<p>\(\displaystyle\int_1^{\sqrt3}\frac{dx}{1+x^2}=\left[\tan^{-1}x\right]_1^{\sqrt3}=\frac\pi3-\frac\pi4=\frac\pi{12}\).</p>
<p><span class="box">(d) \(\dfrac{\pi}{12}\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int\frac{dx}{1+x^2}=\tan^{-1}x+C\).</li>
<li>\(\tan^{-1}\sqrt3=\frac\pi3,\ \tan^{-1}1=\frac\pi4\).</li></ul>"""),

        Q("1(viii)", 1, r"""<p>The value of \(\dfrac{dy}{dx}\) if \(y=|x-1|+|x-4|\) at \(x=3\) is</p>
<p>(a) −2 &emsp; (b) 0 &emsp; (c) 2 &emsp; (d) 4</p>""",
          a=r"""<p>Near \(x=3\) (i.e. \(1\lt x\lt 4\)): \(x-1\gt 0\) and \(x-4\lt 0\), so \(y=(x-1)-(x-4)=3\), a constant.</p>
<p>Hence \(\dfrac{dy}{dx}=0\) at \(x=3\).</p>
<p><span class="box">(b) 0</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Remove the modulus using the sign of each bracket on the interval containing the point.</li>
<li>\(|u|=u\) if \(u\ge0\), \(-u\) if \(u\lt 0\).</li></ul>"""),

        Q("1(ix)", 1, r"""<p><b>Statement 1</b>: The function \(f:N\to N\) given by f(x) = 5x is one to one and onto.<br>
<b>Statement 2</b>: The function \(f:R\to R\) given by f(x) = 5x is one to one and onto.</p>
<p>Which one of the following options is correct?<br>(a) Both the statements are true.<br>(b) Both the statements are false.<br>
(c) Statement 1 is true and Statement 2 is false.<br>(d) Statement 1 is false and Statement 2 is true</p>""",
          a=r"""<p>On N: \(5x_1=5x_2\Rightarrow x_1=x_2\) (one-one), but 1, 2, 3, 4, 6, … have no pre-image (range is multiples of 5),
so not onto. Statement 1 is false.</p>
<p>On R: one-one as above, and any \(y\in R\) has pre-image \(x=\frac y5\in R\): onto. Statement 2 is true.</p>
<p><span class="box">(d)</span></p>""",
          topic="Relations and Functions",
          recall=r"""<ul><li>Onto: every element of the co-domain has a pre-image <em>in the domain</em>.</li>
<li>The same rule can be onto on R and not onto on N.</li></ul>"""),

        Q("1(x)", 1, r"""<p><b>Assertion:</b> Let the matrices \(A=\begin{bmatrix}-3&2\\-5&4\end{bmatrix}\) and
\(B=\begin{bmatrix}4&-2\\5&-3\end{bmatrix}\) be such that \(A^{100}B=BA^{100}\)<br>
<b>Reason:</b> AB = BA implies \(A^nB=BA^n\) for all positive integers n.</p>""" + AR,
          a=r"""<p>\(AB=\begin{bmatrix}-12+10&6-6\\-20+20&10-12\end{bmatrix}=\begin{bmatrix}-2&0\\0&-2\end{bmatrix}\),
\(BA=\begin{bmatrix}-12+10&8-8\\-15+15&10-12\end{bmatrix}=\begin{bmatrix}-2&0\\0&-2\end{bmatrix}\). So \(AB=BA\).</p>
<p>Reason: if \(A^kB=BA^k\) then \(A^{k+1}B=A(A^kB)=A(BA^k)=(AB)A^k=(BA)A^k=BA^{k+1}\); true for all n by induction.</p>
<p>So the Assertion is true, and it follows from the Reason with n = 100.</p>
<p><span class="box">(a)</span></p>""",
          topic="Matrices",
          recall=r"""<ul><li>Matrix multiplication is not commutative in general; check \(AB\) and \(BA\) separately.</li>
<li>If A and B commute, every power of A commutes with B (induction).</li></ul>"""),

        Q("1(xi)", 1, r"""<p><b>Assertion:</b> Degree of the differential equation: \(a\left(\dfrac{dy}{dx}\right)^2+b\dfrac{dx}{dy}=c\), is 3<br>
<b>Reason:</b> If each term involving derivatives of a differential equation is a polynomial (or can be expressed as
polynomial) then highest exponent of the highest order derivative is called the degree of the differential equation.</p>""" + AR,
          a=r"""<p>\(\dfrac{dx}{dy}=\dfrac{1}{dy/dx}\). Writing \(p=\dfrac{dy}{dx}\): \(ap^2+\dfrac bp=c\Rightarrow ap^3-cp+b=0\).</p>
<p>The equation is now a polynomial in \(\dfrac{dy}{dx}\); its highest power is 3, so the degree is 3. Assertion true.</p>
<p>The Reason is the definition of degree, and it is exactly what gives 3 here.</p>
<p><span class="box">(a)</span></p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Degree is read only after the equation is made polynomial in the derivatives.</li>
<li>\(\dfrac{dx}{dy}=1\Big/\dfrac{dy}{dx}\): clear the fraction first.</li></ul>"""),

        Q("1(xii)", 1, r"""<p>The value of the determinant of a matrix A of order 3 is 3. If C is the matrix of cofactors of the matrix A,
then what is the value of determinant of \(C^2\)?</p>""",
          a=r"""<p>\(C^T=\operatorname{adj}A\), so \(|C|=|\operatorname{adj}A|=|A|^{n-1}=3^{2}=9\).</p>
<p>\(|C^2|=|C|^2=81\).</p>
<p><span class="box">\(|C^2|=81\)</span></p>""",
          topic="Determinants",
          recall=r"""<ul><li>\(\operatorname{adj}A\) is the transpose of the cofactor matrix; \(|A^T|=|A|\).</li>
<li>\(|\operatorname{adj}A|=|A|^{n-1}\) for order n; \(|AB|=|A||B|\).</li></ul>"""),

        Q("1(xiii)", 1, r"""<p>Find the derivative of \(y=\log x+\dfrac1x\) w.r.t x.</p>""",
          a=r"""<p>\(\dfrac{dy}{dx}=\dfrac1x+\dfrac{d}{dx}(x^{-1})=\dfrac1x-\dfrac1{x^2}\).</p>
<p><span class="box">\(\dfrac{dy}{dx}=\dfrac1x-\dfrac1{x^2}=\dfrac{x-1}{x^2}\)</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>\(\frac{d}{dx}\log x=\frac1x\); \(\frac{d}{dx}x^n=nx^{n-1}\).</li></ul>"""),

        Q("1(xiv)", 1, r"""<p>Evaluate: \(\displaystyle\int_0^6|x+3|\,dx\)</p>""",
          a=r"""<p>For \(0\le x\le6\), \(x+3\gt 0\), so \(|x+3|=x+3\).</p>
<p>\(\displaystyle\int_0^6(x+3)\,dx=\left[\frac{x^2}{2}+3x\right]_0^6=18+18=36\).</p>
<p><span class="box">36</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>Check the sign of the expression inside the modulus over the interval of integration.</li></ul>"""),

        Q("1(xv)", 1, r"""<p>Teena is practising for an upcoming Rifle Shooting tournament. The probability of her shooting the target in the
1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup> and 4<sup>th</sup> shots are 0.4, 0.3, 0.2 and 0.1 respectively. Find the
probability of at least one shot of Teena hitting the target.</p>""",
          a=r"""<p>Shots are independent. P(all four miss) \(=0.6\times0.7\times0.8\times0.9=0.3024\).</p>
<p>P(at least one hit) \(=1-0.3024\).</p>
<p><span class="box">0.6976</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>“At least one” = 1 − P(none).</li>
<li>Independent events: \(P(\bar A\bar B\dots)=P(\bar A)P(\bar B)\dots\).</li></ul>"""),

        # ---------------------------------------------------------------- Questions 2–6 (2 marks)
        Q("2", 2, r"""<p>Solve: \(5\tan^{-1}x+3\cot^{-1}x=2\pi\)</p>""",
          a=r"""<p>Use \(\cot^{-1}x=\dfrac\pi2-\tan^{-1}x\):</p>
<p>\(5\tan^{-1}x+\dfrac{3\pi}{2}-3\tan^{-1}x=2\pi\Rightarrow2\tan^{-1}x=\dfrac\pi2\Rightarrow\tan^{-1}x=\dfrac\pi4\).</p>
<p><span class="box">\(x=1\)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>\(\tan^{-1}x+\cot^{-1}x=\dfrac\pi2\) for all real x.</li></ul>"""),

        Q("3", 2, r"""<p>Without expanding at any stage, find the value of the determinant.</p>
<p>\[\begin{vmatrix}qr&rp&pq\\5&5&5\\p(q+r)&q(r+p)&r(p+q)\end{vmatrix}\]</p>""",
          a=r"""<p>\(R_3\to R_3+R_1\):</p>
<p>\[\Delta=\begin{vmatrix}qr&rp&pq\\5&5&5\\pq+qr+rp&pq+qr+rp&pq+qr+rp\end{vmatrix}
=(pq+qr+rp)\cdot5\begin{vmatrix}qr&rp&pq\\1&1&1\\1&1&1\end{vmatrix}\]</p>
<p>(taking \(pq+qr+rp\) common from \(R_3\) and 5 from \(R_2\)). Two rows are identical, so the determinant is 0.</p>
<p><span class="box">\(\Delta=0\)</span></p>""",
          topic="Determinants",
          recall=r"""<ul><li>Adding a multiple of one row to another leaves the determinant unchanged.</li>
<li>A common factor of a row can be taken outside; two identical rows give 0.</li></ul>"""),

        Q("3 (OR)", 2, r"""<p>For what value of k, the matrix \(\begin{bmatrix}0&k\\-6&0\end{bmatrix}\) is skew symmetric?</p>""",
          a=r"""<p>Skew symmetric means \(A^T=-A\), i.e. \(a_{ij}=-a_{ji}\).</p>
<p>\(a_{12}=-a_{21}\Rightarrow k=-(-6)=6\) (diagonal entries are already 0).</p>
<p><span class="box">\(k=6\)</span></p>""",
          topic="Matrices",
          recall=r"""<ul><li>Skew symmetric: \(A^T=-A\); diagonal entries are 0 and \(a_{ij}=-a_{ji}\).</li></ul>"""),

        Q("4", 2, r"""<p>If \(f:R\to R\) is defined by \(f(x)=\dfrac{2x-7}{4}\), show that f(x) is one-one and onto.</p>""",
          a=r"""<p><b>One-one:</b> let \(f(x_1)=f(x_2)\). Then \(\dfrac{2x_1-7}{4}=\dfrac{2x_2-7}{4}\Rightarrow2x_1=2x_2\Rightarrow x_1=x_2\). So f is one-one.</p>
<p><b>Onto:</b> let \(y\in R\) (co-domain). Solve \(y=\dfrac{2x-7}{4}\): \(x=\dfrac{4y+7}{2}\in R\), and
\(f\left(\dfrac{4y+7}{2}\right)=\dfrac{(4y+7)-7}{4}=y\). Every y has a pre-image, so f is onto.</p>
<p><span class="box">f is one-one and onto (a bijection)</span></p>""",
          topic="Relations and Functions",
          recall=r"""<ul><li>One-one: \(f(x_1)=f(x_2)\Rightarrow x_1=x_2\).</li>
<li>Onto: for every y in the co-domain, solve \(f(x)=y\) and show the x found lies in the domain.</li></ul>"""),

        Q("5", 2, r"""<p>Find the point on the curve \(y=x^2+2x-1\), where the tangent is parallel to x-axis.</p>""",
          a=r"""<p>Tangent parallel to the x-axis \(\Rightarrow\) slope \(\dfrac{dy}{dx}=0\).</p>
<p>\(\dfrac{dy}{dx}=2x+2=0\Rightarrow x=-1\); then \(y=1-2-1=-2\).</p>
{{fig:0}}
<p><span class="box">\((-1,\,-2)\)</span></p>""",
          afig=[(F.fig_q5_tangent, "The tangent at the vertex (−1, −2) is the horizontal line y = −2.")],
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Slope of the tangent at a point is \(\dfrac{dy}{dx}\) there.</li>
<li>Parallel to x-axis: slope 0; parallel to y-axis: \(\frac{dx}{dy}=0\).</li></ul>"""),

        Q("5 (OR)", 2, r"""<p>Evaluate: \(\displaystyle\int\frac{1+\cos x}{\sin^2x}\,dx\)</p>""",
          a=r"""<p>\(\displaystyle\int\frac{1+\cos x}{\sin^2x}\,dx=\int\left(\csc^2x+\csc x\cot x\right)dx\).</p>
<p><span class="box">\(-\cot x-\csc x+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int\csc^2x\,dx=-\cot x\); \(\int\csc x\cot x\,dx=-\csc x\).</li>
<li>Split the numerator over the denominator.</li></ul>"""),

        Q("6", 2, r"""<p>Find the value of P (A∪ B) if \(2P(A)=P(B)=\dfrac{5}{13}\) and \(P(A/B)=\dfrac25\).</p>""",
          a=r"""<p>\(P(B)=\dfrac5{13}\), \(P(A)=\dfrac5{26}\).</p>
<p>\(P(A\cap B)=P(A|B)\,P(B)=\dfrac25\cdot\dfrac5{13}=\dfrac2{13}\).</p>
<p>\(P(A\cup B)=P(A)+P(B)-P(A\cap B)=\dfrac5{26}+\dfrac{10}{26}-\dfrac4{26}=\dfrac{11}{26}\).</p>
<p><span class="box">\(P(A\cup B)=\dfrac{11}{26}\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>\(P(A|B)=\dfrac{P(A\cap B)}{P(B)}\).</li>
<li>Addition theorem \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\).</li></ul>"""),

        # ---------------------------------------------------------------- Questions 7–10 (4 marks)
        Q("7", 4, r"""<p>If \(y=\left(x+\sqrt{a^2+x^2}\right)^m\), prove that \((a^2+x^2)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}-m^2y=0\).</p>""",
          a=r"""<p>\(\dfrac{dy}{dx}=m\left(x+\sqrt{a^2+x^2}\right)^{m-1}\left(1+\dfrac{x}{\sqrt{a^2+x^2}}\right)
=m\left(x+\sqrt{a^2+x^2}\right)^{m-1}\cdot\dfrac{\sqrt{a^2+x^2}+x}{\sqrt{a^2+x^2}}=\dfrac{my}{\sqrt{a^2+x^2}}\).</p>
<p>So \(\sqrt{a^2+x^2}\,\dfrac{dy}{dx}=my\). Squaring: \((a^2+x^2)\left(\dfrac{dy}{dx}\right)^2=m^2y^2\).</p>
<p>Differentiate w.r.t. x:
\(2x\left(\dfrac{dy}{dx}\right)^2+(a^2+x^2)\cdot2\dfrac{dy}{dx}\dfrac{d^2y}{dx^2}=2m^2y\dfrac{dy}{dx}\).</p>
<p>Divide by \(2\dfrac{dy}{dx}\) \(\left(\ne0\right)\):</p>
<p><span class="box">\((a^2+x^2)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}-m^2y=0\)</span> &nbsp; Hence proved.</p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Chain rule; \(\frac{d}{dx}\sqrt{a^2+x^2}=\frac{x}{\sqrt{a^2+x^2}}\).</li>
<li>Second-order proofs: get a first-order relation, square to remove the root, then differentiate again.</li></ul>"""),

        Q("7 (OR)", 4, r"""<p>Determine the value of the constant ‘k’ so that the function
\(f(x)=\begin{cases}\dfrac{kx}{|x|}, & x\lt 0\\ 3, & x\ge0\end{cases}\) is continuous at x = 0</p>""",
          a=r"""<p>For \(x\lt 0\), \(|x|=-x\), so \(f(x)=\dfrac{kx}{-x}=-k\).</p>
<p>LHL \(=\displaystyle\lim_{x\to0^-}f(x)=-k\); RHL \(=\displaystyle\lim_{x\to0^+}3=3\); \(f(0)=3\).</p>
<p>Continuity at 0: LHL = RHL = f(0) \(\Rightarrow -k=3\).</p>
<p><span class="box">\(k=-3\)</span></p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>Continuity at a: \(\lim_{x\to a^-}f=\lim_{x\to a^+}f=f(a)\).</li>
<li>\(\dfrac{x}{|x|}=-1\) for \(x\lt 0\) and \(+1\) for \(x\gt 0\).</li></ul>"""),

        Q("8", 4, r"""<p>If \(\sin^{-1}x+\sin^{-1}y+\sin^{-1}z=\pi\), show that \(x^2-y^2-z^2+2yz\sqrt{1-x^2}=0\)</p>""",
          a=r"""<p>Let \(\sin^{-1}x=A,\ \sin^{-1}y=B,\ \sin^{-1}z=C\), each in \(\left[-\frac\pi2,\frac\pi2\right]\), so
\(\cos A=\sqrt{1-x^2},\ \cos B=\sqrt{1-y^2},\ \cos C=\sqrt{1-z^2}\) (cosine is non-negative there).</p>
<p>\(B+C=\pi-A\Rightarrow\cos(B+C)=-\cos A\):</p>
<p>\(\cos B\cos C-\sin B\sin C=-\cos A\Rightarrow\sqrt{1-y^2}\sqrt{1-z^2}-yz=-\sqrt{1-x^2}\)</p>
<p>\(\Rightarrow\sqrt{1-y^2}\sqrt{1-z^2}=yz-\sqrt{1-x^2}\).</p>
<p>Square both sides: \((1-y^2)(1-z^2)=y^2z^2-2yz\sqrt{1-x^2}+1-x^2\)</p>
<p>\(1-y^2-z^2+y^2z^2=y^2z^2-2yz\sqrt{1-x^2}+1-x^2\)</p>
<p><span class="box">\(x^2-y^2-z^2+2yz\sqrt{1-x^2}=0\)</span> &nbsp; Hence shown.</p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>Principal value range of \(\sin^{-1}\): \(\left[-\frac\pi2,\frac\pi2\right]\), where \(\cos\theta=\sqrt{1-\sin^2\theta}\ge0\).</li>
<li>\(\cos(B+C)=\cos B\cos C-\sin B\sin C\); \(\cos(\pi-A)=-\cos A\).</li></ul>"""),

        Q("9", 4, r"""<p>Evaluate: \(\displaystyle\int x^2\cos x\,dx\)</p>""",
          a=r"""<p>By parts with \(u=x^2,\ dv=\cos x\,dx\):</p>
<p>\(\displaystyle\int x^2\cos x\,dx=x^2\sin x-\int2x\sin x\,dx\).</p>
<p>Again by parts: \(\displaystyle\int x\sin x\,dx=-x\cos x+\int\cos x\,dx=-x\cos x+\sin x\).</p>
<p>\(\displaystyle\int x^2\cos x\,dx=x^2\sin x-2(-x\cos x+\sin x)\)</p>
<p><span class="box">\(x^2\sin x+2x\cos x-2\sin x+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int u\,dv=uv-\int v\,du\); choose the polynomial as \(u\) (ILATE).</li>
<li>Repeat by parts until the polynomial is used up.</li></ul>"""),

        Q("10", 4, r"""<p>Aman, Bhuvan and Chandan go to a restaurant for lunch. They decide who will pay for the lunch by tossing a coin.
It is decided that each one of them will toss a coin and if one person gets a different result (head or tail) than the other
two, that person would pay. If all three get the same result (all heads or all tails), they will toss again until they get a
different result.</p>
<p>(a) What is the probability that all three friends will get the same result (all heads or all tails) in one round of tossing?<br>
(b) What is the probability that they will get a different result in one round of tossing?<br>
(c) What is the probability that they will need exactly four rounds of tossing to determine who would pay?</p>""",
          a=r"""<p>One round: three coins, \(2^3=8\) equally likely outcomes.</p>
<p>(a) Same result: HHH or TTT, \(P=\dfrac28=\) <span class="box">\(\dfrac14\)</span></p>
<p>(b) Different result (someone is the odd one out): \(1-\dfrac14=\) <span class="box">\(\dfrac34\)</span></p>
<p>(c) Exactly four rounds: the first three rounds all give the same result and the fourth does not. Rounds are independent:</p>
<p>\(P=\left(\dfrac14\right)^3\cdot\dfrac34=\) <span class="box">\(\dfrac{3}{256}\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Complement rule \(P(\bar E)=1-P(E)\).</li>
<li>Independent repeated trials: multiply; “first success on the k-th trial” = \(q^{k-1}p\).</li></ul>"""),

        Q("10 (OR)", 4, r"""<p>A jewellery seller has precious gems in white and red colour which he has put in three boxes. The distribution of
these gems is shown in the table given below</p>
<table class="data"><tr><th rowspan="2">Box</th><th colspan="2">Number of Gems</th></tr>
<tr><th>White</th><th>Red</th></tr>
<tr><td>I</td><td>1</td><td>2</td></tr><tr><td>II</td><td>2</td><td>3</td></tr><tr><td>III</td><td>3</td><td>1</td></tr></table>
<p>He wants to gift two gems to his mother. So, he asks her to select one box at random and pick out any two gems one
after the other without replacement from the selected box. The mother selects one white and one red gem. Calculate
the probability that the gems drawn are from Box II.</p>""",
          a=r"""<p>Let \(E_1,E_2,E_3\): Box I, II, III is chosen; \(P(E_i)=\dfrac13\). Let A: one white and one red gem are drawn.</p>
<p>Two gems drawn without replacement = a selection of 2 from the box:</p>
<p>\(P(A|E_1)=\dfrac{\binom11\binom21}{\binom32}=\dfrac23,\quad P(A|E_2)=\dfrac{\binom21\binom31}{\binom52}=\dfrac6{10}=\dfrac35,\quad
P(A|E_3)=\dfrac{\binom31\binom11}{\binom42}=\dfrac36=\dfrac12\).</p>
{{fig:0}}
<p>By Bayes’ theorem:</p>
<p>\[P(E_2|A)=\frac{\frac13\cdot\frac35}{\frac13\left(\frac23+\frac35+\frac12\right)}=\frac{\frac35}{\frac{20+18+15}{30}}=\frac{18}{53}\]</p>
<p><span class="box">\(P(\text{Box II}\mid\text{one white, one red})=\dfrac{18}{53}\approx0.34\)</span></p>""",
          afig=[F.fig_q10or_tree],
          topic="Probability",
          recall=r"""<ul><li>Bayes: \(P(E_k|A)=\dfrac{P(E_k)P(A|E_k)}{\sum P(E_i)P(A|E_i)}\).</li>
<li>Drawing 2 one after the other without replacement, order ignored: use combinations (or add WR and RW).</li></ul>"""),

        # ---------------------------------------------------------------- Questions 11–14 (6 marks)
        Q("11", 6, r"""<p>Mrs. Roy designs a window in her son’s study room so that the room gets maximum sunlight. She designs the window in
the shape of a rectangle surmounted by an equilateral triangle. If the perimeter of the window is 12 m, find the
dimensions of the window that will admit maximum sunlight into the room.</p>
{{fig:0}}""",
          qfig=F.fig_q11_window,
          a=r"""<p>Let the width of the rectangle (= side of the equilateral triangle) be \(x\) m and its height \(y\) m.</p>
{{fig:0}}
<p>Perimeter (the common side is inside, not on the boundary): \(x+2y+2x=12\Rightarrow y=\dfrac{12-3x}{2}\).</p>
<p>Maximum sunlight \(\Leftrightarrow\) maximum area:
\(A=xy+\dfrac{\sqrt3}{4}x^2=\dfrac{x(12-3x)}{2}+\dfrac{\sqrt3}{4}x^2=6x-\dfrac32x^2+\dfrac{\sqrt3}{4}x^2\).</p>
<p>\(\dfrac{dA}{dx}=6-3x+\dfrac{\sqrt3}{2}x=0\Rightarrow x\left(3-\dfrac{\sqrt3}{2}\right)=6\Rightarrow x=\dfrac{12}{6-\sqrt3}=\dfrac{12(6+\sqrt3)}{33}=\dfrac{4(6+\sqrt3)}{11}\).</p>
<p>\(\dfrac{d^2A}{dx^2}=-3+\dfrac{\sqrt3}{2}\lt 0\): a maximum.</p>
<p>\(y=6-\dfrac32x=6-\dfrac{6(6+\sqrt3)}{11}=\dfrac{30-6\sqrt3}{11}\).</p>
<p><span class="box">Width \(=\dfrac{4(6+\sqrt3)}{11}\approx2.81\) m, height of rectangle \(=\dfrac{30-6\sqrt3}{11}\approx1.78\) m</span></p>
<p>(each side of the triangle is also \(\approx2.81\) m).</p>""",
          afig=[(F.fig_q11_window_ans, "Width x (also the triangle's side), height y; the dashed side is inside the window.")],
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Area of an equilateral triangle of side \(x\): \(\frac{\sqrt3}{4}x^2\).</li>
<li>Use the constraint to write the area in one variable; \(A'=0\), then \(A''\lt 0\) for a maximum.</li></ul>"""),

        Q("11 (OR)", 6, r"""<p>A given quantity of metal is to be cast into a solid half circular cylinder with a rectangular base and semi-circular
ends. If the total surface is minimum then prove that the ratio of the length of cylinder to the diameter of
semi-circular ends is \(\pi:\pi+2\).</p>
{{fig:0}}""",
          qfig=F.fig_q11or_halfcyl,
          a=r"""<p>Let r be the radius of the semicircular ends and h the length. Volume (fixed):
\(V=\dfrac12\pi r^2h\Rightarrow h=\dfrac{2V}{\pi r^2}\).</p>
<p>Total surface = two semicircular ends + curved surface + rectangular base:</p>
<p>\(S=2\cdot\dfrac12\pi r^2+\pi rh+2rh=\pi r^2+(\pi+2)rh=\pi r^2+\dfrac{2(\pi+2)V}{\pi r}\).</p>
<p>\(\dfrac{dS}{dr}=2\pi r-\dfrac{2(\pi+2)V}{\pi r^2}=0\Rightarrow V=\dfrac{\pi^2r^3}{\pi+2}\).</p>
<p>\(\dfrac{d^2S}{dr^2}=2\pi+\dfrac{4(\pi+2)V}{\pi r^3}\gt 0\): S is minimum.</p>
<p>Then \(\dfrac12\pi r^2h=\dfrac{\pi^2r^3}{\pi+2}\Rightarrow h=\dfrac{2\pi r}{\pi+2}\Rightarrow\dfrac{h}{2r}=\dfrac{\pi}{\pi+2}\).</p>
<p><span class="box">length : diameter \(=h:2r=\pi:(\pi+2)\)</span> &nbsp; Hence proved.</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Half cylinder: volume \(\frac12\pi r^2h\); curved surface \(\pi rh\); flat base \(2r\times h\); two ends \(\pi r^2\) in all.</li>
<li>Eliminate h using the fixed volume, then \(S'(r)=0\), \(S''\gt 0\).</li></ul>"""),

        Q("12", 6, r"""<p>Garima owns a cafe that serves burgers, samosas, and juice bottles. On a particular day, 100 items in total were sold.
The number of burgers sold was thrice the number of samosas sold. Also, the number of samosas sold was 10 more than
the number of juice bottles sold.</p>
<p>i) Form a set of simultaneous equations for the above information.<br>
ii) Solve the set of equations formed in (i) by matrix method.<br>
iii) Hence, find the number of items sold in each category.</p>""",
          a=r"""<p>(i) Let x, y, z be the numbers of burgers, samosas and juice bottles sold.</p>
<p>\(x+y+z=100,\qquad x-3y=0,\qquad y-z=10\).</p>
<p>(ii) \(AX=B\) with \(A=\begin{bmatrix}1&1&1\\1&-3&0\\0&1&-1\end{bmatrix},\ X=\begin{bmatrix}x\\y\\z\end{bmatrix},\ B=\begin{bmatrix}100\\0\\10\end{bmatrix}\).</p>
<p>\(|A|=1(3-0)-1(-1-0)+1(1-0)=5\ne0\), so \(A^{-1}\) exists and the solution is unique.</p>
<p>Cofactors: \(C_{11}=3,\ C_{12}=1,\ C_{13}=1;\ C_{21}=2,\ C_{22}=-1,\ C_{23}=-1;\ C_{31}=3,\ C_{32}=1,\ C_{33}=-4\).</p>
<p>\(\operatorname{adj}A=\begin{bmatrix}3&2&3\\1&-1&1\\1&-1&-4\end{bmatrix}\), \(A^{-1}=\dfrac15\begin{bmatrix}3&2&3\\1&-1&1\\1&-1&-4\end{bmatrix}\).</p>
<p>\(X=A^{-1}B=\dfrac15\begin{bmatrix}300+0+30\\100-0+10\\100-0-40\end{bmatrix}=\dfrac15\begin{bmatrix}330\\110\\60\end{bmatrix}=\begin{bmatrix}66\\22\\12\end{bmatrix}\).</p>
<p>(iii) <span class="box">66 burgers, 22 samosas and 12 juice bottles</span> (check: 66 + 22 + 12 = 100, 66 = 3 × 22, 22 = 12 + 10).</p>""",
          topic="Matrices and Determinants (system of equations)",
          recall=r"""<ul><li>\(AX=B\Rightarrow X=A^{-1}B\) when \(|A|\ne0\).</li>
<li>\(A^{-1}=\dfrac{\operatorname{adj}A}{|A|}\); adj A is the transpose of the cofactor matrix.</li></ul>"""),

        Q("13", 6, r"""<p>Solve the following differential equation:</p>
<p>\(2ye^{\frac xy}dx+\left(y-2xe^{\frac xy}\right)dy=0\), given x = 0 and y = 1</p>""",
          a=r"""<p>\(\dfrac{dx}{dy}=\dfrac{2xe^{x/y}-y}{2ye^{x/y}}=\dfrac{2\frac xy e^{x/y}-1}{2e^{x/y}}\): homogeneous in \(\frac xy\). Put \(x=vy\), \(\dfrac{dx}{dy}=v+y\dfrac{dv}{dy}\).</p>
<p>\(v+y\dfrac{dv}{dy}=\dfrac{2ve^v-1}{2e^v}=v-\dfrac{1}{2e^v}\Rightarrow y\dfrac{dv}{dy}=-\dfrac1{2e^v}\).</p>
<p>Separate: \(2e^v\,dv=-\dfrac{dy}{y}\Rightarrow2e^v=-\log|y|+C\Rightarrow2e^{x/y}+\log|y|=C\).</p>
<p>At \(x=0,\ y=1\): \(2e^0+\log1=C\Rightarrow C=2\).</p>
<p><span class="box">\(2e^{x/y}+\log|y|=2\)</span></p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Homogeneous equation in \(x/y\): take \(\frac{dx}{dy}\) and put \(x=vy\).</li>
<li>Separate variables, integrate, then use the initial condition for C.</li></ul>"""),

        Q("13 (OR)", 6, r"""<p>Evaluate: \(\displaystyle\int_0^{\pi/2}\frac{\cos^2x}{1+\sin x\cos x}\,dx\)</p>""",
          a=r"""<p>Let \(I=\displaystyle\int_0^{\pi/2}\frac{\cos^2x}{1+\sin x\cos x}dx\). Using \(\int_0^af(x)dx=\int_0^af(a-x)dx\):
\(I=\displaystyle\int_0^{\pi/2}\frac{\sin^2x}{1+\sin x\cos x}dx\).</p>
<p>Adding: \(2I=\displaystyle\int_0^{\pi/2}\frac{dx}{1+\sin x\cos x}\). Divide numerator and denominator by \(\cos^2x\):</p>
<p>\(2I=\displaystyle\int_0^{\pi/2}\frac{\sec^2x\,dx}{\sec^2x+\tan x}=\int_0^{\pi/2}\frac{\sec^2x\,dx}{\tan^2x+\tan x+1}\). Put \(t=\tan x\), \(dt=\sec^2x\,dx\); \(t:0\to\infty\).</p>
<p>\(2I=\displaystyle\int_0^\infty\frac{dt}{\left(t+\frac12\right)^2+\frac34}=\frac{2}{\sqrt3}\left[\tan^{-1}\frac{2t+1}{\sqrt3}\right]_0^\infty
=\frac2{\sqrt3}\left(\frac\pi2-\frac\pi6\right)=\frac{2\pi}{3\sqrt3}\).</p>
<p><span class="box">\(I=\dfrac{\pi}{3\sqrt3}\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int_0^af(x)dx=\int_0^af(a-x)dx\); \(\sin\) and \(\cos\) swap under \(x\to\frac\pi2-x\).</li>
<li>\(\int\frac{dt}{t^2+a^2}=\frac1a\tan^{-1}\frac ta\); complete the square.</li></ul>"""),

        Q("14", 6, r"""<p>A group of class XI students designed a game for class XII students to be played at the farewell programme. They kept
two sets of cards on the stage. Each set contained four cards numbered 1,2,3 and 4. Each student of class XII had to draw
one card from each set simultaneously.</p>
<p>The score a student received was defined as the difference between the numbers shown on the cards. The possible outcome
of the score is given in the table below:</p>
<table class="data"><tr><th></th><th colspan="5">Numbers on card 1</th></tr>
<tr><th rowspan="5">Numbers on card 2</th><th></th><th>1</th><th>2</th><th>3</th><th>4</th></tr>
<tr><th>1</th><td>0</td><td>p</td><td>2</td><td>3</td></tr>
<tr><th>2</th><td>1</td><td>0</td><td>p</td><td>2</td></tr>
<tr><th>3</th><td>q</td><td>1</td><td>0</td><td>p</td></tr>
<tr><th>4</th><td>3</td><td>q</td><td>1</td><td>0</td></tr></table>
<p>i) Calculate the values of p and q in the above table.<br>
ii) Reshma plays the game once. Let the random variable ‘S’ represents Reshma’s score. Construct the probability distribution for ‘S’</p>
<table class="data"><tr><th>s</th><td>&emsp;</td><td>&emsp;</td><td>&emsp;</td><td>&emsp;</td></tr>
<tr><th>P(S = s)</th><td></td><td></td><td></td><td></td></tr></table>
<p>iii) Find the probability that Reshma’s score is at most 2.<br>
iv) Find Reshma’s expected score.</p>""",
          a=r"""<p>(i) The score is the (non-negative) difference \(|a-b|\). Card 1 = 2, card 2 = 1 gives \(p=|2-1|=1\) (also \(|3-2|,|4-3|\));
card 1 = 1, card 2 = 3 gives \(q=|1-3|=2\) (also \(|2-4|\)).</p>
<p><span class="box">\(p=1,\ q=2\)</span></p>
<p>(ii) All \(4\times4=16\) outcomes are equally likely. Counting the table: score 0 four times, 1 six times, 2 four times, 3 twice.</p>
<table class="data"><tr><th>s</th><td>0</td><td>1</td><td>2</td><td>3</td></tr>
<tr><th>P(S = s)</th><td>\(\frac4{16}=\frac14\)</td><td>\(\frac6{16}=\frac38\)</td><td>\(\frac4{16}=\frac14\)</td><td>\(\frac2{16}=\frac18\)</td></tr></table>
<p>(Total \(=1\).)</p>
{{fig:0}}
<p>(iii) \(P(S\le2)=1-P(S=3)=1-\dfrac18=\) <span class="box">\(\dfrac78\)</span></p>
<p>(iv) \(E(S)=\sum sP(S=s)=0\cdot\dfrac14+1\cdot\dfrac38+2\cdot\dfrac14+3\cdot\dfrac18=\dfrac{3+4+3}{8}=\) <span class="box">\(\dfrac54=1.25\)</span></p>""",
          afig=[(F.fig_q14_dist, "Probability distribution of the score S; the mean 1.25 is marked.")],
          topic="Probability",
          recall=r"""<ul><li>Probability distribution: list every value with its probability; probabilities add to 1.</li>
<li>Mean (expectation) \(E(X)=\sum x_iP(x_i)\).</li></ul>"""),

        # ---------------------------------------------------------------- Section B
        SEC("Section B – 15 Marks",
            "Question 15. In subparts (i) and (ii) choose the correct options and in subparts (iii) to (v), "
            "answer the questions as instructed."),

        Q("15(i)", 1, r"""<p>Consider the following statements and choose the correct option:</p>
<p><b>Statement 1:</b> If \(\vec a\) and \(\vec b\) represents two adjacent sides of a parallelogram then the diagonals are
represented by \(\vec a+\vec b\) and \(\vec a-\vec b\).<br>
<b>Statement 2:</b> If \(\vec a\) and \(\vec b\) represents two diagonals of a parallelogram then the adjacent sides are
represented by \(2(\vec a+\vec b)\) and \(2(\vec a-\vec b)\).</p>
<p>Which of the following is correct?<br>(a) Only Statement 1 &emsp; (b) Only Statement 2 &emsp;
(c) Both Statements 1 and 2 &emsp; (d) Neither Statement 1 nor Statement 2</p>""",
          a=r"""<p>Statement 1: with \(\vec{OA}=\vec a,\ \vec{OB}=\vec b\), \(\vec{OC}=\vec a+\vec b\) and \(\vec{BA}=\vec a-\vec b\). True.</p>
{{fig:0}}
<p>Statement 2: if the diagonals are \(\vec a=\vec p+\vec q\) and \(\vec b=\vec p-\vec q\) (sides \(\vec p,\vec q\)), then
\(\vec p=\frac12(\vec a+\vec b)\), \(\vec q=\frac12(\vec a-\vec b)\) — halves, not doubles. False.</p>
<p><span class="box">(a) Only Statement 1</span></p>""",
          afig=[F.fig_q15i_par],
          topic="Vector Algebra",
          recall=r"""<ul><li>Triangle/parallelogram law of addition; \(\vec{BA}=\vec{OA}-\vec{OB}\).</li></ul>"""),

        Q("15(ii)", 1, r"""<p>If a line makes an angle α, β, and γ with positive direction of the coordinate axes, then the value of
\(\sin^2\alpha+\sin^2\beta+\sin^2\gamma\) will be:</p>
<p>(a) 1 &emsp; (b) 3 &emsp; (c) – 2 &emsp; (d) 2</p>""",
          a=r"""<p>\(\sum\sin^2\alpha=\sum(1-\cos^2\alpha)=3-(\cos^2\alpha+\cos^2\beta+\cos^2\gamma)=3-1=2\).</p>
<p><span class="box">(d) 2</span></p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Direction cosines satisfy \(l^2+m^2+n^2=1\).</li></ul>"""),

        Q("15(iii)", 1, r"""<p>If \(\vec a=2\hat i+\hat j+2\hat k\) and \(\vec b=5\hat i-3\hat j+\hat k\), find the projection of \(\vec b\) on \(\vec a\).</p>""",
          a=r"""<p>Projection of \(\vec b\) on \(\vec a=\dfrac{\vec a\cdot\vec b}{|\vec a|}=\dfrac{10-3+2}{\sqrt{4+1+4}}=\dfrac93=3\).</p>
<p><span class="box">3</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>Scalar projection of \(\vec b\) on \(\vec a\) is \(\dfrac{\vec a\cdot\vec b}{|\vec a|}\) (divide by the vector projected <em>on</em>).</li></ul>"""),

        Q("15(iv)", 1, r"""<p>Find the distance of the plane through the point (1,1, 1) and perpendicular to the line
\(\dfrac{x-1}{3}=\dfrac{y-1}{0}=\dfrac{z-1}{4}\) from the origin.</p>""",
          a=r"""<p>Normal to the plane = direction of the line \((3,0,4)\). Plane: \(3(x-1)+0(y-1)+4(z-1)=0\Rightarrow3x+4z=7\).</p>
<p>Distance from O \(=\dfrac{|0-7|}{\sqrt{9+0+16}}=\dfrac75\).</p>
<p><span class="box">\(\dfrac75\) units</span></p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Plane through \((x_1,y_1,z_1)\) with normal \((a,b,c)\): \(a(x-x_1)+b(y-y_1)+c(z-z_1)=0\).</li>
<li>Distance of a point from \(ax+by+cz+d=0\): \(\frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}\).</li></ul>"""),

        Q("15(v)", 1, r"""<p>If \(\vec a\) is a unit vector perpendicular to \(\vec b\) and \((\vec a+2\vec b)\cdot(3\vec a-\vec b)=-5\), find \(|\vec b|\).</p>""",
          a=r"""<p>\(|\vec a|=1,\ \vec a\cdot\vec b=0\).</p>
<p>\((\vec a+2\vec b)\cdot(3\vec a-\vec b)=3|\vec a|^2-\vec a\cdot\vec b+6\vec b\cdot\vec a-2|\vec b|^2=3-2|\vec b|^2=-5\Rightarrow|\vec b|^2=4\).</p>
<p><span class="box">\(|\vec b|=2\)</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(\vec a\cdot\vec a=|\vec a|^2\); perpendicular vectors: \(\vec a\cdot\vec b=0\).</li>
<li>Expand dot products like algebraic brackets (dot product is distributive and commutative).</li></ul>"""),

        Q("16", 2, r"""<p>If \(\vec a\times\vec b=\vec a\times\vec c\), where \(\vec a,\vec b\) and \(\vec c\) are non-zero vectors, then prove that
either \(\vec b=\vec c\) or \(\vec a\) and \((\vec b-\vec c)\) are parallel.</p>""",
          a=r"""<p>\(\vec a\times\vec b-\vec a\times\vec c=\vec0\Rightarrow\vec a\times(\vec b-\vec c)=\vec0\) (distributive law).</p>
<p>The cross product of two vectors is zero iff one of them is the zero vector or they are parallel. Since \(\vec a\ne\vec0\):</p>
<p>either \(\vec b-\vec c=\vec0\), i.e. <span class="box">\(\vec b=\vec c\)</span>, or \(\vec a\parallel(\vec b-\vec c)\). &nbsp; Hence proved.</p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(\vec a\times\vec b=|\vec a||\vec b|\sin\theta\,\hat n\); it is \(\vec0\) iff a vector is zero or \(\theta=0,\pi\).</li>
<li>Cross product is distributive over subtraction.</li></ul>"""),

        Q("16 (OR)", 2, r"""<p>What are the values of \(x\) for which the angle between the vectors \(2x^2\hat i+3x\hat j+\hat k\) and
\(\hat i-2\hat j+x^2\hat k\) is obtuse?</p>""",
          a=r"""<p>Obtuse angle \(\Rightarrow\cos\theta\lt 0\Rightarrow\) dot product \(\lt 0\):</p>
<p>\(2x^2(1)+3x(-2)+1\cdot x^2=3x^2-6x=3x(x-2)\lt 0\Rightarrow0\lt x\lt 2\).</p>
<p>(For these x the vectors are never in opposite directions — that would need \(\frac{2x^2}{1}=\frac{3x}{-2}\), i.e. \(x\le0\) — so the angle is
genuinely obtuse, not 180°.)</p>
<p><span class="box">\(0\lt x\lt 2\)</span></p>""",
          topic="Vector Algebra",
          recall=r"""<ul><li>\(\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}\); obtuse \(\iff\vec a\cdot\vec b\lt 0\) (excluding 180°).</li></ul>"""),

        Q("17", 4, r"""<p>Find the equation of the plane containing the line \(\dfrac{x}{-2}=\dfrac{y-1}{3}=\dfrac{1-z}{1}\) and the point (−1,0, 2).</p>""",
          a=r"""<p>Write the line in standard form: \(\dfrac{x-0}{-2}=\dfrac{y-1}{3}=\dfrac{z-1}{-1}\). It passes through A(0, 1, 1) with direction \(\vec d=(-2,3,-1)\).</p>
<p>With P(−1, 0, 2): \(\vec{AP}=(-1,-1,1)\). Normal \(\vec n=\vec d\times\vec{AP}\):</p>
<p>\(\vec n=\begin{vmatrix}\hat i&\hat j&\hat k\\-2&3&-1\\-1&-1&1\end{vmatrix}=(3-1)\hat i-(-2-1)\hat j+(2+3)\hat k=2\hat i+3\hat j+5\hat k\).</p>
<p>Plane through A: \(2(x-0)+3(y-1)+5(z-1)=0\).</p>
<p><span class="box">\(2x+3y+5z=8\)</span> &nbsp; (check P: \(-2+0+10=8\) ✓)</p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Rewrite \(\frac{1-z}{1}\) as \(\frac{z-1}{-1}\) before reading the direction ratios.</li>
<li>Normal to a plane containing two directions = their cross product.</li></ul>"""),

        Q("17 (OR)", 4, r"""<p>A mobile tower is situated at the top of a hill. Consider the surface on which the tower stands as a plane having
points A (1, 0, 2), B (3, –1, 1) and C (1, 2, 1) on it. The mobile tower is tied with three cables from the points A, B and C
such that it stands vertically on the ground. The top of the tower is at point P (2, 3, 1) as shown in the figure below. The
foot of the perpendicular from the point P on the plane is at the point \(Q\left(\frac{43}{29},\frac{77}{29},\frac{9}{29}\right)\)</p>
{{fig:0}}
<p>i) Find the equation of the plane containing the points A, B and C.<br>
ii) Find the equation of the line PQ.<br>
iii) Calculate the height of the tower.</p>""",
          qfig=F.fig_q17or_tower,
          a=r"""<p>(i) \(\vec{AB}=(2,-1,-1),\ \vec{AC}=(0,2,-1)\).
\(\vec n=\vec{AB}\times\vec{AC}=\begin{vmatrix}\hat i&\hat j&\hat k\\2&-1&-1\\0&2&-1\end{vmatrix}=(1+2)\hat i-(-2-0)\hat j+(4-0)\hat k=3\hat i+2\hat j+4\hat k\).</p>
<p>Plane: \(3(x-1)+2(y-0)+4(z-2)=0\Rightarrow\) <span class="box">\(3x+2y+4z=11\)</span> (B: 9 − 2 + 4 = 11 ✓, C: 3 + 4 + 4 = 11 ✓)</p>
<p>(ii) PQ is perpendicular to the plane, so its direction ratios are \(3,2,4\):</p>
<p><span class="box">\(\dfrac{x-2}{3}=\dfrac{y-3}{2}=\dfrac{z-1}{4}\)</span>
(Q lies on it: \(\frac{43}{29}-2=-\frac{15}{29}=3\left(-\frac5{29}\right)\), \(\frac{77}{29}-3=2\left(-\frac5{29}\right)\), \(\frac9{29}-1=4\left(-\frac5{29}\right)\) ✓)</p>
<p>(iii) Height = PQ = distance of P from the plane \(=\dfrac{|3(2)+2(3)+4(1)-11|}{\sqrt{9+4+16}}=\dfrac{5}{\sqrt{29}}\).</p>
<p><span class="box">Height \(=\dfrac{5}{\sqrt{29}}\approx0.93\) units</span></p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Plane through three points: normal \(=\vec{AB}\times\vec{AC}\).</li>
<li>The perpendicular from a point to a plane has the plane's normal as its direction.</li>
<li>Distance of a point from a plane formula.</li></ul>"""),

        Q("18", 4, r"""<p>If the area enclosed between the curves \(y=ax^2\) and \(x=ay^2\), \(a\gt 0\), is 27 sq. unit, find the value of ‘a’.</p>
<p class="note">[No mark is printed against Q18; Section B totals 15, so it carries 4.]</p>""",
          a=r"""<p>Intersections: \(y=ax^2\Rightarrow x=a(ax^2)^2=a^3x^4\Rightarrow x=0\) or \(x=\dfrac1a\); points O and \(\left(\frac1a,\frac1a\right)\).</p>
<p>Between them the parabola \(x=ay^2\) (upper branch \(y=\sqrt{x/a}\)) lies above \(y=ax^2\).</p>
{{fig:0}}
<p>Area \(=\displaystyle\int_0^{1/a}\left(\sqrt{\frac xa}-ax^2\right)dx=\left[\frac{2}{3\sqrt a}x^{3/2}-\frac{a x^3}{3}\right]_0^{1/a}
=\frac{2}{3a^2}-\frac{1}{3a^2}=\frac{1}{3a^2}\).</p>
<p>\(\dfrac{1}{3a^2}=27\Rightarrow a^2=\dfrac1{81}\Rightarrow a=\dfrac19\) (as \(a\gt 0\)).</p>
<p><span class="box">\(a=\dfrac19\)</span></p>""",
          afig=[(F.fig_q18_area, "With a = 1/9 the curves y = x²/9 and x = y²/9 meet at O and (9, 9); the shaded area is 27.")],
          topic="Application of Integrals",
          recall=r"""<ul><li>Area between curves \(=\int_a^b(y_{\text{upper}}-y_{\text{lower}})\,dx\) between the intersection points.</li>
<li>\(y=ax^2\) and \(x=ay^2\) are reflections in \(y=x\).</li></ul>"""),

        # ---------------------------------------------------------------- Section C
        SEC("Section C – 15 Marks",
            "Question 19. In subparts (i) and (ii) choose the correct options and in subparts (iii) to (v), answer the "
            "questions as instructed. — In the ISC 2027 syllabus: 19(ii), 19(v), Q20 and Q20 (OR) (marginal cost, marginal "
            "average cost, average cost, marginal revenue — differentiation, Applications of Derivatives) and Q22 (Linear "
            "Programming). Excluded: 19(i), 19(iii), Q21 (regression) and 19(iv) (price from a revenue function — no calculus)."),

        Q("19(i)", 1, r"""<p>If the correlation coefficient of two sets of variables (X, Y) is \(\dfrac{-3}{4}\), then which one of the following
statements is true for the same set of variables?</p>
<p>(a) Only one of the two regression lines has a negative coefficient.<br>(b) Both regression coefficients are positive.<br>
(c) Both regression coefficients are negative.<br>(d) One of the lines of regression is parallel to the x-axis.</p>""",
          excluded=REGR.format("regression coefficients")),

        Q("19(ii)", 1, r"""<p>At a toy factory, the production cost per day for x number of toys is given by the following function:
\(C(x)=0.0001x^3-0.01x^2-20x+3500\)</p>
<p>Which of these represents the approximate additional cost to produce the 201<sup>st</sup> toy?</p>
<p>(a) C(200) &emsp; (b) AC(201) &emsp; (c) MC(200) &emsp; (d) MC(201)</p>""",
          a=r"""<p>The cost of the 201<sup>st</sup> toy is \(C(201)-C(200)\approx C'(200)\cdot1=MC(200)\): the marginal cost at the
current output x = 200 approximates the cost of one more unit.</p>
<p class="note">The cost function is transcribed exactly as printed (\(0.0001x^3-0.01x^2-20x+3500\)). With it \(MC(x)=0.0003x^2-0.02x-20\) and \(MC(200)=12-4-20=-12\), while \(C(201)-C(200)=-11.95\): the approximation holds, but a negative marginal cost is not realistic — the paper's function is presumably mis-set. The question asks only which expression is the approximation, so the answer is unaffected.</p>
<p><span class="box">(c) MC(200)</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Marginal cost \(MC=\dfrac{dC}{dx}\) ≈ cost of producing one more unit: \(C(x+1)-C(x)\approx C'(x)\).</li></ul>"""),

        Q("19(iii)", 1, r"""<p>Given that \(\bar x=53,\ \bar y=28\), regression co-efficient y on x = −1·2, regression co-efficient x on y = −0·3.
Find coefficient of correlation (r).</p>""",
          excluded=REGR.format("coefficient of correlation from regression coefficients")),

        Q("19(iv)", 1, r"""<p>A person runs a company that produces and sells a particular model of laptop. Its revenue function is given by:
\(R(x)=4x^3+\dfrac15x^2+x\), where x is the number of laptops demanded and R(x) is in rupees.</p>
<p>What is the ideal unit price (in rupees) for the person to charge for each laptop if there is a demand for 100 laptops?</p>""",
          excluded=("Price per unit from a revenue function (p = R(x)/x, average revenue) — a Section C commerce "
                    "application with no calculus; not in the ISC 2027 Class XII syllabus.")),

        Q("19(v)", 1, r"""<p>If the total cost function is given by \(C=x+2x^3-\dfrac72x^2\), find the Marginal Average Cost function (MAC).</p>""",
          a=r"""<p>Average cost \(AC=\dfrac Cx=1+2x^2-\dfrac72x\).</p>
<p>Marginal average cost \(MAC=\dfrac{d(AC)}{dx}=4x-\dfrac72\).</p>
<p><span class="box">\(MAC=4x-\dfrac72\)</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>\(AC=\dfrac{C(x)}{x}\); MAC is the derivative of AC (not of C).</li></ul>"""),

        Q("20", 2, r"""<p>The Average Cost function associated with producing and marketing x units of an item is given by
\(AC=x+5+\dfrac{36}{x}\)</p>
<p>(a) Find the Total Cost function.<br>(b) Find the range of values of x for which Average Cost is increasing.</p>""",
          a=r"""<p>(a) \(C=x\cdot AC=\) <span class="box">\(C(x)=x^2+5x+36\)</span></p>
<p>(b) \(\dfrac{d(AC)}{dx}=1-\dfrac{36}{x^2}\gt 0\iff x^2\gt 36\iff x\gt 6\) (output \(x\gt 0\)).</p>
{{fig:0}}
<p><span class="box">AC is increasing for \(x\gt 6\)</span></p>""",
          afig=[(F.fig_q20_ac, "AC falls up to x = 6 (minimum AC = 17) and rises after it.")],
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Total cost = output × average cost.</li>
<li>A function increases where its derivative is positive.</li></ul>"""),

        Q("20 (OR)", 2, r"""<p>The demand function of a monopoly is given by \(x=100-4p\). Find the quantity at which the MR will be zero.</p>""",
          a=r"""<p>\(p=\dfrac{100-x}{4}\); revenue \(R=px=\dfrac{100x-x^2}{4}\).</p>
<p>\(MR=\dfrac{dR}{dx}=\dfrac{100-2x}{4}=0\Rightarrow\) <span class="box">\(x=50\)</span></p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Express p in terms of x; \(R=px\), \(MR=\dfrac{dR}{dx}\).</li></ul>"""),

        Q("21", 4, r"""<p>Shown below is a data set that includes the average temperature and the number of ice cream cones sold per day by an
ice cream truck in a small town over the course of six days. Find the equation of the line of regression of y on x.</p>
<table class="data"><tr><th>Temperature (°F) X</th><th>Cones sold Y</th></tr>
<tr><td>65</td><td>180</td></tr><tr><td>75</td><td>250</td></tr><tr><td>60</td><td>160</td></tr>
<tr><td>70</td><td>210</td></tr><tr><td>80</td><td>300</td></tr><tr><td>70</td><td>220</td></tr></table>
<p class="note">[No mark is printed against Q21; Section C totals 15, so it carries 4.]</p>""",
          excluded=REGR.format("regression line of y on x")),

        Q("22", 4, r"""<p>A soap company manufactures two varieties of soap using two machines. The time taken on each machine to manufacture
one batch of each variety of soap is given below.</p>
<table class="data"><tr><th></th><th>Machine 1</th><th>Machine 2</th></tr>
<tr><th>Soap A</th><td>1 hour</td><td>1 hour</td></tr><tr><th>Soap B</th><td>2 hours</td><td>1 hour</td></tr></table>
<p>Machine 1 and Machine 2 cannot be operational for more than 12 and 10 hours in a day, respectively. The profit earned
from one batch of Soap A and one batch of Soap B is ₹ 3000 and ₹ 4000, respectively. Find the number of batches of each
kind of soap that should be made daily to maximise the profit</p>
<p class="note">[No mark is printed against Q22; Section C totals 15, so it carries 4.]</p>""",
          a=r"""<p>Let x batches of Soap A and y batches of Soap B be made daily.</p>
<p><b>Maximise</b> \(Z=3000x+4000y\) subject to</p>
<p>\(x+2y\le12\) (Machine 1), &nbsp; \(x+y\le10\) (Machine 2), &nbsp; \(x\ge0,\ y\ge0\).</p>
<p>Lines: \(x+2y=12\) through \((12,0),(0,6)\); \(x+y=10\) through \((10,0),(0,10)\). O satisfies both, so the region is on the origin side.</p>
<p>Intersection: subtract, \(y=2,\ x=8\).</p>
{{fig:0}}
<table class="data"><tr><th>Corner</th><td>O(0, 0)</td><td>A(10, 0)</td><td>P(8, 2)</td><td>C(0, 6)</td></tr>
<tr><th>Z = 3000x + 4000y</th><td>0</td><td>30000</td><td><b>32000</b></td><td>24000</td></tr></table>
<p>The feasible region is bounded, so the maximum is at a corner: \(Z_{\max}=32000\) at \((8,2)\).</p>
<p><span class="box">8 batches of Soap A and 2 batches of Soap B daily; maximum profit ₹ 32000</span></p>""",
          afig=[(F.fig_q22_lpp, "Feasible region OAPC; the dashed iso-profit line Z = 32000 touches it only at P(8, 2).")],
          topic="Linear Programming",
          recall=r"""<ul><li>Define the variables; write the objective function and every constraint, including non-negativity.</li>
<li>Bounded feasible region: the optimum is at a corner point — evaluate Z at each.</li></ul>"""),
    ])
