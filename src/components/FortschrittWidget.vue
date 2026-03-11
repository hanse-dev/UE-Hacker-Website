<template>
  <div class="fortschritt-widget">
    <div class="fortschritt-widget-header" @click="fortschrittExpanded = !fortschrittExpanded">
      <h3>🏆 Deine gesammelten Belohnungen</h3>
      <span class="fortschritt-toggle">{{ fortschrittExpanded ? '−' : '+' }}</span>
    </div>
    <div v-show="fortschrittExpanded" class="fortschritt-widget-content">
      <div class="fortschritt-einleitung">
        <p><strong>Was ist das Punkte-System?</strong> In jeder Woche gibt es Missionen, die du meisterst – dabei sammelst du Belohnungen (XP, Huf-Punkte oder Cyber Credits je nach Questreihe). Das soll Spaß machen und dich motivieren, dranzubleiben.</p>
        <p>Klicke bei jeder erledigten Mission auf „Punkte einlösen" – so siehst du deinen Fortschritt und kannst dich über gesammelte Items freuen. Nichts davon ist Pflicht, es ist nur zum Feiern deiner Erfolge da. 🎉</p>
      </div>
      <div class="fortschritt-import-export">
        <button @click="exportFortschritt" class="fortschritt-io-btn" title="Fortschritt als JSON herunterladen">
          📤 Exportieren
        </button>
        <label class="fortschritt-io-btn">
          📥 Importieren
          <input
            type="file"
            accept=".json,application/json"
            class="fortschritt-file-input"
            @change="onImportFile"
          />
        </label>
      </div>
      <div class="fortschritt-skript-erklaerung">
        <div class="fortschritt-skript-header" @click="skriptErklaerungExpanded = !skriptErklaerungExpanded">
          <h4>💻 Lokal arbeiten? So funktioniert das Fortschritt-Skript</h4>
          <span class="fortschritt-toggle">{{ skriptErklaerungExpanded ? '−' : '+' }}</span>
        </div>
        <div v-show="skriptErklaerungExpanded" class="fortschritt-skript-content">
          <div class="fortschritt-skript-download">
            <a href="/fortschritt-script.zip" download class="fortschritt-skript-btn">
              📥 Fortschritt-Skript herunterladen
            </a>
            <span class="fortschritt-skript-btn-hint">ZIP mit <code>fortschritt.py</code> und <code>rewards-manifest.json</code></span>
          </div>
          <p>Wenn du die Notebooks <strong>lokal</strong> in Jupyter oder VS Code ausführst, kannst du trotzdem Punkte sammeln:</p>
          <ol>
            <li><strong>Skript ausführen</strong>, wenn du eine Mission gemeistert hast:
              <pre><code>python fortschritt.py</code></pre>
              Das Skript fragt dich interaktiv: Questreihe (Abenteuer/Pferde/Sci-Fi), Woche (1–12), was du beendet hast (Mission 1–3 oder Boss-Quest 1–3). Es erstellt <code>mein-fortschritt.json</code> im aktuellen Verzeichnis.
            </li>
            <li><strong>Hier importieren</strong>: Klicke oben auf „📥 Importieren" und wähle deine <code>mein-fortschritt.json</code> – die Missionen werden zusammengeführt.</li>
          </ol>
          <p class="fortschritt-skript-details">Lade das ZIP oben herunter, entpacke es und führe <code>python fortschritt.py</code> im entpackten Ordner aus. Oder nutze das vollständige Notebook-Pack unten – es enthält das Skript ebenfalls. Befehle: <code>python fortschritt.py add abenteuer w10-m1</code> oder <code>python fortschritt.py show</code> für den aktuellen Stand.</p>
        </div>
      </div>

      <div class="fortschritt-variant-selector">
        <span class="fortschritt-variant-label">Questreihe:</span>
        <div class="fortschritt-variant-buttons">
          <button
            @click="selectedFortschrittVariant = 'alle'"
            :class="{ active: selectedFortschrittVariant === 'alle' }"
            class="fortschritt-variant-btn"
          >
            Alle
          </button>
          <button
            v-for="v in variantKeys"
            :key="v"
            @click="selectedFortschrittVariant = v"
            :class="{ active: selectedFortschrittVariant === v }"
            class="fortschritt-variant-btn"
          >
            {{ variantLabels[v] }}
          </button>
        </div>
      </div>

      <div class="fortschritt-variants">
        <div class="fortschritt-variant" v-for="v in displayedVariantKeys" :key="v">
          <span class="variant-label">{{ variantLabels[v] }}</span>
          <span class="variant-points">{{ getVariantProgress(v).totalPoints }} {{ variantUnits[v] }}</span>
          <span class="variant-items" v-if="getVariantProgress(v).claims.length > 0">
            ({{ getVariantProgress(v).claims.length }} Missionen)
          </span>
        </div>
      </div>

      <div class="fortschritt-weekly-section">
        <h4>📅 Verlauf nach Woche</h4>
        <p class="fortschritt-weekly-hint">Pro Woche gibt es 6 Missionen (3 Haupt + 3 Boss). Zeigt wie viel % du bereits eingelöst hast.</p>
        <div class="fortschritt-by-week" v-for="v in displayedVariantKeys" :key="`week-${v}`">
          <h5>{{ variantLabels[v] }}</h5>
          <div class="week-progress-grid">
            <div
              v-for="w in getWeeklyProgress(v)"
              :key="`${v}-w${w.week}`"
              class="week-progress-card"
              :class="{ 'has-claims': w.claimedCount > 0, 'complete': w.percentOpen === 0 }"
            >
              <div class="week-progress-header" @click="toggleWeekProgress(v, w.week)">
                <span class="week-number">Woche {{ w.week }}</span>
                <span class="week-stats">{{ w.claimedCount }}/6 ✓ {{ w.percentDone }}%</span>
                <span class="week-open" v-if="w.percentOpen > 0">{{ w.percentOpen }}% offen</span>
                <span class="week-open complete" v-else>✓ Vollständig</span>
                <span class="week-toggle">{{ isWeekProgressExpanded(v, w.week) ? '−' : '+' }}</span>
              </div>
              <div v-show="isWeekProgressExpanded(v, w.week)" class="week-progress-detail">
                <ul v-if="w.claims.length > 0" class="fortschritt-claims-list">
                  <li v-for="(c, i) in w.claims" :key="`${v}-w${w.week}-${c.missionId}-${i}`">
                    <span class="claim-label">{{ formatClaimLabel(c) }}:</span>
                    <span class="claim-reward">{{ c.points }} {{ variantUnits[v] }} + {{ c.item }}</span>
                  </li>
                </ul>
                <p v-else class="week-no-claims">Noch nichts in dieser Woche eingelöst.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="fortschritt-details" v-for="v in displayedVariantKeys" :key="`details-${v}`">
        <div v-if="getVariantProgress(v).claims.length > 0" class="fortschritt-variant-detail">
          <h4>{{ variantLabels[v] }} – alle eingelösten Belohnungen</h4>
          <ul class="fortschritt-claims-list">
            <li v-for="(c, i) in getVariantProgress(v).claims" :key="`${v}-${c.missionId}-${i}`">
              <span class="claim-label">{{ formatClaimLabel(c) }} (Woche {{ getWeekFromMissionId(c.missionId) }}):</span>
              <span class="claim-reward">{{ c.points }} {{ variantUnits[v] }} + {{ c.item }}</span>
            </li>
          </ul>
          <h4 class="items-header">📦 Gesammelte Items</h4>
          <ul class="fortschritt-items-list">
            <li v-for="(item, i) in getVariantProgress(v).items" :key="`${v}-item-${i}`">{{ item }}</li>
          </ul>
        </div>
      </div>
      <p class="fortschritt-hint" v-if="getTotalClaims() === 0">Klicke „Punkte einlösen" bei jeder Mission, die du gemeistert hast!</p>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useFortschritt } from '../composables/useFortschritt';

const VARIANT_KEYS = ['abenteuer', 'pferde', 'scifi'];
const VARIANT_LABELS = { abenteuer: '🗺️ Abenteuer', pferde: '🐴 Pferde', scifi: '🚀 Sci-Fi' };
const VARIANT_UNITS = { abenteuer: 'XP', pferde: 'Huf-Punkte', scifi: 'Cyber Credits' };
const WEEKLY_TOTAL = 6;

export default {
  name: 'FortschrittWidget',
  setup() {
    const fortschrittExpanded = ref(true);
    const skriptErklaerungExpanded = ref(false);
    const selectedFortschrittVariant = ref('alle');
    const weekProgressExpanded = ref({});

    const { getVariantProgress, exportProgress, importProgress } = useFortschritt();

    const displayedVariantKeys = computed(() =>
      selectedFortschrittVariant.value === 'alle' ? VARIANT_KEYS : [selectedFortschrittVariant.value]
    );

    const deriveMissionLabel = (id) => {
      const m = id.match(/w(\d+)-(m|boss)(\d+)/);
      if (!m) return id;
      return m[2] === 'm' ? `Mission ${m[3]}` : `Boss-Quest ${m[3]}`;
    };

    const formatClaimLabel = (c) => c.missionLabel || (c.missionId ? deriveMissionLabel(c.missionId) : '–');
    const getTotalClaims = () => VARIANT_KEYS.reduce((n, v) => n + getVariantProgress(v).claims.length, 0);

    const getWeekFromMissionId = (missionId) => {
      const m = missionId && missionId.match(/w(\d+)-/);
      return m ? parseInt(m[1], 10) : '?';
    };

    const getWeeklyProgress = (variant) => {
      const claims = getVariantProgress(variant).claims;
      const byWeek = {};
      for (let w = 1; w <= 12; w++) byWeek[w] = { week: w, claims: [], claimedCount: 0, percentDone: 0, percentOpen: 100 };
      for (const c of claims) {
        const w = getWeekFromMissionId(c.missionId);
        if (typeof w === 'number' && byWeek[w]) {
          byWeek[w].claims.push(c);
          byWeek[w].claimedCount = byWeek[w].claims.length;
          byWeek[w].percentDone = Math.round((byWeek[w].claimedCount / WEEKLY_TOTAL) * 100);
          byWeek[w].percentOpen = 100 - byWeek[w].percentDone;
        }
      }
      return Object.values(byWeek);
    };

    const isWeekProgressExpanded = (variant, week) => weekProgressExpanded.value[`${variant}-${week}`] ?? false;
    const toggleWeekProgress = (variant, week) => {
      const key = `${variant}-${week}`;
      weekProgressExpanded.value = { ...weekProgressExpanded.value, [key]: !weekProgressExpanded.value[key] };
    };

    const exportFortschritt = () => {
      const json = exportProgress();
      const blob = new Blob([json], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'mein-fortschritt.json';
      a.click();
      URL.revokeObjectURL(a.href);
    };

    const onImportFile = (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        const result = importProgress(reader.result);
        if (result.ok) {
          alert('Fortschritt wurde importiert und mit deinem bestehenden Stand zusammengeführt.');
        } else {
          alert('Import fehlgeschlagen: ' + (result.error || 'Unbekannter Fehler'));
        }
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };

    return {
      fortschrittExpanded,
      skriptErklaerungExpanded,
      selectedFortschrittVariant,
      displayedVariantKeys,
      variantKeys: VARIANT_KEYS,
      variantLabels: VARIANT_LABELS,
      variantUnits: VARIANT_UNITS,
      getVariantProgress,
      formatClaimLabel,
      getTotalClaims,
      exportFortschritt,
      onImportFile,
      getWeekFromMissionId,
      getWeeklyProgress,
      isWeekProgressExpanded,
      toggleWeekProgress,
    };
  },
};
</script>

<style scoped>
.fortschritt-widget {
  background: linear-gradient(135deg, #fef9e7 0%, #fdebd0 100%);
  border: 2px solid #ffd700;
  border-radius: 8px;
  margin-bottom: 40px;
  overflow: hidden;
}

.fortschritt-widget-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  cursor: pointer;
  user-select: none;
}

.fortschritt-widget-header:hover {
  background: rgba(255, 255, 255, 0.3);
}

.fortschritt-widget-header h3 {
  margin: 0;
  color: #333;
  border: none;
  padding: 0;
}

.fortschritt-toggle {
  font-size: 1.5em;
  font-weight: bold;
  color: #666;
}

.fortschritt-widget-content {
  padding: 0 20px 20px 20px;
  border-top: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-einleitung {
  background: rgba(255, 255, 255, 0.6);
  padding: 14px 16px;
  border-radius: 8px;
  margin-bottom: 16px;
  border-left: 4px solid #ffd700;
}

.fortschritt-einleitung p {
  margin: 0 0 8px 0;
  font-size: 0.95em;
  line-height: 1.5;
}

.fortschritt-einleitung p:last-child {
  margin-bottom: 0;
}

.fortschritt-import-export {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-io-btn {
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid #dee2e6;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 0.9em;
  cursor: pointer;
  transition: all 0.2s;
  margin: 0;
}

.fortschritt-io-btn:hover {
  border-color: #ffd700;
  background: white;
}

.fortschritt-file-input {
  display: none;
}

.fortschritt-skript-erklaerung {
  margin-top: 12px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  overflow: hidden;
  background: #f8f9fa;
}

.fortschritt-skript-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  cursor: pointer;
  user-select: none;
}

.fortschritt-skript-header:hover {
  background: #e9ecef;
}

.fortschritt-skript-header h4 {
  margin: 0;
  font-size: 0.95em;
  color: #333;
}

.fortschritt-skript-content {
  padding: 0 16px 16px 16px;
  border-top: 1px solid #dee2e6;
}

.fortschritt-skript-download {
  margin: 12px 0 16px 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.fortschritt-skript-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  background: #ffd700;
  color: #333;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  border: 2px solid #e6c200;
  transition: background 0.2s, border-color 0.2s;
}

.fortschritt-skript-btn:hover {
  background: #ffe033;
  border-color: #ffd700;
}

.fortschritt-skript-btn-hint {
  font-size: 0.85em;
  color: #666;
}

.fortschritt-skript-content p {
  margin: 12px 0 0 0;
  font-size: 0.9em;
  line-height: 1.6;
  color: #444;
}

.fortschritt-skript-content ol {
  margin: 8px 0 0 0;
  padding-left: 20px;
}

.fortschritt-skript-content li {
  margin-bottom: 10px;
  font-size: 0.9em;
  line-height: 1.6;
}

.fortschritt-skript-content pre {
  margin: 6px 0 0 0;
  padding: 8px 12px;
  background: #e9ecef;
  border-radius: 4px;
  font-size: 0.85em;
  overflow-x: auto;
}

.fortschritt-skript-content code {
  background: #e9ecef;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.9em;
}

.fortschritt-skript-details {
  font-size: 0.85em;
  color: #666;
  margin-top: 12px;
}

.fortschritt-variant-selector {
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-variant-label {
  display: block;
  font-size: 0.9em;
  font-weight: 600;
  color: #555;
  margin-bottom: 10px;
}

.fortschritt-variant-buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.fortschritt-variant-btn {
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid #dee2e6;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s;
}

.fortschritt-variant-btn:hover {
  border-color: #ffd700;
  background: rgba(255, 255, 255, 1);
}

.fortschritt-variant-btn.active {
  background: #ffd700;
  border-color: #ffd700;
  font-weight: 600;
  color: #333;
}

.fortschritt-variants {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  margin: 15px 0;
}

.fortschritt-variant {
  background: rgba(255, 255, 255, 0.8);
  padding: 10px 16px;
  border-radius: 8px;
  border: 1px solid #eee;
  font-weight: 600;
}

.variant-label {
  margin-right: 8px;
}

.variant-points {
  color: #ff4136;
}

.variant-items {
  font-size: 0.9em;
  color: #666;
  margin-left: 4px;
}

.fortschritt-weekly-section {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-weekly-section h4 {
  margin: 0 0 6px 0;
  font-size: 1em;
  color: #333;
}

.fortschritt-weekly-hint {
  margin: 0 0 16px 0;
  font-size: 0.85em;
  color: #666;
}

.fortschritt-by-week h5 {
  margin: 12px 0 8px 0;
  font-size: 0.95em;
  color: #555;
}

.week-progress-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 10px;
}

.week-progress-card {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
}

.week-progress-card.has-claims {
  border-color: #c8e6c9;
  background: rgba(232, 245, 233, 0.6);
}

.week-progress-card.complete {
  border-color: #2e7d32;
  background: rgba(200, 230, 201, 0.8);
}

.week-progress-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  padding: 10px 12px;
  cursor: pointer;
  font-size: 0.9em;
}

.week-progress-header:hover {
  background: rgba(255, 255, 255, 0.7);
}

.week-number {
  font-weight: 600;
  color: #333;
  min-width: 65px;
}

.week-stats {
  color: #2e7d32;
  font-weight: 600;
}

.week-open {
  font-size: 0.85em;
  color: #666;
}

.week-open.complete {
  color: #2e7d32;
}

.week-toggle {
  margin-left: auto;
  font-weight: bold;
  color: #999;
}

.week-progress-detail {
  padding: 0 12px 12px 12px;
  border-top: 1px solid rgba(0, 0, 0, 0.06);
}

.week-progress-detail ul {
  margin: 8px 0 0 0;
  padding-left: 18px;
}

.week-no-claims {
  margin: 8px 0 0 0;
  font-size: 0.9em;
  color: #999;
  font-style: italic;
}

.fortschritt-details {
  margin-top: 16px;
}

.fortschritt-variant-detail {
  background: rgba(255, 255, 255, 0.9);
  padding: 16px;
  border-radius: 8px;
  border: 1px solid #eee;
  margin-bottom: 12px;
}

.fortschritt-variant-detail h4 {
  margin: 0 0 10px 0;
  font-size: 1em;
  color: #555;
}

.fortschritt-variant-detail .items-header {
  margin-top: 16px;
  margin-bottom: 8px;
}

.fortschritt-claims-list,
.fortschritt-items-list {
  margin: 0 0 0 4px;
  padding-left: 20px;
}

.fortschritt-claims-list li,
.fortschritt-items-list li {
  margin-bottom: 6px;
}

.claim-label {
  font-weight: 600;
  color: #333;
  margin-right: 6px;
}

.claim-reward {
  color: #666;
}

.fortschritt-hint {
  margin: 15px 0 0 0;
  font-size: 0.9em;
  color: #666;
}
</style>
