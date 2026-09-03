import { ref } from 'vue';

const PYODIDE_CDN = 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full';
const PYODIDE_SCRIPT = `${PYODIDE_CDN}/pyodide.js`;
const CELL_TIMEOUT_SECONDS = 5;
const CELL_TIMEOUT_MARKER = '__PYODIDE_CELL_TIMEOUT__';

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
import time
import ast
import builtins
from io import StringIO
from js import window

def browser_input(prompt=''):
    result = window.prompt(str(prompt))
    return result if result is not None else ''

builtins.input = browser_input


class _CellTimeout(BaseException):
    """Intern: wird geworfen, wenn eine Schleife ihr Zeitlimit überschreitet."""


class _LoopDeadlineGuard(ast.NodeTransformer):
    """Fügt vor jeden for/while-Schleifenkörper eine Deadline-Prüfung ein,
    damit Endlosschleifen nach einem Zeitlimit abgebrochen werden statt den
    Tab für immer einzufrieren."""

    def __init__(self, deadline_name):
        self._deadline_name = deadline_name

    def _guard(self, node):
        self.generic_visit(node)
        check = ast.parse(
            f"if time.time() > {self._deadline_name}:\\n    raise _CellTimeout()"
        ).body
        node.body = check + node.body
        return node

    def visit_For(self, node):
        return self._guard(node)

    def visit_While(self, node):
        return self._guard(node)


def _run_cell_with_guard(source, timeout_seconds=5):
    deadline_name = '__cell_deadline__'
    ns = globals()
    ns[deadline_name] = time.time() + timeout_seconds
    capture = StringIO()
    try:
        tree = ast.parse(source, filename='<cell>', mode='exec')
        tree = _LoopDeadlineGuard(deadline_name).visit(tree)
        ast.fix_missing_locations(tree)
        code = compile(tree, '<cell>', 'exec')

        old_stdout = sys.stdout
        sys.stdout = capture
        try:
            exec(code, ns)
        finally:
            sys.stdout = old_stdout
    except _CellTimeout:
        raise TimeoutError('${CELL_TIMEOUT_MARKER}')
    finally:
        ns.pop(deadline_name, None)
    return capture.getvalue()
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
      pyodideRef.value.globals.set('_cell_source', trimmed);
      const output = await pyodideRef.value.runPythonAsync(
        `_run_cell_with_guard(_cell_source, ${CELL_TIMEOUT_SECONDS})`
      );
      const outputStr = output != null ? String(output) : '';

      return { success: true, output: outputStr };
    } catch (e) {
      const message = e?.message || String(e);
      if (message.includes(CELL_TIMEOUT_MARKER)) {
        return {
          success: false,
          error: `Dein Code lief länger als ${CELL_TIMEOUT_SECONDS} Sekunden – vermutlich eine Endlosschleife. Prüfe deine Schleifenbedingung (ändert sich die Variable in der Schleife wirklich?).`,
        };
      }
      return { success: false, error: message };
    } finally {
      pyodideRef.value.globals.delete('_cell_source');
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
