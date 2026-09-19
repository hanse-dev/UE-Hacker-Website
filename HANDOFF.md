# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-19
> **Aktueller Stand:** `main` ist lokal aktuell (Push nach `origin/main` und Server-Deploy stehen aus —
> Nutzer deployt selbst, siehe Abschnitt 4 "Betrieb"). Zuletzt gemergt: 12-Wochen-Kurs Woche 12 als
> Text-Adventure-Abschlussprojekt, List Comprehensions als Kursinhalt (Woche 6), JS-Grundkurs
> (9 Wochen), Projekte-Übersicht, Profil-Abzeichen.
> **Ziel dieser Datei:** schneller Einstieg für die nächste Session (Mensch oder Claude), ohne
> Chat-Historie. Sie wird per `@` in jede Session geladen — **klein halten** (Richtwert < 25 KB).
> Die ausführliche Feature-Historie liegt kalt in `docs/archiv/HANDOFF-historie.md` (nicht importiert).

Projekt-Regeln immer mitlesen: `CLAUDE.md`, `WORKFLOW.md`. Bei Content-Arbeit zusätzlich `INHALTE.md`,
`KURSPLAN.md`, `todo.md` (werden nicht automatisch geladen).

---

## 1. Was ist das Projekt?

Lernplattform für Kinder/Jugendliche (Python) — Vue 3 + Vite, Notebooks unter `content/`, Docker-Deploy.

**Live/Prod-Modell:** Ein Node-Prozess (`api/`) liefert `/api/*` **und** das gebaute Frontend (`dist/`) auf Port **8080**. Service-Name in Compose: **`app`** (nicht mehr `prod`).

---

## 2. Git / PRs (erledigt)

| PR | Branch | Inhalt |
|----|--------|--------|
| #1 | `python-lernpfad-quiz` | Einstufung + Wochen-Checks, Tests, alter Lernpfad entfernt |
| #2 | `admin-login` | Express+SQLite API, Admin, Login, Progress/Notebook-Sync, Single-Port-Deploy |
| #3 | `fix-notebook-sync-loop` | Hotfix: Notebook-Blink-/Reload-Schleife bei eingeloggt+Sync |

`main` ist der Integrationsstand. Feature-Branches oben sind historisch; neue Arbeit immer **neu von `main`**.

---

## 3. Feature-Kurzübersicht (Details: `docs/archiv/HANDOFF-historie.md`, Nummern = Abschnitte dort)

Alles unten ist nach `main` gemergt. Für Details `grep -n "^### 3.NN" docs/archiv/HANDOFF-historie.md`.

| Nr. | Thema | Kern in einem Satz |
|---|---|---|
| 3.1–3.3 | Einstufung/Checks, Admin+Sync (Express+SQLite), Sync-Loop-Fix | PR #1–#3 |
| 3.4 | Storytelling-Überarbeitung 12-Wochen-Kurs | Regressionstests: `tests/storytelling-content.spec.js` |
| 3.5 | Debug-Notebook-Sicherheit | AST-Loop-Guard (5s) in `usePyodide.js`, bewusst kein Web Worker (`input()`) |
| 3.6/3.15/3.17 | Einstufungstest-Fixes, Distraktoren, personalisierte Falsch-Erklärungen | `optionExplanations(_en)` nur bei `multiple_choice` |
| 3.7 | Interaktiv-Kurs: gestufter Hinweis | 2. Fehlversuch zeigt erst den erwarteten Wert |
| 3.8–3.10 | Tippfehler-Pass (cspell) | alle 444 Notebooks geprüft; `.vue`-Prosa/Interaktiv-Kurse offen |
| 3.11 | Cäsar-Chiffre (erstes Projekt) | Grundlage für `ProjectCourse.vue` |
| 3.12–3.14 | Wochen-Zertifikate statt Punktesystem, PDF-Download, XP-Texte entfernt | Zertifikat = nur Wochen-Check |
| 3.16 | Debug-Ziele Pferde+Abenteuer | `**Ziel:**`-Zeilen |
| 3.18 | `weeks.json` → `config.json` + `week-N.json` | Node-Loader `content/python-checks/index.mjs` |
| 3.19–3.23 | Refactoring 2–6 (CSS, WeekSection, LessonView, Placement, Ternary→`t()`) | Plan abgeschlossen |
| 3.24–3.31 | Curriculum-Lücken 12-Wochen-Kurs | Woche 1/3/4/5/6/7/8/11 inhaltlich bereinigt |
| 3.32 | Turtle lief nie im Browser → eigener Canvas-Shim | bleibt im Code für spätere Mandala-Projekt |
| 3.33 | Zellen-Format (`NN_*.py` statt `.ipynb`), CodeMirror 6 | `_generated`/`_bundle` gitignored |
| 3.34 | Wochen-Check: `variables`/`functionCalls`-Validierung | Hardcoding der Ausgabe reicht nicht mehr |
| 3.35/3.36 | Geführte Wochen-Tour wird echte Kursseite | `WeekTour.vue`; alte Akkordeon-UI entfernt |
| 3.37/3.45 | `VISION.md`, `PROJEKTIDEEN.md` | reine Doku |
| 3.38 | Projekte-Übersicht `/projekte` + Filter, Morsecode, Zahlen-Detektiv | Neuer Projekt-Kurs = Content-Ordner + `kurse.json` |
| 3.39 | JS-Spielewerkstatt (iframe-Sandbox) | `useJsSandbox.js`, `JsLessonView.vue`, `JsCodeCell.vue` |
| 3.40/3.41 | Nav-Link "Projekte", `/profil` mit Abzeichen | Projekt-Fortschritt wird jetzt gesynct (Präfix-Key) |
| 3.42–3.44 | JS-Grundkurs komplett (9 Wochen), Homepage-Redesign | `JsGrundkursTour.vue`, `example`-Aufgaben |
| 3.46 | Woche 12: Text-Adventure-Abschlussprojekt statt Turtle | Komposition einziger neuer Begriff; List Comprehension neu in Woche 6 |

### In Arbeit (Branch noch nicht gemergt — nach dem Merge ins Archiv verschieben)

### 3.47 Python Woche 1–3 (alle Themen, DE + EN) im Lektions-Format (Branch `python-woche1-lektionen-format`)

Woche 1–3, je Abenteuer/Pferde/Sci-Fi, DE und EN (Content `content/python-woche{N}-{thema}[-en]/`, Thema-Schlüssel auch bei EN deutsch) ist nicht mehr ein Notebook-Block pro Schritt, sondern **12 einzeln
durchklickbare Lektionen** wie im JS-Grundkurs (5 Zauberformeln → 1 Debug mit 3 Bugs → 3 Missionen →
3 Extra-Herausforderungen), gruppiert in einer Kuller-Leiste. Content: `content/python-woche1-abenteuer/`
(`lessons.json` + `lektion-NN.md`/`debug-01.md`/`mission-NN.md`/`boss-NN.md`), Pyodide via
`LessonView.vue`. **Umsetzung:** `JsCourseTour.vue` hat neue Props `engine` (`'pyodide'` rendert
`LessonView` statt `JsLessonView`) und `embedded` (kein eigener Breadcrumb). `WeekTourStepper.vue` bekommt
`lessonContentPath`: dann sind die Tour-Schritte nur noch **Lektionen** (die eingebettete Tour) + **Check**
(Zertifikat bleibt erhalten), Glossar/Lösungen/Cheat-Sheets bleiben Nachschlagewerke im Seitenmenü.
`WeekTour.vue` erkennt den Ordner automatisch per `import.meta.glob('content/python-woche*/lessons.json')` — eine neue Woche braucht nur den Content-Ordner (+ Lösungs-Notebook), keinen Code (`lessonContentPath`), alles andere
bleibt Notebook.
- **Aufgaben sind konkretisiert:** `LessonView` prüft nur die Ausgabe (`output_contains`), also mussten
  freie Missionen/Boss-Quests feste Vorgaben bekommen (z.B. "gib genau `Position: 10, 20, 30` aus").
  Bonus-Teile der Originale sind nur noch Text ohne Prüfung.
- **Pferde:** die Übungen heißen dort "Übung N" statt "Lektion N" (sonst Verwechslung mit dem Abschnitt "Lektion"). Zauberformel/Übung/Protokoll = Funktion ist in allen Themen erklärt (Notebooks + Lektionen).
- **Nicht übernommen:** Glossar-Tooltips, die Original-Notebooks (bleiben als Nachschlagewerk
  "Glossar"/"Lösungen" unverändert, Lösungen passen aber inhaltlich noch zu den freien Original-Aufgaben,
  nicht zu den konkretisierten). Woche 2 und 3 wurden per Sub-Agenten (je Woche/Thema/Sprache) erstellt, Skripte in der Session-Scratchpad; Missionen/Boss sind dort vereinfacht (feste Werte, teils weniger Elemente, weil Listen/if erst später kommen). `tests/python-lektionen-format.spec.js` findet alle `python-woche*`-Ordner selbst und prüft Integrität + Tour. **Achtung:** parallel hat eine andere Session Woche-4-Ordner angelegt (nicht Teil dieser Arbeit, siehe dortigen Stand).
- **Gelernte Regel:** `CodeChallenge` startet den Kernel nicht selbst — frühere Tests liefen nur, weil ein
  zuvor gemountetes Notebook ihn nebenbei initialisierte. Tests klicken jetzt `.btn-kernel` explizit
  (`ensureKernel` in `zertifikate.spec.js`). Tests, die Woche 1 Abenteuer als Notebook brauchten
  (`wochen-tour`, `notebooks`, `site`, `week-checks`, `zertifikate`, `storytelling`), nutzen jetzt
  Woche 12 (notebooks.spec überspringt umgestellte Wochen automatisch) bzw. die neue Lektion; neuer Test: `tests/python-woche1-lektionen.spec.js`.

### 3.48 Python Woche 4 (Schleifen) im Lektions-Format (Branch `python-woche1-lektionen-format`)

Alle 6 Ordner `content/python-woche4-{abenteuer|pferde|scifi}[-en]/` per Sub-Agenten erstellt (Muster: Woche 2), jede Aufgabe mit `python3` gegen Referenzlösung/Stub geprüft. `tests/python-lektionen-format.spec.js` deckt Woche 4 mit ab (`WEEKS = [1, 2, 4]`); dabei einen Fehler gefunden und gefixt (Abenteuer EN hatte `section: "mission"` statt `"boss"` bei `boss-*`). DE/EN-Struktur danach angeglichen (Abenteuer 8, Pferde 7, Sci-Fi 7 Lektionen, gleiche IDs/Aufgaben; die kleinere Sprache wurde jeweils als Übersetzung der größeren neu aufgebaut). Mehrzeilige `expected` mit `\n` in der App bestätigt. Offen: Vorgriffe in Missionen/Boss vereinfacht — Details in `todo.md` "Nachbesserungen Lektions-Format Woche 4".

### Gelernte Regeln (wiederverwendbare Fallstricke)

**Content / Notebooks**
- Bulk-Edits an JSON/Notebooks nie per volle Reserialisierung, sondern gezielte Text-Ersetzung + `json.loads()` danach (3.12, 3.16). Seit 3.33 sind 12-Wochen-Notebooks Zellen-Ordner (`NN_*.py`) — keine `.ipynb` als Quelle wieder einführen.
- Debug-Bugs müssen vom Kernel-Zustand unabhängig sein und dürfen die Lösung nicht verraten (3.4). Nach Notebook-Änderung Code-Zellen mit gemeinsamem Namespace per `python3` ausführen.
- Ein "Fund" aus einer Variante gilt nicht automatisch für alle: vor Massenänderungen alle 3 Varianten × DE/EN per grep prüfen (3.26–3.30).
- Standard-PDF-Fonts (pdf-lib/Helvetica) können kein Emoji — Content-Texte vorher per `sanitizeForPdfFont` filtern (3.13).
- Punkte-/Item-System und lokales Fortschritt-Skript **nicht** wieder einführen; Zertifikat = nur Wochen-Check, ein Zertifikat pro Woche, PDF login-gated (3.12/3.13).
- Quizfragen `multiple_choice`: `optionExplanations` mitpflegen, `explanation_en` echt übersetzen; `shuffleQuestionOptions()` muss Text+Erklärung als Paar mischen (3.17). Schwelle nie als exakten Bruch (2/3 → `0.66`, 3.6).

**Pyodide / Ausführung**
- Kein Web Worker: `input()` läuft synchron über `window.prompt()` (65 Notebooks, 3.5). Loop-Guard ist AST-basiert.
- `turtle` gibt es in Pyodide nicht — eigener Canvas-Shim in `usePyodide.js` (3.32).
- `CodeChallenge` startet den Kernel nicht selbst; Tests klicken `.btn-kernel` explizit (3.47-Lektion, `ensureKernel` in `zertifikate.spec.js`).
- Namespace-Variablen vor jedem Check-Lauf löschen; `pyodide.globals.delete()` wirft bei unbekanntem Namen → try/catch (3.34). Vor `functionCalls`-Re-Aufruf `__cell_deadline__` neu setzen (3.34).

**JS-Sandbox (`js-spielewerkstatt`, `js-grundkurs`)**
- `functionCalls` sieht nur `function`-Deklarationen und `var`; `const`/`let`/`class` sind beim zweiten `eval` weg → keine `functionCalls` auf Arrow-Functions/Klassen-Methoden (3.43).
- `valuesMatch()` vergleicht Arrays nur per `===` → nie ein Array als `expected`; nur daraus abgeleitete Skalare validieren. Objekte gehen rekursiv (3.43).
- `dom_text`/`dom_click_text` nutzen `validation.text`, nicht `expected` (sonst greift der Ausgabe-Fallback); `canvas_*` analog (3.43).
- Chromium drosselt `requestAnimationFrame` in Off-screen-iframes → `scrollIntoView()` vor dem Lauf (3.39). `postMessage` nur mit reinen Werten (`JSON.parse(JSON.stringify())`, Vue-Proxies lassen sich nicht klonen).
- Keine echte Endlosschleife als Debug-Bug (kein Loop-Guard in der JS-Sandbox, nur 5s-Timeout).

**Vue / CSS / Tests**
- `@import` in `<style scoped>` bekommt einen anderen Scope-Hash → in separaten **unscoped** `<style>`-Block. Vor CSS-Extraktion Klassennamen repo-weit grep-prüfen (3.19, 3.20).
- Watcher, die nach dem Rendern scrollen: `flush: 'post'` (3.39).
- Sync darf nach Server-Apply keinen vollen Notebook-Re-Fetch auslösen (Blink-Schleife, 3.3).
- CodeMirror ist keine `<textarea>`: Tests nutzen `tests/helpers/codemirror.js` (`setCodeMirrorContent`, `hoverOverCodeMirrorText`).
- Beim Umbenennen von Testdateien `package.json`-Skripte mitprüfen — Playwright ignoriert fehlende Dateien stillschweigend, nur der Test-Zähler sinkt (3.43).
- `test:auth` nutzt Port 5174 mit Proxy-Header; läuft dort schon ein "nackter" Vite, kommen 502er → `lsof -nP -iTCP:5174 -sTCP:LISTEN` (3.36).
- Neue `LessonView.vue`-Kurse: Glob-Listen sind seit 3.38 Wildcards — nur Content-Ordner + `kurse.json` nötig.
- Deep-Links `?week=&tab=` (Einstufung, Cäsar-Chiffre) bewusst unverändert lassen, `WeekTour.vue` übersetzt intern (3.36).
- cspell: Wörterbücher brauchen `"import"`, nicht nur `"dictionaries"`; Ausgabe muss im Repo liegen (3.8/3.9).

**Betrieb**
- SQLite nur per `VACUUM INTO` sichern (WAL), nie `cp`; nie `git clean -fdx` ohne `api/data/` auszuschließen (Abschnitt 4).

---

## 4. Aktueller technischer Stand

### Start lokal

```bash
cp .env.example .env   # ADMIN_PASSWORD setzen
cd api && npm install && cd .. && npm install
npm run start:all      # Vite :5173 + API :3001 (Proxy /api)
# oder
npm run start:prod     # Build + alles :8080
```

### Docker Prod

```bash
# .env mit ADMIN_PASSWORD
docker compose down --remove-orphans
docker compose up -d --build app
curl -s http://127.0.0.1:8080/api/health
```

SQLite bleibt in `./api/data/` (Volume). Env-Änderung → Container **recreate**, nicht nur rebuild.
Ein `git pull` + `docker compose up -d --build app` lässt Nutzerdaten unangetastet — die DB liegt
als Bind-Mount auf dem Host, nicht im Container, und ist gitignored. **Einzige echte Gefahr:**
`git clean -fdx` im Repo-Verzeichnis würde die ungetrackte `.sqlite`-Datei löschen, weil sie
technisch im Working Tree liegt — nie in einem Deploy-Skript ohne Ausschluss von `api/data/`.

### DB-Backup

`api/src/scripts/backup-db.js` zieht per `VACUUM INTO` eine konsistente Kopie der SQLite-DB (sicher
auch im laufenden Betrieb dank WAL-Modus — ein simples `cp` könnte sonst mitten in einem
Schreibvorgang eine kaputte Kopie erzeugen) und behält per Retention nur die N neuesten Backups
(Default 14, über `BACKUP_KEEP` einstellbar). Landet unter `api/data/backups/` — dank Bind-Mount
automatisch auch auf dem Host sichtbar.

```bash
npm run backup:db                 # lokal (nutzt DATA_DIR/DB_PATH wie die App selbst)
docker compose exec app node src/scripts/backup-db.js   # im laufenden Prod-Container
```

**Empfehlung für den Server:** ein Cron-Job, z.B. täglich um 3 Uhr:
```
0 3 * * * cd /pfad/zum/repo && docker compose exec -T app node src/scripts/backup-db.js >> /var/log/ue-hacker-backup.log 2>&1
```
Die Backups selbst liegen weiterhin auf demselben Server-Volume — für echten Schutz vor
Datenverlust (Festplattendefekt, versehentliches Löschen) zusätzlich regelmäßig extern sichern
(z.B. `rsync`/`rclone` von `api/data/backups/` auf einen anderen Host oder Cloud-Speicher). Das ist
mit den Bordmitteln hier noch nicht abgedeckt — bewusst nicht mitgebaut, da das von der jeweiligen
Server-/Backup-Infrastruktur abhängt.

### Tests

| Command | Inhalt |
|---------|--------|
| `npm run test:checks` | Pre-commit: Logic, Week-Checks/Placement, Site, Merge, Storytelling-Content |
| `npm run test:auth` | API + Admin/Optionen-UI (eigene Config, Test-API :3011) |
| `npm --prefix api test` | Node-Test-Runner: `backup-db.js` (Backup + Retention) |

### Wichtige Pfade

```
api/src/          Express (index, auth, db, routes)
api/src/scripts/  backup-db.js (+ Test) — SQLite-Backup mit Retention
src/views/AdminView.vue
src/App.vue       Optionen-Modal
src/composables/useAuth*.js, useProgressSync.js, useWeekChecks.js
src/components/JupyterNotebook.vue, CodeCell.vue, PlacementCourse.vue, QuizStep.vue
scripts/migrate_notebooks_to_cells.py (einmalig gelaufen), build_cell_notebooks.py (bei jedem
  dev/build), pack_notebooks.py (zippt jetzt _bundle/*.py statt *.ipynb)
public/kurse.json
content/python-checks/config.json, week-{N}.json, index.mjs (Node-Loader für Tests)
.env.example / .env (nie committen)
```

---

## 5. Offene Aufgaben

Ausführlich in `todo.md`. Kurzfassung:

**Betrieb**
- [ ] `main` nach `origin/main` pushen und Server-Deploy (Nutzer deployt selbst: `git pull` +
      `docker compose up -d --build app`). `npm run build` muss `build:cells` vor `pack:notebooks`
      laufen lassen. Danach `/kurs/python-12-wochen-grundkurs` prüfen (Wochen-Tour, nicht Akkordeon).
- [ ] Backup-Cron auf dem Server einrichten (Befehl siehe Abschnitt 4); externe Sicherung der
      Backups bewusst nicht mitgebaut.

**Inhalte**
- Interaktiv-Kurs: "Ausführen vs. Prüfen"/Weiter-Flow — braucht konkretes Nutzer-Feedback.
- Tippfehler-Pass: `.vue`-Prosa und Interaktiv-/Projekt-Kurse noch nicht mit cspell geprüft.
- Cäsar-Chiffre und weitere Projekt-Kurse: EN-Version offen (DE-first).
- Zertifikat-PDF: E-Mail-Versand später (hängt an der Kontakt-Adresse, nicht selbst erfinden).
- Bekannte Altlasten: Notebook-Download-ZIP nur DE.
- Überlegung (nicht entschieden): dritte Sprache; UI-Ternarys sind schon auf `t()`, offen nur Content-Suffixe.

**Nächste Kurs-Themen (je eigener Branch von `main`, nicht mischen):** `kurs-python-projekte`
(Ideen in `PROJEKTIDEEN.md`), danach `kurs-ki-labor`. Roadmap: `VISION.md`.

**Bewusst nicht geplant:** öffentliches Sign-up, Mailversand/Kontaktformular, Supabase als Pflicht.

---

## 6. Entscheidungen / Konventionen (nicht ohne Rückfrage ändern)

- Ein Thema = ein Branch von `main` (`WORKFLOW.md`) — **kein** Präfix mehr (früher `cursor/…`,
  wurde entfernt)
- Jede Verhaltensänderung braucht einen Playwright-Test (`WORKFLOW.md`) — reine Text-/Typo-Korrekturen sind ausgenommen
- Accounts: Admin legt an; `ageGroup` kinder|jugendliche; ein Mensch = ein Account
- Sync: per-key Merge nach `updatedAt`
- Prod: ein Container `app`, Port 8080, API serviert Static
- SQLite bleibt; Node ≥ 22 wegen `node:sqlite`
- Vor Commit: `test:checks`; Auth-Änderungen zusätzlich `test:auth`; Verhaltensänderungen brauchen
  einen Test in `tests/*.spec.js` bzw. `api/src/scripts/*.test.js` (`WORKFLOW.md`) — nicht nur
  manuell verifizieren
- Inhaltsänderungen: `INHALTE.md` Abschnitt 6 (DE/EN, Manifeste, `kurse.json`)
- 12-Wochen-Kurs-Notebooks sind seit 3.33 **kein `.ipynb` mehr** — Zellen-Ordner mit `NN_*.py`-
  Dateien, `_generated`/`_bundle` sind generiert (gitignored, `scripts/build_cell_notebooks.py`).
  Nicht versehentlich wieder rohe `.ipynb`-Dateien als Quelle einführen.
- Missionen/Belohnungen kennen seit `wochen-zertifikate` **keine Punkte/Items mehr** — nur noch
  Zertifikate (siehe 3.12). Nicht versehentlich wieder ein Punktesystem einführen.
- Zertifikat = **nur** Wochen-Check (Quiz + beide Coding-Aufgaben), **ein** Zertifikat pro Woche
  (keine Varianten-Aufteilung). Missionen/Boss-Quests sind reine Übung, keine Voraussetzung — nicht
  versehentlich wieder an Missionen koppeln oder wieder 3 Varianten-Zertifikate einführen.
- Kein lokales Fortschritt-Skript mehr (`scripts/fortschritt.py` entfernt) — Fortschritt-Sync läuft
  über den Account (Login), nicht über CLI-Skript + manuellen JSON-Import. Nicht wieder einführen.
- Zertifikat-PDF-Download ist **login-gated** — ohne Account nur ein Hinweistext, kein Button. Nicht
  versehentlich für alle (auch rein lokalen Fortschritt ohne Login) freischalten.
- Falsch-Antwort-Erklärungen (`optionExplanations`/`optionExplanations_en` in `weeks.json`, siehe
  3.17) gibt es **nur** bei `multiple_choice`-Fragen, bewusst nicht bei `multiple_select` (mehrere
  Antworten können gleichzeitig falsch sein). Beim Hinzufügen neuer Quizfragen dieses Feld mit
  ausfüllen, sonst fällt die UI automatisch auf die geteilte `explanation` zurück (kein Bug, aber
  weniger hilfreich) — und `explanation_en` muss eine echte Übersetzung sein, nicht identisch zu
  `explanation` (Test dafür in `tests/week-checks-logic.spec.js`).

---


## 7. Schnellstart für Claude in der nächsten Session

1. `git checkout main && git pull`
2. `HANDOFF.md` + `WORKFLOW.md` lesen (werden automatisch geladen); bei Content-Arbeit `INHALTE.md`/`todo.md`
3. Neues Thema → **neuen** Branch (ohne Präfix)
4. Vor Änderungen an Pyodide, JS-Sandbox, Vue-CSS, Sync oder Notebooks: Abschnitt 3 "Gelernte Regeln" lesen.
   Nicht erwarten: Compose-Service `prod` (heißt `app`), `WeekSection.vue`-Akkordeon (seit 3.36 `WeekTour.vue`),
   `.ipynb`-Quellen im 12-Wochen-Kurs (seit 3.33 Zellen-Ordner).
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`. Nach dem Merge den Feature-Abschnitt
   ins Archiv (`docs/archiv/HANDOFF-historie.md`) verschieben und hier nur eine Zeile in der Tabelle in Abschnitt 3
   plus ggf. eine "Gelernte Regel" behalten (siehe `WORKFLOW.md`).
