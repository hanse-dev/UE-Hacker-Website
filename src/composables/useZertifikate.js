import { ref } from 'vue';
import { assetUrl } from '../utils/assetUrl';
import { useFortschritt } from './useFortschritt';
import { useWeekChecks } from './useWeekChecks';

const COURSE_ID = 'python-12-wochen-grundkurs';

// Manifest ist pro Sprache gecacht, damit nicht jede Komponente einzeln fetcht.
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
  const { isWeekComplete } = useFortschritt();
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

  /** Zertifikat einer Woche/Variante: alle Missionen+Boss-Quest erledigt UND Wochen-Check (Quiz+Coding) bestanden. */
  const isCertificateEarned = (lang, variant, weekNumber) => {
    const ids = getWeekMissionIds(lang, variant, weekNumber);
    if (!ids.length) return false;
    return isWeekComplete(variant, ids) && isWeekCheckPassed(weekNumber);
  };

  const countCertificates = (lang, variant) => {
    let count = 0;
    for (let w = 1; w <= 12; w++) {
      if (isCertificateEarned(lang, variant, w)) count++;
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
