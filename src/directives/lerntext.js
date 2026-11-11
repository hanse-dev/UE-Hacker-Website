/**
 * `v-lerntext="html"` statt `v-html` fuer Lerntexte: Die Oberflaeche ist nicht uebersetzbar
 * (`#app translate="no"` in index.html), weil Seitenuebersetzer (Edge/Chrome) Absaetze neu aufbauen
 * und Vue dann abstuerzt. Lerntexte setzt Vue nur als Ganzes - die duerfen uebersetzt werden, Code
 * darin aber nicht.
 */
const apply = (el, { value, oldValue }, initial) => {
  // Nur bei neuem Text neu setzen, sonst wuerde jedes Re-Rendern die Uebersetzung verwerfen.
  if (!initial && value === oldValue) return;
  el.innerHTML = value ?? '';
  el.querySelectorAll('pre, code').forEach((node) => node.setAttribute('translate', 'no'));
};

// before*-Hooks: Inhalt steht wie bei v-html schon im DOM, wenn Watcher mit `flush: 'post'` laufen
// (z. B. Sprung zu #anker in GuideLessonView.vue).
export default {
  beforeMount(el, binding) {
    el.setAttribute('translate', 'yes');
    apply(el, binding, true);
  },
  beforeUpdate(el, binding) {
    apply(el, binding, false);
  },
};
