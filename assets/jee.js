/* JEE Main-style CBT for the pre-board revision site.  Built pages: src/build_jee.py.
   State per test in localStorage[data-key]:
     {v, started, t0 (start, ms epoch), deadline (ms epoch), cur, resp:{i:value}, stat:[0..4], submitted, at, auto, score}
   stat: 0 not visited, 1 not answered, 2 answered, 3 marked for review, 4 answered & marked.
   A response is saved only by Save & Next / Mark for Review & Next (as on the NTA console).
   The clock always reads the stored deadline, so a reload never resets it. */
(function () {
  "use strict";
  var NAMES = ["Not visited", "Not answered", "Answered", "Marked for review", "Answered & marked for review"];
  var SUBJ = ["Physics", "Chemistry", "Mathematics"];

  function readStore(key) {
    try { var s = localStorage.getItem(key); return s ? JSON.parse(s) : null; } catch (e) { return null; }
  }
  function writeStore(key, v) { try { localStorage.setItem(key, JSON.stringify(v)); } catch (e) {} }
  function dropStore(key) { try { localStorage.removeItem(key); } catch (e) {} }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function hms(ms) {
    var t = Math.max(0, Math.ceil(ms / 1000)), h = Math.floor(t / 3600), m = Math.floor(t % 3600 / 60), s = t % 60;
    return h + ":" + (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
  }
  function fmtScore(v) { return (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v); }

  /* ---------------------------------------------------------------- landing (jee/index.html) */
  function indexPage() {
    $$(".jstat[data-key]").forEach(function (el) {
      var st = readStore(el.getAttribute("data-key"));
      if (!st || !st.started) return;
      if (st.submitted) { el.textContent = "Submitted · " + st.score + " / 300"; el.classList.add("done"); }
      else if (st.deadline > Date.now()) { el.textContent = "In progress · " + hms(st.deadline - Date.now()) + " left"; el.classList.add("live"); }
      else { el.textContent = "Time over · open to see the result"; el.classList.add("live"); }
    });
  }

  /* ---------------------------------------------------------------- test page */
  function testPage(root) {
    var KEY = root.getAttribute("data-key");
    var MIN = +root.getAttribute("data-minutes") || 180;
    var key;
    try { key = JSON.parse(atob($("#jee-key").textContent.trim())); } catch (e) { key = []; }
    var N = key.length;
    var arts = $$("article.jq");
    var palBtns = []; $$(".jpgrid .jp").forEach(function (b) { palBtns[+b.getAttribute("data-i")] = b; });
    var clock = $("#jclock"), gate = $("#jgate"), exam = $("#jexam"), result = $("#jresult"), subBtn = $("#jsubmit");
    var modal = $("#jmodal");
    var timer = null;

    function fresh() {
      var s = []; for (var i = 0; i < N; i++) s.push(0);
      return {v: 1, started: false, deadline: 0, cur: 0, resp: {}, stat: s, submitted: false, at: 0, auto: false, score: null};
    }
    var st = readStore(KEY);
    if (!st || st.v !== 1 || !st.stat || st.stat.length !== N) st = fresh();
    function save() { writeStore(KEY, st); }

    /* ---- reading / writing the response widgets */
    function readInput(i) {
      var a = arts[i];
      if (key[i].k === "m") {
        var c = $("input[type=radio]:checked", a);
        return c ? +c.value : null;
      }
      var v = $(".jin", a).value.replace(/\s+/g, "").replace(/−/g, "-");
      if (v === "") return null;
      if (!/^-?\d+$/.test(v)) return "bad";
      var n = parseInt(v, 10);
      return n === 0 ? 0 : n;          // "-0" is 0
    }
    function writeInput(i) {
      var a = arts[i], r = st.resp[i];
      if (key[i].k === "m") {
        $$("input[type=radio]", a).forEach(function (x) { x.checked = (r !== undefined && +x.value === r); });
      } else {
        $(".jin", a).value = (r === undefined ? "" : String(r));
        $(".jerr", a).hidden = true;
      }
    }

    /* ---- palette, tabs, counts */
    function paintPalette() {
      for (var i = 0; i < N; i++) {
        var b = palBtns[i]; if (!b) continue;
        b.className = "jp s" + st.stat[i] + (i === st.cur ? " cur" : "");
        b.setAttribute("aria-label", "Question " + (i + 1) + ": " + NAMES[st.stat[i]]);
      }
      var s = key[st.cur].s, c = [0, 0, 0, 0, 0];
      for (var j = 0; j < N; j++) if (key[j].s === s) c[st.stat[j]]++;
      $$("#jlegend [data-c]").forEach(function (el) { el.textContent = c[+el.getAttribute("data-c")]; });
      $$(".jpgrid").forEach(function (g) { g.hidden = +g.getAttribute("data-s") !== s; });
      $$(".jtabs button").forEach(function (b) {
        var on = +b.getAttribute("data-s") === s;
        b.classList.toggle("on", on); b.setAttribute("aria-selected", on ? "true" : "false");
      });
      var sec = arts[st.cur].getAttribute("data-sec");
      $$(".jsecs button").forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-sec") === sec); });
      var last = st.cur === N - 1;
      $(".jb-save").textContent = last ? "Save" : "Save & Next";
      $(".jb-mark").textContent = last ? "Mark for Review" : "Mark for Review & Next";
      $(".jb-back").disabled = st.cur === 0;
    }
    /* 2 x 2 options (built for short / matrix options) fall back to one per line if any
       option would overflow its half-width box at this screen width. */
    function fitOpts(a) {
      var o = $(".jopts.grid2", a);
      if (!o || a.hidden) return;
      o.classList.remove("stack");
      if ($$(".jot", o).some(function (t) { return t.scrollWidth > t.clientWidth + 2; })) o.classList.add("stack");
    }
    function show(i, focus) {
      if (i < 0 || i >= N) return;
      arts.forEach(function (a, k) { a.hidden = k !== i; });
      st.cur = i;
      if (st.stat[i] === 0) st.stat[i] = 1;
      writeInput(i);
      paintPalette();
      fitOpts(arts[i]);
      save();
      if (focus) {
        var top = arts[i].getBoundingClientRect().top;
        var hdr = $(".jtop").getBoundingClientRect().height;
        if (top < hdr || top > window.innerHeight * 0.6) window.scrollTo(0, Math.max(0, window.scrollY + top - hdr - 70));
      }
    }
    function firstOf(s, sec) {
      for (var i = 0; i < N; i++) if (key[i].s === s && (!sec || arts[i].getAttribute("data-sec") === sec)) return i;
      return 0;
    }

    /* ---- the four buttons */
    function commit(mark) {
      var i = st.cur, v = readInput(i);
      if (v === "bad") { $(".jerr", arts[i]).hidden = false; $(".jin", arts[i]).focus(); return false; }
      if (v === null) { delete st.resp[i]; st.stat[i] = mark ? 3 : 1; }
      else { st.resp[i] = v; st.stat[i] = mark ? 4 : 2; }
      save();
      if (i < N - 1) show(i + 1, true); else { writeInput(i); paintPalette(); }
      return true;
    }
    function clearResp() {
      var i = st.cur;
      delete st.resp[i]; st.stat[i] = 1;
      writeInput(i); paintPalette(); save();
    }

    /* ---- clock */
    function tick() {
      var s = readStore(KEY);
      if (s && s.submitted && !st.submitted) { st = s; return showResult(); }
      var dl = (s && s.started && s.deadline) ? s.deadline : st.deadline;
      st.deadline = dl;
      var left = dl - Date.now();
      clock.textContent = hms(left);
      clock.classList.toggle("low", left <= 5 * 60 * 1000);
      if (left <= 0) submit(true);
    }
    function startClock() { if (!timer) { tick(); timer = setInterval(tick, 1000); } }
    function stopClock() { if (timer) { clearInterval(timer); timer = null; } }

    /* ---- start / submit / result */
    function enterExam() {
      gate.hidden = true; result.hidden = true; exam.hidden = false; subBtn.hidden = false;
      show(Math.min(Math.max(st.cur | 0, 0), N - 1), false);
      startClock();
    }
    function counts() {
      var c = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]];
      for (var i = 0; i < N; i++) c[key[i].s][st.stat[i]]++;
      return c;
    }
    function askSubmit() {
      var c = counts(), rows = "";
      for (var k = 0; k < 5; k++) {
        rows += "<tr><td class='jl'><span class='jlab'><span class='jp s" + k + "'><span></span></span>" + NAMES[k] + "</span></td>";
        var tot = 0;
        for (var s = 0; s < 3; s++) { rows += "<td>" + c[s][k] + "</td>"; tot += c[s][k]; }
        rows += "<td><b>" + tot + "</b></td></tr>";
      }
      $("#jmodalcounts").innerHTML = "<div class='tbl'><table class='jcount'><tr><th></th><th>Phy</th><th>Chem</th><th>Math</th><th>All</th></tr>" +
        rows + "</table></div><p class='jnote'>Evaluated: answered, and answered &amp; marked for review. Time left: " +
        hms(st.deadline - Date.now()) + ".</p>";
      modal.hidden = false;
      $("#jmodalno").focus();
    }
    function evaluate() {
      var sub = [0, 1, 2].map(function () { return {score: 0, right: 0, wrong: 0, skip: 0}; });
      var per = [];
      for (var i = 0; i < N; i++) {
        var r = st.resp[i], ev = (st.stat[i] === 2 || st.stat[i] === 4) && r !== undefined && r !== null;
        var o = sub[key[i].s], m;
        if (!ev) { o.skip++; m = 0; per.push("skip"); }
        else if (r === key[i].a) { o.right++; m = 4; per.push("right"); }
        else { o.wrong++; m = -1; per.push("wrong"); }
        o.score += m;
      }
      return {sub: sub, per: per, total: sub[0].score + sub[1].score + sub[2].score};
    }
    function submit(auto) {
      if (st.submitted) return showResult();
      st.submitted = true; st.auto = !!auto; st.at = Date.now();
      st.score = evaluate().total;
      save();
      showResult();
    }
    function showResult() {
      stopClock();
      modal.hidden = true;
      var E = evaluate();
      if (st.score === null || st.score === undefined) { st.score = E.total; save(); }
      gate.hidden = true; exam.hidden = true; result.hidden = false; subBtn.hidden = true;
      clock.textContent = "Submitted"; clock.classList.remove("low");
      var used = st.at && st.t0 ? Math.min(MIN * 60000, st.at - st.t0) : 0;
      var rows = "", tr = 0, tw = 0, ts = 0;
      E.sub.forEach(function (o, s) {
        rows += "<tr><td class='jl'>" + SUBJ[s] + "</td><td><b>" + o.score + "</b><span class='jof'> / 100</span></td><td>" + o.right +
          "</td><td>" + o.wrong + "</td><td>" + o.skip + "</td></tr>";
        tr += o.right; tw += o.wrong; ts += o.skip;
      });
      $("#jsummary").innerHTML = "<h1>Result</h1>" +
        (st.auto ? "<p class='jnote'>Time ran out — the test was submitted automatically.</p>" : "") +
        "<div class='jtotal'><span id='jtotal'>" + E.total + "</span> / 300</div>" +
        "<p class='meta'>" + tr + " correct × 4 − " + tw + " incorrect × 1 = " + E.total + " · " + ts + " unattempted" +
        (used > 0 ? " · time used " + hms(used) : "") + "</p>" +
        "<div class='tbl'><table class='jscore'><tr><th>Subject</th><th>Score</th><th>Correct</th><th>Incorrect</th><th>Not attempted</th></tr>" +
        rows + "<tr><th>Total</th><th>" + E.total + "<span class='jof'> / 300</span></th><th>" + tr + "</th><th>" + tw + "</th><th>" + ts + "</th></tr></table></div>" +
        "<h2 class='sec'>Every question, with the worked solution</h2>";
      // the question list itself becomes the review
      var qs = $("#jqs");
      if (qs.parentNode !== $("#jrevslot")) $("#jrevslot").appendChild(qs);
      qs.classList.add("review");
      $$(".jsubh", qs).forEach(function (h) { h.hidden = false; });
      arts.forEach(function (a, i) {
        a.hidden = false;
        a.setAttribute("data-res", E.per[i]);
        var r = st.resp[i], ev = E.per[i] !== "skip", corr = key[i].a, isM = key[i].k === "m";
        $$("input", a).forEach(function (x) { x.disabled = true; });
        $$(".jkeys button", a).forEach(function (x) { x.disabled = true; });
        if (isM) {
          $$(".jopt", a).forEach(function (l) {
            var o = +l.getAttribute("data-o");
            l.classList.toggle("ok", o === corr);
            l.classList.toggle("bad", ev && o === r && o !== corr);
            $("input", l).checked = ev && o === r;
          });
        } else { $(".jin", a).value = ev ? String(r) : ""; $(".jerr", a).hidden = true; }
        var shown = function (v) { return isM ? "(" + (v + 1) + ")" : String(v).replace("-", "−"); };
        var marks = E.per[i] === "right" ? 4 : E.per[i] === "wrong" ? -1 : 0;
        var note = !ev && st.stat[i] === 3 ? " (marked for review, not answered)" : "";
        var rv = $(".jrev", a);
        rv.innerHTML = "<span class='jres " + E.per[i] + "'>" + (E.per[i] === "right" ? "Correct" : E.per[i] === "wrong" ? "Incorrect" : "Not answered") +
          "</span><span>Your answer: <b>" + (ev ? shown(r) : "—") + "</b>" + note + "</span><span>Correct answer: <b>" + shown(corr) +
          "</b></span><span class='jmk'>Marks: <b>" + fmtScore(marks) + "</b></span>";
        rv.hidden = false;
        $(".jsol", a).hidden = false;
      });
      filter("all");
      arts.forEach(fitOpts);
      window.scrollTo(0, 0);
    }
    function filter(f) {
      $$("#jfilter button").forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-f") === f); });
      arts.forEach(function (a) { a.hidden = !(f === "all" || a.getAttribute("data-res") === f); });
      $$(".jsubh").forEach(function (h) {
        var s = h.getAttribute("data-s");
        h.hidden = !arts.some(function (a) { return a.getAttribute("data-s") === s && !a.hidden; });
      });
    }

    /* ---- wiring */
    $("#jagree").addEventListener("change", function () { $("#jstart").disabled = !this.checked; });
    $("#jstart").addEventListener("click", function () {
      st = fresh(); st.started = true; st.t0 = Date.now(); st.deadline = st.t0 + MIN * 60000; save();
      enterExam();
    });
    $$(".jactions button").forEach(function (b) {
      b.addEventListener("click", function () {
        var act = b.getAttribute("data-act");
        if (act === "save") commit(false);
        else if (act === "mark") commit(true);
        else if (act === "clear") clearResp();
        else if (act === "back") show(st.cur - 1, true);
      });
    });
    palBtns.forEach(function (b, i) { b.addEventListener("click", function () { show(i, true); }); });
    $$(".jtabs button").forEach(function (b) {
      b.addEventListener("click", function () { show(firstOf(+b.getAttribute("data-s")), true); });
    });
    $$(".jsecs button").forEach(function (b) {
      b.addEventListener("click", function () { show(firstOf(key[st.cur].s, b.getAttribute("data-sec")), true); });
    });
    arts.forEach(function (a) {
      var inp = $(".jin", a);
      if (!inp) return;
      inp.addEventListener("input", function () {
        var v = inp.value.replace(/\s+/g, "").replace(/−/g, "-");
        $(".jerr", a).hidden = v === "" || v === "-" || /^-?\d+$/.test(v);
      });
      inp.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); commit(false); } });
      $$(".jkeys button", a).forEach(function (k) {
        k.addEventListener("click", function () {
          var c = k.getAttribute("data-k"), v = inp.value;
          if (c === "bs") v = v.slice(0, -1);
          else if (c === "-") v = v.charAt(0) === "-" ? v.slice(1) : "-" + v;
          else if (v.length < 12) v += c;
          inp.value = v;
          inp.dispatchEvent(new Event("input"));
        });
      });
    });
    var rz = null;
    window.addEventListener("resize", function () {
      clearTimeout(rz);
      rz = setTimeout(function () { arts.forEach(fitOpts); }, 150);
    });
    subBtn.addEventListener("click", askSubmit);
    $("#jmodalno").addEventListener("click", function () { modal.hidden = true; });
    $("#jmodalyes").addEventListener("click", function () { submit(false); });
    modal.addEventListener("click", function (e) { if (e.target === modal) modal.hidden = true; });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") modal.hidden = true; });
    $$("#jfilter button").forEach(function (b) { b.addEventListener("click", function () { filter(b.getAttribute("data-f")); }); });
    $("#jretake").addEventListener("click", function () { $("#jretakeconf").hidden = false; });
    $("#jretakeno").addEventListener("click", function () { $("#jretakeconf").hidden = true; });
    $("#jretakeyes").addEventListener("click", function () {
      dropStore(KEY);
      location.replace(location.pathname + location.search);
    });

    /* ---- resume */
    if (st.submitted) showResult();
    else if (st.started && st.deadline) {
      if (Date.now() >= st.deadline) submit(true);
      else enterExam();
    } else {
      clock.textContent = hms(MIN * 60000);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    var root = document.querySelector(".jee[data-key]");
    if (root) testPage(root); else indexPage();
  });
})();
