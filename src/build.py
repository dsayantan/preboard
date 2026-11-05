"""Build the site.   python3 src/build.py [module ...]

With no argument builds every paper in src/data and the index pages.
With module names (e.g. physics_2013_14) builds just those papers (and the index pages).
Exits non-zero if any paper fails kit.check() or any figure fails the SVG checks.
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit

def main(argv):
    papers = kit.load_papers()
    want = set(argv)
    bad = False
    built = []
    for mod, P in papers:
        errs, warns = kit.check(P)
        if want and mod not in want:
            continue
        html, figs = kit.render_paper(P, mod)
        for f in set(figs):
            pass
        # svg checks + page-wide id uniqueness
        ids = {}
        for it in P["items"]:
            if it["kind"] != "q":
                continue
            for fn, _ in it["qfig"] + it["afig"]:
                svg = fn()
                errs += kit.svg_problems(svg, fn.__name__)
        for m in re.finditer(r'<svg.*?</svg>', html, re.S):
            for i in re.findall(r'\bid="([^"]+)"', m.group(0)):
                ids.setdefault(i, set()).add(m.start())
        dup = [i for i, s in ids.items() if len(s) > 1]
        if dup:
            errs.append(f"SVG ids reused across figures: {dup[:8]}")
        for w in warns:
            print(f"  warn {mod}: {w}")
        if errs:
            bad = True
            for e in errs:
                print(f"  ERROR {mod}: {e}")
            continue
        d = os.path.join(kit.ROOT, P["subject"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, kit.slug(P) + ".html"), "w").write(html)
        n = sum(1 for i in P["items"] if i["kind"] == "q" and not i["excluded"])
        x = sum(1 for i in P["items"] if i["kind"] == "q" and i["excluded"])
        print(f"built {P['subject']}/{kit.slug(P)}.html  kept {n}, excluded {x}, figures {len(figs)}")
        built.append(mod)
    build_index(papers)
    return 1 if bad else 0


def build_index(papers):
    by = {}
    for mod, P in papers:
        by.setdefault(P["subject"], []).append(P)
    cards = []
    for s, name in kit.SUBJECTS:
        ps = sorted(by.get(s, []), key=lambda P: kit.slug(P))
        def rows(group):
            out = []
            for P in group:
                n = sum(1 for i in P["items"] if i["kind"] == "q" and not i["excluded"])
                x = sum(1 for i in P["items"] if i["kind"] == "q" and i["excluded"])
                out.append(f'<li><a href="{kit.slug(P)}.html">{kit.esc(P["year"])} — {kit.esc(P["paper"])}</a>'
                           f'<span class="cnt">{n} questions · ' + (f'{x} out of syllabus' if x else 'all in syllabus') + '</span></li>')
            return "".join(out)
        theory = [P for P in ps if not P.get("practical")]
        prac = [P for P in ps if P.get("practical")]
        main = f'<h2 class="sec">Theory papers</h2><ul class="papers">{rows(theory) or "<li>No papers yet.</li>"}</ul>'
        if prac:
            main += f'<h2 class="sec">Practical papers</h2><ul class="papers">{rows(prac)}</ul>'
        body = (f'<header class="top"><a class="crumb" href="../index.html">Pre-Board Revision</a>'
                f'<h1>{name}</h1><p class="meta">Heritage School pre-board papers, solved. '
                f'Only questions in the ISC 2027 syllabus are answered.</p></header>'
                f'<main>{main}</main>')
        d = os.path.join(kit.ROOT, s)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(kit.page(f"{name} · Pre-Board Revision", body, 1))
        tot = sum(sum(1 for i in P["items"] if i["kind"] == "q" and not i["excluded"]) for P in ps)
        cards.append(f'<a class="card" href="{s}/index.html"><h2>{name}</h2>'
                     f'<p>{len(ps)} papers · {tot} solved questions</p></a>')
    # JEE Main mock tests (src/build_jee.py): a card and one line, only once jee/index.html exists.
    jee_line = ""
    if os.path.exists(os.path.join(kit.ROOT, "jee", "index.html")):
        nt = len([f for f in os.listdir(os.path.join(kit.ROOT, "jee")) if re.fullmatch(r"test-\d+\.html", f)])
        cards.append('<a class="card" href="jee/index.html"><h2>JEE Main mock tests</h2>'
                     f'<p>{nt} of 3 tests ready · 75 questions · 3 hours</p></a>')
        jee_line = (' The <a href="jee/index.html">JEE Main mock tests</a> rework these questions into '
                    'timed computer-based tests, +4/−1, with worked solutions after you submit.')
    body = ('<header class="top"><h1>ISC Pre-Board Revision</h1>'
            '<p class="meta">Heritage School Class XII pre-board papers (2013-14 to 2016-17, 2024-25 and 2025-26), '
            'filtered to the ISC 2027 syllabus and solved question by question — '
            'with the diagrams the questions show and the diagrams the answers need.</p></header>'
            f'<main><div class="cards">{"".join(cards)}</div>'
            '<p class="foot">Each question carries its marks and topic; the answer is hidden until you ask for it, '
            'with a <em>Concepts to recall</em> panel beside it. Tick <em>revised</em> to track progress '
            '(kept in this browser only).' + jee_line + '</p></main>')
    open(os.path.join(kit.ROOT, "index.html"), "w").write(kit.page("ISC Pre-Board Revision", body, 0))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
