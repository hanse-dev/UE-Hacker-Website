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
| `npm run dev:skip-checks` | Dev-Server im Modus „Prüfungen überspringen“ (siehe unten) |
| `npm run test:checks` | volle Playwright-Suite (läuft automatisch vor jedem `git push`) |
| `npm run test:changed` | nur die Tests zu geänderten Dateien (läuft automatisch vor jedem Commit) |
| `npm run test:devskip` | prüft den Modus „Prüfungen überspringen“ (läuft vor jedem `git push`) |
| `npm run test:auth` | API + Admin/Login-UI |

## Kurse schnell durchklicken: Prüfungen überspringen

```bash
npm run dev:skip-checks       # wie `npm run dev`, Vite auf :5173
```

Zum Durchgehen eines Kurses beim Entwickeln oder Review, ohne jede Aufgabe lösen zu müssen. In
diesem Modus gilt in **allen** Kursen (Python-Lektionen, JS-Kurse, Projekte, KI-Labor, künftige
Kurse):

- **„Prüfen“** besteht sofort – der Code wird gar nicht erst ausgeführt, kein Warten auf den
  Python-Kernel.
- **Wochen-Check:** jede Quiz-Antwort zählt als richtig, die Coding-Aufgaben bestehen ebenfalls.
- **Alle Lektionen** sind von Anfang an freigeschaltet.
- Ein gelbes **Banner** oben auf jeder Seite zeigt, dass der Modus aktiv ist.

Der Modus wirkt nur im Vite-Dev-Server. Im Produktions-Build (`npm run build`, Docker) ist er
abgeschaltet, auch wenn `VITE_DEV_SKIP_CHECKS=1` gesetzt ist – das prüft `npm run test:devskip`.
Fortschritt, der in diesem Modus entsteht, landet wie sonst im Browser-Speicher; zum normalen
Testen danach den Fortschritt im Kurs zurücksetzen oder ein privates Fenster nutzen.

Technik: `src/composables/devSkipChecks.js`. Damit ein neuer Kurs automatisch mitmacht, muss er
seine Prüfungen über `src/composables/useTaskValidation.js` laufen lassen (und
`isLessonUnlocked` aus `useInteractiveProgress.js` für die Freischaltung nutzen).

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
