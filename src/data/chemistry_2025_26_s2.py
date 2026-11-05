"""Heritage School Pre-Board 2025-26, Chemistry (Paper 1), Set 2 -- transcribed from the page images
of the .docx (rendered to PDF).  The paper's own heading reads 'Improvement Examinations, 2025-2026'."""
from kit import Q, SEC
import chemistry_2025_26_figs as fg
from chemistry_2025_26_s1 import SALT_BRIDGE, CARBYLAMINE_Q, CARBYLAMINE_A

AR = r"""<p>(a) Both assertion and reason are true, and reason is the correct explanation of assertion.<br>
(b) Both assertion and reason are true, but reason is not the correct explanation for assertion.<br>
(c) Assertion is true, but reason is false.<br>
(d) Assertion is false, but reason is true.</p>"""

WORDS = (r"[substitution, decreases, carbocation, tripled, 2-chloro propane, tertiary, halved, allyl chloride, "
         r"Raoult's, does, 2-propanone, elimination, doesn't, iodoform, primary, first, doubled, Lucas, "
         r"free-radical, Hinsberg, doubled, secondary, remains same, vinyl chloride, zero, second]")

PAPER = dict(
    subject="chemistry",
    year="2025-26",
    slug="2025-26-set-2",
    paper="Set 2 (Improvement Examination)",
    source="/home/sayantan/Ujaan/class12/SchoolNotes/PreBoard-PYQ/2025-26/SET-2/CHEMISTRY.docx",
    marks=70, time="3 hours",
    intro=r"""<p><b>The Heritage School &mdash; Improvement Examinations, 2025-2026</b> (as headed on the paper; filed as
Pre-Board Set 2). <b>Subject: Chemistry (Paper 1), Class XII.</b> Maximum Marks: 70. Time Allotted: Three
Hours. Reading Time: Additional Fifteen Minutes.</p>
<p>Instructions to Candidates</p>
<ol>
<li>You are allowed an additional fifteen minutes for only reading the question paper.</li>
<li>You must NOT start writing during the reading time.</li>
<li>This question paper has 9 printed pages.</li>
<li>It is divided into four sections and has twenty-one questions in all.</li>
<li>Answer all questions.</li>
<li>Section A has fourteen subparts. Each question carries 1 mark.</li>
<li>While attempting Multiple Choice Questions in Section A, you are required to write only ONE option as
the answer.</li>
<li>Section B has ten questions. Each question carries 2 marks.</li>
<li>Section C has seven questions. Each question carries 3 marks.</li>
<li>Section D has three questions. Each question carries 5 marks.</li>
<li>Internal choices have been provided in one question each in Sections B, C and D.</li>
<li>The intended marks for questions are given in brackets [ ].</li>
<li>All working, including rough work, should be done on the same sheet as, and adjacent to the rest of
the answer.</li>
<li>Balanced equations must be given wherever possible and diagrams where they are helpful.</li>
<li>When solving numerical problems, all essential workings must be shown.</li>
<li>In working out problems, use the following data: Gas constant R = 1&middot;987 cal deg<sup>&minus;1</sup>
mol<sup>&minus;1</sup> = 8&middot;314 J K<sup>&minus;1</sup> mol<sup>&minus;1</sup> = 0&middot;0821 dm<sup>3</sup>
atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>, 1 l atm = 1 dm<sup>3</sup> atm = 101&middot;3 J.
1 Faraday = 96500 coulombs. Avogadro's number = 6&middot;023 &times; 10<sup>23</sup>.</li>
</ol>""",
    items=[
        SEC("Section A &ndash; (14 marks)", "Question 1"),
        Q("1(A)(i)", 1, r"<p><b>(A) Fill in the blanks by choosing the appropriate word(s) from those given in the "
          r"brackets:</b> " + WORDS + r" [4&times;1]</p>"
          r"<p>(i) Ideal solution obeys ________ law and they ________ form azeotropic mixture.</p>",
          a=r"""<p>Ideal solution obeys <b>Raoult's</b> law and they <b>doesn't</b> [do not] form azeotropic
mixture.</p>
<p>An ideal solution obeys Raoult's law at all compositions (\(\Delta H_\text{mix} = 0\), \(\Delta V_\text{mix} = 0\));
azeotropes arise only from large positive or negative deviations, so ideal solutions can always be separated by
fractional distillation.</p>
<p><span class="box">Raoult's; doesn't</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>Ideal: \(p_A = p^\circ_Ax_A\) at all compositions; A&ndash;B forces = A&ndash;A and B&ndash;B forces.</li>
<li>Azeotrope: boils at constant temperature with the same composition in liquid and vapour (non-ideal only).</li></ul>"""),
        Q("1(A)(ii)", 1, r"<p>(ii) When the concentration of reactant of first order reaction is doubled, the rate "
          r"becomes ______ but for ______ order reaction, the rate remains same.</p>",
          a=r"""<p>When the concentration of reactant of first order reaction is doubled, the rate becomes
<b>doubled</b> but for <b>zero</b> order reaction, the rate remains same.</p>
<p>Rate \(= k[\mathrm{A}]^1\) doubles; rate \(= k[\mathrm{A}]^0 = k\) is independent of concentration.</p>
<p><span class="box">doubled; zero</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Rate \(= k[\mathrm{A}]^n\): changing [A] by a factor \(x\) changes the rate by \(x^n\).</li></ul>"""),
        Q("1(A)(iii)", 1, r"<p>(iii) A mixture of conc. HCl and anhydrous ZnCl<sub>2</sub> is called ______ reagent "
          r"which shows maximum reactivity with _______ alcohol.</p>",
          a=r"""<p>A mixture of conc. HCl and anhydrous \(\ce{ZnCl2}\) is called <b>Lucas</b> reagent which shows
maximum reactivity with <b>tertiary</b> alcohol (turbidity appears immediately, via the most stable 3&deg;
carbocation).</p>
<p><span class="box">Lucas; tertiary</span></p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Lucas test: 3&deg; immediate turbidity, 2&deg; in about 5 min, 1&deg; none at room
temperature (S<sub>N</sub>1 reactivity follows carbocation stability).</li></ul>"""),
        Q("1(A)(iv)", 1, r"<p>(iv) Chlorination of propene at 773 K gives __________ and it involves _________ "
          r"mechanism.</p>",
          a=r"""<p>Chlorination of propene at 773 K gives <b>allyl chloride</b> and it involves <b>free-radical</b>
mechanism.</p>
<p>\(\ce{CH2=CH-CH3 + Cl2 ->[773 K] CH2=CH-CH2Cl + HCl}\) (3-chloropropene): at high temperature allylic
substitution by free radicals replaces addition across the double bond.</p>
<p><span class="box">allyl chloride; free-radical</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Low temperature: addition (1,2-dichloropropane). High temperature: allylic
substitution, via the resonance-stabilised allyl radical.</li></ul>"""),
        Q("1(B)(i)", 1, r"<p><b>(B) Select and write the correct alternative from the choices given below:</b> "
          r"[7&times;1]</p><p>(i) The complex [Ni(CN)<sub>4</sub>]<sup>2&minus;</sup> is:</p>"
          r"<p>(a) tetrahedral and paramagnetic<br>(b) square planar and diamagnetic<br>"
          r"(c) square planar and paramagnetic<br>(d) tetrahedral and diamagnetic</p>",
          a=r"""<p>\(\ce{Ni^2+}\) is 3d<sup>8</sup>. \(\ce{CN-}\) is a strong-field ligand: the two unpaired 3d electrons
pair up, freeing one 3d orbital; dsp<sup>2</sup> hybridisation gives a square planar complex with no unpaired
electron.</p>
{{fig:0}}
<p><span class="box">(b) square planar and diamagnetic</span></p>""",
          afig=[fg.fig_s2_nicn4_vbt],
          topic="Coordination Compounds",
          recall=r"""<ul><li>CN = 4: dsp<sup>2</sup> (strong field, d<sup>8</sup>) &rarr; square planar;
sp<sup>3</sup> (weak field) &rarr; tetrahedral.</li></ul>"""),
        Q("1(B)(ii)", 1, r"<p>(ii) In the spectrochemical series, the magnitude of the crystal field splitting is "
          r"maximum for which ion?</p><p>(a) Cl<sup>&minus;1</sup> &nbsp; (b) F<sup>&minus;1</sup> &nbsp; "
          r"(c) NO<sub>2</sub><sup>&minus;1</sup> &nbsp; (d) CO</p>",
          a=r"""<p>Spectrochemical series: \(\ce{I-} < \ce{Br-} < \ce{Cl-} < \ce{F-} < \ce{OH-} < \ce{H2O} < \ce{NH3}
< \ce{en} < \ce{NO2-} < \ce{CN-} < \ce{CO}\). CO (a &pi;-acceptor) produces the largest splitting.</p>
<p><span class="box">(d) CO</span></p>
<p class="note">CO is a neutral ligand, not an ion; it is nevertheless the intended answer.</p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Halides are weak field; CN<sup>&minus;</sup> and CO are the strongest.</li></ul>"""),
        Q("1(B)(iii)", 1, r"<p>(iii) Which of the following forms propane nitrile as the major product?</p>"
          r"<p>(a) Ethyl bromide + alc. KCN<br>(b) Ethyl bromide + alc. AgCN<br>(c) Propyl bromide + alc. AgCN<br>"
          r"(d) Propyl bromide + alc. KCN</p>",
          a=r"""<p>Propanenitrile is \(\ce{CH3CH2CN}\) (3 C including the CN carbon). Ionic KCN attacks through C:
\(\ce{CH3CH2Br + KCN -> CH3CH2CN + KBr}\). AgCN would give the isocyanide; propyl bromide + KCN gives
butanenitrile.</p>
<p><span class="box">(a) Ethyl bromide + alc. KCN</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>KCN &rarr; R&ndash;CN (one C added); AgCN &rarr; R&ndash;NC.</li>
<li>Nitrile name counts the CN carbon: C<sub>2</sub>H<sub>5</sub>CN = propanenitrile.</li></ul>"""),
        Q("1(B)(iv)", 1, r"<p>(iv) Which of the following carbohydrates is a monosaccharide?</p>"
          r"<p>(a) Sucrose &nbsp; (b) Galactose &nbsp; (c) Maltose &nbsp; (d) Lactose</p>",
          a=r"""<p>Sucrose, maltose and lactose are disaccharides; galactose (\(\ce{C6H12O6}\), an aldohexose) is a
monosaccharide.</p><p><span class="box">(b) Galactose</span></p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Sucrose = glucose + fructose; maltose = 2 glucose; lactose = galactose + glucose.</li></ul>"""),
        Q("1(B)(v)", 1, r"<p>(v) When acetic acid is reacted with Ca(OH)<sub>2</sub> and the product is distilled "
          r"dry, the compound formed is &ndash;</p><p>(a) calcium acetate &nbsp; (b) acetaldehyde &nbsp; "
          r"(c) acetone &nbsp; (d) acetic anhydride</p>",
          a=r"""<p>\(\ce{2CH3COOH + Ca(OH)2 -> (CH3COO)2Ca + 2H2O}\);
\(\ce{(CH3COO)2Ca ->[dry distillation] CH3COCH3 + CaCO3}\).</p>
<p><span class="box">(c) acetone</span></p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Dry distillation of a calcium carboxylate gives a ketone (with calcium formate, an
aldehyde).</li></ul>"""),
        Q("1(B)(vi)", 1, r"<p>(vi) Given below are two statements marked Assertion and Reason. Read the two statements "
          r"carefully and select the correct option.</p><p><b>Assertion</b>: &Delta;H<sub>mix</sub> and "
          r"&Delta;V<sub>mix</sub> are greater than zero for non-ideal solution.<br><b>Reason</b>: The interactions "
          r"between the particles of the components of a non-ideal solution are different from that of particles "
          r"in the liquids.</p>" + AR,
          a=r"""<p>The assertion is true only for solutions with <b>positive</b> deviation; for negative deviation
(e.g. chloroform + acetone) \(\Delta H_\text{mix} < 0\) and \(\Delta V_\text{mix} < 0\). So as a general statement
about non-ideal solutions it is false. The reason correctly describes non-ideal behaviour.</p>
<p><span class="box">(d) Assertion is false, but reason is true</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>Positive deviation: weaker A&ndash;B forces, \(\Delta H, \Delta V > 0\).
Negative deviation: stronger A&ndash;B forces, \(\Delta H, \Delta V < 0\).</li></ul>"""),
        Q("1(B)(vii)", 1, r"<p>(vii) Given below are two statements marked Assertion and Reason. Read the two "
          r"statements carefully and select the correct option.</p><p><b>Assertion</b>: p-nitrophenol is more "
          r"acidic than phenol.<br><b>Reason</b>: Nitro group helps in the stabilisation of the phenoxide ion by "
          r"dispersal of negative charge due to resonance.</p>" + AR,
          a=r"""<p>The p-nitro group withdraws electrons by &ndash;R and &ndash;I effects; the negative charge of the
p-nitrophenoxide ion is delocalised onto the oxygens of \(\ce{-NO2}\), stabilising it, so p-nitrophenol
(pK<sub>a</sub> 7.1) is more acidic than phenol (pK<sub>a</sub> 10.0). The reason explains the assertion.</p>
<p><span class="box">(a) Both true; reason is the correct explanation</span></p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Anything that stabilises the phenoxide ion increases the acidity of phenol.</li></ul>"""),
        Q("1(C)", 3, r"<p><b>C. Read the passage given below carefully and answer the questions that follow:</b></p>"
          r"<p>The study of the conductivity of electrolyte solutions is important for the development of "
          r"electrochemical devices, for the characterization of the dissociation equilibrium of weak electrolytes, "
          r"and for the fundamental understanding of charge transport by ions. The conductivity of the electrolyte "
          r"is measured for electrolyte solution with concentrations in the range of 10<sup>&minus;3</sup> to "
          r"10<sup>&minus;1</sup> mol L<sup>&minus;1</sup>, as a solution in this range of concentrations can be "
          r"easily prepared. The molar conductivity (&Lambda;<sub>m</sub>) of strong electrolyte solutions can be "
          r"nicely fit by the Kohlrausch equation.</p>"
          r"<p>&Lambda;<sub>m</sub> = &Lambda;&deg;<sub>m</sub> &ndash; K &radic;C &hellip;(i)</p>"
          r"<p>Where &Lambda;&deg;<sub>m</sub> is the molar conductivity at infinite dilution and C is the "
          r"concentration of the solution. K is an empirical proportionality constant to be obtained from the "
          r"experiment. The molar conductivity of weak electrolytes, on the other hand, is dependent on the degree "
          r"of dissociation of the electrolyte.</p>"
          r"<p>(i) What happens to molar conductivity of weak electrolyte on dilution?</p>"
          r"<p>(ii) If &Lambda;&deg;<sub>m</sub> of HCl, NaCl and CH<sub>3</sub>COONa is 426.1, 126.4 and 91.0 S "
          r"cm<sup>2</sup> mol<sup>&minus;1</sup> respectively, calculate &Lambda;&deg;<sub>m</sub> of "
          r"CH<sub>3</sub>COOH.</p>"
          r"<p>(iii) 0.05 M NaOH solution offered a resistance of 31.6 ohm in a conductivity cell at 298 K having "
          r"conductivity 0.01161 S cm<sup>&minus;1</sup>. If the same cell filled with 0.02 M HCl solution, the "
          r"resistance changed to 29.2 ohm. Find the conductivity of the acid solution.</p>",
          a=r"""<p><b>(i)</b> It <b>increases steeply</b> on dilution, especially at low concentration: the degree of
dissociation \(\alpha\) increases, so the number of ions per mole rises (\(\Lambda_m = \alpha\Lambda^\circ_m\)). The
curve of \(\Lambda_m\) against \(\sqrt{C}\) is not linear, so \(\Lambda^\circ_m\) cannot be found by
extrapolation.</p>
<p><b>(ii)</b> Kohlrausch's law of independent migration:</p>
<p>\[\Lambda^\circ_m(\ce{CH3COOH}) = \Lambda^\circ_m(\ce{CH3COONa}) + \Lambda^\circ_m(\ce{HCl}) - \Lambda^\circ_m(\ce{NaCl})\]</p>
<p>\[= 91.0 + 426.1 - 126.4 = 390.7\]</p>
<p><span class="box">\(\Lambda^\circ_m(\ce{CH3COOH}) = 390.7\) S cm<sup>2</sup> mol<sup>&minus;1</sup></span></p>
<p><b>(iii)</b> Cell constant \(G^* = \kappa R = 0.01161\times31.6 = 0.3669\) cm<sup>&minus;1</sup>.</p>
<p>\[\kappa_\text{HCl} = \frac{G^*}{R} = \frac{0.3669}{29.2} = 1.256\times10^{-2}\ \text{S cm}^{-1}\]</p>
<p><span class="box">\(\kappa\)(HCl) \(\approx 0.0126\) S cm<sup>&minus;1</sup></span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\kappa = G^*/R\); cell constant \(G^* = l/A\) is fixed for a given cell.</li>
<li>Kohlrausch: \(\Lambda^\circ_m\) of a weak electrolyte from those of strong electrolytes.</li></ul>"""),
        # ------------------------------------------------------------------ Section B
        SEC("Section-B (20 marks)"),
        Q("2", 2, r"<p>The rate of reaction becomes 4 times when the temperature changes from 293 K to 313 K. "
          r"Calculate the activation energy of the reaction. What will be the value of the rate constant at very "
          r"high temperature?</p>",
          a=r"""<p>\[\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2-T_1}{T_1T_2}\right)\]</p>
<p>\[\log 4 = \frac{E_a}{2.303\times8.314}\times\frac{313-293}{293\times313}\]</p>
<p>\[0.6021 = \frac{E_a}{19.147}\times2.181\times10^{-4}\]</p>
<p>\[E_a = \frac{0.6021\times19.147}{2.181\times10^{-4}} = 5.29\times10^{4}\ \text{J mol}^{-1}\]</p>
<p><span class="box">\(E_a \approx 52.9\) kJ mol<sup>&minus;1</sup></span></p>
<p>At very high temperature \(E_a/RT \to 0\), so \(k = Ae^{-E_a/RT} \to A\):
<span class="box">k approaches the pre-exponential (frequency) factor A</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Arrhenius: \(k = Ae^{-E_a/RT}\); as \(T\to\infty\), \(k \to A\).</li>
<li>Rate ratio = rate-constant ratio at fixed concentrations.</li></ul>"""),
        Q("3", 2, r"<p>Devise a scheme for the preparation of</p><p>(i) Bromomethane to propan-2-one</p>"
          r"<p>(ii) Benzene to diphenyl</p>",
          a=r"""<p><b>(i)</b> Make both a nitrile and a Grignard reagent from bromomethane, then combine them:</p>
<p>\[\ce{CH3Br + KCN(alc) -> CH3CN + KBr}\]</p>
<p>\[\ce{CH3Br + Mg ->[dry ether] CH3MgBr}\]</p>
<p>\[\ce{CH3C#N + CH3MgBr -> (CH3)2C=NMgBr}\]</p>
<p>\[\ce{(CH3)2C=NMgBr + 2H2O ->[H+] CH3COCH3 + NH3 + Mg(OH)Br}\]</p>
<p><b>(ii)</b> Chlorinate benzene, then couple by the Fittig reaction:</p>
<p>\[\ce{C6H6 + Cl2 ->[\text{anhyd.} FeCl3] C6H5Cl + HCl}\]</p>
<p>\[\ce{2C6H5Cl + 2Na ->[dry ether] C6H5-C6H5 + 2NaCl}\]</p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Nitrile + RMgX, then hydrolysis &rarr; ketone.</li>
<li>Fittig: 2 ArX + 2Na &rarr; Ar&ndash;Ar (biphenyl/diphenyl).</li></ul>"""),
        Q("4", 2, r"<p>Using IUPAC nomenclature, write the formula of each of the following:</p>"
          r"<p>(i) tetraamminediaquacopper (II) sulphate</p>"
          r"<p>(ii) tetraamminedichloridocobalt (III) hexacyanochromate (III)</p>",
          a=r"""<p><b>(i)</b> Cu(II) + 4 NH<sub>3</sub> + 2 H<sub>2</sub>O: complex ion charge +2, balanced by one
\(\ce{SO4^2-}\).</p>
<p><span class="box">\(\ce{[Cu(NH3)4(H2O)2]SO4}\)</span></p>
<p><b>(ii)</b> Cation: Co(III) + 2 \(\ce{Cl-}\) &rArr; \(\ce{[CoCl2(NH3)4]+}\). Anion: Cr(III) + 6 \(\ce{CN-}\)
&rArr; \(\ce{[Cr(CN)6]^3-}\). Three cations balance one anion.</p>
<p><span class="box">\(\ce{[CoCl2(NH3)4]3[Cr(CN)6]}\)</span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Formula: metal first, then ligands in alphabetical order of their symbols, in [ ].</li>
<li>Charge on complex = oxidation state of metal + sum of ligand charges.</li></ul>"""),
        Q("5", 2, r"<p>A 10 % aqueous solution of cane sugar (mol. wt. 342) is isotonic with 1.754 % aqueous solution "
          r"of urea. Find the molecular mass of urea. If the experimental molecular mass of urea is 60.06 g/mol, "
          r"what is the value of van't Hoff factor of urea?</p>",
          a=r"""<p>Isotonic solutions have equal molar concentrations (\(\pi = CRT\) at the same T). For equal volumes
(100 mL):</p>
<p>\[\frac{10}{342} = \frac{1.754}{M} \;\Rightarrow\; M = \frac{1.754\times342}{10} = 59.99\ \text{g mol}^{-1}\]</p>
<p><span class="box">Molecular mass of urea (from the isotonic data) = 59.99 &asymp; 60.0 g mol<sup>&minus;1</sup></span></p>
<p>Taking the paper's wording as given &mdash; 59.99 g mol<sup>&minus;1</sup> is the value calculated above and
60.06 g mol<sup>&minus;1</sup> the experimental (observed) value:</p>
<p>\[i = \frac{\text{calculated (normal) molar mass}}{\text{experimental (observed) molar mass}} = \frac{59.99}{60.06}
= 0.999 \approx 1\]</p>
<p><span class="box">\(i \approx 1\)</span> &mdash; urea neither dissociates nor associates in water.</p>
<p class="note">Strictly the roles are the other way round: 60.06 g mol<sup>&minus;1</sup> is the formula mass of
\(\ce{CO(NH2)2}\) (the normal value) and 59.99 g mol<sup>&minus;1</sup> is what the colligative (isotonic)
measurement gives (the observed value), so \(i = 60.06/59.99 = 1.001\). Either reading gives \(i \approx 1\).</p>""",
          topic="Solutions",
          recall=r"""<ul><li>Isotonic: \(\pi_1 = \pi_2\) &rArr; \(C_1 = C_2\) (same T, non-electrolytes).</li>
<li>\(i\) = normal / observed molar mass.</li></ul>"""),
        Q("6", 2, r"<p>How do you convert the following? (write chemical equation)</p><p>a) Phenol to picric acid</p>"
          r"<p>b) Propene to propan-1-ol</p>",
          a=r"""<p><b>(a)</b> Nitration with concentrated nitric acid (with conc. \(\ce{H2SO4}\)):</p>
<p>\[\ce{C6H5OH + 3HNO3 ->[\text{conc.} H2SO4] C6H2(NO2)3OH + 3H2O}\]</p>
<p>(2,4,6-trinitrophenol = picric acid; industrially phenol is first sulphonated to avoid oxidation, then
nitrated.)</p>
<p><b>(b)</b> Hydroboration&ndash;oxidation (anti-Markovnikov addition of water):</p>
<p>\[\ce{6CH3CH=CH2 + B2H6 -> 2(CH3CH2CH2)3B}\]</p>
<p>\[\ce{(CH3CH2CH2)3B + 3H2O2 ->[OH-] 3CH3CH2CH2OH + B(OH)3}\]</p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Acid-catalysed hydration of propene gives propan-2-ol (Markovnikov); hydroboration
gives propan-1-ol.</li><li>&ndash;OH activates o/p: three nitro groups enter.</li></ul>"""),
        Q("7", 2, r"<p>Conductivity of 0.00241 M acetic acid is 7.896 &times; 10<sup>&minus;5</sup> S cm<sup>&minus;1</sup>. "
          r"Calculate the dissociation constant of acetic acid. Given the molar conductivity of acetic acid at "
          r"infinite dilution is 390 S cm<sup>2</sup> mol<sup>&minus;1</sup>.</p>",
          a=r"""<p>\[\Lambda_m = \frac{\kappa\times1000}{C} = \frac{7.896\times10^{-5}\times1000}{0.00241}
= 32.76\ \text{S cm}^2\,\text{mol}^{-1}\]</p>
<p>\[\alpha = \frac{\Lambda_m}{\Lambda^\circ_m} = \frac{32.76}{390} = 0.0840\]</p>
<p>\[K_a = \frac{C\alpha^2}{1-\alpha} = \frac{0.00241\times(0.0840)^2}{1-0.0840} = 1.86\times10^{-5}\]</p>
<p><span class="box">\(K_a \approx 1.86\times10^{-5}\) mol L<sup>&minus;1</sup></span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\Lambda_m = 1000\kappa/C\); \(\alpha = \Lambda_m/\Lambda^\circ_m\);
\(K_a = C\alpha^2/(1-\alpha)\).</li></ul>"""),
        Q("8", 2, r"<p>(i) Cr<sup>2+</sup> is reducing but Mn<sup>3+</sup> is oxidizing agent when both have "
          r"d<sup>4</sup> configuration. Explain.</p>"
          r"<p>(ii) Why is copper considered as transition element but zinc is not?</p>",
          a=r"""<p><b>(i)</b> \(\ce{Cr^2+}\) (3d<sup>4</sup>) loses an electron to become \(\ce{Cr^3+}\) (3d<sup>3</sup>), which
has a stable half-filled \(t_{2g}^3\) set &mdash; so it readily gives electrons: a reducing agent
(\(E^\circ_{\ce{Cr^3+/Cr^2+}} = -0.41\) V). \(\ce{Mn^3+}\) (3d<sup>4</sup>) gains an electron to become \(\ce{Mn^2+}\)
(3d<sup>5</sup>), the extra-stable half-filled d<sup>5</sup> configuration &mdash; so it readily accepts electrons: an
oxidising agent (\(E^\circ_{\ce{Mn^3+/Mn^2+}} = +1.57\) V).</p>
<p><b>(ii)</b> A transition element has an incompletely filled d subshell in the atom or in a common ion.
Copper: Cu is 3d<sup>10</sup>4s<sup>1</sup> but its common ion \(\ce{Cu^2+}\) is 3d<sup>9</sup> &mdash; incomplete d
&rArr; transition element. Zinc: 3d<sup>10</sup> in the atom and in \(\ce{Zn^2+}\), its only ion &mdash; never an
incomplete d subshell &rArr; not a transition element.</p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Half-filled (d<sup>5</sup>, t<sub>2g</sub><sup>3</sup>) and full (d<sup>10</sup>)
configurations are extra stable; ions move towards them.</li></ul>"""),
        Q("9(i)", 2, r"<p>(i) State the IUPAC name of the main products formed when propanal is reacted with 2-methyl "
          r"propanal in the presence of dil. NaOH? Write the balanced chemical equation. Write the name of the "
          r"reaction also.</p>",
          a=r"""<p>Both aldehydes have &alpha;-hydrogen (propanal two, 2-methylpropanal one), so each can form a
carbanion (enolate) and each can be attacked: <b>cross aldol condensation</b> gives four &beta;-hydroxy
aldehydes.</p>
<table class="tbl"><tr><th>carbanion of &rarr; C=O of</th><th>product (IUPAC name)</th></tr>
<tr><td>propanal &rarr; propanal</td><td>\(\ce{CH3CH2CH(OH)CH(CH3)CHO}\)<br>3-hydroxy-2-methylpentanal</td></tr>
<tr><td>2-methylpropanal &rarr; 2-methylpropanal</td><td>\(\ce{(CH3)2CHCH(OH)C(CH3)2CHO}\)<br>3-hydroxy-2,2,4-trimethylpentanal</td></tr>
<tr><td>propanal &rarr; 2-methylpropanal</td><td>\(\ce{(CH3)2CHCH(OH)CH(CH3)CHO}\)<br>3-hydroxy-2,4-dimethylpentanal</td></tr>
<tr><td>2-methylpropanal &rarr; propanal</td><td>\(\ce{CH3CH2CH(OH)C(CH3)2CHO}\)<br>3-hydroxy-2,2-dimethylpentanal</td></tr></table>
<p>Cross product, e.g.:</p>
<p>\[\ce{CH3CH2CHO + (CH3)2CHCHO ->[\text{dil.} NaOH]}\]</p>
<p>\[\ce{(CH3)2CH-CH(OH)-CH(CH3)-CHO}\]</p>
<p>Name of reaction: <span class="box">cross aldol condensation (addition)</span></p>
<p>(On warming, the products with an &alpha;-H left can lose water to give &alpha;,&beta;-unsaturated aldehydes.)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Aldol: needs &alpha;-H; dil. NaOH forms a carbanion that adds to C=O of another
molecule &rarr; &beta;-hydroxy aldehyde.</li><li>Two different aldehydes, both with &alpha;-H &rarr; four products.</li></ul>"""),
        Q("9(ii) OR", 2, r"<p style='text-align:center'>OR</p><p>(ii) Write chemical equations to convert each of the "
          r"following:</p><p>a. acetaldehyde to acetamide</p><p>b. acetic acid to acetone</p>",
          a=r"""<p><b>(a)</b> Oxidise, then make the ammonium salt and heat:</p>
<p>\[\ce{CH3CHO ->[K2Cr2O7/H2SO4][{[O]}] CH3COOH}\]</p>
<p>\[\ce{CH3COOH + NH3 -> CH3COONH4 ->[\Delta] CH3CONH2 + H2O}\]</p>
<p><b>(b)</b> Calcium salt, then dry distillation:</p>
<p>\[\ce{2CH3COOH + Ca(OH)2 -> (CH3COO)2Ca + 2H2O}\]</p>
<p>\[\ce{(CH3COO)2Ca ->[\Delta] CH3COCH3 + CaCO3}\]</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Ammonium carboxylate &rarr; amide on heating (loss of H<sub>2</sub>O).</li>
<li>Calcium acetate, dry distilled &rarr; acetone.</li></ul>"""),
        Q("10", 2, r"<p>The rate constant of a first order reaction at T K is given by the following expression</p>"
          r"<p>\[\log k = \frac{-3163}{T} + 11.9\]</p>"
          r"<p>K is expressed in min<sup>&minus;1</sup>. What is the activation energy and half-life period of the "
          r"reaction at 20 <sup>o</sup>C?</p>",
          a=r"""<p>Compare with the Arrhenius equation in log form: \(\log k = \log A - \dfrac{E_a}{2.303RT}\).</p>
<p>\[\frac{E_a}{2.303R} = 3163 \;\Rightarrow\; E_a = 3163\times2.303\times8.314 = 6.06\times10^{4}\ \text{J mol}^{-1}\]</p>
<p><span class="box">\(E_a \approx 60.6\) kJ mol<sup>&minus;1</sup></span></p>
<p>At 20 &deg;C, T = 293 K: \(\log k = -\dfrac{3163}{293} + 11.9 = -10.795 + 11.9 = 1.105\)
&rArr; \(k = 12.7\) min<sup>&minus;1</sup>.</p>
<p>\[t_{1/2} = \frac{0.693}{k} = \frac{0.693}{12.7} = 0.0544\ \text{min}\]</p>
<p><span class="box">\(t_{1/2} \approx 5.4\times10^{-2}\) min (about 3.3 s)</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>\(\log k = \log A - \dfrac{E_a}{2.303RT}\): slope of log k vs 1/T is \(-E_a/2.303R\).</li>
<li>First order: \(t_{1/2} = 0.693/k\).</li></ul>"""),
        Q("11", 2, r"<p>Write the chemical equation for each of the following named organic reactions:</p>"
          + CARBYLAMINE_Q + r"<p>(ii) Sandmeyer reaction</p>",
          a=CARBYLAMINE_A + r"""<p><b>(ii) Sandmeyer reaction</b> &mdash; a diazonium salt with cuprous halide (or
cyanide) in the corresponding acid replaces &ndash;N<sub>2</sub><sup>+</sup> by Cl, Br or CN:</p>
<p>\[\ce{C6H5N2+Cl- ->[CuCl/HCl] C6H5Cl + N2 ^}\]</p>
<p>\[\ce{C6H5N2+Cl- ->[CuBr/HBr] C6H5Br + N2 ^}\]</p>
<p>\[\ce{C6H5N2+Cl- ->[CuCN/KCN] C6H5CN + N2 ^}\]</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Sandmeyer: Cu(I) salts; Gattermann: Cu powder + HX.</li>
<li>Carbylamine: 1&deg; amines only; foul-smelling isocyanide.</li></ul>"""),
        # ------------------------------------------------------------------ Section C
        SEC("Section- C (21 marks)"),
        Q("12", 3, r"<p>How will you convert the following? (Write chemical equations)</p>"
          r"<p>i) Diethyl ether from ethyl bromide.</p><p>ii) Phenol from chlorobenzene</p>"
          r"<p>iii) Propan-2-ol from ethanal</p>",
          a=r"""<p><b>(i)</b> Williamson synthesis:</p>
<p>\[\ce{C2H5OH + Na -> C2H5ONa + 1/2H2}\]</p>
<p>\[\ce{C2H5Br + C2H5ONa ->[\Delta] C2H5OC2H5 + NaBr}\]</p>
<p><b>(ii)</b> Dow's process:</p>
<p>\[\ce{C6H5Cl + 2NaOH ->[623 K][300 atm] C6H5ONa + NaCl + H2O}\]</p>
<p>\[\ce{C6H5ONa + HCl -> C6H5OH + NaCl}\]</p>
<p><b>(iii)</b> Grignard addition of a methyl group:</p>
<p>\[\ce{CH3CHO + CH3MgBr ->[dry ether] (CH3)2CHOMgBr}\]</p>
<p>\[\ce{(CH3)2CHOMgBr + H2O ->[H+] (CH3)2CHOH + Mg(OH)Br}\]</p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Williamson: RX (1&deg;) + R&prime;ONa &rarr; ROR&prime; (S<sub>N</sub>2).</li>
<li>Dow: chlorobenzene + NaOH at 623 K, 300 atm.</li><li>RMgX + aldehyde (not HCHO) &rarr; 2&deg; alcohol.</li></ul>"""),
        Q("13", 3, r"<p>(i) Complete and balance the following equations:</p>"
          r"<p>(a) KMnO<sub>4</sub> + H<sub>2</sub>C<sub>2</sub>O<sub>4</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; ______ + "
          r"______ + ______ + _______</p>"
          r"<p>(b) K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> + SO<sub>2</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; ______ + "
          r"______ + ______ + _______</p>"
          r"<p>(ii) Explain why the transition metal form complexes</p>",
          a=r"""<p><b>(i)(a)</b> \[\ce{2KMnO4 + 5H2C2O4 + 3H2SO4 -> K2SO4 + 2MnSO4 + 10CO2 + 8H2O}\]</p>
<p>(\(\ce{2MnO4- + 5C2O4^2- + 16H+ -> 2Mn^2+ + 10CO2 + 8H2O}\))</p>
<p><b>(b)</b> \[\ce{K2Cr2O7 + 3SO2 + H2SO4 -> K2SO4 + Cr2(SO4)3 + H2O}\]</p>
<p>(\(\ce{Cr2O7^2- + 3SO2 + 2H+ -> 2Cr^3+ + 3SO4^2- + H2O}\): orange &rarr; green.)</p>
<p><b>(ii)</b> Transition metal ions form complexes because they have:</p><ol>
<li><b>small size and high nuclear charge</b> (high charge density), so they strongly attract ligand lone pairs;</li>
<li><b>vacant d orbitals of suitable energy</b> ((n&minus;1)d, ns, np) that can accept electron pairs from ligands
and hybridise to give definite geometries;</li>
<li>variable oxidation states.</li></ol>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Acidic \(\ce{MnO4-}\): Mn +7 &rarr; +2 (5e<sup>&minus;</sup>); oxalate: C +3 &rarr; +4 (2e<sup>&minus;</sup> per
\(\ce{C2O4^2-}\)).</li><li>Acidic \(\ce{Cr2O7^2-}\): 6e<sup>&minus;</sup>; \(\ce{SO2}\) &rarr; \(\ce{SO4^2-}\): 2e<sup>&minus;</sup>.</li></ul>"""),
        Q("14", 3, r"<p>Write the structural formula of the major product formed in each of the following reactions.</p>"
          r"<p>i) \(\ce{CH3CH2OCH2CH3 ->[HI/373 K]}\)</p><p>ii) \(\ce{CH3CONH2 + Br2 ->[KOH]}\)</p>"
          r"<p>iii) \(\ce{C2H5Br + NH3 ->[C2H5OH/\Delta]}\)</p>",
          a=r"""<p><b>(i)</b> Ethers are cleaved by HI at 373 K: \(\ce{CH3CH2OCH2CH3 + HI -> CH3CH2I + CH3CH2OH}\);
with excess HI the ethanol is also converted, giving two molecules of iodoethane.</p>
<p><span class="box">\(\ce{CH3CH2-I}\) (iodoethane) [+ \(\ce{CH3CH2OH}\)]</span></p>
<p>\(\ce{CH3CH2OCH2CH3 + 2HI(excess) -> 2CH3CH2I + H2O}\)</p>
<p><b>(ii)</b> Hofmann bromamide degradation:
\(\ce{CH3CONH2 + Br2 + 4KOH -> CH3NH2 + K2CO3 + 2KBr + 2H2O}\)</p>
<p><span class="box">\(\ce{CH3-NH2}\) (methanamine)</span></p>
<p><b>(iii)</b> Ammonolysis (sealed tube, ethanolic \(\ce{NH3}\), excess ammonia):
\(\ce{C2H5Br + NH3 -> C2H5NH3+Br- ->[NH3] C2H5NH2 + NH4Br}\)</p>
<p><span class="box">\(\ce{CH3CH2-NH2}\) (ethanamine)</span> &mdash; with excess \(\ce{C2H5Br}\) the 2&deg;, 3&deg; amines and
the quaternary salt also form.</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Ether + HI: C&ndash;O cleavage (S<sub>N</sub>2 by I<sup>&minus;</sup>).</li>
<li>Hofmann: amide &rarr; amine with one C less. Ammonolysis: excess NH<sub>3</sub> favours the 1&deg; amine.</li></ul>"""),
        Q("15", 3, r"<p>i) Which vitamin deficiencies are responsible for Rickets and scurvy?</p>"
          r"<p>ii) Name the nitrogen bases present in DNA.</p><p>iii) Why NaCl is used to clear snow on roads?</p>",
          a=r"""<p><b>(i)</b> Rickets &mdash; <b>vitamin D</b>; scurvy &mdash; <b>vitamin C</b> (ascorbic acid).</p>
<p><b>(ii)</b> Adenine (A) and guanine (G) &mdash; purines; cytosine (C) and thymine (T) &mdash; pyrimidines.</p>
<p><b>(iii)</b> NaCl dissolves in the thin film of water on ice to form a solution whose <b>freezing point is
lower</b> than 0 &deg;C (depression of freezing point, \(\Delta T_f = iK_fm\), with \(i \approx 2\)). At the
prevailing temperature the ice cannot remain frozen, so it melts and the road is cleared.</p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>DNA: A, G, C, T (RNA has U in place of T).</li>
<li>Colligative: depression of freezing point.</li></ul>"""),
        Q("16(i)", 3, r"<p>(i) (a) A cell is prepared by dipping copper rod in 1 M copper sulphate solution and zinc rod "
          r"in 1 M zinc sulphate solution. The standard reduction potential of copper and zinc are 0.34 V and "
          r"&ndash;0.76 V respectively. Write the cell reaction and calculate the standard free energy change of the "
          r"reaction.</p><p>(b) What is the role of salt-bridge in a galvanic cell?</p>",
          a=r"""<p><b>(a)</b> Zn (lower E&deg;) is the anode, Cu the cathode.</p>
<p>Anode: \(\ce{Zn -> Zn^2+ + 2e-}\); cathode: \(\ce{Cu^2+ + 2e- -> Cu}\).</p>
<p>Cell reaction: <span class="box">\(\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}\)</span></p>
<p>\(E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode} = 0.34 - (-0.76) = 1.10\) V.</p>
<p>\[\Delta G^\circ = -nFE^\circ_\text{cell} = -2\times96500\times1.10 = -2.123\times10^{5}\ \text{J mol}^{-1}\]</p>
<p><span class="box">\(\Delta G^\circ = -212.3\) kJ mol<sup>&minus;1</sup></span></p>
{{fig:0}}
<p><b>(b) Role of the salt bridge:</b></p>""" + SALT_BRIDGE,
          afig=[(fg.fig_s2_daniell, "Daniell cell: Zn | ZnSO₄(1 M) || CuSO₄(1 M) | Cu")],
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\Delta G^\circ = -nFE^\circ_\text{cell}\), F = 96500 C mol<sup>&minus;1</sup>.</li>
<li>Anode: oxidation (&minus; in a galvanic cell); cathode: reduction (+).</li></ul>"""),
        Q("16(ii) OR", 3, r"<p style='text-align:center'>OR</p><p>(ii) a) A solution of Ni(NO<sub>3</sub>)<sub>2</sub> is "
          r"electrolyzed between platinum electrodes. How many moles of Ni will be deposited at the cathode if 5 "
          r"amperes of electricity are passed for 2 hours?</p>"
          r"<p>b) Write the anode and cathode reaction occurring in a lead storage battery during discharging of cell.</p>",
          a=r"""<p><b>(a)</b> \(Q = It = 5\ \text{A}\times(2\times3600)\ \text{s} = 36000\) C.</p>
<p>\(\ce{Ni^2+ + 2e- -> Ni}\): 2 F (= 2 &times; 96500 C) deposit 1 mol Ni.</p>
<p>\[n(\ce{Ni}) = \frac{36000}{2\times96500} = 0.187\ \text{mol}\]</p>
<p><span class="box">0.187 mol Ni (&asymp; 10.9 g)</span></p>
<p><b>(b)</b> Discharging (galvanic action), electrolyte dil. \(\ce{H2SO4}\):</p>
<p>Anode (&minus;, Pb): \(\ce{Pb(s) + SO4^2-(aq) -> PbSO4(s) + 2e-}\)</p>
<p>Cathode (+, PbO<sub>2</sub>): \(\ce{PbO2(s) + SO4^2-(aq) + 4H+(aq) + 2e- -> PbSO4(s) + 2H2O(l)}\)</p>
<p>Overall: \(\ce{Pb + PbO2 + 2H2SO4 -> 2PbSO4 + 2H2O}\)</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Moles deposited \(= \dfrac{It}{nF}\).</li>
<li>Lead accumulator: both electrodes become \(\ce{PbSO4}\) on discharge; acid density falls.</li></ul>"""),
        Q("17", 3, r"<p>i) The rate constant of a reaction is found to be 3 &times; 10<sup>&minus;3</sup> mol<sup>&minus;2</sup> "
          r"L<sup>2</sup> sec<sup>&minus;1</sup>. What is the order of the reaction?</p>"
          r"<p>ii) If the activation energy of a reaction is zero, will the rate constant of the reaction depend upon "
          r"temperature? Give reason.</p>"
          r"<p>iii) Rate of a reaction can be expressed by following rate expression, Rate = k[A]<sup>2</sup>[B]. If "
          r"concentration of A is increased by 3 times and concentration of B is increased by 2 times, by how many "
          r"times rate of reaction increases?</p>",
          a=r"""<p><b>(i)</b> Units of k = (mol L<sup>&minus;1</sup>)<sup>1&minus;n</sup> s<sup>&minus;1</sup>. Here
(mol L<sup>&minus;1</sup>)<sup>&minus;2</sup> s<sup>&minus;1</sup> &rArr; \(1-n = -2\) &rArr;
<span class="box">third order</span></p>
<p><b>(ii)</b> <b>No.</b> \(k = Ae^{-E_a/RT}\); with \(E_a = 0\), \(e^{0} = 1\) and \(k = A\), which is (to this
approximation) independent of temperature. Every collision with proper orientation would be effective
regardless of temperature.</p>
<p><b>(iii)</b> \(\text{Rate}_2 = k(3[\mathrm A])^2(2[\mathrm B]) = 9\times2\,k[\mathrm A]^2[\mathrm B]\).</p>
<p><span class="box">The rate becomes 18 times</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Units of k: (mol L<sup>&minus;1</sup>)<sup>1&minus;n</sup> s<sup>&minus;1</sup>.</li>
<li>Arrhenius \(k = Ae^{-E_a/RT}\).</li></ul>"""),
        Q("18", 3, r"<p>Identify the compounds [A], [B] and [C] in the following reactions.</p>"
          r"<p>i) \(\ce{C6H5NO2 ->[Fe/HCl] A ->[NaNO2 + HCl][\text{0–5 °C}] B ->[KI] C}\)</p>"
          r"<p>ii) \(\ce{C6H5N2+Cl- ->[CuCN/\Delta] A ->[H2O/H+] B ->[NH3][\Delta] C}\)</p>",
          a=r"""<p><b>(i)</b> <span class="box">A = aniline; B = benzenediazonium chloride; C = iodobenzene</span></p>
<p>\(\ce{C6H5NO2 + 6[H] ->[Fe/HCl] C6H5NH2 + 2H2O}\)</p>
<p>\(\ce{C6H5NH2 + NaNO2 + 2HCl ->[273-278 K] C6H5N2+Cl- + NaCl + 2H2O}\)</p>
<p>\(\ce{C6H5N2+Cl- + KI -> C6H5I + KCl + N2 ^}\)</p>
<p><b>(ii)</b> <span class="box">A = benzonitrile; B = benzoic acid; C = benzamide</span></p>
<p>\(\ce{C6H5N2+Cl- ->[CuCN/KCN][\Delta] C6H5CN + N2}\) (Sandmeyer)</p>
<p>\(\ce{C6H5CN + 2H2O + H+ -> C6H5COOH + NH4+}\)</p>
<p>\(\ce{C6H5COOH + NH3 -> C6H5COONH4 ->[\Delta] C6H5CONH2 + H2O}\)</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>&ndash;N<sub>2</sub><sup>+</sup> replaced by I with KI (no catalyst), by CN with CuCN.</li>
<li>Nitrile &rarr; acid (hydrolysis) &rarr; ammonium salt &rarr; amide (heat).</li></ul>"""),
        # ------------------------------------------------------------------ Section D
        SEC("Section- D (15 marks)"),
        Q("19", 5, r"<p>i) What happens when (Give chemical equations):</p>"
          r"<p>a) Benzaldehyde on treatment with HCN and then hydrolysed.<br>b) Formaldehyde undergoes Cannizaro "
          r"reaction.<br>c) Acetic acid reacts with ethanol in presence of conc. H<sub>2</sub>SO<sub>4</sub>.</p>"
          r"<p>ii) A ketone A (C<sub>4</sub>H<sub>8</sub>O) which undergoes a haloform reaction, gives compound B on "
          r"reduction. B on heating with conc. sulphuric acid at 170 <sup>o</sup>C gives a compound C which on "
          r"treatment with O<sub>3</sub> and Zn/H<sub>2</sub>O gives a compound D. Identify A, B, C and D.</p>",
          a=r"""<p><b>(i)(a)</b> Nucleophilic addition of HCN gives benzaldehyde cyanohydrin; acid hydrolysis converts
&ndash;CN to &ndash;COOH, giving <b>mandelic acid</b> (2-hydroxy-2-phenylethanoic acid):</p>
<p>\[\ce{C6H5CHO + HCN -> C6H5CH(OH)CN ->[H3O+] C6H5CH(OH)COOH}\]</p>
<p><b>(b)</b> HCHO has no &alpha;-H; with conc. NaOH one molecule is oxidised and one reduced:</p>
<p>\[\ce{2HCHO + NaOH(\text{conc.}) -> CH3OH + HCOONa}\]</p>
<p><b>(c)</b> Esterification &mdash; ethyl acetate (fruity smell):</p>
<p>\[\ce{CH3COOH + C2H5OH <=>[\text{conc.} H2SO4] CH3COOC2H5 + H2O}\]</p>
<p><b>(ii)</b> \(\ce{C4H8O}\) ketone giving the haloform test must contain \(\ce{CH3CO-}\): butan-2-one.</p>
<table class="tbl"><tr><td>A</td><td>butan-2-one, \(\ce{CH3COCH2CH3}\)</td></tr>
<tr><td>B</td><td>butan-2-ol, \(\ce{CH3CH(OH)CH2CH3}\)</td></tr>
<tr><td>C</td><td>but-2-ene, \(\ce{CH3CH=CHCH3}\) (major, Saytzeff)</td></tr>
<tr><td>D</td><td>ethanal, \(\ce{CH3CHO}\) (two molecules)</td></tr></table>
<p>\(\ce{CH3COCH2CH3 + 3I2 + 4NaOH -> CHI3 + CH3CH2COONa + 3NaI + 3H2O}\) (haloform)</p>
<p>\(\ce{CH3COCH2CH3 ->[NaBH4 \text{ or } H2/Ni] CH3CH(OH)CH2CH3}\)</p>
<p>\(\ce{CH3CH(OH)CH2CH3 ->[\text{conc.} H2SO4][443 K] CH3CH=CHCH3 + H2O}\)</p>
<p>\(\ce{CH3CH=CHCH3 ->[1. O3][2. Zn/H2O] 2CH3CHO}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Haloform: \(\ce{CH3CO-}\) group; Cannizzaro: no &alpha;-H, conc. alkali.</li>
<li>Saytzeff: the more substituted alkene is major. Ozonolysis splits C=C into two C=O.</li></ul>"""),
        Q("20", 5, r"<p>i) What would be the molar mass of compound if 6.21 g of it is dissolved in 24.0 g of "
          r"CHCl<sub>3</sub> to from a solution that has a boiling point of 68.04&deg;C. The boiling point of pure "
          r"chloroform is 61.7&deg;C and the boiling point elevation constant K<sub>b</sub> for chloroform is "
          r"3.63&deg;C/m.</p>"
          r"<p>ii) A 0.15 M aqueous solution of KCl exerts an osmotic pressure of 6.8 atm at 310 K. Calculate the "
          r"van't Hoff factor.</p>"
          r"<p>iii) Given below is the decreasing order of depression in freezing point of water observed for the "
          r"following solutions.</p><p style='text-align:center'>0.1 molal urea &gt; 0.1 molal NaCl &gt; 0.1 molal "
          r"MgCl<sub>2</sub>.</p><p>Provide a reason to explain if the above ordered arrangement is correct or not</p>"
          r"<p>iv) Which colligative property is preferred for the molar mass determination of macromolecules? "
          r"Give reasons.</p>",
          a=r"""<p><b>(i)</b> \(\Delta T_b = 68.04 - 61.7 = 6.34\) &deg;C.</p>
<p>\[M_B = \frac{K_b\times w_B\times1000}{\Delta T_b\times w_A} = \frac{3.63\times6.21\times1000}{6.34\times24.0}
= 148\ \text{g mol}^{-1}\]</p>
<p><span class="box">\(M \approx 148\) g mol<sup>&minus;1</sup></span></p>
<p><b>(ii)</b> \[\pi = iCRT \Rightarrow i = \frac{\pi}{CRT} = \frac{6.8}{0.15\times0.0821\times310} = 1.78\]</p>
<p><span class="box">\(i \approx 1.78\)</span> (KCl is about 78% dissociated)</p>
<p><b>(iii)</b> <b>Not correct.</b> \(\Delta T_f = iK_fm\); at the same molality it depends on \(i\): urea
\(i = 1\), NaCl \(i \approx 2\), \(\ce{MgCl2}\) \(i \approx 3\). The correct decreasing order is</p>
<p><span class="box">0.1 m MgCl<sub>2</sub> &gt; 0.1 m NaCl &gt; 0.1 m urea</span> &mdash; the given order is
reversed.</p>
<p><b>(iv)</b> <b>Osmotic pressure.</b></p><ul>
<li>Even very dilute solutions of a macromolecule give an osmotic pressure large enough to measure accurately,
whereas \(\Delta T_b\) and \(\Delta T_f\) would be tiny (fractions of a millikelvin).</li>
<li>It is measured at room temperature, so heat-sensitive biomolecules (proteins, polymers) are not
denatured or decomposed.</li>
<li>Molarity is used, not molality, and the solution need not be heated or cooled.</li></ul>""",
          topic="Solutions",
          recall=r"""<ul><li>\(M_B = \dfrac{1000K_bw_B}{\Delta T_bw_A}\).</li><li>\(\pi = iCRT\); \(\Delta T_f = iK_fm\).</li></ul>"""),
        Q("21(i)", 5, r"<p>i. a) [Co(NH<sub>3</sub>)<sub>6</sub>]<sup>3+</sup> is an inner orbital complex whereas "
          r"[Ni(NH<sub>3</sub>)<sub>6</sub>]<sup>2+</sup> is an outer orbital complex. Explain.</p>"
          r"<p>b) [Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>3+</sup> is strongly paramagnetic while "
          r"[Fe(CN)<sub>6</sub>]<sup>3&minus;</sup> is weakly paramagnetic. Explain.</p>"
          r"<p>c) Arrange the following complexes on the basis of their increasing order of conductivity in the "
          r"solution: [Co(NH<sub>3</sub>)<sub>4</sub>Cl<sub>2</sub>]Cl, [Co(NH<sub>3</sub>)<sub>3</sub>Cl<sub>3</sub>], "
          r"[Co(en)<sub>3</sub>]Cl<sub>3</sub>, [Co(NH<sub>3</sub>)<sub>5</sub>Cl]Cl<sub>2</sub>.</p>"
          r"<p>d) CoClSO<sub>4</sub>.5NH<sub>3</sub> exists in two isomeric forms &lsquo;A&rsquo; and &lsquo;B&rsquo;. "
          r"Isomer A reacts with AgNO<sub>3</sub> to give white precipitate, but it does not react with "
          r"BaCl<sub>2</sub>. Isomer B gives white precipitate with BaCl<sub>2</sub> but does not react with "
          r"AgNO<sub>3</sub>. Answer the following questions:<br>1) Identify A and B<br>2) Name the type of "
          r"isomerism involved.</p>",
          a=r"""<p><b>(a)</b> \(\ce{Co^3+}\) is 3d<sup>6</sup>. Towards the highly charged \(\ce{Co^3+}\), \(\ce{NH3}\) acts as a
strong-field ligand: the six d electrons pair into three 3d orbitals, leaving two inner 3d orbitals empty &rArr;
<b>d<sup>2</sup>sp<sup>3</sup></b> (inner orbital, low spin, diamagnetic). \(\ce{Ni^2+}\) is 3d<sup>8</sup>: even after
pairing, only one 3d orbital could be emptied, so two inner d orbitals are never available; the outer 4d orbitals
are used &rArr; <b>sp<sup>3</sup>d<sup>2</sup></b> (outer orbital, two unpaired electrons, paramagnetic).</p>
{{fig:0}}
<p><b>(b)</b> \(\ce{Fe^3+}\) is 3d<sup>5</sup>. \(\ce{H2O}\) is a weak-field ligand (\(\Delta_o < P\)): configuration
\(t_{2g}^3e_g^2\), five unpaired electrons, \(\mu \approx 5.92\) BM &rArr; strongly paramagnetic. \(\ce{CN-}\) is a
strong-field ligand (\(\Delta_o > P\)): electrons pair in \(t_{2g}\), giving \(t_{2g}^5e_g^0\), one unpaired electron,
\(\mu \approx 1.73\) BM &rArr; weakly paramagnetic.</p>
{{fig:1}}
<p><b>(c)</b> Conductivity rises with the number of ions per formula unit:</p>
<table class="tbl"><tr><th>complex</th><th>ions in solution</th></tr>
<tr><td>\(\ce{[Co(NH3)3Cl3]}\)</td><td>0 (non-electrolyte)</td></tr>
<tr><td>\(\ce{[Co(NH3)4Cl2]Cl}\)</td><td>2</td></tr>
<tr><td>\(\ce{[Co(NH3)5Cl]Cl2}\)</td><td>3</td></tr>
<tr><td>\(\ce{[Co(en)3]Cl3}\)</td><td>4</td></tr></table>
<p><span class="box">[Co(NH<sub>3</sub>)<sub>3</sub>Cl<sub>3</sub>] &lt; [Co(NH<sub>3</sub>)<sub>4</sub>Cl<sub>2</sub>]Cl
&lt; [Co(NH<sub>3</sub>)<sub>5</sub>Cl]Cl<sub>2</sub> &lt; [Co(en)<sub>3</sub>]Cl<sub>3</sub></span></p>
<p><b>(d)1.</b> A gives AgCl, so \(\ce{Cl-}\) is the counter ion and sulphate is coordinated;
B gives \(\ce{BaSO4}\), so sulphate is the counter ion.</p>
<p><span class="box">A = \(\ce{[Co(NH3)5(SO4)]Cl}\); B = \(\ce{[Co(NH3)5Cl]SO4}\)</span></p>
<p>\(\ce{[Co(NH3)5SO4]Cl + AgNO3 -> [Co(NH3)5SO4]NO3 + AgCl v}\);
\(\ce{[Co(NH3)5Cl]SO4 + BaCl2 -> [Co(NH3)5Cl]Cl2 + BaSO4 v}\)</p>
<p><b>(d)2.</b> <span class="box">Ionisation isomerism</span> &mdash; same formula, different ions in solution.</p>""",
          afig=[fg.fig_s2_vbt_co_ni, fg.fig_s2_fe_cft],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Inner orbital (d<sup>2</sup>sp<sup>3</sup>) needs two empty (n&minus;1)d orbitals; outer
orbital (sp<sup>3</sup>d<sup>2</sup>) uses nd.</li>
<li>Weak field: \(\Delta_o < P\), high spin; strong field: \(\Delta_o > P\), low spin.</li>
<li>Ionisation isomers exchange a ligand with a counter ion.</li></ul>"""),
        Q("21(ii) OR", 5, r"<p style='text-align:center'>OR</p><p>ii) a) For the complex compound "
          r"NiCl<sub>4</sub><sup>2&minus;</sup> write:<br>1) IUPAC name<br>2) Hybridisation of the central atom.<br>"
          r"3) Shape of the complex<br>4) State whether it is high-spin or low-spin complex</p>"
          r"<p>b) Draw the structures of optical isomers [Co(en)<sub>3</sub>]<sup>3+</sup></p>"
          r"<p>c) Give the electronic configuration of the following complexes on the basis of crystal field theory "
          r"and identify the diamagnetic species among them.<br>[CoF<sub>6</sub>]<sup>3&minus;</sup>, "
          r"[Cr(NH<sub>3</sub>)<sub>6</sub>]<sup>3+</sup>, [Cu(CN)<sub>6</sub>]<sup>5&minus;</sup></p>",
          a=r"""<p><b>(a)</b> \(\ce{[NiCl4]^2-}\): Ni is +2 (3d<sup>8</sup>); \(\ce{Cl-}\) is weak field, so no pairing.</p>
<ol><li>IUPAC name: <span class="box">tetrachloridonickelate(II) ion</span></li>
<li>Hybridisation: <b>sp<sup>3</sup></b></li><li>Shape: <b>tetrahedral</b></li>
<li><b>High-spin</b> (two unpaired electrons, paramagnetic; \(\Delta_t\) is small, \(\Delta_t \approx \frac49\Delta_o\), so
tetrahedral complexes are always high spin).</li></ol>
{{fig:0}}
<p><b>(b)</b> \(\ce{[Co(en)3]^3+}\) is octahedral with three bidentate en ligands arranged like a propeller; the
two forms are non-superimposable mirror images (enantiomers), the d- and l-forms, which rotate plane-polarised
light equally in opposite directions:</p>
{{fig:1}}
<p><b>(c)</b></p>
<table class="tbl"><tr><th>complex</th><th>metal ion</th><th>ligand field</th><th>CFT configuration</th><th>unpaired</th></tr>
<tr><td>\(\ce{[CoF6]^3-}\)</td><td>Co<sup>3+</sup>, d<sup>6</sup></td><td>weak (F<sup>&minus;</sup>), high spin</td>
<td>\(t_{2g}^4e_g^2\)</td><td>4 (paramagnetic)</td></tr>
<tr><td>\(\ce{[Cr(NH3)6]^3+}\)</td><td>Cr<sup>3+</sup>, d<sup>3</sup></td><td>&mdash;</td><td>\(t_{2g}^3e_g^0\)</td><td>3 (paramagnetic)</td></tr>
<tr><td>\(\ce{[Cu(CN)6]^5-}\)</td><td>Cu<sup>+</sup>, d<sup>10</sup></td><td>&mdash;</td><td>\(t_{2g}^6e_g^4\)</td><td>0</td></tr></table>
{{fig:2}}
<p><span class="box">Diamagnetic: [Cu(CN)<sub>6</sub>]<sup>5&minus;</sup></span> (Cu oxidation state: \(x - 6 = -5\)
&rArr; +1, d<sup>10</sup>).</p>
<p class="note">[Cu(CN)<sub>6</sub>]<sup>5&minus;</sup> is not a known species &mdash; copper(I) forms
[Cu(CN)<sub>4</sub>]<sup>3&minus;</sup> (tetrahedral) &mdash; but the conclusion is the same for any Cu(I) complex:
d<sup>10</sup>, all electrons paired, diamagnetic. Answered as set.</p>""",
          afig=[fg.fig_s2_nicl4_vbt, fg.fig_s2_co_en3_optical, fg.fig_s2_cft_three],
          topic="Coordination Compounds",
          recall=r"""<ul><li>d<sup>1</sup>&ndash;d<sup>3</sup> and d<sup>8</sup>&ndash;d<sup>10</sup> have the same
configuration in weak and strong fields; d<sup>4</sup>&ndash;d<sup>7</sup> depend on \(\Delta_o\) vs P.</li>
<li>[M(AA)<sub>3</sub>] octahedral chelates are chiral: d and l forms.</li></ul>"""),
    ])
