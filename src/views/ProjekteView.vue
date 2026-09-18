<template>
  <div class="projekte-view">
    <section id="projekte-hero">
      <h2>{{ t('projekte.title') }}</h2>
      <p>{{ t('projekte.intro') }}</p>
    </section>

    <section v-if="!loading" class="projekte-filters">
      <div class="filter-group">
        <span class="filter-label">{{ t('projekte.filter.language') }}</span>
        <div class="filter-chips">
          <button
            v-for="lang_ in languageOptions"
            :key="lang_"
            type="button"
            class="filter-chip"
            :class="{ active: selectedLanguages.includes(lang_) }"
            @click="toggle(selectedLanguages, lang_)"
          >
            {{ languageLabel(lang_) }}
          </button>
        </div>
      </div>

      <div class="filter-group">
        <span class="filter-label">{{ t('projekte.filter.level') }}</span>
        <div class="filter-chips">
          <button
            v-for="level in levelOptions"
            :key="level"
            type="button"
            class="filter-chip"
            :class="{ active: selectedLevels.includes(level) }"
            @click="toggle(selectedLevels, level)"
          >
            {{ t(`projectLevel.${level}`) }}
          </button>
        </div>
      </div>

      <div class="filter-group">
        <span class="filter-label">{{ t('projekte.filter.tags') }}</span>
        <div class="filter-chips">
          <button
            v-for="tag in tagOptions"
            :key="tag"
            type="button"
            class="filter-chip"
            :class="{ active: selectedTags.includes(tag) }"
            @click="toggle(selectedTags, tag)"
          >
            {{ t(`projectTag.${tag}`) }}
          </button>
        </div>
      </div>

      <div class="filter-group">
        <span class="filter-label">{{ t('projekte.filter.duration') }}</span>
        <div class="filter-chips">
          <button
            v-for="duration in durationOptions"
            :key="duration"
            type="button"
            class="filter-chip"
            :class="{ active: selectedDurations.includes(duration) }"
            @click="toggle(selectedDurations, duration)"
          >
            {{ t(`projectDuration.${duration}`) }}
          </button>
        </div>
      </div>

      <button
        v-if="hasActiveFilters"
        type="button"
        class="filter-reset"
        @click="resetFilters"
      >
        {{ t('projekte.filter.reset') }}
      </button>
    </section>

    <p v-if="!loading" class="projekte-count">
      {{ filteredProjects.length }} {{ t('projekte.of') }} {{ projects.length }}
    </p>

    <section id="projekte-liste">
      <div v-if="loading" class="loading">{{ t('projekte.loading') }}</div>
      <p v-else-if="!filteredProjects.length" class="projekte-empty">{{ t('projekte.noResults') }}</p>
      <div v-else class="course-list">
        <div v-for="projekt in filteredProjects" :key="projekt.id" class="course-card projekt-card">
          <div class="projekt-badges">
            <span class="badge badge-language">{{ languageLabel(projekt.language) }}</span>
            <span class="badge badge-level">{{ t(`projectLevel.${projekt.level}`) }}</span>
            <span class="badge badge-duration">{{ t(`projectDuration.${projekt.duration}`) }}</span>
          </div>
          <h3>{{ lang === 'en' && projekt.title_en ? projekt.title_en : projekt.title }}</h3>
          <p>{{ lang === 'en' && projekt.description_en ? projekt.description_en : projekt.description }}</p>
          <div class="projekt-tags">
            <span v-for="tag in projekt.tags" :key="tag" class="tag-chip">{{ t(`projectTag.${tag}`) }}</span>
          </div>
          <p class="projekt-lessons">{{ projekt.lessonCount }} {{ t('projekte.lessonsLabel') }}</p>
          <router-link :to="`/kurs/${projekt.id}`" class="course-link">{{ t('projekte.startBtn') }}</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { assetUrl } from '../utils/assetUrl';
import { useLanguage } from '../composables/useLanguage.js';

const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');

const LEVEL_ORDER = ['einsteiger', 'fortgeschritten'];
const DURATION_ORDER = ['kurz', 'mittel', 'laenger'];
const LANGUAGE_LABELS = { python: 'Python', javascript: 'JavaScript' };

function durationBucket(lessonCount) {
  if (lessonCount <= 5) return 'kurz';
  if (lessonCount <= 9) return 'mittel';
  return 'laenger';
}

async function loadLessonCount(contentPath) {
  const key = `../../content/${contentPath}/lessons.json`;
  const loader = lessonJsonModules[key];
  if (!loader) return 0;
  try {
    const mod = await loader();
    return (mod.default || []).length;
  } catch {
    return 0;
  }
}

export default {
  name: 'ProjekteView',
  setup() {
    const { lang, t } = useLanguage();
    const projects = ref([]);
    const loading = ref(true);

    const selectedLanguages = ref([]);
    const selectedLevels = ref([]);
    const selectedTags = ref([]);
    const selectedDurations = ref([]);

    const languageOptions = computed(() =>
      [...new Set(projects.value.map((p) => p.language))].sort()
    );
    const levelOptions = computed(() =>
      LEVEL_ORDER.filter((level) => projects.value.some((p) => p.level === level))
    );
    const tagOptions = computed(() =>
      [...new Set(projects.value.flatMap((p) => p.tags || []))].sort()
    );
    const durationOptions = computed(() =>
      DURATION_ORDER.filter((duration) => projects.value.some((p) => p.duration === duration))
    );

    const hasActiveFilters = computed(
      () =>
        selectedLanguages.value.length ||
        selectedLevels.value.length ||
        selectedTags.value.length ||
        selectedDurations.value.length
    );

    const filteredProjects = computed(() =>
      projects.value.filter((p) => {
        if (selectedLanguages.value.length && !selectedLanguages.value.includes(p.language)) return false;
        if (selectedLevels.value.length && !selectedLevels.value.includes(p.level)) return false;
        if (selectedTags.value.length && !(p.tags || []).some((tag) => selectedTags.value.includes(tag))) return false;
        if (selectedDurations.value.length && !selectedDurations.value.includes(p.duration)) return false;
        return true;
      })
    );

    const toggle = (list, value) => {
      const idx = list.indexOf(value);
      if (idx === -1) list.push(value);
      else list.splice(idx, 1);
    };

    const resetFilters = () => {
      selectedLanguages.value = [];
      selectedLevels.value = [];
      selectedTags.value = [];
      selectedDurations.value = [];
    };

    const languageLabel = (slug) => LANGUAGE_LABELS[slug] || slug;

    const loadProjects = async () => {
      loading.value = true;
      try {
        const response = await fetch(assetUrl('kurse.json'));
        const kurse = await response.json();
        const projektKurse = kurse.filter((k) => k.type === 'projekt');
        projects.value = await Promise.all(
          projektKurse.map(async (p) => {
            const lessonCount = await loadLessonCount(p.contentPath);
            return { ...p, lessonCount, duration: durationBucket(lessonCount) };
          })
        );
      } catch (e) {
        console.error('Could not load Projekte:', e);
        projects.value = [];
      } finally {
        loading.value = false;
      }
    };

    onMounted(loadProjects);

    return {
      lang,
      t,
      projects,
      loading,
      selectedLanguages,
      selectedLevels,
      selectedTags,
      selectedDurations,
      languageOptions,
      levelOptions,
      tagOptions,
      durationOptions,
      hasActiveFilters,
      filteredProjects,
      toggle,
      resetFilters,
      languageLabel,
    };
  },
};
</script>

<style scoped>
.projekte-view {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

#projekte-hero {
  margin-bottom: 24px;
}

.projekte-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  align-items: flex-end;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 10px;
  padding: 16px 20px;
  margin-bottom: 16px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.filter-label {
  font-size: 0.85em;
  font-weight: 600;
  color: #555;
}

.filter-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.filter-chip {
  border: 1px solid var(--border-color, #ccc);
  background: white;
  border-radius: 999px;
  padding: 5px 12px;
  font-size: 0.85em;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border-color 0.2s;
}

.filter-chip:hover {
  border-color: var(--primary-purple, #4a2274);
}

.filter-chip.active {
  background: var(--primary-purple, #4a2274);
  border-color: var(--primary-purple, #4a2274);
  color: white;
}

.filter-reset {
  border: none;
  background: none;
  color: var(--accent-orange, #fb8c00);
  font-weight: 600;
  cursor: pointer;
  font-size: 0.85em;
  padding: 5px 0;
}

.filter-reset:hover {
  text-decoration: underline;
}

.projekte-count {
  color: #666;
  font-size: 0.9em;
  margin: 0 0 16px;
}

.projekte-empty {
  color: #666;
  padding: 20px 0;
}

.projekt-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 8px;
}

.badge {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 0.78em;
  font-weight: 600;
}

.badge-language {
  background: #e0f2fe;
  color: #075985;
}

.badge-level {
  background: #fef3c7;
  color: #92400e;
}

.badge-duration {
  background: #ede9fe;
  color: #5b21b6;
}

.projekt-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 8px 0;
}

.tag-chip {
  background: #f1f3f5;
  color: #495057;
  border-radius: 6px;
  padding: 2px 8px;
  font-size: 0.78em;
}

.projekt-lessons {
  color: #666;
  font-size: 0.85em;
  margin: 8px 0 12px;
}
</style>
