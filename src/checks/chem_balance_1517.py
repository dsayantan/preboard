"""Atom- and charge-balance checker for the \\ce{} equations in a data module
(used by chemistry_2015_16_check.py and chemistry_2016_17_check.py).

Every \\ce{...} containing a reaction arrow is parsed: reagents written above/below
the arrow (->[..][..]) are ignored, bond symbols (- = #) and precipitate/gas marks
(v, ^) are stripped, [O]/[H] count as O/H atoms.  An equation that is a scheme
(several arrows) or deliberately unbalanced is listed in SKIP with its reason.
"""
import re
from collections import Counter

ARROW = re.compile(r"(<=>|<->|->|<-)(\[[^\]]*\])?(\[[^\]]*\])?")


def _ce_blocks(text):
    out, i = [], 0
    while True:
        j = text.find(r"\ce{", i)
        if j < 0:
            return out
        k, depth = j + 4, 1
        while depth:
            depth += {"{": 1, "}": -1}.get(text[k], 0)
            k += 1
        out.append(text[j + 4:k - 1])
        i = k


def _atoms(s):
    """Atom counts and charge of one species string like 'C6H4(OK)COOK' or 'Mn^2+'."""
    s = s.strip()
    charge = 0
    m = re.search(r"\^\{?(\d*)([+-])\}?$", s)
    if m:
        charge = (int(m.group(1)) if m.group(1) else 1) * (1 if m.group(2) == "+" else -1)
        s = s[:m.start()]
    else:
        if len(s) > 1 and s[-1] in "+-":    # mhchem shorthand: H+, OH-, NH4+, Cl- (sign only)
            charge = 1 if s[-1] == "+" else -1
            s = s[:-1]
    charge += s.count("+")                  # an internal + (e.g. CH3CONH3+Cl-) is a cation charge
    s = s.replace("+", "")
    s = re.sub(r"[-=#]", "", s)
    s = s.replace("e", "") if s == "e" else s
    stack = [Counter()]
    i = 0
    while i < len(s):
        c = s[i]
        if c in "([":
            stack.append(Counter()); i += 1
        elif c in ")]":
            i += 1
            n = re.match(r"\d+", s[i:])
            k = int(n.group()) if n else 1
            if n:
                i += len(n.group())
            top = stack.pop()
            for a, v in top.items():
                stack[-1][a] += v * k
        elif c.isupper():
            m = re.match(r"([A-Z][a-z]?)(\d*)", s[i:])
            stack[-1][m.group(1)] += int(m.group(2) or 1)
            i += len(m.group())
        else:
            raise ValueError(f"cannot parse {s!r} at {s[i:]!r}")
    return stack[0], charge


def _side(side):
    tot, q = Counter(), 0
    side = re.sub(r"\(\s*(aq|s|l|g)\s*\)", "", side)
    for sp in re.split(r"\s\+\s", side):
        sp = sp.strip()
        sp = re.sub(r"\s+(v|\^)$", "", sp)
        if not sp:
            continue
        m = re.match(r"^(\d+)\s*", sp)
        k = int(m.group(1)) if m else 1
        sp = sp[m.end():] if m else sp
        if sp in ("e-", "e^-"):
            q -= k
            continue
        a, c = _atoms(sp)
        for x, v in a.items():
            tot[x] += v * k
        q += c * k
    return tot, q


def check_module(mod, skip=()):
    import itertools
    texts = []
    for it in mod.PAPER["items"]:
        if it["kind"] == "q" and not it["excluded"]:
            texts += [(it["num"], it["q"]), (it["num"], it["a"])]
    ok, bad, skipped = 0, [], []
    for num, t in texts:
        for ce in _ce_blocks(t):
            arrows = ARROW.findall(ce)
            if not arrows:
                continue
            parts = [x for i, x in enumerate(ARROW.split(ce)) if i % 4 == 0]
            if ce in skip or not parts[-1].strip():          # listed, or an unfinished prompt "A + B ->"
                skipped.append((num, ce)); continue
            if any(re.fullmatch(r"\s*\[?[A-F]\]?\s*", p_) for p_ in parts):   # lettered unknowns
                skipped.append((num, ce)); continue
            for lhs, rhs in zip(parts, parts[1:]):            # a chain is checked step by step
                try:
                    L, ql = _side(lhs); R, qr = _side(rhs)
                except Exception as e:
                    bad.append((num, ce, f"parse: {e}")); continue
                if L == R and ql == qr:
                    ok += 1
                else:
                    diff = {k: L[k] - R[k] for k in set(L) | set(R) if L[k] != R[k]}
                    bad.append((num, f"{lhs}->{rhs}", f"atoms L-R {diff}, charge {ql} vs {qr}"))
    return ok, bad, skipped
