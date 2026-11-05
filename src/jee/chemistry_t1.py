"""JEE Main mock test 1 — Chemistry (Q26–50).  Every item is adapted from a kept pre-board item."""
from jee_kit import MCQ, NUM
import chemistry_figs as JF
from chemistry_2015_16_figs import fig_pt_cis_trans
from chemistry_2016_17_figs import fig_cof6_cft

SUBJECT = "chemistry"
TEST = 1

QUESTIONS = [
    # ------------------------------------------------------------------ Solutions
    MCQ(src=("chemistry_2013_14", "2(d)"), topic="Solutions",
        q=r"""<p>Benzene and toluene form an ideal solution. At 310 K the vapour pressure of pure
        benzene is 150 mm Hg and that of pure toluene is 45 mm Hg. The vapour pressure of a mixture
        containing <b>equal masses</b> of the two liquids at 310 K is closest to
        (molar masses: benzene 78, toluene 92 g mol\(^{-1}\))</p>""",
        options=[r"\(93\) mm Hg", r"\(102\) mm Hg", r"\(97.5\) mm Hg", r"\(81\) mm Hg"],
        answer=1,
        sol=r"""<p>Take \(w\) g of each. Mole fraction of benzene:
        \[x_B = \frac{w/78}{w/78 + w/92} = \frac{92}{78+92} = \frac{92}{170} = 0.541\]
        Raoult's law for the total pressure:
        \[p = p_T^\circ + (p_B^\circ - p_T^\circ)\,x_B = 45 + 105\times0.541 = 101.8\ \text{mm Hg}\approx 102\ \text{mm Hg}\]</p>
        <p>Slips behind the other options: \(97.5\) treats equal masses as equal moles (\(x_B = 0.5\));
        \(93\) swaps the mole fractions (\(x_B = 78/170\)); \(81\) is only the partial pressure of benzene.</p>
        <p><b>Answer: (2) 102 mm Hg</b></p>"""),

    MCQ(src=("chemistry_2024_25_s1", "1(B)(ii)"), topic="Solutions",
        q=r"""<p>Three aqueous solutions of \(\ce{K2SO4}\) have molalities 0.1 (A), 0.01 (B) and
        0.001 (C) mol kg\(^{-1}\). Their van't Hoff factors \(i_A, i_B, i_C\) satisfy</p>""",
        options=[r"\(i_A > i_B > i_C\), all less than 3",
                 r"\(i_A = i_B = i_C = 3\)",
                 r"\(i_A < i_B < i_C\), all less than 3",
                 r"\(i_A < i_B < i_C\), all greater than 3"],
        answer=2,
        sol=r"""<p>\(\ce{K2SO4 -> 2K+ + SO4^2-}\) gives 3 ions, so the limiting value is \(i = 3\).
        In a real solution interionic attraction makes the ions behave as fewer free particles,
        so \(i &lt; 3\); the effect weakens as the solution is diluted, so \(i\) rises towards 3:
        \(i_A &lt; i_B &lt; i_C &lt; 3\).</p>
        <p>Why not the others: \(i = 3\) exactly holds only at infinite dilution; \(i\) cannot
        exceed the number of ions per formula unit; and \(i\) <i>increases</i>, not decreases, on dilution.</p>
        <p><b>Answer: (3)</b></p>"""),

    # ------------------------------------------------------------------ Electrochemistry
    MCQ(src=("chemistry_2024_25_s1", "10"), topic="Electrochemistry",
        q=r"""<p>The emf at 298 K of the cell
        \(\ce{Al | Al^3+ (0.1 M) || Sn^2+ (0.001 M) | Sn}\) is
        (\(E^\circ_{\ce{Al^3+/Al}} = -1.66\) V, \(E^\circ_{\ce{Sn^2+/Sn}} = -0.14\) V,
        \(2.303RT/F = 0.0591\) V)</p>""",
        options=[r"\(1.45\) V", r"\(1.52\) V", r"\(1.31\) V", r"\(1.59\) V"],
        answer=0,
        sol=r"""<p>Cell reaction (6 electrons): \(\ce{2Al + 3Sn^2+ -> 2Al^3+ + 3Sn}\);
        \(E^\circ_\text{cell} = -0.14 - (-1.66) = 1.52\) V.</p>
        <p>\[E = E^\circ - \frac{0.0591}{6}\log\frac{[\ce{Al^3+}]^2}{[\ce{Sn^2+}]^3}
        = 1.52 - \frac{0.0591}{6}\log\frac{(0.1)^2}{(0.001)^3} = 1.52 - 0.00985\times7 = 1.45\ \text{V}\]</p>
        <p>\(1.52\) V is \(E^\circ\) (concentration term forgotten); \(1.31\) V uses \(n = 2\);
        \(1.59\) V adds the correction (quotient inverted).</p>
        <p><b>Answer: (1) 1.45 V</b></p>"""),

    MCQ(src=("chemistry_2015_16", "1(d)(i)"), topic="Electrochemistry",
        q=r"""<p>A current of 9.65 A is passed for 1000 s through molten \(\ce{BaCl2}\) using inert
        electrodes. The mass of barium deposited at the cathode is (Ba = 137 g mol\(^{-1}\))</p>""",
        options=[r"\(13.7\) g", r"\(3.43\) g", r"\(27.4\) g", r"\(6.85\) g"],
        answer=3,
        sol=r"""<p>\(Q = It = 9.65\times1000 = 9650\) C \(= 0.1\) F.
        \(\ce{Ba^2+ + 2e- -> Ba}\): 2 F deposit 1 mol, so 0.1 F deposits 0.05 mol.</p>
        <p>\[m = 0.05\times137 = 6.85\ \text{g}\]</p>
        <p>\(13.7\) g takes one electron per Ba; \(27.4\) g multiplies by 2 instead of dividing;
        \(3.43\) g divides by 2 twice.</p>
        <p><b>Answer: (4) 6.85 g</b></p>"""),

    # ------------------------------------------------------------------ Chemical Kinetics
    MCQ(src=("chemistry_2014_15", "1(c)(i)"), topic="Chemical Kinetics",
        q=r"""<p>A reaction is 50% complete in 20 min and 75% complete in 40 min. The time needed for
        99.9% completion is about</p>""",
        options=[r"\(60\) min", r"\(100\) min", r"\(200\) min", r"\(400\) min"],
        answer=2,
        sol=r"""<p>50% in 20 min and the next half of what is left (to 75%) in another 20 min: the
        half-life is independent of concentration, so the reaction is <b>first order</b>,
        \(t_{1/2} = 20\) min, \(k = 0.693/20\) min\(^{-1}\).</p>
        <p>\[t_{99.9\%} = \frac{2.303}{k}\log\frac{100}{0.1} = \frac{2.303\times3}{0.693}\times20 = 199\ \text{min}\approx 10\,t_{1/2} = 200\ \text{min}\]</p>
        <p>60 min (3 half-lives) gives only 87.5%; 100 min (5 half-lives) gives 96.9%;
        400 min would be 99.9999%.</p>
        <p><b>Answer: (3) 200 min</b></p>"""),

    MCQ(src=("chemistry_2024_25_s1", "5"), topic="Chemical Kinetics",
        q=r"""<p>A hydrogenation proceeds at a certain rate at 500 K. In the presence of a catalyst
        the same rate is obtained at 400 K. If the catalyst lowers the activation energy by
        20 kJ mol\(^{-1}\) (and leaves \(A\) unchanged), the activation energy of the uncatalysed
        reaction is</p>""",
        options=[r"\(100\) kJ mol\(^{-1}\)", r"\(80\) kJ mol\(^{-1}\)",
                 r"\(120\) kJ mol\(^{-1}\)", r"\(50\) kJ mol\(^{-1}\)"],
        answer=0,
        sol=r"""<p>Same rate \(\Rightarrow\) same \(k = Ae^{-E_a/RT}\), with the same \(A\):</p>
        <p>\[\frac{E_a}{500} = \frac{E_a - 20}{400}\;\Rightarrow\;400E_a = 500E_a - 10\,000\;\Rightarrow\;E_a = 100\ \text{kJ mol}^{-1}\]</p>
        <p>80 kJ mol\(^{-1}\) is the activation energy <i>with</i> the catalyst; the other two do
        not satisfy \(E_a/T\) = constant.</p>
        <p><b>Answer: (1) 100 kJ mol\(^{-1}\)</b></p>"""),

    # ------------------------------------------------------------------ d- and f-Block
    MCQ(src=("chemistry_2025_26_s1", "8(i)"), topic="d- and f-Block Elements",
        q=r"""<p>Chromite ore, \(\ce{FeCr2O4}\), is fused with \(\ce{Na2CO3}\) in air to give a yellow
        compound A. Acidification of A gives B, and B with KCl gives an orange compound C.
        A and C are respectively</p>""",
        options=[r"\(\ce{Na2Cr2O7}\) and \(\ce{K2CrO4}\)", r"\(\ce{Na2CrO4}\) and \(\ce{K2Cr2O7}\)",
                 r"\(\ce{Na2CrO4}\) and \(\ce{K2CrO4}\)", r"\(\ce{Cr2O3}\) and \(\ce{K2Cr2O7}\)"],
        answer=1,
        sol=r"""<p>\[\ce{4FeCr2O4 + 8Na2CO3 + 7O2 -> 8Na2CrO4 + 2Fe2O3 + 8CO2}\]
        \[\ce{2Na2CrO4 + H2SO4 -> Na2Cr2O7 + Na2SO4 + H2O}\]
        \[\ce{Na2Cr2O7 + 2KCl -> K2Cr2O7 + 2NaCl}\]</p>
        <p>Chromate is yellow (A = \(\ce{Na2CrO4}\)); dichromate is orange (C = \(\ce{K2Cr2O7}\)).
        Acid converts chromate to dichromate, never the reverse, so a chromate cannot be C;
        \(\ce{Cr2O3}\) is green and is not formed in an oxidising fusion.</p>
        <p><b>Answer: (2)</b></p>"""),

    MCQ(src=("chemistry_2024_25_s1", "1(B)(vii)"), topic="d- and f-Block Elements",
        q=r"""<p><b>Assertion (A):</b> Zirconium and hafnium are very difficult to separate.<br>
        <b>Reason (R):</b> Because of the lanthanoid contraction, Zr and Hf have almost identical
        atomic radii.</p>""",
        options=[r"A is true but R is false", r"A is false but R is true",
                 r"Both A and R are true but R is not the correct explanation of A",
                 r"Both A and R are true and R is the correct explanation of A"],
        answer=3,
        sol=r"""<p>Hf comes after the 14 lanthanoids; the poor shielding by 4f electrons cancels the
        expected increase in size, so Hf (159 pm) and Zr (160 pm) have almost the same radius.
        Same radius and same valence configuration give nearly identical chemistry, so they occur
        together and are hard to separate. Both statements are true and R explains A.</p>
        <p><b>Answer: (4)</b></p>"""),

    # ------------------------------------------------------------------ Coordination
    MCQ(src=("chemistry_2016_17", "1(d)(i)"), topic="Coordination Compounds",
        q=r"""<p>The spin-only magnetic moment of \(\ce{[CoF6]^3-}\) is</p>""",
        options=[r"\(4.90\) BM", r"\(0\) BM", r"\(3.87\) BM", r"\(5.92\) BM"],
        answer=0,
        sol=r"""<p>\(\ce{Co^3+}\) is \(3d^6\). \(\ce{F-}\) is a weak-field ligand (\(\Delta_o &lt; P\)), so the
        complex is high spin: \(t_{2g}^4e_g^2\), 4 unpaired electrons.</p>
        {{fig:0}}
        <p>\[\mu = \sqrt{n(n+2)} = \sqrt{4\times6} = \sqrt{24} = 4.90\ \text{BM}\]</p>
        <p>0 BM is the low-spin \(t_{2g}^6\) case (as in \(\ce{[Co(NH3)6]^3+}\)); 3.87 BM is 3 unpaired,
        5.92 BM is 5 unpaired (\(d^5\)).</p>
        <p><b>Answer: (1) 4.90 BM</b></p>""",
        sfig=fig_cof6_cft),

    MCQ(src=("chemistry_2015_16", "1(d)(iii)"), topic="Coordination Compounds",
        q=r"""<p>Which of the following shows geometrical (cis–trans) isomerism?</p>""",
        options=[r"\(\ce{[Zn(NH3)2Cl2]}\)", r"\(\ce{[Co(NH3)5Cl]^2+}\)",
                 r"\(\ce{[Pt(NH3)2Cl2]}\)", r"\(\ce{[Ag(NH3)2]+}\)"],
        answer=2,
        sol=r"""<p>\(\ce{[Pt(NH3)2Cl2]}\) is square planar (\(\ce{Pt^2+}\), \(d^8\), \(dsp^2\)), type
        \(\ce{MA2B2}\): the two Cl can be adjacent (cis) or opposite (trans).</p>
        {{fig:0}}
        <p>\(\ce{[Zn(NH3)2Cl2]}\) is tetrahedral — every position is adjacent to every other, so no
        cis/trans. \(\ce{[Co(NH3)5Cl]^2+}\) is \(\ce{MA5B}\): only one arrangement.
        \(\ce{[Ag(NH3)2]+}\) is linear.</p>
        <p><b>Answer: (3)</b></p>""",
        sfig=fig_pt_cis_trans),

    # ------------------------------------------------------------------ Haloalkanes
    MCQ(src=("chemistry_2025_26_s2", "1(B)(iii)"), topic="Haloalkanes and Haloarenes",
        q=r"""<p>Ethyl isocyanide, \(\ce{C2H5NC}\), is obtained as the major product from</p>""",
        options=[r"\(\ce{C2H5Br}\) + alcoholic KCN", r"\(\ce{C2H5OH}\) + KCN",
                 r"\(\ce{CH3Br}\) + alcoholic AgCN", r"\(\ce{C2H5Br}\) + alcoholic AgCN"],
        answer=3,
        sol=r"""<p>Cyanide is ambident. AgCN is largely covalent (Ag–C bond), so only the lone pair on
        nitrogen is free to attack: \(\ce{C2H5Br + AgCN -> C2H5-N#C + AgBr}\).</p>
        <p>KCN is ionic; attack occurs through the more nucleophilic carbon and gives the nitrile
        \(\ce{C2H5CN}\). Ethanol has a poor leaving group (\(\ce{OH-}\)) and does not react.
        \(\ce{CH3Br}\) + AgCN gives methyl isocyanide, one carbon short.</p>
        <p><b>Answer: (4)</b></p>"""),

    MCQ(src=("chemistry_2024_25_s2", "1(B)(vi)"), topic="Haloalkanes and Haloarenes",
        q=r"""<p>The correct order of reactivity towards \(\mathrm{S_N1}\) hydrolysis in aqueous ethanol is</p>""",
        options=[r"\(\ce{CH3Br}\) &gt; \(\ce{CH3CH2Br}\) &gt; \(\ce{(CH3)2CHBr}\) &gt; \(\ce{(CH3)3CBr}\)",
                 r"\(\ce{(CH3)3CBr}\) &gt; \(\ce{(CH3)2CHBr}\) &gt; \(\ce{CH3CH2Br}\) &gt; \(\ce{CH3Br}\)",
                 r"\(\ce{(CH3)2CHBr}\) &gt; \(\ce{(CH3)3CBr}\) &gt; \(\ce{CH3CH2Br}\) &gt; \(\ce{CH3Br}\)",
                 r"\(\ce{CH3CH2Br}\) &gt; \(\ce{CH3Br}\) &gt; \(\ce{(CH3)2CHBr}\) &gt; \(\ce{(CH3)3CBr}\)"],
        answer=1,
        sol=r"""<p>The slow step of \(\mathrm{S_N1}\) is ionisation to a carbocation, so the rate follows
        carbocation stability: \(3^\circ > 2^\circ > 1^\circ > \ce{CH3+}\) (+I effect and
        hyperconjugation).</p>
        {{fig:0}}
        <p>Option (1) is the \(\mathrm{S_N2}\) order (steric hindrance); the other two put a less
        stable cation ahead of a more stable one.</p>
        <p><b>Answer: (2)</b></p>""",
        sfig=JF.fig_jc_sn1_tbubr),

    # ------------------------------------------------------------------ Alcohols, Phenols, Ethers
    MCQ(src=("chemistry_2025_26_s1", "1(B)(vii)"), topic="Alcohols, Phenols and Ethers",
        q=r"""<p>The correct order of <b>increasing</b> acid strength is</p>""",
        options=[r"p-cresol &lt; phenol &lt; m-nitrophenol &lt; p-nitrophenol",
                 r"phenol &lt; p-cresol &lt; m-nitrophenol &lt; p-nitrophenol",
                 r"p-cresol &lt; phenol &lt; p-nitrophenol &lt; m-nitrophenol",
                 r"m-nitrophenol &lt; p-nitrophenol &lt; phenol &lt; p-cresol"],
        answer=0,
        sol=r"""<p>Acidity depends on the stability of the phenoxide ion.</p>
        <ul><li>\(\ce{-CH3}\) (+I, hyperconjugation) intensifies the negative charge: p-cresol is
        weaker than phenol (p\(K_a\) 10.2 vs 10.0).</li>
        <li>\(\ce{-NO2}\) at <i>meta</i> withdraws only by −I (p\(K_a\) 8.4).</li>
        <li>\(\ce{-NO2}\) at <i>para</i> withdraws by −I and −R: the charge is delocalised onto
        the nitro oxygens (p\(K_a\) 7.1), the strongest acid of the four.</li></ul>
        {{fig:0}}
        <p>Option (3) is the common slip of thinking the meta isomer is strongest; option (2) puts
        p-cresol above phenol, ignoring the electron-releasing methyl group; option (4) is the
        order of <i>decreasing</i> acidity with the two nitrophenols also swapped.</p>
        <p><b>Answer: (1)</b></p>""",
        sfig=JF.fig_jc_p_nitrophenoxide),

    MCQ(src=("chemistry_2014_15", "1(b)(ii)"), topic="Alcohols, Phenols and Ethers",
        q=r"""<p>In the sequence
        \[\ce{(CH3)2CHOH ->[P/I2] A ->[Mg][\text{dry ether}] B ->[HCHO] C ->[H3O+] D}\]
        the compound D is</p>""",
        options=[r"butan-2-ol", r"2-methylpropan-2-ol", r"2-methylpropan-1-ol", r"butan-1-ol"],
        answer=2,
        sol=r"""<p>\[\ce{(CH3)2CHOH ->[P/I2] (CH3)2CHI ->[Mg] (CH3)2CHMgI}\]
        \[\ce{(CH3)2CHMgI + HCHO -> (CH3)2CHCH2OMgI ->[H3O+] (CH3)2CHCH2OH}\]</p>
        <p>A Grignard reagent with formaldehyde gives a <b>primary</b> alcohol with one more carbon,
        and the isopropyl skeleton is kept: 2-methylpropan-1-ol.</p>
        <p>Butan-1-ol would need an n-propyl Grignard; the 2° and 3° alcohols would need an
        aldehyde other than HCHO or a ketone.</p>
        <p><b>Answer: (3)</b></p>"""),

    # ------------------------------------------------------------------ Aldehydes, Ketones, Acids
    MCQ(src=("chemistry_2024_25_s1", "3"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>An aromatic compound \(\ce{C8H8O}\) gives an orange precipitate with 2,4-DNP and a
        yellow precipitate with \(\ce{I2}\)/NaOH, but does not reduce Tollens' reagent. On vigorous
        oxidation it gives an acid \(\ce{C7H6O2}\). The compound is</p>""",
        options=[r"phenylethanal", r"4-methylbenzaldehyde", r"2-methylbenzaldehyde", r"acetophenone"],
        answer=3,
        sol=r"""<p>2,4-DNP positive → carbonyl group; no Tollens' test → ketone, not aldehyde;
        iodoform positive → \(\ce{CH3CO-}\) group; oxidation to benzoic acid \(\ce{C7H6O2}\) → a
        single side chain on the ring. Hence \(\ce{C6H5COCH3}\).</p>
        {{fig:0}}
        <p>\[\ce{C6H5COCH3 + 3I2 + 4NaOH -> C6H5COONa + CHI3 v + 3NaI + 3H2O}\]</p>
        <p>The other three are aldehydes (Tollens' positive); 4-methylbenzaldehyde would also be
        oxidised to a dicarboxylic acid.</p>
        <p><b>Answer: (4) acetophenone</b></p>""",
        sfig=JF.fig_jc_acetophenone_tests),

    MCQ(src=("chemistry_2025_26_s1", "18"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>The correct order of <b>decreasing</b> acid strength is</p>""",
        options=[r"p-hydroxybenzoic &gt; m-hydroxybenzoic &gt; benzoic &gt; o-hydroxybenzoic",
                 r"o-hydroxybenzoic &gt; m-hydroxybenzoic &gt; benzoic &gt; p-hydroxybenzoic",
                 r"benzoic &gt; o-hydroxybenzoic &gt; m-hydroxybenzoic &gt; p-hydroxybenzoic",
                 r"o-hydroxybenzoic &gt; p-hydroxybenzoic &gt; m-hydroxybenzoic &gt; benzoic"],
        answer=1,
        sol=r"""<p>p\(K_a\): o-hydroxy 2.98, m-hydroxy 4.08, benzoic 4.20, p-hydroxy 4.58.</p>
        <ul><li><b>ortho</b>: the carboxylate is stabilised by an intramolecular hydrogen bond from the
        neighbouring OH (ortho effect) — much the strongest.</li>
        <li><b>meta</b>: OH acts only by −I, so slightly stronger than benzoic acid.</li>
        <li><b>para</b>: +R of OH pushes electron density towards the carboxylate and outweighs −I,
        so weaker than benzoic acid.</li></ul>
        {{fig:0}}
        <p><b>Answer: (2)</b></p>""",
        sfig=JF.fig_jc_salicylate),

    MCQ(src=("chemistry_2016_17", "8(b)"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>Identify D:
        \[\ce{CH3CH2Br ->[KCN] A ->[H3O+] B ->[PCl5] C ->[NH3] D}\]</p>""",
        options=[r"propanamide", r"ethanamide", r"propanenitrile", r"propan-1-amine"],
        answer=0,
        sol=r"""<p>\[\ce{CH3CH2Br + KCN -> CH3CH2CN + KBr}\ (A)\qquad
        \ce{CH3CH2CN ->[H3O+] CH3CH2COOH}\ (B)\]
        \[\ce{CH3CH2COOH + PCl5 -> CH3CH2COCl + POCl3 + HCl}\ (C)\]
        \[\ce{CH3CH2COCl + 2NH3 -> CH3CH2CONH2 + NH4Cl}\ (D)\]</p>
        <p>The cyanide step adds one carbon, so the chain has three carbons (not ethanamide);
        propanenitrile is A, and an amine would need a reduction or Hofmann step.</p>
        <p><b>Answer: (1) propanamide</b></p>"""),

    # ------------------------------------------------------------------ Nitrogen compounds
    MCQ(src=("chemistry_2024_25_s2", "1(B)(i)"), topic="Organic Compounds containing Nitrogen",
        q=r"""<p>The correct order of <b>decreasing</b> basic strength of the nitroanilines is</p>""",
        options=[r"p &gt; o &gt; m", r"o &gt; m &gt; p", r"m &gt; p &gt; o", r"p &gt; m &gt; o"],
        answer=2,
        sol=r"""<p>\(\ce{-NO2}\) withdraws electron density from the nitrogen lone pair. At <i>meta</i>
        it acts only by −I, so m-nitroaniline is the least weakened (strongest base). At <i>para</i>
        it acts by −R and −I. At <i>ortho</i> −R and the strongest −I (short range) act together,
        plus intramolecular H-bonding and steric hindrance to protonation: weakest base.
        (p\(K_b\): m 11.5, p 13.0, o 14.3.)</p>
        <p><b>Answer: (3) m &gt; p &gt; o</b></p>"""),

    MCQ(src=("chemistry_2024_25_s1", "9(i)"), topic="Organic Compounds containing Nitrogen",
        q=r"""<p>In the sequence
        \[\ce{C6H5COOH ->[SOCl2] A ->[NH3] B ->[Br2/KOH] C ->[NaNO2/HCl][\text{0–5 °C}] D ->[H2O][\text{warm}] E}\]
        E is</p>""",
        options=[r"benzyl alcohol", r"benzoic acid", r"aniline", r"phenol"],
        answer=3,
        sol=r"""<p>A = \(\ce{C6H5COCl}\); B = \(\ce{C6H5CONH2}\); Hofmann bromamide degradation removes
        one carbon: C = \(\ce{C6H5NH2}\); diazotisation: D = \(\ce{C6H5N2+Cl-}\); warming with water:
        \[\ce{C6H5N2+Cl- + H2O ->[\Delta] C6H5OH + N2 ^ + HCl}\]</p>
        <p>The C–N bond goes to the ring carbon, so the product is phenol, not benzyl alcohol.
        Aniline is C; benzoic acid is the starting material.</p>
        <p><b>Answer: (4) phenol</b></p>"""),

    # ------------------------------------------------------------------ Biomolecules
    MCQ(src=("chemistry_2025_26_s1", "1(B)(iv)"), topic="Biomolecules",
        q=r"""<p>Which nitrogenous base is a <b>purine</b> and occurs in both DNA and RNA?</p>""",
        options=[r"thymine", r"adenine", r"uracil", r"cytosine"],
        answer=1,
        sol=r"""<p>Purines (fused two-ring bases): adenine and guanine — both occur in DNA and RNA.
        Pyrimidines (single ring): cytosine (DNA and RNA), thymine (DNA only), uracil (RNA only).
        So cytosine is common to both but is a pyrimidine.</p>
        <p><b>Answer: (2) adenine</b></p>"""),

    # ================================================================== Section B (numerical)
    NUM(src=("chemistry_2025_26_s1", "5"), topic="Solutions",
        q=r"""<p>A 2 molal aqueous solution of NaCl boils 1.88 K above pure water
        (\(K_b = 0.52\) K kg mol\(^{-1}\)). Assuming the deviation of \(i\) from 2 is due only to
        incomplete dissociation, the apparent degree of dissociation of NaCl, in percent, is
        ______ (nearest integer).</p>""",
        answer=81,
        sol=r"""<p>\[i = \frac{\Delta T_b}{K_b m} = \frac{1.88}{0.52\times2} = 1.808\]
        For \(\ce{NaCl -> Na+ + Cl-}\): \(i = 1 + \alpha\Rightarrow \alpha = 0.808\) = 80.8%.</p>
        <p><b>Answer: 81</b></p>"""),

    NUM(src=("chemistry_2025_26_s2", "7"), topic="Electrochemistry",
        q=r"""<p>The conductivity of 0.00241 M acetic acid is \(7.896\times10^{-5}\) S cm\(^{-1}\) and its
        limiting molar conductivity is 390 S cm\(^2\) mol\(^{-1}\). If its dissociation constant is
        \(x\times10^{-7}\) (use \(K_a = c\alpha^2/(1-\alpha)\), without neglecting \(\alpha\)), then \(x\) is
        ______ (nearest integer).</p>""",
        answer=186,
        sol=r"""<p>\[\Lambda_m = \frac{1000\,\kappa}{c} = \frac{1000\times7.896\times10^{-5}}{0.00241} = 32.76\ \text{S cm}^2\text{ mol}^{-1}\]
        \[\alpha = \frac{\Lambda_m}{\Lambda_m^\circ} = \frac{32.76}{390} = 0.0840\]
        \[K_a = \frac{c\alpha^2}{1-\alpha} = \frac{0.00241\times(0.0840)^2}{0.916} = 1.857\times10^{-5} = 185.7\times10^{-7}\]</p>
        <p>(Dropping \(1-\alpha\) gives 170 — that approximation is not good enough here.)</p>
        <p><b>Answer: 186</b></p>"""),

    NUM(src=("chemistry_2025_26_s1", "10"), topic="Chemical Kinetics",
        q=r"""<p>The rate constant of a first-order reaction becomes six times when the temperature is
        raised from 350 K to 410 K. The activation energy of the reaction is ______ kJ mol\(^{-1}\)
        (nearest integer). (\(R = 8.314\) J K\(^{-1}\) mol\(^{-1}\), \(\log 6 = 0.778\))</p>""",
        answer=36,
        sol=r"""<p>\[\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\cdot\frac{T_2 - T_1}{T_1T_2}\]
        \[E_a = \frac{2.303\times8.314\times350\times410\times0.778}{60} = 3.56\times10^4\ \text{J mol}^{-1} = 35.6\ \text{kJ mol}^{-1}\]</p>
        <p><b>Answer: 36</b></p>"""),

    NUM(src=("chemistry_2025_26_s1", "13"), topic="d- and f-Block Elements",
        q=r"""<p>Acidified permanganate oxidises iron(II) to iron(III). When the ionic equation
        \[\ce{MnO4- + Fe^2+ + H+ -> Mn^2+ + Fe^3+ + H2O}\]
        is balanced with the smallest whole-number coefficients, the sum of all the coefficients
        (reactants and products) is ______.</p>""",
        answer=24,
        sol=r"""<p>Mn: +7 → +2 (gains 5 e\(^-\)); Fe: +2 → +3 (loses 1 e\(^-\)). So 5 \(\ce{Fe^2+}\) per
        \(\ce{MnO4-}\); balance O with water and H with \(\ce{H+}\):
        \[\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}\]
        Charge check: left \(-1 + 10 + 8 = +17\); right \(+2 + 15 = +17\).</p>
        <p>Sum \(= 1 + 5 + 8 + 1 + 5 + 4 = 24\).</p>
        <p><b>Answer: 24</b></p>"""),

    NUM(src=("chemistry_2025_26_s1", "1(B)(ii)"), topic="Coordination Compounds",
        q=r"""<p>Excess \(\ce{AgNO3}\) is added to 250 mL of a 0.02 M solution of
        dichloridotetraaquachromium(III) chloride. The amount of AgCl precipitated, in
        millimoles, is ______.</p>""",
        answer=5,
        sol=r"""<p>The compound is \(\ce{[CrCl2(H2O)4]Cl}\): the two chlorido ligands are inside the
        coordination sphere and are not precipitated; only the one counter-ion \(\ce{Cl-}\) is.</p>
        <p>Complex \(= 250\times0.02 = 5\) mmol, so AgCl \(= 5\times1 = 5\) mmol.
        (Counting all three Cl would give 15.)</p>
        <p><b>Answer: 5</b></p>"""),
]
