<template>
  <div ref="host" class="cm-host"></div>
</template>

<script>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue';
import { EditorView, basicSetup } from 'codemirror';
import { EditorState, Prec } from '@codemirror/state';
import { keymap, hoverTooltip } from '@codemirror/view';
import { indentUnit } from '@codemirror/language';
import { indentWithTab } from '@codemirror/commands';
import { javascript, localCompletionSource, scopeCompletionSource } from '@codemirror/lang-javascript';
import { autocompletion, acceptCompletion } from '@codemirror/autocomplete';

// Kurzsignaturen fuer genau die Canvas-/Browser-API, die in den Lektionen dieses Kurses vorkommt
// (siehe content/js-spielewerkstatt/). Keine generische Typableitung (das koennte nur ein echter
// TypeScript-Sprachserver, weit ausserhalb des Rahmens hier) - eine handkuratierte Liste reicht,
// weil die API-Oberflaeche des Kurses klein und fest ist.
const API_DOCS = {
  getContext: "canvas.getContext('2d')\nGibt den Zeichenkontext des Canvas zurück.",
  getElementById: 'document.getElementById(id)\nSucht ein Element anhand seiner ID im Dokument.',
  addEventListener: "element.addEventListener(ereignis, funktion)\nRuft funktion auf, sobald ereignis eintritt (z.B. 'keydown').",
  requestAnimationFrame: 'requestAnimationFrame(funktion)\nRuft funktion kurz vor dem nächsten Bild auf – Grundbaustein jeder Animationsschleife.',
  fillRect: 'ctx.fillRect(x, y, breite, hoehe)\nZeichnet ein gefülltes Rechteck.',
  strokeRect: 'ctx.strokeRect(x, y, breite, hoehe)\nZeichnet den Rahmen eines Rechtecks.',
  clearRect: 'ctx.clearRect(x, y, breite, hoehe)\nLöscht einen Bereich des Canvas (z.B. vor jedem neuen Frame).',
  fillStyle: 'ctx.fillStyle = farbe\nSetzt die Füllfarbe für die nächste Zeichnung, z.B. "red" oder "#ff0000".',
  strokeStyle: 'ctx.strokeStyle = farbe\nSetzt die Rahmenfarbe für die nächste Zeichnung.',
  beginPath: 'ctx.beginPath()\nStartet einen neuen Zeichenpfad.',
  arc: 'ctx.arc(x, y, radius, startWinkel, endWinkel)\nZeichnet einen Kreisbogen (für einen ganzen Kreis: 0 bis Math.PI * 2).',
  fill: 'ctx.fill()\nFüllt den aktuellen Pfad mit der Farbe aus fillStyle.',
  fillText: 'ctx.fillText(text, x, y)\nSchreibt Text auf das Canvas.',
  font: 'ctx.font = größe_und_schriftart\nSetzt Schriftgröße/-art für fillText, z.B. "20px sans-serif".',
  floor: 'Math.floor(zahl)\nRundet zahl immer nach unten ab (z.B. 3.7 → 3).',
  random: 'Math.random()\nGibt eine Zufallszahl zwischen 0 (einschließlich) und 1 (ausschließlich) zurück.',
  log: 'console.log(wert1, wert2, ...)\nGibt Werte in der Ausgabe unter dem Code aus.',
};

function jsApiHoverTooltip() {
  return hoverTooltip((view, pos) => {
    const line = view.state.doc.lineAt(pos);
    let start = pos;
    let end = pos;
    while (start > line.from && /\w/.test(line.text[start - line.from - 1])) start--;
    while (end < line.to && /\w/.test(line.text[end - line.from])) end++;
    if (start === end) return null;
    const word = line.text.slice(start - line.from, end - line.from);
    const doc = API_DOCS[word];
    if (!doc) return null;
    return {
      pos: start,
      end,
      above: true,
      create() {
        const dom = document.createElement('div');
        dom.className = 'cm-api-hover';
        dom.textContent = doc;
        return { dom };
      },
    };
  });
}

// Gleiches Autocomplete/Tab-Verhalten wie CodeCell.vue (12-Wochen-Notebooks), nur mit JS statt
// Python. scopeCompletionSource(scope) schlaegt echte Browser-Globals vor (document, console,
// Math, requestAnimationFrame, ...) - genau die Namen, die im Sandbox-Code gebraucht werden.
//
// scopeCompletionSource kann KEINE Typen ableiten - "ctx." haette ohne Weiteres keine
// Vorschlaege, weil `ctx` nur eine lokale Variable ist, deren Wert (ein CanvasRenderingContext2D)
// nirgends statisch bekannt ist. Fix: ein eigenes Scope-Objekt, das per Prototyp-Kette alle
// globalThis-Namen erbt UND zusaetzlich `ctx`/`canvas` als eigene Properties traegt, die auf einen
// echten (nie ans DOM gehaengten) Canvas-Context zeigen - genau die Namen, die jede Aufgabe in
// diesem Kurs immer verwendet (siehe Content-Konvention in content/js-spielewerkstatt/).
function buildCompletionScope() {
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  return Object.assign(Object.create(globalThis), { canvas, ctx });
}
export default {
  name: 'JsCodeCell',
  props: {
    modelValue: { type: String, default: '' },
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const host = ref(null);
    let view = null;
    let applyingExternal = false;

    onMounted(() => {
      const state = EditorState.create({
        doc: props.modelValue,
        extensions: [
          basicSetup,
          // Tab: erst versuchen, einen offenen Autocomplete-Vorschlag zu uebernehmen
          // (wie in VS Code) - nur wenn kein Popup offen ist, faellt es auf Einruecken zurueck.
          Prec.highest(keymap.of([
            { key: 'Tab', run: acceptCompletion },
            indentWithTab,
          ])),
          indentUnit.of('  '),
          javascript(),
          autocompletion({ override: [localCompletionSource, scopeCompletionSource(buildCompletionScope())] }),
          jsApiHoverTooltip(),
          EditorView.updateListener.of((update) => {
            if (update.docChanged && !applyingExternal) {
              emit('update:modelValue', update.state.doc.toString());
            }
          }),
          EditorView.theme({
            '&': { fontSize: '13.5px' },
            '.cm-content': {
              fontFamily: "'Courier New', Consolas, Monaco, monospace",
              padding: '8px 0',
            },
            // Mindestens ~6 Zeilen sichtbar, auch wenn die Zelle leer ist - eine leere
            // "hier Code schreiben"-Stelle soll klar als Coding-Bereich erkennbar bleiben.
            '.cm-scroller': { minHeight: '140px' },
          }),
        ],
      });
      view = new EditorView({ state, parent: host.value });
    });

    watch(() => props.modelValue, (next) => {
      if (!view) return;
      const current = view.state.doc.toString();
      if (current === next) return;
      applyingExternal = true;
      view.dispatch({ changes: { from: 0, to: current.length, insert: next } });
      applyingExternal = false;
    });

    onBeforeUnmount(() => {
      if (view) view.destroy();
    });

    return { host };
  },
};
</script>

<style scoped>
.cm-host {
  border: 1px solid #d9c7ea;
  border-radius: 6px;
  margin-bottom: 12px;
  background: #f7f1fb;
  overflow: hidden;
}
.cm-host:focus-within {
  border-color: var(--primary-purple, #4a2274);
  box-shadow: 0 0 0 1px var(--primary-purple, #4a2274);
}
.cm-host :deep(.cm-editor) { outline: none; background: transparent; }
.cm-host :deep(.cm-scroller) { overflow: auto; }
.cm-host :deep(.cm-gutters) {
  background: #efe3f6;
  border-right: 1px solid #d9c7ea;
  color: #7c5a94;
}
</style>

<style>
/* Unscoped: CodeMirror haengt Tooltips als eigenes DOM-Element ausserhalb des Vue-Templates an
   (meist direkt an document.body) - eine gescopte Regel wuerde es nie erreichen. */
.cm-api-hover {
  max-width: 320px;
  padding: 6px 10px;
  background: #2b1a3d;
  color: #f4ecfa;
  border-radius: 6px;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 12.5px;
  line-height: 1.5;
  white-space: pre-line;
}
</style>
