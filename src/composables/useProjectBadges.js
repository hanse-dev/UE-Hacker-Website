import { ref, shallowRef, computed } from 'vue';
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
  // Stammdaten je Projekt plus der *lebende* Fortschritt (computed). Die Abzeichen werden daraus
  // berechnet, nicht beim Laden eingefroren: Kommt der Account-Fortschritt erst nach dem Öffnen
  // des Profils vom Server (Login, Neuladen), ziehen sie von selbst nach.
  const projects = shallowRef([]);
  const loading = ref(true);

  const load = async () => {
    loading.value = true;
    try {
      const response = await fetch(assetUrl('kurse.json'));
      const kurse = await response.json();
      const projekte = kurse.filter((k) => k.type === 'projekt');
      projects.value = await Promise.all(
        projekte.map(async (p) => ({
          id: p.id,
          title: p.title,
          title_en: p.title_en,
          contentPath: p.contentPath,
          totalLessons: await loadLessonCount(p.contentPath),
          unlisted: !!p.unlisted,
          progress: useInteractiveProgress(p.contentPath, p.id).completedCount,
        }))
      );
    } catch (e) {
      console.error('Could not load project badges:', e);
      projects.value = [];
    } finally {
      loading.value = false;
    }
  };

  const badges = computed(() =>
    projects.value
      .map(({ progress, ...p }) => ({
        ...p,
        completedCount: progress.value,
        earned: p.totalLessons > 0 && progress.value >= p.totalLessons,
      }))
      // Ein nicht verlinkter Kurs (`unlisted`) taucht erst auf, wenn man ihn selbst begonnen hat.
      .filter((b) => !b.unlisted || b.completedCount > 0)
  );

  const earnedCount = computed(() => badges.value.filter((b) => b.earned).length);

  return { badges, loading, earnedCount, load };
}
