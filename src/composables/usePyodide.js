import { ref } from 'vue';

const PYODIDE_CDN = 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full';
const PYODIDE_SCRIPT = `${PYODIDE_CDN}/pyodide.js`;

// Shared kernel state across all components (LessonView, JupyterNotebook, …)
const kernelReady = ref(false);
const kernelStatus = ref('');
const pyodideRef = ref(null);
let initPromise = null;

/**
 * Composable für Pyodide – Python im Browser.
 * Bietet Initialisierung und Code-Ausführung mit stdout-Capture.
 */
export function usePyodide() {
  const initializeKernel = async () => {
    if (kernelReady.value) return;
    if (initPromise) {
      await initPromise;
      return;
    }

    initPromise = (async () => {
      try {
        kernelStatus.value = 'Python-Kernel wird gestartet (kann bis zu 30 Sekunden dauern)...';

        if (!window.loadPyodide) {
          const script = document.createElement('script');
          script.src = PYODIDE_SCRIPT;
          await new Promise((resolve, reject) => {
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
          });
        }

        const pyodide = await window.loadPyodide({
          indexURL: `${PYODIDE_CDN}/`,
        });

        await pyodide.runPythonAsync(`
import sys
from io import StringIO
import builtins
from js import window

def browser_input(prompt=''):
    result = window.prompt(str(prompt))
    return result if result is not None else ''

builtins.input = browser_input
        `);

        pyodideRef.value = pyodide;
        kernelReady.value = true;
        kernelStatus.value = 'Python ist bereit!';

        setTimeout(() => {
          kernelStatus.value = '';
        }, 3000);
      } catch (e) {
        console.error('Error initializing Pyodide:', e);
        kernelStatus.value = 'Fehler beim Starten des Kernels: ' + e.message;
        initPromise = null;
        throw e;
      }
    })();

    await initPromise;
  };

  /**
   * Führt Python-Code aus und gibt stdout zurück.
   * @param {string} code - Python-Code
   * @returns {Promise<{ success: boolean, output?: string, error?: string }>}
   */
  const runPython = async (code) => {
    if (!kernelReady.value || !pyodideRef.value) {
      return { success: false, error: 'Python-Kernel nicht initialisiert. Bitte zuerst Python starten.' };
    }

    const trimmed = code.trim();
    if (!trimmed) {
      return { success: true, output: '' };
    }

    try {
      const captureCode = `
import sys
from io import StringIO

_stdout_capture = StringIO()
_old_stdout = sys.stdout
sys.stdout = _stdout_capture

try:
${trimmed.split('\n').map((line) => '    ' + line).join('\n')}
    pass
finally:
    sys.stdout = _old_stdout

_stdout_capture.getvalue()
`;

      const output = await pyodideRef.value.runPythonAsync(captureCode);
      const outputStr = output != null ? String(output) : '';

      return { success: true, output: outputStr };
    } catch (e) {
      return { success: false, error: e.message || String(e) };
    }
  };

  return {
    kernelReady,
    kernelStatus,
    pyodideRef,
    initializeKernel,
    runPython,
  };
}
