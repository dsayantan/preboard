"""JEE Main mock test 1 — Mathematics (Q51-75).  Every item adapted from a kept pre-board question."""
from jee_kit import MCQ, NUM
import maths_figs as F

SUBJECT = "maths"
TEST = 1

QUESTIONS = [
    # 51 ----------------------------------------------------------------- Relations and Functions
    MCQ(src=("maths_2024_25_s1", "1(ix)"), topic="Relations and Functions",
        q=r"<p>The number of onto functions from \(A=\{1,2,3,4,5\}\) to \(B=\{p,q\}\) is</p>",
        options=[r"\(30\)", r"\(32\)", r"\(25\)", r"\(31\)"],
        answer=0,
        sol=r"""<p>Of the \(2^5=32\) functions \(A\to B\), exactly two are not onto: the two constant
functions (everything to \(p\), or everything to \(q\)). So the number of onto functions is
\(32-2=30\).</p>
<p>\(32\) counts all functions; \(31\) removes only one constant function; \(25=5^2\) confuses
\(|B|^{|A|}\) with \(|A|^{|B|}\).</p><p><b>Answer: \(30\).</b></p>"""),

    # 52 ----------------------------------------------------------------- Relations and Functions
    MCQ(src=("maths_2024_25_s2", "1(i)"), topic="Relations and Functions",
        q=r"""<p>On the set \(L\) of all straight lines in a plane, the relation \(R\) is defined by
\(\ell_1\,R\,\ell_2 \iff \ell_1\perp\ell_2\). Then \(R\) is</p>""",
        options=[r"reflexive and symmetric but not transitive",
                 r"an equivalence relation",
                 r"symmetric but neither reflexive nor transitive",
                 r"transitive but not symmetric"],
        answer=2,
        sol=r"""<p><b>Reflexive?</b> No line is perpendicular to itself, so \((\ell,\ell)\notin R\).</p>
<p><b>Symmetric?</b> If \(\ell_1\perp\ell_2\) then \(\ell_2\perp\ell_1\). Yes.</p>
<p><b>Transitive?</b> \(\ell_1\perp\ell_2\) and \(\ell_2\perp\ell_3\) make \(\ell_1\parallel\ell_3\),
not perpendicular. No.</p>
<p>So the first two options fail (not reflexive), and the last fails (it is symmetric and not
transitive).</p><p><b>Answer: symmetric but neither reflexive nor transitive.</b></p>"""),

    # 53 ----------------------------------------------------------------- Inverse Trigonometric Functions
    MCQ(src=("maths_2013_14", "1(iii)"), topic="Inverse Trigonometric Functions",
        q=r"<p>The set of all solutions of \(\tan^{-1}(2x)+\tan^{-1}(3x)=\dfrac{\pi}{4}\) is</p>",
        options=[r"\(\left\{-1,\ \tfrac16\right\}\)", r"\(\left\{\tfrac16\right\}\)",
                 r"\(\{-1\}\)", r"\(\left\{1,\ -\tfrac16\right\}\)"],
        answer=1,
        sol=r"""<p>Take \(\tan\) of both sides: \(\dfrac{2x+3x}{1-6x^2}=1\Rightarrow 6x^2+5x-1=0
\Rightarrow (6x-1)(x+1)=0\), so \(x=\tfrac16\) or \(x=-1\).</p>
<p><b>Check.</b> At \(x=-1\) both terms are negative, so the left side is negative and cannot equal
\(\tfrac{\pi}{4}\) (in fact it equals \(-\tfrac{3\pi}{4}\)). At \(x=\tfrac16\):
\(6x^2=\tfrac16\lt 1\), so the addition formula holds and the sum is \(\tfrac{\pi}{4}\).</p>
<p>The option \(\{-1,\tfrac16\}\) is what one gets by not checking the roots.</p>
<p><b>Answer: \(x=\tfrac16\) only.</b></p>"""),

    # 54 ----------------------------------------------------------------- Matrices
    MCQ(src=("maths_2016_17", "1(a)"), topic="Matrices",
        q=r"""<p>If \(A=\begin{bmatrix}2&5\\-1&3\end{bmatrix}\) is written as \(A=P+Q\) with \(P\)
symmetric and \(Q\) skew-symmetric, then \(Q\) is</p>""",
        options=[r"\(\begin{bmatrix}0&6\\-6&0\end{bmatrix}\)",
                 r"\(\begin{bmatrix}0&-3\\3&0\end{bmatrix}\)",
                 r"\(\begin{bmatrix}2&2\\2&3\end{bmatrix}\)",
                 r"\(\begin{bmatrix}0&3\\-3&0\end{bmatrix}\)"],
        answer=3,
        sol=r"""<p>\(Q=\tfrac12(A-A^{T})=\tfrac12\left(\begin{bmatrix}2&5\\-1&3\end{bmatrix}-
\begin{bmatrix}2&-1\\5&3\end{bmatrix}\right)=\tfrac12\begin{bmatrix}0&6\\-6&0\end{bmatrix}
=\begin{bmatrix}0&3\\-3&0\end{bmatrix}\).</p>
<p>(Check: \(P=\tfrac12(A+A^T)=\begin{bmatrix}2&2\\2&3\end{bmatrix}\) and \(P+Q=A\).) The other
options are \(A-A^T\) without the \(\tfrac12\), \(\tfrac12(A^T-A)\) (sign slip) and \(P\) itself.</p>
<p><b>Answer: \(\begin{bmatrix}0&3\\-3&0\end{bmatrix}\).</b></p>"""),

    # 55 ----------------------------------------------------------------- Determinants
    MCQ(src=("maths_2024_25_s1", "1(i)"), topic="Determinants",
        q=r"<p>If \(A=\begin{bmatrix}3&1\\4&2\end{bmatrix}\), then \(|A\,(\operatorname{adj}A)|\) equals</p>",
        options=[r"\(2\)", r"\(4\)", r"\(8\)", r"\(16\)"],
        answer=1,
        sol=r"""<p>\(|A|=6-4=2\). For any square matrix of order \(n\), \(A(\operatorname{adj}A)=|A|\,I_n\), so
\(|A(\operatorname{adj}A)|=|A|^{n}\). Here \(n=2\): \(|A(\operatorname{adj}A)|=2^2=4\).</p>
<p>\(8=|A|^3\) uses \(n=3\); \(2\) forgets that the scalar comes out to the power \(n\);
\(16=|A|^4\).</p><p><b>Answer: \(4\).</b></p>"""),

    # 56 ----------------------------------------------------------------- Determinants
    MCQ(src=("maths_2025_26", "1(viii)"), topic="Determinants",
        q=r"""<p>The value of \(\begin{vmatrix}p&p&p\\p&p+x&p\\p&p&p+y\end{vmatrix}\) is</p>""",
        options=[r"\(pxy\)", r"\(p^2xy\)", r"\(pxy(p+x+y)\)", r"\(0\)"],
        answer=0,
        sol=r"""<p>\(R_2\to R_2-R_1,\ R_3\to R_3-R_1\):
\(\begin{vmatrix}p&p&p\\0&x&0\\0&0&y\end{vmatrix}\), an upper-triangular determinant, so its value is
the product of the diagonal: \(p\cdot x\cdot y\).</p>
<p><b>Answer: \(pxy\).</b></p>"""),

    # 57 ----------------------------------------------------------------- Continuity and Differentiability
    MCQ(src=("maths_2024_25_s2", "1(viii)"), topic="Continuity and Differentiability",
        q=r"<p>If \(y=|x-2|+|x-5|\), then \(\dfrac{dy}{dx}\) at \(x=6\) is</p>",
        options=[r"\(0\)", r"\(-2\)", r"\(1\)", r"\(2\)"],
        answer=3,
        sol=r"""<p>Near \(x=6\) both \(x-2\gt 0\) and \(x-5\gt 0\), so \(y=(x-2)+(x-5)=2x-7\) and
\(\dfrac{dy}{dx}=2\).</p>
<p>\(0\) is the slope on \(2\lt x\lt 5\) (where \(y=3\)); \(-2\) is the slope for \(x\lt 2\).</p>
<p><b>Answer: \(2\).</b></p>"""),

    # 58 ----------------------------------------------------------------- Continuity and Differentiability
    MCQ(src=("maths_2025_26", "1(xiv)"), topic="Continuity and Differentiability",
        q=r"""<p>The number of points in the open interval \((-2,\,3)\) at which
\(f(x)=\dfrac{1}{x-[x]}\) is discontinuous (\([\cdot]\) = greatest integer function; a point at
which \(f\) is not defined is to be counted as a point of discontinuity) is</p>""",
        options=[r"\(5\)", r"\(0\)", r"\(4\)", r"infinitely many"],
        answer=2,
        sol=r"""<p>\(x-[x]=\{x\}\) is zero exactly at the integers, so \(f\) is undefined (hence discontinuous)
there; between consecutive integers \(\{x\}=x-n\) is continuous and non-zero, so \(f\) is
continuous.</p>
<p>Integers in the <i>open</i> interval \((-2,3)\): \(-1,0,1,2\) — four points.</p>
<p>\(5\) counts an end-point, which is not in the open interval; \(0\) is what one gets by judging
continuity only on the domain \(\mathbb R\setminus\mathbb Z\) — excluded here by the stem, which
counts the points where \(f\) is undefined; "infinitely many" is true on all of \(\mathbb R\), not on
a bounded interval.</p><p><b>Answer: \(4\).</b></p>"""),

    # 59 ----------------------------------------------------------------- Applications of Derivatives
    MCQ(src=("maths_2024_25_s2", "1(vi)"), topic="Applications of Derivatives",
        q=r"<p>The function \(f(x)=x^3-27x+5\) is strictly increasing in</p>",
        options=[r"\((-\infty,-3)\) and \((3,\infty)\)", r"\((-3,3)\)", r"\((-\infty,3)\)",
                 r"\((-3,\infty)\)"],
        answer=0,
        sol=r"""<p>\(f'(x)=3x^2-27=3(x-3)(x+3)\gt 0 \iff x\lt -3\) or \(x\gt 3\).</p>
<p>On \((-3,3)\) \(f'\lt 0\), so \(f\) decreases there; the two half-lines in the other options
each contain part of \((-3,3)\).</p>
<p>(Note: \(f\) is strictly increasing on each of the two intervals separately, not on their union —
\(f(-4)=49\gt f(4)=-39\).)</p>
<p><b>Answer: \((-\infty,-3)\) and \((3,\infty)\).</b></p>"""),

    # 60 ----------------------------------------------------------------- Applications of Derivatives
    MCQ(src=("maths_2024_25_s1", "4"), topic="Applications of Derivatives",
        q=r"""<p>The point on the curve \(\sqrt x+\sqrt y=6\) at which the tangent is equally inclined to the
coordinate axes is</p>""",
        options=[r"\((3,3)\)", r"\((9,9)\)", r"\((6,6)\)", r"\((16,4)\)"],
        answer=1,
        sol=r"""<p>Differentiate: \(\dfrac{1}{2\sqrt x}+\dfrac{1}{2\sqrt y}\dfrac{dy}{dx}=0\Rightarrow
\dfrac{dy}{dx}=-\dfrac{\sqrt y}{\sqrt x}\).</p>
<p>Equally inclined to the axes means slope \(\pm1\); the slope here is always negative, so
\(-\sqrt{y}/\sqrt{x}=-1\Rightarrow x=y\). Then \(2\sqrt x=6\Rightarrow x=9\).</p>
<p>\((3,3)\) and \((6,6)\) are not on the curve (\(2\sqrt3\ne6\), \(2\sqrt6\ne6\)); \((16,4)\) is on
the curve but its slope is \(-\tfrac12\).</p><p><b>Answer: \((9,9)\).</b></p>"""),

    # 61 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2013_14", "1(v)"), topic="Integrals",
        q=r"<p>\(\displaystyle\int e^x\left(\frac{1+\sin x}{1+\cos x}\right)dx\) is equal to</p>",
        options=[r"\(e^x\cot\dfrac x2+C\)", r"\(-e^x\tan\dfrac x2+C\)",
                 r"\(e^x\tan\dfrac x2+C\)", r"\(\tfrac12e^x\sec^2\dfrac x2+C\)"],
        answer=2,
        sol=r"""<p>\(\dfrac{1+\sin x}{1+\cos x}=\dfrac{1+2\sin\frac x2\cos\frac x2}{2\cos^2\frac x2}
=\tfrac12\sec^2\dfrac x2+\tan\dfrac x2\).</p>
<p>With \(f(x)=\tan\frac x2\), \(f'(x)=\tfrac12\sec^2\frac x2\), so the integrand is
\(e^x\{f(x)+f'(x)\}\) and \(\displaystyle\int e^x\{f+f'\}\,dx=e^xf(x)+C\).</p>
<p><b>Answer: \(e^x\tan\dfrac x2+C\).</b></p>"""),

    # 62 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2016_17", "1(f)"), topic="Integrals",
        q=r"<p>\(\displaystyle\int_{\pi/6}^{\pi/3}\frac{dx}{1+\sqrt{\tan x}}\) is equal to</p>",
        options=[r"\(\dfrac{\pi}{6}\)", r"\(\dfrac{\pi}{4}\)", r"\(\dfrac{\pi}{3}\)", r"\(\dfrac{\pi}{12}\)"],
        answer=3,
        sol=r"""<p>Write \(I=\displaystyle\int_{\pi/6}^{\pi/3}\frac{\sqrt{\cos x}}{\sqrt{\cos x}+\sqrt{\sin x}}dx\).
Using \(\int_a^bf(x)\,dx=\int_a^bf(a+b-x)\,dx\) with \(a+b=\tfrac\pi2\) swaps \(\sin\) and
\(\cos\):</p>
<p>\(I=\displaystyle\int_{\pi/6}^{\pi/3}\frac{\sqrt{\sin x}}{\sqrt{\sin x}+\sqrt{\cos x}}dx\).
Adding, \(2I=\displaystyle\int_{\pi/6}^{\pi/3}1\,dx=\frac{\pi}{6}\), so \(I=\dfrac{\pi}{12}\).</p>
<p>\(\tfrac\pi6\) forgets to halve; \(\tfrac\pi4\) is the answer over \([0,\tfrac\pi2]\).</p>
<p><b>Answer: \(\dfrac{\pi}{12}\).</b></p>"""),

    # 63 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2024_25_s1", "3"), topic="Integrals",
        q=r"<p>\(\displaystyle\int_0^{3\pi/2}|\cos x|\,dx\) is equal to</p>",
        options=[r"\(3\)", r"\(-1\)", r"\(1\)", r"\(2\)"],
        answer=0,
        sol=r"""<p>\(\cos x\ge0\) on \([0,\tfrac\pi2]\) and \(\le0\) on \([\tfrac\pi2,\tfrac{3\pi}2]\):</p>
<p>\(\displaystyle\int_0^{\pi/2}\cos x\,dx-\int_{\pi/2}^{3\pi/2}\cos x\,dx=[\sin x]_0^{\pi/2}-[\sin x]_{\pi/2}^{3\pi/2}
=1-(-1-1)=3\).</p>
<p>\(-1\) is \(\int_0^{3\pi/2}\cos x\,dx\) with the modulus ignored; \(1\) and \(2\) take only one of
the two pieces.</p><p><b>Answer: \(3\).</b></p>"""),

    # 64 ----------------------------------------------------------------- Application of Integrals
    MCQ(src=("maths_2013_14", "6(b)"), topic="Application of Integrals",
        q=r"<p>The area of the region bounded by the parabola \(y^2=x\) and the line \(y=x-2\) is</p>",
        options=[r"\(\dfrac{10}{3}\)", r"\(9\)", r"\(\dfrac{9}{2}\)", r"\(\dfrac{7}{6}\)"],
        answer=2,
        sol=r"""<p>Intersections: \(y^2=y+2\Rightarrow y=-1,\,2\), i.e. \((1,-1)\) and \((4,2)\). Integrate
along \(y\): the line \(x=y+2\) is to the right of the parabola \(x=y^2\).</p>
<p>\(A=\displaystyle\int_{-1}^{2}\big[(y+2)-y^2\big]dy=\Big[\frac{y^2}{2}+2y-\frac{y^3}{3}\Big]_{-1}^{2}
=\frac{10}{3}-\Big(-\frac{7}{6}\Big)=\frac{9}{2}\).</p>
<p>\(\tfrac{10}3\) and \(\tfrac76\) are the two halves of the evaluation (one end-point only);
\(9\) doubles the area.</p><p><b>Answer: \(\dfrac92\) sq. units.</b></p>""",
        sfig=(F.fig_jt1_area, "The region between \\(x=y^2\\) and \\(x=y+2\\), \\(-1\\le y\\le2\\).")),

    # 65 ----------------------------------------------------------------- Differential Equations
    MCQ(src=("maths_2015_16", "9(b)"), topic="Differential Equations",
        q=r"""<p>If \(y(x)\) satisfies \((1-x^2)\dfrac{dy}{dx}-xy=x\) for \(|x|\lt1\) and \(y(0)=1\), then
\(y\!\left(\dfrac{\sqrt3}{2}\right)\) equals</p>""",
        options=[r"\(4\)", r"\(3\)", r"\(1\)", r"\(5\)"],
        answer=1,
        sol=r"""<p>Linear form: \(\dfrac{dy}{dx}-\dfrac{x}{1-x^2}\,y=\dfrac{x}{1-x^2}\).
I.F. \(=e^{-\int\frac{x}{1-x^2}dx}=e^{\frac12\log(1-x^2)}=\sqrt{1-x^2}\).</p>
<p>\(y\sqrt{1-x^2}=\displaystyle\int\frac{x}{\sqrt{1-x^2}}\,dx=-\sqrt{1-x^2}+C\Rightarrow
y=-1+\frac{C}{\sqrt{1-x^2}}\).</p>
<p>\(y(0)=1\Rightarrow C=2\). At \(x=\tfrac{\sqrt3}{2}\): \(\sqrt{1-x^2}=\tfrac12\), so
\(y=-1+4=3\).</p><p>(\(4\) drops the \(-1\).) <b>Answer: \(3\).</b></p>"""),

    # 66 ----------------------------------------------------------------- Differential Equations
    MCQ(src=("maths_2025_26", "1(iii)"), topic="Differential Equations",
        q=r"""<p>If \(m\) and \(n\) are the order and degree of the differential equation
\(\dfrac{d}{dx}\left[\left(\dfrac{dy}{dx}\right)^4\right]=0\), then \(m+n\) is</p>""",
        options=[r"\(5\)", r"\(6\)", r"\(2\)", r"\(3\)"],
        answer=3,
        sol=r"""<p>Carry out the differentiation: \(4\left(\dfrac{dy}{dx}\right)^3\dfrac{d^2y}{dx^2}=0\).
The highest derivative is \(\dfrac{d^2y}{dx^2}\) (order \(m=2\)) and it appears to the power 1
(degree \(n=1\)). So \(m+n=3\).</p>
<p>Reading the equation before differentiating gives order 1, degree 4 (sum 5) — wrong, because
the outer \(\dfrac{d}{dx}\) raises the order; \(6\) mixes order 2 with power 4.</p>
<p><b>Answer: \(3\).</b></p>"""),

    # 67 ----------------------------------------------------------------- Vector Algebra
    MCQ(src=("maths_2024_25_s1", "16"), topic="Vector Algebra",
        q=r"""<p>If \(|\vec a|=2\), \(|\vec b|=\dfrac{1}{\sqrt3}\) and \(\vec a\times\vec b\) is a unit vector,
then the angle \(\theta\) between \(\vec a\) and \(\vec b\) is</p>""",
        options=[r"\(\dfrac{\pi}{3}\) only", r"\(\dfrac{\pi}{3}\) or \(\dfrac{2\pi}{3}\)",
                 r"\(\dfrac{\pi}{6}\) or \(\dfrac{5\pi}{6}\)", r"\(\dfrac{\pi}{6}\) only"],
        answer=1,
        sol=r"""<p>\(|\vec a\times\vec b|=|\vec a||\vec b|\sin\theta=\dfrac{2}{\sqrt3}\sin\theta=1
\Rightarrow\sin\theta=\dfrac{\sqrt3}{2}\).</p>
<p>With \(0\le\theta\le\pi\), both \(\theta=\tfrac\pi3\) and \(\theta=\tfrac{2\pi}3\) work — the
magnitude of the cross product cannot tell an acute angle from its supplement. (\(\tfrac\pi6\)
comes from using \(\cos\theta\) instead of \(\sin\theta\).)</p>
<p><b>Answer: \(\dfrac\pi3\) or \(\dfrac{2\pi}3\).</b></p>"""),

    # 68 ----------------------------------------------------------------- Three-dimensional Geometry
    MCQ(src=("maths_2024_25_s1", "15(ii)"), topic="Three-dimensional Geometry",
        q=r"""<p>If a line makes angles \(\alpha,\beta,\gamma\) with the positive coordinate axes, then
\(\cos2\alpha+\cos2\beta+\cos2\gamma\) equals</p>""",
        options=[r"\(-1\)", r"\(1\)", r"\(2\)", r"\(-2\)"],
        answer=0,
        sol=r"""<p>\(\cos2\theta=2\cos^2\theta-1\) and \(\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1\):</p>
<p>\(\sum\cos2\alpha=2\sum\cos^2\alpha-3=2-3=-1\).</p>
<p>\(1\) uses \(\sum\cos^2=1\) directly; \(2\) is \(\sum\sin^2\alpha\).</p>
<p><b>Answer: \(-1\).</b></p>"""),

    # 69 ----------------------------------------------------------------- Three-dimensional Geometry
    MCQ(src=("maths_2024_25_s1", "15(iii)"), topic="Three-dimensional Geometry",
        q=r"""<p>The planes \(\vec r\cdot(3\hat i-\lambda\hat j+2\hat k)=1\) and
\(\vec r\cdot(\lambda\hat i+4\hat j-\hat k)=5\) are perpendicular. Then \(\lambda\) equals</p>""",
        options=[r"\(2\)", r"\(\tfrac12\)", r"\(-2\)", r"\(-\tfrac{2}{7}\)"],
        answer=2,
        sol=r"""<p>Planes are perpendicular when their normals are:
\(\vec n_1\cdot\vec n_2=3\lambda-4\lambda-2=-\lambda-2=0\Rightarrow\lambda=-2\).</p>
<p>\(2\) is the sign slip \(+\lambda-2=0\); \(-\tfrac27\) comes from \(3\lambda+4\lambda+2=0\)
(dropping the minus on \(\lambda\hat j\)).</p><p><b>Answer: \(\lambda=-2\).</b></p>"""),

    # 70 ----------------------------------------------------------------- Probability
    MCQ(src=("maths_2013_14", "12(a)"), topic="Probability",
        q=r"""<p>Machines \(M_1,M_2,M_3\) produce \(30\%,30\%\) and \(40\%\) of a factory's bolts, of which
\(2\%,3\%\) and \(4\%\) respectively are defective. A bolt chosen at random is defective. The
probability that it was made by \(M_3\) is</p>""",
        options=[r"\(\dfrac{6}{31}\)", r"\(\dfrac{9}{31}\)", r"\(\dfrac{2}{5}\)", r"\(\dfrac{16}{31}\)"],
        answer=3,
        sol=r"""<p>\(P(D)=0.3(0.02)+0.3(0.03)+0.4(0.04)=0.006+0.009+0.016=0.031\).</p>
<p>Bayes: \(P(M_3\mid D)=\dfrac{0.016}{0.031}=\dfrac{16}{31}\).</p>
<p>\(\tfrac6{31},\tfrac9{31}\) are the posteriors of \(M_1,M_2\); \(\tfrac25\) is the prior of
\(M_3\).</p><p><b>Answer: \(\dfrac{16}{31}\).</b></p>"""),

    # ===================================================================== Section B (integer)
    # 71 ----------------------------------------------------------------- Applications of Derivatives
    NUM(src=("maths_2013_14", "5(b)"), topic="Applications of Derivatives",
        q=r"""<p>A right circular cone is inscribed in a sphere of radius \(9\) cm. If the volume of the cone
is maximum, its height (in cm) is ______.</p>""",
        answer=12,
        sol=r"""<p>Let the cone have height \(h\) and base radius \(\rho\), its vertex at the top of the sphere.
The base is at distance \(h-9\) from the centre, so \(\rho^2=81-(h-9)^2=18h-h^2\).</p>
<p>\(V=\tfrac13\pi\rho^2h=\tfrac{\pi}{3}(18h^2-h^3)\);
\(\dfrac{dV}{dh}=\tfrac\pi3(36h-3h^2)=0\Rightarrow h=12\) and
\(\dfrac{d^2V}{dh^2}=\tfrac\pi3(36-6h)=-12\pi\lt0\) there, a maximum. (In general \(h=\tfrac{4r}{3}\).)</p>
<p><b>Answer: \(12\).</b></p>"""),

    # 72 ----------------------------------------------------------------- Linear Programming
    NUM(src=("maths_2024_25_s1", "22"), topic="Linear Programming",
        q=r"""<p>The maximum value of \(Z=3x+5y\) subject to \(x+y\le70\), \(x+2y\le100\), \(2x+y\le120\),
\(x\ge0\), \(y\ge0\) is ______.</p>""",
        answer=270,
        sol=r"""<p>Corner points of the feasible region: \(O(0,0)\), \((60,0)\) (on \(2x+y=120\)),
\((50,20)\) (\(x+y=70\) with \(2x+y=120\)), \((40,30)\) (\(x+y=70\) with \(x+2y=100\)) and
\((0,50)\).</p>
<p>\(Z\): \(0,\ 180,\ 250,\ 270,\ 250\). The maximum is \(270\) at \((40,30)\).</p>
<p><b>Answer: \(270\).</b></p>""",
        sfig=(F.fig_jt1_lpp, "Feasible region; \\(Z\\) is largest at \\((40,30)\\).")),

    # 73 ----------------------------------------------------------------- Probability
    NUM(src=("maths_2016_17", "12(b)"), topic="Probability",
        q=r"""<p>Four cards are drawn successively <i>with replacement</i> from a well-shuffled pack of 52
cards. If \(X\) is the number of spades drawn, then \(16\,\operatorname{Var}(X)\) is ______.</p>""",
        answer=12,
        sol=r"""<p>Each draw is a spade with probability \(p=\tfrac14\), independently, so \(X\sim B(4,\tfrac14)\).</p>
<p>\(\operatorname{Var}(X)=npq=4\cdot\tfrac14\cdot\tfrac34=\tfrac34\), and
\(16\operatorname{Var}(X)=12\).</p><p><b>Answer: \(12\).</b></p>"""),

    # 74 ----------------------------------------------------------------- Matrices and Determinants
    NUM(src=("maths_2013_14", "2(b)"), topic="Determinants",
        q=r"""<p>If \((x,y,z)\) is the solution of \(4x+2y+3z=5,\ x+y+z=2,\ 3x+y-2z=7\), then
\(x^2+y^2+z^2\) is ______.</p>""",
        answer=6,
        sol=r"""<p>\(A=\begin{bmatrix}4&2&3\\1&1&1\\3&1&-2\end{bmatrix}\), \(|A|=4(-3)-2(-5)+3(-2)=-8\ne0\),
so the solution is unique: \(X=A^{-1}B\) with
\(\operatorname{adj}A=\begin{bmatrix}-3&7&-1\\5&-17&-1\\-2&2&2\end{bmatrix}\).</p>
<p>\(X=-\tfrac18\begin{bmatrix}-3&7&-1\\5&-17&-1\\-2&2&2\end{bmatrix}\begin{bmatrix}5\\2\\7\end{bmatrix}
=-\tfrac18\begin{bmatrix}-8\\-16\\8\end{bmatrix}=\begin{bmatrix}1\\2\\-1\end{bmatrix}\).</p>
<p>\(x^2+y^2+z^2=1+4+1=6\).</p><p><b>Answer: \(6\).</b></p>"""),

    # 75 ----------------------------------------------------------------- Integrals
    NUM(src=("maths_2013_14", "1(vi)"), topic="Integrals",
        q=r"<p>If \(\displaystyle\int_0^{K}\frac{dx}{9+x^2}=\frac{\pi}{12}\) with \(K\gt0\), then \(K\) is ______.</p>",
        answer=3,
        sol=r"""<p>\(\displaystyle\int_0^K\frac{dx}{9+x^2}=\frac13\tan^{-1}\frac K3=\frac\pi{12}\Rightarrow
\tan^{-1}\frac K3=\frac\pi4\Rightarrow K=3\).</p><p><b>Answer: \(3\).</b></p>"""),
]
