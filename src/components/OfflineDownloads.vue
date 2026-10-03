<template>
  <div class="offline-downloads">
    <span class="offline-downloads-title">{{ t('offline.title') }}</span>
    <div class="offline-downloads-buttons">
      <a
        v-for="format in FORMATS"
        :key="format"
        :href="`${base}-${format}.zip`"
        :data-offline-format="format"
        class="btn-offline-download"
        download
      >
        {{ t(`offline.${format}`) }}
      </a>
    </div>
    <span class="offline-downloads-hint">{{ t('offline.hint') }}</span>
  </div>
</template>

<script>
import { useLanguage } from '../composables/useLanguage';

// Reihenfolge = Reihenfolge der Buttons. Die ZIPs baut scripts/pack_notebooks.py als
// `<base>-<format>.zip` (z.B. /wochen-zips/woche-4-notebooks.zip).
export const OFFLINE_FORMATS = ['notebooks', 'komplett', 'einzeln'];

export default {
  name: 'OfflineDownloads',
  props: {
    // URL-Praefix ohne Format-Endung, z.B. "/wochen-zips/woche-4-en" oder "/projekt-zips/morsecode"
    base: { type: String, required: true },
  },
  setup() {
    const { t } = useLanguage();
    return { t, FORMATS: OFFLINE_FORMATS };
  },
};
</script>

<style scoped>
.offline-downloads {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 18px 0 4px;
}

.offline-downloads-title {
  font-weight: 600;
  color: #374151;
}

.offline-downloads-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.btn-offline-download {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  padding: 6px 14px;
  font-size: 0.9em;
  color: var(--primary-purple, #4a2274);
  text-decoration: none;
  white-space: nowrap;
  transition: background 0.15s, border-color 0.15s;
}

.btn-offline-download:hover {
  background: #e9ecef;
  border-color: var(--primary-purple, #4a2274);
}

.offline-downloads-hint {
  font-size: 0.8em;
  color: #888;
}
</style>
