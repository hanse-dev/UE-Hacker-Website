import { ref } from 'vue';
import de from '../locales/de.js';
import en from '../locales/en.js';

const LOCALES = { de, en };

const lang = ref(localStorage.getItem('ue-hacker-lang') || 'de');

export function useLanguage() {
  const t = (key) => LOCALES[lang.value]?.[key] ?? key;

  const setLang = (l) => {
    lang.value = l;
    localStorage.setItem('ue-hacker-lang', l);
  };

  return { lang, t, setLang };
}
