<template>
  <div class="jupyter-notebook">
    <!-- Controls bar -->
    <div class="notebook-controls-bar">
      <button @click="initializeKernel" :disabled="kernelReady" class="btn-kernel">
        {{ kernelReady ? '✓ Python bereit' : 'Python initialisieren' }}
      </button>
      <button @click="runAllCells" :disabled="!kernelReady" class="btn-run-all">
        ▶ Alle ausführen
      </button>
      <a :href="notebookUrl" download class="btn-download">
        ⬇ .ipynb
      </a>
    </div>

    <div v-if="loading" class="loading">Lade Notebook…</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="notebook-cells">
      <div
        v-for="(cell, index) in cells"
        :key="index"
        :class="['cell', `cell-${cell.cell_type}`]"
      >
        <div v-if="cell.cell_type === 'markdown'" class="cell-markdown">
          <div v-html="renderMarkdown(cell.source)"></div>
        </div>

        <div v-else-if="cell.cell_type === 'code'" class="cell-code">
          <div class="code-header">
            <span class="cell-label">In [{{ index + 1 }}]</span>
            <button @click="runCell(index)" :disabled="!kernelReady" class="btn-run-cell">
              ▶ Ausführen
            </button>
          </div>
          <textarea
            :id="`code-${index}`"
            class="code-editor"
            spellcheck="false"
            v-model="cell.source"
            rows="5"
          ></textarea>
          <div :id="`output-${index}`" class="cell-output"></div>
        </div>
      </div>
    </div>

    <div class="kernel-status" v-if="kernelStatus">{{ kernelStatus }}</div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { marked } from 'marked';
import { usePyodide } from '../composables/usePyodide';

export default {
  name: 'JupyterNotebook',
  props: {
    notebookPath: { type: String, required: true },
    notebookUrl:  { type: String, required: true },
    weekNumber:   { type: Number, required: true },
    variant:      { type: String, default: null },
    courseId:     { type: String, default: null },
  },
  setup(props) {
    const cells   = ref([]);
    const loading = ref(true);
    const error   = ref(null);

    const { kernelReady, kernelStatus, initializeKernel: initPyodide, runPython } = usePyodide();

    const renderMarkdown = (source) => {
      const text = Array.isArray(source) ? source.join('') : source;
      return marked(text);
    };

    const loadNotebook = async () => {
      try {
        loading.value = true;
        const res = await fetch(props.notebookPath);
        if (!res.ok) throw new Error('Notebook konnte nicht geladen werden');
        const nb = await res.json();
        cells.value = (nb.cells || []).map(cell => ({
          ...cell,
          source: Array.isArray(cell.source) ? cell.source.join('') : cell.source,
        }));
      } catch (e) {
        error.value = 'Fehler beim Laden: ' + e.message;
      } finally {
        loading.value = false;
      }
    };

    const initializeKernel = async () => {
      try { await initPyodide(); }
      catch (e) { error.value = 'Python-Start fehlgeschlagen – Seite neu laden.'; }
    };

    const escapeHtml = (text) => {
      const d = document.createElement('div');
      d.textContent = text;
      return d.innerHTML;
    };

    const runCell = async (index) => {
      if (!kernelReady.value) return;
      const cell = cells.value[index];
      if (cell.cell_type !== 'code') return;
      const code = cell.source.trim();
      const out  = document.getElementById(`output-${index}`);
      if (!out) return;
      if (!code) { out.innerHTML = ''; return; }
      out.innerHTML = '<div class="output-running">Wird ausgeführt…</div>';
      const result = await runPython(code);
      if (result.success) {
        out.innerHTML = result.output?.trim()
          ? `<pre class="output-stream">${escapeHtml(result.output)}</pre>`
          : '';
      } else {
        out.innerHTML = `<pre class="output-error">${escapeHtml(result.error)}</pre>`;
      }
    };

    const runAllCells = async () => {
      if (!kernelReady.value) return;
      for (let i = 0; i < cells.value.length; i++) {
        if (cells.value[i].cell_type === 'code') {
          await runCell(i);
          await new Promise(r => setTimeout(r, 100));
        }
      }
    };

    onMounted(loadNotebook);

    return { cells, loading, error, kernelReady, kernelStatus,
             renderMarkdown, initializeKernel, runCell, runAllCells };
  },
};
</script>

<style scoped>
.jupyter-notebook {
  border: 1px solid #e5e7eb;
  border-top: none;
  border-radius: 0 0 8px 8px;
  background: white;
  overflow: hidden;
}

/* Controls bar */
.notebook-controls-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: #f9fafb;
  border-bottom: 1px solid #e5e7eb;
}

.btn-kernel {
  background: #ef4444; color: white; border: none;
  padding: 6px 14px; border-radius: 6px; cursor: pointer;
  font-size: 0.85em; font-weight: 600; transition: background 0.15s;
}
.btn-kernel:hover:not(:disabled) { background: #dc2626; }
.btn-kernel:disabled { background: #22c55e; cursor: default; }

.btn-run-all {
  background: #3b82f6; color: white; border: none;
  padding: 6px 14px; border-radius: 6px; cursor: pointer;
  font-size: 0.85em; font-weight: 600; transition: background 0.15s;
}
.btn-run-all:hover:not(:disabled) { background: #2563eb; }
.btn-run-all:disabled { opacity: 0.4; cursor: not-allowed; }

.btn-download {
  margin-left: auto; background: transparent; color: #6b7280;
  border: 1px solid #d1d5db; padding: 5px 12px; border-radius: 6px;
  text-decoration: none; font-size: 0.8em; transition: all 0.15s;
}
.btn-download:hover { background: #f3f4f6; color: #374151; }

/* Status / loading */
.loading { padding: 30px; text-align: center; color: #9ca3af; font-size: 0.9em; }
.error {
  padding: 16px; color: #dc2626; background: #fef2f2;
  border: 1px solid #fecaca; margin: 12px; border-radius: 6px; font-size: 0.9em;
}

/* Cells */
.notebook-cells { display: flex; flex-direction: column; }

.cell { border-bottom: 1px solid #f3f4f6; }
.cell:last-child { border-bottom: none; }

.cell-markdown { padding: 18px 22px; }

.cell-markdown :deep(h1) {
  font-size: 1.6em; margin: 0.3em 0 0.5em;
  border-bottom: 2px solid #fbbf24; padding-bottom: 0.25em;
}
.cell-markdown :deep(h2) { font-size: 1.25em; margin: 1em 0 0.4em; color: #1f2937; }
.cell-markdown :deep(h3) { font-size: 1.05em; margin: 0.8em 0 0.3em; color: #374151; }
.cell-markdown :deep(p) { line-height: 1.65; margin: 0 0 0.75em; }
.cell-markdown :deep(ul), .cell-markdown :deep(ol) { padding-left: 1.5em; margin: 0.5em 0; }
.cell-markdown :deep(li) { margin-bottom: 0.25em; line-height: 1.6; }
.cell-markdown :deep(code) {
  background: #f3f4f6; padding: 1px 5px; border-radius: 3px;
  font-family: 'Courier New', monospace; font-size: 0.88em;
}
.cell-markdown :deep(pre) {
  background: #1e1e1e; color: #d4d4d4; padding: 14px 16px;
  border-radius: 6px; overflow-x: auto; margin: 0.75em 0;
}
.cell-markdown :deep(pre code) { background: none; padding: 0; color: inherit; font-size: 0.9em; }
.cell-markdown :deep(table) { width: 100%; border-collapse: collapse; margin: 0.75em 0; font-size: 0.9em; }
.cell-markdown :deep(th) { background: #f9fafb; font-weight: 600; }
.cell-markdown :deep(th), .cell-markdown :deep(td) {
  border: 1px solid #e5e7eb; padding: 7px 12px; text-align: left;
}
.cell-markdown :deep(blockquote) {
  border-left: 3px solid #d1d5db; padding-left: 14px;
  margin: 0.75em 0; color: #6b7280; font-style: italic;
}

.cell-code { background: #fafafa; }

.code-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 5px 10px; background: #f3f4f6; border-bottom: 1px solid #e5e7eb;
}
.cell-label { font-family: monospace; font-size: 0.75em; color: #9ca3af; }

.btn-run-cell {
  background: #22c55e; color: white; border: none;
  padding: 3px 10px; border-radius: 4px; font-size: 0.78em;
  font-weight: 600; cursor: pointer; transition: background 0.15s;
}
.btn-run-cell:hover:not(:disabled) { background: #16a34a; }
.btn-run-cell:disabled { opacity: 0.4; cursor: not-allowed; }

.code-editor {
  width: 100%; min-height: 80px; padding: 12px 14px;
  background: #ffffff; border: none;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 13.5px; line-height: 1.55; color: #1f2937;
  resize: vertical; overflow: auto;
  white-space: pre; word-wrap: normal;
  box-sizing: border-box;
}
.code-editor:focus { outline: 2px solid #3b82f6; outline-offset: -2px; }

.cell-output {
  padding: 8px 14px; background: #fff;
  border-top: 1px solid #f3f4f6; min-height: 0;
}
.cell-output:empty { display: none; }

.output-running { color: #9ca3af; font-style: italic; font-size: 0.85em; }
.output-stream {
  margin: 0; font-family: monospace; font-size: 13px;
  white-space: pre-wrap; color: #111827;
}
.output-error {
  margin: 0; font-family: monospace; font-size: 13px;
  white-space: pre-wrap; color: #dc2626;
  background: #fef2f2; padding: 8px; border-radius: 4px;
}

.kernel-status {
  position: fixed; bottom: 20px; right: 20px;
  background: #1f2937; color: white; padding: 8px 16px;
  border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  font-size: 0.85em; z-index: 1000;
}
</style>
