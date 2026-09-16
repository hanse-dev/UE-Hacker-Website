<template>
  <div class="jupyter-notebook">
    <!-- Controls bar -->
    <div class="notebook-controls-bar">
      <button @click="initializeKernel" :disabled="kernelReady" class="btn-kernel">
        {{ kernelReady ? t('jupyter.ready') : t('jupyter.init') }}
      </button>
      <button @click="runAllCells" :disabled="!kernelReady" class="btn-run-all">
        {{ t('jupyter.runAll') }}
      </button>
      <a :href="notebookUrl" :download="downloadName || true" class="btn-download">
        ⬇ .py
      </a>
    </div>

    <div v-if="loading" class="loading">{{ t('jupyter.loading') }}</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="notebook-cells">
      <div
        v-for="(cell, index) in cells"
        :key="index"
        :id="`cell-${index}`"
        :class="['cell', `cell-${cell.cell_type}`]"
      >
        <div v-if="cell.cell_type === 'markdown'" class="cell-markdown">
          <div v-html="renderMarkdown(cell.source)"></div>
        </div>

        <div v-else-if="cell.cell_type === 'code'" class="cell-code">
          <div class="code-header">
            <span class="cell-label">In [{{ index + 1 }}]</span>
            <button @click="runCell(index)" :disabled="!kernelReady" class="btn-run-cell">
              {{ t('jupyter.runCell') }}
            </button>
          </div>
          <CodeCell v-model="cell.source" />
          <div v-if="cellOutputs[index]" class="cell-output">
            <div v-if="cellOutputs[index].status === 'running'" class="output-running">
              {{ t('jupyter.running') }}
            </div>
            <pre
              v-else-if="cellOutputs[index].status === 'success' && cellOutputs[index].text"
              class="output-stream"
            >{{ cellOutputs[index].text }}</pre>
            <pre
              v-else-if="cellOutputs[index].status === 'success'"
              class="output-empty"
            >{{ t('jupyter.noOutput') }}</pre>
            <pre
              v-else-if="cellOutputs[index].status === 'error'"
              class="output-error"
            >{{ cellOutputs[index].text }}</pre>
          </div>
          <div :id="`turtle-${index}`" class="turtle-canvas-container"></div>
        </div>
      </div>
    </div>

    <div class="kernel-status" v-if="kernelStatus">{{ kernelStatus }}</div>
  </div>
</template>

<script>
import { ref, watch, onMounted, onUnmounted } from 'vue';
import { marked } from 'marked';
import { usePyodide } from '../composables/usePyodide';
import { useLanguage } from '../composables/useLanguage.js';
import { PROGRESS_APPLIED_EVENT, touchSyncKey } from '../composables/useProgressSync.js';
import CodeCell from './CodeCell.vue';

const stateKey = (notebookPath) => `ue-hacker-notebook-state-${notebookPath}`;

const loadSavedState = (notebookPath) => {
  try {
    const raw = localStorage.getItem(stateKey(notebookPath));
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
};

const saveState = (notebookPath, cells, cellOutputs, originalSources) => {
  try {
    const key = stateKey(notebookPath);
    const payload = JSON.stringify({
      originals: originalSources,
      sources: cells.map(cell => cell.source),
      outputs: cellOutputs,
    });
    if (localStorage.getItem(key) === payload) return;
    localStorage.setItem(key, payload);
    touchSyncKey(key);
  } catch {
    /* localStorage voll oder deaktiviert */
  }
};

export default {
  name: 'JupyterNotebook',
  components: { CodeCell },
  props: {
    notebookPath: { type: String, required: true },
    notebookUrl:  { type: String, required: true },
    downloadName: { type: String, default: null },
    weekNumber:   { type: Number, required: true },
    variant:      { type: String, default: null },
    courseId:     { type: String, default: null },
  },
  setup(props) {
    const { t } = useLanguage();
    const cells       = ref([]);
    const cellOutputs = ref({});
    const loading     = ref(true);
    const error       = ref(null);
    let originalSources = [];

    const { kernelReady, kernelStatus, initializeKernel: initPyodide, runPython } = usePyodide();

    const renderMarkdown = (source) => {
      const text = Array.isArray(source) ? source.join('') : source;
      return marked(text);
    };

    const loadNotebook = async () => {
      try {
        loading.value = true;
        const res = await fetch(props.notebookPath);
        if (!res.ok) throw new Error(t('jupyter.loadError'));
        const nb = await res.json();
        const loadedCells = (nb.cells || []).map(cell => ({
          ...cell,
          source: Array.isArray(cell.source) ? cell.source.join('') : cell.source,
        }));

        originalSources = loadedCells.map(cell => cell.source);

        const saved = loadSavedState(props.notebookPath);
        const outputs = {};
        if (saved && saved.originals?.length === loadedCells.length) {
          loadedCells.forEach((cell, i) => {
            if (cell.cell_type !== 'code') return;
            const unchanged = saved.originals[i] === originalSources[i];
            if (!unchanged) return;
            cell.source = saved.sources[i];
            if (saved.outputs?.[i]) outputs[i] = saved.outputs[i];
          });
        }
        cellOutputs.value = outputs;

        cells.value = loadedCells;
      } catch (e) {
        error.value = t('jupyter.fetchError') + e.message;
      } finally {
        loading.value = false;
      }
    };

    /** Sync: nur gespeicherten Stand anwenden — kein erneutes Fetch (kein Blinken). */
    const applySyncedNotebookState = () => {
      if (!cells.value.length) return;
      const saved = loadSavedState(props.notebookPath);
      if (!saved || saved.originals?.length !== cells.value.length) return;

      let changed = false;
      const nextOutputs = { ...cellOutputs.value };
      cells.value.forEach((cell, i) => {
        if (cell.cell_type !== 'code') return;
        if (saved.originals[i] !== originalSources[i]) return;
        if (typeof saved.sources?.[i] === 'string' && cell.source !== saved.sources[i]) {
          cell.source = saved.sources[i];
          changed = true;
        }
        if (saved.outputs?.[i] && JSON.stringify(nextOutputs[i]) !== JSON.stringify(saved.outputs[i])) {
          nextOutputs[i] = saved.outputs[i];
          changed = true;
        }
      });
      if (changed) {
        cellOutputs.value = nextOutputs;
        cells.value = [...cells.value];
      }
    };

    const initializeKernel = async () => {
      try { await initPyodide(); }
      catch (e) { error.value = t('jupyter.initError'); }
    };

    const runCell = async (index) => {
      if (!kernelReady.value) return;
      const cell = cells.value[index];
      if (cell.cell_type !== 'code') return;
      const code = cell.source.trim();
      if (!code) {
        cellOutputs.value = { ...cellOutputs.value, [index]: null };
        return;
      }
      cellOutputs.value = { ...cellOutputs.value, [index]: { status: 'running' } };
      const result = await runPython(code, `turtle-${index}`);
      if (result.success) {
        cellOutputs.value = {
          ...cellOutputs.value,
          [index]: { status: 'success', text: result.output ?? '' },
        };
      } else {
        cellOutputs.value = {
          ...cellOutputs.value,
          [index]: { status: 'error', text: result.error || t('jupyter.unknownError') },
        };
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

    onMounted(() => {
      loadNotebook();
      initializeKernel();
      window.addEventListener(PROGRESS_APPLIED_EVENT, applySyncedNotebookState);
    });

    onUnmounted(() => {
      window.removeEventListener(PROGRESS_APPLIED_EVENT, applySyncedNotebookState);
    });

    watch([cells, cellOutputs], () => {
      if (cells.value.length) saveState(props.notebookPath, cells.value, cellOutputs.value, originalSources);
    }, { deep: true });

    return { cells, cellOutputs, loading, error, kernelReady, kernelStatus,
             renderMarkdown, initializeKernel, runCell, runAllCells, t };
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
  background: var(--primary-purple, #4a2274); color: white; border: none;
  padding: 6px 14px; border-radius: 6px; cursor: pointer;
  font-size: 0.85em; font-weight: 600; transition: background 0.15s;
}
.btn-kernel:hover:not(:disabled) { background: #3d1b5c; }
.btn-kernel:disabled { background: #28a745; cursor: default; }

.btn-run-all {
  background: var(--accent-orange, #ff9800); color: white; border: none;
  padding: 6px 14px; border-radius: 6px; cursor: pointer;
  font-size: 0.85em; font-weight: 600; transition: background 0.15s;
}
.btn-run-all:hover:not(:disabled) { background: #fb8c00; }
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
  font-size: 1.6em; margin: 0.3em 0 0.5em; color: var(--primary-purple, #4a2274);
  border-bottom: 3px solid var(--accent-yellow, #fdd835); padding-bottom: 0.25em;
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

.cell-code { background: #faf7fc; }

.code-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 5px 10px 5px 14px; background: #efe3f6; border-bottom: 1px solid #d9c7ea;
}
.cell-label { font-family: monospace; font-size: 0.75em; color: #7c5a94; }

.btn-run-cell {
  background: var(--accent-orange, #ff9800); color: white; border: none;
  padding: 3px 10px; border-radius: 4px; font-size: 0.78em;
  font-weight: 600; cursor: pointer; transition: background 0.15s;
}
.btn-run-cell:hover:not(:disabled) { background: #fb8c00; }
.btn-run-cell:disabled { opacity: 0.4; cursor: not-allowed; }

.cell-output {
  padding: 8px 14px; background: #fff;
  border-top: 1px solid #f3f4f6; min-height: 0;
}

.output-running { color: #9ca3af; font-style: italic; font-size: 0.85em; }
.output-empty { margin: 0; font-family: monospace; font-size: 13px; color: #9ca3af; font-style: italic; }
.output-stream {
  margin: 0; font-family: monospace; font-size: 13px;
  white-space: pre-wrap; color: #111827;
}
.output-error {
  margin: 0; font-family: monospace; font-size: 13px;
  white-space: pre-wrap; color: #dc2626;
  background: #fef2f2; padding: 8px; border-radius: 4px;
}

.turtle-canvas-container:empty { display: none; }
.turtle-canvas-container {
  margin-top: 8px;
}
.turtle-canvas-container :deep(canvas) {
  display: block;
  max-width: 100%;
  border-radius: 4px;
}

.kernel-status {
  position: fixed; bottom: 20px; right: 20px;
  background: #1f2937; color: white; padding: 8px 16px;
  border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  font-size: 0.85em; z-index: 1000;
}
</style>
