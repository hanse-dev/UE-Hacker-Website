// Bloecke als Text im Lektions-Markdown: Codeblock mit Sprache `bloecke`, pro Zeile
// `[kategorie] Beschriftung`, zwei Leerzeichen Einrueckung je Verschachtelungsebene. Daraus werden
// farbige Block-Zeilen (`mc-block mc-<kategorie>`); die Farben setzt die Komponente, die das HTML
// zeigt: GuideLessonView.vue (MakeCode-Kategorien, micro:bit) und SpielLessonView.vue
// (Blockly-Kategorien der Spiel-Projekte).
export function renderBlocks(code) {
  const rows = code.replace(/\n$/, '').split('\n').filter((line) => line.trim()).map((line) => {
    const indent = Math.floor(line.match(/^ */)[0].length / 2);
    const m = line.trim().match(/^\[([a-z]+)\]\s*(.*)$/);
    const category = m ? m[1] : 'grundlagen';
    const label = m ? m[2] : line.trim();
    return `<div class="mc-block mc-${category}" style="margin-left:${indent * 24}px">${label}</div>`;
  });
  return `<div class="mc-blocks">${rows.join('')}</div>`;
}

/** Ersetzt jeden ```bloecke-Codeblock im gerenderten Markdown-HTML durch die Block-Zeilen. */
export function renderBlockListings(html) {
  return html.replace(/<pre><code class="language-bloecke">([\s\S]*?)<\/code><\/pre>/g, (_, code) => renderBlocks(code));
}
