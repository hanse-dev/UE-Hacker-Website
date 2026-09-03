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
      <div class="fortschritt-summary">
        <span class="certificate-count">{{ countCertificates() }}/12 🎓</span>
      </div>

      <div class="fortschritt-weekly-section">
        <div class="fortschritt-weekly-header" @click="weeklySectionExpanded = !weeklySectionExpanded">
          <h4>{{ t('progress.weekly.title') }}</h4>
          <span class="fortschritt-toggle">{{ weeklySectionExpanded ? '−' : '+' }}</span>
        </div>
        <div v-show="weeklySectionExpanded">
          <p class="fortschritt-weekly-hint">{{ t('progress.weekly.hint') }}</p>
          <div class="certificate-grid">
            <div
              v-for="w in 12"
              :key="w"
              class="certificate-card"
              :class="{ earned: isCertificateEarned(w) }"
            >
              <span class="certificate-icon">{{ isCertificateEarned(w) ? '🎓' : '🔒' }}</span>
              <span class="certificate-week">{{ t('week.label') }} {{ w }}</span>
              <span class="certificate-status">
                {{ isCertificateEarned(w) ? t('progress.week.certificate.earned') : t('progress.week.certificate.locked') }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <p class="fortschritt-hint" v-if="countCertificates() === 0">{{ t('progress.hint') }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useFortschritt } from '../composables/useFortschritt';
import { useZertifikate } from '../composables/useZertifikate';
import { useLanguage } from '../composables/useLanguage.js';

export default {
  name: 'FortschrittWidget',
  setup() {
    const { t } = useLanguage();
    const fortschrittExpanded = ref(false);
    const weeklySectionExpanded = ref(false);

    const { exportProgress, importProgress } = useFortschritt();
    const { isCertificateEarned, countCertificates } = useZertifikate();

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
      weeklySectionExpanded,
      isCertificateEarned,
      countCertificates,
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

.fortschritt-skript-details {
  font-size: 0.85em;
  color: #666;
  margin-top: 12px;
}

.fortschritt-summary {
  margin: 15px 0;
}

.certificate-count {
  background: rgba(255, 255, 255, 0.8);
  padding: 10px 16px;
  border-radius: 8px;
  border: 1px solid #eee;
  font-weight: 600;
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
