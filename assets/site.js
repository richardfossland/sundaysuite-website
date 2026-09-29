// SundaySuite — shows the newest release next to the SundayRec download
// links. Progressive enhancement: the page works the same without it.
(function () {
  var slot = document.querySelector('[data-app-version]');
  if (!slot || !window.fetch) return;
  fetch('/download/' + slot.getAttribute('data-app-version') + '/version')
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) {
      if (!d || !d.version) return;
      var nb = document.documentElement.lang !== 'en';
      var txt = (nb ? 'Nyeste versjon: v' : 'Latest version: v') + d.version;
      if (d.pub_date) {
        var dt = new Date(d.pub_date);
        if (!isNaN(dt)) txt += ' (' + dt.toLocaleDateString(nb ? 'nb-NO' : 'en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) + ')';
      }
      slot.textContent = txt + '. ';
      slot.hidden = false;
    })
    .catch(function () {});
})();
