"""Heritage School Pre-Board 2013-14, Mathematics (Class XII). Transcribed from the page images."""
from kit import Q, SEC
import maths_2013_14_figs as F

CONICS = "Conic sections (ellipse/hyperbola) — Class XI Coordinate Geometry in ISC 2027; not in the Class XII syllabus"
REGR = "Correlation and regression — linear regression has been dropped; the ISC 2027 Class XII paper has no statistics unit"
COMPLEX = "Complex numbers — Class XI Algebra in ISC 2027; not in the Class XII syllabus"
BOOL = "Boolean algebra and switching circuits — not in the ISC 2027 Mathematics syllabus"
MVT = "Rolle's theorem / mean value theorems — not listed in ISC 2027 Class XII Calculus"
COMM = ("Financial mathematics (bills of exchange, discounting, annuities) — old Section C commerce topic; the ISC 2027 Class XII syllabus "
        "(Relations & Functions, Algebra, Calculus, Vectors, 3-D, LPP, Probability) has no such unit")
VGEOM = "Proof of a geometrical theorem by vectors — ISC 2027 Vector Algebra: 'Proofs of geometrical theorems by using Vector algebra are excluded'"
TRIPLE = ("Scalar triple product — ISC 2027 Vector Algebra lists only the dot and cross products "
          "(box product removed, as in the rationalised NCERT)")

STATS = ("Index numbers and moving averages (old Section C statistics) — the ISC 2027 Class XII syllabus has no statistics unit")

PAPER = dict(
    subject="maths",
    year="2013-14",
    slug="2013-14",
    paper="Mathematics",
    source="PreBoard-PYQ/2013-14/Mathematics.pdf",
    marks=100, time="3 hours",
    intro=r"""<p><em>(Candidates are allowed additional 15 minutes for only reading the paper.
They must NOT start writing during this time.)</em></p>
<p><b>Section A</b> – Answer Question 1 (compulsory) and <b>five</b> other questions.<br>
<b>Section B and Section C</b> – Answer <b>two</b> questions from <b>either</b> Section B <b>or</b> Section C.</p>
<p>All working, including rough work, should be done on the same sheet as, and adjacent to, the rest of the answer.</p>
<p>The intended marks for questions or parts of questions are given in brackets [ ].</p>
<p>Mathematical tables and graph papers are provided. Slide rule may be used.</p>""",
    items=[
        SEC("Section A"),
        # ------------------------------------------------------------- Q1
        Q("1(i)", 3, r"<p>Express the matrix \(A=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}\) as the sum of a symmetric and a skew-symmetric matrix.</p>",
          a=r"""<p>Every square matrix can be written as \(A=P+Q\) with \(P=\tfrac12(A+A')\) symmetric and \(Q=\tfrac12(A-A')\) skew-symmetric.</p>
<p>\(A'=\begin{bmatrix}3&1\\-4&-1\end{bmatrix}\).</p>
<p>\[P=\tfrac12(A+A')=\tfrac12\begin{bmatrix}6&-3\\-3&-2\end{bmatrix}=\begin{bmatrix}3&-\tfrac32\\-\tfrac32&-1\end{bmatrix},\qquad P'=P\ \text{(symmetric)}\]</p>
<p>\[Q=\tfrac12(A-A')=\tfrac12\begin{bmatrix}0&-5\\5&0\end{bmatrix}=\begin{bmatrix}0&-\tfrac52\\\tfrac52&0\end{bmatrix},\qquad Q'=-Q\ \text{(skew-symmetric)}\]</p>
<p>Check: \(P+Q=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}=A\).</p>
<p><span class="box">\(A=\begin{bmatrix}3&-\tfrac32\\-\tfrac32&-1\end{bmatrix}+\begin{bmatrix}0&-\tfrac52\\\tfrac52&0\end{bmatrix}\)</span></p>""",
          topic="Matrices",
          recall=r"<ul><li>\(A=\tfrac12(A+A')+\tfrac12(A-A')\).</li><li>Symmetric: \(P'=P\); skew-symmetric: \(Q'=-Q\) (diagonal entries 0).</li><li>Always verify the two parts add back to \(A\).</li></ul>"),
        Q("1(ii)", 3, r"<p>Determine K so that the straight line \(y=x+K\) may touch the ellipse \(2x^2+3y^2=1\).</p>", excluded=CONICS),
        Q("1(iii)", 3, r"<p>Solve for \(x\): \(\tan^{-1}(2x)+\tan^{-1}(3x)=\dfrac{\pi}{4}\).</p>",
          a=r"""<p>Using \(\tan^{-1}a+\tan^{-1}b=\tan^{-1}\dfrac{a+b}{1-ab}\) (valid when \(ab<1\)):</p>
<p>\[\tan^{-1}\frac{2x+3x}{1-6x^2}=\frac{\pi}{4}\ \Rightarrow\ \frac{5x}{1-6x^2}=1\ \Rightarrow\ 6x^2+5x-1=0\]</p>
<p>\[(6x-1)(x+1)=0\ \Rightarrow\ x=\tfrac16\ \text{or}\ x=-1.\]</p>
<p>Check: for \(x=-1\) the left side is \(\tan^{-1}(-2)+\tan^{-1}(-3)\), a sum of two negative angles, so it cannot equal \(\pi/4\); also \(ab=6>1\). Reject.</p>
<p>For \(x=\tfrac16\): \(\tan^{-1}\tfrac13+\tan^{-1}\tfrac12=\tan^{-1}\dfrac{5/6}{5/6}=\tan^{-1}1=\tfrac{\pi}{4}\). ✓</p>
<p><span class="box">\(x=\tfrac16\)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"<ul><li>\(\tan^{-1}a+\tan^{-1}b=\tan^{-1}\frac{a+b}{1-ab}\) for \(ab<1\).</li><li>Always substitute back: a root can make the left side negative or need \(ab>1\).</li></ul>"),
        Q("1(iv)", 3, r"<p>Evaluate: \(\displaystyle\lim_{x\to0}\frac{1-\cos x^2}{x^2\sin x^2}\).</p>",
          excluded="Evaluation of limits — Class XI Calculus in ISC 2027; the Class XII syllabus uses limits only inside continuity, not as a stand-alone question"),
        Q("1(v)", 3, r"<p>Evaluate: \(\displaystyle\int e^x\left(\frac{1+\sin x}{1+\cos x}\right)dx\).</p>",
          a=r"""<p>Use \(1+\cos x=2\cos^2\frac x2\) and \(\sin x=2\sin\frac x2\cos\frac x2\):</p>
<p>\[\frac{1+\sin x}{1+\cos x}=\frac{1}{2\cos^2\frac x2}+\frac{2\sin\frac x2\cos\frac x2}{2\cos^2\frac x2}=\tfrac12\sec^2\tfrac x2+\tan\tfrac x2.\]</p>
<p>So the integral has the form \(\int e^x\{f(x)+f'(x)\}\,dx\) with \(f(x)=\tan\frac x2\), \(f'(x)=\tfrac12\sec^2\frac x2\).</p>
<p>\[\int e^x\{f(x)+f'(x)\}dx=e^x f(x)+C\]</p>
<p><span class="box">\(\displaystyle\int e^x\frac{1+\sin x}{1+\cos x}\,dx=e^x\tan\frac x2+C\)</span></p>""",
          topic="Integrals",
          recall=r"<ul><li>\(\int e^x\{f(x)+f'(x)\}dx=e^xf(x)+C\) (from \((e^xf)'\)).</li><li>Half-angle forms: \(1+\cos x=2\cos^2\frac x2\), \(\sin x=2\sin\frac x2\cos\frac x2\).</li></ul>"),
        Q("1(vi)", 3, r"<p>If \(\displaystyle\int_0^K\frac{dx}{2+8x^2}=\frac{\pi}{16}\), then find K.</p>",
          a=r"""<p>\[\int_0^K\frac{dx}{2+8x^2}=\frac18\int_0^K\frac{dx}{x^2+\left(\frac12\right)^2}=\frac18\cdot\frac{1}{1/2}\Big[\tan^{-1}2x\Big]_0^K=\frac14\tan^{-1}2K.\]</p>
<p>\[\frac14\tan^{-1}2K=\frac{\pi}{16}\ \Rightarrow\ \tan^{-1}2K=\frac{\pi}{4}\ \Rightarrow\ 2K=1.\]</p>
<p><span class="box">\(K=\tfrac12\)</span></p>""",
          topic="Definite Integrals",
          recall=r"<ul><li>\(\int\frac{dx}{x^2+a^2}=\frac1a\tan^{-1}\frac xa+C\).</li><li>Take the coefficient of \(x^2\) out first.</li></ul>"),
        Q("1(vii)", 3, r"<p>The equation of two regression lines in correlation analysis are \(2x+3y=10\) &amp; \(4x+y=5\). Find the correlation co-efficient.</p>", excluded=REGR),
        Q("1(viii)", 3, r"<p>Find the locus of a complex number \(Z=x+iy\) satisfying the relation \(\left|\dfrac{z-2i}{z+2i}\right|=\sqrt2\).</p>", excluded=COMPLEX),
        Q("1(ix)", 3, r"<p>Find the particular solution of \(y(1-x^2)\,dy+x(1-y^2)\,dx=0\) given that \(y=1\) when \(x=0\).</p>",
          a=r"""<p><b>Separating the variables</b> (for \(x^2\ne1,\ y^2\ne1\)):</p>
<p>\[\frac{y\,dy}{1-y^2}=-\frac{x\,dx}{1-x^2}.\]</p>
<p>Integrate: \(-\tfrac12\log|1-y^2|=\tfrac12\log|1-x^2|+c\), i.e.</p>
<p>\[\log|1-y^2|+\log|1-x^2|=-2c\ \Rightarrow\ \boxed{(1-x^2)(1-y^2)=C}\quad\text{(general solution).}\]</p>
<p><b>Particular solution.</b> Putting \(x=0,\ y=1\): \(C=(1)(0)=0\), so \((1-x^2)(1-y^2)=0\). Near \(x=0\) the factor \(1-x^2\ne0\), so \(1-y^2=0\), and the branch through \((0,1)\) is</p>
<p><span class="box">\(y=1\)</span></p>
<p>Check: with \(y=1\), \(dy=0\) and \(1-y^2=0\), so both terms of the equation vanish. ✓</p>
<p class="note">[The given condition lies on the line \(y=1\), where the separation step divides by \(1-y^2=0\); the answer is therefore the constant solution. The question was very likely meant to read \(y(1+x^2)dy+x(1+y^2)dx=0\): then \(\frac{y\,dy}{1+y^2}=-\frac{x\,dx}{1+x^2}\) gives \((1+x^2)(1+y^2)=C\), and \(y=1\) at \(x=0\) gives the particular solution \((1+x^2)(1+y^2)=2\).]</p>""",
          topic="Differential Equations",
          recall=r"<ul><li>Variable separable: collect \(y\) with \(dy\), \(x\) with \(dx\), integrate both sides, one constant.</li><li>\(\int\frac{x\,dx}{1\pm x^2}=\pm\frac12\log|1\pm x^2|\).</li><li>Particular solution: substitute the condition to fix \(C\).</li></ul>"),
        Q("1(x)", 3, r"<p>Bag P contains 5 red and 3 green balls and bag Q contains 3 red and 4 green balls. A ball is transferred from bag P to Q and then a ball is drawn from bag Q. What is the probability that the ball drawn is green?</p>",
          a=r"""<p>Let \(E_1\): the transferred ball is red, \(E_2\): it is green; \(G\): the ball drawn from Q is green.</p>
{{fig:0}}
<p>\(P(E_1)=\tfrac58,\ P(E_2)=\tfrac38\). After transfer Q has 8 balls:</p>
<p>\(P(G\mid E_1)=\tfrac48\) (3 red + 1 red, 4 green); \(P(G\mid E_2)=\tfrac58\) (3 red, 4 + 1 green).</p>
<p>By the theorem of total probability,</p>
<p>\[P(G)=\tfrac58\cdot\tfrac48+\tfrac38\cdot\tfrac58=\tfrac{20}{64}+\tfrac{15}{64}=\tfrac{35}{64}.\]</p>
<p><span class="box">\(P(\text{green})=\dfrac{35}{64}\)</span></p>""",
          topic="Probability",
          afig=[(F.fig_tree_transfer, "First stage: the ball moved from P; second stage: the ball drawn from Q.")],
          recall=r"<ul><li>Total probability: \(P(A)=\sum P(E_i)P(A\mid E_i)\) over a partition \(E_1,E_2,\dots\)</li><li>Recount the second bag after the transfer (it now holds 8 balls).</li></ul>"),
        # ------------------------------------------------------------- Q2
        Q("2(a)", 5, r"""<p>Using properties of determinants, prove that:</p>
<p>\[\begin{vmatrix}b+c&c+a&a+b\\c+a&a+b&b+c\\a+b&b+c&c+a\end{vmatrix}=-2(a^3+b^3+c^3-3abc)\]</p>""",
          a=r"""<p>Let \(\Delta\) be the determinant. Apply \(C_1\to C_1+C_2+C_3\); every entry of \(C_1\) becomes \(2(a+b+c)\):</p>
<p>\[\Delta=\begin{vmatrix}2(a+b+c)&c+a&a+b\\2(a+b+c)&a+b&b+c\\2(a+b+c)&b+c&c+a\end{vmatrix}=2(a+b+c)\begin{vmatrix}1&c+a&a+b\\1&a+b&b+c\\1&b+c&c+a\end{vmatrix}\]</p>
<p>(taking the common factor \(2(a+b+c)\) out of \(C_1\)). Now \(R_2\to R_2-R_1,\ R_3\to R_3-R_1\):</p>
<p>\[\Delta=2(a+b+c)\begin{vmatrix}1&c+a&a+b\\0&b-c&c-a\\0&b-a&c-b\end{vmatrix}\]</p>
<p>Expanding along \(C_1\):</p>
<p>\[\begin{aligned}\Delta&=2(a+b+c)\big[(b-c)(c-b)-(c-a)(b-a)\big]\\&=2(a+b+c)\big[-(b^2-2bc+c^2)-(bc-ab-ac+a^2)\big]\\&=-2(a+b+c)(a^2+b^2+c^2-ab-bc-ca).\end{aligned}\]</p>
<p>Since \(a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)\),</p>
<p><span class="box">\(\Delta=-2(a^3+b^3+c^3-3abc)\)</span> &nbsp;Hence proved.</p>""",
          topic="Determinants",
          recall=r"<ul><li>Adding all columns to one column does not change the determinant; a common factor of a row/column comes out.</li><li>\(R_i\to R_i-R_j\) creates zeros without changing the value.</li><li>\(a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)\).</li></ul>"),
        Q("2(b)", 5, r"""<p>Find \(A^{-1}\) when \(A=\begin{bmatrix}4&2&3\\1&1&1\\3&1&-2\end{bmatrix}\). Hence solve the system of equations</p>
<p>\(4x+2y+3z=2,\ x+y+z=1,\ 3x+y-2z=5\).</p>
<p class="note">[Unclear in the original: the first row of \(A\) is cut off at the page break of the scan. It is read as \(4\ \ 2\ \ 3\), the coefficients of the first equation, which the 'hence' requires.]</p>""",
          a=r"""<p>\(|A|=4(-2-1)-2(-2-3)+3(1-3)=-12+10-6=-8\ne0\), so \(A^{-1}\) exists.</p>
<p>Cofactors: \(A_{11}=-3,\ A_{12}=5,\ A_{13}=-2;\ A_{21}=7,\ A_{22}=-17,\ A_{23}=2;\ A_{31}=-1,\ A_{32}=-1,\ A_{33}=2.\)</p>
<p>\[\operatorname{adj}A=\begin{bmatrix}-3&7&-1\\5&-17&-1\\-2&2&2\end{bmatrix},\qquad A^{-1}=\frac{\operatorname{adj}A}{|A|}=-\frac18\begin{bmatrix}-3&7&-1\\5&-17&-1\\-2&2&2\end{bmatrix}.\]</p>
<p>The system is \(AX=B\) with \(X=\begin{bmatrix}x\\y\\z\end{bmatrix},\ B=\begin{bmatrix}2\\1\\5\end{bmatrix}\), so \(X=A^{-1}B\):</p>
<p>\[X=-\frac18\begin{bmatrix}-6+7-5\\10-17-5\\-4+2+10\end{bmatrix}=-\frac18\begin{bmatrix}-4\\-12\\8\end{bmatrix}=\begin{bmatrix}\tfrac12\\\tfrac32\\-1\end{bmatrix}.\]</p>
<p><span class="box">\(x=\tfrac12,\ y=\tfrac32,\ z=-1\)</span></p>
<p>Check: \(4(\tfrac12)+2(\tfrac32)+3(-1)=2\) ✓, \(\tfrac12+\tfrac32-1=1\) ✓, \(\tfrac32+\tfrac32+2=5\) ✓.</p>""",
          topic="Matrices and Determinants",
          recall=r"<ul><li>\(A^{-1}=\dfrac{\operatorname{adj}A}{|A|}\); adj A is the transpose of the cofactor matrix.</li><li>Cofactor \(A_{ij}=(-1)^{i+j}M_{ij}\).</li><li>\(AX=B\Rightarrow X=A^{-1}B\) when \(|A|\ne0\).</li></ul>"),
        # ------------------------------------------------------------- Q3
        Q("3(a)", 5, r"""<p>Construct a switching circuit representing the polynomial: \(P(P+Q)Q(Q+R')\).</p>
<p>Use Boolean Algebra to simplify the expression and construct the simplified switching circuit.</p>""", excluded=BOOL),
        Q("3(b)", 5, r"<p>Prove that: \(\sin\!\left(2\tan^{-1}\dfrac35-\sin^{-1}\dfrac{7}{25}\right)=\dfrac{304}{425}\).</p>",
          a=r"""<p>Let \(\alpha=\tan^{-1}\frac35\) and \(\beta=\sin^{-1}\frac{7}{25}\) (both acute).</p>
<p>With \(\tan\alpha=\frac35\):</p>
<p>\[\sin2\alpha=\frac{2\tan\alpha}{1+\tan^2\alpha}=\frac{6/5}{34/25}=\frac{15}{17},\qquad \cos2\alpha=\frac{1-\tan^2\alpha}{1+\tan^2\alpha}=\frac{16/25}{34/25}=\frac{8}{17}.\]</p>
<p>With \(\sin\beta=\frac7{25}\): \(\cos\beta=\sqrt{1-\frac{49}{625}}=\frac{24}{25}\).</p>
<p>\[\sin(2\alpha-\beta)=\sin2\alpha\cos\beta-\cos2\alpha\sin\beta=\frac{15}{17}\cdot\frac{24}{25}-\frac{8}{17}\cdot\frac{7}{25}=\frac{360-56}{425}.\]</p>
<p><span class="box">\(\sin\!\left(2\tan^{-1}\tfrac35-\sin^{-1}\tfrac7{25}\right)=\dfrac{304}{425}\)</span> &nbsp;Hence proved.</p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"<ul><li>\(\sin2\theta=\frac{2\tan\theta}{1+\tan^2\theta}\), \(\cos2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}\).</li><li>\(\sin(A-B)=\sin A\cos B-\cos A\sin B\).</li><li>Name each inverse-trig term as an angle and read its other ratios off a right triangle.</li></ul>"),
        # ------------------------------------------------------------- Q4
        Q("4(a)", 5, r"<p>Using Rolle's theorem, find a point on the curve \(y=\sin x+\cos x-1,\ x\in\left[0,\dfrac{\pi}{2}\right]\) where the tangent is parallel to the x-axis.</p>", excluded=MVT),
        Q("4(b)", 5, r"<p>Find the equation of the hyperbola whose foci are \((4,1)\) and \((8,1)\) with eccentricity 2.</p>", excluded=CONICS),
        # ------------------------------------------------------------- Q5
        Q("5(a)", 5, r"<p>If \(x=\sin\phi,\ y=\sin\lambda\phi\), then prove that \((1-x^2)\dfrac{d^2y}{dx^2}-x\dfrac{dy}{dx}+\lambda^2y=0\).</p>",
          a=r"""<p>\(\dfrac{dx}{d\phi}=\cos\phi,\quad\dfrac{dy}{d\phi}=\lambda\cos\lambda\phi\), so</p>
<p>\[\frac{dy}{dx}=\frac{\lambda\cos\lambda\phi}{\cos\phi}.\]</p>
<p>Since \(\cos\phi=\sqrt{1-x^2}\) and \(\cos\lambda\phi=\sqrt{1-y^2}\) (up to sign, which squaring removes):</p>
<p>\[\sqrt{1-x^2}\,y_1=\lambda\cos\lambda\phi\ \Rightarrow\ (1-x^2)y_1^2=\lambda^2\cos^2\lambda\phi=\lambda^2(1-y^2).\]</p>
<p>Differentiate both sides with respect to \(x\):</p>
<p>\[(1-x^2)\,2y_1y_2-2x\,y_1^2=-2\lambda^2y\,y_1.\]</p>
<p>Divide by \(2y_1\) (\(y_1\ne0\)):</p>
<p><span class="box">\((1-x^2)\dfrac{d^2y}{dx^2}-x\dfrac{dy}{dx}+\lambda^2y=0\)</span> &nbsp;Hence proved.</p>""",
          topic="Differentiation (second order)",
          recall=r"<ul><li>Parametric: \(\frac{dy}{dx}=\frac{dy/d\phi}{dx/d\phi}\).</li><li>Square first to clear roots, then differentiate implicitly — much shorter than differentiating the quotient.</li><li>\(\frac{d}{dx}(y_1^2)=2y_1y_2\).</li></ul>"),
        Q("5(b)", 5, r"<p>A cone is inscribed in a sphere of radius \(r\). If the volume of the cone is maximum then find the height of the cone.</p>",
          a=r"""<p>Let the cone have height \(h\) and base radius \(\rho\); its vertex V is on the sphere and its axis passes through the centre O.</p>
{{fig:0}}
<p>In the right triangle formed by O, the base centre M and a point on the base rim: \(OM=h-r\), so</p>
<p>\[\rho^2=r^2-(h-r)^2=2rh-h^2.\]</p>
<p>\[V=\frac13\pi\rho^2h=\frac{\pi}{3}(2rh^2-h^3),\qquad 0&lt;h&lt;2r.\]</p>
<p>\[\frac{dV}{dh}=\frac{\pi}{3}(4rh-3h^2)=0\ \Rightarrow\ h=\frac{4r}{3}\quad(h\ne0).\]</p>
<p>\[\frac{d^2V}{dh^2}=\frac{\pi}{3}(4r-6h)\Big|_{h=4r/3}=-\frac{4\pi r}{3}&lt;0,\]</p>
<p>so V is maximum there.</p>
<p><span class="box">Height of the cone \(=\dfrac{4r}{3}\)</span> &nbsp;(maximum volume \(=\frac{32}{81}\pi r^3=\frac{8}{27}\times\) volume of the sphere).</p>""",
          topic="Applications of Derivatives (maxima and minima)",
          afig=[(F.fig_cone_in_sphere, "Section through the axis, drawn to scale with h = 4r/3.")],
          recall=r"<ul><li>Express the quantity in one variable using the geometry (Pythagoras in the axial section).</li><li>\(V_{\text{cone}}=\frac13\pi\rho^2h\).</li><li>Second-derivative test: \(f''&lt;0\) ⇒ maximum.</li></ul>"),
        # ------------------------------------------------------------- Q6
        Q("6(a)", 5, r"<p>Evaluate: \(\displaystyle\int\frac{\cos x}{(1+\sin x)(2+\sin x)}\,dx\).</p>",
          a=r"""<p>Put \(\sin x=t\), \(\cos x\,dx=dt\):</p>
<p>\[I=\int\frac{dt}{(1+t)(2+t)}.\]</p>
<p>Partial fractions: \(\dfrac{1}{(1+t)(2+t)}=\dfrac{A}{1+t}+\dfrac{B}{2+t}\); \(t=-1\Rightarrow A=1\); \(t=-2\Rightarrow B=-1\).</p>
<p>\[I=\int\left(\frac{1}{1+t}-\frac{1}{2+t}\right)dt=\log|1+t|-\log|2+t|+C.\]</p>
<p><span class="box">\(I=\log\left|\dfrac{1+\sin x}{2+\sin x}\right|+C\)</span></p>""",
          topic="Integrals (substitution, partial fractions)",
          recall=r"<ul><li>Spot \(f'(x)\) beside \(f(x)\): here \(\cos x\) is \((\sin x)'\).</li><li>Distinct linear factors: \(\frac{1}{(t-a)(t-b)}=\frac{A}{t-a}+\frac{B}{t-b}\), cover-up rule.</li></ul>"),
        Q("6(b)", 5, r"<p>Find the area of the region bounded by the curve \(y^2=4x\) and the straight line \(y=2x-4\).</p>",
          a=r"""<p><b>Points of intersection.</b> From the line, \(x=\frac{y+4}{2}\). Substituting in \(y^2=4x\): \(y^2=2y+8\Rightarrow y^2-2y-8=0\Rightarrow y=4\) or \(y=-2\). The points are \(A(4,4)\) and \(B(1,-2)\).</p>
{{fig:0}}
<p>Integrating with respect to \(y\) (the line is to the right of the parabola for \(-2&lt;y&lt;4\)):</p>
<p>\[\text{Area}=\int_{-2}^{4}\left[\frac{y+4}{2}-\frac{y^2}{4}\right]dy=\left[\frac{y^2}{4}+2y-\frac{y^3}{12}\right]_{-2}^{4}\]</p>
<p>\[=\left(4+8-\tfrac{16}{3}\right)-\left(1-4+\tfrac{2}{3}\right)=\tfrac{20}{3}+\tfrac{7}{3}=9.\]</p>
<p><span class="box">Area \(=9\) square units</span></p>""",
          topic="Application of Integrals (area)",
          afig=[(F.fig_area_parabola_line, "The region between y² = 4x and y = 2x − 4.")],
          recall=r"<ul><li>Find the intersection points first; they are the limits.</li><li>When the region is bounded left/right, integrate in \(y\): \(\int(x_{\text{right}}-x_{\text{left}})\,dy\).</li><li>Area is always positive — sketch to see which curve is on the right.</li></ul>"),
        # ------------------------------------------------------------- Q7
        Q("7(a)", 5, r"""<p>Ten candidates received percentage marks in two subjects as follows:</p>
<div class="tbl"><table><tr><th>Candidate</th><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td></tr>
<tr><th>Mathematics</th><td>80</td><td>88</td><td>76</td><td>74</td><td>68</td><td>65</td><td>40</td><td>43</td><td>40</td><td>80</td></tr>
<tr><th>Statistics</th><td>72</td><td>84</td><td>90</td><td>66</td><td>54</td><td>50</td><td>54</td><td>38</td><td>30</td><td>43</td></tr></table></div>
<p>Calculate Spearman's correlation coefficient and interpret your result.</p>""", excluded=REGR),
        Q("7(b)", 5, r"""<p>You are given the following data:</p>
<div class="tbl"><table><tr><th></th><th>X</th><th>Y</th></tr><tr><td>MEAN</td><td>36</td><td>85</td></tr><tr><td>STANDARD DEVIATION</td><td>11</td><td>8</td></tr></table></div>
<p>The Coefficient of correlation between X and Y is 0.66. Find the two regressions and the most likely value of Y when X = 10.</p>""", excluded=REGR),
        # ------------------------------------------------------------- Q8
        Q("8(a)", 5, r"""<p>An urn contains 9 balls, 2 of which are white, 3 blue and 4 black. 3 balls are drawn at random. What is the chance that:</p>
<p>(i) Three balls will be of different colors?<br>(ii) 2 balls will be of same colors and third of different color?<br>(iii) 3 balls will be of same color?</p>""",
          a=r"""<p>Total number of ways of drawing 3 balls from 9: \(\binom93=84\).</p>
<p><b>(i)</b> One of each colour: \(\binom21\binom31\binom41=2\cdot3\cdot4=24\).</p>
<p>\[P=\frac{24}{84}=\frac27.\]</p>
<p><b>(iii)</b> All three the same colour: only blue or black is possible (there are just 2 white): \(\binom33+\binom43=1+4=5\).</p>
<p>\[P=\frac{5}{84}.\]</p>
<p><b>(ii)</b> Exactly two of one colour and the third different:</p>
<p>\(\binom22\cdot7+\binom32\cdot6+\binom42\cdot5=7+18+30=55\), so \(P=\dfrac{55}{84}\).</p>
<p>(Check: the three cases are exhaustive, \(24+55+5=84\).)</p>
<p><span class="box">(i) \(\tfrac27\) &nbsp; (ii) \(\tfrac{55}{84}\) &nbsp; (iii) \(\tfrac{5}{84}\)</span></p>""",
          topic="Probability",
          recall=r"<ul><li>Classical probability with combinations: favourable \(\binom{}{}\) products over \(\binom{n}{r}\).</li><li>Mutually exclusive, exhaustive cases must add to the total — a free check.</li></ul>"),
        Q("8(b)", 5, r"<p>A and B cut a pack of 52 playing cards alternately and every time the card is put back. The pack is shuffled after each cut. A starts the game and the one who cuts a heart first wins. Find the probability that B wins the game.</p>",
          a=r"""<p>On each cut, \(p=P(\text{heart})=\frac{13}{52}=\frac14\), \(q=\frac34\); cuts are independent (the card is replaced and the pack shuffled).</p>
<p>B wins on the 2nd, 4th, 6th, … cut:</p>
<p>\[P(B)=qp+q^3p+q^5p+\cdots=\frac{qp}{1-q^2}\quad\text{(infinite G.P., ratio }q^2&lt;1).\]</p>
<p>\[P(B)=\frac{\frac34\cdot\frac14}{1-\frac9{16}}=\frac{3/16}{7/16}=\frac37.\]</p>
<p><span class="box">\(P(\text{B wins})=\dfrac37\)</span> &nbsp;(and \(P(\text{A wins})=\frac47\)).</p>""",
          topic="Probability (independent events)",
          recall=r"<ul><li>Independent trials: multiply probabilities along the sequence of failures then success.</li><li>Sum of infinite G.P.: \(\frac{a}{1-r}\), \(|r|&lt;1\).</li><li>First player: \(\frac{p}{1-q^2}\); second: \(\frac{qp}{1-q^2}\).</li></ul>"),
        # ------------------------------------------------------------- Q9
        Q("9(a)", 5, r"<p>Using De Moivre's Theorem find the least of n for which the expression \(\left(\dfrac{\sqrt3+3i}{2\sqrt3}\right)^{2n-1}\) is purely real.</p>", excluded=COMPLEX),
        Q("9(b)", 5, r"<p>Solve the differential equation: \(\left(\dfrac{e^{-2\sqrt x}}{\sqrt x}-\dfrac{y}{\sqrt x}\right)\dfrac{dx}{dy}=1,\ (x\ne0)\).</p>",
          a=r"""<p>Rewrite: \(\dfrac{dy}{dx}=\dfrac{e^{-2\sqrt x}}{\sqrt x}-\dfrac{y}{\sqrt x}\), i.e.</p>
<p>\[\frac{dy}{dx}+\frac{1}{\sqrt x}\,y=\frac{e^{-2\sqrt x}}{\sqrt x},\]</p>
<p>a linear equation \(\frac{dy}{dx}+Py=Q\) with \(P=\frac1{\sqrt x}\), \(Q=\frac{e^{-2\sqrt x}}{\sqrt x}\).</p>
<p>Integrating factor: \(\int P\,dx=\int x^{-1/2}dx=2\sqrt x\), so \(\text{I.F.}=e^{2\sqrt x}\).</p>
<p>Solution: \(y\cdot\text{I.F.}=\int Q\cdot\text{I.F.}\,dx+C\):</p>
<p>\[y\,e^{2\sqrt x}=\int\frac{e^{-2\sqrt x}}{\sqrt x}\,e^{2\sqrt x}dx=\int x^{-1/2}dx=2\sqrt x+C.\]</p>
<p><span class="box">\(y\,e^{2\sqrt x}=2\sqrt x+C\)</span></p>""",
          topic="Differential Equations (linear)",
          recall=r"<ul><li>Linear form \(\frac{dy}{dx}+Py=Q\): I.F. \(=e^{\int P\,dx}\), solution \(y\cdot\text{I.F.}=\int Q\cdot\text{I.F.}\,dx+C\).</li><li>Turn \(\frac{dx}{dy}\) upside-down first to see which variable is dependent.</li></ul>"),
        # ------------------------------------------------------------- Section B
        SEC("Section B", "(Attempt any two question)"),
        Q("10(a)", 5, r"<p>If \(\vec a,\vec b,\vec c\) are three vectors, prove that \(\vec a\cdot\left[(\vec b+\vec c)\times(\vec a+2\vec b+3\vec c)\right]=\left[\vec a\ \vec b\ \vec c\right]\).</p>", excluded=TRIPLE),
        Q("10(b)", 5, r"<p>Using vectors prove that in any triangle ABC, \(a=b\cos C+c\cos B\).</p>", excluded=VGEOM),
        Q("11(a)", 5, r"<p>Find the vector equation of the plane containing the line \(\dfrac{x+2}{2}=\dfrac{y+3}{3}=\dfrac{z-4}{-2}\) and the point \((0,6,0)\).</p>",
          a=r"""<p>The line passes through \(A(-2,-3,4)\) with direction \(\vec b=2\hat i+3\hat j-2\hat k\). The plane also contains \(P(0,6,0)\), so it contains \(\overrightarrow{AP}=2\hat i+9\hat j-4\hat k\).</p>
<p>A normal to the plane is perpendicular to both:</p>
<p>\[\vec n=\vec b\times\overrightarrow{AP}=\begin{vmatrix}\hat i&\hat j&\hat k\\2&3&-2\\2&9&-4\end{vmatrix}\]</p>
<p>\[\vec n=(-12+18)\hat i-(-8+4)\hat j+(18-6)\hat k=6\hat i+4\hat j+12\hat k.\]</p>
<p>Take \(\vec n=3\hat i+2\hat j+6\hat k\). The plane through \(P\): \(\vec r\cdot\vec n=\vec p\cdot\vec n=0+12+0=12\).</p>
<p><span class="box">\(\vec r\cdot(3\hat i+2\hat j+6\hat k)=12\)</span> &nbsp;(Cartesian: \(3x+2y+6z=12\)).</p>
<p>Check with A: \(-6-6+24=12\) ✓.</p>""",
          topic="Three-dimensional Geometry (planes)",
          recall=r"<ul><li>A plane through a line and a point: normal \(=\) line direction \(\times\) (vector from a point of the line to the given point).</li><li>Plane through \(\vec a\) with normal \(\vec n\): \(\vec r\cdot\vec n=\vec a\cdot\vec n\).</li></ul>"),
        Q("11(b)", 5, r"<p>Find the vector equation of the line passing through the point \((2,3,2)\) and parallel to the line \(\vec r=-2\hat i+3\hat j+\lambda(2\hat i-3\hat j+6\hat k)\) and find the distance between them.</p>",
          a=r"""<p>Parallel lines have the same direction \(\vec b=2\hat i-3\hat j+6\hat k\). Required line:</p>
<p><span class="box">\(\vec r=2\hat i+3\hat j+2\hat k+\mu(2\hat i-3\hat j+6\hat k)\)</span></p>
<p><b>Distance between the parallel lines</b> \(\vec r=\vec a_1+\lambda\vec b\) and \(\vec r=\vec a_2+\mu\vec b\):</p>
<p>\[d=\frac{|(\vec a_2-\vec a_1)\times\vec b|}{|\vec b|}\]</p>
<p>Here \(\vec a_1=-2\hat i+3\hat j\), \(\vec a_2=2\hat i+3\hat j+2\hat k\), so \(\vec a_2-\vec a_1=4\hat i+0\hat j+2\hat k\).</p>
<p>\[(\vec a_2-\vec a_1)\times\vec b=\begin{vmatrix}\hat i&\hat j&\hat k\\4&0&2\\2&-3&6\end{vmatrix}=(0+6)\hat i-(24-4)\hat j+(-12-0)\hat k\]</p>
<p>\[=6\hat i-20\hat j-12\hat k.\]</p>
<p>\(|6\hat i-20\hat j-12\hat k|=\sqrt{36+400+144}=\sqrt{580}=2\sqrt{145}\); \(|\vec b|=\sqrt{4+9+36}=7\).</p>
<p><span class="box">\(d=\dfrac{2\sqrt{145}}{7}\approx3.44\) units</span></p>""",
          topic="Three-dimensional Geometry (lines)",
          recall=r"<ul><li>Line through \(\vec a\) parallel to \(\vec b\): \(\vec r=\vec a+\lambda\vec b\).</li><li>Distance between parallel lines: \(\frac{|(\vec a_2-\vec a_1)\times\vec b|}{|\vec b|}\).</li></ul>"),
        Q("12(a)", 5, r"<p>In a bolt factory machines \(M_1,M_2\) and \(M_3\) manufacture respectively 25, 35, and 40 percent of the total of their output, out of which 5, 4 and 2 percent respectively are defective bolts. One bolt is drawn at random from the product and is found defective. What is the probability that it is manufactured in the machine \(M_2\)?</p>",
          a=r"""<p>Let \(E_1,E_2,E_3\): the bolt is made by \(M_1,M_2,M_3\); \(D\): the bolt is defective.</p>
{{fig:0}}
<p>\(P(E_1)=0.25,\ P(E_2)=0.35,\ P(E_3)=0.40\); \(P(D|E_1)=0.05,\ P(D|E_2)=0.04,\ P(D|E_3)=0.02\).</p>
<p>Total probability: \(P(D)=0.25(0.05)+0.35(0.04)+0.40(0.02)=0.0125+0.0140+0.0080=0.0345\).</p>
<p>By Bayes' theorem,</p>
<p>\[P(E_2\mid D)=\frac{P(E_2)P(D|E_2)}{\sum P(E_i)P(D|E_i)}=\frac{0.0140}{0.0345}=\frac{140}{345}=\frac{28}{69}.\]</p>
<p><span class="box">\(P(M_2\mid\text{defective})=\dfrac{28}{69}\approx0.406\)</span></p>""",
          topic="Probability (Bayes' theorem)",
          afig=[(F.fig_tree_bolts, "Machine first, then defective or good.")],
          recall=r"<ul><li>Bayes: \(P(E_i|A)=\dfrac{P(E_i)P(A|E_i)}{\sum_j P(E_j)P(A|E_j)}\).</li><li>The denominator is the total probability of the observed event.</li></ul>"),
        Q("12(b)", 5, r"<p>Four defective oranges are accidently mixed with sixteen good ones. Three oranges are drawn from the mixed lot. Find the probability distribution of x, the number of defective oranges.</p>",
          a=r"""<p>The lot has 20 oranges (4 defective, 16 good); 3 are drawn together (without replacement), so \(x\in\{0,1,2,3\}\) and \(\binom{20}{3}=1140\).</p>
<p>\[P(x=k)=\frac{\binom4k\binom{16}{3-k}}{\binom{20}{3}}\]</p>
<div class="tbl"><table><tr><th>\(x\)</th><td>0</td><td>1</td><td>2</td><td>3</td></tr>
<tr><th>favourable</th><td>\(\binom{16}{3}=560\)</td><td>\(4\cdot\binom{16}{2}=480\)</td><td>\(\binom42\cdot16=96\)</td><td>\(\binom43=4\)</td></tr>
<tr><th>\(P(x)\)</th><td>\(\frac{28}{57}\)</td><td>\(\frac{8}{19}\)</td><td>\(\frac{8}{95}\)</td><td>\(\frac{1}{285}\)</td></tr></table></div>
<p>Check: \(560+480+96+4=1140\), so the probabilities add to 1. (Mean \(=\sum xP(x)=\frac{480+192+12}{1140}=0.6\).)</p>
<p><span class="box">\(P(0)=\frac{28}{57},\ P(1)=\frac{8}{19},\ P(2)=\frac{8}{95},\ P(3)=\frac{1}{285}\)</span></p>""",
          topic="Probability (random variable and its distribution)",
          recall=r"<ul><li>A probability distribution lists every value of the random variable with its probability; they must total 1.</li><li>Drawing without replacement: \(\binom{\text{def}}{k}\binom{\text{good}}{n-k}/\binom{N}{n}\).</li><li>Mean \(=\sum x_iP(x_i)\).</li></ul>"),
        # ------------------------------------------------------------- Section C
        SEC("Section C", "(Attempt any two question)"),
        Q("13(a)", 5, r"<p>A bill for Rs 65000 drawn on January 18, 2013 at 7 months was discounted at a bank on March 21, 2013, @ of interest being 6% per annum. How much did the holder receive?</p>", excluded=COMM),
        Q("13(b)", 5, r"<p>A man buys a machine on installment basis such that he pays Rs 5000 on signing of the contract and remaining in 4 equal installment of Rs 10000 the first being paid at the end of the first year and so far each year. If the rate of interest is 8% compounded annually find the cash down price of the machine.</p>", excluded=COMM),
        Q("14(a)", 5, r"<p>A company produces soft drinks that has a contract which requires that a minimum of 80 units of chemical A and 60 units of chemical B to go into each bottle of the drink. The chemicals are available in a prepared mixture from two different suppliers. Supplier S has a mix of 4 units of A and 2 units of B that cost Rs 10, and supplier T has a mix of 1 unit of A and 1 unit of B that cost Rs 4. How many mixes from S and T should the company purchase to honor contract requirement and yet minimize cost?</p>",
          a=r"""<p><b>Formulation.</b> Let \(x\) mixes be bought from S and \(y\) from T.</p>
<p>Minimise \(Z=10x+4y\) subject to</p>
<p>\[4x+y\ge80\ \text{(chemical A)},\qquad 2x+y\ge60\ \text{(chemical B)},\qquad x\ge0,\ y\ge0.\]</p>
<p><b>Graph.</b> \(4x+y=80\) meets the axes at \((20,0),(0,80)\); \(2x+y=60\) at \((30,0),(0,60)\). Both inequalities are \(\ge\), so the feasible region lies on the side away from the origin (O does not satisfy them). The lines meet where \(2x=20\): \(x=10,\ y=40\).</p>
{{fig:0}}
<p>The feasible region is unbounded with corner points \(A(0,80),\ B(10,40),\ C(30,0)\).</p>
<div class="tbl"><table><tr><th>Corner</th><th>\(Z=10x+4y\)</th></tr><tr><td>A(0, 80)</td><td>320</td></tr><tr><td>B(10, 40)</td><td><b>260</b></td></tr><tr><td>C(30, 0)</td><td>300</td></tr></table></div>
<p>Since the region is unbounded, check the open half-plane \(10x+4y&lt;260\): it has no point in common with the feasible region (the dashed line touches the region only at B). So 260 is the minimum.</p>
<p><span class="box">Buy 10 mixes from S and 40 from T; minimum cost Rs 260</span></p>""",
          topic="Linear Programming",
          afig=[(F.fig_lpp_drinks, "Feasible region (shaded, unbounded) and the minimum-cost line through B.")],
          recall=r"<ul><li>Formulate: decision variables, objective, constraints, non-negativity.</li><li>Corner-point method; for an unbounded region confirm the optimum by checking the half-plane \(Z&lt;Z_{\min}\) (or \(&gt;Z_{\max}\)).</li><li>'Minimum of … units' gives \(\ge\) constraints.</li></ul>"),
        Q("14(b)", 5, r"<p>The cost function of a firm is \(c(x)=5x^2+28x+5\) where 'c' is the cost &amp; 'x' is the level of output. A tax at the rate of Rs 2 per unit output is imposed and the producer adds it to his cost. Find the minimum value of the average cost.</p>",
          a=r"""<p>With the tax of Rs 2 per unit added, the new total cost is</p>
<p>\[C(x)=5x^2+28x+5+2x=5x^2+30x+5.\]</p>
<p>Average cost: \[AC(x)=\frac{C(x)}{x}=5x+30+\frac{5}{x},\qquad x&gt;0.\]</p>
<p>\[\frac{d(AC)}{dx}=5-\frac{5}{x^2}=0\ \Rightarrow\ x^2=1\ \Rightarrow\ x=1\quad(x&gt;0).\]</p>
<p>\[\frac{d^2(AC)}{dx^2}=\frac{10}{x^3}=10&gt;0\ \text{at}\ x=1,\]</p>
<p>so AC is minimum at \(x=1\): \(AC(1)=5+30+5=40\).</p>
<p><span class="box">Minimum average cost \(=\) Rs 40 (at output \(x=1\) unit)</span></p>""",
          topic="Applications of Derivatives (maxima and minima)",
          recall=r"<ul><li>Average cost \(AC=\dfrac{C(x)}{x}\); a per-unit tax \(t\) adds \(tx\) to \(C(x)\).</li><li>Stationary point: \(\frac{d}{dx}(AC)=0\); second-derivative test \(&gt;0\Rightarrow\) minimum.</li><li>Only \(x&gt;0\) is meaningful for an output.</li></ul>"),
        Q("15(a)", 5, r"""<p>Calculate the index number for 2010 with 2008 as the base year by the weighted aggregate method:</p>
<div class="tbl"><table><tr><th>Commodity</th><th>Price in Rs in year 2008</th><th>Price in Rs in year 2010</th><th>Weight</th></tr>
<tr><td>A</td><td>140</td><td>180</td><td>10</td></tr><tr><td>B</td><td>400</td><td>550</td><td>7</td></tr><tr><td>C</td><td>100</td><td>250</td><td>6</td></tr>
<tr><td>D</td><td>125</td><td>150</td><td>8</td></tr><tr><td>E</td><td>200</td><td>300</td><td>4</td></tr></table></div>""", excluded=STATS),
        Q("15(b)", 5, r"""<p>The following table gives the number of failures of commercial industries in a country during the years 1990 to 2005:</p>
<div class="tbl"><table><tr><th>Year</th><td>1990</td><td>1991</td><td>1992</td><td>1993</td><td>1994</td><td>1995</td><td>1996</td><td>1997</td><td>1998</td><td>1999</td><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td></tr>
<tr><th>No. of failures</th><td>23</td><td>26</td><td>28</td><td>32</td><td>20</td><td>12</td><td>12</td><td>10</td><td>9</td><td>13</td><td>11</td><td>14</td><td>12</td><td>9</td><td>3</td><td>1</td></tr></table></div>
<p>Calculate 4-yearly moving averages and display these and the original figures on the same graph. [Use graph paper for these question].</p>""", excluded=STATS),
    ])
