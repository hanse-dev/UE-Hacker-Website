# Workflow-Regeln

## Keine Sub-Agenten (Agent-Tool) für dieses Projekt

**Keine Sub-Agenten spawnen, auch nicht für Recherche/Exploration.** Jeder Sub-Agent lädt
`CLAUDE.md` samt aller `@`-Imports (`VISION.md`, `todo.md`, `HANDOFF.md`, `WORKFLOW.md`) neu —
das verbraucht bei parallelen/mehreren Spawns unnötig viele Tokens gleichzeitig, ohne
projektspezifischen Nutzen gegenüber sequenzieller Arbeit in der Hauptsession. Stattdessen:
Aufgaben nacheinander in der Hauptsession erledigen (Read/Grep/Bash direkt nutzen), auch wenn
das bedeutet, dass Recherche und Umsetzung mehr Turns brauchen. Ausnahme nur, wenn der Nutzer
explizit einen Sub-Agenten verlangt.

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

## Auffälligkeiten: fixen oder dokumentieren (gilt auch für Sub-Agenten)

Fällt bei der Arbeit etwas auf (Vorgriff auf spätere Wochen, Inkonsistenz zwischen Varianten/Sprachen,
vereinfachte oder gekürzte Aufgaben, Lücken, Bugs), wird es **nie nur im Bericht erwähnt und dann
liegengelassen**. Entweder:
1. **gleich beheben**, wenn es klar ist und im eigenen Arbeitsbereich liegt (inkl. Lösungs-Notebook,
   Texte, Tests dazu) — oder
2. **dokumentieren**, damit es später überarbeitet werden kann: Eintrag in `todo.md` (Abschnitt
   "Nachbesserungen") mit Fundstelle (Datei), was auffiel, warum es so blieb und Vorschlag zur Lösung.

**Nacharbeiten gleich miterledigen:** Solche Arbeiten (Vorgriffe in die passende spätere Woche nachziehen,
bewusst weggelassene Inhalte wieder aufnehmen, gekürzte Mengen mit den Original-Mengen wiederholen,
generische Namen themenspezifisch machen, veraltete Tests/Doku anpassen) werden **im selben Zug erledigt**,
sobald der Grund dafür bekannt ist — nicht als Punkt in `todo.md` geparkt und später abgefragt. In `todo.md`
kommt nur, was **wirklich nicht jetzt** geht (z.B. hängt von noch nicht umgestellten Wochen ab), mit Begründung.
**Flaky Tests** (einzeln grün, im Volllauf/unter Last rot) werden nicht toleriert oder wiederholt, sondern mit
`test.skip`/`describe.skip` und einem Kommentar zum Grund abgeschaltet.

**Sub-Agenten:** Das Prompt-Briefing muss diese Regel enthalten. Sie fixen, was in ihren eigenen
Dateien liegt, und melden alles andere unter **"Auffälligkeiten (nicht behoben)"** mit Datei, Grund und
Lösungsvorschlag — die aufrufende Session überträgt das in `todo.md` bzw. behebt es selbst. Sie ändern
keine geteilten Dateien (`todo.md`, `HANDOFF.md`, `src/`, `tests/`) selbst.

## Bei Inhaltsänderungen: Zusammenhänge prüfen

Wann immer du Inhalte änderst (Notebooks, Markdown-Lektionen, JSON-Manifeste), **prüfe immer `INHALTE.md` Abschnitt 6** — dort steht, welche Dateien gleichzeitig angepasst werden müssen.

Kurzübersicht der wichtigsten Kopplungen:
- **Notebook ändern** → DE- und EN-Version synchron halten (`python-12-wochen-grundkurs` ↔ `python-12-wochen-grundkurs-en`)
- **Interaktive Lektion ändern** → alle drei Ordner prüfen (`python-grundlagen-interaktiv`, `-kinder`, `-jugendliche`) — oder bewusst nur eine Variante ändern und das begründen
- **Missionen/Punkte ändern** → `rewards-manifest.json` und `rewards-manifest-en.json`
- **Kursmetadaten ändern** → `public/kurse.json` (inkl. `title_en`, `description_en`) und ggf. `beschreibung.md` in beiden Sprachordnern

## Nach jeder Änderung committen

**Nach jeder abgeschlossenen Änderung sofort einen Commit anlegen** — nicht Änderungen sammeln und
am Ende der Session in einem Riesen-Commit bündeln. Eine "Änderung" ist eine in sich stimmige
Einheit (ein Bugfix, ein Feature-Schritt, eine Content-Korrektur, eine Doku-Umstrukturierung).

- Ein Commit pro Einheit, mit aussagekräftiger Nachricht; nur die dazugehörigen Dateien stagen
  (keine fremden, uncommitteten Änderungen mitnehmen).
- Das gilt auch für Sub-Agenten-Ergebnisse und für Claude Code: nicht auf eine Aufforderung warten.
- Pushen und Mergen nach `main` bleibt davon getrennt (erst wenn das Thema fertig/getestet ist).

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

`HANDOFF.md` und `todo.md` werden per `@` in **jede** Session und jeden Sub-Agenten geladen — sie
sind "heiß" und müssen klein bleiben (Richtwert: HANDOFF.md < 25 KB, todo.md < 10 KB). Ausführliches
liegt "kalt" unter `docs/archiv/` (nicht importiert, nur bei Bedarf gelesen).

- **Bei jedem Task, nicht erst wenn die Schwelle gerissen ist:** proaktiv prüfen, ob erledigte
  Punkte in `todo.md`/`HANDOFF.md` inzwischen archiviert werden können, ob sich Punkte doppeln oder
  veraltete Referenzen stehen geblieben sind — diese Dateien werden bei jeder Session/jedem
  Sub-Agenten per `@` geladen und kosten dort Tokens, auch wenn die KB-Schwelle noch nicht
  überschritten ist. Reines Aufschieben bis zum nächsten großen Aufräum-Task lässt die Dateien
  unnötig aufblähen.
- **Während der Arbeit an einem Branch:** den Feature-Abschnitt ausführlich in HANDOFF.md Abschnitt 3
  schreiben (als `### 3.NN`), solange der Branch noch nicht gemergt ist.
- **Nach dem Mergen nach `main`:** den vollständigen Abschnitt unverändert ans Ende von
  `docs/archiv/HANDOFF-historie.md` verschieben. In HANDOFF.md bleibt nur eine Zeile in der
  Tabelle in Abschnitt 3 (Nr., Thema, Kern) — die Nummer ist die Referenz ins Archiv. Wiederverwendbare
  Fallstricke (Bug-Typen, die wieder auftreten können) als Zeile in "Gelernte Regeln" übernehmen.
- **`todo.md`:** erledigte (`[x]`) Blöcke und "Fertige Branches" nach `docs/archiv/todo-erledigt.md`
  verschieben; in `todo.md` nur offene Punkte und "Nächste Themen".
- Abschnitt 5 (Offene Aufgaben) und Abschnitt 7 (Schnellstart) bleiben immer knapp und aktuell —
  das sind die Abschnitte, die eine neue Session tatsächlich zuerst braucht.
- Faustregel: wenn `HANDOFF.md` über 25 KB wächst, ist Aufräumen fällig.
- `INHALTE.md`, `KURSPLAN.md`, `PROJEKTIDEEN.md` sind bewusst **nicht** importiert (siehe CLAUDE.md,
  "Bei Bedarf lesen") — bei Inhaltsänderungen `INHALTE.md` Abschnitt 6 aktiv lesen.
