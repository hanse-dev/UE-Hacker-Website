<template>
  <div class="js-sandbox-wrapper" v-show="showCanvas">
    <iframe
      ref="iframeEl"
      :key="frameKey"
      class="js-sandbox"
      sandbox="allow-scripts"
      :srcdoc="srcdoc"
    ></iframe>
    <div class="sandbox-toolbar">
      <span class="sandbox-status">{{ ready ? t('jsLesson.ready') : t('jsLesson.starting') }}</span>
      <button type="button" class="btn-restart-sandbox" @click="restart">
        {{ t('jsLesson.restartFrame') }}
      </button>
    </div>
    <p v-if="!alive" class="sandbox-stalled-hint">{{ t('jsLesson.frameStalled') }}</p>
  </div>
</template>

<script>
import { useJsSandbox } from '../composables/useJsSandbox';
import { useLanguage } from '../composables/useLanguage';

export default {
  name: 'JsSandboxFrame',
  props: {
    // Das iframe bleibt in jedem Fall gemountet (es ist die eigentliche Ausfuehrungsumgebung,
    // nicht nur eine Anzeige) - showCanvas steuert nur, ob es sichtbar ist. Kurse ohne Canvas-
    // Zeichnen (z.B. die meisten js-grundkurs-Wochen) brauchen keine leere graue Box zu zeigen,
    // die Ausgabe-Box unter dem Code-Editor reicht dort. Seit js-grundkurs Woche 7 (DOM &
    // Interaktivitaet) blendet derselbe Schalter zusaetzlich das feste DOM-Uebungs-Markup
    // (#dom-uebung in useJsSandbox.js) ein/aus - beides sitzt im selben iframe, es gibt keinen
    // separaten Schalter dafuer.
    showCanvas: { type: Boolean, default: true },
    // Steuert, welcher Inhalt im iframe angezeigt wird (Canvas vs. feste DOM-Uebungsflaeche) -
    // unabhaengig von showCanvas, das nur die Sichtbarkeit des ganzen Sandbox-Bereichs regelt.
    // Siehe useJsSandbox.js fuer die beiden srcdoc-Varianten.
    domMode: { type: Boolean, default: false },
  },
  setup(props, { expose }) {
    const { t } = useLanguage();
    const {
      iframeEl, frameKey, srcdoc, ready, alive,
      run, callFunction, checkCanvasNotBlank, checkCanvasChanged,
      checkDomText, checkDomClickText, restart,
    } = useJsSandbox(props.domMode ? 'dom' : 'canvas');

    // Chromium drosselt requestAnimationFrame in einem (cross-origin/opaken) iframe, das gerade
    // ausserhalb des sichtbaren Viewports liegt (bestaetigt: praktisch 0 Frames off-screen vs.
    // ~60fps sichtbar) - ohne das wuerde eine Animationsschleife fuer Lernende, die noch nicht bis
    // zum Spielfeld gescrollt haben, einfach eingefroren wirken.
    const scrollIntoView = () => {
      // 'auto' statt 'smooth': das Canvas muss VOR dem naechsten rAF-Frame schon im Viewport
      // liegen, sonst faengt eine canvas_changed-Pruefung (siehe useTaskValidation.js) noch die
      // gedrosselte Off-Screen-Phase ein.
      iframeEl.value?.scrollIntoView({ behavior: 'auto', block: 'center' });
    };

    expose({
      run, callFunction, checkCanvasNotBlank, checkCanvasChanged,
      checkDomText, checkDomClickText, restart, scrollIntoView,
    });

    return { iframeEl, frameKey, srcdoc, ready, alive, restart, t };
  },
};
</script>

<style scoped>
.js-sandbox-wrapper {
  margin-bottom: 16px;
}

.js-sandbox {
  width: 100%;
  max-width: 400px;
  height: 300px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  display: block;
  background: #eef2f7;
}

.sandbox-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-top: 8px;
  max-width: 400px;
}

.sandbox-status {
  font-size: 0.85em;
  color: #6c757d;
}

.btn-restart-sandbox {
  background: #6c757d;
  color: white;
  border: none;
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85em;
  font-weight: 500;
}

.btn-restart-sandbox:hover {
  background: #5a6268;
}

.sandbox-stalled-hint {
  max-width: 400px;
  margin: 8px 0 0 0;
  padding: 8px 12px;
  background: #fff3cd;
  border: 1px solid #ffe69c;
  border-radius: 6px;
  font-size: 0.85em;
  color: #664d03;
}
</style>
