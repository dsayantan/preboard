"""Render figures to PNG so they can be LOOKED AT.

    python3 src/preview.py <figs_module> [name_substring]     -> one PNG per fig_* function
    python3 src/preview.py --page physics/2013-14.html        -> full page, all answers open,
                                                                 split into 1400px-tall PNG slices

PNGs go to $PREVIEW_DIR (default /var/tmp/pbrev-preview/<module>/).  Open them with the Read tool.
"""
import os, sys, subprocess, importlib, tempfile, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, os.path.join(HERE, "figs"), os.path.join(HERE, "data")]
OUT = os.environ.get("PREVIEW_DIR", "/var/tmp/pbrev-preview")
CHROME = shutil.which("google-chrome") or "google-chrome"

def shot(html_path, png, w, h):
    prof = tempfile.mkdtemp(prefix="pbrevchrome")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={prof}",
                    f"--window-size={w},{h}", f"--screenshot={png}", "--virtual-time-budget=4000",
                    "file://" + html_path], capture_output=True, timeout=120)
    shutil.rmtree(prof, ignore_errors=True)

CSS = open(os.path.join(ROOT, "assets", "site.css")).read()

def figs(modname, sub=""):
    m = importlib.import_module(modname)
    d = os.path.join(OUT, modname); os.makedirs(d, exist_ok=True)
    for name in sorted(dir(m)):
        if not name.startswith("fig_") or sub not in name:
            continue
        svg = getattr(m, name)()
        p = os.path.join(d, name + ".html")
        open(p, "w").write(f"<!doctype html><meta charset=utf-8><style>{CSS} body{{margin:0;padding:12px;background:#fff}}"
                           f" figure{{margin:0;max-width:680px}} figure svg{{width:100%;height:auto}}</style>"
                           f"<p style='font:12px sans-serif;color:#666'>{name}</p><figure>{svg}</figure>")
        png = os.path.join(d, name + ".png")
        shot(p, png, 720, 720)
        print(png)

def full_page(rel):
    src = os.path.join(ROOT, rel)
    tmp = src.replace(".html", ".preview.html")
    # Long pages are captured in 4000px windows: each pass shifts the page up with a CSS
    # transform (layout is unchanged), until a window comes back empty.
    from PIL import Image, ImageChops
    d = os.path.join(OUT, rel.replace("/", "_").replace(".html", "")); os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if f.endswith(".png"): os.remove(os.path.join(d, f))
    CH, k = 4000, 0
    for part in range(60):
        shift = part * (CH - 300)   # 300px overlap so nothing is lost at a window edge
        s = open(src).read().replace("</body>", "<script>addEventListener('load',()=>setTimeout(()=>{"
            "document.querySelectorAll('.ans').forEach(a=>a.hidden=false);"
            "document.querySelectorAll('details').forEach(d=>d.open=true);"
            f"document.body.style.transform='translateY(-{shift}px)';document.querySelector('.tools')&&(document.querySelector('.tools').style.position='static')}},300))</script></body>")
        open(tmp, "w").write(s)
        big = os.path.join(d, f"part{part}.png")
        shot(tmp, big, 1100, CH)
        im = Image.open(big); W, H = im.size
        bg = Image.new(im.mode, im.size, im.getpixel((5, im.size[1] - 5)))
        bbox = ImageChops.difference(im, bg).getbbox()
        os.remove(big)
        if not bbox:
            break
        last = bbox[3] < H - 300         # a long blank band = end of page (card gaps are ~14px)
        H = bbox[3] + 20 if last else H
        for y in range(0, H, 1400):
            im.crop((0, y, W, min(H, y + 1400))).save(os.path.join(d, f"slice{k:02d}.png")); k += 1
        if last:
            break
    os.remove(tmp)
    print(f"{k} slices in {d}")

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--page":
        full_page(a[1])
    else:
        figs(a[0], a[1] if len(a) > 1 else "")
