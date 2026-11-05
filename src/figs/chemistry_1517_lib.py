"""Shared drawing helpers for the Chemistry 2015-16 and 2016-17 figure modules.

Not a figure module itself (no fig_* functions).  Everything draws onto a svg.Fig.
"""
from svg import Fig

INK, ACC, WARM, MUTED, LIG = "#111", "#0d6e6e", "#b5651d", "#777", "#1f4fa8"


def spin_box(f, x, y, fill, w=22, h=20, color=INK):
    """One orbital box. fill: '' empty, 'u' one electron, 'ud' a pair,
    'L' a ligand electron pair (drawn as a pair of crosses in the ligand colour)."""
    f.rect(x, y, w, h, color=MUTED, w=1.1)
    if fill in ("u", "ud"):
        xa = x + (w * 0.33 if fill == "ud" else w * 0.5)
        f.line(xa, y + h - 3, xa, y + 4, color=color, w=1.4)
        f.path(f"M {xa} {y+4} l 3.2 4.4", color=color, w=1.4)
        if fill == "ud":
            xb = x + w * 0.67
            f.line(xb, y + 4, xb, y + h - 3, color=color, w=1.4)
            f.path(f"M {xb} {y+h-3} l -3.2 -4.4", color=color, w=1.4)
    elif fill == "L":
        for xc in (x + w * 0.32, x + w * 0.68):
            f.text(xc, y + h * 0.72, "x", size=12, color=LIG, bold=True)


def box_row(f, x, y, fills, w=22, h=20, gap=0, color=INK):
    for k, fl in enumerate(fills):
        spin_box(f, x + k * (w + gap), y, fl, w, h, color)
    return x + len(fills) * (w + gap)


def level(f, x, y, n, fills, w=26, gap=8, color=INK):
    """n degenerate orbitals drawn as short horizontal lines with electrons above."""
    for k in range(n):
        x0 = x + k * (w + gap)
        f.line(x0, y, x0 + w, y, color=INK, w=2)
        fl = fills[k] if k < len(fills) else ""
        if fl in ("u", "ud"):
            xa = x0 + (w * 0.35 if fl == "ud" else w * 0.5)
            f.line(xa, y - 3, xa, y - 18, color=color, w=1.4)
            f.path(f"M {xa} {y-18} l 3.2 4.4", color=color, w=1.4)
            if fl == "ud":
                xb = x0 + w * 0.65
                f.line(xb, y - 18, xb, y - 3, color=color, w=1.4)
                f.path(f"M {xb} {y-3} l -3.2 -4.4", color=color, w=1.4)
    return x + n * (w + gap) - gap


def chem(f, x, y, parts, size=14, anchor="middle", color=INK, bold=False):
    """Text with subscripts/superscripts: parts is a list of (text, kind) where kind is
    '' normal, 'b' subscript, 'p' superscript.  Emits <tspan>s (no HTML in <text>)."""
    from html import escape
    st = ' font-weight="bold"' if bold else ""
    out = []
    for s, kind in parts:
        s = escape(s)
        if kind == "b":
            out.append(f'<tspan baseline-shift="sub" font-size="{size*0.72:.1f}">{s}</tspan>')
        elif kind == "p":
            out.append(f'<tspan baseline-shift="super" font-size="{size*0.72:.1f}">{s}</tspan>')
        else:
            out.append(f"<tspan>{s}</tspan>")
    f.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
          f'font-family="Times New Roman,serif"{st}>{"".join(out)}</text>')


def F(s):
    """Parse a compact formula string into chem() parts: digits after a letter or ')'
    become subscripts; text after '^' up to a space becomes a superscript.
    e.g. F('CH3COOH'), F('[Co(en)2Cl2]^+')."""
    parts, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "^":
            j = i + 1
            while j < len(s) and s[j] != " ":
                j += 1
            parts.append((s[i + 1:j], "p")); i = j; continue
        if c.isdigit() and i > 0 and (s[i - 1].isalpha() or s[i - 1] in ")]"):
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            parts.append((s[i:j], "b")); i = j; continue
        parts.append((c, "")); i += 1
    # merge adjacent normal runs
    out = []
    for p in parts:
        if out and out[-1][1] == p[1] == "":
            out[-1] = (out[-1][0] + p[0], "")
        else:
            out.append(p)
    return out
