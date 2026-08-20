# Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-08-20
> **Aktueller Branch (WIP):** `cursor/python-lernpfad-quiz` — Einstufung + Wochen-Checks (bereit zum Commit/Merge)

**Was zuletzt gemacht wurde:**
- Kurs **Python Einstufung** + **Check-Tab** in allen 12 Wochen (`content/python-checks/weeks.json`)
- Placement: 2 Fragen/Woche, Rotation, Multi-Select, gemischte Antwortreihenfolge
- Bei allem bestanden: 3 Projektideen; Deep-Link öffnet Lektion/Notebooks
- Playwright: `npm run test:checks` + Pre-commit-Hook (`.githooks/pre-commit`)
- Alter Lernpfad-Code/Content entfernt (`LearningPathCourse`, `python-lernpfad*`, …)

**Als Nächstes (Priorität):**
1. Änderungen committen (ohne unnötigen Ballast)
2. `npm run test:checks` / Commit-Hook grün → in `main` mergen
3. **Später (neuer Branch `cursor/admin-login`):** [`ACCOUNT-SYNC-PLAN.md`](ACCOUNT-SYNC-PLAN.md)

**Git-Regel:** Jedes neue Thema = neuer Branch (`cursor/…`). Siehe `WORKFLOW.md`.

**Bekannte offene Baustellen (nicht dieses Feature):**
- Docker prod-Build noch nicht getestet
- README.md noch nicht aktualisiert
- Notebook-Download-ZIP ist nur DE (kein EN-Zip)

**Workflow:**
1. `npm run dev` oder `./node_modules/.bin/vite --port 5173`
2. Commit triggert `test:checks` (Skip: `SKIP_CHECKS=1`)
