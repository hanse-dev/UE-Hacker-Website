<template>
  <div class="fortschritt-widget">
    <div class="fortschritt-widget-header" @click="fortschrittExpanded = !fortschrittExpanded">
      <h3>{{ t('progress.title') }}</h3>
      <span class="fortschritt-toggle">{{ fortschrittExpanded ? '−' : '+' }}</span>
    </div>
    <div v-show="fortschrittExpanded" class="fortschritt-widget-content">
      <div class="fortschritt-einleitung">
        <p><strong>{{ t('progress.intro1.label') }}</strong> {{ t('progress.intro1') }}</p>
        <p>{{ t('progress.intro2') }}</p>
      </div>
      <div class="fortschritt-import-export">
        <button @click="exportFortschritt" class="fortschritt-io-btn">
          {{ t('progress.export') }}
        </button>
        <label class="fortschritt-io-btn">
          {{ t('progress.import') }}
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
          <h4>{{ t('progress.script.title') }}</h4>
          <span class="fortschritt-toggle">{{ skriptErklaerungExpanded ? '−' : '+' }}</span>
        </div>
        <div v-show="skriptErklaerungExpanded" class="fortschritt-skript-content">
          <div class="fortschritt-skript-download">
            <a href="/fortschritt-script.zip" download class="fortschritt-skript-btn">
              {{ t('progress.script.download') }}
            </a>
            <span class="fortschritt-skript-btn-hint">{{ t('progress.script.hint') }}</span>
          </div>
          <p>{{ t('progress.script.p1') }}</p>
          <ol>
            <li><strong>{{ t('progress.script.step1') }}</strong>
              <pre><code>python fortschritt.py</code></pre>
              {{ t('progress.script.step1.detail') }}
            </li>
            <li><strong>{{ t('progress.script.step2') }}</strong>: {{ t('progress.script.step2.detail') }}</li>
          </ol>
          <p class="fortschritt-skript-details">{{ t('progress.script.details') }}</p>
        </div>
      </div>

      <div class="fortschritt-variant-selector">
        <span class="fortschritt-variant-label">{{ t('progress.variant.label') }}</span>
        <div class="fortschritt-variant-buttons">
          <button
            @click="selectedFortschrittVariant = 'alle'"
            :class="{ active: selectedFortschrittVariant === 'alle' }"
            class="fortschritt-variant-btn"
          >
            {{ t('progress.variant.all') }}
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
          <span class="variant-certificate-count">{{ countCertificates(lang, v) }}/12 🎓</span>
        </div>
      </div>

      <div class="fortschritt-weekly-section">
        <div class="fortschritt-weekly-header" @click="weeklySectionExpanded = !weeklySectionExpanded">
          <h4>{{ t('progress.weekly.title') }}</h4>
          <span class="fortschritt-toggle">{{ weeklySectionExpanded ? '−' : '+' }}</span>
        </div>
        <div v-show="weeklySectionExpanded">
          <p class="fortschritt-weekly-hint">{{ t('progress.weekly.hint') }}</p>
          <div class="weekly-tabs">
            <button
              v-for="v in variantKeys"
              :key="v"
              class="weekly-tab-btn"
              :class="{ active: weeklyTabVariant === v }"
              @click="weeklyTabVariant = v"
            >{{ variantLabels[v] }}</button>
          </div>
          <div class="certificate-grid">
            <div
              v-for="w in 12"
              :key="`${weeklyTabVariant}-w${w}`"
              class="certificate-card"
              :class="{ earned: isCertificateEarned(lang, weeklyTabVariant, w) }"
            >
              <span class="certificate-icon">{{ isCertificateEarned(lang, weeklyTabVariant, w) ? '🎓' : '🔒' }}</span>
              <span class="certificate-week">{{ t('week.label') }} {{ w }}</span>
              <span class="certificate-status">
                {{ isCertificateEarned(lang, weeklyTabVariant, w) ? t('progress.week.certificate.earned') : t('progress.week.certificate.locked') }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <p class="fortschritt-hint" v-if="getTotalCertificates() === 0">{{ t('progress.hint') }}</p>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useFortschritt } from '../composables/useFortschritt';
import { useZertifikate } from '../composables/useZertifikate';
import { useLanguage } from '../composables/useLanguage.js';

const VARIANT_KEYS = ['abenteuer', 'pferde', 'scifi'];

export default {
  name: 'FortschrittWidget',
  setup() {
    const { t, lang } = useLanguage();
    const fortschrittExpanded = ref(false);
    const skriptErklaerungExpanded = ref(false);
    const weeklySectionExpanded = ref(false);
    const weeklyTabVariant = ref('abenteuer');
    const selectedFortschrittVariant = ref('alle');

    const { exportProgress, importProgress } = useFortschritt();
    const { ensureManifestLoaded, isCertificateEarned, countCertificates } = useZertifikate();
    ensureManifestLoaded(lang.value);

    const variantLabels = computed(() => ({
      abenteuer: t('variant.adventure'),
      pferde:    t('variant.horses'),
      scifi:     t('variant.scifi'),
    }));

    const displayedVariantKeys = computed(() =>
      selectedFortschrittVariant.value === 'alle' ? VARIANT_KEYS : [selectedFortschrittVariant.value]
    );

    const getTotalCertificates = () =>
      VARIANT_KEYS.reduce((n, v) => n + countCertificates(lang.value, v), 0);

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
          alert(t('progress.import.success'));
        } else {
          alert(t('progress.import.failure') + ' ' + (result.error || '?'));
        }
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };

    return {
      fortschrittExpanded,
      skriptErklaerungExpanded,
      weeklySectionExpanded,
      weeklyTabVariant,
      selectedFortschrittVariant,
      displayedVariantKeys,
      variantKeys: VARIANT_KEYS,
      variantLabels,
      lang,
      isCertificateEarned,
      countCertificates,
      getTotalCertificates,
      exportFortschritt,
      onImportFile,
      t,
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

.variant-certificate-count {
  color: #7c3aed;
}

.fortschritt-weekly-section {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-weekly-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  user-select: none;
  padding: 6px 0;
}

.fortschritt-weekly-header:hover h4 {
  color: #555;
}

.fortschritt-weekly-section h4 {
  margin: 0;
  font-size: 1em;
  color: #333;
}

.fortschritt-weekly-hint {
  margin: 0 0 16px 0;
  font-size: 0.85em;
  color: #666;
}

.weekly-tabs {
  display: flex;
  gap: 0;
  border-bottom: 2px solid rgba(255, 215, 0, 0.6);
  margin: 10px 0 0;
}

.weekly-tab-btn {
  padding: 8px 16px;
  border: none;
  border-bottom: 3px solid transparent;
  background: transparent;
  cursor: pointer;
  font-size: 0.88em;
  font-weight: 500;
  color: #666;
  margin-bottom: -2px;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.weekly-tab-btn:hover {
  color: #333;
  background: rgba(255, 255, 255, 0.5);
}

.weekly-tab-btn.active {
  color: #7a5c00;
  border-bottom-color: #ffd700;
  font-weight: 700;
  background: rgba(255, 255, 255, 0.5);
}

.certificate-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 10px;
  padding-top: 12px;
}

.certificate-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 14px 10px;
  text-align: center;
}

.certificate-card.earned {
  border-color: #c4b5fd;
  background: rgba(237, 233, 254, 0.8);
}

.certificate-icon {
  font-size: 1.8em;
}

.certificate-week {
  font-weight: 600;
  color: #333;
  font-size: 0.9em;
}

.certificate-status {
  font-size: 0.78em;
  color: #666;
}

.certificate-card.earned .certificate-status {
  color: #5b21b6;
  font-weight: 600;
}

.fortschritt-hint {
  margin: 15px 0 0 0;
  font-size: 0.9em;
  color: #666;
}
</style>
