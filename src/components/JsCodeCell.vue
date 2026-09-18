<template>
  <div ref="host" class="cm-host"></div>
</template>

<script>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue';
import { EditorView, basicSetup } from 'codemirror';
import { EditorState, Prec } from '@codemirror/state';
import { keymap } from '@codemirror/view';
import { indentUnit } from '@codemirror/language';
import { indentWithTab } from '@codemirror/commands';
import { javascript, localCompletionSource, scopeCompletionSource } from '@codemirror/lang-javascript';
import { autocompletion, acceptCompletion } from '@codemirror/autocomplete';

// Gleiches Autocomplete/Tab-Verhalten wie CodeCell.vue (12-Wochen-Notebooks), nur mit JS statt
// Python. scopeCompletionSource(globalThis) schlaegt echte Browser-Globals vor (document,
// console, Math, requestAnimationFrame, ...) - genau die Namen, die im Sandbox-Code gebraucht
// werden.
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
          autocompletion({ override: [localCompletionSource, scopeCompletionSource(globalThis)] }),
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
