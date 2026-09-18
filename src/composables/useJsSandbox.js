import { ref, nextTick, onMounted, onBeforeUnmount } from 'vue';

// Nachrichten-Kanal-Kennung, damit der Parent postMessage-Events von anderen Quellen (Browser-
// Extensions, andere iframes) sicher ignoriert.
const CHANNEL = 'ue-js-sandbox';
const RPC_TIMEOUT_MS = 1500;
const RUN_TIMEOUT_MS = 5000;
const HEARTBEAT_STALL_MS = 2000;

// Das Spielfeld: eine feste Canvas-Groesse/ID fuer den ganzen Kurs, kein Setup-Aufwand pro Lektion.
export const SANDBOX_CANVAS_ID = 'spielfeld';

// Harness-Script, das im sandboxed iframe laeuft. `sandbox="allow-scripts"` OHNE
// `allow-same-origin` gibt dem Frame eine opake Origin - localStorage/Cookies/DOM des Elternfensters
// sind fuer den Schueler-Code unerreichbar, ganz ohne eigenes Zutun. Kein Web Worker (siehe
// HANDOFF.md 3.32/3.5): das Spiel braucht ein sichtbares Canvas mit echten keydown/click-Events,
// die im Worker erst per postMessage nachgebaut werden muessten.
//
// `(0, eval)(code)` statt `new Function(code)`: bei Funktions-Konstruktoren werden Top-Level
// `let`/`const` nur lokal im Funktionsaufruf sichtbar und gehen beim Zurueckkehren verloren - nur
// `var`/`function` wuerden ueberleben. Indirekter eval fuehrt Code dagegen im globalen Scope aus;
// `let`/`const` landen dort in der persistenten globalen lexikalischen Umgebung des Realms und
// bleiben ueber den ganzen Lauf hinweg per Bezeichner (`(0, eval)(name)`) abrufbar - unabhaengig
// davon, ob der Name mit `function`, `var`, `let` oder `const` deklariert wurde.
function buildSandboxHtml() {
  return `<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline' 'unsafe-eval'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'">
<style>
  html, body { margin: 0; padding: 0; background: #eef2f7; }
  canvas { display: block; background: #eef2f7; }
</style>
</head>
<body>
<canvas id="${SANDBOX_CANVAS_ID}" width="400" height="300"></canvas>
<script>
(function () {
  var CH = '${CHANNEL}';
  var consoleBuffer = [];
  var frames = 0;

  function send(msg) {
    msg.ch = CH;
    parent.postMessage(msg, '*');
  }

  function stringifyArg(a) {
    if (typeof a === 'string') return a;
    if (a === undefined) return 'undefined';
    try { return JSON.stringify(a); } catch (e) { return String(a); }
  }

  function captureConsole(level) {
    return function () {
      var text = Array.prototype.map.call(arguments, stringifyArg).join(' ');
      consoleBuffer.push(text);
      send({ type: 'console', level: level, text: text });
    };
  }
  console.log = captureConsole('log');
  console.warn = captureConsole('warn');
  console.error = captureConsole('error');

  window.onerror = function (message) {
    send({ type: 'console', level: 'error', text: String(message) });
    return true;
  };
  window.addEventListener('unhandledrejection', function (e) {
    send({ type: 'console', level: 'error', text: String(e.reason) });
  });

  function cloneSafe(value) {
    if (value === undefined) return undefined;
    try { return JSON.parse(JSON.stringify(value)); } catch (e) { return null; }
  }

  function readCanvasData() {
    var canvas = document.getElementById('${SANDBOX_CANVAS_ID}');
    if (!canvas) return null;
    var ctx = canvas.getContext('2d');
    return ctx.getImageData(0, 0, canvas.width, canvas.height).data;
  }

  window.addEventListener('message', function (e) {
    var msg = e.data;
    if (!msg || msg.ch !== CH) return;

    if (msg.type === 'run') {
      consoleBuffer = [];
      var ok = true, error = null;
      try {
        (0, eval)(msg.code);
      } catch (err) {
        ok = false;
        error = err && err.message ? err.message : String(err);
      }
      send({ type: 'runResult', ok: ok, output: consoleBuffer.join('\\n'), error: error });
      return;
    }

    if (msg.type === 'get') {
      var gok = true, gval, gerr;
      try {
        gval = cloneSafe((0, eval)(msg.name));
      } catch (err) {
        gok = false;
        gerr = err && err.message ? err.message : String(err);
      }
      send({ type: 'result', reqId: msg.reqId, ok: gok, value: gval, error: gerr });
      return;
    }

    if (msg.type === 'call') {
      var cok = true, cval, cerr;
      try {
        var fn = (0, eval)(msg.name);
        if (typeof fn !== 'function') throw new Error(msg.name + ' ist keine Funktion');
        cval = cloneSafe(fn.apply(null, msg.args || []));
      } catch (err) {
        cok = false;
        cerr = err && err.message ? err.message : String(err);
      }
      send({ type: 'result', reqId: msg.reqId, ok: cok, value: cval, error: cerr });
      return;
    }

    if (msg.type === 'canvas') {
      if (msg.mode === 'notBlank') {
        var data = readCanvasData();
        var notBlank = false;
        if (data) {
          for (var i = 3; i < data.length; i += 4) {
            if (data[i] !== 0) { notBlank = true; break; }
          }
        }
        send({ type: 'result', reqId: msg.reqId, ok: true, value: notBlank });
        return;
      }
      if (msg.mode === 'changed') {
        var before = readCanvasData();
        setTimeout(function () {
          var after = readCanvasData();
          var changed = false;
          if (before && after) {
            for (var j = 0; j < before.length; j++) {
              if (before[j] !== after[j]) { changed = true; break; }
            }
          }
          send({ type: 'result', reqId: msg.reqId, ok: true, value: changed });
        }, msg.ms || 400);
        return;
      }
    }
  });

  function heartbeat() {
    frames++;
    requestAnimationFrame(heartbeat);
  }
  requestAnimationFrame(heartbeat);
  setInterval(function () {
    send({ type: 'beat', frames: frames });
  }, 500);

  send({ type: 'ready' });
})();
</script>
</body>
</html>`;
}

const SANDBOX_SRCDOC = buildSandboxHtml();

/**
 * Kapselt Aufbau/Neustart des Sandbox-iframes und das postMessage-RPC-Protokoll zum Ausfuehren von
 * JS-Code darin. Jeder `run()`/`restart()` baut das iframe komplett neu (Vue-`:key`-Bump) - Reset
 * ist der Normalfall, kein Sonderfall, dadurch entfaellt jede Namespace-Hygiene zwischen Laeufen
 * (anders als beim geteilten Pyodide-Kernel in usePyodide.js).
 */
export function useJsSandbox() {
  const iframeEl = ref(null);
  const frameKey = ref(0);
  const ready = ref(false);
  const alive = ref(true);

  let readyResolvers = [];
  const pending = new Map();
  let reqCounter = 0;
  let lastBeatAt = Date.now();
  let heartbeatTimer = null;

  const waitForReady = () => {
    if (ready.value) return Promise.resolve();
    return new Promise((resolve) => readyResolvers.push(resolve));
  };

  const handleMessage = (e) => {
    if (!iframeEl.value || e.source !== iframeEl.value.contentWindow) return;
    const msg = e.data;
    if (!msg || msg.ch !== CHANNEL) return;

    if (msg.type === 'ready') {
      ready.value = true;
      alive.value = true;
      lastBeatAt = Date.now();
      readyResolvers.forEach((r) => r());
      readyResolvers = [];
      return;
    }
    if (msg.type === 'beat') {
      alive.value = true;
      lastBeatAt = Date.now();
      return;
    }
    if (msg.type === 'runResult') {
      const entry = pending.get('run');
      if (entry) {
        clearTimeout(entry.timer);
        pending.delete('run');
        entry.resolve({ success: msg.ok, output: msg.output || '', error: msg.error });
      }
      return;
    }
    if (msg.type === 'result') {
      const entry = pending.get(msg.reqId);
      if (entry) {
        clearTimeout(entry.timer);
        pending.delete(msg.reqId);
        entry.resolve({ ok: msg.ok, value: msg.value, error: msg.error });
      }
      return;
    }
    // 'console'-Nachrichten (Logs nach dem urspruenglichen Lauf, z.B. aus einem Event-Handler)
    // werden aktuell nicht separat ausgewertet - der Check-Flow arbeitet mit dem synchronen
    // `runResult`-Output, wie beim Pyodide-Pendant `runPython()`.
  };

  const post = (msg) => {
    // `msg` (z.B. `args` aus einem functionCalls-Eintrag) stammt oft aus reaktiven Vue-Refs -
    // ein Proxy-Array laesst sich nicht per postMessage klonen (DataCloneError). Ueber JSON in
    // reine Werte umwandeln, bevor es das Fenster verlaesst.
    const plain = JSON.parse(JSON.stringify({ ...msg, ch: CHANNEL }));
    iframeEl.value?.contentWindow?.postMessage(plain, '*');
  };

  const rpc = (type, extra) => {
    const reqId = ++reqCounter;
    return new Promise((resolve) => {
      const timer = setTimeout(() => {
        pending.delete(reqId);
        resolve({ ok: false, error: 'timeout' });
      }, RPC_TIMEOUT_MS);
      pending.set(reqId, { resolve, timer });
      post({ type, reqId, ...extra });
    });
  };

  const rebuildFrame = async () => {
    ready.value = false;
    alive.value = true;
    pending.forEach(({ timer }) => clearTimeout(timer));
    pending.clear();
    frameKey.value += 1;
    await nextTick();
    await waitForReady();
  };

  const run = async (code) => {
    await rebuildFrame();
    return new Promise((resolve) => {
      const timer = setTimeout(() => {
        pending.delete('run');
        resolve({ success: false, output: '', error: 'timeout' });
      }, RUN_TIMEOUT_MS);
      pending.set('run', { resolve, timer });
      post({ type: 'run', code });
    });
  };

  const getVariable = async (name) => {
    const r = await rpc('get', { name });
    return r.ok ? r.value : undefined;
  };

  const callFunction = async (name, args) => rpc('call', { name, args });

  const checkCanvasNotBlank = async () => {
    const r = await rpc('canvas', { mode: 'notBlank' });
    return !!r.value;
  };

  const checkCanvasChanged = async (ms) => {
    const r = await rpc('canvas', { mode: 'changed', ms });
    return !!r.value;
  };

  const restart = async () => rebuildFrame();

  onMounted(() => {
    window.addEventListener('message', handleMessage);
    heartbeatTimer = setInterval(() => {
      if (ready.value && Date.now() - lastBeatAt > HEARTBEAT_STALL_MS) {
        alive.value = false;
      }
    }, 500);
  });

  onBeforeUnmount(() => {
    window.removeEventListener('message', handleMessage);
    clearInterval(heartbeatTimer);
    pending.forEach(({ timer }) => clearTimeout(timer));
    pending.clear();
  });

  return {
    iframeEl,
    frameKey,
    srcdoc: SANDBOX_SRCDOC,
    ready,
    alive,
    run,
    getVariable,
    callFunction,
    checkCanvasNotBlank,
    checkCanvasChanged,
    restart,
  };
}
