# Account-Sync-Plan

> Umgesetzt und in `main` (PR #2). Sync-Loop-Fix: PR #3.

## Stack

- **API + Frontend (Prod):** Express in `api/` liefert `/api/*` **und** den Vite-`dist/` (ein Port)
- **DB:** SQLite via `node:sqlite` (`api/data/ue-hacker.sqlite`)
- **Admin:** `/admin`, Passwort = `ADMIN_PASSWORD` in `.env` (nur beim Prozess-/Container-Start geladen)
- **Accounts:** ein Mensch = ein Account, `ageGroup`: `kinder` | `jugendliche`
- **UI:** Header „Optionen“-Modal (Sprache + Login), nicht mehr permanente DE/EN-Buttons in der Nav

## Phasen

1. **API + Admin-CRUD** — erledigt
2. **Login + Progress-Sync** — erledigt (lokal bleibt Fallback)
3. **Notebook-Sync** — erledigt  
   - **Wichtig:** Bei Sync kein volles Notebook-Re-Fetch (sonst Blink-Schleife). Siehe `JupyterNotebook.vue` + `useProgressSync.js`.

## Sync-Regel (pro Key)

1. Gleicher Key, gleicher Wert → behalten  
2. Nur eine Seite hat den Key → behalten  
3. Beide unterschiedlich → neueres `updatedAt` gewinnt  
4. Merged Ergebnis lokal speichern **und** zum Server pushen (nur wenn sich etwas geändert hat)

## Lokaler Dev / Docker / Tests

Siehe `README.md` und `HANDOFF.md`.

## Nicht geplant

- E-Mail-Registrierung / öffentliche Sign-up
- Supabase
