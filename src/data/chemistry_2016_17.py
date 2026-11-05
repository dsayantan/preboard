"""Heritage School Pre-Board 2016-17, Chemistry (Class XII) -- scanned paper, transcribed from the
page images (the OCR in Chemistry/OCR/heritage-2016-17-preboard.txt was only a starting point)."""
from kit import Q, SEC
import chemistry_2016_17_figs as fg

FILL = (r"<p><b>Fill in the blanks with appropriate words given below:</b> [Greater, lesser, nitric acid, "
        r"nitrous acid, common ion effect, salt hydrolysis, decreased, increased, does not change, acidic, "
        r"basic, neutral, PCl<sub>5</sub>, SOCl<sub>2</sub>, methyl cyanide, primary amine, vapour, "
        r"vapourpressure, positive, negative]</p>")
MATCH = (r"<p><b>Match the following:</b></p><table class='tbl'><tr><th colspan='2'>A</th>"
         r"<th colspan='2'>B</th></tr>"
         r"<tr><td>i)</td><td>Nernst equation</td><td>a)</td><td>Glycine</td></tr>"
         r"<tr><td>ii)</td><td>Ostwald's dilution law</td><td>b)</td><td>Ammonia</td></tr>"
         r"<tr><td>iii)</td><td>Lewis base</td><td>c)</td><td>Amine</td></tr>"
         r"<tr><td>iv)</td><td>Zwitter ion</td><td>d)</td><td>Electrode potential</td></tr>"
         r"<tr><td>v)</td><td>Hinsberg's reagent</td><td>e)</td><td>Weak electrolyte</td></tr></table>")
EXPL = r"<p><b>Explain the following facts in brief:</b></p>"
MCQ = r"<p><b>Choose the correct answer from the alternatives given:</b></p>"

PAPER = dict(
    subject="chemistry",
    year="2016-17",
    slug="2016-17",
    paper="Chemistry (Theory)",
    source="PreBoard-PYQ/2016-17/CHEMISTRY.pdf",
    marks=70, time="3 hours",
    intro=r"""<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT
start writing during this time.)</p>
<p>Answer all questions in <b>Part I</b> and six from <b>Part II</b>.</p>
<p>All working, including rough work, should be done on the same sheet as and adjacent to, the rest of
the answer.</p>
<p>The intended marks for questions or parts of questions are given in brackets [ ].</p>
<p>Balanced equations must be given wherever possible and diagrams where they are helpful.</p>
<p>When solving numerical problems, all essential working must be shown. In working out problems, use
the following data: Gas constant R = 1.987 cal deg<sup>&minus;1</sup> mol<sup>&minus;1</sup> = 0.0821
dm<sup>3</sup> atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>. 1 L atm = 1 dm<sup>3</sup> atm.</p>""",
    items=[
        SEC("Part I", "(Answer all questions)"),
        # ------------------------------------------------------------ 1(a)
        Q("1(a)(i)", 1, FILL + r"<p>i) Solubility of Calcium oxalate is ________ in the presence of ammonium "
          r"oxalate because of ________.</p>",
          excluded="Common-ion effect on solubility (ionic equilibrium, solubility product) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("1(a)(ii)", 1, FILL + r"<p>ii) Ethanol is ________ to litmus while phenol is ________ to litmus.</p>",
          a=r"""<p>Ethanol is <b>neutral</b> to litmus while phenol is <b>acidic</b> to litmus.</p>
<p>Phenol ionises slightly in water, \(\ce{C6H5OH + H2O <=> C6H5O- + H3O+}\), because the phenoxide ion is
stabilised by resonance; ethanol (\(\mathrm{p}K_a\approx16\)) does not ionise appreciably.</p>
<p><span class="box">neutral; acidic</span></p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Acid strength: carboxylic acid &gt; phenol &gt; water &gt; alcohol.</li>
<li>Phenoxide is resonance-stabilised; alkoxide is destabilised by the +I alkyl group.</li></ul>"""),
        Q("1(a)(iii)", 1, FILL + r"<p>iii) The ________ pressure of an aqueous solution of 0.1(M) cane sugar is "
          r"________ than that of pure water measured at the same temperature.</p>",
          a=r"""<p>The <b>vapour</b> pressure of an aqueous solution of 0.1 M cane sugar is <b>lesser</b> than that
of pure water at the same temperature.</p>
<p>The non-volatile solute occupies part of the surface, so fewer solvent molecules escape (Raoult's law,
\(p = x_{\text{solvent}}\,p^\circ\)).</p>
<p><span class="box">vapour; lesser</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>Relative lowering of vapour pressure \(\dfrac{p^\circ - p}{p^\circ} = x_{\text{solute}}\).</li></ul>"""),
        Q("1(a)(iv)", 1, FILL + r"<p>iv) On treating a ________ with ________ nitrogen gas is evolved.</p>",
          a=r"""<p>On treating a <b>primary amine</b> with <b>nitrous acid</b>, nitrogen gas is evolved.</p>
<p>\(\ce{CH3NH2 + HNO2 -> CH3OH + N2 ^ + H2O}\)</p>
<p><span class="box">primary amine; nitrous acid</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>\(\ce{HNO2}\) from \(\ce{NaNO2 + HCl}\); aliphatic 1&deg; amines evolve \(\ce{N2}\),
2&deg; amines give yellow nitrosamines, 3&deg; form soluble nitrites.</li></ul>"""),
        Q("1(a)(v)", 1, FILL + r"<p>v) The more ________ the reduction potential of a metal, the ________ is its "
          r"ability to displace hydrogen from acids.</p>",
          a=r"""<p>The more <b>negative</b> the reduction potential of a metal, the <b>greater</b> is its ability
to displace hydrogen from acids.</p>
<p>A metal with \(E^\circ &lt; 0\) (below hydrogen in the electrochemical series, e.g. Zn, &minus;0.76 V) is
oxidised by \(\ce{H+}\): \(\ce{Zn + 2H+ -> Zn^2+ + H2}\).</p>
<p><span class="box">negative; greater</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Electrochemical series: lower \(E^\circ_{red}\) &rArr; stronger reducing agent.</li>
<li>\(E^\circ(\ce{H+/H2}) = 0\) by definition (SHE).</li></ul>"""),
        # ------------------------------------------------------------ 1(b)
        Q("1(b)(i)", 1, MATCH + r"<p>Match (i) Nernst equation.</p>",
          a=r"""<p>(i) Nernst equation &rarr; <b>(d) Electrode potential</b>.</p>
<p>It gives the electrode potential at any concentration:
\(E = E^\circ - \dfrac{0.0591}{n}\log\dfrac{1}{[\ce{M^{n+}}]}\) at 298 K.</p>
<p><span class="box">(i) &ndash; (d)</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Nernst: \(E = E^\circ - \dfrac{2.303RT}{nF}\log Q\).</li></ul>"""),
        Q("1(b)(ii)", 1, MATCH + r"<p>Match (ii) Ostwald's dilution law.</p>",
          excluded="Ostwald's dilution law (degree of ionisation of weak electrolytes, ionic equilibrium) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("1(b)(iii)", 1, MATCH + r"<p>Match (iii) Lewis base.</p>",
          excluded="Lewis acid–base concept &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("1(b)(iv)", 1, MATCH + r"<p>Match (iv) Zwitter ion.</p>",
          a=r"""<p>(iv) Zwitter ion &rarr; <b>(a) Glycine</b>: \(\ce{H3N+-CH2-COO-}\).</p>
<p><span class="box">(iv) &ndash; (a)</span></p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>A zwitter ion carries both + and &minus; charges; net charge zero at the isoelectric point.</li></ul>"""),
        Q("1(b)(v)", 1, MATCH + r"<p>Match (v) Hinsberg's reagent.</p>",
          a=r"""<p>(v) Hinsberg's reagent (benzenesulphonyl chloride) &rarr; <b>(c) Amine</b> &mdash; used to
distinguish 1&deg;, 2&deg; and 3&deg; amines.</p>
<p><span class="box">(v) &ndash; (c)</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>1&deg;: sulphonamide soluble in alkali; 2&deg;: insoluble; 3&deg;: no reaction.</li></ul>"""),
        # ------------------------------------------------------------ 1(c)
        Q("1(c)(i)", 1, EXPL + r"<p>(i) Unlike most phenolic compounds, 2,4,6-trinitrophenol is soluble in "
          r"sodium bicarbonate solution.</p>",
          a=r"""<p>The three &ndash;NO<sub>2</sub> groups at the o- and p-positions withdraw electrons (&minus;I and
&minus;R) and delocalise the negative charge of the picrate ion, so 2,4,6-trinitrophenol (picric acid,
p<i>K</i><sub>a</sub> &asymp; 0.4) is a stronger acid than carbonic acid (p<i>K</i><sub>a</sub> 6.4). It therefore
decomposes \(\ce{NaHCO3}\) with effervescence and dissolves; ordinary phenol (p<i>K</i><sub>a</sub> 10) is weaker
than carbonic acid and cannot.</p>
<p>\(\ce{C6H2(NO2)3OH + NaHCO3 -> C6H2(NO2)3ONa + H2O + CO2 ^}\)</p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Electron-withdrawing groups at o/p increase the acidity of phenol; electron-releasing
groups decrease it.</li>
<li>An acid stronger than \(\ce{H2CO3}\) liberates \(\ce{CO2}\) from bicarbonate.</li></ul>"""),
        Q("1(c)(ii)", 1, EXPL + r"<p>(ii) Specific conductance of a solution decreases with dilution.</p>",
          a=r"""<p>Specific conductance is the conductance of 1 cm<sup>3</sup> of solution. On dilution the number of
ions present per cm<sup>3</sup> decreases (although the degree of ionisation rises), so fewer ions carry current
in that unit volume and \(\kappa\) falls. (Molar conductance, by contrast, increases.)</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\kappa\) depends on ions per unit volume; \(\Lambda_m = \kappa\times1000/M\) increases with dilution.</li></ul>"""),
        Q("1(c)(iii)", 1, EXPL + r"<p>(iii) Transition metals form complex compounds.</p>",
          a=r"""<ul><li>Their ions are small and highly charged (high charge density), so they strongly attract
ligands.</li>
<li>They have vacant (n&minus;1)d (and ns, np) orbitals of suitable energy which can accept lone pairs
from ligands to form coordinate bonds.</li></ul>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Complex formation, colour, paramagnetism, variable valency and catalysis all stem
from the partly filled d subshell.</li></ul>"""),
        Q("1(c)(iv)", 1, EXPL + r"<p>(iv) Interhalogen compounds are more reactive than their constituent elements.</p>",
          excluded="Interhalogen compounds (p-block, group 17) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("1(c)(v)", 1, EXPL + r"<p>(v) Zinc sulphide is precipitated from an ammoniacal solution in presence of "
          r"hydrogen sulphide.</p>",
          a=r"""<p>\(\ce{H2S}\) is a weak acid: \(\ce{H2S <=> 2H+ + S^2-}\). In ammoniacal (basic) solution the
\(\ce{OH-}\) ions remove \(\ce{H+}\), so the ionisation of \(\ce{H2S}\) increases and [\(\ce{S^2-}\)] becomes
high. The ionic product [\(\ce{Zn^2+}\)][\(\ce{S^2-}\)] then exceeds the solubility product of ZnS and a white
precipitate forms. In acid solution (Group II) [\(\ce{S^2-}\)] is suppressed by \(\ce{H+}\), so ZnS is not
precipitated &mdash; which is why \(\ce{Zn^2+}\) is a Group IV cation.</p>
<p>\(\ce{ZnCl2 + H2S + 2NH4OH -> ZnS v + 2NH4Cl + 2H2O}\) (white ppt)</p>""",
          topic="Practical: qualitative analysis (Group IV)",
          recall=r"""<ul><li>Group II: \(\ce{H2S}\) in dil. HCl (low [S<sup>2&minus;</sup>]) &rarr; CuS, PbS.</li>
<li>Group IV: \(\ce{H2S}\) in \(\ce{NH4Cl + NH4OH}\) (high [S<sup>2&minus;</sup>]) &rarr; ZnS (white), MnS
(buff), NiS, CoS (black).</li></ul>"""),
        # ------------------------------------------------------------ 1(d)
        Q("1(d)(i)", 1, MCQ + r"""<p>(i) The number of unpaired electrons in the complex ion [CoF<sub>6</sub>]<sup>3&minus;</sup> will be:</p>
<p>(a) 2 &nbsp; (b) 3 &nbsp; (c) 4 &nbsp; (d) 0</p>""",
          a=r"""<p>\(\ce{Co^3+}\) is 3d<sup>6</sup>. \(\ce{F-}\) is a weak-field ligand, so the complex is high spin
(outer-orbital, sp<sup>3</sup>d<sup>2</sup>):</p>
{{fig:0}}
<p><span class="box">(c) 4</span></p>""",
          afig=[fg.fig_cof6_cft],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Spectrochemical series: I<sup>&minus;</sup> &lt; Br<sup>&minus;</sup> &lt; Cl<sup>&minus;</sup> &lt; F<sup>&minus;</sup> &lt; H<sub>2</sub>O &lt; NH<sub>3</sub> &lt; en &lt; CN<sup>&minus;</sup> &lt; CO.</li>
<li>High spin when \(\Delta_o &lt; P\) (pairing energy).</li></ul>"""),
        Q("1(d)(ii)", 1, MCQ + r"""<p>(ii) The fibre obtained by condensation of hexamethylenediamine and adipic acid is:</p>
<p>(a) dacron &nbsp; (b) nylon 66 &nbsp; (c) rayon &nbsp; (d) teflon</p>""",
          excluded="Polymers &mdash; removed; not in the ISC 2027 Class XII unit list."),
        Q("1(d)(iii)", 1, MCQ + r"""<p>(iii) In the metallurgy of copper, matte is considered to be a mixture of:</p>
<p>(a) FeS+ZnS &nbsp; (b) CuS+FeS &nbsp; (c) CuFeS<sub>2</sub>+FeS &nbsp; (d) Cu<sub>2</sub>S+FeS</p>""",
          excluded="Metallurgy (extraction of copper) &mdash; removed; not in the ISC 2027 Class XII unit list."),
        Q("1(d)(iv)", 1, MCQ + r"""<p>(iv) Wohler's synthesis is used for the preparation of:</p>
<p>(a) glycine &nbsp; (b) amino acids &nbsp; (c) urea &nbsp; (d) protein</p>""",
          excluded="Wöhler's synthesis of urea (history of organic chemistry) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("1(d)(v)", 1, MCQ + r"""<p>(v) Dehydration of amide with P<sub>2</sub>O<sub>5</sub> yields:</p>
<p>(a) NH<sub>3</sub> &nbsp; (b) RCN &nbsp; (c) RNC &nbsp; (d) RNH<sub>2</sub></p>""",
          a=r"""<p>\(\ce{RCONH2 ->[P2O5][\Delta] RC#N + H2O}\)</p>
<p><span class="box">(b) RCN</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Cyanides from amides (dehydration) and from RX + KCN; isocyanides from RX + AgCN.</li></ul>"""),
        # ============================================================ PART II
        SEC("Part II", "Answer six questions choosing two from Section A, two from Section B and two from Section C"),
        SEC("Section A", ""),
        Q("2(a)(i)", 2, r"<p>A solution containing 8 gm of compound per 100 ml solution was found to have an osmotic "
          r"pressure of 500 cm of Hg at 27&deg;C. calculate the molecular mass of the compound.</p>",
          a=r"""<p>\(\pi = \dfrac{500}{76}\ \text{atm} = 6.579\ \text{atm}\); \(T = 300\ \text{K}\);
\(w = 8\ \text{g}\) in \(V = 0.100\ \text{L}\).</p>
<p>\[\pi V = \frac{w}{M}RT \;\Rightarrow\; M = \frac{wRT}{\pi V} = \frac{8\times0.0821\times300}{6.579\times0.100}
= 299.5\ \text{g mol}^{-1}\]</p>
<p><span class="box">Molecular mass &asymp; 299.5 g mol<sup>&minus;1</sup> (about 300)</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>van't Hoff: \(\pi = CRT\), C in mol L<sup>&minus;1</sup>, R = 0.0821 L atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>.</li>
<li>76 cm Hg = 1 atm; T in kelvin.</li></ul>"""),
        Q("2(a)(ii)", 1, r"<p>What happens to the boiling point of water when small amount of sodium chloride is "
          r"dissolved in it?</p>",
          a=r"""<p>The boiling point <b>rises</b> (elevation of boiling point): the non-volatile solute lowers the
vapour pressure, so a higher temperature is needed to make it equal to the external pressure. Since NaCl
dissociates into \(\ce{Na+}\) and \(\ce{Cl-}\) (i &asymp; 2), the elevation is nearly twice that of the same
molality of a non-electrolyte: \(\Delta T_b = iK_bm\).</p>""",
          topic="Solutions",
          recall=r"""<ul><li>\(\Delta T_b = iK_b m\); van't Hoff factor i &gt; 1 for dissociating solutes.</li></ul>"""),
        Q("2(b)(i)", 2, r"<p>The density of A<sup>+</sup>B<sup>&minus;</sup> which has (CsCl) bcc structure is "
          r"4.4 gm/cm<sup>3</sup>. Calculate the edge length of the crystal. [Formula mass = 213]</p>",
          excluded="Solid state (unit cell, density and edge length) &mdash; removed; not in the ISC 2027 Class XII unit list."),
        Q("2(b)(ii)", 1, r"<p>What is the coordination number of copper in its crystal?</p>",
          excluded="Solid state (coordination number in a metallic crystal) &mdash; removed; not in the ISC 2027 Class XII unit list."),
        Q("2(b)(iii)", 1, r"<p>An aqueous solution of acetic acid and sodium acetate having PH = 4.2 is diluted "
          r"to half the initial concentration. What will be the PH of the new solution.</p>",
          excluded="Buffer solutions (ionic equilibrium) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("2(c)(i)", 2, r"<p>If one Faraday were to be 48250C instead of 96500C, what will be the charge of an electron?</p>",
          a=r"""<p>One faraday is the charge on one mole of electrons: \(F = N_A e\). With Avogadro's number
unchanged,</p>
<p>\[e = \frac{F}{N_A} = \frac{48250}{6.022\times10^{23}} = 8.01\times10^{-20}\ \text{C}\]</p>
<p><span class="box">e = 8.01 &times; 10<sup>&minus;20</sup> C (half the actual 1.602 &times; 10<sup>&minus;19</sup> C)</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(F = N_A e = 6.022\times10^{23}\times1.602\times10^{-19} = 96500\) C mol<sup>&minus;1</sup>.</li></ul>"""),
        Q("2(c)(ii)", 1, r"<p>Explain the term Ferrimagnetic.</p>",
          excluded="Magnetic properties of solids (ferrimagnetism) &mdash; solid state, removed; not in the ISC 2027 Class XII unit list."),
        # ------------------------------------------------------------ Q3
        Q("3(a)(i)", 2, r"<p>The values of &lambda;<sup>&infin;</sup><sub>m</sub> for HCl, NaCl and CH<sub>3</sub>COONa "
          r"are 426.1, 126.5 and 91 ohm<sup>&minus;1</sup> cm<sup>2</sup> mol<sup>&minus;1</sup> respectively. "
          r"Calculate the value of &lambda;<sup>&infin;</sup><sub>m</sub> for acetic acid.</p>",
          a=r"""<p>By Kohlrausch's law of independent migration of ions:</p>
<p>\[\Lambda^\infty_m(\ce{CH3COOH}) = \Lambda^\infty_m(\ce{CH3COONa}) + \Lambda^\infty_m(\ce{HCl}) - \Lambda^\infty_m(\ce{NaCl})\]</p>
<p>\[= 91.0 + 426.1 - 126.5 = 390.6\ \Omega^{-1}\,\text{cm}^2\,\text{mol}^{-1}\]</p>
<p><span class="box">\(\Lambda^\infty_m(\ce{CH3COOH}) = 390.6\ \text{S cm}^2\,\text{mol}^{-1}\)</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Kohlrausch: \(\Lambda^\infty_m = \nu_+\lambda^\infty_+ + \nu_-\lambda^\infty_-\).</li>
<li>\(\Lambda^\infty_m\) of a weak electrolyte cannot be found by extrapolation; combine strong electrolytes
so that the unwanted ions cancel.</li></ul>"""),
        Q("3(a)(ii)", 3, r"<p>The temperature coefficient for the hydrolysis of ethyl acetate by sodium hydroxide "
          r"solution is 1.75. Calculate the energy of activation for the reaction.</p>",
          a=r"""<p>The temperature coefficient is \(k_{T+10}/k_T\). Take \(T_1 = 298\) K, \(T_2 = 308\) K, so
\(k_2/k_1 = 1.75\).</p>
<p>\[\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1T_2}\right)\]</p>
<p>\[E_a = \frac{2.303\,R\,T_1T_2}{T_2 - T_1}\log\frac{k_2}{k_1}
= \frac{2.303\times1.987\times298\times308}{10}\times\log1.75\]</p>
<p>\(\log 1.75 = 0.2430\):</p>
<p>\[E_a = 2.303\times1.987\times9178.4\times0.2430 = 1.021\times10^{4}\ \text{cal mol}^{-1}\]</p>
<p><span class="box">E<sub>a</sub> &asymp; 10.2 kcal mol<sup>&minus;1</sup> (= 42.7 kJ mol<sup>&minus;1</sup>)</span></p>
<p class="note">The temperature range is not stated; 298&ndash;308 K is assumed, as is usual for a
temperature coefficient.</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Temperature coefficient = \(k_{T+10}/k_T\), usually 2&ndash;3.</li>
<li>Arrhenius two-temperature form: \(\log\dfrac{k_2}{k_1} = \dfrac{E_a}{2.303R}\cdot\dfrac{T_2-T_1}{T_1T_2}\).</li>
<li>R = 1.987 cal = 8.314 J K<sup>&minus;1</sup> mol<sup>&minus;1</sup>.</li></ul>"""),
        Q("3(b)", 2, r"<p>Deduce the equation to calculate the PH of an acid buffer solution.</p>",
          excluded="Buffer solutions / Henderson equation (ionic equilibrium) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("3(c)", 1, r"<p>AgNO<sub>3</sub> solution cannot be stored in a copper vessel &ndash; Explain.</p>",
          a=r"""<p>\(E^\circ(\ce{Cu^2+/Cu}) = +0.34\) V is lower than \(E^\circ(\ce{Ag+/Ag}) = +0.80\) V, so copper is a
stronger reducing agent and displaces silver:</p>
<p>\(\ce{Cu + 2AgNO3 -> Cu(NO3)2 + 2Ag}\); \(E^\circ_{cell} = 0.80 - 0.34 = +0.46\) V &gt; 0, so the
reaction is spontaneous and the vessel would be eaten away.</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>A metal displaces from solution any metal with a higher reduction potential.</li></ul>"""),
        Q("3(d)", 2, r"<p>Calculate the molality of solution prepared by dissolving 3.6 gm glucose in 500 gm water.</p>",
          a=r"""<p>Moles of glucose (\(\ce{C6H12O6}\), M = 180 g mol<sup>&minus;1</sup>) \(= \dfrac{3.6}{180} = 0.020\) mol</p>
<p>\[m = \frac{\text{moles of solute}}{\text{mass of solvent in kg}} = \frac{0.020}{0.500} = 0.040\ \text{mol kg}^{-1}\]</p>
<p><span class="box">Molality = 0.04 m</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>Molality = mol solute / kg solvent (not solution); independent of temperature.</li></ul>"""),
        # ------------------------------------------------------------ Q4
        Q("4(a)", 3, r"<p>The standard electrode potential of Pb/Pb<sup>2+</sup> and Pt/I<sup>&minus;</sup>/I<sub>2</sub> are "
          r"&minus;0.126 v and 0.536 v respectively. When a galvanic cell is constructed using 0.1 M concentration "
          r"of the ions. Pt is found to be the cathode. What is the emf of the cell?</p>"
          r"<p class='note'>[The values are standard reduction potentials: E&deg;(Pb<sup>2+</sup>/Pb) = &minus;0.126 V, "
          r"E&deg;(I<sub>2</sub>/I<sup>&minus;</sup>) = +0.536 V.]</p>",
          a=r"""<p>Cell: \(\ce{Pb | Pb^2+ (0.1 M) || I- (0.1 M) | I2 | Pt}\)</p>
<p>Anode: \(\ce{Pb -> Pb^2+ + 2e-}\); cathode: \(\ce{I2 + 2e- -> 2I-}\); cell reaction
\(\ce{Pb + I2 -> Pb^2+ + 2I-}\), n = 2.</p>
<p>\(E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} = 0.536 - (-0.126) = 0.662\ \text{V}\)</p>
<p>\[E_{cell} = E^\circ_{cell} - \frac{0.0591}{2}\log\left([\ce{Pb^2+}][\ce{I-}]^2\right)
= 0.662 - 0.02955\log(0.1\times0.1^2)\]</p>
<p>\[= 0.662 - 0.02955\times(-3) = 0.662 + 0.0887 = 0.751\ \text{V}\]</p>
<p><span class="box">E<sub>cell</sub> = 0.751 V</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(E_{cell} = E^\circ_{cell} - \dfrac{0.0591}{n}\log Q\) at 298 K; pure solids and \(\ce{I2}\) (s) are omitted from Q.</li>
<li>\(E^\circ_{cell} = E^\circ_{\text{right}} - E^\circ_{\text{left}}\) (reduction potentials).</li></ul>"""),
        Q("4(b)(i)", 2, r"<p>What is Arrhenius equation? How can it be used graphically to calculate the energy of "
          r"activation for a reaction?</p>",
          a=r"""<p><b>Arrhenius equation</b>: \(k = A\,e^{-E_a/RT}\), where k is the rate constant, A the frequency
(pre-exponential) factor, \(E_a\) the activation energy, R the gas constant and T the absolute temperature.</p>
<p>Taking logarithms: \[\log k = \log A - \frac{E_a}{2.303R}\cdot\frac{1}{T}\]</p>
<p>This has the form y = c + mx. Measure k at several temperatures and plot log k against 1/T: a
straight line is obtained.</p>
{{fig:0}}
<p><span class="box">slope = \(-\dfrac{E_a}{2.303R}\) &rArr; \(E_a = -2.303R\times\text{slope}\); intercept = log A</span></p>""",
          afig=[fg.fig_arrhenius_plot],
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Higher \(E_a\) &rArr; steeper line &rArr; rate more sensitive to temperature.</li>
<li>Using ln k instead: slope = \(-E_a/R\).</li></ul>"""),
        Q("4(b)(ii)", 2, r"<p>The solubility product of BaSO<sub>4</sub> is 1.5 &times; 10<sup>&minus;9</sup>. Find its "
          r"solubility in 0.1 M BaCl<sub>2</sub> solution.</p>",
          excluded="Solubility product and common-ion effect (ionic equilibrium) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("4(c)", 3, r"""<p>(i) How many formula units of sodium chloride are present in an unit cell of sodium chloride?</p>
<p>(ii) The what type of cubic system does this cell belong?</p>
<p>(iii) What is the geometry of sodium ions around chloride ions?</p>""",
          excluded="Solid state (NaCl unit cell, cubic systems, coordination geometry) &mdash; removed; not in the ISC 2027 Class XII unit list."),
        # ============================================================ Section B
        SEC("Section B", "Answer any two questions"),
        Q("5(a)", 2, r"<p>Write the formulae of the following coordination compounds: (i) Potassium "
          r"dicyanoargentate(I) &nbsp; (ii) hexaaquairon (III) chloride</p>",
          a=r"""<p>(i) <span class="box">\(\ce{K[Ag(CN)2]}\)</span> &nbsp; (Ag +1, two \(\ce{CN-}\): complex ion
\(\ce{[Ag(CN)2]-}\))</p>
<p>(ii) <span class="box">\(\ce{[Fe(H2O)6]Cl3}\)</span> &nbsp; (Fe +3, six neutral water ligands: complex ion
\(\ce{[Fe(H2O)6]^3+}\))</p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>In the formula the metal is written first inside [ ], then ligands (anionic before
neutral); the counter-ion goes outside.</li></ul>"""),
        Q("5(b)", 1, r"<p>Using C.F.T determine the number of unpaired electrons for FeCl<sub>4</sub><sup>&minus;</sup> complex</p>",
          a=r"""<p>\(\ce{[FeCl4]-}\): Fe is +3 (\(x - 4 = -1\)), 3d<sup>5</sup>; four ligands &rArr; tetrahedral.
In a tetrahedral field the d orbitals split into a lower <i>e</i> pair and an upper <i>t</i><sub>2</sub> set, with
\(\Delta_t \approx \tfrac49\Delta_o\) &mdash; always smaller than the pairing energy, especially with weak-field
\(\ce{Cl-}\):</p>
{{fig:0}}
<p><span class="box">5 unpaired electrons (e<sup>2</sup> t<sub>2</sub><sup>3</sup>), high spin; &mu; = 5.92 BM</span></p>""",
          afig=[fg.fig_fecl4_cft],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Octahedral: t<sub>2g</sub> below, e<sub>g</sub> above; tetrahedral: the reverse, e below, t<sub>2</sub> above.</li>
<li>Tetrahedral complexes are practically always high spin.</li></ul>"""),
        Q("5(c)", 2, r"<p>Explain why tetrahedral nickel complexes are paramagnetic but square planar Ni(II) "
          r"complexes are diamagnetic.</p>",
          a=r"""<p>\(\ce{Ni^2+}\) is 3d<sup>8</sup> with two unpaired electrons.</p>
<ul><li><b>Tetrahedral</b> (e.g. \(\ce{[NiCl4]^2-}\), weak-field \(\ce{Cl-}\)): the 3d electrons are not
disturbed; the ligand pairs enter the 4s and three 4p orbitals (sp<sup>3</sup>). Two unpaired electrons remain
&rArr; <b>paramagnetic</b> (&mu; &asymp; 2.83 BM).</li>
<li><b>Square planar</b> (e.g. \(\ce{[Ni(CN)4]^2-}\), strong-field \(\ce{CN-}\)): the two odd electrons pair
up, leaving one 3d orbital empty; it hybridises with 4s and two 4p orbitals (dsp<sup>2</sup>). No unpaired
electron &rArr; <b>diamagnetic</b>.</li></ul>
{{fig:0}}
<p>(In CFT terms: in a square-planar field the \(d_{x^2-y^2}\) orbital is raised so high that all eight
electrons pair in the four lower orbitals.)</p>""",
          afig=[fg.fig_ni_vbt],
          topic="Coordination Compounds",
          recall=r"""<ul><li>sp<sup>3</sup> &rarr; tetrahedral; dsp<sup>2</sup> (uses an inner (n&minus;1)d orbital) &rarr; square planar.</li>
<li>\(\mu = \sqrt{n(n+2)}\): n = 2 gives 2.83 BM.</li></ul>"""),
        Q("6(a)(i)", 2, r"<p>Explain the following facts: (i) Silver bromide is used in photography.</p>",
          excluded="Silver halides and photography (compounds of silver) &mdash; not in the ISC 2027 syllabus, which treats only K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> and KMnO<sub>4</sub> among d-block compounds."),
        Q("6(a)(ii)", 2, r"<p>Explain the following facts: (ii) In a given transition series, there is no significant "
          r"change in the atomic radii of elements with increase in atomic number.</p>",
          a=r"""<ul><li>Across a transition series the nuclear charge rises by one unit at each element, and the added
electron goes into the inner <b>(n&minus;1)d</b> subshell.</li>
<li>These d electrons screen the outer ns electrons from the nucleus. The increase in nuclear charge is
therefore almost balanced by the increase in screening, so the effective nuclear charge on the outer
electrons hardly changes.</li>
<li>Hence the atomic radii remain nearly constant (a small decrease at the start; a slight increase near
the end of the series because of repulsion among the paired d electrons).</li></ul>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Z<sub>eff</sub> = Z &minus; screening constant; d electrons screen poorly but enough to
offset the +1 per step.</li></ul>"""),
        Q("6(b)", 1, r"<p>Draw the structure of xenonoxyfluoride molecules</p>",
          excluded="Compounds of xenon (noble gases, p-block group 18) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("7(a)(i)", 1, r"<p>Give balanced equations for the following reactions. (i) Ozone and mercury.</p>",
          excluded="Ozone (p-block, group 16) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("7(a)(ii)", 1, r"<p>Give balanced equations for the following reactions. (ii) Chlorine is passed through "
          r"hot concentrated NaOH solution.</p>",
          excluded="Chlorine (p-block, group 17) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("7(a)(iii)", 1, r"<p>Give balanced equations for the following reactions. (iii) Silver nitrate is added "
          r"to dilute solution of sodium thiosulphate</p>",
          excluded="Compounds of silver / thiosulphate chemistry &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("7(b)", 2, r"<p>How is silver extracted from its sulphide ore by cyanide process? Give only the reactions.</p>",
          excluded="Metallurgy (cyanide process for silver) &mdash; removed; not in the ISC 2027 Class XII unit list."),
        # ============================================================ Section C
        SEC("Section C", "(Answer any two questions)"),
        Q("8(a)(i)", 2, r"<p>How can the following conversions be brought about: (i) Benzoic acid to phenol</p>"
          r"<p class='note'>[The marks in 8(a) are printed one line low in the original; read as (i) 2, (ii) 1, "
          r"(iii) 1, (iv) 2, which matches the length of each conversion and the question total of 10.]</p>",
          a=r"""<p>Benzoic acid &rarr; benzamide &rarr; aniline (Hofmann bromamide) &rarr; benzenediazonium chloride
&rarr; phenol:</p>
<p>\(\ce{C6H5COOH + NH3 -> C6H5COONH4 ->[\Delta] C6H5CONH2 + H2O}\)</p>
<p>\(\ce{C6H5CONH2 + Br2 + 4KOH -> C6H5NH2 + K2CO3 + 2KBr + 2H2O}\)</p>
<p>\(\ce{C6H5NH2 + NaNO2 + 2HCl ->[273-278 K] C6H5N2Cl + NaCl + 2H2O}\)</p>
<p>\(\ce{C6H5N2Cl + H2O ->[warm] C6H5OH + N2 + HCl}\)</p>
<p>(Alternative: decarboxylate with soda lime to benzene, sulphonate, fuse the sodium benzenesulphonate
with NaOH and acidify.)</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Hofmann bromamide: \(\ce{RCONH2 -> RNH2}\), one carbon fewer.</li>
<li>Diazonium salt + warm water &rarr; phenol.</li></ul>"""),
        Q("8(a)(ii)", 1, r"<p>How can the following conversions be brought about: (ii) Acetaldehyde to acetamide.</p>",
          a=r"""<p>Oxidise to acetic acid, convert to the ammonium salt and heat:</p>
<p>\(\ce{CH3CHO + [O] ->[K2Cr2O7/H2SO4] CH3COOH}\)</p>
<p>\(\ce{CH3COOH + NH3 -> CH3COONH4 ->[\Delta] CH3CONH2 + H2O}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Aldehydes are easily oxidised to acids; ammonium salts of acids lose water on heating to give amides.</li></ul>"""),
        Q("8(a)(iii)", 1, r"<p>How can the following conversions be brought about: (iii) Aniline to fluorobenzene</p>",
          a=r"""<p>Diazotise, then the Balz&ndash;Schiemann reaction:</p>
<p>\(\ce{C6H5NH2 + NaNO2 + 2HCl ->[273-278 K] C6H5N2Cl + NaCl + 2H2O}\)</p>
<p>\(\ce{C6H5N2Cl + HBF4 -> C6H5N2BF4 v + HCl}\)</p>
<p>\(\ce{C6H5N2BF4 ->[\Delta] C6H5F + N2 + BF3}\)</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Fluoro- (Balz&ndash;Schiemann) and iodo-arenes (KI) are made via diazonium salts; Cl/Br/CN by Sandmeyer.</li></ul>"""),
        Q("8(a)(iv)", 2, r"<p>How can the following conversions be brought about: (iv) Propionic acid to acetic acid</p>",
          a=r"""<p>A step-down (one carbon fewer) through the Hofmann bromamide reaction:</p>
<p>\(\ce{CH3CH2COOH + NH3 -> CH3CH2COONH4 ->[\Delta] CH3CH2CONH2 + H2O}\)</p>
<p>\(\ce{CH3CH2CONH2 + Br2 + 4KOH -> CH3CH2NH2 + K2CO3 + 2KBr + 2H2O}\)</p>
<p>\(\ce{CH3CH2NH2 + HNO2 -> CH3CH2OH + N2 + H2O}\)</p>
<p>\(\ce{CH3CH2OH + 2[O] ->[K2Cr2O7/H2SO4] CH3COOH + H2O}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Descending a series: acid &rarr; amide &rarr; amine (Hofmann) &rarr; alcohol &rarr; acid.</li></ul>"""),
        Q("8(b)", 2, r"""<p>Identify the products A,B,C and D</p>
<p>\(\ce{CH3CH2Br ->[KCN] A ->[H2O/H+] B ->[PCl5] C ->[NH3] D}\)</p>""",
          a=r"""<p>\(\ce{CH3CH2Br + KCN -> CH3CH2CN + KBr}\)</p>
<p>\(\ce{CH3CH2CN + 2H2O + HCl -> CH3CH2COOH + NH4Cl}\)</p>
<p>\(\ce{CH3CH2COOH + PCl5 -> CH3CH2COCl + POCl3 + HCl}\)</p>
<p>\(\ce{CH3CH2COCl + 2NH3 -> CH3CH2CONH2 + NH4Cl}\)</p>
<table class="tbl"><tr><td>A</td><td>Propanenitrile (ethyl cyanide), \(\ce{CH3CH2CN}\)</td></tr>
<tr><td>B</td><td>Propanoic acid, \(\ce{CH3CH2COOH}\)</td></tr>
<tr><td>C</td><td>Propanoyl chloride, \(\ce{CH3CH2COCl}\)</td></tr>
<tr><td>D</td><td>Propanamide, \(\ce{CH3CH2CONH2}\)</td></tr></table>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>KCN on RX adds one carbon (nitrile); hydrolysis gives the acid.</li>
<li>\(\ce{PCl5}\): &ndash;COOH &rarr; &ndash;COCl; acid chloride + \(\ce{NH3}\) &rarr; amide.</li></ul>"""),
        Q("8(c)", 2, r"""<p>Complete the given reactions</p>
<p>(i) \(\ce{CH3COCH3 + I2 + KOH ->}\) &nbsp;&nbsp; (ii) \(\ce{C6H5NH2 + CH3COCl ->[Pyridine]}\)</p>""",
          a=r"""<p>(i) Iodoform reaction:</p>
<p>\(\ce{CH3COCH3 + 3I2 + 4KOH -> CHI3 v + CH3COOK + 3KI + 3H2O}\) (yellow iodoform)</p>
<p>(ii) Acetylation of aniline; pyridine removes the HCl formed:</p>
<p>\(\ce{C6H5NH2 + CH3COCl ->[pyridine] C6H5NHCOCH3 + HCl}\) (acetanilide)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Methyl ketones and acetaldehyde give the iodoform test.</li>
<li>Pyridine is a base that neutralises HCl and drives acylation forward.</li></ul>"""),
        Q("9(a)", 3, r"""<p>Give balanced equations for the following name reactions:</p>
<p>(i) Kolbe-Schmidt reaction. (ii) Hellvolard's Zelinsky reaction (iii) Clemmensen's reduction reaction.</p>""",
          a=r"""<p>(i) <b>Kolbe&ndash;Schmidt</b>: sodium phenoxide and \(\ce{CO2}\) at about 400 K and 4&ndash;7 atm, then acid:</p>
<p>\(\ce{C6H5ONa + CO2 -> C6H4(OH)COONa}\) (sodium salicylate)</p>
<p>\(\ce{C6H4(OH)COONa + HCl -> C6H4(OH)COOH + NaCl}\) (salicylic acid)</p>
<p>(ii) <b>Hell&ndash;Volhard&ndash;Zelinsky</b>: &alpha;-halogenation with red P:</p>
<p>\(\ce{CH3COOH + Cl2 ->[red P] ClCH2COOH + HCl}\)</p>
<p>(iii) <b>Clemmensen reduction</b>: C=O &rarr; CH<sub>2</sub> with zinc amalgam and conc. HCl:</p>
<p>\(\ce{CH3COCH3 + 4[H] ->[Zn-Hg/conc. HCl] CH3CH2CH3 + H2O}\)</p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Kolbe: phenoxide + \(\ce{CO2}\) &rarr; o-hydroxy acid.</li>
<li>HVZ: needs &alpha;-H. Clemmensen (acid) vs Wolff&ndash;Kishner (base) both give the alkane.</li></ul>"""),
        Q("9(b)", 4, r"""<p>An organic compound[A] with molecular formula C<sub>3</sub>H<sub>6</sub>O which reduces
Tollen's reagent gives compound [B] on treatment with hydroxylamine. [B] on reduction with LiAlH<sub>4</sub>
gives compound [C]. Compound [C] on warming with chloroform and potassium hydroxide gives compound [D] with
unpleasant smell. [D] on reduction with Na/C<sub>2</sub>H<sub>5</sub>OH gives [E] which gives insoluble compound
with benzene sulphonyl chloride and NaOH. Give the sequence of reactions and suggest structures of[A] to [E]</p>""",
          a=r"""<p>\(\ce{C3H6O}\) reducing Tollens' reagent is an aldehyde: propanal (acetone does not reduce it).</p>
<p>\(\ce{CH3CH2CHO + NH2OH -> CH3CH2CH=NOH + H2O}\)</p>
<p>\(\ce{CH3CH2CH=NOH + 4[H] ->[LiAlH4] CH3CH2CH2NH2 + H2O}\)</p>
<p>\(\ce{CH3CH2CH2NH2 + CHCl3 + 3KOH ->[\Delta] CH3CH2CH2NC + 3KCl + 3H2O}\) (carbylamine; offensive smell)</p>
<p>\(\ce{CH3CH2CH2NC + 4[H] ->[Na/C2H5OH] CH3CH2CH2NHCH3}\)</p>
<p>E is a secondary amine; its sulphonamide has no H on N, so it is insoluble in NaOH:</p>
<p>\(\ce{CH3CH2CH2NHCH3 + C6H5SO2Cl -> C6H5SO2N(CH3)CH2CH2CH3 + HCl}\)</p>
<table class="tbl"><tr><td>A</td><td>Propanal, \(\ce{CH3CH2CHO}\)</td></tr>
<tr><td>B</td><td>Propanal oxime, \(\ce{CH3CH2CH=NOH}\)</td></tr>
<tr><td>C</td><td>Propan-1-amine, \(\ce{CH3CH2CH2NH2}\)</td></tr>
<tr><td>D</td><td>Propyl isocyanide, \(\ce{CH3CH2CH2NC}\)</td></tr>
<tr><td>E</td><td>N-Methylpropan-1-amine, \(\ce{CH3CH2CH2NHCH3}\)</td></tr></table>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Oximes are reduced to 1&deg; amines; isocyanides are reduced to N-methyl 2&deg; amines.</li>
<li>Carbylamine test: only 1&deg; amines, foul-smelling isocyanide.</li>
<li>Hinsberg: 2&deg; amine &rarr; sulphonamide insoluble in alkali.</li></ul>"""),
        Q("9(c)", 3, r"""<p>Give one chemical test to distinguish between the following pairs.</p>
<p>i) Formic acid and oxalic acid . &nbsp; ii) Glucose and fructose</p>""",
          a=r"""<p>(i) <b>Tollens' reagent</b>: formic acid (it has an H&ndash;C=O group) gives a silver mirror on
warming; oxalic acid does not.</p>
<p>\(\ce{HCOOH + Ag2O -> 2Ag v + CO2 + H2O}\)</p>
<p>(ii) <b>Bromine water</b>: glucose decolourises it (oxidised to gluconic acid); fructose, a ketose, does
not.</p>
<p>\(\ce{CH2OH(CHOH)4CHO + Br2 + H2O -> CH2OH(CHOH)4COOH + 2HBr}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Formic acid is a reducing acid (Tollens', Fehling's +ve).</li>
<li>Bromine water oxidises aldoses only.</li></ul>"""),
        Q("10(a)", 4, r"""<p>Write balanced reactions for the following:</p>
<p>(i) Acetamide is heated with phosphorous pentoxide followed by hydrolysis.</p>
<p>(ii) Benzoic acid is treated with a mixture of conc.H<sub>2</sub>SO<sub>4</sub> and conc.HNO<sub>3</sub>.</p>
<p>(iii) Ethyl magnesium chloride is treated with formaldehyde and the product is hydrolysed in presence of an acid.</p>
<p>(iv) Diethyl ether reacts with excess of HI.</p>""",
          a=r"""<p>(i) Dehydration to methyl cyanide, then acid hydrolysis to acetic acid:</p>
<p>\(\ce{CH3CONH2 ->[P2O5][\Delta] CH3CN + H2O}\); \(\ce{CH3CN + 2H2O + HCl -> CH3COOH + NH4Cl}\)</p>
<p>(ii) &ndash;COOH is meta-directing: m-nitrobenzoic acid is formed.</p>
<p>\(\ce{C6H5COOH + HNO3 ->[conc. H2SO4] C6H4(NO2)COOH + H2O}\)</p>
<p>(iii) A primary alcohol with one carbon more (propan-1-ol):</p>
<p>\(\ce{C2H5MgCl + HCHO ->[dry ether] C2H5CH2OMgCl}\); \(\ce{C2H5CH2OMgCl + H2O ->[H+] CH3CH2CH2OH + Mg(OH)Cl}\)</p>
<p>(iv) With excess HI both C&ndash;O bonds are cleaved:</p>
<p>\(\ce{C2H5OC2H5 + 2HI ->[\Delta] 2C2H5I + H2O}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>RMgX + HCHO &rarr; 1&deg; alcohol; + RCHO &rarr; 2&deg;; + ketone &rarr; 3&deg;.</li>
<li>Ether + 1 HI (cold) &rarr; ROH + RI; excess HI (hot) &rarr; 2 RI.</li></ul>"""),
        Q("10(b)", 2, r"<p>On electrolysis in acidic solution amino acids migrate towards cathode, while in alkaline "
          r"solution these migrate towards anode. Explain</p>",
          a=r"""<p>In water an amino acid exists as a zwitter ion. In <b>acid</b> the &ndash;COO<sup>&minus;</sup> is
protonated and the molecule becomes a <b>cation</b>, \(\ce{H3N+-CHR-COOH}\), which moves to the cathode. In
<b>alkali</b> the &ndash;NH<sub>3</sub><sup>+</sup> loses a proton and the molecule becomes an <b>anion</b>,
\(\ce{H2N-CHR-COO-}\), which moves to the anode. At the isoelectric point it does not migrate.</p>
{{fig:0}}""",
          afig=[fg.fig_amino_acid_forms],
          topic="Biomolecules",
          recall=r"""<ul><li>Isoelectric point: pH at which the amino acid is electrically neutral (zwitter ion).</li></ul>"""),
        Q("10(c)", 2, r"<p>Deficiency of which vitamin will cause the following diseases: (i) Night blindness "
          r"&nbsp; (ii) Ricket</p>",
          a=r"""<p>(i) Night blindness &mdash; <span class="box">vitamin A</span> (fat soluble)</p>
<p>(ii) Rickets &mdash; <span class="box">vitamin D</span> (fat soluble)</p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Fat soluble: A, D, E, K; water soluble: B group, C.</li>
<li>B<sub>1</sub> beri-beri, C scurvy, K delayed clotting.</li></ul>"""),
        Q("10(d)", 2, r"<p>Name the type of polymerization and the monomers in each of the following polymers: "
          r"(i) Dacron &nbsp; (ii) Nylon- 66</p>",
          excluded="Polymers &mdash; removed; not in the ISC 2027 Class XII unit list."),
    ])
