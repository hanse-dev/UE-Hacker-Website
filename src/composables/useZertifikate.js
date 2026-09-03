import { ref } from 'vue';
import { assetUrl } from '../utils/assetUrl';
import { useWeekChecks } from './useWeekChecks';

const COURSE_ID = 'python-12-wochen-grundkurs';

// Manifest ist pro Sprache gecacht, damit nicht jede Komponente einzeln fetcht.
// Wird nur noch für die Missionen-Anzeige (Übungs-Checkliste) gebraucht, nicht mehr fürs Zertifikat.
const manifestByLang = { de: ref(null), en: ref(null) };
const loadPromises = {};

async function ensureManifestLoaded(lang) {
  const key = lang === 'en' ? 'en' : 'de';
  if (manifestByLang[key].value) return manifestByLang[key].value;
  if (!loadPromises[key]) {
    const file = key === 'en' ? 'rewards-manifest-en.json' : 'rewards-manifest.json';
    loadPromises[key] = fetch(assetUrl(file))
      .then((res) => (res.ok ? res.json() : null))
      .then((data) => { manifestByLang[key].value = data; return data; })
      .catch(() => null);
  }
  return loadPromises[key];
}

export function useZertifikate() {
  const { isWeekCheckPassed } = useWeekChecks();

  const getManifest = (lang) => manifestByLang[lang === 'en' ? 'en' : 'de'].value;

  const getWeekMissionsAndBosses = (lang, variant, weekNumber) => {
    const manifest = getManifest(lang);
    const weekData = manifest?.[COURSE_ID]?.[variant]?.[String(weekNumber)];
    return { missions: weekData?.missions || [], bossQuests: weekData?.bossQuests || [] };
  };

  const getWeekMissionIds = (lang, variant, weekNumber) => {
    const { missions, bossQuests } = getWeekMissionsAndBosses(lang, variant, weekNumber);
    return [...missions, ...bossQuests];
  };

  /**
   * Zertifikat einer Woche: nur der Wochen-Check zählt (Quiz + beide Coding-Aufgaben bestanden).
   * Missionen/Boss-Quests sind reine Übungs-Checkliste und keine Voraussetzung mehr — es gibt
   * damit nur noch EIN Zertifikat pro Woche, unabhängig von der gewählten Variante.
   */
  const isCertificateEarned = (weekNumber) => isWeekCheckPassed(weekNumber);

  const countCertificates = () => {
    let count = 0;
    for (let w = 1; w <= 12; w++) {
      if (isCertificateEarned(w)) count++;
    }
    return count;
  };

  return {
    ensureManifestLoaded,
    getManifest,
    getWeekMissionsAndBosses,
    getWeekMissionIds,
    isCertificateEarned,
    countCertificates,
  };
}
