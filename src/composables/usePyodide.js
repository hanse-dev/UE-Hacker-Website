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
from js import window, document

def browser_input(prompt=''):
    result = window.prompt(str(prompt))
    return result if result is not None else ''

builtins.input = browser_input


def _install_turtle_shim():
    """Pyodide entfernt 'turtle' aus der Standardbibliothek (basiert auf
    tkinter, das im Browser keinen Anzeige-Server hat). Dieser Shim bildet
    die im Kurs tatsächlich genutzten turtle-Methoden auf ein <canvas>
    ab, das in den DOM-Container mit der ID window.__turtleContainerId
    gezeichnet wird (von JupyterNotebook.vue pro Zelle gesetzt)."""
    import math
    import types

    class _Screen:
        def __init__(self, container_id):
            self.width = 500
            self.height = 400
            self._bgcolor = 'white'
            self.container = document.getElementById(container_id) if container_id else None
            self.canvas = None
            self.ctx = None
            self._build_canvas()

        def _build_canvas(self):
            if self.container is None:
                return
            self.container.innerHTML = ''
            canvas = document.createElement('canvas')
            canvas.width = self.width
            canvas.height = self.height
            canvas.style.background = self._bgcolor
            canvas.style.border = '1px solid #999'
            canvas.style.maxWidth = '100%'
            self.container.appendChild(canvas)
            self.canvas = canvas
            self.ctx = canvas.getContext('2d')

        def _to_canvas(self, x, y):
            return (self.width / 2 + x, self.height / 2 - y)

        def bgcolor(self, color=None):
            if color is None:
                return self._bgcolor
            self._bgcolor = color
            if self.canvas is not None:
                self.canvas.style.background = color

        def title(self, _text):
            pass

        def setup(self, width=500, height=400, *args, **kwargs):
            self.width = width
            self.height = height
            if self.canvas is not None:
                self.canvas.width = width
                self.canvas.height = height

        def screensize(self, *args, **kwargs):
            pass

        def tracer(self, *args, **kwargs):
            pass

        def update(self):
            pass

        def onscreenclick(self, *args, **kwargs):
            pass

        def onkey(self, *args, **kwargs):
            pass

        def listen(self):
            pass

        def clear(self):
            if self.ctx is not None:
                self.ctx.clearRect(0, 0, self.width, self.height)

        def bye(self):
            if self.container is not None:
                self.container.innerHTML = ''

    class _Turtle:
        def __init__(self, screen):
            self.screen = screen
            self.x = 0.0
            self.y = 0.0
            self.heading_deg = 0.0
            self._down = True
            self._pencolor = 'black'
            self._fillcolor = 'black'
            self._width = 1
            self._visible = True
            self._filling = False
            self._fill_points = []
            self._speed = 3

        def _move_to(self, nx, ny):
            ctx = self.screen.ctx
            if ctx is not None and self._down:
                x1, y1 = self.screen._to_canvas(self.x, self.y)
                x2, y2 = self.screen._to_canvas(nx, ny)
                ctx.beginPath()
                ctx.moveTo(x1, y1)
                ctx.lineTo(x2, y2)
                ctx.strokeStyle = self._pencolor
                ctx.lineWidth = self._width
                ctx.stroke()
            if self._filling:
                self._fill_points.append((nx, ny))
            self.x, self.y = nx, ny

        def forward(self, distance):
            rad = math.radians(self.heading_deg)
            self._move_to(self.x + distance * math.cos(rad), self.y + distance * math.sin(rad))

        fd = forward

        def backward(self, distance):
            self.forward(-distance)

        bk = backward
        back = backward

        def left(self, angle):
            self.heading_deg = (self.heading_deg + angle) % 360

        lt = left

        def right(self, angle):
            self.heading_deg = (self.heading_deg - angle) % 360

        rt = right

        def setheading(self, angle):
            self.heading_deg = angle % 360

        seth = setheading

        def heading(self):
            return self.heading_deg

        def goto(self, x, y=None):
            if y is None:
                x, y = x
            self._move_to(x, y)

        setpos = goto
        setposition = goto

        def setx(self, x):
            self._move_to(x, self.y)

        def sety(self, y):
            self._move_to(self.x, y)

        def home(self):
            self._move_to(0, 0)
            self.heading_deg = 0

        def position(self):
            return (self.x, self.y)

        pos = position

        def xcor(self):
            return self.x

        def ycor(self):
            return self.y

        def distance(self, x, y=None):
            if y is None:
                x, y = x
            return math.hypot(x - self.x, y - self.y)

        def towards(self, x, y=None):
            if y is None:
                x, y = x
            return math.degrees(math.atan2(y - self.y, x - self.x)) % 360

        def penup(self):
            self._down = False

        pu = penup
        up = penup

        def pendown(self):
            self._down = True

        pd = pendown
        down = pendown

        def isdown(self):
            return self._down

        def width(self, w=None):
            if w is None:
                return self._width
            self._width = w

        pensize = width

        def color(self, *args):
            if not args:
                return (self._pencolor, self._fillcolor)
            if len(args) == 1:
                self._pencolor = args[0]
                self._fillcolor = args[0]
            else:
                self._pencolor, self._fillcolor = args[0], args[1]

        def pencolor(self, c=None):
            if c is None:
                return self._pencolor
            self._pencolor = c

        def fillcolor(self, c=None):
            if c is None:
                return self._fillcolor
            self._fillcolor = c

        def begin_fill(self):
            self._filling = True
            self._fill_points = [(self.x, self.y)]

        def end_fill(self):
            self._filling = False
            ctx = self.screen.ctx
            if ctx is not None and len(self._fill_points) > 2:
                ctx.beginPath()
                x0, y0 = self.screen._to_canvas(*self._fill_points[0])
                ctx.moveTo(x0, y0)
                for px, py in self._fill_points[1:]:
                    cx, cy = self.screen._to_canvas(px, py)
                    ctx.lineTo(cx, cy)
                ctx.closePath()
                ctx.fillStyle = self._fillcolor
                ctx.fill()
            self._fill_points = []

        def circle(self, radius, extent=360, steps=None):
            if steps is None:
                steps = max(int(abs(extent) / 10) + 1, 6)
            arc_length = 2 * math.pi * abs(radius) * (abs(extent) / 360)
            seg_len = arc_length / steps
            seg_angle = abs(extent) / steps
            turn = self.left if radius >= 0 else self.right
            for _ in range(steps):
                self.forward(seg_len)
                turn(seg_angle)

        def dot(self, size=None, color=None):
            ctx = self.screen.ctx
            if ctx is None:
                return
            radius = (size or max(self._width + 4, 6)) / 2
            cx, cy = self.screen._to_canvas(self.x, self.y)
            ctx.beginPath()
            ctx.arc(cx, cy, radius, 0, 2 * math.pi)
            ctx.fillStyle = color or self._pencolor
            ctx.fill()

        def write(self, text, move=False, align='left', font=('Arial', 12, 'normal')):
            ctx = self.screen.ctx
            if ctx is None:
                return
            cx, cy = self.screen._to_canvas(self.x, self.y)
            size = font[1] if len(font) > 1 else 12
            ctx.font = str(size) + 'px Arial'
            ctx.fillStyle = self._pencolor
            ctx.textAlign = align if align in ('left', 'center', 'right') else 'left'
            ctx.fillText(str(text), cx, cy)

        def shape(self, _name=None):
            pass

        def shapesize(self, *args, **kwargs):
            pass

        def speed(self, s=None):
            if s is None:
                return self._speed
            self._speed = s

        def showturtle(self):
            self._visible = True

        st = showturtle

        def hideturtle(self):
            self._visible = False

        ht = hideturtle

        def isvisible(self):
            return self._visible

        def reset(self):
            self.x = self.y = 0.0
            self.heading_deg = 0.0

        def undo(self):
            pass

        def stamp(self):
            self.dot()
            return 0

        def clearstamp(self, _stamp_id):
            pass

        def clearstamps(self, _n=None):
            pass

    _current = {'screen': None}

    def _get_container_id():
        try:
            container_id = getattr(window, '__turtleContainerId', None)
            return str(container_id) if container_id else None
        except Exception:
            return None

    def _current_screen():
        if _current['screen'] is None:
            _current['screen'] = _Screen(_get_container_id())
        return _current['screen']

    def Screen():
        _current['screen'] = _Screen(_get_container_id())
        return _current['screen']

    def Turtle(*args, **kwargs):
        return _Turtle(_current_screen())

    def done():
        pass

    def mainloop():
        pass

    def bye():
        if _current['screen'] is not None:
            _current['screen'].bye()
        _current['screen'] = None

    def write(text, **kwargs):
        turtle_module.Turtle().write(text, **kwargs)

    def ontimer(*args, **kwargs):
        pass

    turtle_module = types.ModuleType('turtle')
    turtle_module.Screen = Screen
    turtle_module.Turtle = Turtle
    turtle_module.Pen = Turtle
    turtle_module.done = done
    turtle_module.mainloop = mainloop
    turtle_module.bye = bye
    turtle_module.write = write
    turtle_module.ontimer = ontimer
    sys.modules['turtle'] = turtle_module


_install_turtle_shim()


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
   * @param {string} [turtleContainerId] - ID eines DOM-Elements, in das der
   *   turtle-Shim (siehe _install_turtle_shim) ein <canvas> zeichnet, falls
   *   der Code `import turtle` nutzt. Ohne Angabe wird nur nicht gezeichnet,
   *   der Code läuft trotzdem (kein Fehler).
   * @returns {Promise<{ success: boolean, output?: string, error?: string }>}
   */
  const runPython = async (code, turtleContainerId) => {
    if (!kernelReady.value || !pyodideRef.value) {
      return { success: false, error: 'Python-Kernel nicht initialisiert. Bitte zuerst Python starten.' };
    }

    const trimmed = code.trim();
    if (!trimmed) {
      return { success: true, output: '' };
    }

    window.__turtleContainerId = turtleContainerId || null;

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
      window.__turtleContainerId = null;
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
