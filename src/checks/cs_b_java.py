"""Run every Java answer of a CS module with the JDK 11 single-file launcher,
record input/output under java/<module>/<name>.in/.out, and assert expected text.
Used by computers_2015_16_*_check.py and computers_2016_17_*_check.py."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))


def run(module, cases):
    d = os.path.join(HERE, "java", module)
    bad = 0
    for name, fname, stdin, expect in cases:
        r = subprocess.run(["java", fname], cwd=d, input=stdin, capture_output=True,
                           text=True, timeout=120)
        out = r.stdout
        ok = r.returncode == 0 and not r.stderr.strip()
        miss = [e for e in expect if e not in out]
        if miss or not ok:
            bad += 1
            print("FAIL %s/%s rc=%s stderr=%r missing=%r\n%s" % (module, name, r.returncode,
                  r.stderr[:300], miss, out))
        else:
            print("ok   %s/%s" % (module, name))
        open(os.path.join(d, name + ".in"), "w").write(stdin)
        open(os.path.join(d, name + ".out"), "w").write(out)
    return bad


def truth(n, f):
    """All 2^n rows of f as a set of row indices where f is 1 (MSB first)."""
    on = set()
    for v in range(2 ** n):
        bits = [(v >> (n - 1 - i)) & 1 for i in range(n)]
        if f(*bits):
            on.add(v)
    return on
