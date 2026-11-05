"""JEE Main mock test 2 — Physics (Q1-25).  Every item adapted from a kept pre-board question.

Options are written correct-first and placed by `_mcq(..., k=…)` so that the correct one lands at
index k; solutions never refer to an option by letter.
"""
from jee_kit import MCQ, NUM

SUBJECT = "physics"
TEST = 2

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
    _mcq(("physics_2014_15", "3(a)"), ES,
         r"""<p>Charges \(+q\), \(-2q\) and \(+q\) are placed at the vertices of an equilateral triangle
of side \(a\). The magnitude of the electric dipole moment of the system is</p>""",
         [r"\(\sqrt3\,qa\)", r"\(2qa\)", r"\(qa\)", r"zero"], 1,
         r"""<p>Split \(-2q\) into two charges \(-q\). The system is then two dipoles, each of moment
\(qa\), pointing from the \(-2q\) vertex to the two \(+q\) vertices, with \(60^\circ\) between them.</p>
<p>\(p = \sqrt{p_1^2 + p_2^2 + 2p_1p_2\cos60^\circ} = qa\sqrt{1+1+1} = \sqrt3\,qa\), along the
bisector from the \(-2q\) vertex.</p>
<p>\(2qa\) adds the two moments as if parallel; \(qa\) counts one dipole; "zero" confuses zero net
charge with zero dipole moment — the charges are not arranged symmetrically about a point, so the
two dipoles do not cancel.</p>
<p><b>Answer: \(\sqrt3\,qa\).</b></p>"""),

    # 2 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2015_16", "2(b)"), ES,
         r"""<p>A \(4\ \mu\)F capacitor charged to 300 V is disconnected from the supply and connected
across an uncharged \(2\ \mu\)F capacitor. The energy lost in the process is</p>""",
         [r"\(0.06\) J", r"\(0.18\) J", r"\(0.12\) J", r"\(0.03\) J"], 2,
         r"""<p>Charge \(Q = 4\times10^{-6}\times300 = 1.2\times10^{-3}\) C is shared:
common potential \(V = \dfrac{Q}{C_1 + C_2} = \dfrac{1.2\times10^{-3}}{6\times10^{-6}} = 200\) V.</p>
<p>\(U_i = \tfrac12(4\times10^{-6})(300)^2 = 0.18\) J; \(U_f = \tfrac12(6\times10^{-6})(200)^2 = 0.12\) J.</p>
<p>Loss \(= 0.18 - 0.12 = 0.06\) J
\(\left(= \dfrac{C_1C_2}{2(C_1+C_2)}V_1^2\right)\), dissipated as heat and radiation.</p>
<p>\(0.18\) J and \(0.12\) J are the initial and final energies; \(0.03\) J halves the loss formula
once too often.</p>
<p><b>Answer: \(0.06\) J.</b></p>"""),

    # 3 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2024_25", "10"), ES,
         r"""<p>A point charge of \(2\ \mu\)C is at the centre of a cube. The electric flux through
<i>one face</i> of the cube is (\(\varepsilon_0 = 8.85\times10^{-12}\) C\(^2\) N\(^{-1}\) m\(^{-2}\))</p>""",
         [r"\(3.77\times10^{4}\) N m\(^2\) C\(^{-1}\)", r"\(2.26\times10^{5}\) N m\(^2\) C\(^{-1}\)",
          r"\(1.88\times10^{4}\) N m\(^2\) C\(^{-1}\)", r"\(7.53\times10^{4}\) N m\(^2\) C\(^{-1}\)"], 3,
         r"""<p>Total flux through the closed cube (Gauss): \(\phi = \dfrac{q}{\varepsilon_0}
= \dfrac{2\times10^{-6}}{8.85\times10^{-12}} = 2.26\times10^{5}\) N m\(^2\) C\(^{-1}\).</p>
<p>By symmetry the six faces share it equally: \(\phi_{\text{face}} = \dfrac{q}{6\varepsilon_0}
= 3.77\times10^{4}\) N m\(^2\) C\(^{-1}\).</p>
<p>\(2.26\times10^{5}\) is the total flux; \(1.88\times10^{4}\) divides by 12 and
\(7.53\times10^{4}\) by 3.</p>
<p><b>Answer: \(3.77\times10^{4}\) N m\(^2\) C\(^{-1}\).</b></p>"""),

    # 4 ------------------------------------------------------------------ Current Electricity
    _mcq(("physics_2016_17", "3(a)"), CE,
         r"""<p>On a potentiometer wire a cell of emf 1.5 V is balanced at 75 cm, and another cell at
110 cm. The emf of the second cell is</p>""",
         [r"\(2.2\) V", r"\(1.02\) V", r"\(1.1\) V", r"\(1.65\) V"], 0,
         r"""<p>At balance no current is drawn from the cell, so \(\varepsilon = kl\) with the same
potential gradient \(k\) for both:
\(\dfrac{\varepsilon_2}{\varepsilon_1} = \dfrac{l_2}{l_1}\).</p>
<p>\(\varepsilon_2 = 1.5\times\dfrac{110}{75} = 2.2\) V.</p>
<p>\(1.02\) V inverts the ratio; \(1.1\) V assumes 1 V per metre of wire; \(1.65\) V multiplies
1.5 V by the length 1.10 m instead of by the ratio of the lengths.</p>
<p><b>Answer: \(2.2\) V.</b></p>"""),

    # 5 ------------------------------------------------------------------ Current Electricity
    _mcq(("physics_2025_26", "11(a)"), CE,
         r"""<p>In a metre bridge a 3 Ω resistor is in the left gap and an unknown resistance \(X\) in the
right gap. The null point is 60 cm from the left end. To shift the null point to 50 cm one must
connect</p>""",
         [r"\(1\ \Omega\) in series with \(X\)", r"\(1\ \Omega\) in parallel with \(X\)",
          r"\(9\ \Omega\) in parallel with \(X\)", r"\(2\ \Omega\) in series with \(X\)"], 1,
         r"""<p>Balance: \(\dfrac{3}{X} = \dfrac{60}{100-60}\Rightarrow X = 3\times\dfrac{40}{60} = 2\ \Omega\).</p>
<p>Null point at 50 cm needs equal arms, so the right gap must hold 3 Ω. Raising 2 Ω to 3 Ω needs
\(1\ \Omega\) in <i>series</i> (a parallel resistor can only lower it).</p>
<p>"\(1\ \Omega\) in parallel" would give 0.67 Ω; "\(9\ \Omega\) in parallel" comes from taking
\(X = 3\times60/40 = 4.5\ \Omega\) (the ratio inverted); "\(2\ \Omega\) in series" gives 4 Ω.</p>
<p><b>Answer: \(1\ \Omega\) in series with \(X\).</b></p>"""),

    # 6 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2014_15", "1(A)(ii)"), MAG,
         r"""<p>A wire bent into a single circular loop gives a magnetic field \(B\) at its centre when a
current \(I\) flows. The same wire is rebent into a circular coil of 2 turns and carries the same
current. The field at the centre becomes</p>""",
         [r"\(4B\)", r"\(2B\)", r"\(B\)", r"\(B/2\)"], 2,
         r"""<p>Same length of wire: \(2\pi R = 2(2\pi R')\Rightarrow R' = R/2\).</p>
<p>\(B = \dfrac{\mu_0NI}{2R}\Rightarrow B' = \dfrac{\mu_0(2)I}{2(R/2)} = 4\cdot\dfrac{\mu_0I}{2R} = 4B\)
(in general \(B\propto N^2\) for a fixed length).</p>
<p>\(2B\) counts the extra turn but forgets the smaller radius; \(B\) is what happens if both \(N\)
and \(R\) are doubled; \(B/2\) doubles the radius and forgets the extra turn.</p>
<p><b>Answer: \(4B\).</b></p>"""),

    # 7 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2013_14", "8(a)"), MAG,
         r"""<p>Electrons moving to the right with speed \(2\times10^{6}\) m s\(^{-1}\) pass undeviated
through crossed fields: an electric field of \(5\times10^{4}\) V m\(^{-1}\) pointing vertically
downward in the plane of the page, and a magnetic field \(\vec B\). Then \(\vec B\) is</p>""",
         [r"\(0.025\) T, into the page", r"\(0.025\) T, out of the page",
          r"\(40\) T, into the page", r"\(0.05\) T, into the page"], 3,
         r"""<p>Undeviated: \(eE = evB\Rightarrow B = \dfrac{E}{v} = \dfrac{5\times10^{4}}{2\times10^{6}}
= 0.025\) T.</p>
<p>Direction: the electric force on an electron is opposite to \(\vec E\), i.e. upward, so the
magnetic force \(-e(\vec v\times\vec B)\) must be downward, i.e. \(\vec v\times\vec B\) upward. With
\(\vec v\) to the right, \(\hat x\times(-\hat z) = +\hat y\): \(\vec B\) is into the page.</p>
<p>"Out of the page" treats the electron as a positive charge; \(40\) T is \(v/E\); \(0.05\) T is
\(2E/v\).</p>
<p><b>Answer: \(0.025\) T, into the page.</b></p>"""),

    # 8 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2024_25", "3(a)"), MAG,
         r"""<p>A long solenoid has 40 turns per centimetre and carries a current of 2.5 A. The magnetic
field well inside it, near the centre, is (\(\mu_0 = 4\pi\times10^{-7}\) T m A\(^{-1}\))</p>""",
         [r"\(12.6\) mT", r"\(0.126\) mT", r"\(6.3\) mT", r"\(1.26\) mT"], 0,
         r"""<p>\(n = 40\) cm\(^{-1}\) \(= 4000\) m\(^{-1}\).</p>
<p>\(B = \mu_0nI = 4\pi\times10^{-7}\times4000\times2.5 = 4\pi\times10^{-3}\) T \(= 12.6\) mT.</p>
<p>\(0.126\) mT leaves \(n\) per centimetre (40 m\(^{-1}\)); \(1.26\) mT uses 400 m\(^{-1}\);
\(6.3\) mT is the value at an <i>end</i> of the solenoid, \(\tfrac12\mu_0nI\).</p>
<p><b>Answer: \(12.6\) mT.</b></p>"""),

    # 9 ------------------------------------------------------------------ AC
    _mcq(("physics_2016_17", "1(B)(vii)"), EMI,
         r"""<p>A capacitor of capacitance \(\dfrac{100}{\pi}\ \mu\)F is connected to a 220 V, 50 Hz a.c.
supply. The r.m.s. current is</p>""",
         [r"\(2.2\) A", r"\(3.11\) A", r"\(1.56\) A", r"\(6.91\) A"], 1,
         r"""<p>\(X_C = \dfrac{1}{2\pi fC} = \dfrac{1}{2\pi\times50\times(10^{-4}/\pi)} = \dfrac{1}{10^{-2}}
= 100\ \Omega\).</p>
<p>\(I_{\text{rms}} = \dfrac{V_{\text{rms}}}{X_C} = \dfrac{220}{100} = 2.2\) A.</p>
<p>\(3.11\) A is the peak current (\(\times\sqrt2\)), \(1.56\) A divides by \(\sqrt2\) once more,
and \(6.91\) A drops the \(\pi\) from the capacitance (\(C = 100\ \mu\)F).</p>
<p><b>Answer: \(2.2\) A.</b></p>"""),

    # 10 ----------------------------------------------------------------- AC
    _mcq(("physics_2024_25", "1(A)(vi)"), EMI,
         r"""<p>A 50 Hz a.c. source is connected to a resistor of resistance \(P\) in series with a
component B of reactance \(Y\). The applied voltage <i>leads</i> the current by \(\pi/4\). Then</p>""",
         [r"B is an inductor and \(Y = P\)", r"B is a capacitor and \(Y = P\)",
          r"B is an inductor and \(Y = 2P\)", r"B is a capacitor and \(Y = 2P\)"], 2,
         r"""<p>Voltage leading the current means the circuit is inductive, so B is an inductor.</p>
<p>\(\tan\varphi = \dfrac{Y}{P} = \tan\dfrac{\pi}{4} = 1\Rightarrow Y = P\).</p>
<p>A capacitor would make the current lead the voltage, so both "capacitor" options are wrong;
\(Y = 2P\) would give \(\varphi = \tan^{-1}2 = 63.4^\circ\), not \(45^\circ\).</p>
<p><b>Answer: B is an inductor and \(Y = P\).</b></p>"""),

    # 11 ----------------------------------------------------------------- EM waves
    _mcq(("physics_2014_15", "8(b)"), EMW,
         r"""<p>Which sequence lists the radiations in order of <i>increasing wavelength</i>?</p>""",
         [r"X-rays, ultraviolet, infrared, microwaves",
          r"microwaves, infrared, ultraviolet, X-rays",
          r"ultraviolet, X-rays, microwaves, infrared",
          r"X-rays, infrared, ultraviolet, microwaves"], 3,
         r"""<p>Typical wavelengths: X-rays \(\sim10^{-10}\) m, ultraviolet \(\sim10^{-8}\) m,
infrared \(\sim10^{-5}\) m, microwaves \(\sim10^{-2}\) m.</p>
<p>"Microwaves, infrared, ultraviolet, X-rays" is the order of increasing <i>frequency</i> (decreasing
wavelength). "Ultraviolet, X-rays, microwaves, infrared" puts ultraviolet before X-rays and infrared after
microwaves; "X-rays, infrared, ultraviolet, microwaves" swaps infrared and ultraviolet, which lie on
opposite sides of the visible band.</p>
<p><b>Answer: X-rays, ultraviolet, infrared, microwaves.</b></p>"""),

    # 12 ----------------------------------------------------------------- Ray optics
    _mcq(("physics_2016_17", "1(B)(viii)"), RAY,
         r"""<p>A thin biconvex <i>air</i> lens with both radii of curvature 20 cm is formed inside a
block of glass of refractive index 1.5. The focal length of this air lens is</p>""",
         [r"\(-30\) cm (diverging)", r"\(+30\) cm (converging)", r"\(+20\) cm (converging)",
          r"\(-20\) cm (diverging)"], 1,
         r"""<p>Lens maker's formula with the lens in a medium:
\(\dfrac1f = \left(\dfrac{\mu_{\text{lens}}}{\mu_{\text{medium}}} - 1\right)\left(\dfrac1{R_1} - \dfrac1{R_2}\right)\),
with \(R_1 = +20\) cm, \(R_2 = -20\) cm.</p>
<p>\(\dfrac1f = \left(\dfrac{1}{1.5} - 1\right)\left(\dfrac{2}{20}\right) = -\dfrac13\times\dfrac1{10}
= -\dfrac1{30}\Rightarrow f = -30\) cm. A convex lens of a <i>rarer</i> medium diverges.</p>
<p>\(+30\) cm loses the sign; \(+20\) cm is a glass lens in air; \(-20\) cm uses
\((\mu_{\text{air}} - \mu_{\text{glass}})\) instead of the ratio.</p>
<p><b>Answer: \(-30\) cm (diverging).</b></p>"""),

    # 13 ----------------------------------------------------------------- Ray optics
    _mcq(("physics_2014_15", "1(A)(v)"), RAY,
         r"""<p>An astronomical telescope has lenses of focal lengths 90 cm and 10 cm. In normal
adjustment (final image at infinity) the length of the tube and the magnifying power are</p>""",
         [r"\(100\) cm and \(9\)", r"\(80\) cm and \(9\)", r"\(100\) cm and \(0.11\)",
          r"\(100\) cm and \(12.6\)"], 0,
         r"""<p>The lens of larger focal length is the objective: \(f_o = 90\) cm, \(f_e = 10\) cm.</p>
<p>Normal adjustment: \(L = f_o + f_e = 100\) cm, \(M = \dfrac{f_o}{f_e} = 9\).</p>
<p>\(80\) cm subtracts the focal lengths; \(0.11\) is \(f_e/f_o\); \(12.6 = \dfrac{f_o}{f_e}
\left(1 + \dfrac{f_e}{D}\right)\) is the magnifying power when the final image is at 25 cm, not at
infinity (and then the tube is shorter than 100 cm).</p>
<p><b>Answer: \(100\) cm and \(9\).</b></p>"""),

    # 14 ----------------------------------------------------------------- Wave optics
    _mcq(("physics_2013_14", "7(b)"), WAVE,
         r"""<p>Two coherent waves of intensities \(I\) and \(4I\) superpose at a point where their phase
difference is \(\pi/3\). The resultant intensity is</p>""",
         [r"\(7I\)", r"\(9I\)", r"\(5I\)", r"\(3I\)"], 1,
         r"""<p>\(I_R = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\varphi = I + 4I + 2(2I)\cos60^\circ = 5I + 2I = 7I\).</p>
<p>\(9I\) is the maximum (\(\varphi = 0\)), \(5I\) the value at \(\varphi = \pi/2\) (or for
incoherent sources), and \(3I\) uses \(\cos\varphi = -\tfrac12\) (\(\varphi = 2\pi/3\)).</p>
<p><b>Answer: \(7I\).</b></p>"""),

    # 15 ----------------------------------------------------------------- Wave optics
    _mcq(("physics_2024_25", "18(b)"), WAVE,
         r"""<p>Light of wavelength 600 nm falls normally on a single slit. The first minimum of the
diffraction pattern is at an angle of \(30^\circ\). The width of the slit is</p>""",
         [r"\(1.2\ \mu\)m", r"\(0.6\ \mu\)m", r"\(2.4\ \mu\)m", r"\(0.3\ \mu\)m"], 2,
         r"""<p>First minimum of a single slit: \(a\sin\theta = \lambda\).</p>
<p>\(a = \dfrac{\lambda}{\sin30^\circ} = \dfrac{600\times10^{-9}}{0.5} = 1.2\times10^{-6}\) m
\(= 1.2\ \mu\)m.</p>
<p>\(0.6\ \mu\)m sets \(a = \lambda\); \(2.4\ \mu\)m uses \(a\sin\theta = 2\lambda\) (second minimum);
\(0.3\ \mu\)m multiplies by \(\sin\theta\) instead of dividing.</p>
<p><b>Answer: \(1.2\ \mu\)m.</b></p>"""),

    # 16 ----------------------------------------------------------------- Dual nature
    _mcq(("physics_2013_14", "1(B)(v)"), DUAL,
         r"""<p>The threshold frequency of a metal is \(5\times10^{14}\) Hz. Its threshold wavelength and
work function are (\(h = 6.6\times10^{-34}\) J s, \(c = 3\times10^{8}\) m s\(^{-1}\))</p>""",
         [r"\(600\) nm and \(2.06\) eV", r"\(600\) nm and \(3.30\) eV", r"\(500\) nm and \(2.48\) eV",
          r"\(6000\) nm and \(2.06\) eV"], 3,
         r"""<p>\(\lambda_0 = \dfrac{c}{\nu_0} = \dfrac{3\times10^{8}}{5\times10^{14}} = 6\times10^{-7}\) m
\(= 600\) nm.</p>
<p>\(\phi_0 = h\nu_0 = 6.6\times10^{-34}\times5\times10^{14} = 3.3\times10^{-19}\) J
\(= \dfrac{3.3\times10^{-19}}{1.6\times10^{-19}} = 2.06\) eV.</p>
<p>\(3.30\) eV reads the joule figure as if it were in eV; \(500\) nm and \(2.48\) eV come from misreading
the 5 of \(5\times10^{14}\) Hz as a 500 nm threshold and then using \(1240/500\); \(6000\) nm slips a
power of ten.</p>
<p><b>Answer: \(600\) nm and \(2.06\) eV.</b></p>"""),

    # 17 ----------------------------------------------------------------- Dual nature
    _mcq(("physics_2025_26", "9"), DUAL,
         r"""<p>A monochromatic source emits light of wavelength 660 nm. The energy and the momentum of
each photon are (\(h = 6.6\times10^{-34}\) J s, \(c = 3\times10^{8}\) m s\(^{-1}\))</p>""",
         [r"\(3.0\times10^{-19}\) J and \(1.0\times10^{-27}\) kg m s\(^{-1}\)",
          r"\(3.0\times10^{-19}\) J and \(9.0\times10^{-11}\) kg m s\(^{-1}\)",
          r"\(1.0\times10^{-27}\) J and \(3.0\times10^{-19}\) kg m s\(^{-1}\)",
          r"\(4.4\times10^{-40}\) J and \(1.0\times10^{-27}\) kg m s\(^{-1}\)"], 0,
         r"""<p>\(E = \dfrac{hc}{\lambda} = \dfrac{6.6\times10^{-34}\times3\times10^{8}}{6.6\times10^{-7}}
= 3.0\times10^{-19}\) J (about 1.9 eV).</p>
<p>\(p = \dfrac{h}{\lambda} = \dfrac{6.6\times10^{-34}}{6.6\times10^{-7}} = 1.0\times10^{-27}\)
kg m s\(^{-1}\) (equivalently \(p = E/c\)).</p>
<p>\(9.0\times10^{-11}\) is \(Ec\) instead of \(E/c\); "\(1.0\times10^{-27}\) J and \(3.0\times10^{-19}\) kg m s\(^{-1}\)" swaps the two values;
\(4.4\times10^{-40}\) J is \(h\lambda\).</p>
<p><b>Answer: \(3.0\times10^{-19}\) J and \(1.0\times10^{-27}\) kg m s\(^{-1}\).</b></p>"""),

    # 18 ----------------------------------------------------------------- Atoms
    _mcq(("physics_2024_25", "1(B)(iii)"), ATOM,
         r"""<p>In the Bohr model of hydrogen the radius of the first orbit is \(a_0\). The de Broglie
wavelength of the electron in the <i>second</i> orbit is</p>""",
         [r"\(4\pi a_0\)", r"\(8\pi a_0\)", r"\(2\pi a_0\)", r"\(16\pi a_0\)"], 3,
         r"""<p>Bohr's condition \(mvr = \dfrac{nh}{2\pi}\) with \(\lambda = \dfrac{h}{mv}\) gives
\(2\pi r_n = n\lambda\): the orbit holds \(n\) whole wavelengths.</p>
<p>\(r_2 = 2^2a_0 = 4a_0\), so \(\lambda = \dfrac{2\pi r_2}{2} = \dfrac{2\pi(4a_0)}{2} = 4\pi a_0\).</p>
<p>\(8\pi a_0\) is the whole circumference (forgets \(n = 2\)); \(2\pi a_0\) is the first-orbit
value; \(16\pi a_0\) multiplies by \(n\) instead of dividing.</p>
<p><b>Answer: \(4\pi a_0\).</b></p>"""),

    # 19 ----------------------------------------------------------------- Semiconductors
    _mcq(("physics_2015_16", "1(B)(xv)"), SEMI,
         r"""<p>Pure silicon is doped with a small amount of arsenic (group 15). The resulting
semiconductor is</p>""",
         [r"n-type, with electrons as majority carriers",
          r"p-type, with holes as majority carriers",
          r"n-type, with holes as majority carriers",
          r"intrinsic, with equal numbers of electrons and holes"], 2,
         r"""<p>Arsenic is pentavalent: four of its valence electrons form covalent bonds with silicon
and the fifth is loosely bound and easily freed. Arsenic is a donor, so the material is n-type and
electrons are the majority carriers (holes, made only thermally, are the minority).</p>
<p>p-type needs a trivalent (group 13) acceptor; "n-type with holes as majority" contradicts what
n-type means; a doped crystal is extrinsic, not intrinsic.</p>
<p><b>Answer: n-type, with electrons as majority carriers.</b></p>"""),

    # 20 ----------------------------------------------------------------- Semiconductors
    _mcq(("physics_2025_26", "20"), SEMI,
         r"""<p>A full-wave rectifier is fed from the 50 Hz mains. The fundamental frequency of the
ripple in its output is</p>""",
         [r"\(100\) Hz", r"\(50\) Hz", r"\(25\) Hz", r"zero (the output is steady d.c.)"], 3,
         r"""<p>The full-wave rectifier passes both half-cycles with the same polarity, giving one
output pulse every half-cycle: \(2\times50 = 100\) pulses per second, so the ripple frequency is
100 Hz.</p>
<p>\(50\) Hz is the half-wave rectifier's ripple; \(25\) Hz halves instead of doubling; a rectifier
alone gives pulsating, not steady, d.c. — a filter is needed to smooth it.</p>
<p><b>Answer: \(100\) Hz.</b></p>"""),

    # ===================================================================== Section B (integer)
    # 21 ----------------------------------------------------------------- Electrostatics
    NUM(src=("physics_2014_15", "2(b)"), topic=ES,
        q=r"""<p>A parallel-plate capacitor has plates of area 100 cm\(^2\) separated by 0.885 mm in air.
It is connected to a 200 V battery. With the battery still connected, the gap is completely filled
with a dielectric of dielectric constant 5. Find the energy now stored in the capacitor, in
microjoule. (\(\varepsilon_0 = 8.85\times10^{-12}\) F m\(^{-1}\))</p>""",
        answer=10,
        sol=r"""<p>\(C_0 = \dfrac{\varepsilon_0A}{d} = \dfrac{8.85\times10^{-12}\times10^{-2}}{8.85\times10^{-4}}
= 1.0\times10^{-10}\) F.</p>
<p>Battery connected: \(V = 200\) V stays fixed and \(C = KC_0 = 5\times10^{-10}\) F.</p>
<p>\(U = \tfrac12CV^2 = \tfrac12\times5\times10^{-10}\times(200)^2 = 1.0\times10^{-5}\) J
\(= 10\ \mu\)J. (Had the battery been disconnected first, \(U\) would have fallen to
\(0.4\ \mu\)J instead.)</p>
<p><b>Answer: 10</b></p>"""),

    # 22 ----------------------------------------------------------------- Current Electricity
    NUM(src=("physics_2025_26", "4(a)"), topic=CE,
        q=r"""<p>An electric heater boils a quantity of water in 20 minutes. Its heating coil is cut into
two equal halves, which are connected in parallel and used on the same supply. Find the time, in
minutes, to boil the same quantity of water from the same initial temperature.</p>""",
        answer=5,
        sol=r"""<p>The same heat is needed: \(H = \dfrac{V^2}{R}t\) with \(V\) fixed, so \(t\propto R\).</p>
<p>Each half has \(R/2\); two in parallel give \(R/4\).</p>
<p>\(t' = 20\times\dfrac14 = 5\) minutes.</p>
<p><b>Answer: 5</b></p>"""),

    # 23 ----------------------------------------------------------------- AC
    NUM(src=("physics_2015_16", "7(b)"), topic=EMI,
        q=r"""<p>A series LCR circuit with \(R = 50\ \Omega\) is connected to a 220 V a.c. source. When
only the capacitor is removed, the current lags the voltage by \(45^\circ\); when only the inductor
is removed, the current leads the voltage by \(45^\circ\). Find the average power dissipated in the
LCR circuit, in watt.</p>""",
        answer=968,
        sol=r"""<p>Capacitor removed: \(\tan45^\circ = X_L/R\Rightarrow X_L = R\).
Inductor removed: \(\tan45^\circ = X_C/R\Rightarrow X_C = R\).</p>
<p>So \(X_L = X_C\): the full circuit is at resonance, \(Z = R = 50\ \Omega\), power factor 1.</p>
<p>\(P = \dfrac{V^2}{R} = \dfrac{220^2}{50} = 968\) W.</p>
<p><b>Answer: 968</b></p>"""),

    # 24 ----------------------------------------------------------------- Ray optics
    NUM(src=("physics_2016_17", "11(a)"), topic=RAY,
        q=r"""<p>A small bulb is at the bottom of a wide tank filled with water (\(\mu = 4/3\)) to a depth of
\(2\sqrt7\) cm. Light from the bulb leaves the water surface only through a circular patch. Find the
radius of this patch, in cm.</p>""",
        answer=6,
        sol=r"""<p>Light escapes only where it meets the surface at less than the critical angle:
\(\sin C = \dfrac1\mu = \dfrac34\), so \(\cos C = \dfrac{\sqrt7}{4}\) and \(\tan C = \dfrac{3}{\sqrt7}\).</p>
<p>Radius \(r = h\tan C = 2\sqrt7\times\dfrac{3}{\sqrt7} = 6\) cm.</p>
<p><b>Answer: 6</b></p>"""),

    # 25 ----------------------------------------------------------------- Nuclei
    NUM(src=("physics_2015_16", "1(B)(xiv)"), topic=NUC,
        q=r"""<p>If 2 mg of matter were converted completely into energy, the energy released would be
\(N\times10^{10}\) J. Find \(N\). (\(c = 3\times10^{8}\) m s\(^{-1}\))</p>""",
        answer=18,
        sol=r"""<p>\(E = mc^2 = (2\times10^{-6}\ \text{kg})(3\times10^{8})^2 = 1.8\times10^{11}\) J
\(= 18\times10^{10}\) J. (Note 2 mg = \(2\times10^{-6}\) kg, not \(2\times10^{-3}\).)</p>
<p><b>Answer: 18</b></p>"""),
]
