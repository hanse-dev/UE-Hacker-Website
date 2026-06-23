# Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-06-23
> **Letzter Commit:** `adb85d6` — chore: add content-change coupling rules to CLAUDE.md

**Was zuletzt gemacht wurde:**
- `language-toggle` Branch vollständig in `main` gemergt (alle 6 Phasen)
- Interaktiven Einführungskurs (`python-grundlagen-interaktiv`) in 2 Varianten aufgeteilt:
  - `content/python-grundlagen-interaktiv-kinder/` — Zielgruppe 8–12 Jahre (Tier-/Spielbeispiele, Code-Templates, 2 Aufgaben/Lektion)
  - `content/python-grundlagen-interaktiv-jugendliche/` — Zielgruppe 13–17 Jahre (App-/Alltag-Beispiele, leere Templates, 3 Aufgaben mit Bonus)
- `InteractiveCourse.vue` komplett neu: Variantenauswahl-Screen, dynamisches Laden per `import.meta.glob`, Mobile-Layout mit Toggle-Button
- `LessonView.vue`: `variant`-Prop, dynamische Glossar-/Lesson-Loader, Bonus-Badge
- `useInteractiveProgress.js`: Per-Variante State-Map mit eigenem localStorage-Slot
- Mobile-Bugs behoben: Sidebar-Overlay-Fix (CSS-Kaskade), Grid-Row-Sizing, Code-Textarea overflow
- `INHALTE.md` neu erstellt: Referenzdokument für alle Inhaltsdateien und ihre Zusammenhänge
- `CLAUDE.md` in separate Dateien aufgeteilt (`HANDOFF.md`, `WORKFLOW.md`)

**Bekannte offene Baustellen:**
- Docker prod-Build noch nicht getestet
- README.md noch nicht aktualisiert
- Notebook-Download-ZIP ist nur DE (kein EN-Zip)
- EN-Titel für Wochen 5–12 in `INHALTE.md` noch mit Platzhaltern (aus Notebooks nachlesen)
- Interaktiver Kurs noch nicht auf Englisch übersetzt

**Workflow:**
1. `./node_modules/.bin/vite --port 5173` starten (kein Docker auf diesem Rechner)
2. Weiter auf `main` arbeiten
3. Am Ende: `git add`, `git commit`, `git push`
