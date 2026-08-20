import { fetchProgress, getUserToken, putProgress } from './useAuthApi.js';
import { mergeProgressPayload } from '../utils/progressMerge.js';

export const SYNC_META_KEY = 'ue-hacker-sync-meta';
export const PROGRESS_APPLIED_EVENT = 'ue-hacker-progress-applied';

const FIXED_SYNC_KEYS = [
  'ue-hacker-fortschritt',
  'ue-hacker-week-checks',
  'ue-hacker-interactive-progress-kinder',
  'ue-hacker-interactive-progress-jugendliche',
];

const NOTEBOOK_PREFIX = 'ue-hacker-notebook-state-';

let debounceTimer = null;
let syncing = false;
let applying = false;

function loadMeta() {
  try {
    const raw = localStorage.getItem(SYNC_META_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

function saveMeta(meta) {
  try {
    localStorage.setItem(SYNC_META_KEY, JSON.stringify(meta));
  } catch (e) {
    console.error('Sync-Meta speichern fehlgeschlagen:', e);
  }
}

export function isSyncableKey(key) {
  if (!key || key === SYNC_META_KEY) return false;
  if (FIXED_SYNC_KEYS.includes(key)) return true;
  return key.startsWith(NOTEBOOK_PREFIX);
}

export function touchSyncKey(key, at = new Date().toISOString()) {
  if (!isSyncableKey(key) || applying) return;
  const meta = loadMeta();
  meta[key] = at;
  saveMeta(meta);
  scheduleSync();
}

function listLocalSyncKeys() {
  const keys = new Set(FIXED_SYNC_KEYS);
  for (let i = 0; i < localStorage.length; i += 1) {
    const key = localStorage.key(i);
    if (isSyncableKey(key)) keys.add(key);
  }
  return [...keys];
}

function readEntry(key, meta) {
  const raw = localStorage.getItem(key);
  if (raw == null) return null;
  let value;
  try {
    value = JSON.parse(raw);
  } catch {
    value = raw;
  }
  return {
    value,
    updatedAt: meta[key] || '1970-01-01T00:00:00.000Z',
  };
}

export function collectLocalPayload() {
  const meta = loadMeta();
  const payload = {};
  for (const key of listLocalSyncKeys()) {
    const entry = readEntry(key, meta);
    if (entry) payload[key] = entry;
  }
  return payload;
}

export function applyProgressPayload(payload) {
  applying = true;
  try {
    const meta = loadMeta();
    for (const [key, entry] of Object.entries(payload || {})) {
      if (!isSyncableKey(key) || !entry) continue;
      try {
        const raw = typeof entry.value === 'string'
          ? entry.value
          : JSON.stringify(entry.value);
        localStorage.setItem(key, raw);
        meta[key] = entry.updatedAt || new Date().toISOString();
      } catch (e) {
        console.error('Konnte Sync-Key nicht anwenden:', key, e);
      }
    }
    saveMeta(meta);
    window.dispatchEvent(new CustomEvent(PROGRESS_APPLIED_EVENT));
  } finally {
    applying = false;
  }
}

export async function syncNow() {
  if (!getUserToken() || syncing) return { ok: false, skipped: true };
  syncing = true;
  try {
    const remote = await fetchProgress();
    const local = collectLocalPayload();
    const merged = mergeProgressPayload(local, remote?.payload || {});
    applyProgressPayload(merged);
    await putProgress(merged);
    return { ok: true };
  } catch (e) {
    console.warn('Progress-Sync fehlgeschlagen:', e.message || e);
    return { ok: false, error: e };
  } finally {
    syncing = false;
  }
}

export function scheduleSync(delayMs = 1500) {
  if (!getUserToken()) return;
  if (debounceTimer) clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    debounceTimer = null;
    syncNow();
  }, delayMs);
}
