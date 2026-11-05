"""JEE Main mock test 2 — Chemistry (Q26–50).  Every item is adapted from a kept pre-board item."""
from jee_kit import MCQ, NUM
import chemistry_figs as JF
from chemistry_2015_16_figs import fig_azeotropes
from chemistry_2024_25_s2_figs import fig_b_mn_cft

SUBJECT = "chemistry"
TEST = 2

QUESTIONS = [
    # ------------------------------------------------------------------ Solutions
    MCQ(src=("chemistry_2013_14", "2(e)"), topic="Solutions",
        q=r"""<p>A solution containing 10.2 g of glycerine per litre is isotonic with a 2% (w/v)
        solution of glucose (\(M = 180\) g mol\(^{-1}\)) at the same temperature. The molar mass of
        glycerine is</p>""",
        options=[r"\(918\) g mol\(^{-1}\)", r"\(46\) g mol\(^{-1}\)",
                 r"\(184\) g mol\(^{-1}\)", r"\(92\) g mol\(^{-1}\)"],
        answer=3,
        sol=r"""<p>Isotonic non-electrolyte solutions at the same \(T\) have equal molar concentration
        (\(\pi = CRT\)). 2% w/v glucose = 2 g per 100 mL = 20 g L\(^{-1}\):
        \[\frac{10.2}{M} = \frac{20}{180}\;\Rightarrow\;M = \frac{10.2\times180}{20} = 91.8\approx 92\ \text{g mol}^{-1}\]</p>
        <p>918 reads 2% as 2 g per litre; 46 and 184 are the result halved and doubled.</p>
        <p><b>Answer: (4) 92 g mol\(^{-1}\)</b></p>"""),

    MCQ(src=("chemistry_2024_25_s2", "1(B)(ii)"), topic="Solutions",
        q=r"""<p>Which of the following mixtures forms a <b>minimum</b>-boiling azeotrope?</p>""",
        options=[r"benzene + toluene", r"chloroform + acetone", r"ethanol + water",
                 r"nitric acid + water"],
        answer=2,
        sol=r"""<p>A minimum-boiling azeotrope has a <i>maximum</i> vapour pressure: large positive
        deviation from Raoult's law, A–B attractions weaker than A–A and B–B. Ethanol–water
        (95.6% ethanol, b.p. 351 K) is the standard example: ethanol breaks up the hydrogen-bonded
        network of water.</p>
        {{fig:0}}
        <p>Chloroform–acetone and nitric acid–water show negative deviation (new H-bonds /
        strong attraction) and give <i>maximum</i>-boiling azeotropes; benzene–toluene is nearly
        ideal and forms no azeotrope.</p>
        <p><b>Answer: (3)</b></p>""",
        sfig=fig_azeotropes),

    # ------------------------------------------------------------------ Electrochemistry
    MCQ(src=("chemistry_2024_25_s2", "10"), topic="Electrochemistry",
        q=r"""<p>For the cell \(\ce{Ni(s) | Ni^2+ (aq) || Ag+ (aq) | Ag(s)}\) with
        \(E^\circ_{\ce{Ni^2+/Ni}} = -0.25\) V and \(E^\circ_{\ce{Ag+/Ag}} = 0.80\) V, the standard Gibbs
        energy change of the cell reaction is (F = 96500 C mol\(^{-1}\))</p>""",
        options=[r"\(-202.7\) kJ mol\(^{-1}\)", r"\(-101.3\) kJ mol\(^{-1}\)",
                 r"\(-106.2\) kJ mol\(^{-1}\)", r"\(-405.3\) kJ mol\(^{-1}\)"],
        answer=0,
        sol=r"""<p>\(\ce{Ni + 2Ag+ -> Ni^2+ + 2Ag}\), \(n = 2\);
        \(E^\circ_\text{cell} = 0.80 - (-0.25) = 1.05\) V.</p>
        <p>\[\Delta G^\circ = -nFE^\circ = -2\times96500\times1.05 = -2.027\times10^5\ \text{J mol}^{-1} = -202.7\ \text{kJ mol}^{-1}\]</p>
        <p>\(-101.3\) uses \(n = 1\); \(-106.2\) uses \(E^\circ = 0.80 - 0.25 = 0.55\) V (sign of the
        Ni potential dropped); \(-405.3\) doubles \(E^\circ\) because 2 Ag appear (potentials are
        intensive and are never multiplied by coefficients).</p>
        <p><b>Answer: (1)</b></p>"""),

    MCQ(src=("chemistry_2013_14", "3(c)"), topic="Electrochemistry",
        q=r"""<p>The limiting molar conductivities of NaOH, NaCl and \(\ce{BaCl2}\) are
        \(2.481\times10^{-2}\), \(1.265\times10^{-2}\) and \(2.800\times10^{-2}\) S m\(^2\) mol\(^{-1}\)
        respectively. \(\Lambda_m^\circ\) for \(\ce{Ba(OH)2}\) is</p>""",
        options=[r"\(4.016\times10^{-2}\) S m\(^2\) mol\(^{-1}\)", r"\(5.232\times10^{-2}\) S m\(^2\) mol\(^{-1}\)",
                 r"\(6.497\times10^{-2}\) S m\(^2\) mol\(^{-1}\)", r"\(0.368\times10^{-2}\) S m\(^2\) mol\(^{-1}\)"],
        answer=1,
        sol=r"""<p>Kohlrausch's law: build \(\ce{Ba^2+}\) + \(2\ce{OH-}\) from the given electrolytes.
        \[\Lambda^\circ(\ce{Ba(OH)2}) = \Lambda^\circ(\ce{BaCl2}) + 2\Lambda^\circ(\ce{NaOH}) - 2\Lambda^\circ(\ce{NaCl})\]
        \[= (2.800 + 4.962 - 2.530)\times10^{-2} = 5.232\times10^{-2}\ \text{S m}^2\text{ mol}^{-1}\]</p>
        <p>4.016 forgets both factors of 2; 6.497 doubles NaOH but not NaCl (leaving a stray
        \(\ce{Na+}\)); 0.368 reverses the signs of NaOH and NaCl.</p>
        <p><b>Answer: (2)</b></p>"""),

    # ------------------------------------------------------------------ Chemical Kinetics
    MCQ(src=("chemistry_2024_25_s2", "18"), topic="Chemical Kinetics",
        q=r"""<p>For \(\ce{2NO2 + F2 -> 2NO2F}\) the initial rates are:</p>
        <table class="tbl"><tr><th>[\(\ce{NO2}\)] / mol L\(^{-1}\)</th><th>[\(\ce{F2}\)] / mol L\(^{-1}\)</th><th>rate / mol L\(^{-1}\) min\(^{-1}\)</th></tr>
        <tr><td>0.20</td><td>0.05</td><td>\(6.0\times10^{-3}\)</td></tr>
        <tr><td>0.40</td><td>0.05</td><td>\(1.2\times10^{-2}\)</td></tr>
        <tr><td>0.80</td><td>0.10</td><td>\(4.8\times10^{-2}\)</td></tr></table>
        <p>The rate law and rate constant are</p>""",
        options=[r"rate \(= k[\ce{NO2}][\ce{F2}]\), \(k = 0.6\) L mol\(^{-1}\) min\(^{-1}\)",
                 r"rate \(= k[\ce{NO2}]^2[\ce{F2}]\), \(k = 3.0\) L\(^2\) mol\(^{-2}\) min\(^{-1}\)",
                 r"rate \(= k[\ce{NO2}]\), \(k = 0.03\) min\(^{-1}\)",
                 r"rate \(= k[\ce{NO2}][\ce{F2}]^2\), \(k = 12\) L\(^2\) mol\(^{-2}\) min\(^{-1}\)"],
        answer=0,
        sol=r"""<p>Rows 1→2 ([\(\ce{F2}\)] fixed): \([\ce{NO2}]\) doubles, rate doubles ⇒ order 1 in \(\ce{NO2}\).
        Rows 2→3: both double, rate \(\times4 = 2\times2^y\) ⇒ order 1 in \(\ce{F2}\).</p>
        <p>\[k = \frac{6.0\times10^{-3}}{0.20\times0.05} = 0.6\ \text{L mol}^{-1}\text{ min}^{-1}\]</p>
        <p>The orders do not follow the stoichiometric coefficient 2 of \(\ce{NO2}\) (option 2);
        option 3 ignores the \(\ce{F2}\) dependence shown by row 3; option 4 would make row 3
        eight times row 2, not four.</p>
        <p><b>Answer: (1)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s1", "2"), topic="Chemical Kinetics",
        q=r"""<p>The \(\ce{^14C}\) content of an ancient wooden object is 10% of that in living wood.
        Taking \(t_{1/2}(\ce{^14C}) = 5730\) y, the age of the object is about</p>""",
        options=[r"\(871\) y", r"\(19\,040\) y", r"\(28\,650\) y", r"\(57\,300\) y"],
        answer=1,
        sol=r"""<p>Radioactive decay is first order: \(k = 0.693/5730 = 1.209\times10^{-4}\) y\(^{-1}\).
        \[t = \frac{2.303}{k}\log\frac{[A]_0}{[A]} = \frac{2.303}{1.209\times10^{-4}}\log 10 = 1.904\times10^4\ \text{y}\]</p>
        <p>871 y is the time for 10% to decay (ratio 100/90 used); 28 650 y (5 half-lives) and
        57 300 y (10 half-lives) treat the decay as linear in the number of half-lives.</p>
        <p><b>Answer: (2) about 19 040 y</b></p>"""),

    # ------------------------------------------------------------------ d- and f-Block
    MCQ(src=("chemistry_2014_15", "1(b)(v)"), topic="d- and f-Block Elements",
        q=r"""<p>The lanthanoid contraction is caused by</p>""",
        options=[r"the increase in atomic number alone",
                 r"the increase in size of the 4f orbitals",
                 r"the filling of the 5d orbitals",
                 r"the imperfect shielding of one 4f electron by another"],
        answer=3,
        sol=r"""<p>Across La → Lu each added proton is matched by an electron entering the 4f subshell.
        4f orbitals are diffuse and shield each other poorly, so the effective nuclear charge felt by
        the outer electrons rises steadily and the atoms/ions shrink.</p>
        <p>The rising atomic number alone would be cancelled by perfect shielding; the 4f orbitals
        do not grow; the electrons enter 4f, not 5d.</p>
        <p><b>Answer: (4)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s2", "8"), topic="d- and f-Block Elements",
        q=r"""<p>Both \(\ce{Cr^2+}\) and \(\ce{Mn^3+}\) are \(d^4\) ions. Which statement is correct?</p>""",
        options=[r"\(\ce{Cr^2+}\) is oxidising because \(\ce{Cr+}\) would be \(d^5\)",
                 r"\(\ce{Mn^3+}\) is reducing because \(\ce{Mn^4+}\) is \(d^3\)",
                 r"\(\ce{Cr^2+}\) is reducing because \(\ce{Cr^3+}\) has the stable \(t_{2g}^3\) configuration",
                 r"both are oxidising because \(d^4\) is unstable"],
        answer=2,
        sol=r"""<p>\(\ce{Cr^2+ -> Cr^3+ + e-}\) gives \(d^3\), a half-filled \(t_{2g}\) set — very stable —
        so \(\ce{Cr^2+}\) is a strong reducing agent (\(E^\circ_{\ce{Cr^3+/Cr^2+}} = -0.41\) V).
        \(\ce{Mn^3+ + e- -> Mn^2+}\) gives \(d^5\), the stable half-filled \(d\) subshell, so
        \(\ce{Mn^3+}\) is a strong oxidising agent (\(E^\circ = +1.57\) V).</p>
        <p>Options 1 and 2 reverse the direction of change; option 4 ignores that \(\ce{Cr^2+}\)
        is reducing.</p>
        <p><b>Answer: (3)</b></p>"""),

    # ------------------------------------------------------------------ Coordination
    MCQ(src=("chemistry_2024_25_s2", "15"), topic="Coordination Compounds",
        q=r"""<p>The crystal field stabilisation energy of \(\ce{[Mn(CN)6]^3-}\) (\(P\) = pairing
        energy) is</p>""",
        options=[r"\(-0.6\,\Delta_o\)", r"\(-1.6\,\Delta_o + P\)", r"\(-2.4\,\Delta_o + 2P\)",
                 r"\(-1.2\,\Delta_o\)"],
        answer=1,
        sol=r"""<p>\(\ce{Mn^3+}\) is \(3d^4\). \(\ce{CN-}\) is strong field (\(\Delta_o > P\)), so the
        complex is low spin: \(t_{2g}^4e_g^0\), with one pair more than in the free ion.</p>
        <p>\[\text{CFSE} = 4(-0.4\Delta_o) + 0(+0.6\Delta_o) + P = -1.6\Delta_o + P\]</p>
        {{fig:0}}
        <p>\(-0.6\Delta_o\) is high spin \(t_{2g}^3e_g^1\) (e.g. \(\ce{[MnCl6]^3-}\)); \(-2.4\Delta_o + 2P\)
        is low-spin \(d^6\); \(-1.2\Delta_o\) is \(d^3\).</p>
        <p><b>Answer: (2)</b></p>""",
        sfig=fig_b_mn_cft),

    MCQ(src=("chemistry_2014_15", "7(a)"), topic="Coordination Compounds",
        q=r"""<p>The IUPAC name of \(\ce{[Co(NH3)6][Cr(CN)6]}\) is</p>""",
        options=[r"hexaamminecobalt(III) hexacyanidochromate(III)",
                 r"hexaamminecobalt(III) hexacyanidochromium(III)",
                 r"hexacyanidochromium(III) hexaamminecobaltate(III)",
                 r"hexaamminecobalt(III) hexacyanidochromate(II)"],
        answer=0,
        sol=r"""<p>Cation first, then anion. \(\ce{[Co(NH3)6]^3+}\) (Co +3) and \(\ce{[Cr(CN)6]^3-}\)
        (Cr: \(x - 6 = -3\Rightarrow x = +3\)). An <b>anionic</b> complex takes the suffix
        <i>-ate</i>: chromate.</p>
        <p>Option 2 omits <i>-ate</i> in the anion; option 3 names the anion first and puts
        <i>-ate</i> on the cation; option 4 gives Cr +2, which would make the anion
        \(\ce{[Cr(CN)6]^4-}\) and the salt unbalanced against \(\ce{[Co(NH3)6]^3+}\).</p>
        <p><b>Answer: (1)</b></p>"""),

    # ------------------------------------------------------------------ Haloalkanes
    MCQ(src=("chemistry_2024_25_s1", "1(B)(iii)"), topic="Haloalkanes and Haloarenes",
        q=r"""<p>Toluene is treated with chlorine in the dark in the presence of anhydrous
        \(\ce{FeCl3}\). The main product is</p>""",
        options=[r"benzyl chloride", r"m-chlorotoluene",
                 r"a mixture of o- and p-chlorotoluene", r"benzal chloride, \(\ce{C6H5CHCl2}\)"],
        answer=2,
        sol=r"""<p>With a Lewis acid and no light the reaction is electrophilic substitution in the ring
        (\(\ce{Cl+}\) from \(\ce{Cl2/FeCl3}\)). \(\ce{-CH3}\) is ortho/para directing (+I,
        hyperconjugation), so o- and p-chlorotoluene are formed.</p>
        <p>Benzyl chloride and benzal chloride come from free-radical side-chain chlorination in light
        or heat without a catalyst; the meta isomer is a minor product.</p>
        <p><b>Answer: (3)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s2", "1(A)(iv)"), topic="Haloalkanes and Haloarenes",
        q=r"""<p>Propene reacts with \(\ce{Cl2}\) at 773 K to give</p>""",
        options=[r"1,2-dichloropropane by electrophilic addition",
                 r"2-chloropropane by Markovnikov addition",
                 r"1-chloroprop-1-ene by elimination",
                 r"3-chloroprop-1-ene by free-radical substitution"],
        answer=3,
        sol=r"""<p>At high temperature \(\ce{Cl2}\) dissociates into radicals and substitution occurs at
        the allylic carbon, whose radical is resonance stabilised:
        \[\ce{CH2=CH-CH3 + Cl2 ->[773 K] CH2=CH-CH2Cl + HCl}\]
        (allyl chloride, 3-chloroprop-1-ene).</p>
        <p>Addition to give 1,2-dichloropropane happens at room temperature; 2-chloropropane needs HCl,
        not \(\ce{Cl2}\); no elimination is involved.</p>
        <p><b>Answer: (4)</b></p>"""),

    # ------------------------------------------------------------------ Alcohols, Phenols, Ethers
    MCQ(src=("chemistry_2025_26_s2", "1(A)(iii)"), topic="Alcohols, Phenols and Ethers",
        q=r"""<p>Which alcohol gives turbidity <b>immediately</b> with Lucas reagent at room temperature?</p>""",
        options=[r"butan-1-ol", r"butan-2-ol", r"2-methylpropan-2-ol", r"2-methylpropan-1-ol"],
        answer=2,
        sol=r"""<p>Lucas reagent (conc. HCl + anhydrous \(\ce{ZnCl2}\)) converts the alcohol into an
        insoluble alkyl chloride via a carbocation, so the speed follows carbocation stability.
        2-Methylpropan-2-ol (3°) reacts at once:
        \(\ce{(CH3)3COH + HCl ->[ZnCl2] (CH3)3CCl + H2O}\).</p>
        <p>Butan-2-ol (2°) turns turbid in about 5 min; the two primary alcohols do not react at
        room temperature.</p>
        <p><b>Answer: (3)</b></p>"""),

    MCQ(src=("chemistry_2016_17", "1(c)(i)"), topic="Alcohols, Phenols and Ethers",
        q=r"""<p>Which of the following dissolves in aqueous sodium hydrogencarbonate with
        effervescence?</p>""",
        options=[r"phenol", r"4-methylphenol", r"4-nitrophenol", r"2,4,6-trinitrophenol"],
        answer=3,
        sol=r"""<p>\(\ce{NaHCO3}\) liberates \(\ce{CO2}\) only from an acid stronger than carbonic acid
        (p\(K_a\) 6.4). Picric acid (p\(K_a\) 0.4) qualifies: its three \(\ce{-NO2}\) groups at o and p
        delocalise the charge of the phenoxide ion by −R and −I.
        \[\ce{C6H2(NO2)3OH + NaHCO3 -> C6H2(NO2)3ONa + CO2 ^ + H2O}\]</p>
        <p>Phenol (10.0), 4-methylphenol (10.2) and even 4-nitrophenol (7.1) are weaker than carbonic
        acid, so they do not react.</p>
        <p><b>Answer: (4)</b></p>"""),

    # ------------------------------------------------------------------ Aldehydes, Ketones, Acids
    MCQ(src=("chemistry_2024_25_s2", "3"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>The correct order of <b>decreasing</b> reactivity towards nucleophilic addition of HCN is</p>""",
        options=[r"ethanal &gt; propanal &gt; propanone &gt; butanone",
                 r"butanone &gt; propanone &gt; propanal &gt; ethanal",
                 r"propanone &gt; ethanal &gt; butanone &gt; propanal",
                 r"ethanal &gt; propanone &gt; propanal &gt; butanone"],
        answer=0,
        sol=r"""<p>Alkyl groups (+I) reduce the positive character of the carbonyl carbon and crowd the
        approach of the nucleophile. Aldehydes have one alkyl group and ketones two, so aldehydes are
        more reactive; within each pair the larger alkyl group (ethyl &gt; methyl) lowers reactivity
        further: ethanal &gt; propanal &gt; propanone &gt; butanone.</p>
        <p>Option 4 puts a ketone ahead of an aldehyde; options 2 and 3 reverse the trend.</p>
        <p><b>Answer: (1)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s2", "9(i)"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>A mixture of propanal and 2-methylpropanal is treated with dilute NaOH. The number of
        different β-hydroxy aldehydes (aldols) that can form is (count structural isomers only)</p>""",
        options=[r"\(2\)", r"\(4\)", r"\(3\)", r"\(1\)"],
        answer=1,
        sol=r"""<p>Both aldehydes have α-H (propanal two, 2-methylpropanal one), so each forms an enolate
        and each can be attacked: 2 donors × 2 acceptors = 4 aldols.</p>
        <ul><li>propanal + propanal: \(\ce{CH3CH2CH(OH)CH(CH3)CHO}\), 3-hydroxy-2-methylpentanal</li>
        <li>2-methylpropanal + 2-methylpropanal: \(\ce{(CH3)2CHCH(OH)C(CH3)2CHO}\),
        3-hydroxy-2,2,4-trimethylpentanal</li>
        <li>enolate of propanal + 2-methylpropanal: \(\ce{(CH3)2CHCH(OH)CH(CH3)CHO}\),
        3-hydroxy-2,4-dimethylpentanal</li>
        <li>enolate of 2-methylpropanal + propanal: \(\ce{CH3CH2CH(OH)C(CH3)2CHO}\),
        3-hydroxy-2,2-dimethylpentanal</li></ul>
        <p>Counting only the two crossed products (2) or only the self products misses half. Note
        that the aldols with a quaternary α-carbon cannot dehydrate, but they are still aldols.</p>
        <p><b>Answer: (2) 4</b></p>"""),

    MCQ(src=("chemistry_2015_16", "10(a)"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>Toluene is oxidised by chromyl chloride in \(\ce{CCl4}\) (followed by hydrolysis) to B,
        which gives a silver mirror with Tollens' reagent. B with concentrated NaOH gives C and D.
        C and D are</p>""",
        options=[r"\(\ce{C6H5CH2OH}\) and \(\ce{C6H5COONa}\)",
                 r"\(\ce{C6H5COOH}\) and \(\ce{C6H5CH3}\)",
                 r"\(\ce{C6H5CH2OH}\) and \(\ce{HCOONa}\)",
                 r"\(\ce{C6H5CH(OH)COC6H5}\) and \(\ce{NaCl}\)"],
        answer=0,
        sol=r"""<p>Étard reaction: \(\ce{C6H5CH3 ->[CrO2Cl2/CCl4][H3O+] C6H5CHO}\) (B, benzaldehyde).
        Benzaldehyde has no α-H, so in concentrated alkali it undergoes the Cannizzaro reaction:
        \[\ce{2C6H5CHO + NaOH -> C6H5CH2OH + C6H5COONa}\]</p>
        <p>Sodium formate is formed only in a <i>crossed</i> Cannizzaro with HCHO; benzoin needs
        alcoholic KCN; toluene is not regenerated.</p>
        <p><b>Answer: (1)</b></p>"""),

    # ------------------------------------------------------------------ Nitrogen compounds
    MCQ(src=("chemistry_2025_26_s2", "18"), topic="Organic Compounds containing Nitrogen",
        q=r"""<p>Identify C:
        \[\ce{C6H5N2+Cl- ->[CuCN][\Delta] A ->[H3O+] B ->[NH3][\Delta] C}\]</p>""",
        options=[r"aniline", r"benzonitrile", r"benzylamine", r"benzamide"],
        answer=3,
        sol=r"""<p>Sandmeyer: A = \(\ce{C6H5CN}\); acid hydrolysis: B = \(\ce{C6H5COOH}\);
        with \(\ce{NH3}\) then heat:
        \[\ce{C6H5COOH + NH3 -> C6H5COONH4 ->[\Delta] C6H5CONH2 + H2O}\]</p>
        <p>Benzonitrile is A; benzylamine needs reduction of A; aniline needs a further Hofmann step.</p>
        <p><b>Answer: (4) benzamide</b></p>"""),

    MCQ(src=("chemistry_2024_25_s1", "6"), topic="Organic Compounds containing Nitrogen",
        q=r"""<p>The correct order of basic strength in <b>aqueous solution</b> is</p>""",
        options=[r"\(\ce{(CH3)3N}\) &gt; \(\ce{(CH3)2NH}\) &gt; \(\ce{CH3NH2}\) &gt; \(\ce{NH3}\)",
                 r"\(\ce{(CH3)2NH}\) &gt; \(\ce{CH3NH2}\) &gt; \(\ce{(CH3)3N}\) &gt; \(\ce{NH3}\)",
                 r"\(\ce{CH3NH2}\) &gt; \(\ce{(CH3)2NH}\) &gt; \(\ce{(CH3)3N}\) &gt; \(\ce{NH3}\)",
                 r"\(\ce{NH3}\) &gt; \(\ce{CH3NH2}\) &gt; \(\ce{(CH3)2NH}\) &gt; \(\ce{(CH3)3N}\)"],
        answer=1,
        sol=r"""<p>Three factors act together in water: the +I effect of methyl groups (raises basicity),
        solvation of the protonated amine by hydrogen bonding (falls as N–H bonds are lost) and
        steric hindrance. For methylamines the balance gives
        \(\ce{(CH3)2NH}\) &gt; \(\ce{CH3NH2}\) &gt; \(\ce{(CH3)3N}\) &gt; \(\ce{NH3}\) (p\(K_b\) 3.27, 3.38, 4.22, 4.75).</p>
        <p>Option 1 is the gas-phase (inductive-only) order; options 3 and 4 ignore the +I effect
        or misplace \(\ce{(CH3)3N}\).</p>
        <p><b>Answer: (2)</b></p>"""),

    # ------------------------------------------------------------------ Biomolecules
    MCQ(src=("chemistry_2024_25_s1", "17"), topic="Biomolecules",
        q=r"""<p>Sucrose (\([\alpha]_D = +66.5^\circ\)) is hydrolysed completely into an equimolar
        mixture of D-glucose (\(+52.5^\circ\)) and D-fructose (\(-92.4^\circ\)). The specific rotation
        of the resulting invert sugar is about</p>""",
        options=[r"\(+66.5^\circ\)", r"\(-39.9^\circ\)", r"\(-20^\circ\)", r"\(+20^\circ\)"],
        answer=2,
        sol=r"""<p>Equal amounts of the two sugars: the rotation is the average.
        \[[\alpha]_\text{mix} = \frac{52.5 + (-92.4)}{2} = -19.95^\circ\approx -20^\circ\]</p>
        {{fig:0}}
        <p>The sign changes from (+) to (−): hence "inversion" and "invert sugar". \(-39.9^\circ\)
        adds the two without averaging; \(+20^\circ\) has the wrong sign; \(+66.5^\circ\) is sucrose.</p>
        <p><b>Answer: (3)</b></p>""",
        sfig=JF.fig_jc_invert_rotation),

    # ================================================================== Section B (numerical)
    NUM(src=("chemistry_2014_15", "2(a)"), topic="Solutions",
        q=r"""<p>75.2 g of phenol is dissolved in 1 kg of a solvent with \(K_f = 14\) K kg mol\(^{-1}\).
        The depression in freezing point is 7 K. The percentage of phenol that dimerises is ______
        (\(M_\text{phenol} = 94\) g mol\(^{-1}\)).</p>""",
        answer=75,
        sol=r"""<p>\(m = 75.2/94 = 0.8\) mol kg\(^{-1}\); expected \(\Delta T_f = 14\times0.8 = 11.2\) K.
        \[i = \frac{7}{11.2} = 0.625\]
        For \(\ce{2C6H5OH <=> (C6H5OH)2}\) with fraction \(\alpha\) dimerised:
        \(i = 1 - \alpha + \alpha/2 = 1 - \alpha/2\Rightarrow \alpha = 0.75\).</p>
        <p><b>Answer: 75</b></p>"""),

    NUM(src=("chemistry_2024_25_s2", "16 OR"), topic="Electrochemistry",
        q=r"""<p>A solution of \(\ce{Ni(NO3)2}\) is electrolysed between platinum electrodes with a
        current of 5 A for 2 hours. The mass of nickel deposited at the cathode is ______ g
        (nearest integer). (Ni = 58.7 g mol\(^{-1}\), F = 96500 C mol\(^{-1}\))</p>""",
        answer=11,
        sol=r"""<p>\(Q = 5\times7200 = 36\,000\) C. \(\ce{Ni^2+ + 2e- -> Ni}\):
        \[n(\ce{Ni}) = \frac{36\,000}{2\times96\,500} = 0.1865\ \text{mol};\qquad m = 0.1865\times58.7 = 10.95\ \text{g}\]</p>
        <p><b>Answer: 11</b></p>"""),

    NUM(src=("chemistry_2024_25_s2", "5"), topic="Chemical Kinetics",
        q=r"""<p>The rate constant of a first-order reaction varies with temperature as
        \[\log k = 11.9 - \frac{3500}{T}\]
        The activation energy of the reaction is ______ kJ mol\(^{-1}\) (nearest integer).
        (\(R = 8.314\) J K\(^{-1}\) mol\(^{-1}\))</p>""",
        answer=67,
        sol=r"""<p>Arrhenius in log form: \(\log k = \log A - \dfrac{E_a}{2.303RT}\). Comparing,
        \[\frac{E_a}{2.303R} = 3500\;\Rightarrow\;E_a = 3500\times2.303\times8.314 = 6.70\times10^4\ \text{J mol}^{-1} = 67.0\ \text{kJ mol}^{-1}\]</p>
        <p>(Forgetting the 2.303 — reading the slope as \(E_a/R\) — gives 29.)</p>
        <p><b>Answer: 67</b></p>"""),

    NUM(src=("chemistry_2025_26_s2", "13"), topic="d- and f-Block Elements",
        q=r"""<p>The volume of 0.02 M \(\ce{KMnO4}\) needed to oxidise completely 50 mL of 0.05 M
        oxalic acid in the presence of dilute \(\ce{H2SO4}\) is ______ mL.</p>""",
        answer=50,
        sol=r"""<p>\[\ce{2KMnO4 + 5H2C2O4 + 3H2SO4 -> K2SO4 + 2MnSO4 + 10CO2 + 8H2O}\]
        Oxalic acid \(= 50\times0.05 = 2.5\) mmol, so \(\ce{KMnO4} = \tfrac{2}{5}\times2.5 = 1.0\) mmol.
        \[V = \frac{1.0}{0.02} = 50\ \text{mL}\]</p>
        <p>(Ratio inverted, 5:2, gives 312.5 mL.)</p>
        <p><b>Answer: 50</b></p>"""),

    NUM(src=("chemistry_2025_26_s1", "1(B)(i)"), topic="Coordination Compounds",
        q=r"""<p>The total number of unpaired electrons in the four aqua ions
        \(\ce{[Cr(H2O)6]^3+}\), \(\ce{[Fe(H2O)6]^2+}\), \(\ce{[Cu(H2O)6]^2+}\) and
        \(\ce{[Zn(H2O)6]^2+}\) taken together is ______.</p>""",
        answer=8,
        sol=r"""<p>Water is a weak-field ligand, so all are high spin.</p>
        <table class="tbl"><tr><th>ion</th><th>configuration</th><th>unpaired</th></tr>
        <tr><td>\(\ce{Cr^3+}\)</td><td>\(3d^3\), \(t_{2g}^3\)</td><td>3</td></tr>
        <tr><td>\(\ce{Fe^2+}\)</td><td>\(3d^6\), \(t_{2g}^4e_g^2\)</td><td>4</td></tr>
        <tr><td>\(\ce{Cu^2+}\)</td><td>\(3d^9\), \(t_{2g}^6e_g^3\)</td><td>1</td></tr>
        <tr><td>\(\ce{Zn^2+}\)</td><td>\(3d^{10}\)</td><td>0</td></tr></table>
        <p>Total \(= 3 + 4 + 1 + 0 = 8\).</p>
        <p><b>Answer: 8</b></p>"""),
]
