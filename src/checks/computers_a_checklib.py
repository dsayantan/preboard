"""Shared checks for computers_2013_14_p1 and computers_2014_15_p1 (agent A)."""
import os, re, subprocess, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
CS = os.path.normpath(os.path.join(SRC, "..", "..", "Computers", "src"))
for p in (SRC, os.path.join(SRC, "data"), os.path.join(SRC, "figs"), CS):
    if p not in sys.path:
        sys.path.insert(0, p)
import kmapsolve as K          # noqa: E402
import _computers_a_util as U  # noqa: E402
import computers_a_lib as L    # noqa: E402

FAILS = []
N = [0]


def ok(cond, what):
    N[0] += 1
    if not cond:
        FAILS.append(what)
        print("FAIL:", what)


def rows(n):
    return [tuple((k >> (n - 1 - i)) & 1 for i in range(n)) for k in range(2 ** n)]


def on_set(expr, names):
    return K.evaluate(expr, len(names), names)


def equiv(e1, e2, names, what):
    ok(on_set(e1, names) == on_set(e2, names), what + ": %s == %s" % (e1, e2))


def kmap_check(kind, cells, names, groups, terms, stated, what):
    """K-map: kmapsolve's minimum has the same number of terms as ours; our
    expression has exactly the required on-set; each drawn group is exactly the
    cell set of one term; the drawn circuit (netlist) computes the function."""
    n = len(names)
    expr, rws = K.solve(kind, n, cells, names)
    want = set(cells) if kind == "sop" else set(range(2 ** n)) - set(cells)
    ok(on_set(stated, names) == want, what + ": stated %s has the right truth table" % stated)
    ok(len(rws) == len(terms), what + ": minimal term count %d (kmapsolve %s)" % (len(terms), expr))
    lits = sum(len(L.parse_term(t)) for t in terms)
    klits = sum(len(L.parse_term(t)) for t, _, _ in rws)
    ok(lits == klits, what + ": literal count %d == minimal %d" % (lits, klits))
    for g, t in zip(groups, terms):
        tt = L.parse_term(t)
        cov = set()
        for v in range(2 ** n):
            env = {nm: (v >> (n - 1 - i)) & 1 for i, nm in enumerate(names)}
            bits = [env[x] ^ neg for x, neg in tt]
            if kind == "sop" and all(bits):
                cov.add(v)
            if kind == "pos" and not any(bits):
                cov.add(v)
        ok(cov == set(g), what + ": group %s is term %s (covers %s)" % (g, t, sorted(cov)))
    covered = set().union(*map(set, groups))
    ok(covered == set(cells), what + ": groups cover every %s" % ("1" if kind == "sop" else "0"))
    circuit_check(terms, kind, None, names, want, what + " circuit")


def circuit_check(terms, kind, uni, names, want, what):
    got = set()
    n = len(names)
    for v in range(2 ** n):
        env = {nm: (v >> (n - 1 - i)) & 1 for i, nm in enumerate(names)}
        if L.two_level_eval(terms, kind, uni, env):
            got.add(v)
    ok(got == set(want), what + ": netlist output matches over all %d rows" % 2 ** n)


def traversals(t):
    def pre(t): return [] if t is None else [t[0]] + pre(t[1]) + pre(t[2])
    def ino(t): return [] if t is None else ino(t[1]) + [t[0]] + ino(t[2])
    def post(t): return [] if t is None else post(t[1]) + post(t[2]) + [t[0]]
    return " ".join(pre(t)), " ".join(ino(t)), " ".join(post(t))


def run_java(mod):
    d = os.path.join(U.JAVA, mod)
    files = sorted(f for f in os.listdir(d) if f.endswith(".java"))
    for f in files:
        ok((mod, f) in U.RUNS, "%s/%s has an expected run" % (mod, f))
        for stdin, expect in U.RUNS.get((mod, f), []):
            r = subprocess.run(["java", f], cwd=d, input=stdin, capture_output=True, text=True, timeout=120)
            ok(r.returncode == 0, "%s compiles and runs (%s)" % (f, r.stderr.strip()[:200]))
            ok(r.stdout == expect, "%s output as shown on the page\n--- got ---\n%s--- want ---\n%s" % (f, r.stdout, expect))
    print("ran %d Java programs in %s" % (len(files), mod))


def in_page(P, num, *needles):
    it = [i for i in P["items"] if i["kind"] == "q" and i["num"] == num][0]
    txt = it["a"]
    for s in needles:
        ok(s in txt, "Q%s answer text contains %r" % (num, s))


def done(name):
    print("%s: %d checks, %d failed" % (name, N[0], len(FAILS)))
    sys.exit(1 if FAILS else 0)
