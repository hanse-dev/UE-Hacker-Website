<template>
  <section class="stolperstellen">
    <p class="muted">{{ t('admin.stats.hint') }}</p>
    <div class="stats-toolbar">
      <input v-model="filter" class="stats-filter" :placeholder="t('admin.stats.filter')">
      <label class="stats-min">
        <input v-model="onlyEnough" type="checkbox">
        {{ t('admin.stats.onlyEnough').replace('{n}', MIN_KIDS) }}
      </label>
      <button type="button" class="btn-secondary" :disabled="busy" @click="refresh">{{ t('admin.stats.refresh') }}</button>
    </div>
    <p v-if="error" class="error">{{ error }}</p>
    <table v-if="visibleRows.length" class="stats-table">
      <thead>
        <tr>
          <th>{{ t('admin.stats.col.task') }}</th>
          <th :title="t('admin.stats.col.kidsHint')">{{ t('admin.stats.col.kids') }}</th>
          <th>{{ t('admin.stats.col.fails') }}</th>
          <th>{{ t('admin.stats.col.skipped') }}</th>
          <th>{{ t('admin.stats.col.solutions') }}</th>
          <th />
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="row in visibleRows"
          :key="row.key"
          :data-stats-row="row.key"
          :class="{ 'few-kids': row.kids < MIN_KIDS }"
        >
          <td>
            <div class="stats-course">{{ row.course }} · {{ row.lessonTitle }}</div>
            <div class="stats-task">{{ t('admin.stats.taskNo').replace('{n}', row.task + 1) }}: {{ row.instruction }}</div>
          </td>
          <td>{{ row.kids }}<span v-if="row.opens" class="muted"> / {{ row.opens }}</span></td>
          <td data-col="fails">{{ row.failsPerKid.toFixed(1) }}</td>
          <td data-col="skipped">{{ row.skipped }}</td>
          <td data-col="solutions">{{ row.solutions }}</td>
          <td><button type="button" class="btn-link" @click="reset(row)">{{ t('admin.stats.reset') }}</button></td>
        </tr>
      </tbody>
    </table>
    <p v-else-if="!busy" class="muted">{{ t('admin.stats.empty') }}</p>
  </section>
</template>

<script>
import { computed, onMounted, ref } from 'vue';
import { useLanguage } from '../composables/useLanguage';
import { listTaskStats, resetTaskStats } from '../composables/useAdminApi.js';

const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');
// Unter so vielen Kindern ist eine Zahl Zufall - die Zeile wird blass angezeigt.
const MIN_KIDS = 3;

// Je Aufgabe ein Wert, nach dem sortiert wird: Fehlversuche zählen einfach, eine angesehene Lösung
// doppelt, Überspringen dreifach - jeweils pro Kind, das die Aufgabe abgeschlossen hat.
function struggleScore({ fails, skipped, solutions, kids }) {
  return (fails + 2 * solutions + 3 * skipped) / Math.max(1, kids);
}

export default {
  name: 'AdminStolperstellen',
  setup() {
    const { t } = useLanguage();
    const rows = ref([]);
    const busy = ref(false);
    const error = ref('');
    const filter = ref('');
    const onlyEnough = ref(false);
    const lessonsByCourse = {};

    const loadLessons = async (course) => {
      if (course in lessonsByCourse) return lessonsByCourse[course];
      const loader = lessonJsonModules[`../../content/${course}/lessons.json`];
      lessonsByCourse[course] = loader ? (await loader()).default : [];
      return lessonsByCourse[course];
    };

    const refresh = async () => {
      busy.value = true;
      error.value = '';
      try {
        const data = await listTaskStats();
        const enriched = [];
        for (const r of data.rows) {
          const lessons = await loadLessons(r.course);
          const lesson = lessons.find((l) => l.id === r.lesson);
          const kids = r.solved + r.skipped;
          enriched.push({
            ...r,
            key: `${r.course}|${r.lesson}|${r.task}`,
            lessonTitle: lesson?.title || r.lesson,
            instruction: lesson?.tasks?.[r.task]?.instruction || '',
            kids,
            failsPerKid: r.fails / Math.max(1, kids),
            score: struggleScore({ ...r, kids }),
          });
        }
        rows.value = enriched.sort((a, b) => b.score - a.score);
      } catch (e) {
        error.value = e.message;
      } finally {
        busy.value = false;
      }
    };

    const visibleRows = computed(() => rows.value.filter((r) => (!onlyEnough.value || r.kids >= MIN_KIDS)
      && (!filter.value || `${r.course} ${r.lessonTitle}`.toLowerCase().includes(filter.value.toLowerCase()))));

    const reset = async (row) => {
      if (!window.confirm(t('admin.stats.resetConfirm'))) return;
      await resetTaskStats(row.course, row.lesson, row.task);
      await refresh();
    };

    onMounted(refresh);
    return { t, MIN_KIDS, busy, error, filter, onlyEnough, visibleRows, refresh, reset };
  },
};
</script>

<style scoped>
.stats-toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin: 12px 0 16px;
}

.stats-filter {
  flex: 1 1 200px;
  padding: 8px 10px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--surface);
  color: var(--text);
}

.stats-min {
  display: flex;
  gap: 6px;
  align-items: center;
}

.btn-secondary {
  border: none;
  border-radius: 6px;
  padding: 10px 16px;
  font-weight: 600;
  cursor: pointer;
  background: var(--surface-muted);
  color: var(--text);
}

.btn-link {
  border: none;
  background: none;
  color: var(--brand-text);
  cursor: pointer;
  padding: 0;
}

.stats-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--surface);
}

.stats-table th,
.stats-table td {
  text-align: left;
  padding: 10px 12px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}

.stats-course {
  font-size: 0.85em;
  color: var(--text-muted);
}

.few-kids {
  opacity: 0.55;
}

.muted {
  color: var(--text-muted);
}

.error {
  color: var(--danger-text);
  background: var(--danger-bg);
  padding: 8px 10px;
  border-radius: 6px;
}
</style>
