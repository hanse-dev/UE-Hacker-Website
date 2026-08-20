# Workflow-Regeln

## Git: Ein Thema = ein Branch

**Immer einen neuen Branch anlegen, wenn ein neues Thema beginnt.**

- Prefix: `cursor/` (z.B. `cursor/kurs-python-spiele`, `cursor/admin-login`)
- Branch von aktuellem `main` aus starten
- Ein Branch = ein Thema; Admin/Accounts nicht auf dem Lernpfad-Branch mischen
- Nächste Kurs-Themen (geplant): `cursor/kurs-python-spiele` → `cursor/kurs-python-projekte` → `cursor/kurs-js-minigames` oder `cursor/kurs-ki-labor` (siehe `todo.md`)
- Erst mergen, wenn das Thema fertig/getestet ist — danach neues Thema → neuer Branch

## Pre-commit Hook (Checks)

Beim Commit läuft automatisch `npm run test:checks` (Einstufung, Check-Tab, Home, Interaktiv-Smoke).

- Einmalig nach Clone: `npm install` (setzt `core.hooksPath` auf `.githooks`) und ggf. `npx playwright install chromium`
- Überspringen: `SKIP_CHECKS=1 git commit …` oder `git commit --no-verify`
- Voller Notebook-Test weiterhin manuell: `npm test`

## Bei Inhaltsänderungen: Zusammenhänge prüfen

Wann immer du Inhalte änderst (Notebooks, Markdown-Lektionen, JSON-Manifeste), **prüfe immer `INHALTE.md` Abschnitt 6** — dort steht, welche Dateien gleichzeitig angepasst werden müssen.

Kurzübersicht der wichtigsten Kopplungen:
- **Notebook ändern** → DE- und EN-Version synchron halten (`python-12-wochen-grundkurs` ↔ `python-12-wochen-grundkurs-en`)
- **Interaktive Lektion ändern** → alle drei Ordner prüfen (`python-grundlagen-interaktiv`, `-kinder`, `-jugendliche`) — oder bewusst nur eine Variante ändern und das begründen
- **Missionen/Punkte ändern** → `rewards-manifest.json` und `rewards-manifest-en.json`
- **Kursmetadaten ändern** → `public/kurse.json` (inkl. `title_en`, `description_en`) und ggf. `beschreibung.md` in beiden Sprachordnern

## Nach jedem Commit

Nach jedem `git commit` prüfen:
- Welche Aufgaben aus `todo.md` wurden durch diesen Commit erledigt?
- Diese Einträge in `todo.md` von `[ ]` auf `[x]` setzen.
- `todo.md` mit in den nächsten Commit aufnehmen, oder direkt committen.

## Handoff automatisch aktualisieren

**Vor jedem Commit** ohne explizite Aufforderung:
1. `HANDOFF.md` aktualisieren (letzter Commit, was wurde gemacht, was ist offen)
2. `todo.md` prüfen und erledigte Punkte markieren
3. `HANDOFF.md` und `todo.md` mit in denselben Commit aufnehmen (kein Extra-Commit)
