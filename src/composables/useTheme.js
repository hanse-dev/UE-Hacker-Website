import { computed, ref } from 'vue';

// Darstellung: 'system' (folgt prefers-color-scheme), 'light' oder 'dark'. Nur lokal im Browser
// gespeichert, nicht im Account-Sync. Das Inline-Skript in index.html setzt data-theme schon vor
// dem ersten Rendern (kein helles Aufblitzen) — dieselbe Logik, beide gleich halten.
export const THEME_STORAGE_KEY = 'ue-hacker-theme';
const PREFERENCES = ['system', 'light', 'dark'];

const readPreference = () => {
  try {
    const stored = localStorage.getItem(THEME_STORAGE_KEY);
    return PREFERENCES.includes(stored) ? stored : 'system';
  } catch {
    return 'system';
  }
};

const media = typeof window !== 'undefined' && window.matchMedia
  ? window.matchMedia('(prefers-color-scheme: dark)')
  : null;

const preference = ref(readPreference());
const systemDark = ref(Boolean(media?.matches));

const resolvedTheme = computed(() => {
  if (preference.value === 'system') return systemDark.value ? 'dark' : 'light';
  return preference.value;
});

const apply = () => {
  document.documentElement.dataset.theme = resolvedTheme.value;
};

media?.addEventListener('change', (event) => {
  systemDark.value = event.matches;
  apply();
});

apply();

export function useTheme() {
  const setPreference = (value) => {
    if (!PREFERENCES.includes(value)) return;
    preference.value = value;
    try {
      localStorage.setItem(THEME_STORAGE_KEY, value);
    } catch {
      // Speicher gesperrt (privates Fenster): Auswahl gilt nur für diese Sitzung.
    }
    apply();
  };

  return { preference, resolvedTheme, setPreference, preferences: PREFERENCES };
}
