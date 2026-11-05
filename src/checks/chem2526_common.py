"""Shared helpers for the 2025-26 Chemistry checks: approx compare and an atom/charge balancer."""
import re
from collections import Counter

FAIL = []


def near(name, got, want, rel=0.01):
    ok = abs(got - want) <= rel * abs(want)
    print(f"{'ok ' if ok else 'BAD'} {name}: computed {got:.6g}, printed {want:.6g}")
    if not ok:
        FAIL.append(name)


def atoms(f):
    """Charges: write '^2-' (or a bare trailing + / - for 1). Count atoms in a formula like 'K2Cr2O7', 'Cr2(SO4)3', '[Ag(NH3)2]+', 'CuSO4.5H2O'."""
    f = f.split("^")[0] if "^" in f else re.sub(r"[+-]$", "", f)
    if f == "e":
        return Counter()
    def parse(s, i=0):
        c = Counter()
        while i < len(s):
            ch = s[i]
            if ch in "([":
                sub, i = parse(s, i + 1)
                m = re.match(r"\d+", s[i:]); n = int(m.group()) if m else 1
                i += len(m.group()) if m else 0
                for k, v in sub.items(): c[k] += v * n
            elif ch in ")]":
                return c, i + 1
            else:
                m = re.match(r"([A-Z][a-z]?)(\d*)", s[i:])
                c[m.group(1)] += int(m.group(2) or 1); i += len(m.group())
        return c, i
    return parse(f)[0]


def charge(f):
    m = re.search(r"\^(\d*)([+-])$", f) or re.search(r"()([+-])$", f)
    if not m:
        return 0
    n = int(m.group(1) or 1)
    return n if m.group(2) == "+" else -n


def side(s):
    c, q = Counter(), 0
    for term in s.split(" + "):
        term = term.strip()
        m = re.match(r"^(\d+)\s*(.*)$", term)
        n, f = (int(m.group(1)), m.group(2)) if m else (1, term)
        for k, v in atoms(f).items(): c[k] += n * v
        q += n * charge(f)
    return c, q


def balanced(name, eq):
    l, r = eq.split("->")
    (a, qa), (b, qb) = side(l), side(r)
    ok = (a == b and qa == qb)
    print(f"{'ok ' if ok else 'BAD'} balance {name}: {eq}" + ("" if ok else f"   L={dict(a)} q{qa} R={dict(b)} q{qb}"))
    if not ok:
        FAIL.append(name)


def done():
    print("FAILED:" if FAIL else "all checks pass", FAIL if FAIL else "")
    raise SystemExit(1 if FAIL else 0)
