<template>
  <div class="jupyter-notebook">
    <!-- Toggle Button -->
    <div class="notebook-toggle">
      <button @click="isExpanded = !isExpanded" class="btn-toggle">
        <span class="toggle-icon">{{ isExpanded ? '▼' : '▶' }}</span>
        <span class="toggle-text">
          {{ isExpanded ? 'Interaktives Notebook einklappen' : 'Interaktives Notebook öffnen' }}
        </span>
        <span class="toggle-badge">Live Code Editor</span>
      </button>
      <a :href="notebookUrl" download class="btn-download-small">
        ⬇ Woche {{ weekNumber }} Notebook
      </a>
    </div>

    <!-- Expandable Content -->
    <div v-if="isExpanded" class="notebook-content">
      <!-- Instructions -->
      <div class="notebook-instructions">
        <h4>📝 So funktioniert's:</h4>
        <ol>
          <li>Klicke auf <strong>"Python initialisieren"</strong> (lädt Python im Browser, ~30 Sek.)</li>
          <li>Führe einzelne Code-Zellen mit <strong>"▶ Ausführen"</strong> aus</li>
          <li>Oder nutze <strong>"Alle Zellen ausführen"</strong> für das gesamte Notebook</li>
          <li>Alle Änderungen bleiben lokal in deinem Browser</li>
        </ol>
      </div>

      <!-- Controls -->
      <div class="notebook-header">
        <div class="notebook-controls">
          <button @click="initializeKernel" :disabled="kernelReady" class="btn-kernel">
            {{ kernelReady ? '✓ Python bereit' : 'Python initialisieren' }}
          </button>
          <button @click="runAllCells" :disabled="!kernelReady" class="btn-run-all">
            ▶ Alle Zellen ausführen
          </button>
        </div>
      </div>

      <div v-if="loading" class="loading">
        Lade Notebook...
      </div>

      <div v-else-if="error" class="error">
        {{ error }}
      </div>

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
            <span class="cell-label">Code-Zelle {{ index + 1 }}</span>
            <button
              @click="runCell(index)"
              :disabled="!kernelReady"
              class="btn-run-cell"
            >
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
          <div
            :id="`output-${index}`"
            class="cell-output"
          ></div>
        </div>
      </div>
      </div>

      <div class="kernel-status" v-if="kernelStatus">
        {{ kernelStatus }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { marked } from 'marked';

export default {
  name: 'JupyterNotebook',
  props: {
    notebookPath: {
      type: String,
      required: true,
    },
    notebookUrl: {
      type: String,
      required: true,
    },
    weekNumber: {
      type: Number,
      required: true,
    },
  },
  setup(props) {
    const cells = ref([]);
    const loading = ref(true);
    const error = ref(null);
    const kernelReady = ref(false);
    const kernelStatus = ref('');
    const pyodide = ref(null);
    const isExpanded = ref(false);

    const renderMarkdown = (source) => {
      const text = Array.isArray(source) ? source.join('') : source;
      return marked(text);
    };

    const getSourceText = (source) => {
      return Array.isArray(source) ? source.join('') : source;
    };

    const loadNotebook = async () => {
      try {
        loading.value = true;
        const response = await fetch(props.notebookPath);
        if (!response.ok) {
          throw new Error('Notebook konnte nicht geladen werden');
        }
        const notebook = await response.json();
        // Convert source arrays to strings for v-model
        cells.value = (notebook.cells || []).map(cell => ({
          ...cell,
          source: Array.isArray(cell.source) ? cell.source.join('') : cell.source
        }));
        loading.value = false;
      } catch (e) {
        console.error('Error loading notebook:', e);
        error.value = 'Fehler beim Laden des Notebooks: ' + e.message;
        loading.value = false;
      }
    };

    const initializeKernel = async () => {
      if (kernelReady.value) return;

      try {
        kernelStatus.value = 'Python-Kernel wird gestartet (kann bis zu 30 Sekunden dauern)...';

        // Load Pyodide from CDN
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js';

        await new Promise((resolve, reject) => {
          script.onload = resolve;
          script.onerror = reject;
          document.head.appendChild(script);
        });

        // Initialize Pyodide
        pyodide.value = await window.loadPyodide({
          indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/',
        });

        // Redirect stdout and setup input() function
        await pyodide.value.runPythonAsync(`
import sys
from io import StringIO
import builtins
from js import window

# Replace input() with JavaScript prompt
def browser_input(prompt=''):
    result = window.prompt(str(prompt))
    return result if result is not None else ''

builtins.input = browser_input
        `);

        kernelReady.value = true;
        kernelStatus.value = 'Python ist bereit!';

        setTimeout(() => {
          kernelStatus.value = '';
        }, 3000);
      } catch (e) {
        console.error('Error initializing Pyodide:', e);
        kernelStatus.value = 'Fehler beim Starten des Kernels: ' + e.message;
        error.value = 'Konnte Python-Kernel nicht starten. Bitte Seite neu laden.';
      }
    };

    const runCell = async (index) => {
      if (!kernelReady.value) {
        alert('Bitte zuerst Python initialisieren!');
        return;
      }

      const cell = cells.value[index];
      if (cell.cell_type !== 'code') return;

      const code = cell.source.trim();
      const outputElement = document.getElementById(`output-${index}`);

      if (!outputElement) return;

      // Skip empty cells
      if (!code) {
        outputElement.innerHTML = '';
        return;
      }

      try {
        outputElement.innerHTML = '<div class="output-running">Wird ausgeführt...</div>';

        // Capture stdout and execute code
        const captureCode = `
import sys
from io import StringIO

_stdout_capture = StringIO()
_old_stdout = sys.stdout
sys.stdout = _stdout_capture

try:
${code.split('\n').map(line => '    ' + line).join('\n')}
    pass  # Ensure try block is never empty
finally:
    sys.stdout = _old_stdout

_output = _stdout_capture.getvalue()
`;

        await pyodide.value.runPythonAsync(captureCode);
        const output = pyodide.value.globals.get('_output');

        if (output && output.trim()) {
          outputElement.innerHTML = `<pre class="output-stream">${escapeHtml(output)}</pre>`;
        } else {
          outputElement.innerHTML = '';
        }
      } catch (e) {
        console.error('Error running cell:', e);
        outputElement.innerHTML = `<pre class="output-error">${escapeHtml(e.message)}</pre>`;
      }
    };

    const runAllCells = async () => {
      if (!kernelReady.value) {
        alert('Bitte zuerst Python initialisieren!');
        return;
      }

      for (let i = 0; i < cells.value.length; i++) {
        if (cells.value[i].cell_type === 'code') {
          await runCell(i);
          // Small delay between cells
          await new Promise(resolve => setTimeout(resolve, 100));
        }
      }
    };

    const escapeHtml = (text) => {
      const div = document.createElement('div');
      div.textContent = text;
      return div.innerHTML;
    };

    const setCellRef = () => {
      // Not needed anymore but keeping for compatibility
    };

    onMounted(() => {
      loadNotebook();
    });

    return {
      cells,
      loading,
      error,
      kernelReady,
      kernelStatus,
      isExpanded,
      renderMarkdown,
      getSourceText,
      initializeKernel,
      runCell,
      runAllCells,
      setCellRef,
    };
  },
};
</script>

<style scoped>
.jupyter-notebook {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0;
  margin-bottom: 30px;
}

/* Toggle Section */
.notebook-toggle {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 15px;
  padding: 15px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 8px;
  margin-bottom: 0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.btn-toggle {
  background: rgba(255, 255, 255, 0.95);
  color: #333;
  border: none;
  padding: 12px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.3s ease;
  flex: 1;
}

.btn-toggle:hover {
  background: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.toggle-icon {
  font-size: 14px;
  color: #667eea;
}

.toggle-text {
  flex: 1;
}

.toggle-badge {
  background: #ffd700;
  color: #333;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-download-small {
  background: rgba(255, 215, 0, 0.95);
  color: #333;
  border: none;
  padding: 10px 16px;
  border-radius: 6px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.btn-download-small:hover {
  background: #ffd700;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* Expandable Content */
.notebook-content {
  animation: slideDown 0.3s ease-out;
  background: #f8f9fa;
  border: 2px solid #667eea;
  border-top: none;
  border-radius: 0 0 8px 8px;
  padding: 20px;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Instructions */
.notebook-instructions {
  background: #fff;
  border-left: 4px solid #667eea;
  border-radius: 6px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.notebook-instructions h4 {
  margin-top: 0;
  margin-bottom: 15px;
  color: #667eea;
  font-size: 18px;
}

.notebook-instructions ol {
  margin: 0;
  padding-left: 25px;
}

.notebook-instructions li {
  margin-bottom: 10px;
  line-height: 1.6;
  color: #333;
}

.notebook-instructions strong {
  color: #667eea;
}

.notebook-header {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.notebook-controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}

.btn-kernel,
.btn-run-all,
.btn-run-cell {
  background: #ff4136;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: background 0.2s;
}

.btn-kernel:hover:not(:disabled),
.btn-run-all:hover:not(:disabled),
.btn-run-cell:hover:not(:disabled) {
  background: #e60000;
}

.btn-kernel:disabled,
.btn-run-all:disabled,
.btn-run-cell:disabled {
  background: #6c757d;
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-download {
  background: #ffd700;
  color: #333;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: background 0.2s;
  display: inline-block;
}

.btn-download:hover {
  background: #ffed4e;
}

.loading,
.error {
  padding: 20px;
  text-align: center;
  font-size: 16px;
}

.error {
  color: #dc3545;
  background: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 4px;
}

.notebook-cells {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.cell {
  border: 1px solid #dee2e6;
  border-radius: 4px;
  overflow: hidden;
  background: white;
}

.cell-markdown {
  padding: 20px;
}

.cell-markdown :deep(h1) {
  font-size: 2em;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  border-bottom: 2px solid #ffd700;
  padding-bottom: 0.3em;
}

.cell-markdown :deep(h2) {
  font-size: 1.5em;
  margin-top: 0.8em;
  margin-bottom: 0.5em;
  color: #333;
}

.cell-markdown :deep(h3) {
  font-size: 1.2em;
  margin-top: 0.6em;
  margin-bottom: 0.4em;
}

.cell-markdown :deep(ul),
.cell-markdown :deep(ol) {
  margin: 10px 0;
  padding-left: 30px;
}

.cell-markdown :deep(code) {
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}

.cell-code {
  background: #f8f9fa;
}

.code-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  background: #e9ecef;
  border-bottom: 1px solid #dee2e6;
}

.cell-label {
  font-family: monospace;
  color: #6c757d;
  font-weight: bold;
}

.btn-run-cell {
  padding: 4px 12px;
  font-size: 12px;
}

.code-editor {
  width: 100%;
  min-height: 120px;
  padding: 15px;
  background: #ffffff;
  border: none;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  resize: vertical;
  overflow: auto;
  white-space: pre;
  word-wrap: normal;
  word-break: normal;
}

.code-editor:focus {
  outline: 2px solid #667eea;
  outline-offset: -2px;
  background: #f9f9f9;
}

.cell-output {
  padding: 10px 15px;
  background: #fff;
  border-top: 1px solid #dee2e6;
  min-height: 20px;
}

.cell-output:empty {
  display: none;
}

.output-running {
  color: #6c757d;
  font-style: italic;
}

.output-stream,
.output-result {
  margin: 0;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  white-space: pre-wrap;
  color: #000;
}

.output-error {
  margin: 0;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  white-space: pre-wrap;
  color: #dc3545;
  background: #f8d7da;
  padding: 10px;
  border-radius: 4px;
}

.kernel-status {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #333;
  color: white;
  padding: 10px 20px;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  z-index: 1000;
}
</style>
