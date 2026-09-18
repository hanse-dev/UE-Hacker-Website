// Gemeinsamer Helper fuer alle CodeMirror-6-Editoren im Repo (12-Wochen-Notebooks via
// CodeCell.vue, JS-Spielewerkstatt via JsCodeCell.vue) - .fill()/.inputValue() funktionieren
// dort nicht, da es keine <textarea> ist. insertText() statt type(), damit CodeMirrors
// Auto-Indent literale "\n"-Zeichen in mehrzeiligem Test-Code nicht zusaetzlich einrueckt.
export async function setCodeMirrorContent(cmHost, code) {
  const content = cmHost.locator('.cm-content');
  await content.click();
  await content.press('ControlOrMeta+a');
  await content.press('Backspace');
  await content.page().keyboard.insertText(code);
}

// Bewegt die Maus praezise ueber einen Textabschnitt im Editor (z.B. fuer hoverTooltip-Checks in
// JsCodeCell.vue). `.hover()` auf einer Text-Locator-Suche trifft oft die ganze Zeile statt nur
// das gesuchte Wort, weil CodeMirror Tokens nicht zwingend in eigene DOM-Spans packt - das
// DOM-Range-API liefert die exakte Pixel-Position des gesuchten Substrings.
export async function hoverOverCodeMirrorText(cmContentLocator, text) {
  const page = cmContentLocator.page();
  const handle = await cmContentLocator.elementHandle();
  const rect = await page.evaluate(
    ({ el, needle }) => {
      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      let node;
      while ((node = walker.nextNode())) {
        const idx = node.textContent.indexOf(needle);
        if (idx !== -1) {
          const range = document.createRange();
          range.setStart(node, idx);
          range.setEnd(node, idx + needle.length);
          const r = range.getBoundingClientRect();
          return { x: r.x, y: r.y, width: r.width, height: r.height };
        }
      }
      return null;
    },
    { el: handle, needle: text }
  );
  if (!rect) throw new Error(`hoverOverCodeMirrorText: "${text}" nicht im Editor gefunden`);
  const cx = rect.x + rect.width / 2;
  const cy = rect.y + rect.height / 2;
  // Zwei Bewegungen statt einer: CodeMirrors Hover-Erkennung reagiert auf ein "mousemove"-Event
  // an der Zielposition, ein direkter Sprung ohne vorherige Bewegung wird manchmal nicht als
  // Hover-Beginn gewertet.
  await page.mouse.move(cx, cy);
  await page.mouse.move(cx + 0.1, cy);
}
