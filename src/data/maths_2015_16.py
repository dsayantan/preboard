"""Heritage School Pre-Board 2015-16, Mathematics (Class XII). Transcribed from the page images."""
from kit import Q, SEC
import maths_2015_16_figs as F

CONICS = "Conic sections (ellipse/hyperbola) — Class XI Coordinate Geometry in ISC 2027; not in the Class XII syllabus"
REGR = "Correlation and regression — linear regression has been dropped; the ISC 2027 Class XII paper has no statistics unit"
COMPLEX = "Complex numbers (cube roots of unity, De Moivre's theorem) — Class XI Algebra in ISC 2027; not in the Class XII syllabus"
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
    year="2015-16",
    slug="2015-16",
    paper="Mathematics",
    source="PreBoard-PYQ/2015-16/Math.pdf",
    marks=100, time="3 hours",
    intro=r"""<p><b>Answer to this paper must be written on the paper provided separately.</b><br>
You will not be allowed to write during the first 15 minutes. The time given at the head of this paper is the time allowed for writing the answers.</p>
<p><u>Answer <em>Question 1</em> and any <em>five</em> from <em>SECTION A</em> and any <em>two</em> from <em>SECTION B</em> or from <em>SECTION C</em>.</u></p>
<p>All working including <b>rough work</b>, must be clearly shown on the same sheet as the rest of the answer. Omission of essential working will result in loss of marks.</p>
<p><em>Mathematical tables are provided.</em></p>""",
    items=[
        SEC("Section A", "Question 1: 10 × 3 = 30"),
        # ------------------------------------------------------------- Q1
        Q("1(i)", 3, r"<p>Show that \(A=\begin{bmatrix}2&-3\\3&4\end{bmatrix}\) satisfies the equation \(x^2-6x+17I=0\). Hence find \(A^{-1}\).</p>",
          a=r"""<p>\[A^2=\begin{bmatrix}2&-3\\3&4\end{bmatrix}\begin{bmatrix}2&-3\\3&4\end{bmatrix}=\begin{bmatrix}4-9&-6-12\\6+12&-9+16\end{bmatrix}=\begin{bmatrix}-5&-18\\18&7\end{bmatrix}.\]</p>
<p>\[A^2-6A+17I=\begin{bmatrix}-5&-18\\18&7\end{bmatrix}-\begin{bmatrix}12&-18\\18&24\end{bmatrix}+\begin{bmatrix}17&0\\0&17\end{bmatrix}=\begin{bmatrix}0&0\\0&0\end{bmatrix}.\]</p>
<p>So \(A\) satisfies \(x^2-6x+17I=0\). Since \(|A|=8+9=17\ne0\), \(A^{-1}\) exists. Multiply \(A^2-6A+17I=O\) by \(A^{-1}\):</p>
<p>\[A-6I+17A^{-1}=O\ \Rightarrow\ A^{-1}=\frac{1}{17}(6I-A)=\frac1{17}\begin{bmatrix}6-2&3\\-3&6-4\end{bmatrix}.\]</p>
<p><span class="box">\(A^{-1}=\dfrac{1}{17}\begin{bmatrix}4&3\\-3&2\end{bmatrix}\)</span></p>""",
          topic="Matrices",
          recall=r"<ul><li>A matrix 'satisfies' a polynomial when substituting \(A\) (with \(I\) for the constant) gives \(O\).</li><li>Multiplying the equation by \(A^{-1}\) gives the inverse without cofactors.</li><li>For 2×2: \(A^{-1}=\frac1{|A|}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}\) — a check.</li></ul>"),
        Q("1(ii)", 3, r"<p>Find the equations of tangents to the hyperbola \(3x^2-y^2=3\) which are perpendicular to the line \(3y+x=2\).</p>", excluded=CONICS),
        Q("1(iii)", 3, r"<p>Solve for x: \(\sin(2\tan^{-1}x)=1\).</p>",
          a=r"""<p>Let \(\tan^{-1}x=\theta\), so \(x=\tan\theta\), \(-\frac{\pi}{2}&lt;\theta&lt;\frac{\pi}{2}\).</p>
<p>\[\sin2\theta=\frac{2\tan\theta}{1+\tan^2\theta}=\frac{2x}{1+x^2}.\]</p>
<p>\[\frac{2x}{1+x^2}=1\ \Rightarrow\ x^2-2x+1=0\ \Rightarrow\ (x-1)^2=0\ \Rightarrow\ x=1.\]</p>
<p>Check: \(\sin(2\tan^{-1}1)=\sin\frac{\pi}{2}=1\). ✓</p>
<p><span class="box">\(x=1\)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"<ul><li>\(\sin(2\tan^{-1}x)=\dfrac{2x}{1+x^2}\) (i.e. \(2\tan^{-1}x=\sin^{-1}\frac{2x}{1+x^2}\) for \(|x|\le1\)).</li><li>Principal range of \(\tan^{-1}\): \((-\frac\pi2,\frac\pi2)\).</li></ul>"),
        Q("1(iv)", 3, r"<p>Evaluate: \(\displaystyle\lim_{x\to\frac{\pi}{4}}(1-\tan x)\sec2x\).</p>",
          excluded="Evaluation of limits — Class XI Calculus in ISC 2027; the Class XII syllabus uses limits only inside continuity, not as a stand-alone question"),
        Q("1(v)", 3, r"<p>\(\displaystyle\int\frac{(x+1)e^x}{\cot^2(xe^x)}\,dx\).</p>",
          a=r"""<p>Put \(xe^x=t\); then \(\dfrac{dt}{dx}=e^x+xe^x=(x+1)e^x\), so \((x+1)e^x\,dx=dt\).</p>
<p>\[I=\int\frac{dt}{\cot^2t}=\int\tan^2t\,dt=\int(\sec^2t-1)\,dt=\tan t-t+C.\]</p>
<p><span class="box">\(I=\tan(xe^x)-xe^x+C\)</span></p>""",
          topic="Integrals (substitution)",
          recall=r"<ul><li>\(\frac{d}{dx}(xe^x)=(x+1)e^x\) — the numerator is the derivative of the inner function.</li><li>\(\tan^2t=\sec^2t-1\).</li></ul>"),
        Q("1(vi)", 3, r"<p>Simplify the boolean expression: \(a+a'(a+b)+bc\) and draw the simplified circuit.</p>", excluded=BOOL),
        Q("1(vii)", 3, r"<p>If \(1,\omega,\omega^2\) are the cube roots of unity, simplify \((1-\omega+\omega^2)^7+(1+\omega-\omega^2)^7\).</p>", excluded=COMPLEX),
        Q("1(viii)", 3, r"""<p>Find correlation coefficients (r) from the data given:</p>
<p>\(\sum x=30,\ \sum y=42,\ \sum xy=199,\ \sum x^2=184,\ \sum y^2=318\) and \(n=6\). Find \(b_{xy}\) and \(b_{yx}\).</p>""", excluded=REGR),
        Q("1(ix)", 3, r"<p>The probability of an event A occurring is \(\dfrac23\) and the probability of an event B occurring is \(\dfrac49\). If the probability of getting success in atleast one of the two events is \(\dfrac45\), what is the probability of success in both the events?</p>",
          a=r"""<p>Given \(P(A)=\frac23,\ P(B)=\frac49,\ P(A\cup B)=\frac45\). By the addition theorem,</p>
<p>\[P(A\cap B)=P(A)+P(B)-P(A\cup B)=\frac23+\frac49-\frac45=\frac{30+20-36}{45}.\]</p>
<p><span class="box">\(P(A\cap B)=\dfrac{14}{45}\)</span></p>
<p>(Note \(P(A)P(B)=\frac{8}{27}\ne\frac{14}{45}\), so A and B are <em>not</em> independent — the product rule must not be used here.)</p>""",
          topic="Probability",
          recall=r"<ul><li>'At least one' = \(A\cup B\); 'both' = \(A\cap B\).</li><li>\(P(A\cup B)=P(A)+P(B)-P(A\cap B)\).</li><li>\(P(A\cap B)=P(A)P(B)\) only for independent events.</li></ul>"),
        Q("1(x)", 3, r"<p>Solve the differential equation: \(y-x\dfrac{dy}{dx}=a\left(y^2+\dfrac{dy}{dx}\right)\).</p>",
          a=r"""<p>Collect the \(\frac{dy}{dx}\) terms: \(y-ay^2=(x+a)\dfrac{dy}{dx}\), so the variables separate:</p>
<p>\[\frac{dy}{y(1-ay)}=\frac{dx}{x+a}.\]</p>
<p>Partial fractions: \(\dfrac{1}{y(1-ay)}=\dfrac1y+\dfrac{a}{1-ay}\). Integrating,</p>
<p>\[\log|y|-\log|1-ay|=\log|x+a|+\log|C|\ \Rightarrow\ \frac{y}{1-ay}=C(x+a).\]</p>
<p><span class="box">\(y=C(x+a)(1-ay)\)</span> &nbsp;(C an arbitrary constant)</p>""",
          topic="Differential Equations (variable separable)",
          recall=r"<ul><li>Bring every \(\frac{dy}{dx}\) term to one side; if what remains factorises as \(f(x)g(y)\), separate.</li><li>\(\int\frac{a\,dy}{1-ay}=-\log|1-ay|\).</li><li>Write the constant as \(\log|C|\) to combine logs.</li></ul>"),
        # ------------------------------------------------------------- Q2
        Q("2(a)", 5, r"""<p>Using properties of determinants, show that</p>
<p>\[\begin{vmatrix}(b+c)^2&a^2&a^2\\b^2&(c+a)^2&b^2\\c^2&c^2&(a+b)^2\end{vmatrix}=2abc(a+b+c)^3\]</p>""",
          a=r"""<p>Let \(\Delta\) be the determinant. Apply \(C_2\to C_2-C_1,\ C_3\to C_3-C_1\) and use \(p^2-q^2=(p-q)(p+q)\):</p>
<p>\[\Delta=\begin{vmatrix}(b+c)^2&(a-b-c)(a+b+c)&(a-b-c)(a+b+c)\\b^2&(c+a-b)(a+b+c)&0\\c^2&0&(a+b-c)(a+b+c)\end{vmatrix}\]</p>
<p>Take \((a+b+c)\) common from \(C_2\) and from \(C_3\):</p>
<p>\[\Delta=(a+b+c)^2\begin{vmatrix}(b+c)^2&a-b-c&a-b-c\\b^2&c+a-b&0\\c^2&0&a+b-c\end{vmatrix}\]</p>
<p>Apply \(R_1\to R_1-R_2-R_3\): the entries become \((b+c)^2-b^2-c^2=2bc\), \((a-b-c)-(c+a-b)=-2c\), \((a-b-c)-(a+b-c)=-2b\):</p>
<p>\[\Delta=(a+b+c)^2\begin{vmatrix}2bc&-2c&-2b\\b^2&c+a-b&0\\c^2&0&a+b-c\end{vmatrix}\]</p>
<p>Multiply \(C_2\) by \(b\) and \(C_3\) by \(c\), dividing outside by \(bc\) (for \(b,c\ne0\)):</p>
<p>\[\Delta=\frac{(a+b+c)^2}{bc}\begin{vmatrix}2bc&-2bc&-2bc\\b^2&b(c+a-b)&0\\c^2&0&c(a+b-c)\end{vmatrix}\]</p>
<p>Apply \(C_2\to C_2+C_1,\ C_3\to C_3+C_1\):</p>
<p>\[\Delta=\frac{(a+b+c)^2}{bc}\begin{vmatrix}2bc&0&0\\b^2&b(c+a)&b^2\\c^2&c^2&c(a+b)\end{vmatrix}\]</p>
<p>Expand along \(R_1\):</p>
<p>\[\begin{aligned}\Delta&=\frac{(a+b+c)^2}{bc}\cdot2bc\big[bc(c+a)(a+b)-b^2c^2\big]\\&=2bc\,(a+b+c)^2\big[(c+a)(a+b)-bc\big]\\&=2bc\,(a+b+c)^2(a^2+ab+ac)=2abc\,(a+b+c)^3.\end{aligned}\]</p>
<p><span class="box">\(\Delta=2abc(a+b+c)^3\)</span> &nbsp;Hence proved.</p>
<p>(Both sides are polynomials in \(a,b,c\), so the identity proved for \(b,c\ne0\) holds for all values.)</p>""",
          topic="Determinants",
          recall=r"<ul><li>Subtracting columns turns \(p^2-q^2\) entries into factors \((p-q)(p+q)\) that can be taken out.</li><li>\(R_1\to R_1-R_2-R_3\) and \(C_j\to C_j+C_1\) do not change the value; multiplying a column by \(k\) multiplies \(\Delta\) by \(k\).</li><li>Aim for a row with two zeros, then expand.</li></ul>"),
        Q("2(b)", 5, r"""<p>Compute \(A^{-1}\) for the matrix \(A=\begin{bmatrix}0&1&2\\1&2&3\\3&1&1\end{bmatrix}\). Hence solve the system of equations</p>
<p>\(y+2z+8=0,\ x+2y+3z+14=0,\ 3x+y+z+8=0\).</p>""",
          a=r"""<p>\(|A|=0(2-3)-1(1-9)+2(1-6)=0+8-10=-2\ne0\).</p>
<p>Cofactors: \(A_{11}=-1,\ A_{12}=8,\ A_{13}=-5;\ A_{21}=1,\ A_{22}=-6,\ A_{23}=3;\ A_{31}=-1,\ A_{32}=2,\ A_{33}=-1.\)</p>
<p>\[\operatorname{adj}A=\begin{bmatrix}-1&1&-1\\8&-6&2\\-5&3&-1\end{bmatrix},\qquad A^{-1}=-\frac12\begin{bmatrix}-1&1&-1\\8&-6&2\\-5&3&-1\end{bmatrix}=\begin{bmatrix}\tfrac12&-\tfrac12&\tfrac12\\-4&3&-1\\\tfrac52&-\tfrac32&\tfrac12\end{bmatrix}.\]</p>
<p>The equations are \(y+2z=-8,\ x+2y+3z=-14,\ 3x+y+z=-8\), i.e. \(AX=B\) with \(B=\begin{bmatrix}-8\\-14\\-8\end{bmatrix}\). Then \(X=A^{-1}B\):</p>
<p>\[X=-\frac12\begin{bmatrix}8-14+8\\-64+84-16\\40-42+8\end{bmatrix}=-\frac12\begin{bmatrix}2\\4\\6\end{bmatrix}=\begin{bmatrix}-1\\-2\\-3\end{bmatrix}.\]</p>
<p><span class="box">\(x=-1,\ y=-2,\ z=-3\)</span></p>
<p>Check: \(-2-6+8=0\) ✓; \(-1-4-9+14=0\) ✓; \(-3-2-3+8=0\) ✓.</p>""",
          topic="Matrices and Determinants",
          recall=r"<ul><li>Move the constants to the right before writing \(AX=B\) (here \(B\) is negative).</li><li>\(A^{-1}=\frac{\operatorname{adj}A}{|A|}\); \(X=A^{-1}B\).</li><li>Substitute back into the original equations.</li></ul>"),
        # ------------------------------------------------------------- Q3
        Q("3(a)", 5, r"<p>Prove that \(\sin^{-1}\dfrac45+\cos^{-1}\dfrac{2}{\sqrt5}=\cot^{-1}\dfrac{2}{11}\).</p>",
          a=r"""<p>Let \(\alpha=\sin^{-1}\frac45\): \(\sin\alpha=\frac45,\ \cos\alpha=\frac35\), so \(\alpha=\tan^{-1}\frac43\).</p>
<p>Let \(\beta=\cos^{-1}\frac2{\sqrt5}\): \(\cos\beta=\frac2{\sqrt5},\ \sin\beta=\frac1{\sqrt5}\), so \(\beta=\tan^{-1}\frac12\).</p>
<p>Since \(\frac43\cdot\frac12=\frac23&lt;1\),</p>
<p>\[\alpha+\beta=\tan^{-1}\frac{\frac43+\frac12}{1-\frac43\cdot\frac12}=\tan^{-1}\frac{11/6}{1/3}=\tan^{-1}\frac{11}{2}.\]</p>
<p>As \(\frac{11}{2}&gt;0\), \(\tan^{-1}\frac{11}{2}=\cot^{-1}\frac{2}{11}\).</p>
<p><span class="box">\(\sin^{-1}\frac45+\cos^{-1}\frac{2}{\sqrt5}=\cot^{-1}\frac{2}{11}\)</span> &nbsp;Hence proved.</p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"<ul><li>Convert every term to \(\tan^{-1}\) using a right triangle.</li><li>\(\tan^{-1}a+\tan^{-1}b=\tan^{-1}\frac{a+b}{1-ab}\) for \(ab&lt;1\).</li><li>\(\tan^{-1}x=\cot^{-1}\frac1x\) for \(x&gt;0\).</li></ul>"),
        Q("3(b)", 5, r"<p>A, B, C represent switches in an 'on position' and \(A',B',C'\) represent switches in an 'off position'. Construct a switching circuit representing the polynomial \(A(A+B)B(B+C')\). Use Boolean Algebra to show that the above circuit is equivalent to a switching circuit in which when A and B are on, the light is on. Construct the equivalent circuit.</p>", excluded=BOOL),
        # ------------------------------------------------------------- Q4
        Q("4(a)", 5, r"<p>Verify the Rolle's theorem for the function \(f(x)=\log\left\{\dfrac{x^2+ab}{x(a+b)}\right\}\) on \([a,b]\), where \(0&lt;a&lt;b\).</p>", excluded=MVT),
        Q("4(b)", 5, r"<p>Find the equation of the ellipse whose foci are \((2,3)\) and \((-2,3)\) and whose semi-minor axis is \(\sqrt5\).</p>", excluded=CONICS),
        # ------------------------------------------------------------- Q5
        Q("5(a)", 5, r"<p>If \(y=(\cos^{-1}x)^2\), prove that \((1-x^2)\dfrac{d^2y}{dx^2}-x\dfrac{dy}{dx}=2\). Hence find the value of \(\dfrac{d^2y}{dx^2}\) at \(x=0\).</p><p class='note'>[No mark is printed against 5(a); it is taken as 5, like every other Section A part.]</p>",
          a=r"""<p>\[y_1=\frac{dy}{dx}=2\cos^{-1}x\cdot\left(-\frac{1}{\sqrt{1-x^2}}\right)\ \Rightarrow\ \sqrt{1-x^2}\,y_1=-2\cos^{-1}x.\]</p>
<p>Squaring: \((1-x^2)y_1^2=4(\cos^{-1}x)^2=4y\).</p>
<p>Differentiate with respect to \(x\):</p>
<p>\[(1-x^2)\,2y_1y_2-2x\,y_1^2=4y_1.\]</p>
<p>Divide by \(2y_1\) (\(y_1\ne0\)):</p>
<p><span class="box">\((1-x^2)\dfrac{d^2y}{dx^2}-x\dfrac{dy}{dx}=2\)</span> &nbsp;Hence proved.</p>
<p><b>At \(x=0\):</b> \((1-0)y_2-0\cdot y_1=2\), so <span class="box">\(\left.\dfrac{d^2y}{dx^2}\right|_{x=0}=2\)</span></p>""",
          topic="Differentiation (second order)",
          recall=r"<ul><li>\(\frac{d}{dx}\cos^{-1}x=-\frac{1}{\sqrt{1-x^2}}\).</li><li>Clear the root by squaring before the second differentiation.</li><li>At \(x=0\) the \(x\,y_1\) term vanishes, so \(y_1(0)\) is not needed.</li></ul>"),
        Q("5(b)", 5, r"<p>An open box with a square base is to be made out of a given quantity of sheet of area \(a^2\). Show that the maximum volume of the box is \(a^3\).</p>",
          a=r"""<p class="note">[The paper's stated answer is a misprint: the maximum volume works out to \(\dfrac{a^3}{6\sqrt3}\), the standard result for this problem. It cannot be \(a^3\): a box made from sheet of area \(a^2\) has every edge shorter than \(a\), so its volume is less than \(a^3\).]</p>
{{fig:0}}
<p>Let the side of the square base be \(x\) and the height \(h\). The box is open, so the sheet used is base + four sides:</p>
<p>\[x^2+4xh=a^2\ \Rightarrow\ h=\frac{a^2-x^2}{4x}.\]</p>
<p>\[V=x^2h=\frac{x(a^2-x^2)}{4}=\frac{a^2x-x^3}{4},\qquad 0&lt;x&lt;a.\]</p>
<p>\[\frac{dV}{dx}=\frac{a^2-3x^2}{4}=0\ \Rightarrow\ x=\frac{a}{\sqrt3}.\qquad \frac{d^2V}{dx^2}=-\frac{3x}{2}&lt;0,\]</p>
<p>so V is maximum at \(x=\frac{a}{\sqrt3}\), where \(h=\dfrac{a^2-a^2/3}{4a/\sqrt3}=\dfrac{a}{2\sqrt3}=\dfrac x2\).</p>
<p>\[V_{\max}=x^2h=\frac{a^2}{3}\cdot\frac{a}{2\sqrt3}=\frac{a^3}{6\sqrt3}.\]</p>
<p><span class="box">Maximum volume \(=\dfrac{a^3}{6\sqrt3}\) (when the height is half the side of the base)</span></p>""",
          topic="Applications of Derivatives (maxima and minima)",
          afig=[(F.fig_open_box, "Open box: square base of side x, height h, no lid.")],
          recall=r"<ul><li>Use the fixed quantity (area of sheet) to eliminate one variable.</li><li>Open box: surface \(=x^2+4xh\) (no lid).</li><li>Second-derivative test for the maximum; state the dimensions too.</li></ul>"),
        # ------------------------------------------------------------- Q6
        Q("6(a)", 5, r"<p>Evaluate the integral: \(\displaystyle\int_0^{\pi}\frac{x\tan x}{\sec x+\tan x}\,dx\).</p>",
          a=r"""<p>Let \(I=\displaystyle\int_0^{\pi}\frac{x\tan x}{\sec x+\tan x}dx\). Using \(\int_0^af(x)dx=\int_0^af(a-x)dx\) with \(\tan(\pi-x)=-\tan x,\ \sec(\pi-x)=-\sec x\):</p>
<p>\[I=\int_0^{\pi}\frac{(\pi-x)(-\tan x)}{-\sec x-\tan x}dx=\int_0^{\pi}\frac{(\pi-x)\tan x}{\sec x+\tan x}dx.\]</p>
<p>Adding the two forms of \(I\):</p>
<p>\[2I=\pi\int_0^{\pi}\frac{\tan x}{\sec x+\tan x}dx=\pi\int_0^{\pi}\frac{\sin x}{1+\sin x}dx=\pi\int_0^{\pi}\left(1-\frac{1}{1+\sin x}\right)dx.\]</p>
<p>Now \(\displaystyle\int_0^{\pi}\frac{dx}{1+\sin x}=2\int_0^{\pi/2}\frac{dx}{1+\sin x}\) (since \(\sin(\pi-x)=\sin x\)), and</p>
<p>\[\int_0^{\pi/2}\frac{dx}{1+\sin x}=\int_0^{\pi/2}\frac{dx}{1+\cos x}=\int_0^{\pi/2}\tfrac12\sec^2\tfrac x2\,dx=\Big[\tan\tfrac x2\Big]_0^{\pi/2}=1.\]</p>
<p>(using \(\int_0^{a}f(x)dx=\int_0^af(a-x)dx\) with \(a=\frac\pi2\)). So \(\int_0^{\pi}\frac{dx}{1+\sin x}=2\) and</p>
<p>\[2I=\pi(\pi-2)\ \Rightarrow\ I=\frac{\pi(\pi-2)}{2}.\]</p>
<p><span class="box">\(I=\dfrac{\pi(\pi-2)}{2}=\dfrac{\pi^2}{2}-\pi\)</span></p>""",
          topic="Definite Integrals (properties)",
          recall=r"<ul><li>\(\int_0^af(x)dx=\int_0^af(a-x)dx\) — removes the factor \(x\) when \(f(a-x)=f(x)\).</li><li>\(\int_0^{2a}f(x)dx=2\int_0^af(x)dx\) if \(f(2a-x)=f(x)\).</li><li>\(1+\cos x=2\cos^2\frac x2\).</li></ul>"),
        Q("6(b)", 5, r"<p>Find the area bounded by the curve \(x=8+2y-y^2\), the y-axis and the lines \(y=-1,\ y=3\).</p>",
          a=r"""<p>\(x=8+2y-y^2=9-(y-1)^2\) is a parabola opening to the left with vertex \((9,1)\). It meets \(y=-1\) and \(y=3\) at \(x=5\), so \(x&gt;0\) for \(-1\le y\le3\): the region lies to the right of the y-axis.</p>
{{fig:0}}
<p>\[\text{Area}=\int_{-1}^{3}x\,dy=\int_{-1}^{3}(8+2y-y^2)\,dy=\Big[8y+y^2-\frac{y^3}{3}\Big]_{-1}^{3}\]</p>
<p>\[=(24+9-9)-\left(-8+1+\frac13\right)=24+\frac{20}{3}=\frac{92}{3}.\]</p>
<p><span class="box">Area \(=\dfrac{92}{3}\) square units \((\approx30.67)\)</span></p>""",
          topic="Application of Integrals (area)",
          afig=[(F.fig_area_sideways_parabola, "Region between x = 8 + 2y − y², the y-axis, y = −1 and y = 3.")],
          recall=r"<ul><li>Area between a curve \(x=g(y)\), the y-axis and \(y=c,\ y=d\): \(\int_c^d|g(y)|\,dy\).</li><li>Complete the square to find the vertex and check the sign of \(x\) on the interval.</li></ul>"),
        # ------------------------------------------------------------- Q7
        Q("7(a)", 5, r"""<p>Find the rank correlation coefficient of the following data and interpret the result.</p>
<div class="tbl"><table><tr><th>A</th><td>115</td><td>109</td><td>112</td><td>87</td><td>98</td><td>120</td><td>98</td><td>100</td><td>98</td><td>118</td></tr>
<tr><th>B</th><td>75</td><td>73</td><td>85</td><td>70</td><td>76</td><td>82</td><td>65</td><td>73</td><td>68</td><td>80</td></tr></table></div>""", excluded=REGR),
        Q("7(b)", 5, r"""<p>In a bivariate distribution the following data are given:</p>
<p>\(\bar X=36,\ \bar Y=85,\ \sigma_x=11,\ \sigma_y=8\). Correlation coefficient of X and Y is 0.66. Find</p>
<p>i) the two regression coefficients<br>ii) the two regression equations<br>iii) the most likely value of \(y\) when \(x=10\).</p>""", excluded=REGR),
        # ------------------------------------------------------------- Q8
        Q("8(a)", 5, r"<p>Two persons throw a die, alternately till one of them gets a multiple of 3 and wins the game. Find their respective probability of winning.</p>",
          a=r"""<p>On each throw \(p=P(3\text{ or }6)=\frac26=\frac13\), \(q=\frac23\); throws are independent.</p>
<p>The first thrower wins on the 1st, 3rd, 5th, … throw:</p>
<p>\[P_1=p+q^2p+q^4p+\cdots=\frac{p}{1-q^2}=\frac{1/3}{1-4/9}=\frac{1/3}{5/9}=\frac35.\]</p>
<p>The second thrower wins on the 2nd, 4th, … throw:</p>
<p>\[P_2=qp+q^3p+\cdots=\frac{qp}{1-q^2}=\frac{2/9}{5/9}=\frac25.\]</p>
<p><span class="box">First thrower \(\tfrac35\), second thrower \(\tfrac25\)</span> &nbsp;(they add to 1: the game ends with probability 1).</p>""",
          topic="Probability (independent events)",
          recall=r"<ul><li>Multiples of 3 on a die: 3 and 6.</li><li>Alternate trials: first player \(\frac{p}{1-q^2}\), second \(\frac{qp}{1-q^2}\).</li><li>Infinite G.P. \(a+ar+\cdots=\frac{a}{1-r}\).</li></ul>"),
        Q("8(b)", 5, r"<p>A bag contains 4 white and 2 black balls. Another contains 3 white and 5 black balls. If one ball is drawn from each bag, find the probability that i) both are white ii) both are black iii) one is white and one is black.</p>",
          a=r"""<p>Bag I: \(P(W_1)=\frac46=\frac23,\ P(B_1)=\frac26=\frac13\). Bag II: \(P(W_2)=\frac38,\ P(B_2)=\frac58\). Draws from different bags are independent.</p>
<p><b>(i)</b> \(P(W_1\cap W_2)=\frac23\cdot\frac38=\frac14\).</p>
<p><b>(ii)</b> \(P(B_1\cap B_2)=\frac13\cdot\frac58=\frac{5}{24}\).</p>
<p><b>(iii)</b> \(P(W_1B_2)+P(B_1W_2)=\frac23\cdot\frac58+\frac13\cdot\frac38=\frac{10}{24}+\frac{3}{24}=\frac{13}{24}\).</p>
<p>Check: \(\frac{6}{24}+\frac{5}{24}+\frac{13}{24}=1\).</p>
<p><span class="box">(i) \(\tfrac14\) &nbsp; (ii) \(\tfrac5{24}\) &nbsp; (iii) \(\tfrac{13}{24}\)</span></p>""",
          topic="Probability (independent events)",
          recall=r"<ul><li>Independent events: \(P(A\cap B)=P(A)P(B)\).</li><li>'One white and one black' has two mutually exclusive orders — add them.</li></ul>"),
        # ------------------------------------------------------------- Q9
        Q("9(a)", 5, r"<p>Using Demoivre's theorem, find the least value of n for which the expression \(\left(\dfrac{1+\sqrt3i}{\sqrt2(1+i)}\right)^n\) is purely imaginary.</p>", excluded=COMPLEX),
        Q("9(b)", 5, r"<p>Solve the differential equation \((1-x^2)\dfrac{dy}{dx}-xy=x\), given \(y=2\) when \(x=0\).</p>",
          a=r"""<p>\((1-x^2)\dfrac{dy}{dx}=x(y+1)\), so the variables separate (for \(|x|&lt;1\), which contains \(x=0\)):</p>
<p>\[\frac{dy}{y+1}=\frac{x\,dx}{1-x^2}.\]</p>
<p>Integrate: \(\log|y+1|=-\frac12\log(1-x^2)+\log C\ \Rightarrow\ y+1=\dfrac{C}{\sqrt{1-x^2}}\).</p>
<p>At \(x=0,\ y=2\): \(3=C\).</p>
<p><span class="box">\(y=\dfrac{3}{\sqrt{1-x^2}}-1\)</span></p>
<p>(It can equally be solved as a linear equation \(\frac{dy}{dx}-\frac{x}{1-x^2}y=\frac{x}{1-x^2}\) with I.F. \(\sqrt{1-x^2}\): \(y\sqrt{1-x^2}=-\sqrt{1-x^2}+C\), the same result.)</p>""",
          topic="Differential Equations",
          recall=r"<ul><li>Factor the right side before reaching for the linear method — here it separates.</li><li>\(\int\frac{x\,dx}{1-x^2}=-\frac12\log|1-x^2|\).</li><li>Use the initial condition to fix C.</li></ul>"),
        # ------------------------------------------------------------- Section B
        SEC("Section B"),
        Q("10(a)", 5, r"<p>Prove by vector method, that in any triangle ABC \(\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}\).</p>", excluded=VGEOM),
        Q("10(b)", 5, r"<p>For any three vectors \(\vec a,\vec b,\vec c\) prove that \(\left[\vec a\times\vec b\ \ \vec b\times\vec c\ \ \vec c\times\vec a\right]=\left[\vec a\ \vec b\ \vec c\right]^2\).</p>", excluded=TRIPLE),
        Q("11(a)", 5, r"<p>The vector equation of two straight lines are \(\vec r_1=\hat i+2\hat j+\hat k+\lambda(\hat i-\hat j+\hat k)\), \(\vec r_2=2\hat i-\hat j-\hat k+\mu(2\hat i+\hat j+\hat k)\). Find the shortest distance between the two lines.</p>",
          a=r"""<p>\(\vec a_1=\hat i+2\hat j+\hat k,\ \vec b_1=\hat i-\hat j+\hat k\); \(\vec a_2=2\hat i-\hat j-\hat k,\ \vec b_2=2\hat i+\hat j+\hat k\). The directions are not parallel.</p>
<p>\[\vec b_1\times\vec b_2=\begin{vmatrix}\hat i&\hat j&\hat k\\1&-1&1\\2&1&1\end{vmatrix}=(-1-1)\hat i-(1-2)\hat j+(1+2)\hat k=-2\hat i+\hat j+3\hat k,\]</p>
<p>\(|\vec b_1\times\vec b_2|=\sqrt{4+1+9}=\sqrt{14}\); \(\vec a_2-\vec a_1=\hat i-3\hat j-2\hat k\).</p>
<p>\[d=\frac{|(\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)|}{|\vec b_1\times\vec b_2|}=\frac{|-2-3-6|}{\sqrt{14}}=\frac{11}{\sqrt{14}}.\]</p>
<p><span class="box">Shortest distance \(=\dfrac{11}{\sqrt{14}}=\dfrac{11\sqrt{14}}{14}\approx2.94\) units</span> &nbsp;(non-zero, so the lines are skew).</p>""",
          topic="Three-dimensional Geometry (shortest distance)",
          recall=r"<ul><li>Skew lines: \(d=\dfrac{|(\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)|}{|\vec b_1\times\vec b_2|}\).</li><li>\(d=0\) means the lines intersect.</li></ul>"),
        Q("11(b)", 5, r"<p>Find the equation of the plane passing through the line of intersection of the planes \(2x-y=0\) and \(3z-y=0\) and perpendicular to the plane \(4x+5y-3z=0\).</p>",
          a=r"""<p>Normals: \(\vec n_1=2\hat i-\hat j\) and \(\vec n_2=-\hat j+3\hat k\). The line of intersection is perpendicular to both, so its direction is</p>
<p>\[\vec n_1\times\vec n_2=\begin{vmatrix}\hat i&\hat j&\hat k\\2&-1&0\\0&-1&3\end{vmatrix}=-3\hat i-6\hat j-2\hat k\ \parallel\ 3\hat i+6\hat j+2\hat k.\]</p>
<p>Both planes pass through the origin, so the line passes through O.</p>
<p>The required plane contains this line, and is perpendicular to \(4x+5y-3z=0\), so it contains the direction \(4\hat i+5\hat j-3\hat k\). Its normal is</p>
<p>\[\vec n=(3\hat i+6\hat j+2\hat k)\times(4\hat i+5\hat j-3\hat k)=\begin{vmatrix}\hat i&\hat j&\hat k\\3&6&2\\4&5&-3\end{vmatrix}=-28\hat i+17\hat j-9\hat k.\]</p>
<p>Through O with normal \(28\hat i-17\hat j+9\hat k\):</p>
<p><span class="box">\(28x-17y+9z=0\)</span> &nbsp;(vector form \(\vec r\cdot(28\hat i-17\hat j+9\hat k)=0\))</p>
<p>Check: \(28(4)-17(5)+9(-3)=112-85-27=0\) ✓ (perpendicular); a point of the line, \((3,6,2)\): \(84-102+18=0\) ✓.</p>
<p>(Equivalently, \(2x-y+\lambda(3z-y)=0\) with \(8-5(1+\lambda)-9\lambda=0\) gives \(\lambda=\frac{3}{14}\) and the same plane.)</p>""",
          topic="Three-dimensional Geometry (planes)",
          recall=r"<ul><li>Line of intersection of two planes has direction \(\vec n_1\times\vec n_2\).</li><li>Plane ⟂ to a given plane contains that plane's normal.</li><li>Normal = cross product of two directions lying in the plane.</li></ul>"),
        Q("12(a)", 5, r"""<p>In an examination, 30% of the students have failed in Mathematics, 20% have failed in Chemistry and 10% have failed in both the subjects. A student is selected at random.</p>
<p>i) What is the probability that the student has failed in Mathematics if it is known that he has failed in Chemistry?<br>ii) What is the probability that the student has failed either in Mathematics or in Chemistry?</p>""",
          a=r"""<p>Let M: failed in Mathematics, C: failed in Chemistry. \(P(M)=0.3,\ P(C)=0.2,\ P(M\cap C)=0.1\).</p>
<p><b>(i)</b> \[P(M\mid C)=\frac{P(M\cap C)}{P(C)}=\frac{0.1}{0.2}=\frac12.\]</p>
<p><b>(ii)</b> \[P(M\cup C)=P(M)+P(C)-P(M\cap C)=0.3+0.2-0.1=0.4.\]</p>
<p><span class="box">(i) \(\tfrac12\) &nbsp; (ii) \(0.4\)</span></p>
<p>(If 'either … or' is read as <em>exactly one</em> of the two, the probability is \(P(M\cup C)-P(M\cap C)=0.3\).)</p>""",
          topic="Probability (conditional probability)",
          recall=r"<ul><li>\(P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}\).</li><li>Addition theorem: \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\).</li></ul>"),
        Q("12(b)", 5, r"<p>Three urns are given. Urn 1 contains 6 red and 4 black balls, Urn 2 contains 2 red and 6 black balls and Urn 3 contains 1 red and 8 black balls. An urn is chosen at random and a ball is drawn. The ball drawn is black. Find the probability that the ball is drawn either from Urn 2 or from Urn 3.</p>",
          a=r"""<p>Let \(E_i\): urn \(i\) is chosen, \(P(E_i)=\frac13\); B: the ball is black.</p>
{{fig:0}}
<p>\(P(B|E_1)=\frac4{10},\ P(B|E_2)=\frac68,\ P(B|E_3)=\frac89\).</p>
<p>\[P(B)=\frac13\left(\frac25+\frac34+\frac89\right)=\frac13\cdot\frac{72+135+160}{180}=\frac{367}{540}.\]</p>
<p>By Bayes' theorem, since \(E_2,E_3\) are mutually exclusive,</p>
<p>\[P(E_2\cup E_3\mid B)=\frac{\frac13\cdot\frac34+\frac13\cdot\frac89}{\frac13\left(\frac25+\frac34+\frac89\right)}=\frac{135+160}{72+135+160}=\frac{295}{367}.\]</p>
<p><span class="box">\(P(\text{Urn 2 or Urn 3}\mid\text{black})=\dfrac{295}{367}\approx0.804\)</span></p>
<p>(Equivalently \(1-P(E_1|B)=1-\frac{72}{367}\).)</p>""",
          topic="Probability (Bayes' theorem)",
          afig=[(F.fig_tree_urns, "Urn chosen first (1/3 each), then the colour drawn.")],
          recall=r"<ul><li>Bayes: \(P(E_i|B)=\dfrac{P(E_i)P(B|E_i)}{\sum P(E_j)P(B|E_j)}\).</li><li>For 'urn 2 or urn 3', add the two posterior probabilities (or take 1 − P(urn 1 | B)).</li><li>Use a common denominator (180) to keep the fractions exact.</li></ul>"),
        # ------------------------------------------------------------- Section C
        SEC("Section C"),
        Q("13(a)", 5, r"<p>The banker's discount and the true discount on a bill due 4 months hence are Rs 210 and Rs 200 respectively. Find the rate percent and the amount of the bill.</p>", excluded=COMM),
        Q("13(b)", 5, r"""<p>The average cost function for a commodity is given by \(AC=x+5+\dfrac{36}{x}\) in terms of output \(x\).</p>
<p>Find: (i) the total cost function and marginal cost function.<br>(ii) the outputs for which AC increases.</p>""",
          a=r"""<p><b>(i)</b> Total cost \(=\) output \(\times\) average cost:</p>
<p>\[C(x)=x\cdot AC=x\left(x+5+\frac{36}{x}\right)=x^2+5x+36.\]</p>
<p>Marginal cost is the rate of change of total cost with output:</p>
<p>\[MC=\frac{dC}{dx}=2x+5.\]</p>
<p><span class="box">\(C(x)=x^2+5x+36,\quad MC=2x+5\)</span></p>
<p><b>(ii)</b> \[\frac{d(AC)}{dx}=1-\frac{36}{x^2}=\frac{x^2-36}{x^2}=\frac{(x-6)(x+6)}{x^2}.\]</p>
<p>For \(x&gt;0\) (output) the sign is that of \(x-6\): \(\frac{d(AC)}{dx}&gt;0\) for \(x&gt;6\) and \(&lt;0\) for \(0&lt;x&lt;6\).</p>
<p><span class="box">AC increases for \(x&gt;6\)</span> &nbsp;(it decreases for \(0&lt;x&lt;6\); its minimum is \(AC(6)=17\)).</p>""",
          topic="Applications of Derivatives (rate measure; increasing and decreasing functions)",
          recall=r"<ul><li>\(C(x)=x\cdot AC(x)\); marginal cost \(MC=\dfrac{dC}{dx}\) (rate of change of cost).</li><li>\(f\) is increasing where \(f'(x)&gt;0\), decreasing where \(f'(x)&lt;0\).</li><li>Output \(x\) is positive, so \(x=-6\) is discarded.</li></ul>"),
        Q("14(a)", 5, r"""<p>Obtain the five year moving average for the following series of observations. Draw the graph.</p>
<div class="tbl"><table><tr><th>Year</th><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td></tr>
<tr><th>Annual sales (in Rs 10000)</th><td>3.6</td><td>4.3</td><td>4.3</td><td>3.4</td><td>4.4</td><td>5.4</td><td>3.4</td><td>2.4</td></tr></table></div>""", excluded=STATS),
        Q("14(b)", 5, r"""<p>The prices for four different commodities for the years 2005 and 2010 are given below. Calculate the index number for 2010 and 2005 as the base year by using the weighted average of price relatives method.</p>
<div class="tbl"><table><tr><th>Commodity</th><th>Weight</th><th>Price in Rs in the year 2005</th><th>Price in Rs in the year 2010</th></tr>
<tr><td>A</td><td>5</td><td>2.00</td><td>4.50</td></tr><tr><td>B</td><td>7</td><td>2.50</td><td>3.20</td></tr>
<tr><td>C</td><td>6</td><td>3.00</td><td>4.50</td></tr><tr><td>D</td><td>2</td><td>1.00</td><td>1.80</td></tr></table></div>""", excluded=STATS),
        Q("15(a)", 5, r"<p>What equal payments made at the beginning of each year for 10 years will pay for a piece of land priced at Rs 400000, if money is worth 7% per annum compounded annually?</p>", excluded=COMM),
        Q("15(b)", 5, r"<p>A manufacturer produces nuts and bolts for industrial machinery. It takes 1 hour of work on machine A and 3 hours on machine B to produce a package of nuts while it takes 3 hours on machine A and 1 hour on machine B to produce a package of bolts. He earns a profit of Rs 2.50 per package of nuts and Re 1.00 per package of bolts. How many packages of each should he produce each day so as to maximize his profit, if he operates his machines for at most 12 hours a day? Formulate this mathematically and then solve it.</p>",
          a=r"""<p><b>Formulation.</b> Let \(x\) packages of nuts and \(y\) packages of bolts be made per day.</p>
<p>Maximise \(Z=2.5x+y\) subject to</p>
<p>\[x+3y\le12\ \text{(machine A)},\qquad 3x+y\le12\ \text{(machine B)},\qquad x\ge0,\ y\ge0.\]</p>
<p><b>Graph.</b> \(x+3y=12\) meets the axes at \((12,0),(0,4)\); \(3x+y=12\) at \((4,0),(0,12)\). O satisfies both, so the feasible region is on the origin side of each line. Solving the two equations: \(x=3,\ y=3\).</p>
{{fig:0}}
<p>The feasible region is the bounded quadrilateral OABC.</p>
<div class="tbl"><table><tr><th>Corner</th><th>\(Z=2.5x+y\)</th></tr><tr><td>O(0, 0)</td><td>0</td></tr><tr><td>A(4, 0)</td><td>10</td></tr><tr><td>B(3, 3)</td><td><b>10.5</b></td></tr><tr><td>C(0, 4)</td><td>4</td></tr></table></div>
<p><span class="box">3 packages of nuts and 3 packages of bolts a day; maximum profit Rs 10.50</span></p>""",
          topic="Linear Programming",
          afig=[(F.fig_lpp_nuts_bolts, "Feasible region OABC (shaded); the dashed profit line touches it at B.")],
          recall=r"<ul><li>'At most 12 hours' gives \(\le\) constraints, one per machine.</li><li>Bounded region: the optimum is at a corner — tabulate Z at every corner.</li><li>Corner B from solving the two boundary equations simultaneously.</li></ul>"),
    ])
