# Übergangshacker Website

Lernplattform für Kinder und Jugendliche (Python). Vue 3 + Vite Frontend, Express-API mit SQLite, Docker-Deployment.

## Schnellstart (lokal)

```bash
cp .env.example .env          # einmalig
# ADMIN_PASSWORD in .env setzen

cd api && npm install && cd ..
npm install

npm run start:all             # API :3001 + Vite :5173
```

- Website: http://localhost:5173/  
- Admin: http://localhost:5173/admin  
- API-Health: http://localhost:3001/api/health  

Ein Port wie in Produktion:

```bash
npm run start:prod            # Build + Server auf :8080
```

## `.env` — wann wird sie geladen?

Die API liest `.env` **beim Prozessstart** (einmalig über `dotenv`). Danach gilt der Wert im laufenden Prozess.

| Situation | Verhalten |
|-----------|-----------|
| `ADMIN_PASSWORD` **vor** dem Start setzen | wird beim Start geladen — so ist es gedacht |
| `.env` **während** der API läuft ändern | **keine** automatische Aktualisierung |
| Nach Passwort-Änderung | API **neu starten** (bzw. Container neu erstellen) |

**Lokal:** Datei `.env` im Projektroot (siehe `.env.example`). Nie committen.

**Docker:** Compose lädt `env_file: .env` beim **Container-Start**. Nach Änderung:

```bash
# .env editieren, dann:
docker compose up -d --force-recreate app
```

Nur `docker compose build` reicht nicht — die Env steckt nicht im Image, sondern wird beim Start injiziert. Neu erstellen / neu starten schon.

`ADMIN_PASSWORD` ist nur für die Admin-Oberfläche (`/admin`). Lernenden-Accounts liegen in der SQLite-DB (`api/data/`), nicht in der `.env`.

Optionale Variablen: siehe `.env.example` (`SESSION_SECRET`, `API_PORT`, …).

## Docker (Produktion)

Ein Container: Static-Frontend + API auf einem Port.

```bash
cp .env.example .env          # ADMIN_PASSWORD setzen
docker compose up -d --build app
```

→ http://localhost:8080  

SQLite bleibt auf dem Host unter `./api/data/` (Volume) — bleibt bei Rebuild erhalten, solange der Ordner nicht gelöscht wird.

Dev mit Hot-Reload im Container:

```bash
docker compose up --build dev
```

→ http://localhost:5173  

## Wichtige npm-Scripts

| Script | Zweck |
|--------|--------|
| `npm run start:all` | Dev: API + Vite parallel |
| `npm run start:prod` | Build + ein Server (:8080) |
| `npm run api` / `api:dev` | nur API |
| `npm run test:checks` | Pre-commit-Suite (Checks, Site, Merge) |
| `npm run test:auth` | API + Admin/Login-UI |

## Admin & Sync (Kurz)

1. `/admin` mit `ADMIN_PASSWORD` öffnen  
2. Lernenden-Account anlegen (`kinder` / `jugendliche`)  
3. Im Header **Optionen** → Anmelden → Fortschritt sync’t (lokal bleibt Fallback)

Details: [`ACCOUNT-SYNC-PLAN.md`](ACCOUNT-SYNC-PLAN.md)

## Stack

- Frontend: Vue 3, Vue Router, Vite  
- Inhalte: Jupyter-Notebooks unter `content/`  
- API: Express + SQLite (`node:sqlite`, Node ≥ 22)  
- Prod: API liefert auch `dist/` (kein separates Nginx nötig)
