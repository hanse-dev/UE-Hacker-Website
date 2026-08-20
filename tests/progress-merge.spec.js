import { test, expect } from '@playwright/test';
import { mergeProgressPayload } from '../src/utils/progressMerge.js';

test.describe('Progress-Merge', () => {
  test('nur lokal → behalten', () => {
    const merged = mergeProgressPayload(
      { a: { value: 1, updatedAt: '2026-01-02T00:00:00.000Z' } },
      {}
    );
    expect(merged.a.value).toBe(1);
  });

  test('nur remote → behalten', () => {
    const merged = mergeProgressPayload(
      {},
      { b: { value: 'x', updatedAt: '2026-01-02T00:00:00.000Z' } }
    );
    expect(merged.b.value).toBe('x');
  });

  test('gleicher Wert → behalten, neueres updatedAt', () => {
    const merged = mergeProgressPayload(
      { k: { value: { ok: true }, updatedAt: '2026-01-01T00:00:00.000Z' } },
      { k: { value: { ok: true }, updatedAt: '2026-01-03T00:00:00.000Z' } }
    );
    expect(merged.k.value).toEqual({ ok: true });
    expect(merged.k.updatedAt).toBe('2026-01-03T00:00:00.000Z');
  });

  test('Konflikt → neueres updatedAt gewinnt', () => {
    const merged = mergeProgressPayload(
      {
        a: { value: 'local', updatedAt: '2026-01-05T00:00:00.000Z' },
        b: { value: 'local-old', updatedAt: '2026-01-01T00:00:00.000Z' },
      },
      {
        a: { value: 'remote-old', updatedAt: '2026-01-01T00:00:00.000Z' },
        b: { value: 'remote', updatedAt: '2026-01-06T00:00:00.000Z' },
        c: { value: 'only-remote', updatedAt: '2026-01-01T00:00:00.000Z' },
      }
    );
    expect(merged.a.value).toBe('local');
    expect(merged.b.value).toBe('remote');
    expect(merged.c.value).toBe('only-remote');
  });
});
