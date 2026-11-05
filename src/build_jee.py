"""Build the JEE Main-style mock tests.   python3 src/build_jee.py

Writes jee/test-1.html … jee/test-3.html and jee/index.html (see src/JEE-BRIEF.md).
A test is built only when all three of its subject modules (src/jee/<subject>_t<N>.py) exist and
jee_kit.check passes for each; otherwise jee/index.html lists it as "coming soon" and any stale
jee/test-N.html is removed.  Exits non-zero on any check error (or a module that fails to import).

Environment (development only):
    JEE_SRC_DIR   read the question modules from here instead of src/jee
    JEE_OUT_DIR   write the pages here instead of <site>/jee (it must sit beside an assets/ dir,
                  e.g. a scratch site whose assets/ and subject dirs are symlinks)

The test page is static: every question, option, figure and solution is in the HTML (solutions
hidden until the candidate submits); assets/jee.js runs the test, assets/jee.css styles it.
Afterwards refresh the landing page card with   python3 src/build.py   (or build_index alone).
"""
import os, sys, re, json, base64, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
import jee_kit

SRC_DIR = os.path.abspath(os.environ.get("JEE_SRC_DIR") or os.path.join(HERE, "jee"))
OUT_DIR = os.path.abspath(os.environ.get("JEE_OUT_DIR") or os.path.join(kit.ROOT, "jee"))
if SRC_DIR in sys.path:
    sys.path.remove(SRC_DIR)
sys.path.insert(0, SRC_DIR)

TESTS = (1, 2, 3)
LABELS = ["(1)", "(2)", "(3)", "(4)"]          # NTA numbers its options
esc = kit.esc
EXTRA_HEAD = '<link rel="stylesheet" href="../assets/jee.css">\n<script defer src="../assets/jee.js"></script>\n'


def source_label(P, num):
    name = kit.SUBJ_NAME[P["subject"]]
    prac = " (practical)" if P.get("practical") else ""
    return f"{name} pre-board {P['year']} {P['paper']}{prac} Q{num}"


# ------------------------------------------------------------------ loading + checks
def load_test(t):
    """-> (status, {subject: QUESTIONS}, errors); status in ready | missing | error."""
    missing = [s for s, _ in jee_kit.SUBJECTS if not os.path.exists(os.path.join(SRC_DIR, f"{s}_t{t}.py"))]
    if missing:
        return "missing", {}, [f"test {t}: no module for {', '.join(missing)}"]
    data, errs = {}, []
    for s, _ in jee_kit.SUBJECTS:
        modname = f"{s}_t{t}"
        try:
            sys.modules.pop(modname, None)
            m = importlib.import_module(modname)
        except Exception as e:
            errs.append(f"{modname}: import failed: {type(e).__name__}: {e}")
            continue
        if getattr(m, "SUBJECT", s) != s or getattr(m, "TEST", t) != t:
            errs.append(f"{modname}: SUBJECT/TEST say {getattr(m, 'SUBJECT', None)!r}/{getattr(m, 'TEST', None)!r}")
        Q = getattr(m, "QUESTIONS", None)
        if not isinstance(Q, list):
            errs.append(f"{modname}: no QUESTIONS list")
            continue
        errs += jee_kit.check(s, t, Q)
        errs += answer_label_errors(s, t, Q)
        data[s] = Q
    return ("error" if errs else "ready"), data, errs


def cross_test_errors(loaded):
    """No question text identical across tests (jee_kit.check_all's rule, over what was loaded)."""
    errs, texts = [], {}
    for t, data in loaded.items():
        for s, Q in data.items():
            for i, x in enumerate(Q, 1):
                k = jee_kit._plain(x["q"])
                if k in texts and texts[k][0] != (s, t, i):
                    errs.append(f"{s} T{t} #{i}: same question text as {texts[k][1]}")
                texts.setdefault(k, ((s, t, i), f"{s} T{t} #{i}"))
    return errs


def answer_label_errors(subject, t, Q):
    """A solution that names its answer as "Answer: (k)" / "Answer: (X)" must name the keyed option."""
    errs = []
    for i, x in enumerate(Q, 1):
        if x["kind"] != "mcq":
            continue
        for m in re.finditer(r"Answer\W{0,12}\(([1-4A-D])\)", re.sub(r"<[^>]+>", "", x["sol"])):
            k = "1234".find(m.group(1)) if m.group(1).isdigit() else "ABCD".find(m.group(1))
            if k != x["answer"]:
                errs.append(f"{subject} T{t} #{i}: solution says Answer ({m.group(1)}) but answer={x['answer']} "
                            f"is option {LABELS[x['answer']]}")
    return errs


def svg_errors(html, figs):
    errs = []
    for fn, _ in figs:
        errs += kit.svg_problems(fn(), fn.__name__)
    ids = {}
    for m in re.finditer(r"<svg.*?</svg>", html, re.S):
        for i in re.findall(r'\bid="([^"]+)"', m.group(0)):
            ids.setdefault(i, set()).add(m.start())
    dup = sorted(i for i, s in ids.items() if len(s) > 1)
    if dup:
        errs.append(f"SVG ids reused across figures on one page (a figure used twice?): {dup[:8]}")
    return errs


# ------------------------------------------------------------------ rendering
def _visual_len(o):
    """Rough rendered width of an option, in characters: tags and TeX commands stripped;
    a matrix or a stacked fraction counts as its widest row / part."""
    t = re.sub(r"<[^>]+>", "", o)
    t = re.sub(r"\\[()\[\]]", "", t)
    t = re.sub(r"\\(begin|end)\{[a-z]*matrix\*?\}", "", t)
    rows = re.split(r"\\\\", t)                       # matrix rows
    t = max(rows, key=len)
    t = re.sub(r"\\(?:d?frac|tfrac)\{([^{}]*)\}\{([^{}]*)\}",
               lambda m: max(m.group(1), m.group(2), key=len), t)
    t = re.sub(r"\\[A-Za-z]+", "x", t)                  # \alpha, \sqrt ... ~ one glyph
    t = re.sub(r"[{}&^_ ]", "", t)
    return len(t)


def options_compact(options):
    """Lay the four options out 2 x 2 when all are short or are matrices (tall but narrow);
    long text options stay one per line."""
    if any(re.search(r"<(table|figure|svg|p|br|div)\b", o) for o in options):
        return 0
    w = max(_visual_len(o) for o in options)
    return 2 if w <= 12 else 1 if w <= 22 else 0


def render_question(n, si, x, figcount):
    """n = 1-based number through the paper, si = subject index."""
    sec = "A" if x["kind"] == "mcq" else "B"
    sname = jee_kit.SUBJECTS[si][1]
    qtext = kit.place(x["q"], x["qfig"], "qfig", figcount)
    stext = kit.place(x["sol"], x["sfig"], "afig", figcount)
    mod, num = x["src"]
    P, _ = jee_kit.source_item(mod, num)
    src = (f'<p class="jsrc">Source: <a href="{esc(jee_kit.anchor(P, num))}">{esc(source_label(P, num))} →</a></p>'
           if P else "")
    if x["kind"] == "mcq":
        opts = "".join(
            f'<label class="jopt" data-o="{k}"><input type="radio" name="jr{n}" value="{k}">'
            f'<span class="jol">{LABELS[k]}</span><span class="jot">{o}</span></label>'
            for k, o in enumerate(x["options"]))
        c = options_compact(x["options"])          # 0 stacked, 1 2x2 on wide screens, 2 2x2 on phones too
        grid = ["", " grid2", " grid2 g2s"][c]
        resp = f'<div class="jopts{grid}" role="radiogroup" aria-label="Options">{opts}</div>'
    else:
        keys = "".join(f'<button type="button" data-k="{k}">{"−" if k == "-" else ("⌫" if k == "bs" else k)}</button>'
                       for k in ["7", "8", "9", "4", "5", "6", "1", "2", "3", "-", "0", "bs"])
        resp = (f'<div class="jnum"><label>Your answer (an integer): '
                f'<input type="text" class="jin" inputmode="numeric" autocomplete="off" spellcheck="false" '
                f'maxlength="12" aria-label="Integer answer to question {n}"></label>'
                f'<div class="jkeys" aria-label="Keypad">{keys}</div>'
                f'<p class="jerr" hidden>Enter a whole number, e.g. 12 or −3. Decimals and fractions are not accepted.</p></div>')
    return f"""<article class="jq" id="jq{n}" data-i="{n - 1}" data-s="{si}" data-sec="{sec}" data-k="{'m' if sec == 'A' else 'n'}" hidden>
<div class="jqhead"><span class="jqn">Question {n}</span><span class="jqmeta">{sname} · Section {sec} · {'Multiple choice' if sec == 'A' else 'Numerical (integer)'} · +4 / −1</span>
<span class="jtopic">{esc(x['topic'])}</span></div>
<div class="jqbody">{qtext}</div>
{resp}
<div class="jrev" hidden></div>
<div class="jsol" hidden><h4>Solution</h4>{stext}{src}</div>
</article>"""


def instructions(t):
    return f"""<h2>Instructions</h2>
<ol class="jinst">
<li><b>75 questions, 300 marks, 180 minutes.</b> Three subjects in order — Physics (Q1–25), Chemistry
(Q26–50), Mathematics (Q51–75).</li>
<li>Each subject has <b>Section A</b>: 20 multiple-choice questions, four options, exactly one correct; and
<b>Section B</b>: 5 numerical-value questions whose answer is an <b>integer</b> (it may be negative) that you type in.
All 75 are compulsory to attempt for full marks.</li>
<li><b>Marking, both sections: +4</b> for a correct answer, <b>−1</b> for a wrong one, <b>0</b> if not answered.</li>
<li>The clock starts when you press <em>Start test</em> and keeps running even if you close the page.
Come back and the test resumes where you left it. When time runs out the test is submitted automatically.</li>
<li>A response counts only after you press <em>Save &amp; Next</em> or <em>Mark for Review &amp; Next</em>.
Choosing an option and moving away with <em>Back</em>, the palette or a subject tab does not save it.</li>
<li><em>Clear Response</em> removes the saved answer to the question on screen. <em>Mark for Review &amp; Next</em>
flags it to come back to; a question that is <b>answered and marked for review is evaluated</b>; one marked without
an answer is not.</li>
</ol>
<h3>Question palette</h3>
<ul class="jlegend jlegend-big">
<li><span class="jp s0"><span>1</span></span> Not visited</li>
<li><span class="jp s1"><span>2</span></span> Not answered</li>
<li><span class="jp s2"><span>3</span></span> Answered</li>
<li><span class="jp s3"><span>4</span></span> Marked for review (not evaluated)</li>
<li><span class="jp s4"><span>5</span></span> Answered &amp; marked for review (evaluated)</li>
</ul>
<p class="jnote">Answers are kept in this browser only. After submitting you get your score, every question with
the correct answer and a worked solution, and a link to the pre-board question it was built on.</p>"""


def render_test(t, data):
    figcount = []
    qs, n = [], 0
    key = []
    pal = []
    for si, (s, sname) in enumerate(jee_kit.SUBJECTS):
        qs.append(f'<h2 class="jsubh" data-s="{si}" hidden>{sname}</h2>')
        btns_a, btns_b = [], []
        for x in data[s]:
            n += 1
            qs.append(render_question(n, si, x, figcount))
            key.append(dict(s=si, k="m" if x["kind"] == "mcq" else "n", a=x["answer"]))
            b = f'<button type="button" class="jp s0" data-i="{n - 1}" aria-label="Question {n}"><span>{n}</span></button>'
            (btns_a if x["kind"] == "mcq" else btns_b).append(b)
        pal.append(f'<div class="jpgrid" data-s="{si}" hidden><h4>{sname} · Section A</h4><div class="jpg">{"".join(btns_a)}</div>'
                   f'<h4>Section B</h4><div class="jpg">{"".join(btns_b)}</div></div>')
    tabs = "".join(f'<button type="button" role="tab" data-s="{si}">{nm}</button>'
                   for si, (_, nm) in enumerate(jee_kit.SUBJECTS))
    blob = base64.b64encode(json.dumps(key, separators=(",", ":")).encode()).decode()
    title = f"JEE Main Mock Test {t}"
    body = f"""<div class="jee" data-test="{t}" data-key="pbrev-jee-test-{t}" data-minutes="{jee_kit.MINUTES}">
<header class="jtop">
<div class="jname"><a class="crumb" href="index.html">JEE mocks</a><b>{title}</b></div>
<div class="jclock" id="jclock" title="Time left">{jee_kit.MINUTES // 60}:00:00</div>
<button type="button" class="jsubmit" id="jsubmit" hidden>Submit</button>
</header>
<noscript><p class="jnote">This test needs JavaScript.</p></noscript>
<section class="jgate" id="jgate">
<h1>{title}</h1>
<p class="meta">JEE Main pattern · Physics, Chemistry, Mathematics · 75 questions · 300 marks · 3 hours.
Every question is adapted from a Heritage School pre-board question on this site.</p>
{instructions(t)}
<label class="jagree"><input type="checkbox" id="jagree"> I have read the instructions.</label>
<button type="button" class="jstart" id="jstart" disabled>Start test</button>
</section>
<section class="jexam" id="jexam" hidden>
<nav class="jtabs" role="tablist" aria-label="Subjects">{tabs}</nav>
<div class="jsecs"><button type="button" data-sec="A">Section A · MCQ</button><button type="button" data-sec="B">Section B · Numerical</button></div>
<div class="jlayout">
<div class="jmain">
<div class="jqs" id="jqs">
{''.join(qs)}
</div>
<div class="jactions">
<button type="button" class="jb-save" data-act="save">Save &amp; Next</button>
<button type="button" class="jb-clear" data-act="clear">Clear Response</button>
<button type="button" class="jb-mark" data-act="mark">Mark for Review &amp; Next</button>
<button type="button" class="jb-back" data-act="back">Back</button>
</div>
</div>
<aside class="jpal" aria-label="Question palette">
<ul class="jlegend" id="jlegend">
<li><span class="jp s0"><span data-c="0">0</span></span> Not visited</li>
<li><span class="jp s1"><span data-c="1">0</span></span> Not answered</li>
<li><span class="jp s2"><span data-c="2">0</span></span> Answered</li>
<li><span class="jp s3"><span data-c="3">0</span></span> Marked for review</li>
<li class="jwide"><span class="jp s4"><span data-c="4">0</span></span> Answered &amp; marked for review (will be evaluated)</li>
</ul>
{''.join(pal)}
</aside>
</div>
</section>
<section class="jresult" id="jresult" hidden>
<div id="jsummary"></div>
<div class="jfilter" id="jfilter"><span>Show:</span>
<button type="button" data-f="all" class="on">All</button><button type="button" data-f="right">Correct</button>
<button type="button" data-f="wrong">Incorrect</button><button type="button" data-f="skip">Unattempted</button></div>
<div id="jrevslot"></div>
<div class="jretake"><button type="button" id="jretake">Retake (clears answers)</button>
<div class="jconfirm" id="jretakeconf" hidden><p>Clear every answer and the score, and start this test again from the instructions?</p>
<button type="button" class="jdanger" id="jretakeyes">Yes, clear and retake</button> <button type="button" id="jretakeno">Cancel</button></div></div>
</section>
<div class="jmodal" id="jmodal" hidden role="dialog" aria-modal="true" aria-labelledby="jmodalh"><div class="jmodalbox">
<h2 id="jmodalh">Submit the test?</h2><div id="jmodalcounts"></div>
<p>Once submitted you cannot change any answer.</p>
<button type="button" class="jdanger" id="jmodalyes">Yes, submit</button> <button type="button" id="jmodalno">No, go back</button>
</div></div>
<script type="application/octet-stream" id="jee-key">{blob}</script>
</div>"""
    return kit.page(f"{title} · Pre-Board Revision", body, 1, EXTRA_HEAD), figcount


def render_index(status):
    rows = []
    for t in TESTS:
        if status[t] == "ready":
            rows.append(f'<li class="jtest" data-test="{t}"><a href="test-{t}.html">JEE Main Mock Test {t}</a>'
                        f'<span class="cnt">75 questions · 300 marks · 3 hours</span>'
                        f'<span class="jstat" data-key="pbrev-jee-test-{t}">Not started</span></li>')
        else:
            rows.append(f'<li class="jtest soon"><span class="jsoonname">JEE Main Mock Test {t}</span>'
                        f'<span class="cnt">Coming soon</span></li>')
    body = f"""<header class="top"><a class="crumb" href="../index.html">Pre-Board Revision</a>
<h1>JEE Main mock tests</h1>
<p class="meta">Three full-length computer-based tests in the JEE Main pattern, every question adapted from a
Heritage School pre-board question on this site — sit one against the clock, then read the worked solutions.</p></header>
<main class="jindex">
<h2 class="sec">Tests</h2>
<ul class="papers">{''.join(rows)}</ul>
<h2 class="sec">The pattern</h2>
<div class="tbl"><table>
<tr><th>Subject</th><th>Questions</th><th>Section A (MCQ)</th><th>Section B (integer)</th><th>Marks</th></tr>
<tr><td>Physics</td><td>1–25</td><td>20</td><td>5</td><td>100</td></tr>
<tr><td>Chemistry</td><td>26–50</td><td>20</td><td>5</td><td>100</td></tr>
<tr><td>Mathematics</td><td>51–75</td><td>20</td><td>5</td><td>100</td></tr>
<tr><th>Total</th><th>75</th><th>60</th><th>15</th><th>300</th></tr></table></div>
<p>Time allowed: <b>3 hours (180 minutes)</b>. Section A questions have four options with exactly one correct;
Section B answers are integers (possibly negative) typed in, with any rounding stated in the question.</p>
<h2 class="sec">How scoring works</h2>
<ul>
<li><b>+4</b> for each correct answer, <b>−1</b> for each wrong answer, <b>0</b> for a question not answered — in
<em>both</em> sections, as in the current NTA pattern.</li>
<li>Only saved responses count. A question <em>answered and marked for review</em> is evaluated; one
<em>marked for review</em> without an answer is not.</li>
<li>The clock keeps running if you leave the page; reopening the test resumes it. At zero the test submits itself.</li>
<li>Your answers and score stay in this browser. <em>Retake</em> on the result page clears them.</li>
</ul>
</main>"""
    return kit.page("JEE Main mock tests · Pre-Board Revision", body, 1, EXTRA_HEAD)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    status, loaded, bad = {}, {}, False
    for t in TESTS:
        st, data, errs = load_test(t)
        status[t] = st
        if st == "missing":
            print(f"  test {t}: coming soon ({errs[0].split(': ', 1)[1]})")
        elif errs:
            bad = True
            for e in errs:
                print(f"  ERROR {e}")
        if data:
            loaded[t] = data
    for e in cross_test_errors(loaded):
        bad = True
        print(f"  ERROR {e}")
        t = int(re.search(r" T(\d) ", e).group(1))
        status[t] = "error"
    for t in TESTS:
        out = os.path.join(OUT_DIR, f"test-{t}.html")
        if status[t] == "ready":
            html, figs = render_test(t, loaded[t])
            allfigs = [f for s in loaded[t].values() for x in s for f in x["qfig"] + x["sfig"]]
            errs = svg_errors(html, allfigs)
            if errs:
                bad = True
                status[t] = "error"
                for e in errs:
                    print(f"  ERROR test {t}: {e}")
            else:
                open(out, "w").write(html)
                print(f"built {os.path.relpath(out, kit.ROOT) if out.startswith(kit.ROOT) else out}  75 questions, figures {len(figs)}")
                continue
        if os.path.exists(out):
            os.remove(out)
            print(f"  removed stale {out}")
    open(os.path.join(OUT_DIR, "index.html"), "w").write(render_index(status))
    print(f"built {os.path.join(OUT_DIR, 'index.html')}  ready: {[t for t in TESTS if status[t] == 'ready']}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
