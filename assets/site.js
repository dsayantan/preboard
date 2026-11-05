(function () {
  function math() {
    if (window.renderMathInElement) {
      renderMathInElement(document.body, {
        delimiters: [{left: "\\[", right: "\\]", display: true}, {left: "\\(", right: "\\)", display: false}],
        throwOnError: false
      });
    }
  }
  function store(key) {
    try { return JSON.parse(localStorage.getItem(key) || "{}"); } catch (e) { return {}; }
  }
  function save(key, v) { try { localStorage.setItem(key, JSON.stringify(v)); } catch (e) {} }
  function setOpen(art, open) {
    var a = art.querySelector(".ans"), b = art.querySelector(".reveal");
    if (!a || !b) return;
    a.hidden = !open; b.textContent = open ? "Hide answer" : "Show answer";
    b.setAttribute("aria-expanded", open ? "true" : "false");
  }
  document.addEventListener("DOMContentLoaded", function () {
    math();
    var main = document.querySelector("main[data-key]");
    if (!main) return;
    var key = main.getAttribute("data-key"), st = store(key);
    var prog = document.querySelector(".prog");
    function count() {
      var all = main.querySelectorAll(".done input"), n = 0;
      all.forEach(function (c) { if (c.checked) n++; });
      if (prog) prog.textContent = n + " / " + all.length + " revised";
    }
    main.querySelectorAll("article.q").forEach(function (art) {
      art.querySelector(".reveal").addEventListener("click", function () {
        setOpen(art, art.querySelector(".ans").hidden);
      });
      var c = art.querySelector(".done input");
      c.checked = !!st[c.dataset.id];
      art.classList.toggle("isdone", c.checked);
      c.addEventListener("change", function () {
        st[c.dataset.id] = c.checked; save(key, st);
        art.classList.toggle("isdone", c.checked); count();
      });
    });
    document.querySelectorAll(".tools button").forEach(function (b) {
      b.addEventListener("click", function () {
        var open = b.dataset.act === "show";
        main.querySelectorAll("article.q").forEach(function (a) { setOpen(a, open); });
      });
    });
    window.addEventListener("beforeprint", function () {
      main.querySelectorAll(".ans").forEach(function (a) { a.hidden = false; });
    });
    count();
  });
})();
