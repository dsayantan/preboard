"""Heritage School Pre-Board 2016-17, Mathematics (Class XII).  Transcribed from the page images."""
from kit import Q, SEC
import maths_2016_17_figs as F

CONICS = "Conic sections (parabola/hyperbola) — Class XI topic in ISC 2027; not in the Class XII units."
COMPLEX = "Complex numbers — Class XI topic in ISC 2027; not in the Class XII units."
REGR = "Correlation and regression — dropped from ISC Mathematics; not in the ISC 2027 Class XII units."
COMMERCE = "Financial mathematics ({}) — not in the ISC 2027 Class XII syllabus; of the old Section C only Linear Programming (and calculus applications) remain."

PAPER = dict(
    subject="maths",
    year="2016-17",
    slug="2016-17",
    paper="Mathematics (Class XII)",
    source="PreBoard-PYQ/2016-17/MATHEMATICS.pdf",
    marks=100, time="3 hours",
    intro=r"""<p><em>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT
start writing during this time.)</em></p>
<p><b>Section A</b> – Answer <b>Question 1</b> (compulsory) and <b>five</b> other questions.<br>
<b>Section B and Section C</b> – Answer <b>two</b> questions from <b>either</b> Section B <b>or</b> Section C.<br>
All working, including rough work, should be done on the same sheet as, and adjacent to, the rest of the answer.<br>
The intended marks for questions or parts of questions are given in brackets [ ].<br>
Mathematical tables and graph papers are provided.<br>
Slide rule may be used.</p>""",
    items=[
        SEC("Section A", "Answer Question 1 (compulsory) and five other questions."),

        # ---------------------------------------------------------------- Question 1
        Q("1(a)", 3, r"""<p>Express the matrix \(A=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}\) as a sum of symmetric
and skew-symmetric matrix.</p>""",
          a=r"""<p>Any square matrix can be written as \(A=P+Q\) with \(P=\tfrac12(A+A')\) symmetric and
\(Q=\tfrac12(A-A')\) skew-symmetric.</p>
<p>\(A'=\begin{bmatrix}3&1\\-4&-1\end{bmatrix}\).</p>
<p>\[P=\tfrac12(A+A')=\tfrac12\begin{bmatrix}6&-3\\-3&-2\end{bmatrix}=\begin{bmatrix}3&-\tfrac32\\-\tfrac32&-1\end{bmatrix},
\quad P'=P\ \text{(symmetric)}\]</p>
<p>\[Q=\tfrac12(A-A')=\tfrac12\begin{bmatrix}0&-5\\5&0\end{bmatrix}=\begin{bmatrix}0&-\tfrac52\\\tfrac52&0\end{bmatrix},
\quad Q'=-Q\ \text{(skew-symmetric)}\]</p>
<p>Check: \(P+Q=\begin{bmatrix}3&-4\\1&-1\end{bmatrix}=A\).</p>
<p><span class="box">\(A=\begin{bmatrix}3&-\tfrac32\\-\tfrac32&-1\end{bmatrix}+\begin{bmatrix}0&-\tfrac52\\\tfrac52&0\end{bmatrix}\)</span></p>""",
          topic="Matrices",
          recall=r"""<ul><li>\(A=\tfrac12(A+A')+\tfrac12(A-A')\).</li>
<li>Symmetric: \(P'=P\); skew-symmetric: \(Q'=-Q\) (diagonal entries 0).</li></ul>"""),

        Q("1(b)", 3, r"""<p>Prove that: \(\sin^{-1}\!\left(\dfrac45\right)+\cos^{-1}\!\left(\dfrac{2}{\sqrt5}\right)=\cot^{-1}\!\left(\dfrac{2}{11}\right)\)</p>""",
          a=r"""<p>Let \(\alpha=\sin^{-1}\tfrac45\). Then \(\sin\alpha=\tfrac45,\ \cos\alpha=\tfrac35\), so
\(\tan\alpha=\tfrac43\), i.e. \(\alpha=\tan^{-1}\tfrac43\).</p>
<p>Let \(\beta=\cos^{-1}\tfrac{2}{\sqrt5}\). Then \(\cos\beta=\tfrac{2}{\sqrt5},\ \sin\beta=\tfrac{1}{\sqrt5}\), so
\(\tan\beta=\tfrac12\), i.e. \(\beta=\tan^{-1}\tfrac12\).</p>
<p>Both angles lie in \((0,\tfrac\pi2)\) and \(\tfrac43\cdot\tfrac12=\tfrac23<1\), so</p>
<p>\[\alpha+\beta=\tan^{-1}\frac{\tfrac43+\tfrac12}{1-\tfrac43\cdot\tfrac12}=\tan^{-1}\frac{\tfrac{11}{6}}{\tfrac13}=\tan^{-1}\frac{11}{2}.\]</p>
<p>Since \(\tfrac{11}{2}>0\), \(\tan^{-1}\tfrac{11}{2}=\cot^{-1}\tfrac{2}{11}\).</p>
<p><span class="box">\(\sin^{-1}\tfrac45+\cos^{-1}\tfrac{2}{\sqrt5}=\cot^{-1}\tfrac{2}{11}\)</span> &nbsp;Hence proved.</p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>Convert every term to \(\tan^{-1}\) using a right triangle.</li>
<li>\(\tan^{-1}x+\tan^{-1}y=\tan^{-1}\dfrac{x+y}{1-xy}\) when \(xy<1\).</li>
<li>\(\tan^{-1}x=\cot^{-1}\dfrac1x\) for \(x>0\).</li></ul>"""),

        Q("1(c)", 3, r"""<p>Find the equations of the tangents to the hyperbola \(x^2-2y^2=18\) which are perpendicular
to the straight line \(x-y=0\).</p>
<p class="note">[The paper prints “equations <s>to</s> of”, corrected by hand.]</p>""",
          excluded=CONICS),

        Q("1(d)", 3, r"""<p>Evaluate: \(\displaystyle\lim_{x\to0}\frac{x\cos x-\sin x}{x^2\sin x}\)</p>""",
          excluded="Limits of indeterminate forms (L'Hospital's rule) — limits are a Class XI topic in ISC 2027; the Class XII Calculus unit has no limits or L'Hospital's rule."),

        Q("1(e)", 3, r"""<p>Evaluate: \(\displaystyle\int\frac{(x-\sin x)\,dx}{1-\cos x}\)</p>""",
          a=r"""<p>Use \(1-\cos x=2\sin^2\tfrac x2\) and \(\sin x=2\sin\tfrac x2\cos\tfrac x2\):</p>
<p>\[I=\int\frac{x}{2\sin^2\frac x2}\,dx-\int\frac{2\sin\frac x2\cos\frac x2}{2\sin^2\frac x2}\,dx
=\int\frac x2\,\operatorname{cosec}^2\tfrac x2\,dx-\int\cot\tfrac x2\,dx.\]</p>
<p>By parts in the first integral, with \(u=x\), \(dv=\tfrac12\operatorname{cosec}^2\tfrac x2\,dx\Rightarrow v=-\cot\tfrac x2\):</p>
<p>\[\int\frac x2\,\operatorname{cosec}^2\tfrac x2\,dx=-x\cot\tfrac x2+\int\cot\tfrac x2\,dx.\]</p>
<p>The two \(\int\cot\frac x2\,dx\) terms cancel:</p>
<p><span class="box">\(\displaystyle\int\frac{x-\sin x}{1-\cos x}\,dx=-x\cot\frac x2+C\)</span></p>
<p>Check: \(\dfrac{d}{dx}\left(-x\cot\frac x2\right)=-\cot\frac x2+\dfrac x2\operatorname{cosec}^2\frac x2
=\dfrac{x-\sin x}{2\sin^2\frac x2}\). ✓</p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(1-\cos x=2\sin^2\frac x2\), \(\sin x=2\sin\frac x2\cos\frac x2\).</li>
<li>\(\int\operatorname{cosec}^2(ax)\,dx=-\frac1a\cot(ax)\).</li>
<li>By parts: \(\int u\,dv=uv-\int v\,du\); look for a term that cancels.</li></ul>"""),

        Q("1(f)", 3, r"""<p>Evaluate \(\displaystyle\int_0^{\pi/2}\frac{dx}{1+\tan x}\)</p>""",
          a=r"""<p>\[I=\int_0^{\pi/2}\frac{\cos x}{\cos x+\sin x}\,dx\qquad(1)\]</p>
<p>Using \(\int_0^a f(x)\,dx=\int_0^a f(a-x)\,dx\) with \(a=\tfrac\pi2\) (\(\cos\to\sin,\ \sin\to\cos\)):</p>
<p>\[I=\int_0^{\pi/2}\frac{\sin x}{\sin x+\cos x}\,dx\qquad(2)\]</p>
<p>Adding (1) and (2): \(2I=\displaystyle\int_0^{\pi/2}1\,dx=\frac\pi2\).</p>
<p><span class="box">\(I=\dfrac\pi4\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\int_0^a f(x)\,dx=\int_0^a f(a-x)\,dx\).</li>
<li>On \([0,\frac\pi2]\) this swaps \(\sin x\) and \(\cos x\) — add the two forms.</li></ul>"""),

        Q("1(g)", 3, r"""<p>If the regression equation of \(X\) on \(Y\) is given by \(Kx-y+10=0\) and the regression equation
of \(Y\) on \(X\) is given by \(2x-5y+14=0\), determine the value of \(K\) if the coefficient of correlation between
\(X\) and \(Y\) is \(\dfrac{1}{\sqrt{10}}\).</p>""",
          excluded=REGR),

        Q("1(h)", 3, r"""<p>Find \(\theta\) if \(\dfrac{3+2i\sin\theta}{1-2i\sin\theta}\) is purely imaginary</p>""",
          excluded=COMPLEX),

        Q("1(i)", 3, r"""<p>Two cards are drawn without replacement from a well shuffled pack of 52 cards. Find the probability
that neither a jack nor a card of spades is drawn.</p>""",
          a=r"""<p>Cards that are a jack or a spade: 13 spades + 3 non-spade jacks = 16.</p>
<p>Cards that are neither a jack nor a spade: \(52-16=36\).</p>
<p>Both cards must come from these 36:</p>
<p>\[P=\frac{{}^{36}C_2}{{}^{52}C_2}=\frac{630}{1326}=\frac{105}{221}\]</p>
<p><span class="box">\(P=\dfrac{105}{221}\approx0.475\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>\(n(J\cup S)=n(J)+n(S)-n(J\cap S)=4+13-1\).</li>
<li>Without replacement, “both from a group of \(k\)”: \({}^kC_2/{}^{52}C_2\).</li></ul>"""),

        Q("1(j)", 3, r"""<p>Solve the differential equation: \(\sec^3x\,dy+\sec y\,dx=0\)</p>""",
          a=r"""<p>Separate the variables (divide by \(\sec^3x\sec y\)):</p>
<p>\[\cos y\,dy=-\cos^3x\,dx.\]</p>
<p>Write \(\cos^3x=(1-\sin^2x)\cos x\) and put \(\sin x=t\), \(\cos x\,dx=dt\):</p>
<p>\[\int\cos^3x\,dx=\int(1-t^2)\,dt=\sin x-\frac{\sin^3x}{3}.\]</p>
<p>Integrating both sides: \(\sin y=-\sin x+\dfrac{\sin^3x}{3}+C\).</p>
<p><span class="box">\(\sin y+\sin x-\dfrac{\sin^3x}{3}=C\)</span></p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Variable separable: bring all \(y\) with \(dy\), all \(x\) with \(dx\).</li>
<li>Odd power of \(\cos\): keep one \(\cos x\), convert the rest with \(\cos^2x=1-\sin^2x\).</li></ul>"""),

        # ---------------------------------------------------------------- Question 2
        Q("2(a)", 5, r"""<p>Using properties of determinants, prove that:</p>
<p>\[\begin{vmatrix}a-b-c&2a&2a\\2b&b-c-a&2b\\2c&2c&c-a-b\end{vmatrix}=(a+b+c)^3\]</p>""",
          a=r"""<p>Let \(\Delta\) be the determinant. Apply \(R_1\to R_1+R_2+R_3\); each entry of the new row is
\(a+b+c\):</p>
<p>\[\Delta=\begin{vmatrix}a+b+c&a+b+c&a+b+c\\2b&b-c-a&2b\\2c&2c&c-a-b\end{vmatrix}
=(a+b+c)\begin{vmatrix}1&1&1\\2b&b-c-a&2b\\2c&2c&c-a-b\end{vmatrix}\]</p>
<p>Apply \(C_2\to C_2-C_1\), \(C_3\to C_3-C_1\):</p>
<p>\[\Delta=(a+b+c)\begin{vmatrix}1&0&0\\2b&-(a+b+c)&0\\2c&0&-(a+b+c)\end{vmatrix}\]</p>
<p>(since \(b-c-a-2b=-(a+b+c)\) and \(c-a-b-2c=-(a+b+c)\)).</p>
<p>Expanding along \(R_1\): \(\Delta=(a+b+c)\cdot1\cdot\big[(-(a+b+c))(-(a+b+c))-0\big]\).</p>
<p><span class="box">\(\Delta=(a+b+c)^3\)</span> &nbsp;Hence proved.</p>""",
          topic="Determinants",
          recall=r"""<ul><li>Adding rows to one row does not change the determinant.</li>
<li>A common factor of a row can be taken outside.</li>
<li>Make zeros in a row with \(C_j\to C_j-C_1\), then expand along that row.</li></ul>"""),

        Q("2(b)", 5, r"""<p>If \(A=\begin{bmatrix}5&3&1\\2&1&3\\1&2&4\end{bmatrix}\) find \(A^{-1}\). Hence, solve the system of linear equations</p>
<p>\(5x+3y+z=16,\ 2x+y+3z=19,\) and \(x+2y+4z=25\).</p>""",
          a=r"""<p>\(|A|=5(4-6)-3(8-3)+1(4-1)=-10-15+3=-22\neq0\), so \(A^{-1}\) exists.</p>
<p>Cofactors:</p>
<p>\(C_{11}=-2,\ C_{12}=-5,\ C_{13}=3;\quad C_{21}=-10,\ C_{22}=19,\ C_{23}=-7;\quad C_{31}=8,\ C_{32}=-13,\ C_{33}=-1.\)</p>
<p>\[\operatorname{adj}A=\begin{bmatrix}-2&-10&8\\-5&19&-13\\3&-7&-1\end{bmatrix},\qquad
A^{-1}=\frac{1}{|A|}\operatorname{adj}A=\frac{1}{22}\begin{bmatrix}2&10&-8\\5&-19&13\\-3&7&1\end{bmatrix}\]</p>
<p>The system is \(AX=B\) with \(X=\begin{bmatrix}x\\y\\z\end{bmatrix}\), \(B=\begin{bmatrix}16\\19\\25\end{bmatrix}\), so \(X=A^{-1}B\):</p>
<p>\[X=\frac1{22}\begin{bmatrix}32+190-200\\80-361+325\\-48+133+25\end{bmatrix}=\frac1{22}\begin{bmatrix}22\\44\\110\end{bmatrix}=\begin{bmatrix}1\\2\\5\end{bmatrix}\]</p>
<p><span class="box">\(x=1,\ y=2,\ z=5\)</span></p>
<p>Check: \(5+6+5=16,\ 2+2+15=19,\ 1+4+20=25\). ✓</p>""",
          topic="Determinants",
          recall=r"""<ul><li>\(A^{-1}=\dfrac{\operatorname{adj}A}{|A|}\); adj \(A\) is the <em>transpose</em> of the cofactor matrix.</li>
<li>Cofactor \(C_{ij}=(-1)^{i+j}M_{ij}\).</li>
<li>\(AX=B\Rightarrow X=A^{-1}B\) (unique solution when \(|A|\neq0\)).</li></ul>"""),

        # ---------------------------------------------------------------- Question 3
        Q("3(b)", 5, r"""<p>Solve the for \(x\): \(\sin^{-1}\!\left(\dfrac{x}{\sqrt{1+x^2}}\right)-\sin^{-1}\!\left(\dfrac{1}{\sqrt{1+x^2}}\right)=\sin^{-1}\!\left(\dfrac{1+x}{1+x^2}\right)\)</p>
<p class="note">[Part (b) is printed before part (a) in the paper.]</p>""",
          a=r"""<p><b>Rewrite the left side.</b> For every real \(x\), \(\sin^{-1}\dfrac{x}{\sqrt{1+x^2}}=\tan^{-1}x\).</p>
<p><b>Case \(x>0\).</b> \(\sin^{-1}\dfrac{1}{\sqrt{1+x^2}}=\tan^{-1}\dfrac1x=\dfrac\pi2-\tan^{-1}x\). Put \(\theta=\tan^{-1}x\):</p>
<p>\[\text{LHS}=\theta-\left(\tfrac\pi2-\theta\right)=2\theta-\tfrac\pi2\in\left(-\tfrac\pi2,\tfrac\pi2\right).\]</p>
<p>Taking sine of both sides (sine is one-one on \([-\frac\pi2,\frac\pi2]\)):</p>
<p>\[\sin\!\left(2\theta-\tfrac\pi2\right)=-\cos2\theta=-\frac{1-x^2}{1+x^2}=\frac{x^2-1}{1+x^2}.\]</p>
<p>So \(\dfrac{x^2-1}{1+x^2}=\dfrac{1+x}{1+x^2}\Rightarrow x^2-x-2=0\Rightarrow(x-2)(x+1)=0\Rightarrow x=2\) or \(x=-1\).
Only \(x=2\) satisfies \(x>0\).</p>
<p><b>Case \(x\le0\).</b> Here \(\sin^{-1}\dfrac{1}{\sqrt{1+x^2}}=\dfrac\pi2+\tan^{-1}x\) (for \(x<0\) it equals
\(\tan^{-1}\frac{1}{|x|}=\frac\pi2-|\tan^{-1}x|\); at \(x=0\) both sides are \(\frac\pi2\)), so
LHS \(=\tan^{-1}x-\frac\pi2-\tan^{-1}x=-\dfrac\pi2\). That needs \(\dfrac{1+x}{1+x^2}=-1\), i.e. \(x^2+x+2=0\),
which has no real root. (In particular \(x=-1\) gives LHS \(=-\frac\pi2\) but RHS \(=\sin^{-1}0=0\), so it is rejected.)</p>
<p><b>Check \(x=2\):</b> LHS \(=\sin^{-1}\frac{2}{\sqrt5}-\sin^{-1}\frac1{\sqrt5}\), whose sine is
\(\frac2{\sqrt5}\cdot\frac2{\sqrt5}-\frac1{\sqrt5}\cdot\frac1{\sqrt5}=\frac35\); RHS \(=\sin^{-1}\frac35\). ✓</p>
<p><span class="box">\(x=2\)</span></p>""",
          topic="Inverse Trigonometric Functions",
          recall=r"""<ul><li>\(\sin^{-1}\dfrac{x}{\sqrt{1+x^2}}=\tan^{-1}x\) (draw the triangle with sides \(x,1,\sqrt{1+x^2}\)).</li>
<li>\(\tan^{-1}x+\tan^{-1}\frac1x=\frac\pi2\) for \(x>0\), \(-\frac\pi2\) for \(x<0\).</li>
<li>\(\cos2\theta=\dfrac{1-\tan^2\theta}{1+\tan^2\theta}\).</li>
<li>Always substitute back: squaring/taking sines can create extra roots.</li></ul>"""),

        Q("3(a)", 5, r"""<p>Construct a switching circuit representing the polynomial: \((A+B)(B'+C)+(B+C)(A'+C')\)</p>
<p>Use laws of Boolean Algebra to simplify the expression and construct the simplified switching circuit.</p>""",
          excluded="Boolean algebra and switching circuits — removed from ISC Mathematics; not in the ISC 2027 Class XII units."),

        # ---------------------------------------------------------------- Question 4
        Q("4(a)", 5, r"""<p>Using Lagrange's Mean Value Theorem find a point on the curve \(f(x)=2\sin x+\sin2x-x\) defined on
the interval \([0,\pi]\) where the tangent is parallel to the chord joining the end points of the curve.</p>""",
          excluded="Mean value theorems (Rolle's / Lagrange's) — not in the ISC 2027 Class XII Calculus unit."),

        Q("4(b)", 5, r"""<p>Show that the equation \(5x^2+30x+2y+59=0\) represents a parabola. Find its (i) focus (ii) Length of
Latus rectum (iii) Equation of directrix (iv) Equation of axis.</p>""",
          excluded=CONICS),

        # ---------------------------------------------------------------- Question 5
        Q("5(a)", 5, r"""<p>If \(y=\left(x+\sqrt{x^2-1}\right)^m\) then show that \((x^2-1)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}=m^2y\)</p>""",
          a=r"""<p>Differentiate with the chain rule:</p>
<p>\[\begin{aligned}\frac{dy}{dx}&=m\left(x+\sqrt{x^2-1}\right)^{m-1}\left(1+\frac{x}{\sqrt{x^2-1}}\right)\\
&=m\left(x+\sqrt{x^2-1}\right)^{m-1}\cdot\frac{x+\sqrt{x^2-1}}{\sqrt{x^2-1}}=\frac{my}{\sqrt{x^2-1}}.\end{aligned}\]</p>
<p>So \(\sqrt{x^2-1}\,y_1=my\). Squaring: \((x^2-1)y_1^2=m^2y^2\).</p>
<p>Differentiate again with respect to \(x\):</p>
<p>\[(x^2-1)\cdot2y_1y_2+2x\,y_1^2=m^2\cdot2y\,y_1.\]</p>
<p>Divide by \(2y_1\) (\(y_1\neq0\)):</p>
<p><span class="box">\((x^2-1)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}=m^2y\)</span> &nbsp;Hence proved.</p>""",
          topic="Continuity, Differentiability and Differentiation",
          recall=r"""<ul><li>\(\dfrac{d}{dx}\sqrt{x^2-1}=\dfrac{x}{\sqrt{x^2-1}}\).</li>
<li>For second-order identities: get \(y_1\) in terms of \(y\), square to remove the root, then differentiate again.</li></ul>"""),

        Q("5(b)", 5, r"""<p>A cylinder is such that the sum of its height and circumference of its base is 10 meters. Find the
maximum volume of the cylinder.</p>""",
          a=r"""<p>Let radius \(=r\) m, height \(=h\) m. Given \(h+2\pi r=10\Rightarrow h=10-2\pi r\).</p>
<p>\[V=\pi r^2h=\pi r^2(10-2\pi r)=10\pi r^2-2\pi^2r^3,\qquad 0\lt r\lt\tfrac5\pi.\]</p>
<p>\(\dfrac{dV}{dr}=20\pi r-6\pi^2r^2=2\pi r(10-3\pi r)\). Setting \(\dfrac{dV}{dr}=0\) (with \(r\neq0\)): \(r=\dfrac{10}{3\pi}\).</p>
<p>\(\dfrac{d^2V}{dr^2}=20\pi-12\pi^2r\); at \(r=\frac{10}{3\pi}\): \(20\pi-40\pi=-20\pi<0\), so \(V\) is maximum.</p>
<p>Then \(h=10-2\pi\cdot\dfrac{10}{3\pi}=\dfrac{10}{3}\) m and</p>
<p>\[V_{\max}=\pi\left(\frac{10}{3\pi}\right)^2\cdot\frac{10}{3}=\frac{1000}{27\pi}\ \text{m}^3.\]</p>
<p><span class="box">\(V_{\max}=\dfrac{1000}{27\pi}\ \text{m}^3\approx11.8\ \text{m}^3\)</span> (when \(r=\frac{10}{3\pi}\) m, \(h=\frac{10}{3}\) m)</p>""",
          topic="Applications of Derivatives",
          recall=r"""<ul><li>Use the constraint to write \(V\) in one variable.</li>
<li>\(V'=0\) for critical points; \(V''<0\Rightarrow\) maximum.</li>
<li>Circumference \(=2\pi r\), volume \(=\pi r^2h\).</li></ul>"""),

        # ---------------------------------------------------------------- Question 6
        Q("6(a)", 5, r"""<p>Evaluate: \(\displaystyle\int\left(\sqrt{\tan x}+\sqrt{\cot x}\right)dx\)</p>""",
          a=r"""<p>(Taking \(0\lt x\lt\frac\pi2\), where both roots are real.)</p>
<p>\[I=\int\left(\sqrt{\frac{\sin x}{\cos x}}+\sqrt{\frac{\cos x}{\sin x}}\right)dx=\int\frac{\sin x+\cos x}{\sqrt{\sin x\cos x}}\,dx.\]</p>
<p>Put \(\sin x-\cos x=t\). Then \((\cos x+\sin x)\,dx=dt\) and
\(t^2=1-2\sin x\cos x\Rightarrow\sin x\cos x=\dfrac{1-t^2}{2}\).</p>
<p>\[I=\int\frac{dt}{\sqrt{\frac{1-t^2}{2}}}=\sqrt2\int\frac{dt}{\sqrt{1-t^2}}=\sqrt2\sin^{-1}t+C.\]</p>
<p><span class="box">\(\displaystyle\int\left(\sqrt{\tan x}+\sqrt{\cot x}\right)dx=\sqrt2\,\sin^{-1}(\sin x-\cos x)+C\)</span></p>""",
          topic="Integrals",
          recall=r"""<ul><li>\(\sqrt{\tan x}+\sqrt{\cot x}=\dfrac{\sin x+\cos x}{\sqrt{\sin x\cos x}}\).</li>
<li>Numerator \(\sin x+\cos x\) ⇒ substitute \(t=\sin x-\cos x\); then \(2\sin x\cos x=1-t^2\).</li>
<li>\(\int\dfrac{dt}{\sqrt{1-t^2}}=\sin^{-1}t\).</li></ul>"""),

        Q("6(b)", 5, r"""<p>Find the area enclosed by the curve \(y^2=2x-x^2\) and the straight line \(y=x\).</p>
<p class="note">[Unclear in the original: the exponent on \(y\) is a faint mark, but the printed gap between \(y\) and “=”
is the width of a superscript, so it is read as \(y^2\) (a circle), which is a standard question; if it is \(y=2x-x^2\) the area is \(\frac16\) sq. unit — worked at the end.]</p>""",
          a=r"""<p>\(y^2=2x-x^2\iff(x-1)^2+y^2=1\): a circle with centre \(C(1,0)\) and radius 1, through the origin.</p>
<p><b>Points of intersection</b> with \(y=x\): \(x^2=2x-x^2\Rightarrow2x(x-1)=0\Rightarrow x=0,1\); points \(O(0,0)\), \(P(1,1)\).</p>
{{fig:0}}
<p>The line cuts off the shaded segment between the upper semicircle \(y=\sqrt{2x-x^2}\) and the line, for \(0\le x\le1\):</p>
<p>\[A=\int_0^1\left(\sqrt{2x-x^2}-x\right)dx=\int_0^1\sqrt{1-(x-1)^2}\,dx-\int_0^1x\,dx.\]</p>
<p>With \(t=x-1\) and \(\int\sqrt{1-t^2}\,dt=\frac t2\sqrt{1-t^2}+\frac12\sin^{-1}t\):</p>
<p>\[\int_{-1}^{0}\sqrt{1-t^2}\,dt=\left[\tfrac t2\sqrt{1-t^2}+\tfrac12\sin^{-1}t\right]_{-1}^{0}=0-\left(-\tfrac\pi4\right)=\tfrac\pi4,
\qquad\int_0^1x\,dx=\tfrac12.\]</p>
<p><span class="box">\(A=\left(\dfrac\pi4-\dfrac12\right)\) sq. units \(\approx0.285\) sq. units</span></p>
<p>(Check: quarter circle \(OCP\) has area \(\frac\pi4\), triangle \(OCP\) has area \(\frac12\); the segment is their difference.)</p>
<p><b>If the curve is read as \(y=2x-x^2\):</b> intersections are again \(x=0,1\), and
\(A=\int_0^1\left[(2x-x^2)-x\right]dx=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1=\frac16\) sq. unit.</p>
{{fig:1}}""",
          afig=[(F.fig_q6b_circle, "y² = 2x − x² is the circle (x − 1)² + y² = 1; the shaded segment is the required area."),
                (F.fig_q6b_parabola, "Alternative reading y = 2x − x²: the region between the parabola and y = x.")],
          topic="Application of Integrals",
          recall=r"""<ul><li>Complete the square to recognise the curve: \(x^2+y^2=2x\) is a circle.</li>
<li>Area between curves \(=\int_a^b(y_{\text{upper}}-y_{\text{lower}})\,dx\), limits from the intersections.</li>
<li>\(\int\sqrt{a^2-t^2}\,dt=\frac t2\sqrt{a^2-t^2}+\frac{a^2}2\sin^{-1}\frac ta+C\).</li></ul>"""),

        # ---------------------------------------------------------------- Question 7
        Q("7(a)", 5, r"""<p>The coefficient of correlation between the values denoted by X and Y is 0.5. The mean of X is 3 and
that of \(Y\) is 5. Their standard deviations are 5 and 4 respectively. Find:</p>
<p>(i) the two lines of regression.<br>(ii) the expected value of \(Y\), when \(X\) is given 14.<br>
(iii) the expected value of \(X\), when \(Y\) is given 9.</p>""",
          excluded=REGR),

        Q("7(b)", 5, r"""<p>Find the Spearman's coefficient of rank correlation between the marks obtained in Mathematics &amp;
Statistics. Also interpret the results.</p>
<table class="data"><tr><th>Student</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th></tr>
<tr><th>Mathematics</th><td>30</td><td>20</td><td>40</td><td>50</td><td>30</td><td>20</td><td>30</td><td>50</td><td>10</td><td>05</td></tr>
<tr><th>Statistics</th><td>15</td><td>40</td><td>40</td><td>45</td><td>20</td><td>30</td><td>15</td><td>50</td><td>20</td><td>10</td></tr></table>
<p class="note">[E's Mathematics mark “30” is handwritten on the paper.]</p>""",
          excluded="Spearman's rank correlation — dropped from ISC Mathematics; not in the ISC 2027 Class XII units."),

        # ---------------------------------------------------------------- Question 8
        Q("8(a)", 5, r"""<p>Two cards are drawn at random from a pack of 52 cards without replacement. Find the probability that</p>
<p>(i) the cards drawn are either both red cards or both jacks.<br>
(ii) one of the cards dawn is a jack of red colour and the other one is a card of spade.</p>""",
          a=r"""<p>Total ways: \({}^{52}C_2=1326\).</p>
<p><b>(i)</b> Let \(R\): both red, \(J\): both jacks. \(R\cap J\): both red jacks.</p>
<p>\(n(R)={}^{26}C_2=325,\quad n(J)={}^4C_2=6,\quad n(R\cap J)={}^2C_2=1\).</p>
<p>\[P(R\cup J)=\frac{325+6-1}{1326}=\frac{330}{1326}=\frac{55}{221}\]</p>
<p><span class="box">(i) \(\dfrac{55}{221}\)</span></p>
<p><b>(ii)</b> Choose one red jack (2 ways) and one spade (13 ways; no red jack is a spade, so the two choices never overlap):</p>
<p>\[P=\frac{2\times13}{1326}=\frac{26}{1326}=\frac1{51}\]</p>
<p><span class="box">(ii) \(\dfrac{1}{51}\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Addition theorem: \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\).</li>
<li>Drawing 2 cards together/without replacement: count with combinations, order ignored.</li></ul>"""),

        Q("8(b)", 5, r"""<p>Bag A contains 4 white balls and 3 black balls, while Bag B contains 2 white balls and 2 black balls.
Two balls are transferred from Bag A to Bag B. Find the probability of drawing 1 white ball and 1 black ball from Bag B.</p>
<p class="note">[Two balls are drawn from Bag B, which then holds 6 balls.]</p>""",
          a=r"""<p>Let \(E_1\): 2 white transferred, \(E_2\): 1 white and 1 black transferred, \(E_3\): 2 black transferred.
\(E_1,E_2,E_3\) are mutually exclusive and exhaustive (\({}^7C_2=21\)):</p>
<p>\(P(E_1)=\dfrac{{}^4C_2}{21}=\dfrac6{21},\quad P(E_2)=\dfrac{4\cdot3}{21}=\dfrac{12}{21},\quad P(E_3)=\dfrac{{}^3C_2}{21}=\dfrac3{21}.\)</p>
<p>Let \(A\): two balls drawn from Bag B (6 balls, \({}^6C_2=15\)) are 1 white and 1 black.</p>
<table class="data"><tr><th></th><th>Bag B then has</th><th>\(P(A\mid E_i)\)</th></tr>
<tr><td>\(E_1\)</td><td>4 W, 2 B</td><td>\(\frac{4\cdot2}{15}=\frac8{15}\)</td></tr>
<tr><td>\(E_2\)</td><td>3 W, 3 B</td><td>\(\frac{3\cdot3}{15}=\frac9{15}\)</td></tr>
<tr><td>\(E_3\)</td><td>2 W, 4 B</td><td>\(\frac{2\cdot4}{15}=\frac8{15}\)</td></tr></table>
<p>By the theorem of total probability:</p>
<p>\[P(A)=\frac6{21}\cdot\frac8{15}+\frac{12}{21}\cdot\frac9{15}+\frac3{21}\cdot\frac8{15}=\frac{48+108+24}{315}=\frac{180}{315}=\frac47.\]</p>
<p><span class="box">\(P=\dfrac47\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Total probability: \(P(A)=\sum P(E_i)\,P(A\mid E_i)\) over exhaustive, mutually exclusive cases.</li>
<li>List every possible transfer and the new contents of the bag.</li></ul>"""),

        # ---------------------------------------------------------------- Question 9
        Q("9(a)", 5, r"""<p>Find the locus of the complex number \(z=x+iy\), satisfying the relation \(|z-1|+|z+1|=4\).
Illustrate the locus in Argand plane.</p>""",
          excluded=COMPLEX),

        Q("9(b)", 5, r"""<p>Solve the differential equation: \((x^2-y^2)\,dx+2xy\,dy=0\), given that \(y=1\) when \(x=1\).</p>""",
          a=r"""<p>\(\dfrac{dy}{dx}=\dfrac{y^2-x^2}{2xy}\) — homogeneous (degree 2 above and below). Put \(y=vx\), \(\dfrac{dy}{dx}=v+x\dfrac{dv}{dx}\):</p>
<p>\[v+x\frac{dv}{dx}=\frac{v^2-1}{2v}\ \Rightarrow\ x\frac{dv}{dx}=\frac{v^2-1-2v^2}{2v}=-\frac{1+v^2}{2v}.\]</p>
<p>Separating: \(\dfrac{2v}{1+v^2}\,dv=-\dfrac{dx}{x}\). Integrating:</p>
<p>\[\begin{aligned}\log(1+v^2)&=-\log|x|+\log C\\ \Rightarrow\ x(1+v^2)&=C\ \Rightarrow\ x\left(1+\frac{y^2}{x^2}\right)=C\ \Rightarrow\ x^2+y^2=Cx.\end{aligned}\]</p>
<p>At \(x=1,\ y=1\): \(1+1=C\Rightarrow C=2\).</p>
<p><span class="box">\(x^2+y^2=2x\)</span></p>""",
          topic="Differential Equations",
          recall=r"""<ul><li>Homogeneous: \(\frac{dy}{dx}=f\!\left(\frac yx\right)\); substitute \(y=vx\).</li>
<li>\(\int\dfrac{f'(v)}{f(v)}dv=\log|f(v)|\).</li>
<li>Use the given point to find \(C\) for the particular solution.</li></ul>"""),

        SEC("Section B", "(Attempt any two question)"),

        Q("10(a)", 5, r"""<p>Using vectors prove that in any triangle ABC, \(\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}\)</p>""",
          excluded="Proof of a geometrical theorem (sine rule) using vectors — the ISC 2027 Vector Algebra unit states “Proofs of geometrical theorems by using Vector algebra are excluded”."),

        Q("10(b)", 5, r"""<p>If \(\vec a,\vec b,\vec c\) are three non-zero, non-coplanar vectors, \(\vec p,\vec q,\vec r\) are vectors defined by the relations</p>
<p>\[\vec p=\frac{\vec b\times\vec c}{[\vec a\ \vec b\ \vec c]},\quad \vec q=\frac{\vec c\times\vec a}{[\vec a\ \vec b\ \vec c]},\quad \vec r=\frac{\vec a\times\vec b}{[\vec a\ \vec b\ \vec c]}.\]</p>
<p>Prove that: \((\vec a+\vec b)\cdot\vec p+(\vec b+\vec c)\cdot\vec q+(\vec c+\vec a)\cdot\vec r=3\)</p>""",
          excluded="Scalar triple product [a b c] (reciprocal vectors) — the ISC 2027 Vector Algebra unit lists only dot and cross products; the scalar triple product is not in it."),

        Q("11(a)", 5, r"""<p>Find the shortest distance between the lines whose vector equations are:</p>
<p>\(\vec r=3\hat i+8\hat j+3\hat k+\lambda(3\hat i-\hat j+\hat k)\) and \(\vec r=-3\hat i-7\hat j+6\hat k+\mu(3\hat i-2\hat j-4\hat k)\)</p>""",
          a=r"""<p>Here \(\vec a_1=3\hat i+8\hat j+3\hat k,\ \vec b_1=3\hat i-\hat j+\hat k;\quad \vec a_2=-3\hat i-7\hat j+6\hat k,\ \vec b_2=3\hat i-2\hat j-4\hat k\).</p>
<p>\[\vec b_1\times\vec b_2=\begin{vmatrix}\hat i&\hat j&\hat k\\3&-1&1\\3&-2&-4\end{vmatrix}
=\hat i(4+2)-\hat j(-12-3)+\hat k(-6+3)=6\hat i+15\hat j-3\hat k,\]</p>
<p>\(|\vec b_1\times\vec b_2|=\sqrt{36+225+9}=\sqrt{270}=3\sqrt{30}\).</p>
<p>\(\vec a_2-\vec a_1=-6\hat i-15\hat j+3\hat k\), so \((\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)=-36-225-9=-270\).</p>
<p>\[d=\left|\frac{(\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)}{|\vec b_1\times\vec b_2|}\right|=\frac{270}{3\sqrt{30}}=\frac{90}{\sqrt{30}}=3\sqrt{30}.\]</p>
<p><span class="box">Shortest distance \(=3\sqrt{30}\) units \(\approx16.43\) units</span></p>
<p>(Since \(d\neq0\), the lines are skew.)</p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Skew lines \(\vec r=\vec a_1+\lambda\vec b_1,\ \vec r=\vec a_2+\mu\vec b_2\):
\(d=\dfrac{|(\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)|}{|\vec b_1\times\vec b_2|}\).</li>
<li>If \(d=0\) the lines intersect.</li></ul>"""),

        Q("11(b)", 5, r"""<p>Find the equation of the plane passing through the line of intersection of the planes
\(\vec r\cdot(4\hat i-\hat j+\hat k)=0\), \(\vec r\cdot(3\hat i+\hat j-\hat k)=5\) and parallel to the straight line
\(\vec r=4\hat i-3\hat j+\hat k+\lambda(\hat i-2\hat j+3\hat k)\)</p>""",
          a=r"""<p>Any plane through the line of intersection:</p>
<p>\[\begin{aligned}&\vec r\cdot(4\hat i-\hat j+\hat k)+k\left[\vec r\cdot(3\hat i+\hat j-\hat k)-5\right]=0\\
\Rightarrow\ &\vec r\cdot\big[(4+3k)\hat i+(k-1)\hat j+(1-k)\hat k\big]=5k.\end{aligned}\]</p>
<p>The plane is parallel to the line, so its normal is perpendicular to the line's direction \(\hat i-2\hat j+3\hat k\):</p>
<p>\[(4+3k)(1)+(k-1)(-2)+(1-k)(3)=0\ \Rightarrow\ 9-2k=0\ \Rightarrow\ k=\tfrac92.\]</p>
<p>Normal \(=\tfrac{35}{2}\hat i+\tfrac72\hat j-\tfrac72\hat k\), right side \(=\tfrac{45}{2}\). Multiplying by 2:</p>
<p><span class="box">\(\vec r\cdot(35\hat i+7\hat j-7\hat k)=45\), i.e. \(35x+7y-7z=45\)</span></p>
<p>Check: normal \(\cdot\) direction \(=35-14-21=0\) ✓.</p>""",
          topic="Three-dimensional Geometry",
          recall=r"""<ul><li>Plane through the intersection of \(\vec r\cdot\vec n_1=d_1\) and \(\vec r\cdot\vec n_2=d_2\):
\(\vec r\cdot(\vec n_1+k\vec n_2)=d_1+kd_2\).</li>
<li>Plane parallel to a line ⇔ normal \(\perp\) direction of the line: \(\vec n\cdot\vec b=0\).</li></ul>"""),

        Q("12(a)", 5, r"""<p>There are three urns, Urn I contains 1 white, 2 black, and 3 red balls. Urn II contains 2 white, 1 black and
1 red balls. Urn III contains 4 white, 5 black, and 3 red balls. One urn is chosen at random and two balls drawn
without replacement. They happen to be 1 white and 1 red ball. What is the probability that they belongs to Urn II.</p>""",
          a=r"""<p>Let \(E_1,E_2,E_3\): urn I, II, III is chosen; \(P(E_i)=\frac13\). Let \(A\): the two balls are 1 white and 1 red.</p>
<p>\(P(A\mid E_1)=\dfrac{1\cdot3}{{}^6C_2}=\dfrac3{15}=\dfrac15,\quad
P(A\mid E_2)=\dfrac{2\cdot1}{{}^4C_2}=\dfrac26=\dfrac13,\quad
P(A\mid E_3)=\dfrac{4\cdot3}{{}^{12}C_2}=\dfrac{12}{66}=\dfrac2{11}.\)</p>
<p>By Bayes' theorem:</p>
<p>\[P(E_2\mid A)=\frac{\frac13\cdot\frac13}{\frac13\left(\frac15+\frac13+\frac2{11}\right)}
=\frac{\frac13}{\frac{33+55+30}{165}}=\frac{\frac13}{\frac{118}{165}}=\frac{165}{354}=\frac{55}{118}.\]</p>
<p><span class="box">\(P(\text{Urn II}\mid\text{1 white, 1 red})=\dfrac{55}{118}\approx0.466\)</span></p>""",
          topic="Probability",
          recall=r"""<ul><li>Bayes: \(P(E_i\mid A)=\dfrac{P(E_i)P(A\mid E_i)}{\sum_j P(E_j)P(A\mid E_j)}\).</li>
<li>Equal priors cancel — only the likelihoods \(P(A\mid E_i)\) matter.</li></ul>"""),

        Q("12(b)", 5, r"""<p>Three cards are drawn successively with replacement from a well-shuffled deck of 52 cards. Find the
probability distribution of the number of spades drawn. Also find the mean and standard deviation of the distribution.</p>""",
          a=r"""<p>Let \(X\) = number of spades. With replacement the three draws are independent, each a spade with
\(p=\frac{13}{52}=\frac14\), not a spade with \(q=\frac34\). \(X\) takes values 0, 1, 2, 3 and
\(P(X=r)={}^3C_r\left(\frac14\right)^r\left(\frac34\right)^{3-r}\):</p>
<table class="data"><tr><th>\(X\)</th><td>0</td><td>1</td><td>2</td><td>3</td></tr>
<tr><th>\(P(X)\)</th><td>\(\frac{27}{64}\)</td><td>\(\frac{27}{64}\)</td><td>\(\frac{9}{64}\)</td><td>\(\frac{1}{64}\)</td></tr>
<tr><th>\(X\,P(X)\)</th><td>0</td><td>\(\frac{27}{64}\)</td><td>\(\frac{18}{64}\)</td><td>\(\frac{3}{64}\)</td></tr>
<tr><th>\(X^2P(X)\)</th><td>0</td><td>\(\frac{27}{64}\)</td><td>\(\frac{36}{64}\)</td><td>\(\frac{9}{64}\)</td></tr></table>
<p>(Total of \(P(X)\) is \(\frac{64}{64}=1\) ✓.)</p>
<p>Mean: \(\mu=\sum XP(X)=\dfrac{48}{64}=\dfrac34\). <span class="box">Mean \(=\dfrac34\)</span></p>
<p>Variance: \(\sigma^2=\sum X^2P(X)-\mu^2=\dfrac{72}{64}-\dfrac9{16}=\dfrac98-\dfrac9{16}=\dfrac9{16}\).</p>
<p><span class="box">Standard deviation \(\sigma=\dfrac34\)</span></p>
<p class="note">ISC 2027 lists the probability distribution and the <em>mean</em> of a random variable; the variance/standard
deviation step is shown for completeness.</p>""",
          topic="Probability",
          recall=r"""<ul><li>With replacement ⇒ independent trials: \(P(X=r)={}^nC_rp^rq^{n-r}\).</li>
<li>Mean \(=\sum x_ip_i\); variance \(=\sum x_i^2p_i-\mu^2\).</li></ul>"""),

        SEC("Section C", "(Attempt any two question)"),

        Q("13(a)", 5, r"""<p>Mr Sen considers the purchase of two different insurance annuities. Annuity X will pay him Rs 10000 per year
for 8 years while Annuity Y will pay him Rs 8000 per year for 12 years. Assuming Mr Sen's money is worth 10% and that
each costs the same today, which Annuity Mr Sen would prefer?</p>""",
          excluded=COMMERCE.format("annuities")),

        Q("13(b)", 5, r"""<p>Suppose every gram of wheat provides 0.1 gm of proteins and 0.25 gm of carbohydrates, while every gram of rice
provides 0.05 gm of proteins and 0.5 gm of proteins. Wheat cost Rs 5 per kg while rice cost Rs 20 per kg. The minimum
daily requirements of protein and carbohydrate for a normal person are 50 gm and 200 gm respectively. In what quantities
should wheat and rice be mixed in the daily diet to provide minimum daily requirements of proteins and carbohydrates at
minimum cost, assuming that both wheat and rice are to be taken in diet?</p>
<p class="note">[Misprint in the original: rice's “0.5 gm of proteins” must be 0.5 gm of <em>carbohydrates</em>.]</p>""",
          a=r"""<p><b>Formulation.</b> Let the diet contain \(x\) g of wheat and \(y\) g of rice. Cost: wheat Rs 5/kg = Rs 0.005 per g,
rice Rs 20/kg = Rs 0.02 per g.</p>
<p>Minimise \(Z=0.005x+0.02y\) subject to</p>
<p>\[0.1x+0.05y\ge50\ \Rightarrow\ 2x+y\ge1000\quad\text{(protein)}\]
\[0.25x+0.5y\ge200\ \Rightarrow\ x+2y\ge800\quad\text{(carbohydrate)}\]
\[x\ge0,\ y\ge0.\]</p>
<p><b>Graph.</b> \(2x+y=1000\) through \((500,0),(0,1000)\); \(x+2y=800\) through \((800,0),(0,400)\). Both are “\(\ge\)”, so the
feasible region lies on the side away from the origin — the unbounded shaded region. The lines meet where
\(2x+y=1000,\ x+2y=800\Rightarrow x=400,\ y=200\).</p>
{{fig:0}}
<table class="data"><tr><th>Corner point</th><th>\(Z=0.005x+0.02y\) (Rs)</th></tr>
<tr><td>A(0, 1000)</td><td>20</td></tr><tr><td>B(400, 200)</td><td>6</td></tr><tr><td>C(800, 0)</td><td><b>4</b> (least)</td></tr></table>
<p>The region is unbounded, so check the open half-plane \(Z<4\), i.e. \(x+4y<800\): it has no point in common with the
feasible region (any feasible point has \(x+2y\ge800\), so \(x+4y\ge800\)). Hence the minimum is Rs 4 at C.</p>
<p><span class="box">Minimum cost Rs 4 per day: 800 g of wheat and no rice</span></p>
<p class="note">On “both wheat and rice are to be taken”: with these prices wheat is cheaper per gram of protein and per
gram of carbohydrate, so the optimum uses no rice. If some rice is insisted on, the cost can be brought as close to
Rs 4 as we like (points on CB near C), but no positive-rice mix attains a minimum; the only corner with both foods,
B (400 g wheat, 200 g rice), costs Rs 6. The data as printed (probably copied with altered prices) do not support
a mixed optimum. In the familiar version of this problem neither food dominates — e.g. wheat Rs 4 per kg and rice
Rs 6 per kg give corner costs A Rs 6, B Rs 2.80, C Rs 3.20 — and the optimum is then the mixed corner B: 400 g of
wheat and 200 g of rice. That is evidently the answer the question's last line expects.</p>""",
          afig=[(F.fig_q13b_lpp, "Feasible region (shaded, unbounded) for 2x + y ≥ 1000, x + 2y ≥ 800, x, y ≥ 0; dashed: iso-cost line Z = 4 touching the region only at C.")],
          topic="Linear Programming",
          recall=r"""<ul><li>Convert all units first (Rs per kg → Rs per g).</li>
<li>Corner-point method: evaluate \(Z\) at each vertex of the feasible region.</li>
<li>Unbounded region: the minimum \(m\) is valid only if \(Z\lt m\) has no point in common with the region.</li></ul>"""),

        Q("14(a)", 5, r"""<p>The banker's gain on a certain bill due 6 months hence is Rs 10, the rate of interest being 10% per annum.
Find (i) face value of the bill. (ii) Banker's Discount and (iii) True Discount</p>""",
          excluded=COMMERCE.format("banker's discount")),

        Q("14(b)", 5, r"""<p>The average cost function for \(x\) units of a commodity is \(AC=\dfrac{x^2}{3}+3x-7+\dfrac{16}{x}\).</p>
<p>(i) Find the Marginal Cost.<br>(ii) Show that the Marginal Average cost is given by \(\dfrac{x(MC)-C(x)}{x^2}\)</p>""",
          topic="Applications of Derivatives (rate of change)",
          a=r"""<p class="step"><b>(i)</b> Total cost \(C(x) = x\cdot AC\):</p>
\[C(x)=x\left(\frac{x^2}{3}+3x-7+\frac{16}{x}\right)=\frac{x^3}{3}+3x^2-7x+16.\]
<p class="step">Marginal cost is the rate of change of total cost with output:</p>
\[MC=\frac{dC}{dx}=x^2+6x-7.\]
<p><span class="box">\(MC = x^2+6x-7\)</span></p>
<p class="step"><b>(ii)</b> Marginal average cost is the rate of change of average cost:
\(MAC=\dfrac{d}{dx}(AC)=\dfrac{d}{dx}\left(\dfrac{C(x)}{x}\right)\).</p>
<p class="step">By the quotient rule,</p>
\[\frac{d}{dx}\left(\frac{C(x)}{x}\right)=\frac{x\,C'(x)-C(x)\cdot 1}{x^2}=\frac{x(MC)-C(x)}{x^2},\]
<p class="step">since \(C'(x)=MC\). Hence \(MAC=\dfrac{x(MC)-C(x)}{x^2}\). \(\blacksquare\)</p>
<p class="step">Check with the given function: \(\dfrac{d}{dx}(AC)=\dfrac{2x}{3}+3-\dfrac{16}{x^2}\), and
\(\dfrac{x(x^2+6x-7)-\left(\frac{x^3}{3}+3x^2-7x+16\right)}{x^2}=\dfrac{\frac{2x^3}{3}+3x^2-16}{x^2}=\dfrac{2x}{3}+3-\dfrac{16}{x^2}\). ✓</p>""",
          recall=r"""<ul><li>\(C(x)=x\cdot AC(x)\)</li><li>Marginal cost \(MC=\dfrac{dC}{dx}\); marginal average cost \(=\dfrac{d(AC)}{dx}\)</li>
<li>Quotient rule: \(\left(\dfrac{u}{v}\right)'=\dfrac{vu'-uv'}{v^2}\)</li></ul>"""),

        Q("15(a)", 5, r"""<p>Find the consumer index number for the year 2016 using 2015 as the base year by using the weighted average of
price relative method</p>
<table class="data"><tr><th>Commodity</th><th>Base price<br>2015 price per unit (in Rs)</th><th>Current Price<br>2016 price per unit (in Rs)</th><th>weights</th></tr>
<tr><td>Rice</td><td>16.00</td><td>20.00</td><td>40</td></tr>
<tr><td>Wheat</td><td>40.00</td><td>60.00</td><td>25</td></tr>
<tr><td>Fish</td><td>0.50</td><td>0.50</td><td>5</td></tr>
<tr><td>Potato</td><td>5.12</td><td>6.25</td><td>20</td></tr>
<tr><td>Coal</td><td>2.00</td><td>1.5</td><td>10</td></tr></table>
<p class="note">[The printed table is misaligned — the base-price column lines up with the commodity names, but the
current-price and weight columns are shifted one row up (Rice's 20.00 and 40 sit in the header row); rows are read in order.]</p>""",
          excluded=COMMERCE.format("index numbers")),

        Q("15(b)", 5, r"""<p>Calculate the 4-yearly moving averages from the following data and calculate the trend by method of moving
average:</p>
<table class="data"><tr><th>Year</th><td>1981</td><td>1982</td><td>1983</td><td>1984</td><td>1985</td><td>1986</td><td>1987</td><td>1988</td><td>1989</td><td>1990</td></tr>
<tr><th>Number</th><td>12</td><td>25</td><td>39</td><td>54</td><td>70</td><td>87</td><td>105</td><td>100</td><td>82</td><td>65</td></tr></table>""",
          excluded=COMMERCE.format("moving averages / time series")),
    ])
