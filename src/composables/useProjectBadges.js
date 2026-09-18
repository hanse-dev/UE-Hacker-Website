import { ref, computed } from 'vue';
import { assetUrl } from '../utils/assetUrl';
import { useInteractiveProgress } from './useInteractiveProgress';

// Gleiches Wildcard-Glob wie ProjekteView.vue - ein neuer Projekt-Kurs braucht hier keine Aenderung.
const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');

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

/**
 * Ein Abzeichen pro Projekt-Kurs, verdient sobald alle seine Lektionen abgeschlossen sind
 * (useInteractiveProgress, gleicher Fortschritts-Mechanismus wie ProjectCourse.vue selbst nutzt -
 * kein eigenes, zweites Punktesystem). Bewusst kein PDF/Login-Zwang wie beim 12-Wochen-Zertifikat:
 * Projekt-Kurse sind laut VISION.md niedrigschwellig, ein leichtes Abzeichen reicht.
 */
export function useProjectBadges() {
  const badges = ref([]);
  const loading = ref(true);

  const load = async () => {
    loading.value = true;
    try {
      const response = await fetch(assetUrl('kurse.json'));
      const kurse = await response.json();
      const projekte = kurse.filter((k) => k.type === 'projekt');
      badges.value = await Promise.all(
        projekte.map(async (p) => {
          const totalLessons = await loadLessonCount(p.contentPath);
          const { completedCount } = useInteractiveProgress(p.contentPath, p.id);
          return {
            id: p.id,
            title: p.title,
            title_en: p.title_en,
            contentPath: p.contentPath,
            totalLessons,
            completedCount: completedCount.value,
            earned: totalLessons > 0 && completedCount.value >= totalLessons,
          };
        })
      );
    } catch (e) {
      console.error('Could not load project badges:', e);
      badges.value = [];
    } finally {
      loading.value = false;
    }
  };

  const earnedCount = computed(() => badges.value.filter((b) => b.earned).length);

  return { badges, loading, earnedCount, load };
}
