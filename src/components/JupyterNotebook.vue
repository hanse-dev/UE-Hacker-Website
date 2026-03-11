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

      <!-- Missionen-Panel (nur für Python 12-Wochen-Kurs) – ein-/ausklappbar -->
      <div v-if="missionen.length > 0" class="missionen-panel">
        <div class="missionen-panel-header" @click="missionenExpanded = !missionenExpanded">
          <h4>🎯 Missionen & Belohnungen – Woche {{ weekNumber }}</h4>
          <span class="missionen-toggle">{{ missionenExpanded ? '−' : '+' }}</span>
        </div>
        <div v-show="missionenExpanded" class="missionen-panel-content">
          <p class="missionen-hint">Hast du eine Mission gemeistert? Klicke auf „Punkte einlösen“! Vergriffen? Nutze „Rückgängig“.</p>
          <div class="missionen-list">
            <div
              v-for="m in missionen"
              :key="m.id"
              class="mission-item"
              :class="{ claimed: isClaimed(m.id) }"
            >
              <span class="mission-label">{{ m.label }}:</span>
              <span class="mission-info">{{ m.points }} {{ pointUnit }} + {{ m.item }}</span>
              <div class="mission-actions">
                <button
                  v-if="!isClaimed(m.id)"
                  @click.stop="claimMission(m)"
                  class="btn-claim"
                >
                  ✨ Punkte einlösen
                </button>
                <template v-else>
                  <span class="mission-claimed">✅ Eingelöst</span>
                  <button
                    @click.stop="unclaimMission(m)"
                    class="btn-unclaim"
                    title="Rückgängig machen"
                  >
                    ↩ Rückgängig
                  </button>
                </template>
              </div>
            </div>
          </div>
        </div>
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
import { ref, onMounted, computed } from 'vue';
import { marked } from 'marked';
import { useFortschritt } from '../composables/useFortschritt';
import { usePyodide } from '../composables/usePyodide';

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
    variant: {
      type: String,
      default: null,
    },
    courseId: {
      type: String,
      default: null,
    },
  },
  setup(props) {
    const cells = ref([]);
    const loading = ref(true);
    const error = ref(null);
    const isExpanded = ref(false);
    const rewardsManifest = ref(null);

    const { kernelReady, kernelStatus, initializeKernel: initPyodide, runPython } = usePyodide();

    const missionenExpanded = ref(true);
    const { claimMission: doClaimMission, unclaimMission: doUnclaimMission, isClaimed: checkClaimed } = useFortschritt();

    const pointUnits = { abenteuer: 'XP', pferde: 'Huf-Punkte', scifi: 'Cyber Credits' };
    const pointUnit = computed(() => pointUnits[props.variant] || 'Punkte');

    const missionen = computed(() => {
      if (!rewardsManifest.value || !props.variant || props.courseId !== 'python-12-wochen-grundkurs') {
        return [];
      }
      const course = rewardsManifest.value[props.courseId];
      if (!course) return [];
      const variantData = course[props.variant];
      if (!variantData) return [];
      const weekData = variantData[String(props.weekNumber)];
      if (!weekData) return [];
      const missions = (weekData.missions || []).map((m, i) => ({ ...m, label: `Mission ${i + 1}` }));
      const bosses = (weekData.bossQuests || []).map((m, i) => ({ ...m, label: `Boss-Quest ${i + 1}` }));
      return [...missions, ...bosses];
    });

    const isClaimed = (missionId) => checkClaimed(props.variant, missionId);

    const claimMission = (m) => {
      doClaimMission(props.variant, m.id, m.points, m.item, m.label);
    };

    const unclaimMission = (m) => {
      doUnclaimMission(props.variant, m.id);
    };

    const loadRewardsManifest = async () => {
      try {
        const res = await fetch('/rewards-manifest.json');
        if (res.ok) rewardsManifest.value = await res.json();
      } catch (e) {
        console.error('Rewards-Manifest konnte nicht geladen werden:', e);
      }
    };

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
      try {
        await initPyodide();
      } catch (e) {
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

      outputElement.innerHTML = '<div class="output-running">Wird ausgeführt...</div>';

      const result = await runPython(code);

      if (result.success) {
        if (result.output && result.output.trim()) {
          outputElement.innerHTML = `<pre class="output-stream">${escapeHtml(result.output)}</pre>`;
        } else {
          outputElement.innerHTML = '';
        }
      } else {
        outputElement.innerHTML = `<pre class="output-error">${escapeHtml(result.error)}</pre>`;
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
      loadRewardsManifest();
    });

    return {
      missionenExpanded,
      missionen,
      pointUnit,
      isClaimed,
      claimMission,
      unclaimMission,
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

/* Missionen Panel */
.missionen-panel {
  background: linear-gradient(135deg, #fef9e7 0%, #fdebd0 100%);
  border: 2px solid #ffd700;
  border-radius: 8px;
  margin-bottom: 20px;
  overflow: hidden;
}

.missionen-panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 20px;
  cursor: pointer;
  user-select: none;
}

.missionen-panel-header:hover {
  background: rgba(255, 255, 255, 0.5);
}

.missionen-panel-header h4 {
  margin: 0;
  color: #333;
  font-size: 1.1em;
}

.missionen-toggle {
  font-size: 1.3em;
  font-weight: bold;
  color: #666;
}

.missionen-panel-content {
  padding: 0 20px 16px 20px;
  border-top: 1px solid rgba(255, 215, 0, 0.5);
}

.missionen-hint {
  margin: 8px 0 12px 0;
  font-size: 0.9em;
  color: #666;
}

.missionen-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.mission-item {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 6px;
  border: 1px solid #eee;
}

.mission-item.claimed {
  background: #e8f5e9;
  border-color: #c8e6c9;
}

.mission-label {
  font-weight: 600;
  color: #555;
  min-width: 90px;
}

.mission-info {
  font-size: 0.95em;
  color: #333;
  flex: 1;
}

.mission-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-claim {
  background: #ffd700;
  color: #333;
  border: none;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 0.9em;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-claim:hover {
  background: #ffed4e;
  transform: translateY(-1px);
}

.btn-unclaim {
  background: transparent;
  color: #666;
  border: 1px solid #ccc;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.85em;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-unclaim:hover {
  background: #ffebee;
  color: #c62828;
  border-color: #ef9a9a;
}

.mission-claimed {
  font-size: 0.9em;
  color: #2e7d32;
  font-weight: 600;
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
