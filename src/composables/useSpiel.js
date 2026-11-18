// Spiel-Laufzeit fuer die Spiel-Projekte (engine "spiel", z. B. content/ausweichen/).
//
// Das Programm der Kinder laeuft im gemeinsamen Pyodide-Kernel (usePyodide.js, mit Loop-Guard und
// Ausgabe). Danach treibt diese Datei die Spielschleife: 60-mal pro Sekunde `jedes_bild()` aufrufen
// (src/spiel/spiel.py, `_bild`), den Stand lesen und auf ein Canvas zeichnen. Eine Python-Schleife
// mit `while True` ginge nicht - Pyodide laeuft im Browser-Tab und darf ihn nie blockieren.
//
// Pruefen spielt das Spiel unsichtbar mit festen Tasten durch (`_pruefe`, validation.checks in
// lessons.json); ob das Ergebnis besteht, entscheidet useTaskValidation.js (validateSpiel).

import { usePyodide } from './usePyodide';
import spielQuelle from '../spiel/spiel.py?raw';
import zuBloeckenQuelle from '../spiel/zu_bloecken.py?raw';

const MODUL_ORDNER = '/ue_spiel';
const BILD_MS = 1000 / 60;
// Zufalls-Startwerte fuers Pruefen: jede Pruefung laeuft mit jedem davon (Glueck zaehlt nicht).
export const SPIEL_STARTWERTE = [1, 2, 3];

let vorbereitet = null;

function bereiteVor(pyodide) {
  if (!vorbereitet) {
    vorbereitet = (async () => {
      try {
        pyodide.FS.mkdir(MODUL_ORDNER);
      } catch {
        // Ordner gibt es schon (z. B. nach Hot-Reload).
      }
      pyodide.FS.writeFile(`${MODUL_ORDNER}/spiel.py`, spielQuelle);
      pyodide.FS.writeFile(`${MODUL_ORDNER}/zu_bloecken.py`, zuBloeckenQuelle);
      pyodide.runPython(`
import sys, importlib
if '${MODUL_ORDNER}' not in sys.path:
    sys.path.insert(0, '${MODUL_ORDNER}')
importlib.invalidate_caches()
import spiel as _ue_spiel
import zu_bloecken as _ue_zu_bloecken
`);
    })();
  }
  return vorbereitet;
}

/** Kurze, kindgerechte Fehlermeldung aus einem Python-Fehler im Spiel (nur die letzte Zeile). */
export function spielFehlertext(e) {
  const text = String(e?.message || e || '');
  if (text.includes('_CellTimeout') || text === 'timeout') {
    return 'jedes_bild brauchte zu lange – vermutlich eine Endlosschleife darin.';
  }
  const zeilen = text.trim().split('\n').filter(Boolean);
  return zeilen[zeilen.length - 1] || text;
}

function zeichne(canvas, stand) {
  const ctx = canvas.getContext('2d');
  const { width, height } = canvas;
  ctx.fillStyle = stand.hintergrund || '#0f172a';
  ctx.fillRect(0, 0, width, height);
  for (const [x, y, b, h, farbe] of stand.figuren) {
    ctx.fillStyle = farbe;
    ctx.beginPath();
    if (ctx.roundRect) ctx.roundRect(x, y, b, h, Math.min(6, b / 4, h / 4));
    else ctx.rect(x, y, b, h);
    ctx.fill();
  }
  ctx.textBaseline = 'top';
  if (stand.text) {
    ctx.font = 'bold 18px system-ui, sans-serif';
    ctx.textAlign = 'left';
    ctx.lineWidth = 4;
    ctx.strokeStyle = 'rgba(0, 0, 0, 0.7)';
    ctx.strokeText(stand.text, 10, 10);
    ctx.fillStyle = '#ffffff';
    ctx.fillText(stand.text, 10, 10);
  }
  if (stand.vorbei) {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.55)';
    ctx.fillRect(0, 0, width, height);
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 36px system-ui, sans-serif';
    ctx.fillText(stand.endtext || 'Spiel vorbei!', width / 2, height / 2 - 14);
    ctx.font = '16px system-ui, sans-serif';
    ctx.fillText('▶ Spielen startet neu', width / 2, height / 2 + 26);
  }
}

export function useSpiel() {
  const { kernelReady, pyodideRef, runPython } = usePyodide();
  let schleife = null;

  const modul = async () => {
    const py = pyodideRef.value;
    await bereiteVor(py);
    return py.globals.get('_ue_spiel');
  };

  /** Python -> Blockly-JSON (Text). Wirft bei Code, den es nicht als Bloecke gibt. */
  const zuBloecken = async (code) => {
    const py = pyodideRef.value;
    await bereiteVor(py);
    return py.globals.get('_ue_zu_bloecken').zu_bloecken(code);
  };

  const stoppe = () => {
    if (!schleife) return;
    schleife.aktiv = false;
    cancelAnimationFrame(schleife.raf);
    schleife = null;
  };

  /**
   * Fuehrt das Programm aus und startet die Spielschleife.
   * @param {string} code - Python-Programm
   * @param {HTMLCanvasElement} canvas
   * @param {() => string[]} tasten - gerade gedrueckte Tasten ("links", "rechts", ...)
   * @param {(fehler: string) => void} beiEnde - Spiel ist von selbst zu Ende: '' nach spiel_ende(),
   *   sonst die Fehlermeldung eines Python-Fehlers in jedes_bild (die Schleife ist dann gestoppt).
   * @returns {Promise<{ success: boolean, output?: string, error?: string, laeuft?: boolean }>}
   */
  const starte = async (code, canvas, tasten, beiEnde) => {
    stoppe();
    if (!kernelReady.value) return { success: false, error: 'Python ist noch nicht bereit.' };
    const py = pyodideRef.value;
    const sp = await modul();
    sp._neu(py.globals);
    const ergebnis = await runPython(code);
    zeichne(canvas, JSON.parse(sp._stand()));
    if (!ergebnis.success || !sp._hat_jedes_bild(py.globals)) return { ...ergebnis, laeuft: false };

    const lauf = { aktiv: true, raf: 0, zuletzt: performance.now(), rest: 0, tastenText: '' };
    schleife = lauf;
    const tick = (jetzt) => {
      if (!lauf.aktiv) return;
      lauf.rest = Math.min(lauf.rest + (jetzt - lauf.zuletzt), BILD_MS * 4);
      lauf.zuletzt = jetzt;
      try {
        const gedrueckt = tasten().join(',');
        if (gedrueckt !== lauf.tastenText) {
          sp._setze_tasten(gedrueckt ? gedrueckt.split(',') : []);
          lauf.tastenText = gedrueckt;
        }
        while (lauf.rest >= BILD_MS) {
          sp._bild(py.globals);
          lauf.rest -= BILD_MS;
        }
        const stand = JSON.parse(sp._stand());
        zeichne(canvas, stand);
        if (stand.vorbei) {
          stoppe();
          beiEnde('');
          return;
        }
      } catch (e) {
        stoppe();
        beiEnde(spielFehlertext(e));
        return;
      }
      lauf.raf = requestAnimationFrame(tick);
    };
    lauf.raf = requestAnimationFrame(tick);
    return { ...ergebnis, laeuft: true };
  };

  /**
   * Prueft ein Programm gegen validation.checks: fuer jeden Startwert frisch ausfuehren und die
   * Pruefschritte durchspielen. Ergebnis wie `_pruefe` in spiel.py, plus `error` bei Abbruch.
   */
  const pruefe = async (code, checks) => {
    stoppe();
    const py = pyodideRef.value;
    const sp = await modul();
    let letztes = { ok: false, schritt: 0, fehler: '' };
    for (const startwert of SPIEL_STARTWERTE) {
      sp._neu(py.globals);
      py.runPython(`import random as _ue_random\n_ue_random.seed(${startwert})`);
      const lauf = await runPython(code);
      if (!lauf.success) return { ok: false, schritt: -1, fehler: lauf.error, output: '' };
      try {
        letztes = { ...JSON.parse(sp._pruefe(py.globals, JSON.stringify(checks))), output: lauf.output };
      } catch (e) {
        letztes = { ok: false, schritt: 0, fehler: spielFehlertext(e), output: lauf.output };
      }
      if (!letztes.ok) break;
    }
    sp._neu(py.globals);
    return letztes;
  };

  return { kernelReady, starte, stoppe, pruefe, zuBloecken, zeichneLeer: (canvas) => zeichne(canvas, { figuren: [] }) };
}
