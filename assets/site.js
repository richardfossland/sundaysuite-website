// Sunday Suite — shared behaviour: nav background + scroll reveals
(function () {
  var nav = document.getElementById('nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 20); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    var burger = document.getElementById('navBurger');
    if (burger) {
      var setOpen = function (open) { nav.classList.toggle('open', open); burger.setAttribute('aria-expanded', open ? 'true' : 'false'); };
      burger.addEventListener('click', function () { setOpen(!nav.classList.contains('open')); });
      nav.querySelectorAll('nav.links a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
    }
  }
  // Desktop product pages: show the latest release version (progressive enhancement)
  var vslot = document.querySelector('[data-app-version]');
  if (vslot && window.fetch) {
    fetch('/download/' + vslot.getAttribute('data-app-version') + '/version').then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !d.version) return;
      var no = document.documentElement.lang === 'no';
      var txt = (no ? 'Nyeste versjon: v' : 'Latest version: v') + d.version;
      if (d.pub_date) {
        var dt = new Date(d.pub_date);
        if (!isNaN(dt)) txt += ' · ' + dt.toLocaleDateString(no ? 'nb-NO' : 'en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
      }
      vslot.textContent = txt + ' · ';
      vslot.hidden = false;
    }).catch(function () {});
  }
  var els = document.querySelectorAll('.reveal:not(.in)');
  if (!('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
})();
