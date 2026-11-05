"""JEE Main mock test 3 — Mathematics (Q51-75).  Every item adapted from a kept pre-board question."""
from jee_kit import MCQ, NUM
import maths_figs as F

SUBJECT = "maths"
TEST = 3

QUESTIONS = [
    # 51 ----------------------------------------------------------------- Relations and Functions
    MCQ(src=("maths_2025_26", "1(xii)"), topic="Relations and Functions",
        q=r"<p>The relation \(R=\{(b,b)\}\) on the set \(\{a,b,c\}\) is</p>",
        options=[r"reflexive only", r"symmetric and transitive but not reflexive",
                 r"an equivalence relation", r"transitive but not symmetric"],
        answer=1,
        sol=r"""<p><b>Reflexive?</b> No: \((a,a)\) and \((c,c)\) are missing.</p>
<p><b>Symmetric?</b> Yes: the only pair \((b,b)\) is its own reverse.</p>
<p><b>Transitive?</b> Yes: the only chain is \((b,b),(b,b)\), giving \((b,b)\in R\).</p>
<p>Not reflexive rules out "reflexive only" and "equivalence"; it is symmetric, which rules out the
last option.</p><p><b>Answer: symmetric and transitive but not reflexive.</b></p>"""),

    # 52 ----------------------------------------------------------------- Relations and Functions
    MCQ(src=("maths_2024_25_s2", "1(ix)"), topic="Relations and Functions",
        q=r"""<p><b>Statement I:</b> \(f:\mathbb Z\to\mathbb Z\), \(f(x)=2x+3\), is one-one and onto.<br>
<b>Statement II:</b> \(g:\mathbb R\to\mathbb R\), \(g(x)=2x+3\), is one-one and onto.</p>""",
        options=[r"Both statements are true", r"Both statements are false",
                 r"Statement I is true, Statement II is false",
                 r"Statement I is false, Statement II is true"],
        answer=3,
        sol=r"""<p>Both maps are one-one: \(2x_1+3=2x_2+3\Rightarrow x_1=x_2\).</p>
<p><b>Onto?</b> For \(y\in\mathbb Z\), the pre-image \(x=\frac{y-3}{2}\) must be an integer, which fails
for even \(y\) (e.g. \(y=0\) needs \(x=-\tfrac32\notin\mathbb Z\)). So \(f\) is not onto: Statement I is
false. For \(g\), \(x=\frac{y-3}{2}\in\mathbb R\) always, so \(g\) is onto: Statement II is true.</p>
<p><b>Answer: Statement I is false, Statement II is true.</b></p>"""),

    # 53 ----------------------------------------------------------------- Inverse Trigonometric Functions
    MCQ(src=("maths_2025_26", "7"), topic="Inverse Trigonometric Functions",
        q=r"<p>For \(0\lt x\lt1\), \(\sin\!\left[\cot^{-1}\left\{\tan\left(\cos^{-1}x\right)\right\}\right]\) equals</p>",
        options=[r"\(\sqrt{1-x^2}\)", r"\(\dfrac{1}{x}\)", r"\(x\)", r"\(\dfrac{x}{\sqrt{1-x^2}}\)"],
        answer=2,
        sol=r"""<p>Let \(\theta=\cos^{-1}x\in(0,\tfrac\pi2)\). Then \(\tan\theta\gt0\) and
\(\cot^{-1}(\tan\theta)=\cot^{-1}\big(\cot(\tfrac\pi2-\theta)\big)=\tfrac\pi2-\theta\), since
\(\tfrac\pi2-\theta\in(0,\pi)\).</p>
<p>\(\sin\left(\tfrac\pi2-\theta\right)=\cos\theta=x\).</p>
<p>\(\sqrt{1-x^2}=\sin\theta\) comes from forgetting the \(\cot^{-1}\) step.</p>
<p><b>Answer: \(x\).</b></p>"""),

    # 54 ----------------------------------------------------------------- Inverse Trigonometric Functions
    MCQ(src=("maths_2015_16", "1(iii)"), topic="Inverse Trigonometric Functions",
        q=r"<p>All real solutions of \(\cos\left(2\tan^{-1}x\right)=\dfrac12\) are</p>",
        options=[r"\(x=\pm\dfrac{1}{\sqrt3}\)", r"\(x=\dfrac{1}{\sqrt3}\) only", r"\(x=\pm\sqrt3\)", r"\(x=\pm1\)"],
        answer=0,
        sol=r"""<p>Let \(\theta=\tan^{-1}x\). \(\cos2\theta=\dfrac{1-\tan^2\theta}{1+\tan^2\theta}=\dfrac{1-x^2}{1+x^2}=\dfrac12\)
\(\Rightarrow 2-2x^2=1+x^2\Rightarrow x^2=\dfrac13\).</p>
<p>Both signs work, because \(\cos2\theta\) is even in \(\theta\) (\(2\theta=\pm\tfrac\pi3\), both inside
\((-\pi,\pi)\)). \(\pm\sqrt3\) solves \(\cos2\theta=-\tfrac12\).</p>
<p><b>Answer: \(x=\pm\dfrac1{\sqrt3}\).</b></p>"""),

    # 55 ----------------------------------------------------------------- Matrices
    MCQ(src=("maths_2025_26", "3"), topic="Matrices",
        q=r"<p>The matrix \(\begin{bmatrix}2&x^2\\2x+8&5\end{bmatrix}\) is symmetric for</p>",
        options=[r"\(x=-4\) or \(x=2\)", r"\(x=4\) only", r"\(x=4\) or \(x=-2\)", r"\(x=2\) or \(x=-2\)"],
        answer=2,
        sol=r"""<p>Symmetric \(\iff a_{12}=a_{21}\): \(x^2=2x+8\Rightarrow x^2-2x-8=0\Rightarrow(x-4)(x+2)=0\).</p>
<p>Both roots are valid (at \(x=-2\) both entries are \(4\); at \(x=4\), both are \(16\)).
\(x=-4\) or \(2\) solves \(x^2=-2x+8\) (sign slip).</p>
<p><b>Answer: \(x=4\) or \(x=-2\).</b></p>"""),

    # 56 ----------------------------------------------------------------- Determinants
    MCQ(src=("maths_2016_17", "2(a)"), topic="Determinants",
        q=r"""<p>\(\begin{vmatrix}a-b-c&2a&2a\\2b&b-c-a&2b\\2c&2c&c-a-b\end{vmatrix}\) is equal to</p>""",
        options=[r"\(-(a+b+c)^3\)", r"\((a+b+c)^3\)", r"\(2(a+b+c)^3\)", r"\((a+b+c)(a^2+b^2+c^2)\)"],
        answer=1,
        sol=r"""<p>\(R_1\to R_1+R_2+R_3\): every entry of \(R_1\) becomes \(a+b+c\). Take it out:
\((a+b+c)\begin{vmatrix}1&1&1\\2b&b-c-a&2b\\2c&2c&c-a-b\end{vmatrix}\).</p>
<p>\(C_2\to C_2-C_1,\ C_3\to C_3-C_1\):
\((a+b+c)\begin{vmatrix}1&0&0\\2b&-(a+b+c)&0\\2c&0&-(a+b+c)\end{vmatrix}=(a+b+c)^3\).</p>
<p>(Spot check \(a=1,b=c=0\): the determinant is \(\begin{vmatrix}1&2&2\\0&-1&0\\0&0&-1\end{vmatrix}=1\).)</p>
<p><b>Answer: \((a+b+c)^3\).</b></p>"""),

    # 57 ----------------------------------------------------------------- Determinants
    MCQ(src=("maths_2024_25_s1", "1(x)"), topic="Determinants",
        q=r"<p>\(A\) is a square matrix of order 3 with \(|A|=-3\). Then \(|2A^{-1}|\) equals</p>",
        options=[r"\(\dfrac83\)", r"\(-\dfrac23\)", r"\(-\dfrac38\)", r"\(-\dfrac83\)"],
        answer=3,
        sol=r"""<p>\(|kA|=k^n|A|\) and \(|A^{-1}|=\dfrac1{|A|}\). With \(n=3\):
\(|2A^{-1}|=2^3\cdot\dfrac{1}{-3}=-\dfrac83\).</p>
<p>\(-\tfrac23\) takes the scalar out once instead of \(n\) times; \(\tfrac83\) loses the sign;
\(-\tfrac38\) inverts the whole answer.</p><p><b>Answer: \(-\dfrac83\).</b></p>"""),

    # 58 ----------------------------------------------------------------- Continuity and Differentiability
    MCQ(src=("maths_2024_25_s1", "2"), topic="Continuity and Differentiability",
        q=r"<p>If \(y=e^{2\sin^{-1}x}\), then \(\dfrac{d^2y}{dx^2}\) at \(x=0\) is</p>",
        options=[r"\(4\)", r"\(2\)", r"\(0\)", r"\(8\)"],
        answer=0,
        sol=r"""<p>\(y'=\dfrac{2y}{\sqrt{1-x^2}}\Rightarrow\sqrt{1-x^2}\,y'=2y\). Square and differentiate:
\((1-x^2)y'^2=4y^2\Rightarrow(1-x^2)\,2y'y''-2xy'^2=8yy'\).</p>
<p>Divide by \(2y'\): \((1-x^2)y''-xy'=4y\).</p>
<p>At \(x=0\): \(y=1\), so \(y''(0)=4\). (\(2\) is \(y'(0)\).)</p><p><b>Answer: \(4\).</b></p>"""),

    # 59 ----------------------------------------------------------------- Continuity and Differentiability
    MCQ(src=("maths_2016_17", "5(a)"), topic="Continuity and Differentiability",
        q=r"""<p>If \(y=\left(x+\sqrt{x^2-1}\right)^m\) \((x\gt1)\), then
\((x^2-1)\dfrac{d^2y}{dx^2}+x\dfrac{dy}{dx}\) equals</p>""",
        options=[r"\(-m^2y\)", r"\(my\)", r"\(m^2y\)", r"\(m^2\)"],
        answer=2,
        sol=r"""<p>\(y'=m\big(x+\sqrt{x^2-1}\big)^{m-1}\Big(1+\dfrac{x}{\sqrt{x^2-1}}\Big)=\dfrac{my}{\sqrt{x^2-1}}\),
so \(\sqrt{x^2-1}\,y'=my\).</p>
<p>Square: \((x^2-1)y'^2=m^2y^2\). Differentiate and divide by \(2y'\):
\((x^2-1)y''+xy'=m^2y\).</p>
<p>(\(-m^2y\) is a sign slip; \(m^2\) drops the factor \(y\).)</p>
<p><b>Answer: \(m^2y\).</b></p>"""),

    # 60 ----------------------------------------------------------------- Applications of Derivatives
    MCQ(src=("maths_2025_26", "12 (OR)"), topic="Applications of Derivatives",
        q=r"""<p>The height of a leaping dolphin above the water, \(t\) seconds after it is first observed, is
\(h(t)=-5t^2+4t+1\) metres (\(t\ge0\)). Its maximum height is</p>""",
        options=[r"\(1\) m", r"\(1.8\) m", r"\(2.6\) m", r"\(0.4\) m"],
        answer=1,
        sol=r"""<p>\(h'(t)=-10t+4=0\Rightarrow t=0.4\) s, and \(h''=-10\lt0\), a maximum.</p>
<p>\(h(0.4)=-5(0.16)+1.6+1=-0.8+1.6+1=1.8\) m.</p>
<p>\(1\) m is the starting height \(h(0)\); \(2.6\) m forgets the \(-5t^2\) term; \(0.4\) is the
time (in s) at which the maximum occurs, not the height.</p>
<p><b>Answer: \(1.8\) m.</b></p>"""),

    # 61 ----------------------------------------------------------------- Applications of Derivatives
    MCQ(src=("maths_2016_17", "5(b)"), topic="Applications of Derivatives",
        q=r"""<p>The sum of the height and the circumference of the base of a right circular cylinder is
\(6\) m. Its maximum possible volume is</p>""",
        options=[r"\(\dfrac{4}{\pi}\) m³", r"\(\dfrac{16}{\pi}\) m³", r"\(8\pi\) m³", r"\(\dfrac{8}{\pi}\) m³"],
        answer=3,
        sol=r"""<p>\(h+2\pi r=6\Rightarrow h=6-2\pi r\); \(V=\pi r^2h=6\pi r^2-2\pi^2r^3\).</p>
<p>\(\dfrac{dV}{dr}=12\pi r-6\pi^2r^2=0\Rightarrow r=\dfrac2\pi\); \(\dfrac{d^2V}{dr^2}=12\pi-12\pi^2r=-12\pi\lt0\).</p>
<p>Then \(h=6-4=2\) and \(V=\pi\cdot\dfrac4{\pi^2}\cdot2=\dfrac8\pi\) m³.</p>
<p><b>Answer: \(\dfrac8\pi\) m³.</b></p>"""),

    # 62 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2015_16", "1(v)"), topic="Integrals",
        q=r"<p>\(\displaystyle\int(1+\log x)\tan^2(x\log x)\,dx\) is equal to</p>",
        options=[r"\(\tan(x\log x)-x\log x+C\)", r"\(\tan(x\log x)+x\log x+C\)",
                 r"\(\sec^2(x\log x)+C\)", r"\(\tan(x\log x)-x+C\)"],
        answer=0,
        sol=r"""<p>Put \(t=x\log x\), \(dt=(1+\log x)\,dx\):
\(\displaystyle\int\tan^2t\,dt=\int(\sec^2t-1)\,dt=\tan t-t+C\).</p>
<p>So the integral is \(\tan(x\log x)-x\log x+C\). The last option integrates the \(-1\) in \(x\)
instead of \(t\).</p><p><b>Answer: \(\tan(x\log x)-x\log x+C\).</b></p>"""),

    # 63 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2016_17", "6(a)"), topic="Integrals",
        q=r"<p>For \(0\lt x\lt\dfrac\pi2\), \(\displaystyle\int\left(\sqrt{\tan x}+\sqrt{\cot x}\right)dx\) is equal to</p>",
        options=[r"\(\sqrt2\sin^{-1}(\sin x+\cos x)+C\)", r"\(\dfrac{1}{\sqrt2}\sin^{-1}(\sin x-\cos x)+C\)",
                 r"\(\sqrt2\sin^{-1}(\sin x-\cos x)+C\)", r"\(\sqrt2\cos^{-1}(\sin x+\cos x)+C\)"],
        answer=2,
        sol=r"""<p>\(\sqrt{\tan x}+\sqrt{\cot x}=\dfrac{\sin x+\cos x}{\sqrt{\sin x\cos x}}\). Put
\(t=\sin x-\cos x\), \(dt=(\cos x+\sin x)\,dx\), and \(t^2=1-2\sin x\cos x\Rightarrow
\sin x\cos x=\dfrac{1-t^2}{2}\).</p>
<p>\(\displaystyle\int\frac{dt}{\sqrt{(1-t^2)/2}}=\sqrt2\int\frac{dt}{\sqrt{1-t^2}}=\sqrt2\sin^{-1}t+C\).</p>
<p>So the integral is \(\sqrt2\sin^{-1}(\sin x-\cos x)+C\). Substituting \(\sin x+\cos x\) instead
gives the wrong \(dt\); \(\tfrac{1}{\sqrt2}\) inverts the constant.</p>
<p><b>Answer: \(\sqrt2\sin^{-1}(\sin x-\cos x)+C\).</b></p>"""),

    # 64 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2025_26", "14 (OR)"), topic="Integrals",
        q=r"<p>\(\displaystyle\int_0^{\pi}\frac{x\sin x}{1+\cos^2x}\,dx\) is equal to</p>",
        options=[r"\(\dfrac{\pi^2}{2}\)", r"\(\dfrac{\pi}{2}\)", r"\(\dfrac{\pi^2}{8}\)", r"\(\dfrac{\pi^2}{4}\)"],
        answer=3,
        sol=r"""<p>With \(x\to\pi-x\): \(I=\displaystyle\int_0^\pi\frac{(\pi-x)\sin x}{1+\cos^2x}dx\). Adding,
\(2I=\pi\displaystyle\int_0^\pi\frac{\sin x}{1+\cos^2x}dx\).</p>
<p>Put \(t=\cos x\): \(\displaystyle\int_0^\pi\frac{\sin x\,dx}{1+\cos^2x}=\int_{-1}^{1}\frac{dt}{1+t^2}=\frac\pi2\).</p>
<p>So \(2I=\dfrac{\pi^2}{2}\) and \(I=\dfrac{\pi^2}{4}\). (\(\tfrac{\pi^2}{2}\) forgets to halve.)</p>
<p><b>Answer: \(\dfrac{\pi^2}{4}\).</b></p>"""),

    # 65 ----------------------------------------------------------------- Application of Integrals
    MCQ(src=("maths_2025_26", "18"), topic="Application of Integrals",
        q=r"""<p>The area bounded by the curve \(y=x(3-x)\), the \(x\)-axis and the lines \(x=0\) and
\(x=4\) is</p>""",
        options=[r"\(\dfrac{19}{3}\)", r"\(\dfrac{8}{3}\)", r"\(\dfrac{9}{2}\)", r"\(\dfrac{11}{3}\)"],
        answer=0,
        sol=r"""<p>The curve is above the axis on \((0,3)\) and below it on \((3,4)\), so split there:</p>
<p>\(\displaystyle\int_0^3(3x-x^2)\,dx=\frac{27}{2}-9=\frac92\), and
\(\displaystyle\Big|\int_3^4(3x-x^2)\,dx\Big|=\Big|\frac{21}{2}-\frac{37}{3}\Big|=\frac{11}{6}\).</p>
<p>Area \(=\dfrac92+\dfrac{11}{6}=\dfrac{19}{3}\) sq. units. \(\tfrac83=\int_0^4\) is the net signed
integral, which subtracts the lower piece.</p><p><b>Answer: \(\dfrac{19}{3}\).</b></p>""",
        sfig=(F.fig_jt3_area, "Area above the axis \\(\\tfrac92\\) plus area below \\(\\tfrac{11}{6}\\).")),

    # 66 ----------------------------------------------------------------- Differential Equations
    MCQ(src=("maths_2013_14", "9(b)"), topic="Differential Equations",
        q=r"<p>The general solution of \(\dfrac{dy}{dx}+\dfrac{y}{2\sqrt x}=\dfrac{e^{-\sqrt x}}{2\sqrt x}\) \((x\gt0)\) is</p>",
        options=[r"\(y\,e^{2\sqrt x}=2\sqrt x+C\)", r"\(y\,e^{\sqrt x}=2\sqrt x+C\)",
                 r"\(y\,e^{-\sqrt x}=\sqrt x+C\)", r"\(y\,e^{\sqrt x}=\sqrt x+C\)"],
        answer=3,
        sol=r"""<p>Linear in \(y\) with \(P=\dfrac{1}{2\sqrt x}\): I.F. \(=e^{\int\frac{dx}{2\sqrt x}}=e^{\sqrt x}\).</p>
<p>\(y\,e^{\sqrt x}=\displaystyle\int\frac{e^{-\sqrt x}}{2\sqrt x}\,e^{\sqrt x}\,dx=\int\frac{dx}{2\sqrt x}=\sqrt x+C\).</p>
<p>\(e^{2\sqrt x}\) is the I.F. when \(P=\tfrac{1}{\sqrt x}\); \(2\sqrt x\) on the right drops the
\(\tfrac12\).</p><p><b>Answer: \(y\,e^{\sqrt x}=\sqrt x+C\).</b></p>"""),

    # 67 ----------------------------------------------------------------- Differential Equations
    MCQ(src=("maths_2024_25_s2", "1(xi)"), topic="Differential Equations",
        q=r"<p>The degree of the differential equation \(a\left(\dfrac{dy}{dx}\right)^2+b\,\dfrac{dx}{dy}=c\) is</p>",
        options=[r"\(2\)", r"\(3\)", r"\(1\)", r"not defined"],
        answer=1,
        sol=r"""<p>\(\dfrac{dx}{dy}=\dfrac{1}{y'}\) is not a polynomial in \(y'\); multiply through by \(y'\):
\(a\,y'^3-c\,y'+b=0\).</p>
<p>Now every term is a polynomial in \(y'\); the highest (and only) derivative is \(y'\) (order 1)
and its highest power is \(3\). So the degree is \(3\).</p>
<p>\(2\) reads the power before clearing \(\tfrac{dx}{dy}\); "not defined" applies only when the
equation cannot be made polynomial in the derivatives (e.g. \(\sin y'\)).</p>
<p><b>Answer: \(3\).</b></p>"""),

    # 68 ----------------------------------------------------------------- Vector Algebra
    MCQ(src=("maths_2025_26", "15(iii)"), topic="Vector Algebra",
        q=r"""<p>The area of the parallelogram whose diagonals are \(3\hat i+\hat j-2\hat k\) and
\(\hat i-3\hat j+4\hat k\) is</p>""",
        options=[r"\(10\sqrt3\)", r"\(\dfrac{5\sqrt3}{2}\)", r"\(5\sqrt3\)", r"\(20\sqrt3\)"],
        answer=2,
        sol=r"""<p>For diagonals \(\vec d_1,\vec d_2\), area \(=\tfrac12|\vec d_1\times\vec d_2|\).</p>
<p>\(\vec d_1\times\vec d_2=\begin{vmatrix}\hat i&\hat j&\hat k\\3&1&-2\\1&-3&4\end{vmatrix}
=-2\hat i-14\hat j-10\hat k\), magnitude \(\sqrt{4+196+100}=10\sqrt3\).</p>
<p>Area \(=5\sqrt3\) sq. units. \(10\sqrt3\) uses the side-vector formula on diagonals.</p>
<p><b>Answer: \(5\sqrt3\).</b></p>"""),

    # 69 ----------------------------------------------------------------- Three-dimensional Geometry
    MCQ(src=("maths_2024_25_s2", "17"), topic="Three-dimensional Geometry",
        q=r"""<p>The equation of the plane containing the line \(\dfrac{x}{2}=\dfrac{y-1}{-1}=\dfrac{z-2}{1}\)
and the point \((1,0,0)\) is</p>""",
        options=[r"\(3x+5y+z=3\)", r"\(3x+5y-z=3\)", r"\(3x-5y-z=3\)", r"\(x+5y-3z=1\)"],
        answer=1,
        sol=r"""<p>The line passes through \(A(0,1,2)\) with direction \(\vec b=2\hat i-\hat j+\hat k\). With
\(P(1,0,0)\), \(\overrightarrow{AP}=\hat i-\hat j-2\hat k\).</p>
<p>Normal \(\vec n=\vec b\times\overrightarrow{AP}=\begin{vmatrix}\hat i&\hat j&\hat k\\2&-1&1\\1&-1&-2\end{vmatrix}=3\hat i+5\hat j-\hat k\).</p>
<p>Plane through \(P\): \(3(x-1)+5y-z=0\), i.e. \(3x+5y-z=3\). Check \(A\): \(0+5-2=3\). ✓
Each other option fails at \(A\) or at \(P\) (e.g. \(3x+5y+z\) gives \(7\) at \(A\)).</p>
<p><b>Answer: \(3x+5y-z=3\).</b></p>"""),

    # 70 ----------------------------------------------------------------- Probability
    MCQ(src=("maths_2015_16", "8(a)"), topic="Probability",
        q=r"""<p>A and B throw a pair of dice alternately, A first; whoever first throws a total of \(9\) wins.
The probability that A wins is</p>""",
        options=[r"\(\dfrac{8}{17}\)", r"\(\dfrac{1}{2}\)", r"\(\dfrac{9}{17}\)", r"\(\dfrac{9}{16}\)"],
        answer=2,
        sol=r"""<p>A total of 9: \((3,6),(4,5),(5,4),(6,3)\), so \(p=\tfrac4{36}=\tfrac19\), \(q=\tfrac89\).</p>
<p>A wins on throws 1, 3, 5, …: \(P(A)=p+q^2p+q^4p+\dots=\dfrac{p}{1-q^2}=\dfrac{1/9}{17/81}=\dfrac{9}{17}\).</p>
<p>\(\tfrac{8}{17}\) is B's chance; \(\tfrac12\) ignores the advantage of going first.</p>
<p><b>Answer: \(\dfrac9{17}\).</b></p>"""),

    # ===================================================================== Section B (integer)
    # 71 ----------------------------------------------------------------- Inverse Trigonometric Functions
    NUM(src=("maths_2024_25_s1", "6"), topic="Inverse Trigonometric Functions",
        q=r"<p>If \(\sin^{-1}\dfrac{5}{x}+\sin^{-1}\dfrac{12}{x}=\dfrac{\pi}{2}\) \((x\gt0)\), then \(x\) is ______.</p>",
        answer=13,
        sol=r"""<p>\(\sin^{-1}\dfrac5x=\dfrac\pi2-\sin^{-1}\dfrac{12}x=\cos^{-1}\dfrac{12}x\). So if
\(\sin\theta=\tfrac5x\) then \(\cos\theta=\tfrac{12}x\), and \(\sin^2\theta+\cos^2\theta=1\):</p>
<p>\(\dfrac{25+144}{x^2}=1\Rightarrow x=13\).</p><p><b>Answer: \(13\).</b></p>"""),

    # 72 ----------------------------------------------------------------- Probability
    NUM(src=("maths_2013_14", "8(a)"), topic="Probability",
        q=r"""<p>A bag contains 3 white, 4 blue and 5 red balls. Three balls are drawn at random together. If
the probability that all three are of the same colour is \(\dfrac{p}{q}\) in lowest terms, then
\(p+q\) is ______.</p>""",
        answer=47,
        sol=r"""<p>Total ways: \(\binom{12}{3}=220\). Same colour:
\(\binom33+\binom43+\binom53=1+4+10=15\).</p>
<p>\(P=\dfrac{15}{220}=\dfrac{3}{44}\), so \(p+q=47\).</p><p><b>Answer: \(47\).</b></p>"""),

    # 73 ----------------------------------------------------------------- Three-dimensional Geometry
    NUM(src=("maths_2024_25_s1", "17"), topic="Three-dimensional Geometry",
        q=r"""<p>The planes \(x-2y+2z=k\) are parallel to \(x-2y+2z=0\) and at a distance of \(4\) units from the
point \((1,2,3)\). The sum of the possible values of \(k\) is ______.</p>""",
        answer=6,
        sol=r"""<p>Distance from \((1,2,3)\) to \(x-2y+2z-k=0\): \(\dfrac{|1-4+6-k|}{\sqrt{1+4+4}}=\dfrac{|3-k|}{3}=4\).</p>
<p>\(|3-k|=12\Rightarrow k=15\) or \(k=-9\); the sum is \(6\).</p><p><b>Answer: \(6\).</b></p>"""),

    # 74 ----------------------------------------------------------------- Linear Programming
    NUM(src=("maths_2015_16", "15(b)"), topic="Linear Programming",
        q=r"""<p>A package of nuts needs 1 hour on machine A and 3 hours on machine B; a package of bolts needs
3 hours on A and 1 hour on B. Each machine can run at most 12 hours a day. The profit is ₹5 per
package of nuts and ₹4 per package of bolts. The maximum daily profit (in ₹) is ______.</p>""",
        answer=27,
        sol=r"""<p>Maximise \(Z=5x+4y\) subject to \(x+3y\le12\) (machine A), \(3x+y\le12\) (machine B),
\(x,y\ge0\).</p>
<p>Corners: \((0,0)\), \((4,0)\), \((3,3)\) (solving the two equalities), \((0,4)\).
\(Z=0,\ 20,\ 27,\ 16\).</p><p>Maximum ₹27 at 3 packages of each. <b>Answer: \(27\).</b></p>""",
        sfig=(F.fig_jt3_lpp, "Feasible region; the optimum is at \\((3,3)\\).")),

    # 75 ----------------------------------------------------------------- Matrices and Determinants
    NUM(src=("maths_2025_26", "11"), topic="Determinants",
        q=r"""<p>A factory makes tables, chairs and cots. Each table needs 2, 1, 3 tonnes of teak, rose and
satin wood; each chair 3, 1, 2; each cot 4, 2, 1. Using exactly 25 t of teak, 12 t of rose and 15 t
of satin wood, the total number of pieces of furniture made is ______.</p>""",
        answer=8,
        sol=r"""<p>With \(x,y,z\) tables, chairs, cots:
\(2x+3y+4z=25,\ x+y+2z=12,\ 3x+2y+z=15\).
\(|A|=\begin{vmatrix}2&3&4\\1&1&2\\3&2&1\end{vmatrix}=2(-3)-3(-5)+4(-1)=5\ne0\).</p>
<p>\(X=A^{-1}B=\tfrac15\begin{bmatrix}-3&5&2\\5&-10&0\\-1&5&-1\end{bmatrix}\begin{bmatrix}25\\12\\15\end{bmatrix}
=\tfrac15\begin{bmatrix}15\\5\\20\end{bmatrix}=\begin{bmatrix}3\\1\\4\end{bmatrix}\).</p>
<p>3 tables, 1 chair, 4 cots: \(3+1+4=8\) pieces. <b>Answer: \(8\).</b></p>"""),
]
