"""Heritage School Pre-Board 2024-25, Chemistry (Paper 1), Set 2 -- transcribed from the page images of the
.docx (rendered to PDF with LibreOffice).  The .docx carries no embedded images; equations are inline text
and Word equation objects, all checked against the rendered pages."""
from kit import Q, SEC
import chemistry_2024_25_s2_figs as fg

AR = r"""<p>(a) Both assertion and reason are true, and reason is the correct explanation of assertion.<br>
(b) Both assertion and reason are true, but reason is not the correct explanation for assertion.<br>
(c) Assertion is true, but reason is false.<br>
(d) Assertion is false, but reason is true.</p>"""

WORDS = (r"[2-propanone, methanol, square planar, gram-equivalent, +3, gram-mol, Ethanal, octahedral, five, six, 1, "
         r"volume, formic acid, 2, tetrahedral, formaldehyde, 0, less, amount, +2, &minus;2, four]")

PAPER = dict(
    subject="chemistry",
    year="2024-25",
    slug="2024-25-set-2",
    paper="Set 2",
    source="PreBoard-PYQ/2024-25/SET-2/Chemistry.docx",
    marks=70, time="3 hours",
    intro=r"""<p><b>The Heritage School &mdash; Pre-board Examinations, 2024-2025. Subject &ndash; Chemistry,
Class &ndash; 12.</b> Maximum Marks: 70. Time Allowed: Three Hours.</p>
<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start writing during
this time.)</p>
<p>This paper is divided into four sections &ndash; A, B, C and D.<br>
Answer all questions.<br>
Section &ndash; A consists of one question having sub-parts of one mark each.<br>
Section &ndash; B consists of ten questions of two marks each.<br>
Section &ndash; C consists of seven questions of three marks each, and<br>
Section &ndash; D consists of three questions of five marks each.<br>
Internal choices have been provided in one question each in Section B, Section C and Section D.</p>
<p>All working, including rough work, should be done on the same sheet as, and adjacent to the rest of the
answer.</p>
<p>The intended marks for questions or parts of questions are given in brackets [ ]. Balanced equations must be
given wherever possible and diagrams where they are helpful. When solving numerical problems, all essential
working must be shown. In working out problems, use the following data: Gas constant R = 1&middot;987 cal
deg<sup>&minus;1</sup> mol<sup>&minus;1</sup> = 8&middot;314 JK<sup>&minus;1</sup> mol<sup>&minus;1</sup> =
0&middot;0821 dm<sup>3</sup>atm K<sup>&minus;1</sup>mol<sup>&minus;1</sup>, 1 l atm = 1 dm<sup>3</sup>atm =
101&middot;3 J. 1 Faraday = 96500 coulombs. Avogadro's number = 6&middot;023&times;10<sup>23</sup>.</p>
<p>This question paper consists of 8 printed pages. [The file itself runs to 9 pages.]</p>""",
    items=[
        # ------------------------------------------------------------------ Section A
        SEC("Section A &ndash; (14 marks)", "Question 1"),
        Q("1(A)(i)", 1, r"<p><b>(A) Fill in the blanks by choosing the appropriate word(s) from those given in the "
          r"brackets:</b> " + WORDS + r" [4&times;1]</p>"
          r"<p>(i) Equivalent conductivity is the conducting power of all the ions furnished by one ________ of an "
          r"electrolyte present in a definite________ of the solution.</p>",
          a=r"""<p>Equivalent conductivity is the conducting power of all the ions furnished by one
<b>gram-equivalent</b> of an electrolyte present in a definite <b>volume</b> of the solution.</p>
<p>\(\Lambda_\text{eq} = \kappa \times V\), where V (cm<sup>3</sup>) is the volume containing 1 g-equivalent:
\(\Lambda_\text{eq} = \dfrac{1000\,\kappa}{N}\).</p>
<p><span class="box">gram-equivalent; volume</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\Lambda_\text{eq} = 1000\kappa/N\) (S cm<sup>2</sup> eq<sup>&minus;1</sup>);
\(\Lambda_m = 1000\kappa/M\) (S cm<sup>2</sup> mol<sup>&minus;1</sup>).</li>
<li>Normality = molarity &times; (total positive charge per formula unit).</li></ul>"""),
        Q("1(A)(ii)", 1, r"<p>(ii) In the complex [Co(NH<sub>3</sub>)<sub>5</sub>(NO<sub>2</sub>)]Cl, the coordination "
          r"number and the oxidation number of the central metal ion are ______ and ______.</p>",
          a=r"""<p>Six donor atoms (5 N of NH<sub>3</sub> + 1 N of \(\ce{NO2-}\)) surround Co: coordination number
<b>six</b>.</p>
<p>One \(\ce{Cl-}\) outside the bracket &rArr; the complex ion is \(\ce{[Co(NH3)5(NO2)]+}\):
\(x + 5(0) + (-1) = +1 \Rightarrow x = +2\).</p>
<p><span class="box">six; +2</span></p>
<p class="note">The familiar compound is [Co(NH<sub>3</sub>)<sub>5</sub>(NO<sub>2</sub>)]Cl<sub>2</sub>, in which
cobalt is +3. With the formula as printed (one Cl) the oxidation number is +2; both +2 and +3 are in the word
list, so write the value the printed formula gives and show the working.</p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Coordination number = number of donor atoms bonded to the metal (not the number of
ligands, for polydentate ligands).</li>
<li>Charge of complex ion = oxidation state of metal + sum of ligand charges.</li></ul>"""),
        Q("1(A)(iii)", 1, r"<p>(iii) Ozonolysis of propene followed by hydrolysis gives ______ and _______.</p>",
          a=r"""<p>\[\ce{CH3-CH=CH2 ->[(i) O3][(ii) Zn/H2O] CH3CHO + HCHO}\]</p>
<p>The C=C is cleaved and each carbon becomes C=O.</p>
<p><span class="box">Ethanal; formaldehyde</span></p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Ozonolysis (reductive, Zn/H<sub>2</sub>O): each alkene carbon becomes a carbonyl
carbon; =CH<sub>2</sub> gives HCHO.</li></ul>"""),
        Q("1(A)(iv)", 1, r"<p>(iv) The number of unpaired electrons and shape of [CuCl<sub>4</sub>]<sup>2-</sup> is "
          r"__________ and _________.</p>",
          a=r"""<p>\(\ce{Cu^2+}\) is 3d<sup>9</sup>: one unpaired electron whatever the ligand. \(\ce{Cl-}\) is a weak-field
ligand; the empty 4s and 4p orbitals take the four ligand pairs: sp<sup>3</sup>, tetrahedral.</p>
{{fig:0}}
<p><span class="box">1; tetrahedral</span></p>
<p class="note">Crystal structures show [CuCl<sub>4</sub>]<sup>2&minus;</sup> as a flattened tetrahedron (and in some
salts square planar); the textbook answer expected here is tetrahedral.</p>""",
          afig=[fg.fig_b_cucl4_vbt],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Cu<sup>2+</sup>: [Ar]3d<sup>9</sup> &mdash; always one unpaired electron
(&mu; &asymp; 1.73 BM).</li>
<li>CN 4 with weak-field ligand &rarr; sp<sup>3</sup>, tetrahedral.</li></ul>"""),
        Q("1(B)(i)", 1, r"<p><b>(B) Select and write the correct alternative from the choices given below:</b> "
          r"[7&times;1]</p><p>(i) Decreasing order of basicity of the three isomers of nitro aniline is :</p>"
          r"<p>(a) p-nitroaniline &gt; o- nitroaniline &gt; m- nitroaniline<br>"
          r"(b) p-nitroaniline &gt; m- nitroaniline &gt; o- nitroaniline<br>"
          r"(c) m-nitroaniline &gt; p- nitroaniline &gt; o- nitroaniline<br>"
          r"(d) m-nitroaniline &gt; o- nitroaniline &gt; p- nitroaniline</p>",
          a=r"""<p>&ndash;NO<sub>2</sub> withdraws electrons from the ring and so from the N lone pair. At o- and p-
positions it acts by both &minus;R (resonance) and &minus;I; at m- by &minus;I only, so m-nitroaniline is the
strongest base. The o-isomer is weakest (strongest &minus;I at short range, plus intramolecular H-bonding and
steric hindrance to protonation &mdash; the ortho effect).</p>
<p><span class="box">(c) m-nitroaniline &gt; p-nitroaniline &gt; o-nitroaniline</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Electron-withdrawing groups lower the basicity of aniline; the effect is largest at o- and
p- (resonance) and smallest at m- (inductive only).</li></ul>"""),
        Q("1(B)(ii)", 1, r"<p>(ii) If two liquids A and B form minimum boiling azeotrope at some specific composition, "
          r"then</p><p>(a) A&ndash;B interactions are stronger than those between A&ndash;A or B&ndash;B.<br>"
          r"(b) Vapour pressure of solution decreases because more number of molecules of liquids A and B can escape "
          r"from the solution.<br>"
          r"(c) Vapour pressure of solution decreases because less number of molecules of only one of the liquids "
          r"escape from the solution.<br>"
          r"(d) A&ndash;B interactions are weaker than those between A&ndash;A or B&ndash;B.</p>",
          a=r"""<p>A minimum-boiling azeotrope has a <i>maximum</i> vapour pressure, i.e. a large positive deviation
from Raoult's law: molecules escape more easily because A&ndash;B attractions are weaker than A&ndash;A and
B&ndash;B attractions (e.g. ethanol + water).</p>
<p><span class="box">(d) A&ndash;B interactions are weaker than those between A&ndash;A or B&ndash;B</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>Positive deviation &rarr; higher vapour pressure &rarr; minimum-boiling azeotrope.</li>
<li>Negative deviation &rarr; lower vapour pressure &rarr; maximum-boiling azeotrope.</li></ul>"""),
        Q("1(B)(iii)", 1, r"<p>(iii) Which of the following reactant gives the best method of preparation of alkyl "
          r"halides when reacts with alcohol?</p><p>(a) Zn/HCl<br>(b) PCl<sub>5</sub><br>"
          r"(c) SOCl<sub>2</sub>/ Pyridine<br>(d) PCl<sub>3</sub></p>",
          a=r"""<p>\[\ce{R-OH + SOCl2 ->[pyridine] R-Cl + SO2 ^ + HCl ^}\]</p>
<p>Both by-products are gases and escape, leaving pure alkyl chloride; pyridine absorbs the HCl.</p>
<p><span class="box">(c) SOCl<sub>2</sub>/pyridine</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Darzen's method (SOCl<sub>2</sub>): gaseous by-products, no separation needed.</li>
<li>PCl<sub>5</sub> gives POCl<sub>3</sub>, PCl<sub>3</sub> gives H<sub>3</sub>PO<sub>3</sub> &mdash; both must be
separated.</li></ul>"""),
        Q("1(B)(iv)", 1, r"<p>(iv) Which of the following monosaccharide is a ketose?</p>"
          r"<p>(a) Glucose<br>(b) Fructose<br>(c) Ribose<br>(d) Galactose</p>",
          a=r"""<p>Fructose has a C=O at C-2 (a ketohexose); glucose, galactose and ribose are aldoses.</p>
<p><span class="box">(b) Fructose</span></p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Aldose: &ndash;CHO at C-1. Ketose: &gt;C=O, usually at C-2.</li></ul>"""),
        Q("1(B)(v)", 1, r"<p>(v) Colourless complex ion in the following is-</p>"
          r"<p>(a) [Cu(NH<sub>3</sub>)<sub>4</sub>]<sup>2+</sup><br>(b) [Zn(NH<sub>3</sub>)<sub>4</sub>]<sup>2+</sup><br>"
          r"(c) [Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup><br>(d) [Fe(CN)<sub>6</sub>]<sup>3-</sup></p>",
          a=r"""<p>\(\ce{Zn^2+}\) is 3d<sup>10</sup>: the d subshell is full, so no d&ndash;d transition is possible
and no visible light is absorbed. Cu<sup>2+</sup> (d<sup>9</sup>), Fe<sup>2+</sup> (d<sup>6</sup>) and
Fe<sup>3+</sup> (d<sup>5</sup>) all have partly filled d orbitals and are coloured.</p>
<p><span class="box">(b) [Zn(NH<sub>3</sub>)<sub>4</sub>]<sup>2+</sup></span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Colour needs a d&ndash;d transition: d<sup>0</sup> and d<sup>10</sup> ions are
colourless.</li></ul>"""),
        Q("1(B)(vi)", 1, r"<p>(vi) Given below are two statements marked Assertion and Reason. Read the two "
          r"statements carefully and select the correct option.</p>"
          r"<p><b>Assertion</b>: Tertiary alkyl halides are most reactive towards S<sub>N</sub>1 reaction.<br>"
          r"<b>Reason</b>: In S<sub>N</sub>1 reaction rate of reaction depends only on the concentration of alkyl "
          r"halide.</p>" + AR,
          a=r"""<p>Both statements are true. But the reason 3&deg; halides react fastest is the stability of the 3&deg;
carbocation formed in the slow step (hyperconjugation and +I effect of three alkyl groups), not the form of the
rate law (rate = k[RX] holds for all S<sub>N</sub>1 substrates).</p>
<p><span class="box">(b) Both true, but reason is not the correct explanation</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>S<sub>N</sub>1: rate = k[RX]; carbocation intermediate; reactivity 3&deg; &gt; 2&deg; &gt;
1&deg;.</li><li>S<sub>N</sub>2: rate = k[RX][Nu<sup>&minus;</sup>]; reactivity 1&deg; &gt; 2&deg; &gt; 3&deg;.</li></ul>"""),
        Q("1(B)(vii)", 1, r"<p>(vii) Given below are two statements marked Assertion and Reason. Read the two "
          r"statements carefully and select the correct option.</p>"
          r"<p><b>Assertion</b>: Actinoids form relatively more stable complexes as compared to lanthanoids.<br>"
          r"<b>Reason</b>: Actinoids can utilise their 5f orbitals along with 6d orbitals in bonding but lanthanoids "
          r"do not use their 4f orbital for bonding</p>" + AR,
          a=r"""<p>Actinoids have a greater tendency to form complexes. The 5f orbitals are less deeply buried than
the 4f, extend beyond the 6s/6p shells and can take part in bonding (with 6d), so actinoid&ndash;ligand bonds have
more covalent character; the 4f orbitals of lanthanoids are shielded and do not take part. The reason explains
the assertion.</p>
<p><span class="box">(a) Both true, and reason is the correct explanation</span></p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>4f: deeply buried, little part in bonding. 5f: more exposed, used in bonding &rarr; more
oxidation states and more complexes for actinoids.</li></ul>"""),
        Q("1(C)", 3, r"<p><b>C. Read the passage given below carefully and answer the questions that follow:</b> "
          r"[3]</p>"
          r"<p>In a reaction, the rates of disappearance of different reactants or rates of formation of different "
          r"products may not be equal but rate of reaction at any instant of time has the same value expected in "
          r"terms of any reactant or product. Further, the rate of reaction may not depend upon the stoichiometric "
          r"coefficients of the balanced chemical equation. The exact powers of molar concentrations of reactants on "
          r"which rate depend are found experimentally and expressed in terms of &lsquo;order of reaction&rsquo;. Each "
          r"reaction has a characteristics rate constant depends upon temperature. The units of the rate constant "
          r"depend upon the order of reaction.</p>"
          r"<p>(i) The rate constant of a reaction is found to be 3 x 10<sup>-3</sup> mol<sup>-2</sup>L<sup>2</sup>"
          r"sec<sup>-1</sup>. What is the order of the reaction?</p>"
          r"<p>(ii) If the half-life of a first order reaction is 50 minutes, what percentages of reactant will be "
          r"left after 250 minutes?</p>"
          r"<p>(iii) Rate of a reaction can be expressed by following rate expression, Rate = k[A]<sup>2</sup>[B]. If "
          r"concentration of A is increased by 3 times and concentration of B is increased by 2 times, by how many "
          r"times rate of reaction increases?</p>",
          a=r"""<p><b>(i)</b> Units of k for order n: (mol L<sup>&minus;1</sup>)<sup>1&minus;n</sup> s<sup>&minus;1</sup>.
Here mol<sup>&minus;2</sup> L<sup>2</sup> s<sup>&minus;1</sup> = (mol L<sup>&minus;1</sup>)<sup>&minus;2</sup>
s<sup>&minus;1</sup> &rArr; \(1 - n = -2\).</p>
<p><span class="box">n = 3: third order</span></p>
<p><b>(ii)</b> For a first-order reaction the half-life is independent of concentration.
Number of half-lives \(= \dfrac{250}{50} = 5\).</p>
<p>\[\frac{[\mathrm A]}{[\mathrm A]_0} = \left(\frac12\right)^5 = \frac1{32} = 0.03125\]</p>
<p><span class="box">3.125 % of the reactant is left</span></p>
<p><b>(iii)</b> \(\text{Rate}_2 = k(3[\mathrm A])^2(2[\mathrm B]) = 9\times2\,k[\mathrm A]^2[\mathrm B]\)</p>
<p><span class="box">The rate increases 18 times</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Units of k: (mol L<sup>&minus;1</sup>)<sup>1&minus;n</sup> time<sup>&minus;1</sup>.</li>
<li>First order: after n half-lives, fraction left = (1/2)<sup>n</sup>.</li>
<li>Rate = k[A]<sup>x</sup>[B]<sup>y</sup>: scaling [A] by a and [B] by b scales the rate by a<sup>x</sup>b<sup>y</sup>.</li></ul>"""),
        # ------------------------------------------------------------------ Section B
        SEC("Section-B (20 marks)"),
        Q("2", 2, r"<p>Sourav, a student of class 12 prepared a 0.01 M H<sub>2</sub>SO<sub>4</sub> solution and found "
          r"that its conductivity and equivalent conductivities are 1.65 &times; 10<sup>-4</sup> S cm<sup>-1</sup> and "
          r"16.5 S cm<sup>2</sup> eqv<sup>-1</sup>. Are these data justified? Explain.</p>",
          a=r"""<p>\(\ce{H2SO4}\) is dibasic: 1 mol = 2 g-equivalents, so
normality N = 2 &times; 0.01 = 0.02 N.</p>
<p>\[\Lambda_\text{eq} = \frac{1000\,\kappa}{N} = \frac{1000\times1.65\times10^{-4}}{0.02} = 8.25\ \text{S cm}^2\ \text{eq}^{-1}\]</p>
<p>\[\Lambda_m = \frac{1000\,\kappa}{M} = \frac{1000\times1.65\times10^{-4}}{0.01} = 16.5\ \text{S cm}^2\ \text{mol}^{-1}\]</p>
<p><span class="box">Not justified: with κ = 1.65 &times; 10<sup>&minus;4</sup> S cm<sup>&minus;1</sup> the equivalent
conductivity is 8.25 S cm<sup>2</sup> eq<sup>&minus;1</sup>. 16.5 is the <i>molar</i> conductivity
(Λ<sub>m</sub> = 2Λ<sub>eq</sub> for H<sub>2</sub>SO<sub>4</sub>).</span></p>
<p>Sourav has divided by the molarity instead of the normality.</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\Lambda_\text{eq} = 1000\kappa/N\), \(\Lambda_m = 1000\kappa/M\).</li>
<li>For \(\ce{H2SO4}\), N = 2M, so \(\Lambda_m = 2\Lambda_\text{eq}\).</li></ul>"""),
        Q("3", 2, r"<p>i) A compound having the molecular formula C<sub>3</sub>H<sub>6</sub>O forms a crystalline white "
          r"ppt. with sodium bisulphite and reduces Fehling&rsquo;s solution. Suggest the structural formula and IUPAC "
          r"name of this compound.</p>"
          r"<p>ii) CH<sub>3</sub>CHO is more reactive than CH<sub>3</sub>COCH<sub>3</sub> towards reaction with HCN. "
          r"Explain</p>",
          a=r"""<p><b>(i)</b> A bisulphite adduct shows a carbonyl compound; reducing Fehling's solution shows an
aldehyde (acetone, the other C<sub>3</sub>H<sub>6</sub>O carbonyl, does not reduce Fehling's).</p>
<p><span class="box">\(\ce{CH3CH2CHO}\), propanal</span></p>
<p>\(\ce{CH3CH2CHO + NaHSO3 -> CH3CH2CH(OH)SO3Na}\) (white crystalline adduct)</p>
<p>\(\ce{CH3CH2CHO + 2Cu^2+ + 5OH- -> CH3CH2COO- + Cu2O v + 3H2O}\) (red ppt.)</p>
<p><b>(ii)</b> Addition of HCN is a nucleophilic addition: \(\ce{CN-}\) attacks the carbonyl carbon.</p>
<ul><li><b>Electronic:</b> the two CH<sub>3</sub> groups of acetone push electrons (+I) to the carbonyl carbon and
reduce its positive character more than the one CH<sub>3</sub> of ethanal does.</li>
<li><b>Steric:</b> the two CH<sub>3</sub> groups crowd the carbonyl carbon of acetone and hinder the approach of
\(\ce{CN-}\); in ethanal one side carries only H.</li></ul>
<p>Hence ethanal is more reactive than propanone.</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>NaHSO<sub>3</sub> adduct: aldehydes and methyl ketones. Fehling's/Tollens': aldehydes only.</li>
<li>Reactivity to nucleophilic addition: HCHO &gt; RCHO &gt; R<sub>2</sub>CO (+I and steric effects).</li></ul>"""),
        Q("4", 2, r"<p>Devise a scheme for the preparation of</p><p>(i) methyl bromide to propan-2-one</p>"
          r"<p>(ii) benzene to diphenyl</p>",
          a=r"""<p><b>(i)</b> Make a nitrile and a Grignard reagent from methyl bromide and combine them:</p>
<p>\[\ce{CH3Br + KCN(alc) -> CH3CN + KBr}\]</p>
<p>\[\ce{CH3Br + Mg ->[dry ether] CH3MgBr}\]</p>
<p>\[\ce{CH3C#N + CH3MgBr -> (CH3)2C=NMgBr}\]</p>
<p>\[\ce{(CH3)2C=NMgBr + 2H2O ->[H+] CH3COCH3 + NH3 + Mg(OH)Br}\]</p>
<p><b>(ii)</b> Chlorinate benzene, then couple by the Fittig reaction:</p>
<p>\[\ce{C6H6 + Cl2 ->[\text{anhyd. } FeCl3] C6H5Cl + HCl}\]</p>
<p>\[\ce{2C6H5Cl + 2Na ->[dry ether] C6H5-C6H5 + 2NaCl}\]</p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Nitrile + RMgX, then hydrolysis &rarr; ketone (RCOR&prime;).</li>
<li>Fittig: 2 ArX + 2Na (dry ether) &rarr; Ar&ndash;Ar.</li></ul>"""),
        Q("5", 2, r"<p>The rate constant of a first order reaction at T K is given by the following expression</p>"
          r"<p>\[\log k = \frac{-3163}{T} + 11.9\]</p>"
          r"<p>K is expressed in min<sup>-1</sup>. What is the activation energy and half-life period of the "
          r"reaction at 20 <sup>o</sup>C?</p>",
          a=r"""<p>Compare with the Arrhenius equation in log form: \(\log k = \log A - \dfrac{E_a}{2.303RT}\).</p>
<p>\[\frac{E_a}{2.303R} = 3163 \;\Rightarrow\; E_a = 3163\times2.303\times8.314 = 6.06\times10^{4}\ \text{J mol}^{-1}\]</p>
<p><span class="box">\(E_a \approx 60.6\) kJ mol<sup>&minus;1</sup></span></p>
<p>At 20 &deg;C, T = 293 K: \(\log k = -\dfrac{3163}{293} + 11.9 = -10.795 + 11.9 = 1.105\)
&rArr; \(k = 12.7\) min<sup>&minus;1</sup>.</p>
<p>\[t_{1/2} = \frac{0.693}{k} = \frac{0.693}{12.7} = 0.0544\ \text{min}\]</p>
<p><span class="box">\(t_{1/2} \approx 5.44\times10^{-2}\) min (about 3.3 s)</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>\(\log k = \log A - \dfrac{E_a}{2.303RT}\): the coefficient of 1/T is \(-E_a/2.303R\).</li>
<li>First order: \(t_{1/2} = 0.693/k\).</li></ul>"""),
        Q("6", 2, r"<p>An aromatic compound &lsquo;A&rsquo; on treatment with aqueous ammonia and heating forms compound "
          r"&lsquo;B&rsquo; which on heating with Br<sub>2</sub> and KOH forms a compound &lsquo;C&rsquo; of molecular "
          r"formula C<sub>6</sub>H<sub>7</sub>N. Write the structures of A, B and C and state the name of the "
          r"reaction for the conversion of B to C.</p>",
          a=r"""<p>C<sub>6</sub>H<sub>7</sub>N = \(\ce{C6H5NH2}\), aniline. Br<sub>2</sub>/KOH on an amide removes one
carbon (Hofmann), so B is benzamide and A is benzoic acid.</p>
<p><span class="box">A = \(\ce{C6H5COOH}\) (benzoic acid); B = \(\ce{C6H5CONH2}\) (benzamide);
C = \(\ce{C6H5NH2}\) (aniline)</span></p>
<p>\[\ce{C6H5COOH + NH3(aq) -> C6H5COONH4 ->[\Delta] C6H5CONH2 + H2O}\]</p>
<p>\[\ce{C6H5CONH2 + Br2 + 4KOH ->[\Delta] C6H5NH2 + K2CO3 + 2KBr + 2H2O}\]</p>
<p>B &rarr; C: <span class="box">Hofmann bromamide degradation</span></p>
<p class="note">Benzoyl chloride (\(\ce{C6H5COCl}\)) would also give benzamide with ammonia and is an acceptable A.</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Hofmann bromamide: RCONH<sub>2</sub> + Br<sub>2</sub> + 4KOH &rarr; RNH<sub>2</sub> (one C
fewer) + K<sub>2</sub>CO<sub>3</sub> + 2KBr + 2H<sub>2</sub>O.</li>
<li>Acid + NH<sub>3</sub> &rarr; ammonium salt &rarr; (heat) amide.</li></ul>"""),
        Q("7", 2, r"<p>During chemistry class, a teacher wrote [Fe(CN)<sub>6</sub>]<sup>3-</sup> as a coordination "
          r"complex ion on the board. The students were asked to find out the hybridisation and magnetic character of "
          r"the complex. Pari, a student, wrote the answer sp<sup>3</sup>d<sup>2</sup> and diamagnetic whereas another "
          r"student Suhail wrote d<sup>2</sup>sp<sup>3</sup>and paramagnetic. Evaluate Pari&rsquo;s and Suhail&rsquo;s "
          r"responses.</p>",
          a=r"""<p>Fe in \(\ce{[Fe(CN)6]^3-}\): \(x + 6(-1) = -3 \Rightarrow x = +3\); \(\ce{Fe^3+}\) = [Ar]3d<sup>5</sup>.</p>
<p>\(\ce{CN-}\) is a strong-field ligand: it forces pairing, so the five electrons occupy three 3d orbitals
(2, 2, 1), leaving two inner 3d orbitals free. Two 3d + one 4s + three 4p &rarr; d<sup>2</sup>sp<sup>3</sup>
(inner-orbital, octahedral). One electron remains unpaired.</p>
{{fig:0}}
<p><span class="box">Suhail is correct: d<sup>2</sup>sp<sup>3</sup>, paramagnetic (1 unpaired e<sup>&minus;</sup>,
&mu; = &radic;3 &asymp; 1.73 BM). Pari is wrong on both counts.</span></p>
<p>sp<sup>3</sup>d<sup>2</sup> would need a weak-field ligand (outer-orbital, 5 unpaired electrons), and with an odd
number of electrons (d<sup>5</sup>) the complex can never be diamagnetic.</p>""",
          afig=[fg.fig_b_fecn6_vbt],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Strong-field ligands (CN<sup>&minus;</sup>, CO) &rarr; pairing &rarr; inner-orbital
d<sup>2</sup>sp<sup>3</sup>.</li>
<li>&mu; = &radic;(n(n+2)) BM; an odd-electron ion is always paramagnetic.</li></ul>"""),
        Q("8", 2, r"<p>How do you convert the following?</p><p>a) Phenol to anisole</p>"
          r"<p>b) Propan-2-one to 2-Methyl propan -2-ol</p>",
          a=r"""<p><b>(a)</b> Williamson synthesis: phenoxide ion + methyl halide.</p>
<p>\[\ce{C6H5OH + NaOH -> C6H5ONa + H2O}\]</p>
<p>\[\ce{C6H5ONa + CH3I -> C6H5OCH3 + NaI}\]</p>
<p><b>(b)</b> Grignard addition to the ketone, then hydrolysis gives a 3&deg; alcohol:</p>
<p>\[\ce{CH3COCH3 + CH3MgBr ->[dry ether] (CH3)3C-OMgBr}\]</p>
<p>\[\ce{(CH3)3C-OMgBr + H2O ->[H+] (CH3)3C-OH + Mg(OH)Br}\]</p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Williamson: RO<sup>&minus;</sup>/ArO<sup>&minus;</sup> + R&prime;X &rarr; ether (the halide must
be the alkyl part).</li>
<li>RMgX + HCHO &rarr; 1&deg;, + RCHO &rarr; 2&deg;, + ketone &rarr; 3&deg; alcohol.</li></ul>"""),
        Q("9(i)", 2, r"<p>(i) Identify the compounds [A] and [B] in each of the following reactions.</p>"
          r"<p>(a) \(\ce{C6H5CH2CH3 ->[\text{Alk. } KMnO4][H+] A ->[NaOH/CaO][\Delta] B}\)</p>"
          r"<p>(b) \(\ce{CH3COOH ->[SOCl2] A ->[H2][Pd/BaSO4] B}\)</p>",
          a=r"""<p><b>(a)</b> <span class="box">A = benzoic acid, \(\ce{C6H5COOH}\); B = benzene, \(\ce{C6H6}\)</span></p>
<p>Alkaline KMnO<sub>4</sub> oxidises the whole side chain (it has a benzylic H) to &ndash;COOH:</p>
<p>\[\ce{C6H5CH2CH3 + 6[O] ->[KMnO4/OH^-][\text{then } H+] C6H5COOH + CO2 + 2H2O}\]</p>
<p>Decarboxylation with soda-lime: \(\ce{C6H5COOH + 2NaOH ->[CaO][\Delta] C6H6 + Na2CO3 + H2O}\)</p>
<p><b>(b)</b> <span class="box">A = acetyl (ethanoyl) chloride, \(\ce{CH3COCl}\); B = acetaldehyde (ethanal),
\(\ce{CH3CHO}\)</span></p>
<p>\[\ce{CH3COOH + SOCl2 -> CH3COCl + SO2 + HCl}\]</p>
<p>\[\ce{CH3COCl + H2 ->[Pd/BaSO4] CH3CHO + HCl}\] (Rosenmund reduction)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Any alkyl side chain with a benzylic H is oxidised to &ndash;COOH by KMnO<sub>4</sub>.</li>
<li>Soda-lime decarboxylation removes CO<sub>2</sub>; Rosenmund (Pd/BaSO<sub>4</sub>, poisoned) stops at the
aldehyde.</li></ul>"""),
        Q("9(ii) OR", 2, r"<p style='text-align:center'>OR</p><p>(ii) Two moles of organic compound &lsquo;A&rsquo; on "
          r"treatment with a strong base gives two compound &lsquo;B&rsquo; and &lsquo;C&rsquo;. Compound &lsquo;B&rsquo; "
          r"on dehydrogenation with Cu gives &lsquo;A&rsquo; while acidification of &lsquo;C&rsquo; yields carboxylic "
          r"acid &lsquo;D&rsquo; with molecular formula of CH<sub>2</sub>O<sub>2</sub>. Identify the compounds A, B, C "
          r"and D.</p>",
          a=r"""<p>D = CH<sub>2</sub>O<sub>2</sub> = HCOOH, so C is a formate and A (with no &alpha;-H, two moles,
strong base) undergoes the Cannizzaro reaction: A = HCHO.</p>
<p>\[\ce{2HCHO + NaOH(\text{conc.}) -> CH3OH + HCOONa}\]</p>
<p>\[\ce{CH3OH ->[Cu][573 K] HCHO + H2}\qquad \ce{HCOONa + HCl -> HCOOH + NaCl}\]</p>
<p><span class="box">A = HCHO (methanal); B = CH<sub>3</sub>OH (methanol); C = HCOONa (sodium formate);
D = HCOOH (formic / methanoic acid)</span></p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Cannizzaro: aldehydes without &alpha;-H + conc. alkali &rarr; alcohol + carboxylate salt
(disproportionation).</li>
<li>Cu/573 K dehydrogenates 1&deg; alcohol &rarr; aldehyde.</li></ul>"""),
        Q("10", 2, r"<p>For the cell reaction: Ni(s) | Ni<sup>2+</sup>(aq) ||Ag<sup>+</sup>(aq) |Ag(s)</p>"
          r"<p>Calculate the equilibrium constant at 25&deg;C. How much maximum work would be obtained by operation "
          r"of this cell?</p><p>Given: E<sup>o</sup>(Ni<sup>2+</sup> /Ni) = -0.25 V and E<sup>o</sup>(Ag<sup>+</sup> "
          r"/Ag) = 0.80 V</p>",
          a=r"""<p>Cell reaction: \(\ce{Ni(s) + 2Ag+(aq) -> Ni^2+(aq) + 2Ag(s)}\), n = 2.</p>
<p>\(E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode} = 0.80 - (-0.25) = 1.05\) V.</p>
<p>\[\log K_c = \frac{nE^\circ_\text{cell}}{0.0591} = \frac{2\times1.05}{0.0591} = 35.53\]</p>
<p><span class="box">\(K_c = 3.4\times10^{35}\)</span></p>
<p>Maximum work = \(-\Delta G^\circ = nFE^\circ_\text{cell} = 2\times96500\times1.05 = 2.027\times10^{5}\) J</p>
<p><span class="box">Maximum work \(\approx 202.7\) kJ per mole of Ni</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>At 298 K: \(\log K_c = nE^\circ_\text{cell}/0.0591\).</li>
<li>\(\Delta G^\circ = -nFE^\circ_\text{cell}\) = &minus;(maximum useful work).</li></ul>"""),
        Q("11", 2, r"<p>Write the chemical test to distinguish between the following pairs of compounds.</p>"
          r"<p>(a) Methanol and ethanol<br>(b) Phenol and propan-2-ol</p>",
          a=r"""<p><b>(a) Iodoform test</b> &mdash; warm with I<sub>2</sub> and NaOH: ethanol (has CH<sub>3</sub>CH(OH)&ndash;)
gives a yellow precipitate of iodoform; methanol gives none.</p>
<p>\[\ce{CH3CH2OH + 4I2 + 6NaOH -> CHI3 v + HCOONa + 5NaI + 5H2O}\]</p>
<p><b>(b) Neutral FeCl<sub>3</sub> test</b> &mdash; phenol gives a violet colour; propan-2-ol gives no colour.</p>
<p>\[\ce{6C6H5OH + FeCl3 -> [Fe(OC6H5)6]^3- + 3H+ + 3HCl}\] (violet)</p>
<p class="note">Alternatively: bromine water gives a white precipitate of 2,4,6-tribromophenol with phenol only;
or the iodoform test is positive for propan-2-ol and negative for phenol.</p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Iodoform test: positive for CH<sub>3</sub>CH(OH)&ndash; and CH<sub>3</sub>CO&ndash;
(ethanol is the only 1&deg; alcohol that gives it).</li>
<li>Phenols: violet with neutral FeCl<sub>3</sub>; white ppt. with Br<sub>2</sub> water.</li></ul>"""),
        # ------------------------------------------------------------------ Section C
        SEC("Section- C (21 marks)"),
        Q("12", 3, r"<p>Identify the compounds [A], [B] and [C] in the following reactions.</p>"
          r"<p>i) \(\ce{C6H5NO2 ->[Fe/HCl] A ->[NaNO2 + HCl][\text{0–5 °C}] B ->[KI] C}\)</p>"
          r"<p>ii) \(\ce{CH3Cl ->[KCN] A ->[LiAlH4] B ->[CHCl3 + \text{alc. } KOH][\Delta] C}\)</p>",
          a=r"""<p><b>(i)</b> <span class="box">A = aniline; B = benzenediazonium chloride; C = iodobenzene</span></p>
<p>\(\ce{C6H5NO2 + 6[H] ->[Fe/HCl] C6H5NH2 + 2H2O}\)</p>
<p>\(\ce{C6H5NH2 + NaNO2 + 2HCl ->[273-278 K] C6H5N2+Cl- + NaCl + 2H2O}\)</p>
<p>\(\ce{C6H5N2+Cl- + KI -> C6H5I + KCl + N2 ^}\)</p>
<p><b>(ii)</b> <span class="box">A = CH<sub>3</sub>CN (ethanenitrile); B = CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub>
(ethanamine); C = CH<sub>3</sub>CH<sub>2</sub>NC (ethyl isocyanide)</span></p>
<p>\(\ce{CH3Cl + KCN -> CH3CN + KCl}\)</p>
<p>\(\ce{CH3C#N + 4[H] ->[LiAlH4] CH3CH2NH2}\)</p>
<p>\(\ce{CH3CH2NH2 + CHCl3 + 3KOH(alc) ->[\Delta] CH3CH2NC + 3KCl + 3H2O}\) (carbylamine reaction; offensive
smell)</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>&ndash;N<sub>2</sub><sup>+</sup> is replaced by I with KI directly (no Cu catalyst).</li>
<li>Nitrile + LiAlH<sub>4</sub> &rarr; 1&deg; amine (same carbons); carbylamine test: 1&deg; amines only.</li></ul>"""),
        Q("13", 3, r"<p>The van 't Hoff factor is a measure of the effect of a solute upon colligative properties such "
          r"as osmotic pressure, relative lowering in vapour pressure, the elevation of boiling point and freezing "
          r"point depression. It is the ratio between the actual concentration of particles produced when the "
          r"substance is dissolved, and the concentration of a substance as calculated from its mass.</p>"
          r"<p>Consider the two cases given below and answer the questions that follow.</p>"
          r"<p>(A) The freezing point depression of a solution containing 2 g benzoic acid in 25 g of benzene is "
          r"1.62 K. (K<sub>f</sub> for benzene is 4.9 K kg mol<sup>-1</sup>)<br>"
          r"(B) A 0.15 M aqueous solution of KCl exerts an osmotic pressure of 6.8 atm at 310 K.</p>"
          r"<p>Answer the following questions.</p>"
          r"<p>(i) Calculate the van&rsquo;t Hoff factor in each case.<br>"
          r"(ii) Inferring the value of van&rsquo;t Hoff factor in both the cases, find out which solution undergoes "
          r"association and which solution undergoes dissociation.<br>"
          r"(iii) Given below is the increasing order of elevation in boiling point of water observed for the "
          r"following solutions.<br>0.1 molal glucose &lt; 0.1 molal NaCl &lt; 0.1 molal K<sub>2</sub>SO<sub>4</sub>."
          r"<br>Provide a reason to explain if the above ordered arrangement is correct or not</p>",
          a=r"""<p><b>(i) Case (A)</b> &mdash; benzoic acid, \(\ce{C6H5COOH}\), M = 122 g mol<sup>&minus;1</sup>.</p>
<p>\[\Delta T_f(\text{calc}) = \frac{K_f\times w\times1000}{M\times W} = \frac{4.9\times2\times1000}{122\times25} = 3.21\ \text{K}\]</p>
<p>\[i = \frac{\Delta T_f(\text{obs})}{\Delta T_f(\text{calc})} = \frac{1.62}{3.21} = 0.504\]</p>
<p><span class="box">i(A) &asymp; 0.50</span></p>
<p><b>Case (B)</b> &mdash; \(\pi = iCRT\):</p>
<p>\[i = \frac{\pi}{CRT} = \frac{6.8}{0.15\times0.0821\times310} = \frac{6.8}{3.818} = 1.78\]</p>
<p><span class="box">i(B) &asymp; 1.78</span></p>
<p><b>(ii)</b> i &lt; 1 means fewer particles than formula units: <b>benzoic acid in benzene associates</b>
(dimerises through hydrogen bonds, \(\ce{2C6H5COOH <=> (C6H5COOH)2}\)). i &gt; 1 means more particles:
<b>KCl in water dissociates</b> (\(\ce{KCl -> K+ + Cl-}\), 78 % dissociated).</p>
<p><b>(iii)</b> \(\Delta T_b = iK_bm\). At the same molality (0.1 m) and the same solvent, \(\Delta T_b \propto i\):
glucose i = 1 (non-electrolyte), NaCl i &asymp; 2, K<sub>2</sub>SO<sub>4</sub> i &asymp; 3. So
\(\Delta T_b\): glucose &lt; NaCl &lt; K<sub>2</sub>SO<sub>4</sub>.</p>
<p><span class="box">The order is correct</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>i = observed colligative property / calculated = calculated M / observed M.</li>
<li>i &lt; 1: association; i &gt; 1: dissociation.</li>
<li>\(\Delta T_b = iK_bm\), \(\Delta T_f = iK_fm\), \(\pi = iCRT\).</li></ul>"""),
        Q("14", 3, r"<p>Write chemical equations to illustrate the following name reactions.</p>"
          r"<p>(i) Wolff&ndash;Kishner reduction<br>(ii) Perkin Reaction<br>(iii) Benzoin condensation</p>",
          a=r"""<p><b>(i) Wolff&ndash;Kishner reduction</b> &mdash; the carbonyl group is reduced to CH<sub>2</sub> via
the hydrazone, heated with KOH in ethylene glycol:</p>
<p>\[\ce{CH3COCH3 + NH2NH2 ->[-H2O] (CH3)2C=NNH2}\]</p>
<p>\[\ce{(CH3)2C=NNH2 ->[KOH/\text{ethylene glycol}][\Delta] CH3CH2CH3 + N2 ^}\]</p>
<p><b>(ii) Perkin reaction</b> &mdash; an aromatic aldehyde heated with an acid anhydride and the sodium salt of
the same acid gives an &alpha;,&beta;-unsaturated acid:</p>
<p>\[\ce{C6H5CHO + (CH3CO)2O ->[CH3COONa][\text{453 K}] C6H5CH=CHCOOH + CH3COOH}\]</p>
<p>(cinnamic acid, 3-phenylprop-2-enoic acid)</p>
<p><b>(iii) Benzoin condensation</b> &mdash; two molecules of benzaldehyde, warmed with alcoholic KCN:</p>
<p>\[\ce{2C6H5CHO ->[\text{alc. } KCN][\Delta] C6H5CH(OH)COC6H5}\]</p>
<p>(benzoin, 2-hydroxy-1,2-diphenylethanone)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Wolff&ndash;Kishner: C=O &rarr; CH<sub>2</sub> in base; Clemmensen: Zn-Hg/HCl, in acid.</li>
<li>Perkin: ArCHO + (RCH<sub>2</sub>CO)<sub>2</sub>O / RCH<sub>2</sub>COONa &rarr; ArCH=C(R)COOH.</li>
<li>Benzoin: CN<sup>&minus;</sup> catalyst, 2 ArCHO &rarr; ArCH(OH)COAr.</li></ul>"""),
        Q("15", 3, r"<p>i) Anhydrous CuSO<sub>4</sub> is white while hydrated CuSO<sub>4</sub> is blue in colour. "
          r"Explain</p>"
          r"<p>ii) On the basis of Crystal Field Theory, calculate the crystal field stabilization energy (CFSE) of "
          r"Mn<sup>3+</sup> in [Mn(CN)<sub>6</sub>]<sup>3&ndash;</sup> and [MnCl<sub>6</sub>]<sup>3&ndash;</sup></p>",
          a=r"""<p><b>(i)</b> \(\ce{Cu^2+}\) is 3d<sup>9</sup>. In \(\ce{CuSO4.5H2O}\) water molecules are coordinated to
Cu<sup>2+</sup> as ligands; their field splits the d orbitals (t<sub>2g</sub> and e<sub>g</sub>), and an electron
can be promoted from t<sub>2g</sub> to the half-empty e<sub>g</sub> level by absorbing red-orange light: the
complementary colour, <b>blue</b>, is seen. In anhydrous CuSO<sub>4</sub> there are no water ligands, so
(in the CFT picture) the crystal field splitting does not occur in the visible region, no d&ndash;d transition
takes place and the salt is <b>white</b>.</p>
{{fig:0}}
<p><b>(ii)</b> Mn<sup>3+</sup> = [Ar]3d<sup>4</sup>. CFSE = (&minus;0.4n<sub>t2g</sub> + 0.6n<sub>eg</sub>)Δ<sub>o</sub>
(+ P for each extra pair forced by the field).</p>
<p>[Mn(CN)<sub>6</sub>]<sup>3&minus;</sup>: CN<sup>&minus;</sup> is strong field (Δ<sub>o</sub> &gt; P), low spin
t<sub>2g</sub><sup>4</sup>e<sub>g</sub><sup>0</sup>:</p>
<p>\[\text{CFSE} = 4(-0.4\Delta_o) + 0 = -1.6\Delta_o\ (+P)\]</p>
<p>[MnCl<sub>6</sub>]<sup>3&minus;</sup>: Cl<sup>&minus;</sup> is weak field (Δ<sub>o</sub> &lt; P), high spin
t<sub>2g</sub><sup>3</sup>e<sub>g</sub><sup>1</sup>:</p>
<p>\[\text{CFSE} = 3(-0.4\Delta_o) + 1(+0.6\Delta_o) = -0.6\Delta_o\]</p>
{{fig:1}}
<p><span class="box">[Mn(CN)<sub>6</sub>]<sup>3&minus;</sup>: &minus;1.6 Δ<sub>o</sub> (+P);
[MnCl<sub>6</sub>]<sup>3&minus;</sup>: &minus;0.6 Δ<sub>o</sub></span></p>""",
          afig=[(fg.fig_b_cu_dd, "d–d transition in hydrated Cu²⁺"), fg.fig_b_mn_cft],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Octahedral field: t<sub>2g</sub> at &minus;0.4Δ<sub>o</sub>, e<sub>g</sub> at +0.6Δ<sub>o</sub>.</li>
<li>Δ<sub>o</sub> &gt; P: low spin; Δ<sub>o</sub> &lt; P: high spin.</li>
<li>Colour = complementary to the light absorbed in the d&ndash;d transition.</li></ul>"""),
        Q("16(i)", 3, r"<p>(i) A cell is prepared by dipping copper rod in 1 M copper sulphate solution and zinc rod "
          r"in 1 M zinc sulphate solution. The standard reduction potential of copper and zinc are 0.34 V and "
          r"&ndash;0.76 V respectively.</p><p>(i) What will be the cell reaction?<br>"
          r"(ii) What will be the standard electromotive force of the cell?<br>"
          r"(iii) Calculate the standard free energy change of the reaction.</p>",
          a=r"""<p>Zn (lower reduction potential) is the anode, Cu the cathode.</p>
<p><b>(i)</b> Anode: \(\ce{Zn -> Zn^2+ + 2e-}\); cathode: \(\ce{Cu^2+ + 2e- -> Cu}\).</p>
<p><span class="box">\(\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}\)</span></p>
<p><b>(ii)</b> \(E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode} = 0.34 - (-0.76)\)
<span class="box">\(E^\circ_\text{cell} = 1.10\) V</span></p>
<p><b>(iii)</b> \[\Delta G^\circ = -nFE^\circ_\text{cell} = -2\times96500\times1.10 = -2.123\times10^{5}\ \text{J mol}^{-1}\]</p>
<p><span class="box">\(\Delta G^\circ = -212.3\) kJ mol<sup>&minus;1</sup></span></p>
{{fig:0}}""",
          afig=[(fg.fig_b_daniell, "Daniell cell: Zn | ZnSO₄(1 M) || CuSO₄(1 M) | Cu")],
          topic="Electrochemistry",
          recall=r"""<ul><li>\(E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode}\) (reduction potentials).</li>
<li>\(\Delta G^\circ = -nFE^\circ_\text{cell}\), F = 96500 C mol<sup>&minus;1</sup>.</li></ul>"""),
        Q("16 OR", 3, r"<p style='text-align:center'>OR</p><p>(i) A solution of Ni(NO<sub>3</sub>)<sub>2</sub> is "
          r"electrolyzed between platinum electrode. How many moles of Ni will be deposited at the cathode if 5 "
          r"ampere of electricity is passed for 2 hours?</p>"
          r"<p>(ii) Write the anode and cathode reaction occurring in a lead storage battery during discharging of "
          r"cell.</p>",
          a=r"""<p><b>(i)</b> \(Q = It = 5\ \text{A}\times(2\times3600)\ \text{s} = 36000\) C.</p>
<p>\(\ce{Ni^2+ + 2e- -> Ni}\): 2 F (2 &times; 96500 C) deposit 1 mol Ni.</p>
<p>\[n(\ce{Ni}) = \frac{36000}{2\times96500} = 0.187\ \text{mol}\]</p>
<p><span class="box">0.187 mol Ni (&asymp; 10.9 g)</span></p>
<p><b>(ii)</b> On discharge (electrolyte: dil. \(\ce{H2SO4}\)):</p>
<p>Anode (&minus;, Pb): \(\ce{Pb(s) + SO4^2-(aq) -> PbSO4(s) + 2e-}\)</p>
<p>Cathode (+, PbO<sub>2</sub>): \(\ce{PbO2(s) + SO4^2-(aq) + 4H+(aq) + 2e- -> PbSO4(s) + 2H2O(l)}\)</p>
<p>Overall: \(\ce{Pb + PbO2 + 2H2SO4 -> 2PbSO4 + 2H2O}\)</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Moles deposited \(= \dfrac{It}{nF}\).</li>
<li>Lead accumulator: both electrodes become PbSO<sub>4</sub> on discharge; acid density falls.</li></ul>"""),
        Q("17", 3, r"<p>(i) Give reasons</p>"
          r"<p>(a) On electrolysis in acidic solution amino acids migrate towards cathode while in alkaline solution "
          r"these migrate towards anode.<br>"
          r"(b) Fructose gives silver mirror test although it contains a keto group.</p>"
          r"<p>(ii) Name the nitrogen bases present in DNA.</p>",
          a=r"""<p><b>(i)(a)</b> An amino acid exists as a dipolar ion (zwitterion), \(\ce{H3N+-CHR-COO-}\).</p>
<ul><li>In acid the \(\ce{-COO^-}\) is protonated, giving a cation, which moves to the <b>cathode</b>:
\(\ce{H3N+-CHR-COO- + H+ -> H3N+-CHR-COOH}\)</li>
<li>In alkali the \(\ce{-NH3^+}\) loses a proton, giving an anion, which moves to the <b>anode</b>:
\(\ce{H3N+-CHR-COO- + OH- -> H2N-CHR-COO- + H2O}\)</li></ul>
<p>(At the isoelectric point the zwitterion does not migrate.)</p>
<p><b>(b)</b> The silver mirror (Tollens') test is done in an alkaline medium. In alkali fructose, an
&alpha;-hydroxy ketone, isomerises through an enediol intermediate to glucose and mannose, which have a free
&ndash;CHO group and reduce \(\ce{[Ag(NH3)2]+}\) to metallic silver. So fructose behaves as a reducing sugar.</p>
<p>\[\ce{-CO-CH2OH <=>[OH-] -C(OH)=CH(OH) <=>[OH-] -CH(OH)-CHO}\]</p>
<p><b>(ii)</b> <span class="box">Adenine (A) and guanine (G) &mdash; purines; cytosine (C) and thymine (T)
&mdash; pyrimidines</span></p>
<p>(RNA has uracil in place of thymine.)</p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Zwitterion: cation in acid, anion in base, neutral at the isoelectric point.</li>
<li>Fructose is a reducing sugar (&alpha;-hydroxy ketone; enolisation in alkali).</li>
<li>DNA: A, G, C, T; RNA: A, G, C, U.</li></ul>"""),
        Q("18", 3, r"<p>Consider the data given below for the reaction 2NO<sub>2</sub> + F<sub>2</sub> &rarr; "
          r"2NO<sub>2</sub>F</p>"
          r"<table class='tbl'><tr><th>Sl. No.</th><th>[NO<sub>2</sub>]<sub>o</sub>, mol L<sup>-1</sup></th>"
          r"<th>[F<sub>2</sub>]<sub>o</sub>, mol L<sup>-1</sup></th><th>Rate, mol L<sup>-1</sup>min<sup>-1</sup></th></tr>"
          r"<tr><td>1</td><td>0.20</td><td>0.05</td><td>6 &times; 10<sup>-3</sup></td></tr>"
          r"<tr><td>2</td><td>0.40</td><td>0.05</td><td>1.2 &times; 10<sup>-2</sup></td></tr>"
          r"<tr><td>3</td><td>0.80</td><td>0.10</td><td>4.8 &times; 10<sup>-2</sup></td></tr></table>"
          r"<p>Answer the following questions.</p>"
          r"<p>(i) What is the order of reaction with respect to NO<sub>2</sub> and F<sub>2</sub>?<br>"
          r"(ii) Write the rate law<br>(iii) Calculate the rate constant.</p>",
          a=r"""<p>Let rate \(= k[\ce{NO2}]^x[\ce{F2}]^y\).</p>
<p><b>(i)</b> Experiments 1 and 2 ([F<sub>2</sub>] constant):
\(\dfrac{1.2\times10^{-2}}{6\times10^{-3}} = \left(\dfrac{0.40}{0.20}\right)^x \Rightarrow 2 = 2^x \Rightarrow x = 1\).</p>
<p>Experiments 2 and 3 (both concentrations doubled):
\(\dfrac{4.8\times10^{-2}}{1.2\times10^{-2}} = 2^x\cdot2^y \Rightarrow 4 = 2\cdot2^y \Rightarrow y = 1\).</p>
<p><span class="box">First order in NO<sub>2</sub> and first order in F<sub>2</sub> (overall second order)</span></p>
<p><b>(ii)</b> <span class="box">Rate = k[NO<sub>2</sub>][F<sub>2</sub>]</span></p>
<p><b>(iii)</b> From experiment 1:</p>
<p>\[k = \frac{\text{Rate}}{[\ce{NO2}][\ce{F2}]} = \frac{6\times10^{-3}}{0.20\times0.05} = 0.6\ \text{L mol}^{-1}\ \text{min}^{-1}\]</p>
<p><span class="box">k = 0.6 L mol<sup>&minus;1</sup> min<sup>&minus;1</sup></span> (experiments 2 and 3 give the same
value).</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Initial-rate method: compare two runs in which only one concentration changes.</li>
<li>Order is found experimentally &mdash; not from the stoichiometric coefficients (here 2 for NO<sub>2</sub>).</li>
<li>Units of k for second order: L mol<sup>&minus;1</sup> time<sup>&minus;1</sup>.</li></ul>"""),
        # ------------------------------------------------------------------ Section D
        SEC("Section- D (15 marks)"),
        Q("19", 5, r"<p>Alcohol is the main ingredient in alcoholic beverages. They are also used in ink, pharma, ink "
          r"and many other industries. Alcohols are mostly colourless, and they usually exist in the liquid state. "
          r"Phenols are mainly used in medicinal products as antiseptic agents. Phenol is also an antiseptic in low "
          r"concentration (0.2%) whereas 2% solution of phenol is used as disinfectant. The fragrance of rose is due "
          r"to citronellol (unsaturated alcohol).</p>"
          r"<p>(a) How would you prepare of phenol from chlorobenzene?<br>"
          r"(b) Phenol, when it first reacts with concentrated sulphuric acid, forms Y. The compound, Y is reacted "
          r"with concentrated nitric acid to form Z. Identify Y and Z.<br>"
          r"(c) What do you observe when phenol is treated with alkaline solution of benzene diazonium chloride at "
          r"0 <sup>o</sup>C to 5 <sup>o</sup>C? Also give the balanced chemical equation.<br>"
          r"(d) Give balanced chemical equation for the conversion of phenol to salicylic acid.</p>",
          a=r"""<p><b>(a) Dow's process</b> &mdash; chlorobenzene is fused with NaOH at 623 K and 300 atm, and the
sodium phenoxide formed is acidified:</p>
<p>\[\ce{C6H5Cl + 2NaOH ->[\text{623 K}][\text{300 atm}] C6H5ONa + NaCl + H2O}\]</p>
<p>\[\ce{C6H5ONa + HCl -> C6H5OH + NaCl}\]</p>
<p><b>(b)</b> Sulphonation first (the &ndash;SO<sub>3</sub>H groups protect the ring from oxidation by conc.
HNO<sub>3</sub>), then nitration replaces them:</p>
<p>\[\ce{C6H5OH + 2H2SO4 -> C6H3(OH)(SO3H)2 + 2H2O}\]</p>
<p>\[\ce{C6H3(OH)(SO3H)2 + 3HNO3 -> C6H2(OH)(NO2)3 + 2H2SO4 + H2O}\]</p>
<p><span class="box">Y = phenol-2,4-disulphonic acid; Z = 2,4,6-trinitrophenol (picric acid)</span></p>
{{fig:0}}
<p><b>(c)</b> An <b>orange (orange-red) dye</b> separates: the diazonium ion couples with phenol at the
para position (azo coupling), giving p-hydroxyazobenzene.</p>
<p>\[\begin{aligned}&\ce{C6H5N2+Cl- + C6H5OH + NaOH}\\ &\qquad\ce{->[\text{273–278 K}] C6H5-N=N-C6H4OH + NaCl + H2O}\end{aligned}\]</p>
{{fig:1}}
<p><b>(d) Kolbe's reaction</b> &mdash; sodium phenoxide with CO<sub>2</sub> at 400 K and 4&ndash;7 atm, then
acidification:</p>
<p>\[\ce{C6H5OH + NaOH -> C6H5ONa + H2O}\]</p>
<p>\[\ce{C6H5ONa + CO2 ->[\text{400 K}][\text{4–7 atm}] C6H4(OH)COONa}\]</p>
<p>\[\ce{C6H4(OH)COONa + HCl -> C6H4(OH)COOH + NaCl}\] (salicylic acid, 2-hydroxybenzoic acid)</p>
{{fig:2}}""",
          afig=[fg.fig_b_picric, fg.fig_b_azo, fg.fig_b_kolbe],
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Dow's process: C<sub>6</sub>H<sub>5</sub>Cl + NaOH, 623 K, 300 atm.</li>
<li>Picric acid via phenol-2,4-disulphonic acid (direct conc. HNO<sub>3</sub> oxidises phenol).</li>
<li>Azo coupling with phenol: mildly alkaline, para position, orange dye.</li>
<li>Kolbe: phenoxide + CO<sub>2</sub> &rarr; ortho-hydroxybenzoic acid.</li></ul>"""),
        Q("20", 5, r"<p>i. Give the IUPAC name of the following:</p>"
          r"<p>a) [Pt(NH<sub>3</sub>)<sub>2</sub>Cl(NO<sub>2</sub>)] &nbsp;&nbsp;&nbsp; "
          r"b) Fe<sub>4</sub>[Fe(CN)<sub>6</sub>]<sub>3</sub></p>"
          r"<p>ii) State the type of isomerism exhibited by [Co(NH<sub>3</sub>)<sub>5</sub>Br]SO<sub>4</sub> and "
          r"[Co(NH<sub>3</sub>)<sub>5</sub>(SO<sub>4</sub>)] Br.</p>"
          r"<p>iii) Using valance bond theory, predict the hybridisation and magnetic behaviour of "
          r"[Co(NH<sub>3</sub>)<sub>6</sub>]<sup>3+</sup>.</p>"
          r"<p>iv) Draw the optical isomers of [CoCl<sub>2</sub>(en)<sub>2</sub>]<sup>+</sup></p>"
          r"<p class='note'>[The paper prints the cobalt symbol in (ii) as &lsquo;C<sub>O</sub>&rsquo;; it is Co.]</p>",
          a=r"""<p><b>(i)(a)</b> Neutral complex; Pt: \(x + 0 - 1 - 1 = 0 \Rightarrow x = +2\). Ligands in alphabetical
order (ammine, chlorido, nitrito-N):</p>
<p><span class="box">diamminechloridonitrito-N-platinum(II)</span></p>
<p><b>(b)</b> Anion \(\ce{[Fe(CN)6]^4-}\) (Fe +2); four \(\ce{Fe^3+}\) cations balance three anions
(4 &times; 3 = 3 &times; 4).</p>
<p><span class="box">iron(III) hexacyanidoferrate(II)</span> (Prussian blue)</p>
<p><b>(ii)</b> The two compounds have the same formula but exchange an ion between the coordination sphere and
the counter-ion, so they give different ions in solution: the first gives \(\ce{SO4^2-}\) (white ppt. with
BaCl<sub>2</sub>), the second gives \(\ce{Br-}\) (pale yellow ppt. with AgNO<sub>3</sub>).</p>
<p><span class="box">Ionisation isomerism</span></p>
<p><b>(iii)</b> \(\ce{Co^3+}\) = [Ar]3d<sup>6</sup>. NH<sub>3</sub> acts as a strong-field ligand towards
Co<sup>3+</sup>: the four unpaired 3d electrons pair up into three orbitals, leaving two 3d orbitals empty for
d<sup>2</sup>sp<sup>3</sup> hybridisation.</p>
{{fig:0}}
<p><span class="box">d<sup>2</sup>sp<sup>3</sup> (inner-orbital, octahedral); no unpaired electron &mdash;
diamagnetic</span></p>
<p><b>(iv)</b> Only the <b>cis</b> isomer is optically active: it has no plane of symmetry and its mirror image is
non-superimposable, giving a pair of enantiomers (d and l forms).</p>
{{fig:1}}
<p>The trans isomer has a plane of symmetry (through Co and the two en ligands) and is optically inactive:</p>
{{fig:2}}""",
          afig=[fg.fig_b_conh36_vbt,
                (fg.fig_b_cocl2en2_optical, "The two optical isomers of cis-[CoCl₂(en)₂]⁺ (wedge = towards viewer, dashed = away)"),
                (fg.fig_b_trans_cocl2en2, "trans-[CoCl₂(en)₂]⁺ — superimposable on its mirror image")],
          topic="Coordination Compounds",
          recall=r"""<ul><li>IUPAC: ligands alphabetically, then metal with oxidation state; anionic complex ends in
&ndash;ate (iron &rarr; ferrate).</li>
<li>Ionisation isomers give different ions in solution.</li>
<li>[M(AA)<sub>2</sub>B<sub>2</sub>]: cis is chiral (two enantiomers), trans is achiral.</li></ul>"""),
        Q("21(i)", 5, r"<p>i) The properties of the solutions which depend only on the number of solute particles but "
          r"not on the nature of the solute are called colligative properties. Relative lowering in vapour pressure, "
          r"boiling point elevation, freezing point depression and osmotic pressure are colligative properties of a "
          r"solution which are widely used for the determination of molar mass of a compound.</p>"
          r"<p>a) Which colligative property is preferred for the molar mass determination of macromolecules?</p>"
          r"<p>b) What would be the molar mass of compound if 6.21 g of it is dissolved in 24.0 g of CHCl<sub>3</sub> "
          r"from a solution that has a boiling point of 68.04&ordm;C. The boiling point of pure chloroform is "
          r"61.7&ordm;C and the boiling point elevation constant K<sub>b</sub> for chloroform is 3.63&ordm;C/m</p>"
          r"<p>c) Why the freezing point depression of 0.4 M NaCl is nearly twice than that 0.4 M glucose "
          r"solution?</p>",
          a=r"""<p><b>(a)</b> <span class="box">Osmotic pressure</span></p>
<p>Macromolecules (polymers, proteins) have very large molar masses, so a solution of reasonable concentration
contains very few moles of solute: \(\Delta T_b\) and \(\Delta T_f\) would be far too small to measure, but the
osmotic pressure is measurable. It is also measured at room temperature, so heat-sensitive biomolecules are not
damaged.</p>
<p><b>(b)</b> \(\Delta T_b = 68.04 - 61.7 = 6.34\) &deg;C.</p>
<p>\[M = \frac{K_b\times w\times1000}{\Delta T_b\times W} = \frac{3.63\times6.21\times1000}{6.34\times24.0} = 148\ \text{g mol}^{-1}\]</p>
<p><span class="box">M &asymp; 148 g mol<sup>&minus;1</sup></span></p>
<p><b>(c)</b> Depression of freezing point is a colligative property: \(\Delta T_f = iK_fm\), proportional to the
number of solute particles. NaCl is a strong electrolyte, \(\ce{NaCl -> Na+ + Cl-}\), so 0.4 M NaCl gives about
0.8 M of particles (i &asymp; 2); glucose does not dissociate (i = 1). Hence \(\Delta T_f\)(NaCl) &asymp;
2 &times; \(\Delta T_f\)(glucose). (It is slightly less than twice because of interionic attraction.)</p>""",
          topic="Solutions",
          recall=r"""<ul><li>\(M_2 = \dfrac{K_b w_2 \times 1000}{\Delta T_b w_1}\).</li>
<li>Osmotic pressure: best for macromolecules (large, measurable at room temperature).</li>
<li>\(\Delta T_f = iK_fm\); i = number of particles per formula unit.</li></ul>"""),
        Q("21(ii) OR", 5, r"<p style='text-align:center'>OR</p><p>ii) a) Calculate the freezing point depression "
          r"expected for 0.0711 molal aqueous solution of Na<sub>2</sub>SO<sub>4</sub>. If this solution freezes at "
          r"&ndash; 0.320&ordm;C, what would be the value of van&rsquo;t Hoff factor? (K<sub>f</sub> = 1.86&ordm;C "
          r"mol<sup>-1</sup>)</p>"
          r"<p>b) Calculate the osmotic pressure at 20<sup>o</sup>C of a suspension containing 60g/l of solid "
          r"particles each particle having a mass of 10<sup>-9</sup> grams (1 nanogram).</p>"
          r"<p>c) Ramesh took 10 g of glucose to prepare 500 ml aqueous solution of it and observed the boiling point "
          r"of the solution as 100.05 <sup>o</sup>C. Now, he prepared two more solutions:<br>"
          r"i) 10 g sucrose dissolved in 500 ml water<br>ii) 10 g glucose in 500 ml acetic acid<br>"
          r"Does the boiling point will remain same in each case?</p>"
          r"<p class='note'>[K<sub>f</sub> is printed as 1.86&ordm;C mol<sup>&minus;1</sup>; its unit is &deg;C kg "
          r"mol<sup>&minus;1</sup>.]</p>",
          a=r"""<p><b>(a)</b> Expected depression (calculated as for an undissociated solute):</p>
<p>\[\Delta T_f(\text{calc}) = K_fm = 1.86\times0.0711 = 0.132\ ^\circ\text{C}\]</p>
<p>Observed \(\Delta T_f = 0 - (-0.320) = 0.320\) &deg;C.</p>
<p>\[i = \frac{\Delta T_f(\text{obs})}{\Delta T_f(\text{calc})} = \frac{0.320}{0.132} = 2.42\]</p>
<p><span class="box">\(\Delta T_f\)(expected) = 0.132 &deg;C; i &asymp; 2.42</span></p>
<p>(Complete dissociation, \(\ce{Na2SO4 -> 2Na+ + SO4^2-}\), would give i = 3 and \(\Delta T_f\) = 0.397 &deg;C;
the smaller observed value shows incomplete dissociation / ion association.)</p>
<p><b>(b)</b> Number of particles per litre \(= \dfrac{60\ \text{g}}{10^{-9}\ \text{g}} = 6\times10^{10}\).</p>
<p>\[C = \frac{6\times10^{10}}{6.023\times10^{23}} = 9.96\times10^{-14}\ \text{mol L}^{-1}\]</p>
<p>\[\pi = CRT = 9.96\times10^{-14}\times0.0821\times293 = 2.40\times10^{-12}\ \text{atm}\]</p>
<p><span class="box">\(\pi \approx 2.4\times10^{-12}\) atm (\(\approx 2.4\times10^{-7}\) Pa)</span> &mdash; negligibly small,
because the particles are so heavy that there are very few of them.</p>
<p><b>(c)</b> <span class="box">No &mdash; the boiling point changes in both cases.</span></p>
<ul><li><b>(i) Sucrose in water:</b> \(\Delta T_b \propto\) moles of solute \(= w/M\). Same mass, but M(sucrose) = 342
against M(glucose) = 180, so fewer moles:
\(\Delta T_b = 0.05\times\dfrac{180}{342} = 0.026\) &deg;C; boiling point &asymp; 100.03 &deg;C (lower than
100.05 &deg;C).</li>
<li><b>(ii) Glucose in acetic acid:</b> the solvent has changed: its own boiling point (&asymp; 118 &deg;C), its
K<sub>b</sub> (&asymp; 3.07 K kg mol<sup>&minus;1</sup> against 0.52 for water) and the mass of 500 mL all differ, so
the boiling point is about 118 &deg;C plus a larger elevation (&asymp; 0.3 &deg;C) &mdash; nowhere near
100.05 &deg;C.</li></ul>""",
          topic="Solutions",
          recall=r"""<ul><li>i = observed / calculated colligative effect.</li>
<li>\(\pi = CRT\) with C in mol L<sup>&minus;1</sup> (R = 0.0821 L atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>).</li>
<li>\(\Delta T_b = K_b m\): K<sub>b</sub> depends on the solvent; m depends on moles of solute per kg of solvent.</li></ul>"""),
    ])
