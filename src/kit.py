"""Pre-board revision site kit.

One data module per paper:  src/data/<subject>_<year>[_prac].py   e.g. physics_2013_14.py,
physics_2013_14_prac.py.  It defines PAPER:

    from kit import Q, SEC
    PAPER = dict(
        subject  = "physics",              # physics | chemistry | maths | computers
        year     = "2013-14",
        slug     = "2013-14",               # output file name: 2013-14 | 2013-14-practical | 2015-16-paper-2
        paper    = "Paper 1 (Theory)",      # as printed
        source   = "PreBoard-PYQ/2013-14/Physics.pdf",
        marks    = 70, time = "3 hours",    # as printed on the paper
        practical = False,                  # True for practical papers (listed under their own heading)
        intro    = "<p>…general instructions, as printed…</p>",   # optional
        items    = [
            SEC("Part I", "Answer all questions."),             # section heading, as printed
            Q("1(a)(i)", 1, r"<p>State Gauss's theorem …</p>",
              a=r"<p>…</p>",
              topic="Electrostatics",
              recall=r"<ul><li>…concept to remember…</li></ul>",
              qfig=figs.fig_xxx,         # the diagram PRINTED IN THE QUESTION (redrawn)
              afig=[figs.fig_yyy],       # diagrams that belong IN THE ANSWER
              ),
            Q("3", 2, r"<p>…</p>", excluded="Not in ISC 2027: Thermodynamics is Class XI."),
            ...
        ])

Rules
- Every question in the paper appears, in printed order (this is the digital copy).
  A question outside the ISC 2027 syllabus gets `excluded="<reason>"` and no answer.
- Math: KaTeX.  Inline \\( … \\), display \\[ … \\].  Chemistry: \\(\\ce{K2Cr2O7}\\) (mhchem).
  Write strings as r"" raw strings.
- Code: <pre class="code">…</pre> (escape < > &).
- A figure is a zero-argument function named fig_* returning an <svg> string with a viewBox
  (no width/height attributes needed).  Never put HTML tags inside SVG <text>;
  use <tspan baseline-shift="sub"> / font-style="italic".  Every id inside an SVG
  (markers, gradients) must be unique across the whole page — prefix with the fig name.
- `qfig` / `afig` take a function or a list of functions.  Captions: pass (fn, "caption").
  Place a figure inside the text with {{fig:0}}, {{fig:1}} … (index into that list);
  figures not placed are appended after the text.
"""
import html, re, os, json, importlib, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJECTS = [("physics", "Physics"), ("chemistry", "Chemistry"),
            ("maths", "Mathematics"), ("computers", "Computer Science")]
SUBJ_NAME = dict(SUBJECTS)


def SEC(title, note=""):
    return dict(kind="sec", title=title, note=note)


def Q(num, marks, q, a="", topic="", recall="", qfig=None, afig=None, excluded=None):
    return dict(kind="q", num=str(num), marks=marks, q=q, a=a, topic=topic, recall=recall,
                qfig=_figlist(qfig), afig=_figlist(afig), excluded=excluded)


def _figlist(f):
    if f is None:
        return []
    if callable(f) or isinstance(f, tuple):
        f = [f]
    out = []
    for x in f:
        fn, cap = (x if isinstance(x, tuple) else (x, ""))
        out.append((fn, cap))
    return out


# ------------------------------------------------------------------ checks
FIG_WORDS = re.compile(r"\b(diagram|draw|sketch|figure|circuit diagram|graph|ray diagram|plot)\b", re.I)


def check(P):
    errs, warns = [], []
    for k in ("subject", "year", "slug", "paper", "source", "items"):
        if not P.get(k):
            errs.append(f"PAPER missing {k}")
    nums = set()
    for it in P["items"]:
        if it["kind"] != "q":
            continue
        n = it["num"]
        if n in nums:
            errs.append(f"duplicate question number {n}")
        nums.add(n)
        if not it["q"].strip():
            errs.append(f"{n}: empty question")
        if it["excluded"]:
            if it["a"].strip():
                warns.append(f"{n}: excluded but has an answer")
        else:
            if not it["a"].strip():
                errs.append(f"{n}: no answer")
            if not it["topic"]:
                errs.append(f"{n}: no topic")
            if not it["recall"].strip():
                warns.append(f"{n}: no recall panel")
            if FIG_WORDS.search(re.sub(r"<[^>]+>", " ", it["q"])) and not (it["qfig"] or it["afig"]):
                errs.append(f"{n}: question mentions a diagram/graph but carries no figure")
        for txt in (it["q"], it["a"], it["recall"]):
            if "{{fig:" in txt and txt is it["recall"]:
                errs.append(f"{n}: figure placeholder in recall")
            for d1, d2 in ((r"\(", r"\)"), (r"\[", r"\]")):
                if txt.count(d1) != txt.count(d2):
                    errs.append(f"{n}: unbalanced {d1} {d2}")
    return errs, warns


def svg_problems(svg, name):
    errs = []
    if "<svg" not in svg:
        errs.append(f"{name}: not an svg")
    if "viewBox" not in svg:
        errs.append(f"{name}: no viewBox")
    for m in re.finditer(r"<text\b[^>]*>(.*?)</text>", svg, re.S):
        if re.search(r"<(?!/?tspan\b)[a-zA-Z/]", m.group(1)):
            errs.append(f"{name}: HTML tag inside <text>: {m.group(1)[:60]!r}")
    return errs


# ------------------------------------------------------------------ rendering
def esc(s):
    return html.escape(s, quote=True)


def page(title, body, depth, extra_head=""):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="stylesheet" href="{up}assets/katex/katex.min.css">
<link rel="stylesheet" href="{up}assets/site.css">
<script defer src="{up}assets/katex/katex.min.js"></script>
<script defer src="{up}assets/katex/contrib/mhchem.min.js"></script>
<script defer src="{up}assets/katex/contrib/auto-render.min.js"></script>
<script defer src="{up}assets/site.js"></script>
{extra_head}</head><body>
{body}
</body></html>
"""


def place(text, figs, cls, figcount):
    """Put figures where the text says {{fig:N}}; any not placed go after the text."""
    rendered = [render_figs([f], cls, figcount) for f in figs]
    used = set()
    def sub(m):
        i = int(m.group(1)); used.add(i); return rendered[i]
    text = re.sub(r"\{\{fig:(\d+)\}\}", sub, text)
    return text + "".join(r for i, r in enumerate(rendered) if i not in used)


def render_figs(figs, cls, figcount):
    out = []
    for fn, cap in figs:
        svg = fn()
        figcount.append(fn.__name__)
        c = f"<figcaption>{cap}</figcaption>" if cap else ""
        m = re.search(r'viewBox="\s*[-\d.]+[ ,]+[-\d.]+[ ,]+([\d.]+)[ ,]+([\d.]+)', svg)
        wide = ""
        if m and float(m.group(1)) > 0 and float(m.group(2)) > 0:
            r = float(m.group(1)) / float(m.group(2))
            wide = " wide" if r > 2.0 else (" tall" if r < 0.9 else "")
        out.append(f'<figure class="{cls}{wide}" data-fig="{fn.__name__}">{svg}{c}</figure>')
    return "".join(out)


def slug(P):
    return P["slug"]


def render_paper(P, modname):
    figs_used = []
    subj = P["subject"]
    kept = [i for i in P["items"] if i["kind"] == "q" and not i["excluded"]]
    excl = [i for i in P["items"] if i["kind"] == "q" and i["excluded"]]
    key = f"pbrev-{subj}-{slug(P)}"
    parts = []
    parts.append(f"""<header class="top"><a class="crumb" href="../index.html">Pre-Board Revision</a> ›
<a class="crumb" href="index.html">{SUBJ_NAME[subj]}</a>
<h1>{SUBJ_NAME[subj]} · Pre-Board {esc(P['year'])}{' · Practical' if P.get('practical') else ''}</h1>
<p class="meta">{esc(P['paper'])} · Maximum marks {P.get('marks','')} · Time {esc(str(P.get('time','')))}</p>
<p class="meta">{len(kept)} questions in the ISC 2027 syllabus, answered below ·
{len(excl)} outside it (listed at the end, unanswered)</p>
<div class="tools"><button data-act="show">Show all answers</button>
<button data-act="hide">Hide all answers</button>
<span class="prog" data-key="{key}"></span></div></header>
<main data-key="{key}">""")
    if P.get("intro"):
        parts.append(f'<details class="intro"><summary>Instructions as printed</summary>{P["intro"]}</details>')
    # Headings wait until a kept question follows them.  Consecutive headings ("Part II",
    # then "Section A") are all shown; a heading whose questions were all excluded is dropped.
    pending = []          # [sec, had_question]
    for it in P["items"]:
        if it["kind"] == "sec":
            pending = [p for p in pending if not p[1]] + [[it, False]]
            continue
        for p in pending:
            p[1] = True
        if it["excluded"]:
            continue
        for sec, _ in pending:
            note = f'<p class="secnote">{sec["note"]}</p>' if sec["note"] else ""
            parts.append(f'<h2 class="sec">{sec["title"]}</h2>{note}')
        pending = []
        qid = "q" + re.sub(r"[^A-Za-z0-9]+", "-", it["num"]).strip("-")
        qtext = place(it["q"], it["qfig"], "qfig", figs_used)
        atext = place(it["a"], it["afig"], "afig", figs_used)
        recall = f'<aside class="recall"><h4>Concepts to recall</h4>{it["recall"]}</aside>' if it["recall"] else ""
        mk = f'<span class="marks">[{it["marks"]}]</span>' if it["marks"] else ""
        parts.append(f"""<article class="q" id="{qid}">
<div class="qhead"><span class="num">Q{esc(it['num'])}</span><span class="topic">{esc(it['topic'])}</span>{mk}
<label class="done"><input type="checkbox" data-id="{qid}"> revised</label></div>
<div class="qbody">{qtext}</div>
<button class="reveal" aria-expanded="false">Show answer</button>
<div class="ans" hidden><div class="anstext"><h4>Answer</h4>{atext}</div>{recall}</div>
</article>""")
    if excl:
        parts.append(f'<details class="excl"><summary>Not in the ISC 2027 syllabus ({len(excl)})</summary>')
        for it in excl:
            qtext = place(it["q"], it["qfig"], "qfig", figs_used)
            parts.append(f"""<div class="xq"><div class="qhead"><span class="num">Q{esc(it['num'])}</span>
<span class="marks">[{it['marks']}]</span></div><div class="qbody">{qtext}</div>
<p class="why">Why left out: {it['excluded']}</p></div>""")
        parts.append("</details>")
    parts.append("</main>")
    title = f"{SUBJ_NAME[subj]} Pre-Board {P['year']}" + (" Practical" if P.get("practical") else "")
    return page(title, "\n".join(parts), 1), figs_used


def load_papers():
    sys.path.insert(0, os.path.join(ROOT, "src"))
    sys.path.insert(0, os.path.join(ROOT, "src", "data"))
    sys.path.insert(0, os.path.join(ROOT, "src", "figs"))
    out = []
    for f in sorted(os.listdir(os.path.join(ROOT, "src", "data"))):
        if f.endswith(".py") and not f.startswith("_"):
            try:
                m = importlib.import_module(f[:-3])
                out.append((f[:-3], m.PAPER))
            except Exception as e:  # another paper being edited must not break this build
                print(f"  skip {f[:-3]}: {type(e).__name__}: {e}")
    return out
