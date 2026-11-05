"""JEE Main mock test 3 — Physics (Q1-25).  Every item adapted from a kept pre-board question.

Options are written correct-first and placed by `_mcq(..., k=…)` so that the correct one lands at
index k; solutions never refer to an option by letter.
"""
from jee_kit import MCQ, NUM
import physics_figs as F
from physics_2013_14_figs import fig_q2b_caps

SUBJECT = "physics"
TEST = 3

ES = "Electrostatics"
CE = "Current Electricity"
MAG = "Magnetic Effects of Current and Magnetism"
EMI = "Electromagnetic Induction and Alternating Currents"
EMW = "Electromagnetic Waves"
RAY = "Optics — Ray Optics and Optical Instruments"
WAVE = "Optics — Wave Optics"
DUAL = "Dual Nature of Radiation and Matter"
ATOM = "Atoms and Nuclei — Atoms"
NUC = "Atoms and Nuclei — Nuclei"
SEMI = "Electronic Devices"


def _mcq(src, topic, q, opts, k, sol, **kw):
    """opts[0] is the correct option; it is placed at index k."""
    rest = list(opts[1:])
    rest.insert(k, opts[0])
    return MCQ(src=src, topic=topic, q=q, options=rest, answer=k, sol=sol, **kw)


QUESTIONS = [
    # 1 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2025_26", "3"), ES,
         r"""<p>\(n\) identical capacitors, each of capacitance \(C\), are first connected in parallel
and then in series, each time across the same source of voltage \(V\). The ratio of the energy
stored in the parallel arrangement to that in the series arrangement is</p>""",
         [r"\(n^2\)", r"\(n\)", r"\(1\)", r"\(1/n^2\)"], 2,
         r"""<p>Parallel: \(C_p = nC\); series: \(C_s = C/n\).</p>
<p>Same \(V\): \(U = \tfrac12C_{\text{eq}}V^2\), so \(\dfrac{U_p}{U_s} = \dfrac{nC}{C/n} = n^2\).</p>
<p>\(n\) compares only one of the two capacitances with \(C\); \(1\) assumes the energy depends only
on \(V\); \(1/n^2\) is the ratio upside-down.</p>
<p><b>Answer: \(n^2\).</b></p>"""),

    # 2 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2015_16", "1(B)(iii)"), ES,
         r"""<p>Capacitors of \(2\ \mu\)F and \(6\ \mu\)F are connected in series across a 160 V supply.
The potential difference across the \(2\ \mu\)F capacitor is</p>""",
         [r"\(120\) V", r"\(40\) V", r"\(80\) V", r"\(160\) V"], 3,
         r"""<p>\(C_s = \dfrac{2\times6}{2+6} = 1.5\ \mu\)F; \(Q = 1.5\times160 = 240\ \mu\)C, the same on
each capacitor in series.</p>
<p>\(V_2 = \dfrac{Q}{C} = \dfrac{240}{2} = 120\) V (and 40 V across the \(6\ \mu\)F).</p>
<p>\(40\) V is the p.d. across the \(6\ \mu\)F (dividing in proportion to \(C\) instead of
\(1/C\)); \(80\) V splits the supply equally; \(160\) V treats the capacitors as in parallel.</p>
<p><b>Answer: \(120\) V.</b></p>"""),

    # 3 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2014_15", "2(a)"), ES,
         r"""<p>An electric dipole of moment \(2\times10^{-8}\) C m is in equilibrium (aligned) in a
uniform electric field of \(5\times10^{3}\) N C\(^{-1}\). The work needed to rotate it through
\(120^\circ\) is</p>""",
         [r"\(1.5\times10^{-4}\) J", r"\(0.5\times10^{-4}\) J", r"\(0.87\times10^{-4}\) J",
          r"\(2.0\times10^{-4}\) J"], 0,
         r"""<p>\(W = \displaystyle\int_0^{\theta}pE\sin\theta\,d\theta = pE(1 - \cos\theta)\), with
\(pE = 2\times10^{-8}\times5\times10^{3} = 10^{-4}\) J.</p>
<p>\(W = 10^{-4}(1 - \cos120^\circ) = 10^{-4}(1 + 0.5) = 1.5\times10^{-4}\) J.</p>
<p>\(0.5\times10^{-4}\) J takes \(\cos120^\circ = +0.5\); \(0.87\times10^{-4}\) J uses
\(pE\sin\theta\) (that is the torque, in N m); \(2.0\times10^{-4}\) J is the work for \(180^\circ\).</p>
<p><b>Answer: \(1.5\times10^{-4}\) J.</b></p>"""),

    # 4 ------------------------------------------------------------------ Current Electricity
    _mcq(("physics_2015_16", "1(B)(vi)"), CE,
         r"""<p>Resistors of 6 Ω and 9 Ω are connected in parallel, and a total current of 5 A enters the
combination. The current through the 9 Ω resistor is</p>""",
         [r"\(2\) A", r"\(3\) A", r"\(2.5\) A", r"\(5\) A"], 1,
         r"""<p>Same p.d. across both: \(I\propto1/R\), so the current divides in the ratio
\(I_6 : I_9 = 9 : 6 = 3 : 2\).</p>
<p>\(I_9 = 5\times\dfrac{6}{6+9} = 2\) A (and 3 A through the 6 Ω).</p>
<p>\(3\) A is the current in the 6 Ω resistor (or dividing in proportion to \(R\)); \(2.5\) A splits
equally; \(5\) A forgets the division.</p>
<p><b>Answer: \(2\) A.</b></p>"""),

    # 5 ------------------------------------------------------------------ Current Electricity
    _mcq(("physics_2016_17", "1(A)(ii)"), CE,
         r"""<p>A metallic resistor connected to a battery warms up as current flows. Which of the
following does <i>not</i> change as it heats up?</p>""",
         [r"the number density of free electrons", r"the drift speed of the electrons",
          r"the resistivity", r"the resistance"], 2,
         r"""<p>In a metal the number of free electrons per unit volume is fixed by the material
(one or two per atom) and is practically independent of temperature.</p>
<p>Heating makes the ions vibrate more, so collisions are more frequent and the relaxation time
\(\tau\) falls: resistivity \(\rho = \dfrac{m}{ne^2\tau}\) rises, so the resistance rises, the current
falls and the drift speed \(v_d = \dfrac{eE}{m}\tau\) falls. All three of those options change.</p>
<p><b>Answer: the number density of free electrons.</b></p>"""),

    # 6 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2016_17", "1(B)(iv)"), MAG,
         r"""<p>An electron and a proton, each starting from rest, are accelerated through the same
potential difference and then enter a uniform magnetic field at right angles to it. The ratio of
the radii of their paths, \(r_e : r_p\), is</p>""",
         [r"\(\sqrt{m_e/m_p}\)", r"\(m_e/m_p\)", r"\(1\)", r"\(\sqrt{m_p/m_e}\)"], 3,
         r"""<p>After acceleration \(K = eV\) for both, so \(p = \sqrt{2meV}\).</p>
<p>\(r = \dfrac{p}{eB} = \dfrac{\sqrt{2meV}}{eB}\propto\sqrt m\) (same \(|q|\)), hence
\(\dfrac{r_e}{r_p} = \sqrt{\dfrac{m_e}{m_p}}\approx\dfrac{1}{43}\).</p>
<p>\(m_e/m_p\) is the answer for equal speeds; \(1\) is the answer for equal momenta; \(\sqrt{m_p/m_e}\)
inverts the ratio — the lighter electron curves more tightly, not less.</p>
<p><b>Answer: \(\sqrt{m_e/m_p}\).</b></p>"""),

    # 7 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2013_14", "1(B)(ii)"), MAG,
         r"""<p>For a short bar magnet, the magnetic field at a distance \(d\) on its axis is \(B_1\) and at
a distance \(2d\) on its equatorial line is \(B_2\). The ratio \(B_1/B_2\) is</p>""",
         [r"\(16\)", r"\(4\)", r"\(2\)", r"\(8\)"], 0,
         r"""<p>\(B_{\text{axial}} = \dfrac{\mu_0}{4\pi}\dfrac{2m}{r^3}\), \(B_{\text{equatorial}} = \dfrac{\mu_0}{4\pi}\dfrac{m}{r^3}\).</p>
<p>\(\dfrac{B_1}{B_2} = \dfrac{2m/d^3}{m/(2d)^3} = 2\times8 = 16\).</p>
<p>\(2\) compares the two at the same distance; \(8\) forgets the factor 2 of the axial field;
\(4\) uses an inverse-square law and also drops the factor 2 of the axial field.</p>
<p><b>Answer: \(16\).</b></p>"""),

    # 8 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2024_25", "19(b)"), MAG,
         r"""<p>A galvanometer of resistance 45 Ω has 30 divisions on its scale and deflects 5 divisions
per mA (figure of merit 0.2 mA per division). A shunt of 5 Ω is connected across it. The maximum current
the combination can now measure is</p>""",
         [r"\(60\) mA", r"\(54\) mA", r"\(6.7\) mA", r"\(150\) mA"], 2,
         r"""<p>Full-scale current of the galvanometer \(I_g = \dfrac{30}{5} = 6\) mA.</p>
<p>Shunt: \(I_gG = (I - I_g)S\Rightarrow I = I_g\left(1 + \dfrac{G}{S}\right) = 6\left(1 + \dfrac{45}{5}\right)
= 60\) mA.</p>
<p>\(54\) mA is the current through the shunt only; \(6.7\) mA uses \(1 + S/G\); \(150\) mA multiplies
the 30 divisions by 5 divisions per mA instead of dividing.</p>
<p><b>Answer: \(60\) mA.</b></p>"""),

    # 9 ------------------------------------------------------------------ AC
    _mcq(("physics_2014_15", "7(b)"), EMI,
         r"""<p>A series circuit of \(R = 100\ \Omega\), \(L = \dfrac{2}{\pi}\) H and
\(C = \dfrac{100}{\pi}\ \mu\)F is connected to a 50 Hz a.c. source. The current</p>""",
         [r"lags the applied emf by \(45^\circ\)", r"leads the applied emf by \(45^\circ\)",
          r"lags the applied emf by \(63.4^\circ\)", r"is in phase with the applied emf"], 1,
         r"""<p>\(X_L = 2\pi fL = 2\pi\times50\times\dfrac2\pi = 200\ \Omega\);
\(X_C = \dfrac{1}{2\pi fC} = \dfrac{1}{2\pi\times50\times10^{-4}/\pi} = 100\ \Omega\).</p>
<p>\(\tan\varphi = \dfrac{X_L - X_C}{R} = \dfrac{100}{100} = 1\Rightarrow\varphi = 45^\circ\); since
\(X_L \gt X_C\) the circuit is inductive and the current lags.</p>
<p>"Leads" would need \(X_C \gt X_L\); \(63.4^\circ = \tan^{-1}(X_L/R)\) ignores the capacitor;
"in phase" would need \(X_L = X_C\) (resonance).</p>
<p><b>Answer: lags the applied emf by \(45^\circ\).</b></p>"""),

    # 10 ----------------------------------------------------------------- AC
    _mcq(("physics_2013_14", "1(B)(iv)"), EMI,
         r"""<p>An alternating current \(i = 5\sqrt2\,\sin(100\pi t + \pi/6)\) A flows through a
20 Ω resistor. The average power dissipated is</p>""",
         [r"\(500\) W", r"\(1000\) W", r"\(250\) W", r"\(433\) W"], 3,
         r"""<p>\(I_{\text{rms}} = \dfrac{I_0}{\sqrt2} = \dfrac{5\sqrt2}{\sqrt2} = 5\) A.</p>
<p>For a pure resistor \(P = I_{\text{rms}}^2R = 25\times20 = 500\) W. The phase constant \(\pi/6\)
only fixes where the cycle starts; it has nothing to do with a power factor.</p>
<p>\(1000\) W uses the peak current; \(250\) W divides by 2 again; \(433\) W multiplies by
\(\cos30^\circ\), misusing the phase constant as a power factor.</p>
<p><b>Answer: \(500\) W.</b></p>"""),

    # 11 ----------------------------------------------------------------- EM waves
    _mcq(("physics_2025_26", "8"), EMW,
         r"""<p>Welders wear special dark glass goggles or face shields mainly to protect the eyes from
the intense</p>""",
         [r"ultraviolet radiation from the arc", r"infrared radiation from the arc",
          r"X-rays produced at the arc", r"microwaves produced at the arc"], 0,
         r"""<p>An electric welding arc is at several thousand kelvin and emits strongly in the
ultraviolet (besides very bright visible light). UV damages the cornea and the skin ("arc eye"), and
the special glass absorbs it.</p>
<p>The arc does emit infrared (heat), but that is not the radiation the goggles are designed against
— infrared trapping is what a greenhouse glass does. A welding arc has far too little energy per
electron to produce X-rays, and microwaves are not emitted by hot sources in significant amount.</p>
<p><b>Answer: ultraviolet radiation from the arc.</b></p>"""),

    # 12 ----------------------------------------------------------------- Ray optics
    _mcq(("physics_2014_15", "8(a)"), RAY,
         r"""<p>A thin glass prism \((\mu = 1.5)\) is immersed in a liquid of refractive index 1.25. The
ratio of its deviation in the liquid to its deviation in air is</p>""",
         [r"\(2/5\)", r"\(1/4\)", r"\(5/6\)", r"\(1/2\)"], 1,
         r"""<p>Thin prism: \(\delta = (\mu_{\text{rel}} - 1)A\).</p>
<p>In air \(\delta_a = (1.5 - 1)A = 0.5A\). In the liquid \(\mu_{\text{rel}} = \dfrac{1.5}{1.25} = 1.2\),
so \(\delta_l = 0.2A\).</p>
<p>\(\dfrac{\delta_l}{\delta_a} = \dfrac{0.2}{0.5} = \dfrac25\).</p>
<p>\(1/4\) is the familiar result for water (\(\mu = 4/3\)), not for this liquid; \(5/6\) is
\(1.25/1.5\); \(1/2\) is the deviation in air divided by \(A\).</p>
<p><b>Answer: \(2/5\).</b></p>"""),

    # 13 ----------------------------------------------------------------- Ray optics
    _mcq(("physics_2025_26", "18(a)"), RAY,
         r"""<p>A thin convex lens of focal length 20 cm is placed in contact with a thin concave lens of
focal length 30 cm. The combination behaves as a</p>""",
         [r"converging lens of focal length \(60\) cm", r"diverging lens of focal length \(60\) cm",
          r"converging lens of focal length \(12\) cm", r"diverging lens of focal length \(10\) cm"], 2,
         r"""<p>\(\dfrac1F = \dfrac1{f_1} + \dfrac1{f_2} = \dfrac1{20} + \dfrac1{-30} = \dfrac{3-2}{60} = \dfrac1{60}\)
\(\Rightarrow F = +60\) cm: converging (power \(+1.67\) D).</p>
<p>A diverging result would need the concave lens to be the stronger one; \(12\) cm is
\(\dfrac{f_1f_2}{f_1+f_2}\) with both focal lengths taken positive; \(10\) cm adds the focal lengths
instead of the powers.</p>
<p><b>Answer: converging lens of focal length \(60\) cm.</b></p>"""),

    # 14 ----------------------------------------------------------------- Wave optics
    _mcq(("physics_2016_17", "1(B)(x)"), WAVE,
         r"""<p>In a Young's double-slit experiment in air the angular width of a fringe is \(0.20^\circ\).
The whole apparatus is immersed in water \((\mu = 4/3)\). The angular fringe width becomes</p>""",
         [r"\(0.15^\circ\)", r"\(0.27^\circ\)", r"\(0.20^\circ\)", r"\(0.10^\circ\)"], 3,
         r"""<p>Angular fringe width \(\theta = \dfrac{\lambda}{d}\). In water the wavelength becomes
\(\lambda/\mu\), so \(\theta' = \dfrac{\theta}{\mu} = \dfrac{0.20^\circ}{4/3} = 0.15^\circ\).</p>
<p>\(0.27^\circ\) multiplies by \(\mu\); \(0.20^\circ\) ignores the change in wavelength;
\(0.10^\circ\) halves it.</p>
<p><b>Answer: \(0.15^\circ\).</b></p>"""),

    # 15 ----------------------------------------------------------------- Wave optics
    _mcq(("physics_2015_16", "9(b)"), WAVE,
         r"""<p>Light of wavelength 500 nm is diffracted by a single slit of width \(1.0\ \mu\)m. The
angular width of the central maximum is</p>""",
         [r"\(60^\circ\)", r"\(30^\circ\)", r"\(57.3^\circ\)", r"\(120^\circ\)"], 0,
         r"""<p>First minima at \(\sin\theta = \dfrac{\lambda}{a} = \dfrac{500\times10^{-9}}{1.0\times10^{-6}} = 0.5
\Rightarrow\theta = 30^\circ\) on each side.</p>
<p>Angular width of the central maximum \(= 2\theta = 60^\circ\).</p>
<p>\(30^\circ\) is the half-width; \(57.3^\circ\) uses the small-angle form \(2\lambda/a = 1\) rad,
which is not valid when \(\lambda/a = 0.5\); \(120^\circ\) doubles twice.</p>
<p><b>Answer: \(60^\circ\).</b></p>"""),

    # 16 ----------------------------------------------------------------- Dual nature
    _mcq(("physics_2015_16", "1(B)(xii)"), DUAL,
         r"""<p>A particle dropped from rest from a height \(H\) has de Broglie wavelength \(\lambda\) just
before hitting the ground. If it is dropped from a height \(4H\) instead (air resistance neglected),
the de Broglie wavelength just before impact is</p>""",
         [r"\(\lambda/2\)", r"\(\lambda/4\)", r"\(2\lambda\)", r"\(\lambda/\sqrt2\)"], 1,
         r"""<p>\(v = \sqrt{2gH}\Rightarrow\lambda = \dfrac{h}{mv} = \dfrac{h}{m\sqrt{2gH}}\propto\dfrac{1}{\sqrt H}\).</p>
<p>Height ×4 ⇒ \(\lambda' = \lambda/\sqrt4 = \lambda/2\).</p>
<p>\(\lambda/4\) uses \(\lambda\propto1/H\); \(2\lambda\) has the dependence inverted;
\(\lambda/\sqrt2\) is the result for a height of \(2H\), not \(4H\).</p>
<p><b>Answer: \(\lambda/2\).</b></p>"""),

    # 17 ----------------------------------------------------------------- Dual nature
    _mcq(("physics_2024_25", "7"), DUAL,
         r"""<p>Light of wavelength 248 nm falls on a metal surface; the photocurrent stops when the
collector is at \(-1.3\) V with respect to the emitter. The work function of the metal is
(\(hc = 1240\) eV nm)</p>""",
         [r"\(3.7\) eV", r"\(6.3\) eV", r"\(5.0\) eV", r"\(1.3\) eV"], 2,
         r"""<p>\(E = \dfrac{1240}{248} = 5.0\) eV; stopping potential 1.3 V ⇒ \(K_{\max} = 1.3\) eV.</p>
<p>\(\phi_0 = E - K_{\max} = 5.0 - 1.3 = 3.7\) eV.</p>
<p>\(6.3\) eV adds instead of subtracting; \(5.0\) eV is the photon energy; \(1.3\) eV is the
maximum kinetic energy.</p>
<p><b>Answer: \(3.7\) eV.</b></p>"""),

    # 18 ----------------------------------------------------------------- Nuclei
    _mcq(("physics_2013_14", "9(c)"), NUC,
         r"""<p>An electron and a positron, both essentially at rest, annihilate to produce two
identical \(\gamma\)-ray photons. The wavelength of each photon is
(\(m_ec^2 = 0.511\) MeV, \(hc = 1240\) eV nm)</p>""",
         [r"\(2.43\) pm", r"\(1.21\) pm", r"\(4.85\) pm", r"\(24.3\) pm"], 3,
         r"""<p>Total energy \(2m_ec^2 = 1.022\) MeV is shared equally by two photons (momentum
conservation), so each has \(E = 0.511\) MeV.</p>
<p>\(\lambda = \dfrac{hc}{E} = \dfrac{1240\ \text{eV nm}}{5.11\times10^{5}\ \text{eV}} = 2.43\times10^{-3}\) nm
\(= 2.43\) pm.</p>
<p>\(1.21\) pm gives each photon the full 1.022 MeV; \(4.85\) pm gives each only half of
0.511 MeV; \(24.3\) pm slips a power of ten.</p>
<p><b>Answer: \(2.43\) pm.</b></p>"""),

    # 19 ----------------------------------------------------------------- Semiconductors
    _mcq(("physics_2024_25", "1(B)(v)"), SEMI,
         r"""<p>To make a p-type semiconductor from pure germanium, the impurity to be added is</p>""",
         [r"indium", r"arsenic", r"phosphorus", r"antimony"], 1,
         r"""<p>p-type needs an acceptor: a trivalent (group 13) atom, which leaves one bond short of an
electron — a hole. Indium is trivalent.</p>
<p>Arsenic, phosphorus and antimony are all pentavalent (group 15) donors and would make the
germanium n-type.</p>
<p><b>Answer: indium.</b></p>"""),

    # 20 ----------------------------------------------------------------- Semiconductors
    _mcq(("physics_2014_15", "14(a)"), SEMI,
         r"""<p>A centre-tap full-wave rectifier using two junction diodes is fed from a 50 Hz supply.
Which statement is correct?</p>""",
         [r"Each diode conducts in alternate half-cycles and the output pulses at 100 Hz",
          r"Both diodes conduct together in every half-cycle and the output pulses at 100 Hz",
          r"Each diode conducts in alternate half-cycles and the output pulses at 50 Hz",
          r"Each diode conducts for the whole cycle and the output pulses at 50 Hz"], 2,
         r"""<p>The two ends of the secondary are in antiphase about the centre tap. In one half-cycle
one diode is forward biased and the other reverse biased; in the next half-cycle the roles swap.
Both send current the same way through the load, so there is one output pulse per half-cycle:
100 pulses per second.</p>
<p>The diodes never conduct together (one is always reverse biased); a 50 Hz output is the
half-wave result; a diode conducts only while forward biased, i.e. for half of each cycle.</p>
<p><b>Answer: each diode conducts in alternate half-cycles and the output pulses at 100 Hz.</b></p>"""),

    # ===================================================================== Section B (integer)
    # 21 ----------------------------------------------------------------- Electrostatics
    NUM(src=("physics_2013_14", "2(b)"), topic=ES,
        q=r"""<p>Three capacitors \(C_1 = 8\ \mu\)F, \(C_2 = 16\ \mu\)F and \(C_3 = 24\ \mu\)F are
connected in series across a 110 V battery, as shown. Find the potential difference across \(C_3\),
in volt.</p>""",
        answer=20,
        sol=r"""<p>\(\dfrac1{C} = \dfrac18 + \dfrac1{16} + \dfrac1{24} = \dfrac{6+3+2}{48} = \dfrac{11}{48}\)
\(\Rightarrow C = \dfrac{48}{11}\ \mu\)F.</p>
<p>\(Q = CV = \dfrac{48}{11}\times110 = 480\ \mu\)C, the same on every capacitor in series.</p>
<p>\(V_3 = \dfrac{Q}{C_3} = \dfrac{480}{24} = 20\) V (check: \(60 + 30 + 20 = 110\) V).</p>
<p><b>Answer: 20</b></p>""",
        qfig=fig_q2b_caps),

    # 22 ----------------------------------------------------------------- Current Electricity
    NUM(src=("physics_2014_15", "1(B)(v)"), topic=CE,
        q=r"""<p>The charge passing through a cross-section of a conductor varies with time as
\(q = 4t^2 + 3t + 2\), where \(q\) is in coulomb and \(t\) in second. Find the current, in ampere,
at \(t = 2.5\) s.</p>""",
        answer=23,
        sol=r"""<p>\(I = \dfrac{dq}{dt} = 8t + 3\).</p>
<p>At \(t = 2.5\) s: \(I = 20 + 3 = 23\) A. (Not \(q/t\), which would give an average current.)</p>
<p><b>Answer: 23</b></p>"""),

    # 23 ----------------------------------------------------------------- EMI
    NUM(src=("physics_2025_26", "15"), topic=EMI,
        q=r"""<p>Two parallel conducting rails AB and CD, 0.5 m apart, are joined at one end by a resistance
\(R = 4\ \Omega\). A uniform magnetic field of 0.2 T acts perpendicular to the plane of the rails,
into the page. A wire MN laid across the rails slides along them at 10 m s\(^{-1}\). Neglecting the
resistance of the rails and the wire, find the current through \(R\), in milliampere.</p>""",
        answer=250,
        sol=r"""<p>Motional emf \(\varepsilon = Blv = 0.2\times0.5\times10 = 1.0\) V.</p>
<p>\(I = \dfrac{\varepsilon}{R} = \dfrac{1.0}{4} = 0.25\) A \(= 250\) mA.</p>
<p>(Direction: the enclosed area and the inward flux grow, so by Lenz's law the induced current
circulates anticlockwise, from N to M in the moving wire.)</p>
<p><b>Answer: 250</b></p>""",
        qfig=F.fig_jp_t3_rails),

    # 24 ----------------------------------------------------------------- Ray optics
    NUM(src=("physics_2015_16", "10(b)"), topic=RAY,
        q=r"""<p>A point object is placed on the axis 15 cm in front of a convex lens of focal length
10 cm. A convex mirror is placed coaxially on the other side, 20 cm from the lens, and the final
image is found to coincide with the object. Find the focal length of the convex mirror, in cm.</p>""",
        answer=5,
        sol=r"""<p>Lens alone: \(\dfrac1v = \dfrac1f + \dfrac1u = \dfrac1{10} - \dfrac1{15} = \dfrac1{30}\Rightarrow v = 30\) cm.</p>
<p>The rays converge towards a point 30 cm from the lens, i.e. \(30 - 20 = 10\) cm behind the mirror.
For the image to coincide with the object, the light must retrace its path, so the rays must meet
the mirror normally — they must be heading for its centre of curvature.</p>
<p>Hence \(R = 10\) cm and \(f = R/2 = 5\) cm.</p>
{{fig:0}}
<p><b>Answer: 5</b></p>""",
        sfig=F.fig_jp_t3_lens_mirror),

    # 25 ----------------------------------------------------------------- Atoms
    NUM(src=("physics_2025_26", "7"), topic=ATOM,
        q=r"""<p>Find the ratio of the shortest wavelength of the Paschen series to the shortest wavelength
of the Lyman series of hydrogen.</p>""",
        answer=9,
        sol=r"""<p>\(\dfrac1\lambda = R\left(\dfrac1{n_f^2} - \dfrac1{n_i^2}\right)\); the shortest wavelength of a
series is the series limit, \(n_i\to\infty\): \(\lambda_{\min} = \dfrac{n_f^2}{R}\).</p>
<p>Paschen \(n_f = 3\): \(9/R\); Lyman \(n_f = 1\): \(1/R\). Ratio \(= 9\).</p>
<p><b>Answer: 9</b></p>"""),
]
