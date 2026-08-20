# Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-08-20
> **Aktueller Branch (WIP):** `cursor/admin-login` — Account-Sync; API liefert auch Static

**Was zuletzt gemacht wurde:**
- Express-API + SQLite; Admin `/admin`; Learner-Login; Progress/Notebook-Sync
- **Prod:** ein Prozess/Container — API serviert `dist/` auf Port 8080
- **Dev:** `npm run start:all` (Vite :5173 + API :3001, Proxy)

**Als Nächstes:**
1. Manuell / Docker `app` testen
2. Optional committen / PR

**Start:**
```bash
npm run start:all          # Dev
npm run start:prod         # gebaut, ein Port :8080
docker compose up --build app
```

**Git-Regel:** Jedes neue Thema = neuer Branch (`cursor/…`). Siehe `WORKFLOW.md`.
