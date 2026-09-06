<template>
  <div class="variant-selector">
    <button
      v-if="week.hasAbenteuerVariant"
      @click="$emit('set-variant', 'abenteuer')"
      :class="{ active: week.selectedVariant === 'abenteuer' }"
      class="variant-btn"
    >{{ t('variant.adventure') }}</button>
    <button
      v-if="week.hasPferdeVariant"
      @click="$emit('set-variant', 'pferde')"
      :class="{ active: week.selectedVariant === 'pferde' }"
      class="variant-btn"
    >{{ t('variant.horses') }}</button>
    <button
      v-if="week.hasScifiVariant"
      @click="$emit('set-variant', 'scifi')"
      :class="{ active: week.selectedVariant === 'scifi' }"
      class="variant-btn"
    >{{ t('variant.scifi') }}</button>
  </div>
</template>

<script>
import { useLanguage } from '../composables/useLanguage.js';

export default {
  name: 'VariantSelector',
  props: {
    week: { type: Object, required: true },
  },
  emits: ['set-variant'],
  setup() {
    const { t } = useLanguage();
    return { t };
  },
};
</script>

<style scoped>
.variant-selector {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.variant-btn {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  padding: 8px 18px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 6px;
  font-weight: 500;
}

.variant-btn:hover {
  background: #e9ecef;
  border-color: #ff4136;
}

.variant-btn.active {
  background: #ff4136;
  color: white;
  border-color: #ff4136;
  font-weight: 700;
}
</style>
