import { ref } from 'vue';
import { fetchProgressAs, getUserInfo, loginUser, patchProgressAs } from './useAuthApi.js';

// Partnerarbeit: Zwei Accounts arbeiten an einem Rechner an einem Kurs. Die zweite Person meldet
// sich einmal im Kurs mit an; ab dann schreibt der Browser jeden Stand dieses Kurses auch in ihren
// Account. Die Verbindung gilt pro Kurs und nur für diesen Tab (sessionStorage) - der eigentliche
// Login (useAuth) bleibt unberührt.
const KEY_PREFIX = 'ue-hacker-partner-';
const PUSH_DELAY_MS = 400;

const partners = {};
const pending = {};
const timers = {};

function load(variant) {
  try {
    const parsed = JSON.parse(sessionStorage.getItem(KEY_PREFIX + variant));
    return parsed?.token && parsed?.username ? parsed : null;
  } catch {
    return null;
  }
}

function partnerRef(variant) {
  if (!partners[variant]) partners[variant] = ref(load(variant));
  return partners[variant];
}

function store(variant, value) {
  partnerRef(variant).value = value;
  try {
    if (value) sessionStorage.setItem(KEY_PREFIX + variant, JSON.stringify(value));
    else sessionStorage.removeItem(KEY_PREFIX + variant);
  } catch {
    // Ohne sessionStorage gilt die Verbindung nur bis zum Neuladen.
  }
}

// Beim Logout/Login-Wechsel: Wer jetzt am Rechner sitzt, arbeitet nicht mehr mit dem alten Partner.
export function clearPartners() {
  try {
    for (let i = sessionStorage.length - 1; i >= 0; i -= 1) {
      const key = sessionStorage.key(i);
      if (key?.startsWith(KEY_PREFIX)) sessionStorage.removeItem(key);
    }
  } catch {
    // siehe store()
  }
  for (const variant of Object.keys(partners)) partners[variant].value = null;
}

async function push(variant) {
  const partner = partnerRef(variant).value;
  const job = pending[variant];
  if (!partner || !job) return;
  delete pending[variant];
  try {
    await patchProgressAs(partner.token, {
      [job.storageKey]: { value: job.state, updatedAt: new Date().toISOString() },
    });
  } catch (e) {
    // 401: Die zweite Person hat inzwischen ihr Passwort geändert oder der Account ist weg.
    if (e.status === 401) store(variant, null);
    console.warn('Stand konnte nicht beim Partner-Account gespeichert werden:', e.message || e);
  }
}

// Von useInteractiveProgress bei jedem Speichern aufgerufen. Ohne Partner passiert nichts.
export function notifyPartner(variant, storageKey, state) {
  if (!partnerRef(variant).value) return;
  pending[variant] = { storageKey, state: JSON.parse(JSON.stringify(state)) };
  clearTimeout(timers[variant]);
  timers[variant] = setTimeout(() => push(variant), PUSH_DELAY_MS);
}

export function usePartner(variant) {
  const partner = partnerRef(variant);

  // Meldet die zweite Person an und liefert ihren bisherigen Stand dieses Kurses (oder null),
  // damit der Aufrufer beide Stände zusammenführen kann. Wirft mit `code`, wenn es nicht geht.
  const link = async (username, password, storageKey) => {
    const fail = (code) => Object.assign(new Error(code), { code });
    const me = getUserInfo();
    if (!me) throw fail('not-logged-in');
    if (me.username.toLowerCase() === username.trim().toLowerCase()) throw fail('self');

    let data;
    try {
      data = await loginUser(username.trim(), password);
    } catch (e) {
      throw fail(e.status === 401 ? 'wrong-credentials' : 'network');
    }
    // Ein Einmal-Passwort muss erst beim eigenen Login ersetzt werden.
    if (data.user?.mustChangePassword) throw fail('must-change-password');

    const remote = await fetchProgressAs(data.token);
    store(variant, { username: data.user.username, token: data.token });
    return remote?.payload?.[storageKey]?.value || null;
  };

  const unlink = () => {
    delete pending[variant];
    clearTimeout(timers[variant]);
    store(variant, null);
  };

  return { partner, link, unlink };
}
