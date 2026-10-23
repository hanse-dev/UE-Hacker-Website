<template>
  <span class="beta-badge" :title="t('course.betaHint')">{{ t('course.beta') }}</span>
</template>

<script>
import { useLanguage } from '../composables/useLanguage.js';

// Kennzeichnet Kurse mit `"beta": true` in kurse.json: neu und noch nicht im Unterricht erprobt.
export default {
  name: 'BetaBadge',
  setup() {
    const { t } = useLanguage();
    return { t };
  },
};
</script>

<style scoped>
.beta-badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 999px;
  background: var(--warning-bg);
  color: var(--warning-text);
  font-size: 0.78rem;
  font-weight: 700;
  vertical-align: middle;
}
</style>
