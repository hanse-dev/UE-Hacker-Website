# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-10-01
> **Aktueller Stand:** `main` enthält KI-Labor komplett (Woche 1–8) sowie 3.69–3.90 (Zertifikate/PDF,
> Skip-Aufgaben, Login-Fortschritt, Pre-commit/Pre-push, Admin-Termine, Interaktiv-Kurs-Überarbeitung,
> Projekt-Kurs-Start-Gate, Worktree-Tooling, Dev-Skip-Flag, JS-Spielewerkstatt mit neuem Konzept).
> Server-Deploy steht weiter aus (Nutzer deployt selbst, siehe Abschnitt 4) — nach dem nächsten Deploy
> den einmaligen Termine-Import laufen lassen (Abschnitt 5).
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

## 2. Git

`main` ist der Integrationsstand, neue Arbeit immer **neu von `main`** in einem eigenen Branch
(siehe `WORKFLOW.md`). Die frühen PRs #1–#3 (vor der Abschnitts-Nummerierung 3.NN unten) stehen im
Archiv (`docs/archiv/HANDOFF-historie.md`).

---

## 3. Feature-Kurzübersicht (Details: `docs/archiv/HANDOFF-historie.md`, Nummern = Abschnitte dort)

Alles unten ist nach `main` gemergt. Für Details `grep -n "^### 3.NN" docs/archiv/HANDOFF-historie.md`.

| Nr. | Thema | Kern in einem Satz |
|---|---|---|
| 3.1–3.17 | Grundlagen: Einstufung/Checks, Admin+Sync (Express+SQLite), Debug-Notebook-Sicherheit (AST-Loop-Guard), Cäsar-Chiffre, Wochen-Zertifikate statt Punktesystem, Tippfehler-Pass | Details im Archiv |
| 3.18–3.31 | Refactorings + Curriculum-Lücken 12-Wochen-Kurs (Woche 1/3/4/5/6/7/8/11 bereinigt) | `config.json`/`week-N.json` statt `weeks.json` |
| 3.32–3.36 | Turtle-Canvas-Shim, Zellen-Format (`NN_*.py` statt `.ipynb`, CodeMirror 6), Wochen-Check-Validierung, `WeekTour.vue` statt Akkordeon | |
| 3.37–3.44 | `VISION.md`/`PROJEKTIDEEN.md`, Projekte-Übersicht `/projekte`, JS-Spielewerkstatt (iframe-Sandbox), `/profil` mit Abzeichen, JS-Grundkurs (9 Wochen) | |
| 3.46 | Woche 12: Text-Adventure-Abschlussprojekt statt Turtle | Komposition einziger neuer Begriff; List Comprehension neu in Woche 6 |
| 3.47/3.48 | Python Woche 1–4 als Einzel-Lektionen (Woche 3 nachträglich DE/EN angeglichen) (Lektions-Format) | `content/python-woche{N}-*`, Engine `pyodide` in `JsCourseTour`; Woche 3 DE/EN angeglichen; Woche 5–12 fertig; Lösungen aller Wochen aus Referenzlösungen (Glossar noch im alten Stil) |
| 3.49–3.53 | Python Woche 5–9 (Funktionen, Listen, Module, Dictionaries/Tupel, JSON/Dateien) als Einzel-Lektionen | je Thema 7–9 Lektionen + Debug + 3 Missionen + 3–4 Extra-Herausforderungen, DE = EN, jede Referenzlösung mit `python3` geprüft |
| 3.54 | Python Woche 10–12 (OOP Grundlagen, OOP Fortgeschritten, Text-Adventure) als Einzel-Lektionen | keine Notebook-Woche mehr in der Tour; `validation.codeContains`/`validation.stdin` eingeführt; alle 2.972 Aufgaben-Lösungen Woche 1–12 neu erzeugt |
| 3.55 | Alte Notebooks entfernt, ZIP-Download neu aus dem Lektions-Format | `scripts/build_lesson_bundle.py` baut Download direkt aus dem Lektions-Format, DE+EN |
| 3.56/3.57 | Woche 2 DE/EN angeglichen (Abenteuer/Pferde, dann Sci-Fi) | Sci-Fi ausnahmsweise umgekehrt: EN war größer, DE wurde angeglichen |
| 3.58 | Projekt-Kurs Vigenère-Chiffre (Nachfolger Cäsar-Chiffre) | `content/vigenere-chiffre`, 5 Lektionen, DE-first |
| 3.59 | Projekt-Kurs Snake (Nachfolger JS-Spielewerkstatt) | `content/js-snake`, JS-Sandbox/Canvas, 6 Lektionen |
| 3.60 | Projekt-Kurs Text-Adventure/Fluchtraum | `content/text-adventure-fluchtraum`, 6 Lektionen, Pyodide |
| 3.61 | Alle 7 Projekt-Kurse auf "selbst schreiben + Lösung auf Wunsch" umgestellt | `codeTemplate` blankt nur neu eingeführte Funktionskörper, neuer "Lösung anzeigen"-Button |
| 3.62 | Projekt-Abschluss zeigt Abzeichen-Hinweis + Link zu /projekte | Neue Komponente `ProjectCompletionBox.vue` |
| 3.63 | Lokales Tool: Account anlegen + Thermodrucker-Ausdruck | `scripts/local-tools/create-account-printout.py`, nicht deployed |
| 3.64 | Login-Formulare für Passwort-Manager + Admin-Nav-Link nur bei Login | Admin-/Account-Login jetzt echte `<form>`s mit `name`-Attributen (1Password-Autofill) |
| 3.65 | Tippfehler-Pass (cspell) auf Lektions-Format/JS-Grundkurs/Interaktiv-/Projekt-Kurse | 0 echte Tippfehler in 1306 Dateien, 280 legitime Wörter in `cspell.json` ergänzt |
| 3.66 | KI-Labor gestartet — Kursplan + Woche 1 "Was ist KI?" | `KiLaborTour.vue`, `content/ki-labor-woche1`, Check-System um `courseKey` vorbereitet |
| 3.67 | KI-Labor: Quiz + Wochen-Zertifikat nachgezogen | `useWeekChecks.js`/`WeekCheckPanel.vue`/`CodeChallenge.vue`/`useCertificatePdf.js` um `courseKey` generalisiert |
| 3.68 | KI-Labor: Woche 2 "Daten sind alles" | 5 Lektionen + Debug + Mission + 3 Extra-Herausforderungen + eigener Wochen-Check |
| 3.69 | Profil zeigt Wochen-Zertifikate + "Kurs starten"-Gate | `useCourseCertificates.js` neu; `CourseDetail.vue` blendet Beschreibung/Struktur hinter einem Start-Button aus |
| 3.70 | Profil: PDF-Download direkt am Zertifikat | `loadWeekLernziele()` (Python) + `src/data/kiLaborWeeks.js` (KI-Labor) liefern die Lernziele fürs PDF |
| 3.71 | Woche 4 + 9: `input()`-Lücken aus `todo.md` geschlossen | Neuer `validation.stdin`-Schritt je Thema (Woche 4 Boss-3, Woche 9 Boss-1 "Eigener Eintrag"), DE+EN, ans Ende der Lektion/Notebook-Zellfolge angehängt statt eingefügt |
| 3.72–3.77 | KI-Labor: Woche 3–8 (k-NN, Training & Test, Entscheidungsbäume, Neuronale Netze I+II, Grenzen & Ethik) | je 5 Lektionen + Debug + Mission + 3 Extra-Herausforderungen + eigener Wochen-Check; alle Beispiele/Lösungen mit `python3` geprüft; nach Woche 8 kein "nächste Woche"-Button mehr |
| 3.78 | `output_contains` toleriert Groß-/Kleinschreibung, Leerzeichen, Satzzeichen am Ende | `output_equals` bleibt bewusst exakt (prüft teils auf ungewollte Extra-Ausgabe); Test in `week-checks-logic.spec.js` |
| 3.79 | Interaktiv-Kurs: Lektionstexte ausführlicher (Kinder + Jugendliche, DE) | reine Textüberarbeitung, keine Logikänderung |
| 3.80 | Lektionsaufgaben prüfen nur noch die Ausgabe, nicht mehr Code-Struktur/Variablen | `useTaskValidation.js` trennt `validateOutput()` (nur Ausgabe) von `structuralChecksOk()` (nur noch `CodeChallenge.vue`/Wochen-Check) |
| 3.81 | Lektionsaufgaben überspringbar (nach 2 Fehlversuchen) | `.btn-skip` in `LessonView.vue`/`JsLessonView.vue`, `skippedTasks` zählt für den Lektions-Abschluss mit (⏭ statt ✓); gilt nicht für `CodeChallenge.vue` |
| 3.82 | Login ersetzt lokalen Fortschritt durch Account-Stand statt zu mergen | `loadAccountProgress()`/`replaceLocalProgress()` in `useProgressSync.js`, nur beim expliziten Login; Seiten-Reload merged weiter nach `updatedAt` |
| 3.83 | Pre-commit/Pre-push zweistufig statt vollem `test:checks` bei jedem Commit | `scripts/test-changed.mjs` mappt staged Dateien auf betroffene Specs (Pre-commit); voller `test:checks` im Pre-push-Hook |
| 3.84 | Termine im Admin-Panel verwaltbar statt per Hand in `public/termine.json` | `termine`-Tabelle (SQLite) + `/api/termine` (GET) + `/api/admin/termine` (CRUD), Tab „Termine“ in `AdminView.vue`; einmaliger Umzug per `api/src/scripts/import-termine-json.js` |
| 3.85 | Interaktiv-Kurs: Editor-Erklärungen, flexible Lektionen (5 Aufgaben, mind. 2 nötig) + Beispiel-Aufgabe | `lesson.editorHint` erklärt Ausführen vs. Prüfen, Hinweis für `___`-Lücken; `lesson.minSolved` in `LessonView.vue` macht eine Lektion "flexibel" (Rest sofort überspringbar) |
| 3.86 | Projekt-Kurse: "Kurs starten"-Gate + Lektionsliste als horizontale Leiste statt Seitenspalte | `isFocusableCourse` (`CourseDetail.vue`) gilt auch für Projekt-Kurse; geteiltes `course-layout.css` einspaltig, `.lessons-list` als Chip-Reihe; `InteractiveCourse.vue` scrollt bei "Weiter" jetzt an den Lektionsanfang |
| 3.87 | Git-Worktree-Tooling | `npm run worktree:new`/`worktree:remove`, eigene Ports je Worktree (`worktree.ports.json`), siehe `WORKFLOW.md` |
| 3.88 | Test-Kurs "Fang den Ball" (neues Konzept) | jede Aufgabe baut am echten laufenden Spiel weiter; `task.showCanvas: false` blendet den Canvas-Kasten pro Aufgabe aus; seit 3.90 Inhalt von `js-spielewerkstatt` |
| 3.89 | Dev-Flag: Aufgaben-Prüfung überspringen | `npm run dev:skip-checks` (`VITE_DEV_SKIP_CHECKS=1`) lässt "Prüfen" in `JsLessonView.vue` sofort durchgehen, hinter `import.meta.env.DEV` (nicht im Prod-Build), mit Hinweis-Banner |
| 3.90 | JS-Spielewerkstatt durch das neue Konzept ersetzt | `content/js-spielewerkstatt` = die 7 Lektionen des Test-Kurses (ID/URL unverändert), alter Inhalt, Test-Eintrag und `hidden`-Flag entfernt; Funktionen per `output_equals` statt `functionCalls` geprüft; empfohlenes Vorwissen JS-Grundkurs Woche 4; Durchlauf-Test über alle Musterlösungen |
| 3.91 | "Zurücksetzen"-Button für vorgegebenen Code | `.btn-reset` in `LessonView.vue`/`JsLessonView.vue`/`CodeChallenge.vue`, sichtbar sobald der Code vom (nicht leeren) `codeTemplate` abweicht; setzt nur diese eine Aufgabe zurück (inkl. Ausgabe/Feedback) |

### Gelernte Regeln (wiederverwendbare Fallstricke)

**Content / Notebooks**
- Bulk-Edits an JSON/Notebooks nie per volle Reserialisierung, sondern gezielte Text-Ersetzung + `json.loads()` danach (3.12, 3.16). Seit 3.33 sind 12-Wochen-Notebooks Zellen-Ordner (`NN_*.py`) — keine `.ipynb` als Quelle wieder einführen.
- Debug-Bugs müssen vom Kernel-Zustand unabhängig sein und dürfen die Lösung nicht verraten. Nach Notebook-Änderung Code-Zellen mit gemeinsamem Namespace per `python3` ausführen.
- Ein "Fund" aus einer Variante gilt nicht automatisch für alle: vor Massenänderungen alle 3 Varianten × DE/EN grep-prüfen.
- Neue Aufgabe im Lektions-Format: in `lessons.json` ans Ende von `tasks` anhängen und im passenden
  `_N_loesungen`-Notebook-Ordner ein neues Markdown+Code-Zell-Paar mit der **höchsten** Nummer ans
  Ende — nie mittendrin einfügen (sonst müssen alle folgenden Zellen umnummeriert werden).
- Standard-PDF-Fonts (pdf-lib/Helvetica) können kein Emoji — Content-Texte vorher per `sanitizeForPdfFont` filtern (3.13).
- Punkte-/Item-System und lokales Fortschritt-Skript **nicht** wieder einführen; Zertifikat = nur Wochen-Check, ein Zertifikat pro Woche, PDF login-gated (3.12/3.13).
- Quizfragen `multiple_choice`: `optionExplanations` mitpflegen, `explanation_en` echt übersetzen; `shuffleQuestionOptions()` muss Text+Erklärung als Paar mischen (3.17). Schwelle nie als exakten Bruch (2/3 → `0.66`, 3.6).
- Projekt-Kurse: der Erklärtext einer Lektion darf die direkt folgende Aufgabe nicht vorwegnehmen — weder als lauffähiger Code (Pseudocode nutzen, siehe 3.61), noch als "Beispiel"-Aufgabe, die exakt dieselbe Funktion wie die nächste "Pflicht"-Aufgabe zeigt (Beispiel muss eine *andere* Instanz desselben Prinzips sein, wie `verdopple` vor `bewegeSchlaeger` in js-spielewerkstatt).

**Pyodide / Ausführung**
- Kein Web Worker: `input()` läuft synchron über `window.prompt()` (65 Notebooks, 3.5). Loop-Guard ist AST-basiert.
- `turtle` gibt es in Pyodide nicht — eigener Canvas-Shim in `usePyodide.js` (3.32).
- Kernel in Tests immer über `startKernel()` starten, nie `if (await btn.isEnabled()) click()` — der
  Button kann dazwischen deaktiviert werden, `click()` hängt dann bis zum Timeout (flaky Tests).
- `CodeChallenge` startet den Kernel nicht selbst; Tests klicken `.btn-kernel` explizit.
- Namespace-Variablen vor jedem Check-Lauf löschen; `pyodide.globals.delete()` wirft bei unbekanntem
  Namen → try/catch. Vor `functionCalls`-Re-Aufruf `__cell_deadline__` neu setzen.
- Seit 3.80 prüft `validateOutput()` (`LessonView.vue`/`JsLessonView.vue`) **nur noch die Ausgabe** —
  `codeContains`/`variables`/`functionCalls` werden dort ignoriert. Neue Aufgaben ohne eigenes
  `output_contains` bestehen dann schon bei fehlerfreiem Code — immer ein `expected` ergänzen. Nur
  der Wochen-Check (`CodeChallenge.vue`) nutzt weiterhin `structuralChecksOk()` mit echten Checks.

**JS-Sandbox (`js-spielewerkstatt`, `js-grundkurs`)**
- `functionCalls` sieht nur `function`-Deklarationen/`var`; keine Arrow-Functions/Klassen-Methoden (3.43).
- `valuesMatch()` vergleicht Arrays nur per `===` → nie ein Array als `expected`, nur abgeleitete Skalare.
- `dom_text`/`dom_click_text`/`canvas_*` nutzen `validation.text`, nicht `expected`.
- Chromium drosselt `requestAnimationFrame` in Off-screen-iframes → `scrollIntoView()` vor dem Lauf.
  `postMessage` nur mit reinen Werten (Vue-Proxies lassen sich nicht klonen).
- Keine echte Endlosschleife als Debug-Bug (kein Loop-Guard, nur 5s-Timeout).

**Vue / CSS / Tests**
- `@import` in `<style scoped>` bekommt einen anderen Scope-Hash → in separaten **unscoped** `<style>`-Block. Vor CSS-Extraktion Klassennamen repo-weit grep-prüfen (3.19, 3.20).
- Watcher, die nach dem Rendern scrollen: `flush: 'post'` (3.39).
- Sync darf nach Server-Apply keinen vollen Notebook-Re-Fetch auslösen (Blink-Schleife, 3.3).
- Seit Woche 12 ist kein Kurs-Schritt mehr ein Notebook: Tests, die `.cell`/`.btn-run-cell` brauchen,
  öffnen „Lösungen“ über `openSolutionsNotebook()` (30s-Timeout, 15s reicht unter Last nicht).
- CodeMirror ist keine `<textarea>`: Tests nutzen `tests/helpers/codemirror.js`.
- Beim Umbenennen von Testdateien `package.json`-Skripte mitprüfen — Playwright ignoriert fehlende
  Dateien stillschweigend, nur der Test-Zähler sinkt (3.43).
- `test:auth` nutzt Port 5174 mit Proxy-Header; läuft dort ein "nackter" Vite, kommen 502er (3.36).
- Neue `LessonView.vue`-Kurse: Glob-Listen sind Wildcards — nur Content-Ordner + `kurse.json` nötig.
- Deep-Links `?week=&tab=` (Einstufung, Cäsar-Chiffre) bewusst unverändert lassen, `WeekTour.vue`
  übersetzt intern.
- cspell: Wörterbücher brauchen `"import"`, nicht nur `"dictionaries"`.
- Komponente wird beim Umschalten eines `v-if`-Zweigs neu gemountet → lokaler State geht verloren,
  wenn er nicht vom Parent gehalten wird; beim Neu-Mount auf sinnvollen Zustand zurückfallen (3.55).
- Login-Felder für Passwort-Manager-Autofill brauchen ein echtes `<form>` + `name`-Attribute; bei
  reinem Passwort-Login (kein Benutzername im Modell, z.B. Admin) ein verstecktes `username`-Feld
  mit festem Wert ergänzen (3.64).
- Reaktiver Zustand über mehrere Komponenten (z.B. Admin-Token) gehört als geteilter `ref` in die
  Composable, nicht als lokaler Ref pro Komponente (3.64).
- Ein Composable, das nur für **einen** Kurs gebaut wurde (Storage-Key/Content-Pfad fest verdrahtet),
  braucht beim Verallgemeinern einen `courseKey`-Parameter mit Default = bisheriges Verhalten, und
  **immer** die komplette bestehende Test-Suite des Erstnutzers gegenlaufen lassen, nicht nur den
  neuen Kurs (3.67).
- Ein Bildschirm hinter einen Klick-Button setzen (z.B. "Kurs starten") heißt: repo-weit nach
  bisherigen `page.goto(...)`-Zeilen grep-suchen, die jetzt den Klick davor brauchen — Deep-Links
  mit Query-Parametern, die den Gate-Zustand ohnehin öffnen, brauchen keine Änderung (3.69).
- CSS-Kind-Selektoren wie `.course-detail > h1` in Tests brechen stillschweigend, wenn ein neuer
  Wrapper-`<div>` dazwischenkommt — vor dem Verschachteln repo-weit nach dem Selektor suchen (3.69).
- `test:checks` (~2 Min, 381 Tests) läuft nicht mehr bei jedem Commit, sondern nur vor dem Push;
  Pre-commit nutzt `scripts/test-changed.mjs` (mappt geänderte Dateien → Specs). Neue Komponenten/
  Composables/Content-Ordner brauchen dort eine eigene Regel in `RULES`, sonst greift nur das
  Sicherheitsnetz (voller Lauf) statt des schnellen Pfads (3.83). Regel mit leerer Liste = Datei
  wird von `test:checks` gar nicht abgedeckt (API, lokales Tooling) → beim Commit kein Lauf.
- Generierte, gitignorte Dateien (Notebook-`_generated`/`_bundle`, ZIPs) erzeugt der Playwright-
  Webserver nicht selbst; `scripts/ensure-test-prereqs.mjs` (`globalSetup`) stellt sie vor jedem
  Lauf sicher. Fehlten sie (frischer Worktree), brauchte `test:checks` >15 Min statt ~2.
- `lesson.minSolved` (flexible Lektion, Rest von Anfang an überspringbar) heißt: Aufgaben dürfen
  sich nicht auf Variablen aus einer vorherigen Aufgabe verlassen — eine übersprungene Aufgabe hat
  ihren Code nie ausgeführt (3.85).
- Letzte Coding-Aufgabe einer Projekt-Lektion darf nicht durch reines Kopieren des vorherigen Teils
  lösbar sein: nur der neue Teil ist blind, bereits Gebautes bleibt als Kontext stehen (3.88).

**Lokale Tools (`scripts/local-tools/`, laufen nie im Deploy)**
- IDN-Domains (Umlaute) vor jedem `urllib`-Request per `.encode('idna')` in Punycode wandeln, sonst
  kappt der Server die Verbindung ohne Fehlermeldung (3.63).
- macOS/Homebrew-Python verweigert systemweite `pip install`s (PEP 668) → eigenes `venv/`; zum
  Erkennen `sys.prefix` prüfen, nicht `Path(sys.executable).resolve()` (venv-Symlink täuscht sonst
  Identität mit System-Interpreter vor) (3.63).
- `bleak`/BLE auf macOS: CoreBluetooth liefert eine app-spezifische UUID statt der echten MAC (per
  Scan ermitteln); Writes ohne kleine Pause (~10ms) zwischen den Häppchen verwirft macOS still (3.63).

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

SQLite bleibt in `./api/data/` (Bind-Mount, gitignored). Env-Änderung → Container **recreate**, nicht
nur rebuild. `git pull` + Rebuild lässt Nutzerdaten unangetastet. **Einzige echte Gefahr:**
`git clean -fdx` würde die ungetrackte `.sqlite`-Datei löschen — nie ohne Ausschluss von `api/data/`.

### DB-Backup

`api/src/scripts/backup-db.js` zieht per `VACUUM INTO` eine konsistente Kopie (sicher im laufenden
Betrieb dank WAL, ein `cp` könnte eine kaputte Kopie erzeugen) und behält per Retention nur die N
neuesten Backups (Default 14, `BACKUP_KEEP`). Landet unter `api/data/backups/`.

```bash
npm run backup:db                 # lokal (nutzt DATA_DIR/DB_PATH wie die App selbst)
docker compose exec app node api/src/scripts/backup-db.js   # im laufenden Prod-Container
```

**Empfehlung für den Server:** ein Cron-Job, z.B. täglich um 3 Uhr:
```
0 3 * * * cd /pfad/zum/repo && docker compose exec -T app node api/src/scripts/backup-db.js >> /var/log/ue-hacker-backup.log 2>&1
```
Externe Sicherung der Backups (z.B. `rsync`/`rclone` auf einen anderen Host) ist bewusst nicht
mitgebaut — hängt von der jeweiligen Server-Infrastruktur ab.

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
- [ ] Server-Deploy (`git pull` + `docker compose up -d --build app`), danach
      `/kurs/python-12-wochen-grundkurs` prüfen (Wochen-Tour).
- [ ] Backup-Cron auf dem Server einrichten (Befehl siehe Abschnitt 4).
- [ ] Nach dem Deploy einmalig `docker compose exec app node api/src/scripts/import-termine-json.js`
      laufen lassen (übernimmt `termine-seed.json` in die neue `termine`-Tabelle).

**Inhalte**
- Interaktiv-Kurs: "Ausführen vs. Prüfen"/Weiter-Flow — braucht konkretes Nutzer-Feedback.
- Alle 7 Projekt-Kurse: EN-Version offen (DE-first, `kurse.json` hat schon `title_en`).
- Zertifikat-PDF: E-Mail-Versand später (hängt an der Kontakt-Adresse, nicht selbst erfinden).
- Überlegung (nicht entschieden): dritte Sprache; UI-Ternarys sind schon auf `t()`, offen nur Content-Suffixe.

**Nächstes Kurs-Thema:** noch nicht entschieden (KI-Track weiter vs. weitere Python-Projekt-Kurse,
siehe `VISION.md` "Offene Fragen"). Ideen-Backlog: `PROJEKTIDEEN.md`.

**Bewusst nicht geplant:** öffentliches Sign-up, Mailversand/Kontaktformular, Supabase als Pflicht.

---

## 6. Entscheidungen / Konventionen (nicht ohne Rückfrage ändern)

- Ein Thema = ein Branch von `main` in einem eigenen Worktree (`WORKFLOW.md`) — **kein** Präfix mehr (früher `cursor/…`,
  wurde entfernt)
- Jede Verhaltensänderung braucht einen Playwright-Test (`WORKFLOW.md`) — reine Text-/Typo-Korrekturen sind ausgenommen
- Accounts: Admin legt an; `ageGroup` kinder|jugendliche; ein Mensch = ein Account
- Sync: per-key Merge nach `updatedAt` beim Seiten-Reload (`restoreSession`/`syncNow`). Beim
  expliziten Login (`loadAccountProgress`) wird dagegen **nicht** gemergt: der Account-Stand
  ersetzt den kompletten lokalen Fortschritt (auch beim allerersten Login mit leerem Account,
  bewusst so — kein Sonderfall, siehe 3.82). Grund: geteilter Rechner, Nutzerwechsel beim Login.
- Prod: ein Container `app`, Port 8080, API serviert Static
- SQLite bleibt; Node ≥ 22 wegen `node:sqlite`
- Vor Commit: `test:checks`; Auth-Änderungen zusätzlich `test:auth`; Verhaltensänderungen brauchen
  einen Test in `tests/*.spec.js` bzw. `api/src/scripts/*.test.js` (`WORKFLOW.md`) — nicht nur
  manuell verifizieren
- Inhaltsänderungen: `INHALTE.md` Abschnitt 6 (DE/EN, Manifeste, `kurse.json`)
- 12-Wochen-Kurs-Notebooks sind seit 3.33 **kein `.ipynb` mehr** — Zellen-Ordner mit `NN_*.py`,
  `_generated`/`_bundle` generiert (gitignored). Nicht wieder rohe `.ipynb`-Quellen einführen.
- Missionen/Belohnungen kennen **keine Punkte/Items mehr** — nur Zertifikate. Nicht wieder
  einführen.
- Zertifikat = **nur** Wochen-Check (Quiz + beide Coding-Aufgaben), **ein** Zertifikat pro Woche.
  Missionen/Boss-Quests sind reine Übung, keine Voraussetzung.
- Kein lokales Fortschritt-Skript mehr — Fortschritt-Sync läuft über den Account (Login).
- Zertifikat-PDF-Download ist **login-gated** — ohne Account nur Hinweistext, kein Button.
- Falsch-Antwort-Erklärungen (`optionExplanations(_en)` in `weeks.json`) gibt es **nur** bei
  `multiple_choice`, bewusst nicht bei `multiple_select`. Bei neuen Quizfragen mitpflegen, sonst
  fällt die UI auf die geteilte `explanation` zurück; `explanation_en` muss echt übersetzt sein.
- `validation.type: "output_contains"` prüft tolerant (Groß-/Kleinschreibung, Leerzeichen,
  Satzzeichen am Ende egal) — `output_equals` bleibt exakt, bewusst nutzen wenn "keine
  Extra-Ausgabe" der Lernpunkt ist.
- Termine kommen aus der `termine`-Tabelle über `/api/termine`, nicht mehr aus
  `public/termine.json` — Pflege nur über Admin-Panel (`/admin` → Tab „Termine“).

---

## 7. Schnellstart für Claude in der nächsten Session

1. `git checkout main && git pull`
2. `HANDOFF.md` + `WORKFLOW.md` lesen (werden automatisch geladen); bei Content-Arbeit `INHALTE.md`/`todo.md`
3. Neues Thema → **neuen** Branch (ohne Präfix), immer im eigenen Worktree: `npm run worktree:new -- <branch>`
4. Vor Änderungen an Pyodide, JS-Sandbox, Vue-CSS, Sync oder Notebooks: Abschnitt 3 "Gelernte Regeln" lesen.
   Nicht erwarten: Compose-Service `prod` (heißt `app`), `WeekSection.vue`-Akkordeon (seit 3.36 `WeekTour.vue`),
   `.ipynb`-Quellen im 12-Wochen-Kurs (seit 3.33 Zellen-Ordner).
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`. Nach dem Merge den Feature-Abschnitt
   ins Archiv (`docs/archiv/HANDOFF-historie.md`) verschieben und hier nur eine Zeile in der Tabelle in Abschnitt 3
   plus ggf. eine "Gelernte Regel" behalten (siehe `WORKFLOW.md`).
