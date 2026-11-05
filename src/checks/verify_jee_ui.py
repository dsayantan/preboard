"""Drive the JEE mock-test pages in headless Chrome and check they behave like the NTA CBT.

    python3 src/checks/verify_jee_ui.py [--test N] [--site DIR] [--shots DIR]

--site   the site root to serve (default: the repo).  During development point it at a scratch
         site built with JEE_OUT_DIR (see src/build_jee.py).
--test   which built test to sit (default: every jee/test-N.html present).
--shots  where screenshots go (default /var/tmp/pbrev-jee-shots).  LOOK at them.

What is checked, per test: the instructions gate; starting the clock; Save & Next, Mark for
Review & Next, Clear Response, Back, palette and tab/section navigation and the status each one
leaves (palette classes and legend counts); integer input (negative accepted, "2.5" rejected,
keypad); reload resumes the same question with the clock read from the stored deadline; the
in-page submit dialog and its counts; the score against an independent +4/-1 computation, per
subject and in total; the review (every question shown with response, correct answer, marks,
solution and a source link whose target file and anchor exist); retake; expiry auto-submit both
while open and on load; jee/index.html; no request leaves the local server; no horizontal
overflow at 400 px; screenshots at 1280 and 400 px.

Chrome is driven over CDP: a free port, --remote-allow-origins=*, websocket-client with
suppress_origin=True, and no_proxy for 127.0.0.1.  The site is served over http from a
throwaway local server, and each run uses a fresh profile.
"""
import os, sys, json, time, base64, socket, shutil, tempfile, subprocess, threading, re, argparse, functools
import http.server
import urllib.request
import websocket

os.environ["no_proxy"] = os.environ["NO_PROXY"] = "127.0.0.1,localhost"
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROME = shutil.which("google-chrome") or "google-chrome"

FAILS, PASSES = [], [0]


def ok(cond, msg):
    if cond:
        PASSES[0] += 1
    else:
        FAILS.append(msg)
        print("  FAIL", msg)
    return cond


def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve(site):
    port = free_port()
    h = functools.partial(Quiet, directory=site)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", port), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, port


class Chrome:
    def __init__(self, url):
        self.port = free_port()
        self.prof = tempfile.mkdtemp(prefix="pbrevjee")
        self.p = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                                   "--no-default-browser-check", f"--remote-debugging-port={self.port}",
                                   "--remote-allow-origins=*", f"--user-data-dir={self.prof}",
                                   "--window-size=1280,900", url],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        tgt = None
        for _ in range(100):
            try:
                L = json.load(urllib.request.urlopen(f"http://127.0.0.1:{self.port}/json"))
                tgt = next((t for t in L if t["type"] == "page"), None)
                if tgt:
                    break
            except Exception:
                pass
            time.sleep(0.1)
        if not tgt:
            raise SystemExit("chrome did not come up")
        self.ws = websocket.create_connection(tgt["webSocketDebuggerUrl"], suppress_origin=True, timeout=60)
        self.n = 0
        self.events = []
        self.cmd("Page.enable"); self.cmd("Runtime.enable"); self.cmd("Network.enable")

    def cmd(self, method, params=None):
        self.n += 1
        mid = self.n
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        while True:
            m = json.loads(self.ws.recv())
            if m.get("id") == mid:
                if "error" in m:
                    raise RuntimeError(f"{method}: {m['error']}")
                return m.get("result", {})
            self.events.append(m)

    def js(self, expr):
        r = self.cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True, "awaitPromise": True})
        if "exceptionDetails" in r:
            raise RuntimeError(f"JS error in {expr[:80]!r}: {r['exceptionDetails'].get('exception', {}).get('description')}")
        return r["result"].get("value")

    def wait(self, expr, timeout=10):
        t = time.time()
        while time.time() - t < timeout:
            try:
                if self.js(expr):
                    return True
            except RuntimeError:
                pass
            time.sleep(0.1)
        return False

    def goto(self, url):
        self.cmd("Page.navigate", {"url": url})
        time.sleep(0.2)
        self.wait("document.readyState==='complete' && !!document.body")
        time.sleep(0.4)          # DOMContentLoaded handlers + KaTeX

    def reload(self):
        self.cmd("Page.reload", {"ignoreCache": True})
        time.sleep(0.2)
        self.wait("document.readyState==='complete' && !!document.body")
        time.sleep(0.4)

    def width(self, w, h=900):
        self.cmd("Emulation.setDeviceMetricsOverride", {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": w < 600})

    def shot(self, path, full=False):
        p = {"format": "png"}
        if full:
            m = self.cmd("Page.getLayoutMetrics")["cssContentSize"]
            p.update(captureBeyondViewport=True,
                     clip={"x": 0, "y": 0, "width": m["width"], "height": min(m["height"], 6000), "scale": 1})
        open(path, "wb").write(base64.b64decode(self.cmd("Page.captureScreenshot", p)["data"]))

    def urls(self):
        return [e["params"]["request"]["url"] for e in self.events if e.get("method") == "Network.requestWillBeSent"]

    def close(self):
        try:
            self.ws.close()
        finally:
            self.p.terminate()
            try:
                self.p.wait(5)
            except Exception:
                self.p.kill()
            shutil.rmtree(self.prof, ignore_errors=True)


# ------------------------------------------------------------------ page helpers
def click(c, sel):
    return c.js(f"(function(){{var e=document.querySelector({json.dumps(sel)}); if(!e) return false; e.click(); return true}})()")


def visible(c, sel):
    return c.js(f"(function(){{var e=document.querySelector({json.dumps(sel)}); return !!(e && e.getClientRects().length>0 && !e.closest('[hidden]'))}})()")


def state(c, T):
    return c.js(f"JSON.parse(localStorage.getItem('pbrev-jee-test-{T}')||'null')")


def cur(c):
    return c.js("(function(){var a=[].slice.call(document.querySelectorAll('article.jq')).filter(function(x){return !x.hidden});"
                "return a.length===1? +a[0].dataset.i : -1})()")


def pick(c, i, opt):
    return click(c, f'#jq{i + 1} input[value="{opt}"]')


def type_in(c, i, text):
    c.js(f"(function(){{var e=document.querySelector('#jq{i + 1} .jin'); e.value=''; e.focus()}})()")
    c.cmd("Input.insertText", {"text": text})


def act(c, a):
    return click(c, f'.jactions button[data-act="{a}"]')


def parse_clock(s):
    m = re.fullmatch(r"(\d+):(\d\d):(\d\d)", s.strip())
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3)) if m else None


def no_overflow(c, w, where):
    sw = c.js("document.documentElement.scrollWidth")
    ok(sw <= w + 1, f"{where}: page scrolls horizontally at {w}px (scrollWidth {sw})")


# ------------------------------------------------------------------ the scenario
def run_test(c, base, site, T, shots):
    url = f"{base}/jee/test-{T}.html"
    print(f"test {T}: {url}")
    c.width(1280)
    c.goto(url)
    c.js("localStorage.clear()")
    c.reload()

    # --- gate
    ok(visible(c, "#jgate") and not visible(c, "#jexam") and not visible(c, "#jresult"), "gate shown first, exam and result hidden")
    ok(c.js("document.getElementById('jstart').disabled"), "Start is disabled until the instructions are acknowledged")
    ok(c.js("document.querySelectorAll('.katex').length") > 0, "KaTeX rendered")
    ok(c.js("document.querySelectorAll('.katex-error').length") == 0, "no KaTeX errors")
    ok(c.js("[].every.call(document.querySelectorAll('.jsol'),function(s){return s.hidden})"), "solutions hidden before submit")
    n = c.js("document.querySelectorAll('article.jq').length")
    ok(n == 75, f"75 questions on the page (found {n})")
    key = c.js("JSON.parse(atob(document.getElementById('jee-key').textContent.trim()))")
    ok(len(key) == 75 and [k["s"] for k in key] == [0] * 25 + [1] * 25 + [2] * 25, "answer key: 25 per subject in order")
    ok([k["k"] for k in key] == (["m"] * 20 + ["n"] * 5) * 3, "answer key: 20 MCQ then 5 numerical per subject")
    ok(c.js("[].every.call(document.querySelectorAll('article.jq'),function(a,i){return a.id==='jq'+(i+1)})"), "questions numbered 1-75")
    ok(state(c, T) is None, "nothing stored before start")

    # --- start
    click(c, "#jagree"); click(c, "#jstart")
    t0 = time.time() * 1000
    st = state(c, T)
    ok(st and st["started"] and abs(st["deadline"] - (t0 + 180 * 60000)) < 5000, "start stores a deadline 180 min ahead")
    ok(visible(c, "#jexam") and not visible(c, "#jgate") and visible(c, "#jsubmit"), "exam view and Submit shown after start")
    ok(cur(c) == 0, "starts on question 1")
    time.sleep(1.2)
    secs = parse_clock(c.js("document.getElementById('jclock').textContent"))
    ok(secs is not None and 10780 <= secs <= 10800, f"clock reads ~2:59:5x after start (got {secs})")
    ok(c.js("document.querySelector('.jtabs button.on').textContent") == "Physics", "Physics tab active")
    ok(c.js("document.querySelector('.jsecs button.on').dataset.sec") == "A", "Section A active")

    if shots:
        shot_question(c, shots, T, 1280)

    exp = {}            # i -> expected status
    resp = {}           # i -> saved response
    wrong = lambda i: (key[i]["a"] + 1) % 4 if key[i]["k"] == "m" else key[i]["a"] + 1

    # i0 correct, save
    pick(c, 0, key[0]["a"]); act(c, "save"); exp[0] = 2; resp[0] = key[0]["a"]
    ok(cur(c) == 1, "Save & Next moves to question 2")
    # i1 wrong, save
    pick(c, 1, wrong(1)); act(c, "save"); exp[1] = 2; resp[1] = wrong(1)
    # i2 correct, mark
    pick(c, 2, key[2]["a"]); act(c, "mark"); exp[2] = 4; resp[2] = key[2]["a"]
    ok(cur(c) == 3, "Mark for Review & Next moves on")
    # i3 wrong, mark  (answered & marked is evaluated -> -1)
    pick(c, 3, wrong(3)); act(c, "mark"); exp[3] = 4; resp[3] = wrong(3)
    # i4 no answer, mark
    act(c, "mark"); exp[4] = 3
    # i5 no answer, save
    act(c, "save"); exp[5] = 1
    ok(cur(c) == 6, "now on question 7")
    # i6: choose the right option but go Back -> not saved
    pick(c, 6, key[6]["a"]); act(c, "back"); exp[6] = 1
    ok(cur(c) == 5, "Back moves to the previous question")
    ok(c.js("!document.querySelector('#jq6 input:checked')"), "question 6 still blank after Back")
    click(c, ".jpgrid .jp[data-i='6']")
    ok(cur(c) == 6 and c.js("!document.querySelector('#jq7 input:checked')"), "unsaved choice on Q7 discarded by Back")
    act(c, "save")                                   # Q7 left blank -> not answered, on to Q8
    ok(cur(c) == 7, "Save & Next on a blank question moves on")
    # i7: answer, save, then come back and Clear Response
    pick(c, 7, key[7]["a"]); act(c, "save"); exp[8] = 1
    click(c, ".jpgrid .jp[data-i='7']"); act(c, "clear"); exp[7] = 1
    ok(c.js("!document.querySelector('#jq8 input:checked')"), "Clear Response unchecks the option")
    ok((state(c, T)["resp"].get("7")) is None, "Clear Response removes the saved answer")
    # Section B via section button
    click(c, '.jsecs button[data-sec="B"]')
    ok(cur(c) == 20, "Section B button jumps to question 21")
    ok(c.js("document.querySelector('.jsecs button.on').dataset.sec") == "B", "Section B highlighted")
    type_in(c, 20, str(key[20]["a"])); act(c, "save"); exp[20] = 2; resp[20] = key[20]["a"]
    type_in(c, 21, str(wrong(21))); act(c, "save"); exp[21] = 2; resp[21] = wrong(21)
    # i22: non-integer rejected
    type_in(c, 22, "2.5"); act(c, "save")
    ok(cur(c) == 22, "a non-integer answer does not advance")
    ok(visible(c, "#jq23 .jerr"), "a non-integer answer shows the error")
    ok("22" not in state(c, T)["resp"], "a non-integer answer is not saved")
    act(c, "clear")
    ok(not visible(c, "#jq23 .jerr"), "Clear Response hides the error")
    # a negative integer typed with a Unicode minus is accepted (always a wrong answer here)
    negw = -abs(key[22]["a"]) - 1
    type_in(c, 22, "\u2212" + str(abs(negw)))
    ok(not visible(c, "#jq23 .jerr"), "a negative integer shows no error")
    act(c, "save"); exp[22] = 2; resp[22] = negw
    ok(state(c, T)["resp"].get("22") == negw, f"negative integer {negw} saved")
    # i23: the correct answer through the on-screen keypad (sign toggled after the digits)
    a23 = key[23]["a"]
    for ch in str(abs(a23)):
        click(c, f'#jq24 .jkeys button[data-k="{ch}"]')
    if a23 < 0:
        click(c, '#jq24 .jkeys button[data-k="-"]')
    click(c, '#jq24 .jkeys button[data-k="-"]'); click(c, '#jq24 .jkeys button[data-k="-"]')   # toggle twice = no-op
    click(c, '#jq24 .jkeys button[data-k="9"]'); click(c, '#jq24 .jkeys button[data-k="bs"]')  # type, backspace
    ok(c.js("document.querySelector('#jq24 .jin').value") == str(a23), f"keypad builds {a23}")
    act(c, "save"); exp[23] = 2; resp[23] = a23; exp[24] = 1
    # chemistry tab
    click(c, '.jtabs button[data-s="1"]')
    ok(cur(c) == 25 and c.js("document.querySelector('.jtabs button.on').textContent") == "Chemistry", "Chemistry tab jumps to Q26")
    ok(c.js("!document.querySelector('.jpgrid[data-s=\"1\"]').hidden && document.querySelector('.jpgrid[data-s=\"0\"]').hidden"),
       "palette shows the current subject only")
    pick(c, 25, key[25]["a"]); act(c, "save"); exp[25] = 2; resp[25] = key[25]["a"]
    pick(c, 26, key[26]["a"]); act(c, "clear"); exp[26] = 1
    click(c, '.jsecs button[data-sec="B"]'); ok(cur(c) == 45, "Chemistry Section B -> Q46")
    type_in(c, 45, str(key[45]["a"])); act(c, "save"); exp[45] = 2; resp[45] = key[45]["a"]; exp[46] = 1
    # maths
    click(c, '.jtabs button[data-s="2"]'); ok(cur(c) == 50, "Mathematics tab jumps to Q51")
    pick(c, 50, wrong(50)); act(c, "save"); exp[50] = 2; resp[50] = wrong(50)
    pick(c, 51, key[51]["a"]); act(c, "save"); exp[51] = 2; resp[51] = key[51]["a"]
    exp[52] = 1                                     # now on Q53: visited
    ok(cur(c) == 52, "on Q53")
    full = [exp.get(i, 0) for i in range(75)]
    st = state(c, T)
    ok(st["stat"] == full, f"stored statuses match (diff at {[i + 1 for i in range(75) if st['stat'][i] != full[i]]})")
    ok({int(k): v for k, v in st["resp"].items()} == resp, f"stored responses match {st['resp']} vs {resp}")
    pal = c.js("[].map.call(document.querySelectorAll('.jpgrid .jp'),function(b){return [+b.dataset.i,b.className]})")
    ok(all(f"s{full[i]}" in cls.split() for i, cls in pal), "palette classes match the statuses")
    ok(sum("cur" in cls.split() for _, cls in pal) == 1, "exactly one palette button is current")
    lc = c.js("[].map.call(document.querySelectorAll('#jlegend [data-c]'),function(e){return +e.textContent})")
    want = [sum(1 for i in range(50, 75) if full[i] == k) for k in range(5)]
    ok(lc == want, f"legend counts for Mathematics {lc} == {want}")

    if shots:
        c.js("document.querySelector('.jpal').scrollIntoView()")
        c.shot(os.path.join(shots, f"t{T}-1280-palette.png"))

    # --- reload: resume
    dl = st["deadline"]
    c.reload()
    ok(visible(c, "#jexam") and not visible(c, "#jgate"), "reload resumes into the exam, not the gate")
    ok(cur(c) == 52, f"reload resumes on the same question (Q53), got Q{cur(c) + 1}")
    st2 = state(c, T)
    ok(st2["deadline"] == dl, "deadline unchanged by reload")
    ok(st2["stat"] == full, "statuses survive reload")
    pal2 = c.js("[].map.call(document.querySelectorAll('.jpgrid .jp'),function(b){return [+b.dataset.i,b.className]})")
    ok(all(f"s{full[i]}" in cls.split() for i, cls in pal2), "palette restored after reload")
    c.js("document.querySelector('.jtabs button[data-s=\"0\"]').click()")
    ok(c.js(f"document.querySelector('#jq1 input[value=\"{key[0]['a']}\"]').checked"), "saved option re-checked after reload")
    c.js("document.querySelector('.jpgrid .jp[data-i=\"23\"]').click()")
    ok(c.js("document.querySelector('#jq24 .jin').value") == str(key[23]['a']), "saved integer restored after reload")
    left = (dl - time.time() * 1000) / 1000
    secs = parse_clock(c.js("document.getElementById('jclock').textContent"))
    ok(secs is not None and abs(secs - left) <= 2, f"clock after reload {secs}s vs stored deadline {left:.0f}s")
    time.sleep(2.1)
    secs2 = parse_clock(c.js("document.getElementById('jclock').textContent"))
    ok(secs2 is not None and 1 <= secs - secs2 <= 3, f"clock keeps counting down ({secs} -> {secs2})")

    # --- submit dialog
    full = state(c, T)["stat"]
    click(c, "#jsubmit")
    ok(visible(c, "#jmodal"), "Submit opens the in-page dialog")
    rows = c.js("[].map.call(document.querySelectorAll('#jmodalcounts tr'),function(r){return [].map.call(r.cells,function(x){return x.textContent})})")
    for k in range(5):
        per = [sum(1 for i in range(s * 25, s * 25 + 25) if full[i] == k) for s in range(3)]
        got = [int(x) for x in rows[k + 1][1:5]]
        ok(got == per + [sum(per)], f"dialog counts for status {k}: {got} vs {per + [sum(per)]}")
    click(c, "#jmodalno")
    ok(not visible(c, "#jmodal") and visible(c, "#jexam"), "'No, go back' returns to the test")
    ok(not state(c, T)["submitted"], "not submitted after cancelling")
    click(c, "#jsubmit"); click(c, "#jmodalyes")
    time.sleep(0.4)

    # --- result
    ok(visible(c, "#jresult") and not visible(c, "#jexam"), "result view after submit")
    st = state(c, T)
    ok(st["submitted"] and not st["auto"], "stored as submitted (manual)")
    score = [0, 0, 0]; right = [0, 0, 0]; wrongc = [0, 0, 0]; skip = [0, 0, 0]
    for i in range(75):
        s = i // 25
        r = st["resp"].get(str(i))
        if st["stat"][i] in (2, 4) and r is not None:
            if r == key[i]["a"]:
                score[s] += 4; right[s] += 1
            else:
                score[s] -= 1; wrongc[s] += 1
        else:
            skip[s] += 1
    total = sum(score)
    # hand count from the scenario: correct 0,2,20,23,25,45,51 (7); wrong 1,3,21,22,50 (5)
    ok(sum(right) == 7 and sum(wrongc) == 5, f"scenario gives 7 correct, 5 incorrect (got {sum(right)}, {sum(wrongc)})")
    ok(total == 7 * 4 - 5, f"+4/-1 total is 23 (computed {total})")
    shown = int(c.js("document.getElementById('jtotal').textContent"))
    ok(shown == total, f"page total {shown} == {total}")
    ok(st["score"] == total, "stored score matches")
    tab = c.js("[].map.call(document.querySelectorAll('table.jscore tr'),function(r){return [].map.call(r.cells,function(x){return x.textContent})})")
    for s in range(3):
        row = tab[s + 1]
        ok(row[1].split(" /")[0].strip() == str(score[s]) and row[2:] == [str(right[s]), str(wrongc[s]), str(skip[s])],
           f"subject {s} row {row} vs score {score[s]} {right[s]}/{wrongc[s]}/{skip[s]}")
    ok(c.js("[].every.call(document.querySelectorAll('article.jq'),function(a){return !a.hidden && !a.querySelector('.jsol').hidden && !a.querySelector('.jrev').hidden})"),
       "every question shown with its solution and response line")
    ok(c.js("[].every.call(document.querySelectorAll('article.jq input'),function(x){return x.disabled})"), "inputs disabled in review")
    marks = c.js("[].map.call(document.querySelectorAll('article.jq .jmk b'),function(b){return b.textContent})")
    want = []
    for i in range(75):
        r = st["resp"].get(str(i))
        want.append("0" if not (st["stat"][i] in (2, 4) and r is not None) else ("+4" if r == key[i]["a"] else "−1"))
    ok(marks == want, f"per-question marks shown {[(i + 1, a, b) for i, (a, b) in enumerate(zip(marks, want)) if a != b][:5]}")
    okmark = c.js("[].map.call(document.querySelectorAll('article.jq[data-k=m]'),function(a){var o=a.querySelector('.jopt.ok');return o?+o.dataset.o:-1})")
    ok(okmark == [k["a"] for k in key if k["k"] == "m"], "the correct option is highlighted on every MCQ")
    # source links
    links = c.js("[].map.call(document.querySelectorAll('.jsrc a'),function(a){return [a.getAttribute('href'),a.textContent]})")
    ok(len(links) == 75, f"75 source links (found {len(links)})")
    badl = []
    for href, text in links:
        m = re.fullmatch(r"\.\./(\w+)/([\w.-]+\.html)#(q[\w-]+)", href)
        if not m or not text.startswith(("Physics pre-board", "Chemistry pre-board", "Mathematics pre-board")):
            badl.append(href); continue
        f = os.path.join(site, m.group(1), m.group(2))
        if not os.path.exists(f) or f'id="{m.group(3)}"' not in open(f).read():
            badl.append(href)
    ok(not badl, f"every source link resolves to a page and anchor: bad {badl[:5]}")
    content_checks(c, 1280, T)
    # filter
    click(c, '#jfilter button[data-f="wrong"]')
    vis = c.js("[].filter.call(document.querySelectorAll('article.jq'),function(a){return !a.hidden}).length")
    ok(vis == sum(wrongc), f"'Incorrect' filter shows {sum(wrongc)} (got {vis})")
    click(c, '#jfilter button[data-f="all"]')
    if shots:
        c.js("window.scrollTo(0,0)")
        c.shot(os.path.join(shots, f"t{T}-1280-result.png"))
        c.js("document.querySelector('article.jq[data-res=wrong]').scrollIntoView()")
        c.shot(os.path.join(shots, f"t{T}-1280-review.png"))
        c.width(400, 860)
        time.sleep(0.6)
        no_overflow(c, 400, "result view")
        content_checks(c, 400, T)
        c.js("window.scrollTo(0,0)")
        c.shot(os.path.join(shots, f"t{T}-400-result.png"))
        c.js("document.querySelector('article.jq[data-res=right]').scrollIntoView()")
        c.shot(os.path.join(shots, f"t{T}-400-review.png"))
        c.width(1280)

    # reload keeps the result
    c.reload()
    ok(visible(c, "#jresult") and int(c.js("document.getElementById('jtotal').textContent")) == total, "result persists across reload")
    ok(c.js("document.getElementById('jclock').textContent") == "Submitted", "clock reads Submitted")

    # index page reflects it
    c.goto(f"{base}/jee/index.html")
    ok(c.js(f"document.querySelector('.jstat[data-key=\"pbrev-jee-test-{T}\"]').textContent") == f"Submitted · {total} / 300",
       "jee/index.html shows the submitted score")
    ok(c.js("document.querySelector('a.crumb').getAttribute('href')") == "../index.html", "index crumb back to the landing page")
    if shots:
        c.shot(os.path.join(shots, f"index-1280.png"))
    nready = len([f for f in os.listdir(os.path.join(site, "jee")) if re.fullmatch(r"test-\d\.html", f)])
    ok(c.js("document.querySelectorAll('li.jtest a').length") == nready and
       c.js("document.querySelectorAll('li.jtest.soon').length") == 3 - nready, "index lists built tests as links, the rest as coming soon")
    c.goto(url)

    # --- retake
    click(c, "#jretake")
    ok(visible(c, "#jretakeconf"), "Retake asks for confirmation in the page")
    click(c, "#jretakeno"); ok(not visible(c, "#jretakeconf") and state(c, T)["submitted"], "cancel keeps the result")
    click(c, "#jretake"); click(c, "#jretakeyes")
    time.sleep(0.3); c.wait("document.readyState==='complete'"); time.sleep(0.4)
    ok(visible(c, "#jgate") and state(c, T) is None, "Retake clears the stored state and returns to the gate")

    # --- expiry while open
    click(c, "#jagree"); click(c, "#jstart")
    pick(c, 0, key[0]["a"]); act(c, "save")
    pick(c, 1, key[1]["a"])                          # chosen but not saved: must not count
    c.js(f"(function(){{var s=JSON.parse(localStorage.getItem('pbrev-jee-test-{T}'));s.deadline=Date.now()+2500;"
         f"localStorage.setItem('pbrev-jee-test-{T}',JSON.stringify(s))}})()")
    ok(c.wait("!document.getElementById('jresult').hidden", 8), "test submits itself when the clock reaches zero")
    st = state(c, T)
    ok(st["submitted"] and st["auto"], "stored as auto-submitted")
    ok(int(c.js("document.getElementById('jtotal').textContent")) == 4, "auto-submit scores only saved answers (4)")
    ok(visible(c, ".jresult .jnote"), "result says the time ran out")
    if shots:
        c.js("window.scrollTo(0,0)")
        c.shot(os.path.join(shots, f"t{T}-1280-autosubmit.png"))

    # --- expiry while closed: deadline passed before the page is opened
    c.js(f"localStorage.setItem('pbrev-jee-test-{T}', JSON.stringify({{v:1,started:true,deadline:Date.now()-60000,cur:3,"
         f"resp:{{'0':{key[0]['a']},'1':{(key[1]['a'] + 1) % 4}}},stat:[2,4].concat(Array(73).fill(0)),submitted:false,at:0,auto:false,score:null}}))")
    c.reload()
    ok(visible(c, "#jresult") and not visible(c, "#jexam"), "a deadline that passed while away submits on load")
    ok(int(c.js("document.getElementById('jtotal').textContent")) == 3, "and scores 4 − 1 = 3")
    ok(state(c, T)["auto"], "flagged auto")

    # --- phone width: question + palette views
    c.js("localStorage.clear()")
    c.width(400, 860)
    c.reload()
    no_overflow(c, 400, "gate")
    click(c, "#jagree"); click(c, "#jstart")
    pick(c, 0, key[0]["a"]); act(c, "save"); act(c, "mark")
    pal_y = c.js("document.querySelector('.jpal').getBoundingClientRect().top")
    q_y = c.js("document.querySelector('article.jq:not([hidden])').getBoundingClientRect().bottom")
    ok(pal_y >= q_y, "at 400px the palette sits below the question")
    no_overflow(c, 400, "exam view")
    if shots:
        shot_question(c, shots, T, 400)
        c.js("document.querySelector('.jpal').scrollIntoView()")
        c.shot(os.path.join(shots, f"t{T}-400-palette.png"))
        click(c, "#jsubmit")
        c.shot(os.path.join(shots, f"t{T}-400-submit-dialog.png"))
        click(c, "#jmodalno")
    c.width(1280)
    c.js("localStorage.clear()")


def content_checks(c, w, T):
    """Run with the review open (every question, option, solution and caption visible)."""
    raw = c.js(r"""(function(){var out=[];document.querySelectorAll('article.jq').forEach(function(a){
        var t=a.innerText; if(/\\[()\[\]]|\$\$|\\(ce|frac|dfrac|begin|end|times|mathrm)\b/.test(t)) out.push(a.id)});return out})()""")
    ok(not raw, f"test {T}: raw TeX left unrendered in {raw[:8]}")
    kerr = c.js("[].map.call(document.querySelectorAll('.katex-error'),function(e){return (e.closest('article')||{}).id+': '+e.textContent.slice(0,60)})")
    ok(not kerr, f"test {T}: KaTeX errors {kerr[:5]}")
    cap = c.js(r"[].filter.call(document.querySelectorAll('figcaption'),function(f){return /\\\(/.test(f.innerText)}).length")
    ok(cap == 0, f"test {T}: {cap} figure captions with raw math")
    over = c.js("""(function(){var out=[];document.querySelectorAll('.jopt').forEach(function(l){var t=l.querySelector('.jot');
        if(t.scrollWidth>t.clientWidth+2) out.push([l.closest('article').id+'('+(+l.dataset.o+1)+')',
          !!l.closest('.jopts.grid2:not(.stack)')])});return out})()""")
    # a 2x2 layout that did not fall back is the shell's fault; a single unbreakable formula wider
    # than the screen scrolls inside its own option box (allowed) and is only reported.
    ok(not [o for o, g in over if g], f"test {T} at {w}px: 2x2 options overflow without stacking: {[o for o, g in over if g][:8]}")
    if over:
        print(f"  note test {T} at {w}px: options scroll sideways inside their box: {[o for o, g in over][:12]}")


def shot_question(c, shots, T, w):
    """Screenshot the first question carrying a figure (else the current one) and a numerical one."""
    i = c.js("(function(){var a=document.querySelector('article.jq .jqbody figure');return a? +a.closest('article').dataset.i : -1})()")
    back = cur(c)
    if i >= 0:
        c.js(f"document.querySelector('.jpgrid .jp[data-i=\"{i}\"]').click()")
    c.js("window.scrollTo(0,0)")
    c.shot(os.path.join(shots, f"t{T}-{w}-question.png"))
    c.js("document.querySelector('.jpgrid .jp[data-i=\"20\"]').click()")
    c.js("window.scrollTo(0,0)")
    c.shot(os.path.join(shots, f"t{T}-{w}-numerical.png"))
    c.js(f"document.querySelector('.jpgrid .jp[data-i=\"{back}\"]').click()")
    # restore: visiting marks questions "not answered"; the caller's expectations account only for
    # questions it touches, so reset those two visits.
    c.js(f"(function(){{var k='pbrev-jee-test-{T}',s=JSON.parse(localStorage.getItem(k));"
         f"[{i},20].forEach(function(j){{if(j>=0&&j!=={back}&&s.stat[j]===1&&s.resp[j]===undefined)s.stat[j]=0}});"
         f"localStorage.setItem(k,JSON.stringify(s))}})()")
    c.reload()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=ROOT)
    ap.add_argument("--test", type=int, action="append")
    ap.add_argument("--shots", default="/var/tmp/pbrev-jee-shots")
    a = ap.parse_args()
    site = os.path.abspath(a.site)
    jd = os.path.join(site, "jee")
    tests = a.test or sorted(int(m.group(1)) for f in os.listdir(jd) if (m := re.fullmatch(r"test-(\d)\.html", f)))
    if not os.path.exists(os.path.join(jd, "index.html")):
        raise SystemExit("no jee/index.html — run python3 src/build_jee.py")
    if not tests:
        print("no built tests (all coming soon) — nothing to sit")
        return 0
    os.makedirs(a.shots, exist_ok=True)
    srv, port = serve(site)
    base = f"http://127.0.0.1:{port}"
    c = Chrome(f"{base}/jee/index.html")
    try:
        for T in tests:
            run_test(c, base, site, T, a.shots)
        ext = [u for u in c.urls() if not u.startswith(base) and not u.startswith("data:")]
        ok(not ext, f"no external requests: {ext[:5]}")
    finally:
        c.close()
        srv.shutdown()
    print(f"{PASSES[0]} passed, {len(FAILS)} failed" + (f"; screenshots in {a.shots}" if a.shots else ""))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
