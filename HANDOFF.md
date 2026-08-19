# Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-08-19
> **Letzter Commit:** fix: render notebook code output correctly in week courses

**Was zuletzt gemacht wurde:**
- Woche 1, Lektion 1 (12-Wochen-Kurs): Kommentare (`#`) waren im Intro als Lernziel genannt, aber nie erklärt — neuer Abschnitt "Zauberformel/Lektion/Systemprotokoll 5" (Markdown + Beispiel-Codezelle) in allen 6 Varianten ergänzt (DE: abenteuer/pferde/scifi, EN: adventure/horses/scifi)
- Interaktiven Einführungskurs auf Englisch übersetzt — 2 neue Inhaltspfade:
  - `content/python-grundlagen-interaktiv-kinder-en/` — 14 Dateien (Lektionen, lessons.json, glossary.json, beschreibung.md)
  - `content/python-grundlagen-interaktiv-jugendliche-en/` — 14 Dateien
- `InteractiveCourse.vue`: `useLanguage` integriert, EN-Pfade in `VARIANT_CONTENT_PATH` und `import.meta.glob`, `contentPathForVariant` jetzt sprachabhängig, `watch(lang)` lädt Lektionen bei Sprachwechsel neu, alle UI-Texte DE/EN
- `LessonView.vue`: `useLanguage` integriert, alle UI-Texte DE/EN (Buttons, Feedback, Statusmeldungen, Zusammenfassung)
- `INHALTE.md`, `CLAUDE.md` in `HANDOFF.md` + `WORKFLOW.md` aufgeteilt

**Bekannte offene Baustellen:**
- Docker prod-Build noch nicht getestet
- README.md noch nicht aktualisiert
- Notebook-Download-ZIP ist nur DE (kein EN-Zip)
- EN-Titel für Wochen 5–12 in `INHALTE.md` noch mit Platzhaltern (aus Notebooks nachlesen)

**Workflow:**
1. `./node_modules/.bin/vite --port 5173` starten (kein Docker auf diesem Rechner)
2. Weiter auf `main` arbeiten
3. Am Ende: `git add`, `git commit`, `git push`
