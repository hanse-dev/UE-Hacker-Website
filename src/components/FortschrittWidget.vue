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
          <div v-if="isLoggedIn" class="certificate-name-field">
            <label for="certificate-name-input">{{ t('progress.certificate.name.label') }}</label>
            <input
              id="certificate-name-input"
              type="text"
              :value="certificateName"
              @input="setCertificateName($event.target.value)"
              class="certificate-name-input"
            />
          </div>
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
              <template v-if="isCertificateEarned(w)">
                <button
                  v-if="isLoggedIn"
                  class="btn-certificate-pdf"
                  :disabled="pdfBusyWeek === w"
                  @click="onDownloadPdf(w)"
                >
                  {{ pdfBusyWeek === w ? t('progress.certificate.generating') : t('progress.certificate.download') }}
                </button>
                <span v-else class="certificate-login-hint">{{ t('progress.certificate.loginRequired') }}</span>
              </template>
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
import { useAuth } from '../composables/useAuth.js';
import { downloadCertificatePdf } from '../composables/useCertificatePdf.js';

const CERTIFICATE_NAME_KEY = 'ue-hacker-certificate-name';

export default {
  name: 'FortschrittWidget',
  props: {
    weeks: {
      type: Array,
      default: () => [],
    },
    startExpanded: {
      type: Boolean,
      default: false,
    },
  },
  setup(props) {
    const { t, lang } = useLanguage();
    const { isLoggedIn, user } = useAuth();
    const fortschrittExpanded = ref(props.startExpanded);
    const weeklySectionExpanded = ref(props.startExpanded);
    const pdfBusyWeek = ref(null);

    const { exportProgress, importProgress } = useFortschritt();
    const { isCertificateEarned, countCertificates } = useZertifikate();

    const certificateName = ref(
      localStorage.getItem(CERTIFICATE_NAME_KEY) || user.value?.username || ''
    );

    const setCertificateName = (value) => {
      certificateName.value = value;
      localStorage.setItem(CERTIFICATE_NAME_KEY, value);
    };

    const getWeekData = (weekNumber) => {
      const match = props.weeks.find((week) => {
        const num = parseInt((week.title || '').match(/\d+/)?.[0], 10);
        return num === weekNumber;
      });
      return match || props.weeks[weekNumber - 1] || null;
    };

    const onDownloadPdf = async (weekNumber) => {
      pdfBusyWeek.value = weekNumber;
      try {
        const weekData = getWeekData(weekNumber);
        await downloadCertificatePdf({
          weekNumber,
          weekTitle: weekData?.title || `${t('week.label')} ${weekNumber}`,
          lernziele: weekData?.lernzieleFull || [],
          learnerName: certificateName.value || user.value?.username || '',
          lang: lang.value,
        });
      } finally {
        pdfBusyWeek.value = null;
      }
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
      isLoggedIn,
      certificateName,
      setCertificateName,
      pdfBusyWeek,
      onDownloadPdf,
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

.certificate-name-field {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  margin: 0 0 16px 0;
}

.certificate-name-field label {
  font-size: 0.85em;
  color: #555;
  font-weight: 600;
}

.certificate-name-input {
  flex: 1;
  min-width: 180px;
  padding: 8px 10px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 0.9em;
}

.btn-certificate-pdf {
  margin-top: 4px;
  background: #7c3aed;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 0.75em;
  cursor: pointer;
}

.btn-certificate-pdf:hover:not(:disabled) {
  background: #6d28d9;
}

.btn-certificate-pdf:disabled {
  opacity: 0.6;
  cursor: default;
}

.certificate-login-hint {
  margin-top: 4px;
  font-size: 0.7em;
  color: #888;
  font-style: italic;
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
