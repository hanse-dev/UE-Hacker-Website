<template>
  <div class="spiel-bloecke" :class="{ 'spiel-bloecke-lesen': readOnly }">
    <p v-if="fehler" class="spiel-bloecke-fehler">{{ fehler }}</p>
    <div ref="host" class="spiel-bloecke-flaeche" :style="{ height: hoehe + 'px' }"></div>
  </div>
</template>

<script>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue';
import { ladeBlockly, pythonAusBloecken, blocklyTheme, WERKZEUGKASTEN } from '../spiel/bloecke.js';
import { useTheme } from '../composables/useTheme';

// Ein Blockly-Arbeitsbereich fuer eine Aufgabe der Spiel-Projekte (SpielLessonView.vue).
// `inhalt` ist Blockly-JSON (Text): der gespeicherte Stand oder die aus Python erzeugte Vorlage
// (useSpiel.js, zuBloecken). Jede echte Aenderung meldet `aenderung` mit neuem JSON und dem daraus
// erzeugten Python. Read-only (ohne Werkzeugkasten) zeigt dieselbe Komponente die Loesung.
export default {
  name: 'SpielBloecke',
  props: {
    inhalt: { type: String, default: '' },
    readOnly: { type: Boolean, default: false },
    hoehe: { type: Number, default: 420 },
  },
  emits: ['aenderung', 'bereit'],
  setup(props, { emit, expose }) {
    const host = ref(null);
    const fehler = ref('');
    const { resolvedTheme } = useTheme();
    let ws = null;
    let api = null;
    let beobachter = null;
    let geladenerInhalt = null;

    const python = () => (ws && api ? pythonAusBloecken(api.pythonGenerator, ws) : '');

    const lade = (inhalt) => {
      if (!ws || !api) return;
      geladenerInhalt = inhalt;
      api.Blockly.Events.disable();
      try {
        ws.clear();
        if (inhalt) {
          const daten = JSON.parse(inhalt);
          api.Blockly.serialization.workspaces.load(daten, ws);
          // Aus Python erzeugte Vorlagen haben nur grobe Positionen - sauber untereinander stellen.
          if (!daten.gespeichert) ws.cleanUp();
        }
        fehler.value = '';
      } catch (e) {
        console.error('Bloecke konnten nicht geladen werden:', e);
        fehler.value = 'Die Blöcke konnten nicht geladen werden.';
      } finally {
        api.Blockly.Events.enable();
      }
      // Oben links anfangen (scrollCenter wuerde den Anfang der Bloecke abschneiden).
      const oben = ws.getTopBlocks(true)[0];
      if (oben) {
        const { x, y } = oben.getRelativeToSurfaceXY();
        ws.scroll(-x * ws.scale + 16, -y * ws.scale + 16);
      }
    };

    onMounted(async () => {
      api = await ladeBlockly();
      if (!host.value) return;
      const { Blockly } = api;
      ws = Blockly.inject(host.value, {
        toolbox: props.readOnly ? undefined : WERKZEUGKASTEN,
        readOnly: props.readOnly,
        renderer: 'geras',
        theme: blocklyTheme(Blockly, resolvedTheme.value === 'dark'),
        trashcan: !props.readOnly,
        // Schmal (Handy) kleiner anfangen, sonst sieht man neben dem Werkzeugkasten kaum Bloecke.
        zoom: { controls: true, wheel: false, startScale: host.value.clientWidth < 500 ? 0.6 : 0.85, maxScale: 1.5, minScale: 0.4 },
        move: { scrollbars: true, drag: true, wheel: true },
        grid: { spacing: 24, length: 2, snap: false },
        sounds: false,
      });
      lade(props.inhalt);
      ws.addChangeListener((ereignis) => {
        Blockly.Events.disableOrphans(ereignis);
        if (props.readOnly || ereignis.isUiEvent) return;
        if (ereignis.type === Blockly.Events.FINISHED_LOADING) return;
        const daten = Blockly.serialization.workspaces.save(ws);
        daten.gespeichert = true;
        const json = JSON.stringify(daten);
        geladenerInhalt = json;
        emit('aenderung', { json, python: python() });
      });
      beobachter = new ResizeObserver(() => ws && Blockly.svgResize(ws));
      beobachter.observe(host.value);
      emit('bereit', { python: python() });
    });

    // Zuruecksetzen/Loesung laden setzt `inhalt` von aussen - eigene Aenderungen kommen schon so zurueck.
    watch(() => props.inhalt, (neu) => {
      if (neu !== geladenerInhalt) {
        lade(neu);
        emit('bereit', { python: python() });
      }
    });

    watch(resolvedTheme, (thema) => {
      if (ws && api) ws.setTheme(blocklyTheme(api.Blockly, thema === 'dark'));
    });

    onBeforeUnmount(() => {
      beobachter?.disconnect();
      ws?.dispose();
      ws = null;
    });

    expose({ python });
    return { host, fehler };
  },
};
</script>

<style scoped>
.spiel-bloecke-flaeche {
  width: 100%;
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.spiel-bloecke-fehler {
  color: var(--danger-text);
  margin: 0 0 0.5rem;
}
</style>
