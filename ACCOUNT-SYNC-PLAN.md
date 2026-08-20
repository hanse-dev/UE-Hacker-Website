# Account-Sync-Plan

> Branch: `cursor/admin-login`

## Stack

- **API + Frontend (Prod):** Express in `api/` liefert `/api/*` **und** den Vite-`dist/` (ein Port)
- **DB:** SQLite via `node:sqlite` (`api/data/ue-hacker.sqlite`)
- **Admin:** `/admin`, Passwort = `ADMIN_PASSWORD` in `.env`
- **Accounts:** ein Mensch = ein Account, `ageGroup`: `kinder` | `jugendliche`

## Phasen

1. **API + Admin-CRUD** — erledigt
2. **Login + Progress-Sync** — erledigt (Header-Modal; lokal bleibt Fallback)
3. **Notebook-Sync** — erledigt (gleiche Payload, Keys `ue-hacker-notebook-state-*`)

## Sync-Regel (pro Key)

1. Gleicher Key, gleicher Wert → behalten  
2. Nur eine Seite hat den Key → behalten  
3. Beide unterschiedlich → neueres `updatedAt` gewinnt  
4. Merged Ergebnis lokal speichern **und** zum Server pushen  

## Lokaler Dev (Hot Reload)

```bash
cp .env.example .env   # ADMIN_PASSWORD setzen
npm run start:all      # API :3001 + Vite :5173 (Proxy /api)
```

Nur gebaut + ein Port (wie Prod):

```bash
npm run start:prod     # http://localhost:8080
```

Tests: `npm run test:auth`

## Docker (ein Container)

```bash
docker compose up --build app
# → http://localhost:8080  (Static + API, SQLite in ./api/data)
```

## Nicht geplant

- E-Mail-Registrierung / öffentliche Sign-up
- Supabase
