"""Chemistry pre-board 2013-14, Paper 1 (Theory).  Transcribed from the page images.
The scan in PreBoard-PYQ holds only pages 1-4 of the 7 printed pages (up to Question 4(b))."""
from kit import Q, SEC
import chemistry_2013_14_figs as F

SOL, EL, KIN = "Solutions", "Electrochemistry", "Chemical Kinetics"
COORD, ALC = "Coordination Compounds", "Alcohols, Phenols and Ethers"
CARB, NIT, BIO = "Aldehydes, Ketones and Carboxylic Acids", "Organic Compounds containing Nitrogen", "Biomolecules"

ION = "Ionic equilibrium (acids and bases, common-ion effect, salt hydrolysis, buffers) — Class XI; not in the ISC 2027 Class XII units."
EQM = "Chemical equilibrium (Le Chatelier's principle) — Class XI; not in the ISC 2027 Class XII units."
SOLID = "Solid state — removed from the ISC Class XII syllabus; not among the ten ISC 2027 units."
PBLK = "p-Block elements (halogens / interhalogens) — not in the ISC 2027 Class XII syllabus, whose inorganic units are only d- and f-block and coordination compounds."
MET = "Metallurgy (extraction of copper, slag) — removed; not in the ISC 2027 Class XII syllabus."

PAPER = dict(
    subject="chemistry",
    year="2013-14",
    slug="2013-14",
    paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2013-14/Chemistry.pdf",
    marks=70, time="3 hours",
    intro=r"""<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start
writing during this time.)</p>
<p>Answer all questions in Part I and six questions from Part II, choosing two questions from Section A,
two from Section B and two from Section C.</p>
<p>All working, including rough work, should be done on the same sheet as, and adjacent to, the rest of the answer.</p>
<p>The intended marks for questions or parts of questions are given in brackets [ ].</p>
<p>Balanced equations must be given wherever possible and diagrams where they are helpful.</p>
<p>When solving numerical problems, all essential working must be shown.</p>
<p>In working out problems use the following data: Gas constant R = 1.987 cal deg<sup>−1</sup> mol<sup>−1</sup>
= 8.314 J K<sup>−1</sup> mol<sup>−1</sup> = 0.0821 dm<sup>3</sup> atm K<sup>−1</sup> mol<sup>−1</sup>;
1 l atm = 1 dm<sup>3</sup> atm = 101.3 J; 1 Faraday = 96500 coulombs.</p>
<p>This paper consists of 7 printed pages.</p>
<p class="note">[The copy of this paper available to us is incomplete: only printed pages 1–4 were scanned.
The paper breaks off after Question 4(b); the rest of Question 4 and Sections B and C (Questions 5–10)
are missing, so they cannot be reproduced here.]</p>""",
    items=[
        SEC("PART I", "Answer all questions"),
        # ---------------------------------------------------------------- 1(a)
        Q("1(a)(i)", 1, r"""<p><b>Fill in the blanks</b> by choosing the appropriate word/words from those given in the
brackets: (high, electron pair donor, low, proton donor, glycerol, glycol, soaps, salt effect, increased, decreased,
common ion effect, cation, anion, cathode, anode, proton acceptor, ester)</p>
<p>(i) According to Brondsted and Lowry, an acid is a ______ while a base is ______.</p>""",
          excluded=ION),
        Q("1(a)(ii)", 1, r"""<p>(ii) The high reactivity of halogens is due to their ______ dissociation energy and ______
negative values of electron gain enthalpy.</p>""", excluded=PBLK),
        Q("1(a)(iii)", 1, r"""<p><b>Fill in the blanks</b> by choosing the appropriate word/words from those given in the
brackets: (high, electron pair donor, low, proton donor, glycerol, glycol, soaps, salt effect, increased, decreased,
common ion effect, cation, anion, cathode, anode, proton acceptor, ester)</p>
<p>(iii) Hydrolysis of fats or oils with sodium hydroxide gives ______ and ______.</p>""",
          a=r"""<p>Hydrolysis of fats or oils with sodium hydroxide gives <b>soaps</b> and <b>glycerol</b>.</p>
<p>A fat is a triester of glycerol (propane-1,2,3-triol) with long-chain fatty acids; alkaline hydrolysis of the
ester (saponification) gives the sodium salts of the acids (soap) and glycerol:</p>
\[\ce{(C17H35COO)3C3H5 + 3NaOH -> 3C17H35COONa + C3H5(OH)3}\]
<p><span class="box">soaps; glycerol</span></p>""",
          topic=ALC,
          recall=r"""<ul><li>Fats/oils are glyceryl esters (triglycerides) of fatty acids.</li>
<li>Ester + NaOH → sodium carboxylate + alcohol (saponification).</li>
<li>Glycerol = propane-1,2,3-triol, a trihydric alcohol.</li></ul>"""),
        Q("1(a)(iv)", 1, r"""<p>(iv) Solubility of sodium chloride is ______ in presence of hydrochloric acid because of ______.</p>""",
          excluded=ION),
        Q("1(a)(v)", 1, r"""<p>(v) In acidic solution, an amino acid exists as a ______ and migrates towards ______ under
the influence of an electric field.</p>""",
          a=r"""<p>In acidic solution an amino acid exists as a <b>cation</b> and migrates towards the <b>cathode</b>.</p>
<p>The zwitterion takes up \(\ce{H+}\) on its –COO⁻ group, leaving only the positive –NH₃⁺ group:</p>
\[\ce{H3N+-CH2-COO- + H+ -> H3N+-CH2-COOH}\]
{{fig:0}}
<p><span class="box">cation; cathode</span></p>""",
          afig=[(F.fig_q1a5_aminoacid, "Glycine in acid, at its isoelectric point and in alkali.")],
          topic=BIO,
          recall=r"""<ul><li>Amino acids exist as dipolar ions (zwitterions) \(\ce{H3N+-CHR-COO-}\).</li>
<li>Below the isoelectric point (acid) → cation → moves to cathode; above it (alkali) → anion → anode.</li>
<li>At the isoelectric point there is no net migration.</li></ul>"""),
        # ---------------------------------------------------------------- 1(b)
        Q("1(b)(i)", 1, r"""<p><b>Complete the following statements by selecting the correct alternative from the choices given:</b></p>
<p>(i) A standard hydrogen electrode has zero electrode potential because</p>
<p>(a) Hydrogen is the lightest element. (b) Hydrogen has only one electron. (c) The electrode potential is
assumed to be zero. (d) None of these.</p>""",
          a=r"""<p><span class="box">(c) The electrode potential is assumed to be zero.</span></p>
<p>A single electrode potential cannot be measured on its own; only differences can. The SHE
(Pt, \(\ce{H2}\) at 1 bar, \(\ce{H+}\) at unit activity, 298 K) is chosen as the reference and its potential is
<i>assigned</i> the value 0.00 V by convention.</p>""",
          topic=EL,
          recall=r"""<ul><li>SHE: Pt | H₂(g, 1 bar) | H⁺(aq, unit activity); E° = 0 by convention.</li>
<li>\(E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode}\), measured against the SHE.</li></ul>"""),
        Q("1(b)(ii)", 1, r"""<p>(ii) For an associated solute in a solution the value of Vant Hoff factor is:</p>
<p>(1) One (2) Two (3) Greater than one (4) Less than one</p>""",
          a=r"""<p><span class="box">(4) Less than one</span></p>
<p>\(i = \dfrac{\text{observed colligative property}}{\text{normal value}} = \dfrac{\text{number of particles after association}}{\text{number before}}\).
Association (e.g. ethanoic acid dimerising in benzene) reduces the number of particles, so \(i &lt; 1\);
for complete dimerisation \(i = \tfrac12\).</p>""",
          topic=SOL,
          recall=r"""<ul><li>Dissociation: \(i = 1 + (n-1)\alpha &gt; 1\).</li>
<li>Association into \(n\)-mers: \(i = 1 - \alpha\left(1 - \tfrac1n\right) &lt; 1\).</li></ul>"""),
        Q("1(b)(iii)", 1, r"""<p>(iii) The major product formed when phenol is heated with carbon tetrachloride in presence of
sodium hydroxide followed by acid hydrolysis is</p>
<p>(1) 4-hydroxy benzoic acid (2) Salicylic acid (3) Phenyl chloride (4) Salicylaldehyde</p>""",
          a=r"""<p><span class="box">(2) Salicylic acid</span></p>
<p>This is the Reimer–Tiemann reaction with \(\ce{CCl4}\) in place of \(\ce{CHCl3}\): the \(\ce{-CCl3}\) group
enters mainly <i>ortho</i> to the phenoxide oxygen and is hydrolysed to \(\ce{-COOH}\). (With chloroform the
product would be salicylaldehyde.)</p>
\[\ce{C6H5OH + CCl4 + 6NaOH -> C6H4(ONa)COONa + 4NaCl + 4H2O}\quad(\text{ortho})\]
\[\ce{C6H4(ONa)COONa + 2HCl -> C6H4(OH)COOH + 2NaCl}\]
{{fig:0}}""",
          afig=[(F.fig_q1b3_salicylic, "Phenol → salicylic acid (2-hydroxybenzoic acid).")],
          topic=ALC,
          recall=r"""<ul><li>Reimer–Tiemann: phenol + \(\ce{CHCl3}\)/NaOH → salicylaldehyde (\(\ce{-CHO}\) ortho).</li>
<li>With \(\ce{CCl4}\)/NaOH the ortho product is salicylic acid (\(\ce{-COOH}\)).</li>
<li>Kolbe's reaction (sodium phenoxide + \(\ce{CO2}\), 400 K, 4–7 atm) also gives salicylic acid.</li></ul>"""),
        Q("1(b)(iv)", 1, r"""<p>(iv) The chemical composition of slag formed during the smelting process in the extraction of copper is</p>
<p>(1) \(\ce{CuFeS2}\) (2) \(\ce{CaSiO3}\) (3) \(\ce{Cu2S + FeO}\) (4) \(\ce{FeSiO3}\)</p>""", excluded=MET),
        Q("1(b)(v)", 1, r"""<p>(v) This is not a colligative property:</p>
<p>(1) Lowering of vapour pressure (2) Osmotic pressure (3) Elevation of boiling point (4) Depression of freezing point</p>""",
          a=r"""<p><span class="box">(1) Lowering of vapour pressure</span></p>
<p>By Raoult's law \(p^\circ - p = p^\circ x_B\): the <i>lowering</i> itself depends on \(p^\circ\), which is a property of the
solvent, so it is not purely colligative. It is the <b>relative</b> lowering
\(\dfrac{p^\circ-p}{p^\circ} = x_B\) that depends only on the number of solute particles. (2), (3) and (4) are colligative.</p>""",
          topic=SOL,
          recall=r"""<ul><li>Colligative = depends only on the number of solute particles, not their nature.</li>
<li>The four: relative lowering of vapour pressure, \(\Delta T_b\), \(\Delta T_f\), osmotic pressure.</li>
<li>Raoult: \((p^\circ - p)/p^\circ = x_\text{solute}\).</li></ul>"""),
        # ---------------------------------------------------------------- 1(c)
        Q("1(c)(i)", 1, r"""<p><b>Answer the following questions:</b></p>
<p>(i) Give balanced equation for the preparation of Phenyl isocyanide from aniline.</p>""",
          a=r"""<p>Carbylamine reaction — heat aniline with chloroform and alcoholic KOH:</p>
\[\ce{C6H5NH2 + CHCl3 + 3KOH(alc) ->[\Delta] C6H5NC + 3KCl + 3H2O}\]
<p>Phenyl isocyanide (\(\ce{C6H5-N#C}\)) is recognised by its offensive smell; the reaction is given only by primary amines.</p>""",
          topic=NIT,
          recall=r"""<ul><li>Carbylamine (isocyanide) test: 1° amine + \(\ce{CHCl3}\) + 3 KOH (alc) → \(\ce{RNC}\) + 3 KCl + 3 \(\ce{H2O}\).</li>
<li>Only primary (aliphatic or aromatic) amines respond — a test for 1° amines.</li></ul>"""),
        Q("1(c)(ii)", 1, r"""<p>(ii) Discuss the effect of pressure on the equilibrium of the following reactions.</p>
\[\ce{H2(g) + I2(g) <=> 2HI(g)}\]""", excluded=EQM),
        Q("1(c)(iii)", 1, r"""<p>(iii) The osmotic pressure produced by dilute equimolar solutions of three substances are in the order
X &gt; glucose &gt; Y. Suggest a reason for this behavior.</p>""",
          a=r"""<p>Osmotic pressure \(\pi = iCRT\) depends on the number of solute particles. Glucose neither dissociates nor
associates (\(i = 1\)). At equal concentration:</p>
<p class="step">• X gives a larger \(\pi\) → \(i &gt; 1\) → X <b>dissociates</b> (ionises) in solution, e.g. NaCl.</p>
<p class="step">• Y gives a smaller \(\pi\) → \(i &lt; 1\) → Y <b>associates</b> in solution (e.g. dimerises).</p>
<p><span class="box">X dissociates (i &gt; 1); glucose is normal (i = 1); Y associates (i &lt; 1)</span></p>""",
          topic=SOL,
          recall=r"""<ul><li>\(\pi = iCRT\); at the same \(C\) and \(T\), \(\pi \propto i\).</li>
<li>Dissociation → \(i &gt; 1\); association → \(i &lt; 1\); non-electrolyte → \(i = 1\).</li></ul>"""),
        Q("1(c)(iv)", 1, r"""<p>(iv) Same quantity of electricity is passed separately through aqueous solution of copper(I) sulphate and
copper(II) sulphate using inert electrodes. In which case the amount of copper deposited will be more and why?</p>""",
          a=r"""<p>More copper is deposited from the <b>copper(I)</b> solution — twice as much.</p>
\[\ce{Cu+ + e- -> Cu}\qquad\]
\[\ce{Cu^2+ + 2e- -> Cu}\]
<p>By Faraday's second law the mass deposited by the same charge is proportional to the equivalent mass
\(M/z\): 1 F deposits 63.5 g of Cu from \(\ce{Cu+}\) (z = 1) but only 31.75 g from \(\ce{Cu^2+}\) (z = 2).</p>
<p><span class="box">Cu(I) sulphate: mass ratio Cu(I) : Cu(II) = 2 : 1</span></p>""",
          topic=EL,
          recall=r"""<ul><li>Faraday I: \(m = ZQ = \dfrac{M}{zF}\,It\).</li>
<li>Faraday II: same charge → masses in the ratio of equivalent masses \(M/z\).</li></ul>"""),
        Q("1(c)(v)", 1, r"""<p>(v) What type of compound is \(\ce{IF7}\)? Write its structure.</p>""", excluded=PBLK),
        # ---------------------------------------------------------------- 1(d)
        Q("1(d)(i)", 1, r"""<p><b>Match the following:</b></p>
<div class="tbl"><table><tr><td>(i) Chelates</td><td>(a) Ostwlad's dilution law</td></tr>
<tr><td>(ii) Ethoxy ethane</td><td>(b) Cannizzaro reaction</td></tr>
<tr><td>(iii) Benzaldehyde</td><td>(c) Polydentate ligands</td></tr>
<tr><td>(iv) Zwitter ion</td><td>(d) Williamson's synthesis</td></tr>
<tr><td>(v) Weak Electrolyte</td><td>(e) Glycine</td></tr></table></div>
<p>(i) Chelates</p>""",
          a=r"""<p><span class="box">(i) Chelates — (c) Polydentate ligands</span></p>
<p>A chelate is a ring complex formed when a ligand with two or more donor atoms (bi- or polydentate, e.g.
ethylenediamine, EDTA) binds the same metal ion.</p>""",
          topic=COORD,
          recall=r"""<ul><li>Denticity = number of donor atoms of a ligand that bind the metal.</li>
<li>Chelating ligands form 5- or 6-membered rings and give extra-stable complexes (chelate effect).</li></ul>"""),
        Q("1(d)(ii)", 1, r"""<p>(ii) Ethoxy ethane</p>""",
          a=r"""<p><span class="box">(ii) Ethoxy ethane — (d) Williamson's synthesis</span></p>
\[\ce{C2H5ONa + C2H5Br -> C2H5-O-C2H5 + NaBr}\]""",
          topic=ALC,
          recall=r"""<ul><li>Williamson synthesis: RO⁻Na⁺ + R′X → R–O–R′ + NaX (S<sub>N</sub>2; use a 1° halide).</li></ul>"""),
        Q("1(d)(iii)", 1, r"""<p>(iii) Benzaldehyde</p>""",
          a=r"""<p><span class="box">(iii) Benzaldehyde — (b) Cannizzaro reaction</span></p>
\[\ce{2C6H5CHO + NaOH(conc) -> C6H5CH2OH + C6H5COONa}\]
<p>Benzaldehyde has no α-hydrogen, so in concentrated alkali it disproportionates.</p>""",
          topic=CARB,
          recall=r"""<ul><li>Cannizzaro: aldehydes without α-H (HCHO, \(\ce{C6H5CHO}\)) + conc. alkali → alcohol + carboxylate salt.</li></ul>"""),
        Q("1(d)(iv)", 1, r"""<p>(iv) Zwitter ion</p>""",
          a=r"""<p><span class="box">(iv) Zwitter ion — (e) Glycine</span></p>
<p>Glycine exists as the dipolar ion \(\ce{H3N+-CH2-COO-}\).</p>""",
          topic=BIO,
          recall=r"""<ul><li>Amino acids: acidic \(\ce{-COOH}\) and basic \(\ce{-NH2}\) in one molecule → internal salt (zwitterion).</li></ul>"""),
        Q("1(d)(v)", 1, r"""<p>(v) Weak Electrolyte</p>""",
          a=r"""<p><span class="box">(v) Weak electrolyte — (a) Ostwald's dilution law</span></p>
<p>Ostwald's dilution law, \(K_a = \dfrac{C\alpha^2}{1-\alpha}\), applies to weak electrolytes, whose degree of
dissociation \(\alpha\) (obtainable from conductance, \(\alpha = \Lambda_m/\Lambda^\circ_m\)) rises with dilution.</p>""",
          topic=EL,
          recall=r"""<ul><li>\(\alpha = \Lambda_m / \Lambda^\circ_m\) for a weak electrolyte (Kohlrausch).</li>
<li>Ostwald: \(K = C\alpha^2/(1-\alpha) \approx C\alpha^2\).</li></ul>"""),
        SEC("PART II", "Answer six questions choosing two from Section A, two from Section B and two from Section C"),
        SEC("SECTION A", "(Answer any two questions)"),
        # ---------------------------------------------------------------- Q2
        Q("2(a)", 2, r"""<p>Calculate the hydrolysis constant, degree of hydrolysis and pH of 0.5 M sodium acetate solution at 25°C.
\(K_a\) for acetic acid = \(1.75\times10^{-5}\)?</p>""", excluded=ION),
        Q("2(b)(i)", 1, r"""<p>Explain why: [2 marks for (i) and (ii) together]</p>
<p>(i) The solubility of AgCl in water decreases on adding NaCl to the solution.</p>""", excluded=ION),
        Q("2(b)(ii)", 1, r"""<p>Explain why:</p><p>(ii) Specific conductance of an electrolyte decreases with dilution.</p>""",
          a=r"""<p>Specific conductance (conductivity) \(\kappa\) is the conductance of <b>1 cm³</b> of the solution (between
electrodes 1 cm² in area, 1 cm apart). On dilution, although the degree of ionisation rises, the <b>number of ions
per unit volume falls</b> (the same ions are spread through more solvent), so \(\kappa\) decreases.</p>
<p>Molar conductivity \(\Lambda_m = \kappa \times 1000/C\) refers to a whole mole of electrolyte, so it
<i>increases</i> with dilution.</p>
{{fig:0}}""",
          afig=[(F.fig_q2b_conductance, "κ falls and Λm rises as the solution is diluted.")],
          topic=EL,
          recall=r"""<ul><li>\(\kappa = G \times \dfrac{l}{A}\) — conductance of unit volume (S cm⁻¹).</li>
<li>\(\Lambda_m = \kappa \times 1000 / C\) (S cm² mol⁻¹).</li>
<li>Dilution: ions per cm³ ↓ ⇒ κ ↓; ionisation and ion mobility ↑ ⇒ Λm ↑.</li></ul>"""),
        Q("2(c)", 2, r"""<p>The specific conductivity of 0.02 M KCl solution at 25°C is \(2.768\times10^{-3}\) ohm⁻¹ cm⁻¹. The
resistance of the solution at 25°C using a particular cell was 250.2 ohm. The resistance of 0.01 M \(\ce{CuSO4}\)
solution at 25°C measured with the same cell was 8331 ohms. Calculate the molar conductivity of the copper
sulphate solution.</p>""",
          a=r"""<p class="step"><b>Cell constant</b> from the KCl standard: \(\kappa = \dfrac{1}{R}\times\dfrac{l}{A}\Rightarrow
\dfrac{l}{A} = \kappa R\)</p>
\[\frac{l}{A} = 2.768\times10^{-3}\ \text{S cm}^{-1}\times 250.2\ \Omega = 0.6925\ \text{cm}^{-1}\]
<p class="step"><b>Conductivity of the \(\ce{CuSO4}\) solution</b> (same cell):</p>
\[\kappa = \frac{l/A}{R} = \frac{0.6925}{8331} = 8.313\times10^{-5}\ \text{S cm}^{-1}\]
<p class="step"><b>Molar conductivity:</b></p>
\[\Lambda_m = \frac{\kappa\times1000}{C} = \frac{8.313\times10^{-5}\times1000}{0.01} = 8.313\ \text{S cm}^2\,\text{mol}^{-1}\]
<p><span class="box">\(\Lambda_m(\ce{CuSO4}) = 8.31\ \text{S cm}^2\,\text{mol}^{-1}\ (= 8.31\times10^{-4}\ \text{S m}^2\,\text{mol}^{-1})\)</span></p>""",
          topic=EL,
          recall=r"""<ul><li>Cell constant \(G^* = l/A = \kappa R\), found with a KCl solution of known κ.</li>
<li>\(\kappa = G^*/R\); \(\Lambda_m = 1000\,\kappa/C\) (κ in S cm⁻¹, C in mol L⁻¹).</li></ul>"""),
        Q("2(d)", 2, r"""<p>Benzene and toluene form ideal solution. At 310 K, the vapour pressure of pure benzene is 150 mm Hg and
of pure toluene 45 mm Hg. Calculate the vapour pressure of a mixture of these two containing equal masses at 310 K.</p>""",
          a=r"""<p class="step">Take 100 g of each. \(M(\ce{C6H6}) = 78\), \(M(\ce{C7H8}) = 92\) g mol⁻¹.</p>
\[n_B = \frac{100}{78} = 1.282\ \text{mol},\qquad n_T = \frac{100}{92} = 1.087\ \text{mol}\]
\[x_B = \frac{1.282}{1.282+1.087} = 0.541,\qquad x_T = 1 - 0.541 = 0.459\]
<p class="step">Raoult's law for an ideal solution: \(p = p^\circ_B x_B + p^\circ_T x_T\)</p>
\[p = 150(0.541) + 45(0.459) = 81.2 + 20.6 = 101.8\ \text{mm Hg}\]
<p><span class="box">Vapour pressure of the mixture ≈ 101.8 mm Hg</span></p>""",
          topic=SOL,
          recall=r"""<ul><li>Raoult's law: \(p_i = p_i^\circ x_i\); total \(p = \sum p_i^\circ x_i\) for an ideal solution.</li>
<li>Equal <i>masses</i> ≠ equal moles: convert with molar masses first.</li></ul>"""),
        Q("2(e)", 2, r"""<p>A solution containing 10.2 g of glycerine per litre is found to be isotonic with a 2% solution of glucose.
Calculate the molecular mass of glycerine. (Molecular weight of glucose is 180)</p>""",
          a=r"""<p class="step">Isotonic solutions (same T) have equal osmotic pressure, hence equal molar concentration
(\(\pi = CRT\), both non-electrolytes).</p>
<p class="step">2% glucose = 2 g per 100 mL = 20 g L⁻¹:</p>
\[C_\text{glucose} = \frac{20}{180} = 0.1111\ \text{mol L}^{-1}\]
\[\frac{10.2}{M} = 0.1111 \;\Rightarrow\; M = \frac{10.2}{0.1111} = 91.8\ \text{g mol}^{-1}\]
<p><span class="box">Molar mass of glycerine ≈ 91.8 g mol⁻¹ (true value 92)</span></p>""",
          topic=SOL,
          recall=r"""<ul><li>Isotonic ⇒ equal π ⇒ equal \(iC\) at the same temperature.</li>
<li>\(\pi = \dfrac{w}{MV}RT\); a "2 % solution" is 2 g per 100 mL.</li></ul>"""),
        # ---------------------------------------------------------------- Q3
        Q("3(a)(i)", 2, r"""<p>(i) What will be the effect on pH value on adding sodium acetate to an aqueous solution of acetic acid and why?</p>""",
          excluded=ION),
        Q("3(b)", 3, r"""<p>An element having bcc geometry has atomic mass 50. Calculate the density of the unit cell, if its edge
length is 290 pm. Give two differences between the crystals on NaCl and Cu.</p>""", excluded=SOLID),
        Q("3(c)", 2, r"""<p>The molar conductance of NaOH, NaCl and \(\ce{BaCl2}\) at infinite dilutions are \(2.481\times10^{-2}\),
\(1.265\times10^{-2}\) and \(2.8\times10^{-2}\) S m² mol⁻¹ respectively; calculate \(\lambda^\infty_m\) for \(\ce{Ba(OH)2}\).</p>""",
          a=r"""<p class="step">By Kohlrausch's law of independent migration of ions, \(\Lambda^\circ_m\) of an electrolyte is the sum of the
limiting molar conductivities of its ions:</p>
\[\Lambda^\circ_m(\ce{Ba(OH)2}) = \lambda^\circ_{\ce{Ba^2+}} + 2\lambda^\circ_{\ce{OH-}}
= \Lambda^\circ_m(\ce{BaCl2}) + 2\Lambda^\circ_m(\ce{NaOH}) - 2\Lambda^\circ_m(\ce{NaCl})\]
\[= 2.8\times10^{-2} + 2(2.481\times10^{-2}) - 2(1.265\times10^{-2})\]
\[= (2.800 + 4.962 - 2.530)\times10^{-2} = 5.232\times10^{-2}\ \text{S m}^2\,\text{mol}^{-1}\]
<p><span class="box">\(\Lambda^\circ_m(\ce{Ba(OH)2}) = 5.232\times10^{-2}\ \text{S m}^2\,\text{mol}^{-1}\)</span></p>""",
          topic=EL,
          recall=r"""<ul><li>Kohlrausch: \(\Lambda^\circ_m = \nu_+\lambda^\circ_+ + \nu_-\lambda^\circ_-\).</li>
<li>Combine known \(\Lambda^\circ_m\) values so that unwanted ions (here \(\ce{Na+}\), \(\ce{Cl-}\)) cancel.</li></ul>"""),
        Q("3(d)", 3, r"""<p>A 0.1539 molal aqueous solution of cane sugar (molar mass = 342 g mol⁻¹) has a freezing point of 271 K while
the freezing point of pure water is 273.15 K. What will be the freezing point of an aqueous solution containing 5 g
of glucose (mol mass = 180 g mol⁻¹) per 100 g of solution?</p>""",
          a=r"""<p class="step"><b>\(K_f\) from the cane-sugar data:</b> \(\Delta T_f = K_f\, m\)</p>
\[\Delta T_f = 273.15 - 271 = 2.15\ \text{K};\qquad K_f = \frac{2.15}{0.1539} = 13.97\ \text{K kg mol}^{-1}\]
<p class="step"><b>Molality of the glucose solution:</b> 5 g glucose in 100 g solution ⇒ 95 g (0.095 kg) water.</p>
\[m = \frac{5/180}{0.095} = \frac{0.02778}{0.095} = 0.2924\ \text{mol kg}^{-1}\]
\[\Delta T_f = 13.97 \times 0.2924 = 4.08\ \text{K}\]
\[T_f = 273.15 - 4.08 = 269.07\ \text{K}\]
<p><span class="box">Freezing point of the glucose solution ≈ 269.07 K</span></p>
<p class="note">Note: 0.1539 mol kg⁻¹ is exactly a 5% (w/w) cane-sugar solution (5 g in 95 g water). The \(K_f\) these
data imply, 13.97 K kg mol⁻¹, is far larger than the real value for water (1.86); the paper uses textbook data, and
the answer is worked with the value the data give, as intended.</p>""",
          topic=SOL,
          recall=r"""<ul><li>\(\Delta T_f = K_f m\), \(m = \dfrac{w_B/M_B}{W_A\ (\text{kg})}\).</li>
<li>"Per 100 g of solution": subtract the solute mass to get the solvent mass.</li>
<li>Same solvent ⇒ same \(K_f\): ratio method \(\Delta T_1/\Delta T_2 = m_1/m_2\).</li></ul>"""),
        # ---------------------------------------------------------------- Q4
        Q("4(a)", 2, r"""<p>For sodium chloride crystal, state:</p>
<p>(i) The type of unit cell (ii) The nature of forces binding the particles (iii) The geometry of sodium ions which
are arranged around a chloride ion (iv) The coordination number of each ion.</p>""", excluded=SOLID),
        Q("4(b)", 2, r"""<p>A 0.5% aqueous solution of potassium chloride freezes at −0.24°C. Calculate the Van't Hoff factor.</p>""",
          a=r"""<p class="step">\(K_f\) for water is not printed; the standard value 1.86 K kg mol⁻¹ is used.</p>
<p class="step">0.5% (w/w): 0.5 g KCl (M = 74.5 g mol⁻¹) in 99.5 g water.</p>
\[m = \frac{0.5/74.5}{0.0995} = 0.06745\ \text{mol kg}^{-1}\]
<p class="step">Normal (calculated) depression: \(\Delta T_f(\text{calc}) = K_f m = 1.86 \times 0.06745 = 0.1255\ \text{K}\)</p>
<p class="step">Observed depression: \(\Delta T_f(\text{obs}) = 0 - (-0.24) = 0.24\ \text{K}\)</p>
\[i = \frac{\Delta T_f(\text{obs})}{\Delta T_f(\text{calc})} = \frac{0.24}{0.1255} = 1.91\]
<p><span class="box">van't Hoff factor \(i \approx 1.91\)</span> — close to 2, since KCl dissociates almost completely into
\(\ce{K+}\) and \(\ce{Cl-}\) (degree of dissociation \(\alpha = i - 1 = 0.91\)).</p>
<p class="note">[Not printed in the original: the value of \(K_f\) for water (taken as 1.86 K kg mol⁻¹).]</p>""",
          topic=SOL,
          recall=r"""<ul><li>\(i = \dfrac{\Delta T_f(\text{obs})}{\Delta T_f(\text{calc})}\)</li>
<li>\(\Delta T_f = iK_f m\); for KCl, \(i = 1 + \alpha\).</li>
<li>\(K_f(\ce{H2O}) = 1.86\ \text{K kg mol}^{-1}\).</li></ul>"""),
    ])
