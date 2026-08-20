/**
 * Per-key progress merge: same value keep; only one side keep;
 * both different → newer updatedAt wins.
 */
export function mergeProgressPayload(local = {}, remote = {}) {
  const keys = new Set([...Object.keys(local || {}), ...Object.keys(remote || {})]);
  const merged = {};

  for (const key of keys) {
    const a = local?.[key];
    const b = remote?.[key];
    if (!a && b) {
      merged[key] = b;
      continue;
    }
    if (a && !b) {
      merged[key] = a;
      continue;
    }
    if (!a && !b) continue;

    const same = stableStringify(a.value) === stableStringify(b.value);
    if (same) {
      merged[key] = {
        value: a.value,
        updatedAt: newerIso(a.updatedAt, b.updatedAt),
      };
      continue;
    }

    const at = Date.parse(a.updatedAt) || 0;
    const bt = Date.parse(b.updatedAt) || 0;
    merged[key] = at >= bt ? a : b;
  }

  return merged;
}

function newerIso(a, b) {
  const at = Date.parse(a) || 0;
  const bt = Date.parse(b) || 0;
  return at >= bt ? (a || b) : (b || a);
}

function stableStringify(value) {
  try {
    return JSON.stringify(value);
  } catch {
    return String(value);
  }
}
