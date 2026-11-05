"""JEE Main mock tests — data contract and checks.  See src/JEE-BRIEF.md.

    MCQ(src=(module, qnum), topic, q, options=[4], answer=0..3, sol, qfig=None, sfig=None)
    NUM(src=(module, qnum), topic, q, answer=int, sol, qfig=None, sfig=None)

Question modules live in src/jee/<subject>_t<N>.py and define SUBJECT, TEST, QUESTIONS.
"""
import os, sys, re, importlib
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "data"), os.path.join(HERE, "figs"), os.path.join(HERE, "jee")):
    if p not in sys.path:
        sys.path.insert(0, p)

SUBJECTS = [("physics", "Physics"), ("chemistry", "Chemistry"), ("maths", "Mathematics")]
N_MCQ, N_NUM = 20, 5
PLUS, MINUS = 4, -1
MINUTES = 180


def _figs(f):
    if f is None:
        return []
    if callable(f) or isinstance(f, tuple):
        f = [f]
    return [(x if isinstance(x, tuple) else (x, "")) for x in f]


def MCQ(src, topic, q, options, answer, sol, qfig=None, sfig=None):
    return dict(kind="mcq", src=tuple(src), topic=topic, q=q, options=list(options),
                answer=answer, sol=sol, qfig=_figs(qfig), sfig=_figs(sfig))


def NUM(src, topic, q, answer, sol, qfig=None, sfig=None):
    return dict(kind="num", src=tuple(src), topic=topic, q=q, options=[], answer=answer,
                sol=sol, qfig=_figs(qfig), sfig=_figs(sfig))


_paper_cache = {}


def source_item(mod, num):
    """The kit item for (module, printed number), or None."""
    if mod not in _paper_cache:
        try:
            _paper_cache[mod] = importlib.import_module(mod).PAPER
        except Exception:
            _paper_cache[mod] = None
    P = _paper_cache[mod]
    if not P:
        return None, None
    for it in P["items"]:
        if it["kind"] == "q" and it["num"] == str(num):
            return P, it
    return P, None


def anchor(P, num):
    """Link to the question on the site (same id rule as kit.render_paper)."""
    qid = "q" + re.sub(r"[^A-Za-z0-9]+", "-", str(num)).strip("-")
    return f"../{P['subject']}/{P['slug']}.html#{qid}"


def _plain(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def check(subject, test, Q):
    errs = []
    if len(Q) != N_MCQ + N_NUM:
        errs.append(f"{len(Q)} questions, want {N_MCQ + N_NUM}")
    kinds = [x["kind"] for x in Q]
    if kinds != ["mcq"] * N_MCQ + ["num"] * N_NUM:
        errs.append("order must be 20 MCQ then 5 NUM")
    seen = set()
    for i, x in enumerate(Q, 1):
        tag = f"{subject} T{test} #{i}"
        mod, num = x["src"]
        P, it = source_item(mod, num)
        if P is None:
            errs.append(f"{tag}: source module {mod} not found")
        elif it is None:
            errs.append(f"{tag}: {mod} has no question {num!r}")
        elif it["excluded"]:
            errs.append(f"{tag}: {mod} {num} is excluded (out of syllabus)")
        elif P["subject"] != subject:
            errs.append(f"{tag}: source {mod} is not a {subject} paper")
        if x["src"] in seen:
            errs.append(f"{tag}: source {x['src']} used twice in this test")
        seen.add(x["src"])
        if not x["topic"]:
            errs.append(f"{tag}: no topic")
        if not x["q"].strip() or not x["sol"].strip():
            errs.append(f"{tag}: empty question or solution")
        if x["kind"] == "mcq":
            if len(x["options"]) != 4:
                errs.append(f"{tag}: needs 4 options")
            elif len({_plain(o) for o in x["options"]}) != 4:
                errs.append(f"{tag}: options not distinct")
            if not (isinstance(x["answer"], int) and 0 <= x["answer"] < 4):
                errs.append(f"{tag}: answer must be an index 0-3")
        else:
            if not isinstance(x["answer"], int) or isinstance(x["answer"], bool):
                errs.append(f"{tag}: numerical answer must be an int")
        for txt in [x["q"], x["sol"]] + x["options"]:
            for d1, d2 in ((r"\(", r"\)"), (r"\[", r"\]")):
                if txt.count(d1) != txt.count(d2):
                    errs.append(f"{tag}: unbalanced {d1} {d2}")
    c = Counter(x["answer"] for x in Q if x["kind"] == "mcq")
    if c and max(c.values()) > 7:
        errs.append(f"{subject} T{test}: correct-answer letters unbalanced {dict(c)}")
    return errs


def load(subject, test):
    m = importlib.import_module(f"{subject}_t{test}")
    return m.QUESTIONS


def check_all():
    errs, texts = [], {}
    for s, _ in SUBJECTS:
        for t in (1, 2, 3):
            try:
                Q = load(s, t)
            except ModuleNotFoundError:
                continue
            errs += check(s, t, Q)
            for i, x in enumerate(Q, 1):
                k = _plain(x["q"])
                if k in texts:
                    errs.append(f"{s} T{t} #{i}: same question text as {texts[k]}")
                texts[k] = f"{s} T{t} #{i}"
    return errs


if __name__ == "__main__":
    e = check_all()
    print("\n".join(e) or "jee_kit: all checks pass")
    sys.exit(1 if e else 0)
