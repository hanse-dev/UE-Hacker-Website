<template>
  <aside class="concept-box">
    <h3 class="concept-box-title">{{ title || t('concepts.title') }}</h3>
    <ul class="concept-box-list">
      <li v-for="c in concepts" :key="c.kurs + c.begriff" class="concept-box-item">
        <strong>{{ c.begriff }}</strong> – {{ c.erklaerung }}
        <a class="concept-box-link" :href="href(c)" target="_blank" rel="noopener">
          <template v-if="c.woche">{{ name(c) }}, {{ t('concepts.week').replace('{n}', c.woche) }}: {{ c.lektion }} ↗</template>
          <template v-else>{{ name(c) }} ↗</template>
        </a>
      </li>
    </ul>
  </aside>
</template>

<script>
import { useLanguage } from '../composables/useLanguage';
import { conceptHref, courseName } from '../composables/useConcepts';

// "Neu oder unklar?"-Kasten am Ende einer Projekt-Lektion: alle Begriffe der Lektion mit einem
// Satz Erklärung und Link auf die Grundkurs-Woche bzw. den micro:bit-Spickzettel (siehe
// useConcepts.js, content/begriffe.json).
export default {
  name: 'ConceptBox',
  props: {
    concepts: { type: Array, required: true },
    title: { type: String, default: '' },
  },
  setup() {
    const { t } = useLanguage();
    return { t, href: conceptHref, name: courseName };
  },
};
</script>

<style scoped>
.concept-box {
  margin-top: 24px;
  padding: 14px 18px;
  background: var(--surface-tint);
  border: 1px solid var(--border-tint);
  border-radius: 8px;
}

.concept-box-title {
  margin: 0 0 8px 0;
  font-size: 1em;
  color: var(--brand-text);
}

.concept-box-list {
  margin: 0;
  padding-left: 18px;
}

.concept-box-item {
  margin-bottom: 6px;
  line-height: 1.5;
}

.concept-box-link {
  display: inline-block;
  margin-left: 4px;
  font-size: 0.9em;
  color: var(--brand-text);
}
</style>
