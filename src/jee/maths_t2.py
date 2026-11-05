"""JEE Main mock test 2 — Mathematics (Q51-75).  Every item adapted from a kept pre-board question."""
from jee_kit import MCQ, NUM
import maths_figs as F

SUBJECT = "maths"
TEST = 2

QUESTIONS = [
    # 51 ----------------------------------------------------------------- Relations and Functions
    MCQ(src=("maths_2024_25_s1", "1(xiii)"), topic="Relations and Functions",
        q=r"<p>The relation \(R=\{(c,a)\}\) on the set \(A=\{a,b,c\}\) is</p>",
        options=[r"symmetric but not transitive",
                 r"reflexive and transitive",
                 r"an equivalence relation",
                 r"transitive but neither reflexive nor symmetric"],
        answer=3,
        sol=r"""<p><b>Reflexive?</b> No: \((a,a)\notin R\).</p>
<p><b>Symmetric?</b> No: \((c,a)\in R\) but \((a,c)\notin R\).</p>
<p><b>Transitive?</b> Yes: transitivity needs a chain \((x,y),(y,z)\in R\). The only pair is \((c,a)\),
and there is no pair starting with \(a\), so no chain exists and the condition holds vacuously.</p>
<p>So every option claiming reflexive or symmetric is false.</p>
<p><b>Answer: transitive but neither reflexive nor symmetric.</b></p>"""),

    # 52 ----------------------------------------------------------------- Relations and Functions
    MCQ(src=("maths_2024_25_s2", "4"), topic="Relations and Functions",
        q=r"<p>\(f:\mathbb R\to\mathbb R\), \(f(x)=\dfrac{3x-5}{2}\), is a bijection. Its inverse is \(f^{-1}(x)=\)</p>",
        options=[r"\(\dfrac{2x+5}{3}\)", r"\(\dfrac{2x-5}{3}\)", r"\(\dfrac{2}{3x-5}\)", r"\(\dfrac{3x+5}{2}\)"],
        answer=0,
        sol=r"""<p>\(y=\dfrac{3x-5}{2}\Rightarrow 3x=2y+5\Rightarrow x=\dfrac{2y+5}{3}\). Hence
\(f^{-1}(x)=\dfrac{2x+5}{3}\).</p>
<p>Check: \(f\!\left(\frac{2x+5}{3}\right)=\frac{(2x+5)-5}{2}=x\). \(\tfrac{2}{3x-5}\) is the
reciprocal, not the inverse.</p><p><b>Answer: \(\dfrac{2x+5}{3}\).</b></p>"""),

    # 53 ----------------------------------------------------------------- Inverse Trigonometric Functions
    MCQ(src=("maths_2024_25_s2", "1(iii)"), topic="Inverse Trigonometric Functions",
        q=r"<p>The value of \(\cot\!\left(\dfrac{\pi}{2}+\tan^{-1}\dfrac13\right)\) is</p>",
        options=[r"\(\dfrac13\)", r"\(-3\)", r"\(-\dfrac13\)", r"\(3\)"],
        answer=2,
        sol=r"""<p>\(\cot\left(\tfrac\pi2+\theta\right)=-\tan\theta\). With \(\theta=\tan^{-1}\tfrac13\):
\(-\tan\left(\tan^{-1}\tfrac13\right)=-\tfrac13\).</p>
<p>\(\tfrac13\) misses the sign change in the second quadrant; \(\pm3\) use \(\cot\theta\) instead of
\(\tan\theta\).</p><p><b>Answer: \(-\dfrac13\).</b></p>"""),

    # 54 ----------------------------------------------------------------- Inverse Trigonometric Functions
    MCQ(src=("maths_2025_26", "1(xiii)"), topic="Inverse Trigonometric Functions",
        q=r"<p>The principal value of \(\cos^{-1}\!\left(\sin\dfrac{9\pi}{7}\right)\) is</p>",
        options=[r"\(\dfrac{3\pi}{14}\)", r"\(\dfrac{11\pi}{14}\)", r"\(-\dfrac{3\pi}{14}\)", r"\(\dfrac{9\pi}{7}\)"],
        answer=1,
        sol=r"""<p>\(\sin\dfrac{9\pi}{7}=\sin\left(\pi+\dfrac{2\pi}{7}\right)=-\sin\dfrac{2\pi}7
=-\cos\left(\dfrac\pi2-\dfrac{2\pi}7\right)=-\cos\dfrac{3\pi}{14}\).</p>
<p>\(\cos^{-1}(-u)=\pi-\cos^{-1}u\), so the value is \(\pi-\dfrac{3\pi}{14}=\dfrac{11\pi}{14}\),
which lies in \([0,\pi]\).</p>
<p>\(\tfrac{3\pi}{14}\) drops the minus sign; \(-\tfrac{3\pi}{14}\) and \(\tfrac{9\pi}{7}\) are outside
the principal range \([0,\pi]\).</p><p><b>Answer: \(\dfrac{11\pi}{14}\).</b></p>"""),

    # 55 ----------------------------------------------------------------- Matrices
    MCQ(src=("maths_2015_16", "1(i)"), topic="Matrices",
        q=r"""<p>The matrix \(A=\begin{bmatrix}3&-2\\4&1\end{bmatrix}\) satisfies \(A^2-4A+11I=O\). Hence
\(A^{-1}\) equals</p>""",
        options=[r"\(\dfrac1{11}\begin{bmatrix}3&2\\-4&1\end{bmatrix}\)",
                 r"\(\dfrac1{11}\begin{bmatrix}-1&-2\\4&-3\end{bmatrix}\)",
                 r"\(\dfrac1{11}\begin{bmatrix}1&-2\\4&3\end{bmatrix}\)",
                 r"\(\dfrac1{11}\begin{bmatrix}1&2\\-4&3\end{bmatrix}\)"],
        answer=3,
        sol=r"""<p>Multiply \(A^2-4A+11I=O\) by \(A^{-1}\) (it exists, \(|A|=3+8=11\ne0\)):
\(A-4I+11A^{-1}=O\Rightarrow A^{-1}=\dfrac{1}{11}(4I-A)\).</p>
<p>\(4I-A=\begin{bmatrix}1&2\\-4&3\end{bmatrix}\), so \(A^{-1}=\dfrac1{11}\begin{bmatrix}1&2\\-4&3\end{bmatrix}\)
(the same as \(\tfrac{1}{|A|}\operatorname{adj}A\)).</p>
<p>The second option is \(\tfrac1{11}(A-4I)\), a sign slip.</p>
<p><b>Answer: \(\dfrac1{11}\begin{bmatrix}1&2\\-4&3\end{bmatrix}\).</b></p>"""),

    # 56 ----------------------------------------------------------------- Determinants
    MCQ(src=("maths_2024_25_s2", "1(xii)"), topic="Determinants",
        q=r"""<p>\(A\) is a square matrix of order 3 with \(|A|=2\), and \(C\) is the matrix of cofactors of
\(A\). Then \(|C^2|\) equals</p>""",
        options=[r"\(16\)", r"\(4\)", r"\(64\)", r"\(256\)"],
        answer=0,
        sol=r"""<p>\(C^{T}=\operatorname{adj}A\), so \(|C|=|\operatorname{adj}A|=|A|^{n-1}=2^{2}=4\).</p>
<p>\(|C^2|=|C|^2=16\).</p>
<p>\(4\) is \(|C|\) itself; \(64=4^3\) cubes instead of squaring; \(256=4^4\).</p>
<p><b>Answer: \(16\).</b></p>"""),

    # 57 ----------------------------------------------------------------- Determinants
    MCQ(src=("maths_2024_25_s1", "1(xii)"), topic="Determinants",
        q=r"""<p>The sum of all real \(x\) for which \(\begin{bmatrix}1&2&4\\1&x&x^2\\1&5&25\end{bmatrix}\) is
singular is</p>""",
        options=[r"\(3\)", r"\(10\)", r"\(7\)", r"\(-7\)"],
        answer=2,
        sol=r"""<p>This is a Vandermonde determinant in \(2,x,5\):
\(\begin{vmatrix}1&2&4\\1&x&x^2\\1&5&25\end{vmatrix}=(x-2)(5-2)(5-x)\).</p>
<p>(Directly: \(R_2-R_1,\ R_3-R_1\) give \((x-2)\cdot3\cdot\begin{vmatrix}1&x+2\\1&7\end{vmatrix}=3(x-2)(5-x)\).)</p>
<p>Singular \(\iff x=2\) or \(x=5\); the sum is \(7\).</p><p><b>Answer: \(7\).</b></p>"""),

    # 58 ----------------------------------------------------------------- Continuity and Differentiability
    MCQ(src=("maths_2024_25_s1", "1(viii)"), topic="Continuity and Differentiability",
        q=r"<p>If \(y=\log\sqrt{\tan x}\), then \(\dfrac{dy}{dx}\) at \(x=\dfrac{\pi}{6}\) is</p>",
        options=[r"\(\dfrac{1}{\sqrt3}\)", r"\(\dfrac{2}{\sqrt3}\)", r"\(\dfrac{4}{\sqrt3}\)", r"\(\dfrac{\sqrt3}{2}\)"],
        answer=1,
        sol=r"""<p>\(y=\tfrac12\log\tan x\Rightarrow\dfrac{dy}{dx}=\dfrac12\cdot\dfrac{\sec^2x}{\tan x}
=\dfrac{1}{2\sin x\cos x}=\dfrac{1}{\sin2x}\).</p>
<p>At \(x=\tfrac\pi6\): \(\dfrac{1}{\sin(\pi/3)}=\dfrac{2}{\sqrt3}\).</p>
<p>\(\tfrac4{\sqrt3}\) forgets the \(\tfrac12\) from the square root.</p>
<p><b>Answer: \(\dfrac{2}{\sqrt3}\).</b></p>"""),

    # 59 ----------------------------------------------------------------- Continuity and Differentiability
    MCQ(src=("maths_2024_25_s2", "7 (OR)"), topic="Continuity and Differentiability",
        q=r"""<p>The value of \(k\) for which \(f(x)=\begin{cases}\dfrac{kx}{|x|}, & x\lt0\\ x+2, & x\ge0\end{cases}\)
is continuous at \(x=0\) is</p>""",
        options=[r"\(2\)", r"\(1\)", r"\(-2\)", r"no such \(k\) exists"],
        answer=2,
        sol=r"""<p>For \(x\lt0\), \(|x|=-x\), so \(\dfrac{kx}{|x|}=-k\) and \(\displaystyle\lim_{x\to0^-}f(x)=-k\).</p>
<p>\(f(0)=\lim_{x\to0^+}f(x)=2\). Continuity: \(-k=2\Rightarrow k=-2\).</p>
<p>\(k=2\) treats \(\tfrac{x}{|x|}\) as \(+1\) on the left.</p><p><b>Answer: \(k=-2\).</b></p>"""),

    # 60 ----------------------------------------------------------------- Linear Programming
    MCQ(src=("maths_2025_26", "22 (OR)"), topic="Linear Programming",
        q=r"""<p>The maximum value of \(Z=3x+2y\) subject to \(2x+y\le50\), \(x+2y\le40\), \(x\ge0\),
\(y\ge0\) is</p>""",
        options=[r"\(75\)", r"\(70\)", r"\(80\)", r"\(40\)"],
        answer=2,
        sol=r"""<p>Corner points: \((0,0)\), \((25,0)\), \((20,10)\) (solving \(2x+y=50,\ x+2y=40\)), \((0,20)\).</p>
<p>\(Z=0,\ 75,\ 80,\ 40\). Maximum \(80\) at \((20,10)\).</p>
<p>\(75\) stops at the \(x\)-intercept; \(70\) evaluates \(2x+3y\) at \((20,10)\).</p>
<p><b>Answer: \(80\).</b></p>""",
        sfig=(F.fig_jt2_lpp, "Feasible region; the optimum is at the vertex \\((20,10)\\).")),

    # 61 ----------------------------------------------------------------- Applications of Derivatives
    MCQ(src=("maths_2025_26", "1(xi)"), topic="Applications of Derivatives",
        q=r"<p>The largest interval on which the function \(f(x)=3+2x-e^{x}\) is strictly increasing is</p>",
        options=[r"\((\log2,\infty)\)", r"\((-\infty,\log2)\)", r"\((-\infty,0)\)", r"\((0,\infty)\)"],
        answer=1,
        sol=r"""<p>\(f'(x)=2-e^{x}\gt0\iff e^{x}\lt2\iff x\lt\log2\).</p>
<p>\((\log2,\infty)\) is where \(f\) decreases. \((-\infty,0)\) is an interval on which \(f\) does
increase, but not the largest one — the function is strictly increasing on the whole of
\((-\infty,\log 2)\); \((0,\infty)\) contains points beyond \(\log2\) where \(f\) decreases.</p>
<p><b>Answer: \((-\infty,\log2)\).</b></p>"""),

    # 62 ----------------------------------------------------------------- Applications of Derivatives
    MCQ(src=("maths_2025_26", "2 (OR)"), topic="Applications of Derivatives",
        q=r"<p>\(f(x)=ax+3\cos x+b\) is increasing on \(\mathbb R\) if and only if</p>",
        options=[r"\(a\ge3\)", r"\(a\le-3\)", r"\(a\ge-3\)", r"\(|a|\le3\)"],
        answer=0,
        sol=r"""<p>\(f'(x)=a-3\sin x\). We need \(a-3\sin x\ge0\) for every \(x\), i.e. \(a\ge3\sin x\) for
all \(x\); the largest value of \(3\sin x\) is \(3\), so \(a\ge3\).</p>
<p>(At \(a=3\), \(f'=0\) only at isolated points \(x=\tfrac\pi2+2n\pi\), so \(f\) is still increasing.)
\(a\ge-3\) uses the minimum of \(3\sin x\) instead of the maximum.</p>
<p><b>Answer: \(a\ge3\).</b></p>"""),

    # 63 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2024_25_s2", "9"), topic="Integrals",
        q=r"<p>\(\displaystyle\int x^2\sin x\,dx\) is equal to</p>",
        options=[r"\(-x^2\cos x+2x\sin x-2\cos x+C\)",
                 r"\(x^2\cos x-2x\sin x-2\cos x+C\)",
                 r"\(-x^2\cos x+2x\sin x+2\cos x+C\)",
                 r"\(-x^2\cos x-2x\sin x+2\cos x+C\)"],
        answer=2,
        sol=r"""<p>By parts twice:
\(\int x^2\sin x\,dx=-x^2\cos x+\int2x\cos x\,dx\) and
\(\int2x\cos x\,dx=2x\sin x-\int2\sin x\,dx=2x\sin x+2\cos x\).</p>
<p>So \(\int x^2\sin x\,dx=-x^2\cos x+2x\sin x+2\cos x+C\).</p>
<p>Check by differentiating: \(-2x\cos x+x^2\sin x+2\sin x+2x\cos x-2\sin x=x^2\sin x\). ✓
The other options each carry one sign slip.</p>
<p><b>Answer: \(-x^2\cos x+2x\sin x+2\cos x+C\).</b></p>"""),

    # 64 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2024_25_s1", "5 (OR)"), topic="Integrals",
        q=r"<p>\(\displaystyle\int e^x\,\frac{x^2+1}{(x+1)^2}\,dx\) is equal to</p>",
        options=[r"\(e^x\dfrac{x+1}{x-1}+C\)", r"\(\dfrac{e^x}{(x+1)^2}+C\)",
                 r"\(e^x\dfrac{x-1}{x+1}+C\)", r"\(\dfrac{e^x}{x+1}+C\)"],
        answer=2,
        sol=r"""<p>\(\dfrac{x^2+1}{(x+1)^2}=\dfrac{(x^2-1)+2}{(x+1)^2}=\dfrac{x-1}{x+1}+\dfrac{2}{(x+1)^2}\).</p>
<p>With \(f(x)=\dfrac{x-1}{x+1}\), \(f'(x)=\dfrac{2}{(x+1)^2}\), so the integrand is
\(e^x\{f+f'\}\) and the integral is \(e^xf(x)+C\).</p>
<p><b>Answer: \(e^x\dfrac{x-1}{x+1}+C\).</b></p>"""),

    # 65 ----------------------------------------------------------------- Integrals
    MCQ(src=("maths_2024_25_s2", "13 (OR)"), topic="Integrals",
        q=r"<p>\(\displaystyle\int_0^{\pi/2}\frac{\cos^2x}{1+\sin x\cos x}\,dx\) is equal to</p>",
        options=[r"\(\dfrac{2\pi}{3\sqrt3}\)", r"\(\dfrac{\pi}{3\sqrt3}\)", r"\(\dfrac{\pi}{\sqrt3}\)", r"\(\dfrac{\pi}{4}\)"],
        answer=1,
        sol=r"""<p>By \(x\to\tfrac\pi2-x\), \(I=\int_0^{\pi/2}\frac{\sin^2x}{1+\sin x\cos x}dx\). Adding,
\(2I=\displaystyle\int_0^{\pi/2}\frac{dx}{1+\sin x\cos x}=\int_0^{\pi/2}\frac{\sec^2x\,dx}{\tan^2x+\tan x+1}\).</p>
<p>Put \(t=\tan x\): \(2I=\displaystyle\int_0^\infty\frac{dt}{(t+\frac12)^2+\frac34}
=\frac{2}{\sqrt3}\Big[\tan^{-1}\frac{2t+1}{\sqrt3}\Big]_0^\infty=\frac2{\sqrt3}\Big(\frac\pi2-\frac\pi6\Big)=\frac{2\pi}{3\sqrt3}\).</p>
<p>So \(I=\dfrac{\pi}{3\sqrt3}\). (\(\tfrac{2\pi}{3\sqrt3}\) forgets to halve.)</p>
<p><b>Answer: \(\dfrac{\pi}{3\sqrt3}\).</b></p>"""),

    # 66 ----------------------------------------------------------------- Application of Integrals
    MCQ(src=("maths_2015_16", "6(b)"), topic="Application of Integrals",
        q=r"""<p>The area of the region bounded by the curve \(x=3+2y-y^2\), the \(y\)-axis and the lines
\(y=-1\) and \(y=3\) is</p>""",
        options=[r"\(\dfrac{28}{3}\)", r"\(\dfrac{16}{3}\)", r"\(9\)", r"\(\dfrac{32}{3}\)"],
        answer=3,
        sol=r"""<p>\(x=(3-y)(1+y)\ge0\) for \(-1\le y\le3\), so the curve is to the right of the \(y\)-axis on
the whole range:</p>
<p>\(A=\displaystyle\int_{-1}^{3}(3+2y-y^2)\,dy=\Big[3y+y^2-\frac{y^3}{3}\Big]_{-1}^{3}=9-\Big(-\frac53\Big)=\frac{32}{3}\).</p>
<p><b>Answer: \(\dfrac{32}{3}\) sq. units.</b></p>""",
        sfig=(F.fig_jt2_area, "The region between \\(x=3+2y-y^2\\) and the \\(y\\)-axis.")),

    # 67 ----------------------------------------------------------------- Differential Equations
    MCQ(src=("maths_2024_25_s1", "12"), topic="Differential Equations",
        q=r"""<p>The solution of \(\left[x\sin^2\!\left(\dfrac yx\right)-y\right]dx+x\,dy=0\) with
\(y(1)=\dfrac{\pi}{4}\) is</p>""",
        options=[r"\(\cot\dfrac yx=\log|x|+1\)", r"\(\tan\dfrac yx=\log|x|+1\)",
                 r"\(\cot\dfrac yx=1-\log|x|\)", r"\(\cot\dfrac yx=\log|x|\)"],
        answer=0,
        sol=r"""<p>Homogeneous: \(\dfrac{dy}{dx}=\dfrac{y}{x}-\sin^2\dfrac yx\). Put \(y=vx\):
\(v+x\dfrac{dv}{dx}=v-\sin^2v\Rightarrow-\operatorname{cosec}^2v\,dv=\dfrac{dx}{x}\).</p>
<p>Integrate: \(\cot v=\log|x|+C\), i.e. \(\cot\dfrac yx=\log|x|+C\).</p>
<p>\(x=1,\ y=\tfrac\pi4\): \(\cot\tfrac\pi4=1=C\). So \(\cot\dfrac yx=\log|x|+1\).</p>
<p><b>Answer: \(\cot\dfrac yx=\log|x|+1\).</b></p>"""),

    # 68 ----------------------------------------------------------------- Vector Algebra
    MCQ(src=("maths_2024_25_s2", "15(v)"), topic="Vector Algebra",
        q=r"""<p>\(\vec a\) is a unit vector perpendicular to \(\vec b\), and
\((3\vec a+\vec b)\cdot(\vec a-2\vec b)=-15\). Then \(|\vec b|\) is</p>""",
        options=[r"\(9\)", r"\(\sqrt6\)", r"\(2\)", r"\(3\)"],
        answer=3,
        sol=r"""<p>Expand: \(3|\vec a|^2-6\,\vec a\cdot\vec b+\vec b\cdot\vec a-2|\vec b|^2=3-0-2|\vec b|^2=-15\).</p>
<p>\(|\vec b|^2=9\Rightarrow|\vec b|=3\). (\(9\) is \(|\vec b|^2\).)</p>
<p><b>Answer: \(3\).</b></p>"""),

    # 69 ----------------------------------------------------------------- Three-dimensional Geometry
    MCQ(src=("maths_2015_16", "11(a)"), topic="Three-dimensional Geometry",
        q=r"""<p>The shortest distance between the lines
\(\vec r=(\hat i+2\hat j+\hat k)+\lambda(\hat i-\hat j+\hat k)\) and
\(\vec r=(2\hat i+\hat j-\hat k)+\mu(2\hat i+\hat j+\hat k)\) is</p>""",
        options=[r"\(\dfrac{11}{\sqrt{14}}\)", r"\(\dfrac{9}{\sqrt{14}}\)", r"\(\dfrac{3}{\sqrt{14}}\)", r"\(\dfrac{9}{\sqrt6}\)"],
        answer=1,
        sol=r"""<p>\(\vec b_1\times\vec b_2=\begin{vmatrix}\hat i&\hat j&\hat k\\1&-1&1\\2&1&1\end{vmatrix}=-2\hat i+\hat j+3\hat k\),
magnitude \(\sqrt{14}\).</p>
<p>\(\vec a_2-\vec a_1=\hat i-\hat j-2\hat k\); \((\vec a_2-\vec a_1)\cdot(\vec b_1\times\vec b_2)=-2-1-6=-9\).</p>
<p>\(d=\dfrac{|-9|}{\sqrt{14}}=\dfrac{9}{\sqrt{14}}\).</p>
<p>\(\tfrac{9}{\sqrt6}\) divides by \(|\vec b_2|\) instead of \(|\vec b_1\times\vec b_2|\).</p>
<p><b>Answer: \(\dfrac{9}{\sqrt{14}}\).</b></p>"""),

    # 70 ----------------------------------------------------------------- Probability
    MCQ(src=("maths_2024_25_s1", "10 (OR)"), topic="Probability",
        q=r"""<p>In each match of a three-match series, independently, a team wins with probability \(0.6\),
loses with probability \(0.3\) and draws with probability \(0.1\). The probability that it wins at
least two matches and loses none is</p>""",
        options=[r"\(0.324\)", r"\(0.648\)", r"\(0.216\)", r"\(0.432\)"],
        answer=0,
        sol=r"""<p>"At least two wins, no loss" means WWW, or two wins and one draw (3 orders):</p>
<p>\(P=0.6^3+3(0.6)^2(0.1)=0.216+0.108=0.324\).</p>
<p>\(0.648\) uses \(0.4\) (not-win) for the third match, which lets a loss in; \(0.216\) counts only
WWW.</p><p><b>Answer: \(0.324\).</b></p>"""),

    # ===================================================================== Section B (integer)
    # 71 ----------------------------------------------------------------- Probability
    NUM(src=("maths_2025_26", "13"), topic="Probability",
        q=r"""<p>Three teachers independently set a surprise test on a given day with probabilities
\(0.9,\ 0.7\) and \(0.4\). If \(X\) is the number of tests on that day, then \(100\operatorname{Var}(X)\)
is ______.</p>""",
        answer=54,
        sol=r"""<p>\(X=X_1+X_2+X_3\) with independent indicator variables, so
\(\operatorname{Var}(X)=\sum p_i(1-p_i)=0.9(0.1)+0.7(0.3)+0.4(0.6)=0.09+0.21+0.24=0.54\).</p>
<p>(Equivalently from the distribution: \(E(X)=2\), \(E(X^2)=4.54\).) \(100\operatorname{Var}(X)=54\).</p>
<p><b>Answer: \(54\).</b></p>"""),

    # 72 ----------------------------------------------------------------- Applications of Derivatives
    NUM(src=("maths_2024_25_s1", "13 (OR)"), topic="Applications of Derivatives",
        q=r"""<p>A closed right circular can has volume \(128\pi\) cm³. If its total surface area \(S\) is
the least possible, then \(S/\pi\) (in cm²) is ______.</p>""",
        answer=96,
        sol=r"""<p>\(\pi r^2h=128\pi\Rightarrow h=\dfrac{128}{r^2}\); \(S=2\pi r^2+2\pi rh=2\pi r^2+\dfrac{256\pi}{r}\).</p>
<p>\(\dfrac{dS}{dr}=4\pi r-\dfrac{256\pi}{r^2}=0\Rightarrow r^3=64\Rightarrow r=4\), \(h=8\) (\(h=2r\));
\(\dfrac{d^2S}{dr^2}=4\pi+\dfrac{512\pi}{r^3}\gt0\), a minimum.</p>
<p>\(S=32\pi+64\pi=96\pi\), so \(S/\pi=96\).</p><p><b>Answer: \(96\).</b></p>"""),

    # 73 ----------------------------------------------------------------- Vector Algebra
    NUM(src=("maths_2025_26", "16"), topic="Vector Algebra",
        q=r"""<p>If \(\Delta\) is the area of the triangle with vertices \(A(1,1,1)\), \(B(1,2,3)\) and
\(C(2,3,1)\), then \(4\Delta^2\) is ______.</p>""",
        answer=21,
        sol=r"""<p>\(\overrightarrow{AB}=\hat j+2\hat k\), \(\overrightarrow{AC}=\hat i+2\hat j\).
\(\overrightarrow{AB}\times\overrightarrow{AC}=\begin{vmatrix}\hat i&\hat j&\hat k\\0&1&2\\1&2&0\end{vmatrix}=-4\hat i+2\hat j-\hat k\),
magnitude \(\sqrt{21}\).</p>
<p>\(\Delta=\tfrac12\sqrt{21}\Rightarrow4\Delta^2=21\).</p><p><b>Answer: \(21\).</b></p>"""),

    # 74 ----------------------------------------------------------------- Application of Integrals
    NUM(src=("maths_2024_25_s2", "18"), topic="Application of Integrals",
        q=r"""<p>The area enclosed between the curves \(y=ax^2\) and \(x=ay^2\) \((a\gt0)\) is \(12\) sq. units.
Then \(\dfrac1a\) is ______.</p>""",
        answer=6,
        sol=r"""<p>The curves meet at \(O\) and at \(\left(\tfrac1a,\tfrac1a\right)\). Between them
\(\sqrt{x/a}\ge ax^2\):</p>
<p>\(A=\displaystyle\int_0^{1/a}\Big(\sqrt{\tfrac{x}{a}}-ax^2\Big)dx=\frac{2}{3a^2}-\frac{1}{3a^2}=\frac{1}{3a^2}\).</p>
<p>\(\dfrac{1}{3a^2}=12\Rightarrow a^2=\dfrac1{36}\Rightarrow a=\dfrac16\), so \(\dfrac1a=6\).</p>
<p><b>Answer: \(6\).</b></p>"""),

    # 75 ----------------------------------------------------------------- Differential Equations
    NUM(src=("maths_2016_17", "9(b)"), topic="Differential Equations",
        q=r"""<p>The curve \(y=y(x)\) with \(y\gt0\) satisfies \((x^2-y^2)\,dx+2xy\,dy=0\) and passes through
\((2,4)\). Then \(y(5)\) is ______.</p>""",
        answer=5,
        sol=r"""<p>Homogeneous: \(\dfrac{dy}{dx}=\dfrac{y^2-x^2}{2xy}\). With \(y=vx\):
\(x\dfrac{dv}{dx}=-\dfrac{1+v^2}{2v}\Rightarrow\dfrac{2v\,dv}{1+v^2}=-\dfrac{dx}{x}\Rightarrow
\log(1+v^2)=-\log|x|+c\).</p>
<p>So \(x(1+v^2)=C\), i.e. \(x^2+y^2=Cx\). Through \((2,4)\): \(20=2C\Rightarrow C=10\).</p>
<p>At \(x=5\): \(25+y^2=50\Rightarrow y=5\) (taking \(y\gt0\)).</p><p><b>Answer: \(5\).</b></p>"""),
]
