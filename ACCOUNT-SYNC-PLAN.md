# Account-Sync-Plan (später, eigener Branch)

> Branch: `cursor/admin-login` (von `main` nach Merge der Einstufung).
> **Nicht** auf dem Branch `cursor/python-lernpfad-quiz` mischen.

## Ziel

Admin legt Accounts an (Username + Passwort). Lernende loggen sich ein und synchronisieren Fortschritt (Checks, Missionen, optional Notebook-State).

## Phasen

1. **Kleine API + Admin** — User anlegen, Passwort setzen
2. **Login + Progress-Sync** — lokaler Stand bleibt Fallback; bei Login debounced push/pull
3. **Notebook-Sync** (optional)

## Nicht geplant

- E-Mail-Registrierung / öffentliche Sign-up
- Supabase als Pflicht-Stack

## Hinweis

Bestehende Composables (`useFortschritt`, `useWeekChecks`, …) speichern weiter lokal und syncen bei Login.
