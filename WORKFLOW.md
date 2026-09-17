# Workflow-Regeln

## Git: Ein Thema = ein Branch

**Immer einen neuen Branch anlegen, wenn ein neues Thema beginnt.**

- **Ohne** Prefix (z.B. `kurs-js-spielewerkstatt`, `admin-login`) — der frühere `cursor/`-Prefix
  wurde nachträglich bei allen Branches entfernt, nicht wieder einführen
- Branch von aktuellem `main` aus starten
- Ein Branch = ein Thema; Admin/Accounts nicht auf dem Lernpfad-Branch mischen
- Nächste Kurs-Themen (geplant): `kurs-js-spielewerkstatt` → `kurs-python-projekte` → `kurs-ki-labor` (siehe `todo.md`, Gesamt-Roadmap in `VISION.md`)
- Erst mergen, wenn das Thema fertig/getestet ist — danach neues Thema → neuer Branch

## Tests für jede Verhaltensänderung

**Jede Änderung an Logik/Verhalten (nicht reine Text-/Content-Korrekturen) braucht einen
dauerhaften Test in der Playwright-Suite (`tests/*.spec.js`), nicht nur eine manuelle
Verifizierung.** Ein Skript, das einmal im Terminal läuft, oder eine manuelle Browser-Prüfung
zeigt nur, dass es *heute* funktioniert — ohne Test in `test:checks` kann die nächste Änderung
das stillschweigend wieder kaputt machen, ohne dass es auffällt.

- Neuer Bugfix, neue Option/Feature, geänderte Berechnung/Schwelle → passenden Test in einer
  bestehenden `describe()`-Gruppe ergänzen (oder eine neue, wenn thematisch nötig) — Vorbild:
  bestehende Tests in `tests/site.spec.js`, `tests/week-checks.spec.js`,
  `tests/storytelling-content.spec.js`
- Vor dem Commit `npm run test:checks` laufen lassen und sicherstellen, dass der neue Test auch
  wirklich fehlschlägt, wenn man die Änderung rückgängig macht (sonst testet er nichts)
- Reine Content-/Text-Änderungen ohne Verhaltensänderung (Tippfehler, Formulierungen) brauchen
  keinen neuen Test, aber bei Content mit eingebetteter Logik (z. B. Datentypen-Reihenfolge in
  Quizfragen) im Zweifel lieber einen Test ergänzen als weglassen

## Pre-commit Hook (Checks)

Beim Commit läuft automatisch `npm run test:checks` (Einstufung, Check-Tab, Home, Interaktiv-Smoke, Storytelling-Content-Regressionen).

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

## HANDOFF.md aufräumen (gegen unbegrenztes Wachstum)

`HANDOFF.md` soll einen schnellen Einstieg in eine neue Session ermöglichen, nicht als
vollständiges Änderungsprotokoll für immer wachsen — die Commit-Historie (`git log`/`git show`)
ist die dauerhafte, verlässliche Quelle für Details.

- **Nach dem Mergen eines Branches nach `main`:** den zugehörigen Abschnitt in HANDOFF.md
  Abschnitt 3 (Feature-Historie) von einer vollständigen Erzählung auf 2–3 Zeilen kürzen
  (Branch-/PR-Name, worum es ging, Verweis auf die Commit-Historie für Details). Eine kurze
  "Gelernte Regel"-Zeile darf bleiben, wenn sie ein wiederverwendbares Muster festhält (z.B. ein
  Bug-Typ, der wieder auftreten könnte) — die Schritt-für-Schritt-Story nicht.
- Abschnitt 5 (Offene Aufgaben) und Abschnitt 7 (Schnellstart) bleiben immer knapp und aktuell —
  das sind die Abschnitte, die eine neue Session tatsächlich zuerst braucht.
- Faustregel: wenn Abschnitt 3 spürbar länger wird als Abschnitt 5+7 zusammen, ist Aufräumen fällig.
