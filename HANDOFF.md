# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-10-14
> **Aktueller Stand:** `main` enthält alles bis 3.113 (siehe Tabelle in Abschnitt 3).
> Server-Deploy steht weiter aus (Nutzer deployt selbst, siehe Abschnitt 4) — nach dem nächsten Deploy
> den einmaligen Termine-Import laufen lassen (Abschnitt 5).
> **Ziel dieser Datei:** Nachschlagewerk für Stand, Feature-Übersicht und gelernte Fallstricke.
> Sie wird **nicht** automatisch geladen (nur `CLAUDE.md` ist das) — gezielt den passenden Abschnitt
> lesen. Die ausführliche Feature-Historie liegt in `docs/archiv/HANDOFF-historie.md`.

---

## 1. Was ist das Projekt?

Lernplattform für Kinder/Jugendliche (Python) — Vue 3 + Vite, Notebooks unter `content/`, Docker-Deploy.

**Live/Prod-Modell:** Ein Node-Prozess (`api/`) liefert `/api/*` **und** das gebaute Frontend (`dist/`) auf Port **8080**. Service-Name in Compose: **`app`** (nicht mehr `prod`).

---

## 2. Git

`main` ist der Integrationsstand, neue Arbeit immer **neu von `main`** in einem eigenen Branch
(siehe `WORKFLOW.md`).

---

## 3. Feature-Kurzübersicht (Details: `docs/archiv/HANDOFF-historie.md`, Nummern = Abschnitte dort)

Alles unten ist nach `main` gemergt. Details: `grep -n "^### 3.NN" docs/archiv/HANDOFF-historie.md`
(dort am Ende auch die frühere, ausführliche Tabelle).

| Nr. | Bereich | Kern |
|---|---|---|
| 3.1–3.46 | Grundlagen | Admin + Sync (Express/SQLite), Wochen-Checks/Zertifikate, Zellen-Format `NN_*.py`, `WeekTour.vue`, `/projekte`, `/profil`, JS-Spielewerkstatt + JS-Grundkurs, Woche 12 Text-Adventure |
| 3.47–3.57, 3.71, 3.100 | Python 12 Wochen im Lektions-Format | `content/python-woche{N}-{thema}[-en]/`, `JsCourseTour` mit `engine="pyodide"`, `codeContains`/`stdin`, Lösungen per `sync_loesungen.py`, ZIP per `build_lesson_bundle.py` |
| 3.58–3.62, 3.105 | Python-Projekt-Kurse | `ProjectCourse.vue`; `codeTemplate` blankt nur neue Funktionskörper; `ProjectCompletionBox.vue` |
| 3.66–3.70, 3.72–3.77, 3.96 | KI-Labor + Zertifikate im Profil | Checks per `courseKey`, `useCourseCertificates.js`, `referenceSolution` (geprüft von `check_kilabor_solutions.py`), Start-Gate auf der Kursseite |
| 3.78–3.81, 3.85, 3.91, 3.94 | Prüf-Logik und Lektions-UI | `validateOutput()` (tolerant/exakt), Struktur-Checks nur im Wochen-Check, Überspringen nach 2 Fehlversuchen, Zurücksetzen, `minSolved`, Glossar-Regex |
| 3.82, 3.99, 3.102 | Accounts und Fortschritt | Login ersetzt lokalen Stand, Fortschritts-Vertrag (`contract:update`), Passwort ändern/Einmal-Passwort |
| 3.83, 3.87, 3.89/3.97, 3.98, 3.118 | Tooling | `test-changed.mjs`, Worktrees, Dev-Modus `dev:skip-checks` (API + Vite, auch Admin ohne Passwort), cspell + `lint:spelling:de` |
| 3.63–3.65, 3.84, 3.112 | Admin und Betrieb | Thermodrucker (`scripts/local-tools/`), Termine im Admin, Beta-Kennzeichen + Admin-Reiter „Kurse“ |
| 3.86/3.93, 3.95 | Kursseite und Downloads | Start-Gate `?started=1`, Offline-Downloads in 3 Formaten |
| 3.88/3.90, 3.92, 3.103/3.104, 3.106/3.107 | JS-Kurse und Sandbox | DOM-Projekte Memory/Quiz (`sandboxMode: "dom"`), eine Arbeitsfläche pro Lektion (breit rechts, auch in reinen Konsolen-Lektionen mit der Ausgabe) |
| 3.101, 3.109, 3.119, 3.120 | micro:bit | `engine: "anleitung"` → `GuideLessonView.vue` (Blöcke/Python, Ampel, „Fang den Stern“ und Einführung auch JavaScript); Einführung `unlisted`, jede micro:bit-Kursseite verweist per Kasten darauf; keine Paar-Rollen (Kurse funktionieren auch allein) |
| 3.121 | Partnerarbeit + Gutschrift | `PartnerBox.vue`/`usePartner.js` (zweiter Account schreibt per `PATCH /api/progress` mit, nur `anleitung`-Kurse), Admin „Projekt gutschreiben“; Tests nur in `test:auth` |
| 3.108, 3.110, 3.111 | Begriffs-Links | `content/begriffe.json` + `useConcepts.js`; jeder neue Kurs braucht Links oder eine begründete Ausnahme |
| 3.113 | Turtle-Shim entfernt | kein Kurs nutzt Turtle mehr |
| 3.114–3.117 | Web-Track „Meine erste Website“ | `sandboxMode: "web"`, `validation.type: 'web'`; Stufenwahl `WebsiteCourse.vue`: Einfach (Lektionsliste, `finalCheck`, „Meine Seite“ wächst mit) und Intensiv (`WeeklyCourseTour.vue`, `content/web-grundkurs-*`) |
| 3.122 | Dark Mode | `useTheme.js` (System/Hell/Dunkel in „Optionen“, nur `localStorage` `ue-hacker-theme`), Inline-Skript in `index.html`, Farb-Tokens in `src/style.css`, Editor-Farben `src/utils/editorTheme.js` |
| 3.123 | Verständlichkeit prüfen | `npm run check:verstaendlichkeit [-- --wochen 1-3 --out bericht.md]` (`scripts/check_verstaendlichkeit.py`): Lösung braucht nie Gezeigtes, zu viel Neues, Begriff zu früh, Fachwörter, lange Sätze/LIX; nur Bericht, kein Test-Gate |
| 3.124 | Stolperstellen-Zähler | anonyme Summen je Aufgabe (`task_stats`, `routes/taskStats.js`), gemeldet von `LessonView`/`JsLessonView` über `useTaskStats.js`, Admin-Reiter „Stolperstellen“ (`AdminStolperstellen.vue`); Tests nur in `test:auth` |
| 3.125 | KI als Test-Kind | `npm run testkind -- --wochen 3 [--lektion lektion-02] [--alter 10] --out bericht.md` (`scripts/ki_testkind.py`): Claude spielt über die `claude`-CLI ein Kind, das nur das bisherige Material kennt; Code wird gegen `expected` geprüft. Nur lokal, Vorfilter fürs Beobachten |

### Gelernte Regeln (wiederverwendbare Fallstricke)

Was schon in `CLAUDE.md` steht (IDs/Fortschritt, Prüf-Logik über `useTaskValidation.js`, kein
Punkte-System, Zertifikate), wird hier nicht wiederholt.

**Content**
- JSON gezielt ersetzen + danach `json.loads()` prüfen; in Skripten erst lesen, dann schreiben (`open(f, 'w')` leert die Datei sofort).
- Lösungs-Markdown-Zellen (`*_6_loesungen/NN_markdown.py`) speichern `"` mal roh, mal als `\"`: beim Ersetzen beide Formen suchen, neue Anführungszeichen immer als `\"` schreiben (ein `"` direkt vor dem schließenden `"""` bricht die Zelle); danach `sync_loesungen.py --check`.
- Ein Fund in einer Variante gilt nicht automatisch für alle: vor Massenänderungen alle 3 Themen × DE/EN per grep prüfen.
- Reihenfolge = Position in `lessons.json`, nicht die ID (3.100). Neue Aufgaben ans Ende einer Lektion hängen.
- Debug-Aufgaben: vom Kernel-Zustand unabhängig, verraten die Lösung nicht, keine echte Endlosschleife (JS hat nur 5 s Timeout). Ihr `codeTemplate` ist absichtlich kaputt – Generatoren kompilieren nur Beispiele und Lösungen (3.95).
- Neue Lektions-Aufgabe (12 Wochen): Lösung als Zell-Paar mit der **höchsten** Nummer in `_6_loesungen`, dann `python3 scripts/sync_loesungen.py`; Aufgabentext ändern = `lessons.json` **und** Lösungs-Markdown, danach jede Lösung per `python3` gegen `expected` laufen lassen (3.98).
- Neuer Python-Projekt-Kurs: `PROJECT_COURSES` in `build_project_notebook.py`, Zähler in `lesson-notebook-generator.spec.js`, `lint:spelling`-Globs, Kartenzahlen in `projekte.spec.js` (Checkliste `INHALTE.md` §6).
- Projekt-Lektionen: Erklärtext und Beispiel dürfen die nächste Pflichtaufgabe nicht vorwegnehmen (andere Instanz desselben Prinzips); letzte Aufgabe nicht durch Kopieren des Vorherigen lösbar (3.61, 3.88).
- Statistik-Beispieltexte (Häufigkeitsanalyse) per Skript prüfen: eindeutiger Spitzenreiter, klarer Abstand (3.105).
- Quiz: `optionExplanations` mitpflegen, `explanation_en` echt übersetzen, Schwelle nie als exakter Bruch (2/3 → `0.66`); keine doppelten Leerzeichen in Fragen (Anzeige fasst sie zusammen). Fragen und Lernziele nur zu Stoff genau dieser Woche.
- PDF-Standardfonts können kein Emoji → `sanitizeForPdfFont` (3.13).
- cspell ist für Deutsch nur ein grobes Netz → zusätzlich `lint:spelling:de` (LanguageTool, nie parallel zu Testläufen – die Last lässt Tests scheitern). Bezeichner nicht ins Wörterbuch, sondern per `ignoreRegExpList` (Code-Felder, `.klasse`, `#id`, `--var`, `id="…"`). Wörterbücher brauchen `"import"`, nicht nur `"dictionaries"`.

**Pyodide / Python-Tests**
- Kein Web Worker: `input()` über `window.prompt()`, Loop-Guard AST-basiert. `turtle` gibt es nicht (Shim seit 3.113 weg, `git log -S _install_turtle_shim`).
- Kernel in Tests über `startKernel()`/`dispatchEvent('click')` (`tests/helpers/kernel.js`), nach „Weiter“ `waitForFreshLesson()`; `CodeChallenge` startet den Kernel nicht selbst.
- Namespace vor jedem Check-Lauf leeren (`globals.delete()` wirft bei unbekanntem Namen); vor `functionCalls` `__cell_deadline__` neu setzen.
- Lektionen prüfen nur die Ausgabe – neue Aufgaben brauchen immer ein `expected` (sonst bestehen sie bei fehlerfreiem Code).
- `lesson.minSolved` (flexible Lektion): Aufgaben dürfen nicht auf Variablen einer vorherigen Aufgabe bauen – übersprungene Aufgaben liefen nie (3.85).

**JS-Sandbox**
- `functionCalls` sieht nur `function`/`var`, keine Arrow-Functions/Methoden; nie ein Array als `expected`; `dom_*`/`canvas_*` nutzen `validation.text`.
- Eine Sandbox pro Lektion (`.js-workspace iframe.js-sandbox`, 3.106): iframe nie im DOM umhängen (lädt neu), Position nur per CSS; `postMessage` nur mit reinen Werten; Off-screen-iframes drosseln `requestAnimationFrame` → `scrollIntoView()`.
- Ids in der Sandbox sind globale Namen; `status`/`name`/`top` gehören dem Fenster.
- DOM-Projekte (`sandboxMode: "dom"`): `dom_click_text` klickt und liest im selben Tick (nichts hinter `setTimeout` prüfbar), klickt auch versteckte, aber keine `disabled` Knöpfe; Zufall nur über reihenfolge-unabhängige Eigenschaften prüfen; Zustand ohne Klick-Folge nur prüfbar, wenn die Vorlage ihn herbeiführt. Ohne `sandboxMode` laufen `dom_*`-Checks unsichtbar trotzdem.
- Web-Modus (`sandboxMode: "web"`): `srcdoc` läuft immer im Standard-Modus; Basis-URL ist die Kursseite (Harness fängt Links/Formulare ab). CSS über `property` + `value`/`notValue` (Probe-Element normalisiert; frei wählbare Werte mit `notValue` gegen die Vorlage, Browser-Standard = `"initial"`). Die Probe hat keinen Rahmenstil → `probeStyle()` setzt ihn für `border-*-width` selbst. `grid-column: span 2` landet in `grid-column-start`. Media Queries über den CSS-Text prüfen (Vorschau-Breite schwankt).
- Browser reparieren kaputtes HTML anders als erwartet (`<p><strong>…</p><p>` legt den zweiten Absatz **in** das strong) → Debug-Aufgaben über den sichtbaren Effekt prüfen.
- Jede Pflichtaufgabe gegenprüfen: unveränderte Vorlage fällt durch, Musterlösung besteht (Web-Kurse: automatisch in `web-*.spec.js`).

**Vue / CSS / Tests**
- Farben nur über die Tokens in `src/style.css` (`--surface`, `--text-muted`, `--brand-text` …), nie fest eintragen; neue Farbe = Token mit Wert für hell **und** `[data-theme="dark"]`. Lila als Schrift/Rand = `--brand-text` (`--primary-purple` nur als Hintergrund). Bewusst fest: `Teaser.vue`, `FinalCertificate.vue` (Papier-Look), Sandbox-Inhalte (3.122).
- `@import` in `<style scoped>` → eigener unscoped Block; Watcher, die nach dem Rendern scrollen: `flush: 'post'`.
- Asynchrones Nachladen je Auswahl (Lektionstext) braucht einen Anfrage-Zähler: Eine spät ankommende alte Antwort darf die neue nicht überschreiben (`useLessonContent.js`, unter Last im vollen Lauf aufgefallen).
- `v-if`-Zweigwechsel mountet neu → State im Parent halten; geteilter Zustand (Admin-Token) als geteilter `ref` im Composable.
- Composable für einen Kurs verallgemeinern: Parameter mit Default = altes Verhalten, und die komplette Suite des Erstnutzers laufen lassen (3.67, so auch `WeeklyCourseTour.vue` aus der KI-Labor-Tour).
- Bildschirm hinter einen Klick legen (Start-Gate, Stufenwahl): repo-weit nach `page.goto(...)` suchen, die jetzt den Klick brauchen; Kind-Selektoren wie `.course-detail > h1` brechen bei neuen Wrappern (3.69).
- CodeMirror ist keine `<textarea>` → `tests/helpers/codemirror.js`; Notebook-Tests öffnen „Lösungen“ über `openSolutionsNotebook()` (30 s).
- Testdatei umbenannt → `package.json`-Skripte prüfen; neue Komponente/Content-Ordner → Regel in `scripts/test-changed.mjs` (leere Liste = nicht von `test:checks` abgedeckt).
- Zwei Playwright-Läufe im selben Checkout vertragen sich nicht (gleicher Port); parallel nur in Worktrees. Flaky-Suche: `test:checks -- --repeat-each=3` mit `caffeinate -i`.
- Änderungen an `kurse.json`, Profil oder Zertifikaten auch mit `npm run test:auth` prüfen (Profil-Tests laufen in keinem Hook). `test:auth` braucht Port 5174 mit Proxy (nackter Vite → 502).
- Deep-Links `?week=&tab=` bleiben stabil (`WeekTour.vue` übersetzt intern); `?week=` ohne `?stufe=` gehört bei „Meine erste Website“ zu Einfach.
- Generierte Dateien stellt `scripts/ensure-test-prereqs.mjs` vor jedem Lauf sicher.
- `test:checks` leitet `/api` an die laufende Dev-API weiter: Was im Browser etwas an die API meldet (Stolperstellen), muss bei `navigator.webdriver` schweigen und im Test gezielt eingeschaltet werden (`window.__ueTaskStatsInTests`).
- Neue npm-Abhängigkeit im Worktree: `npm install` ersetzt den `node_modules`-Symlink; nach dem Merge im Haupt-Checkout `npm install`.
- Profil-Abzeichen rechnen live; nichts beim Laden einfrieren, was der Sync später ändert. Sync darf nach Server-Apply keinen vollen Notebook-Re-Fetch auslösen (3.3).

**Accounts / Betrieb**
- Login-Formulare für Passwort-Manager: echtes `<form>` + `name`, bei reinem Passwort-Login verstecktes `username` (3.64).
- Passwörter nur als Hash: „nochmal anzeigen“ = neues Einmal-Passwort; wer `password_hash` schreibt, setzt auch `password_changed_at` (3.102).
- SQLite nur per `VACUUM INTO` sichern, nie `cp`; nie `git clean -fdx` ohne Ausschluss von `api/data/`.
- Lokale Tools (Thermodrucker, LanguageTool): Regeln in `scripts/local-tools/*/README.md`.

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

`app` hat `restart: unless-stopped`, `init: true` (tini, schneller Stop) und einen Healthcheck auf
`/api/health` (`docker compose ps` zeigt `healthy`). Startet nach Reboot nur, wenn der Docker-Daemon
selbst beim Booten startet (Linux: `systemctl enable docker`, Mac: Docker Desktop „Start at login“)
und der Container vorher nicht per `docker compose stop/down` beendet wurde. Docker startet
`unhealthy`-Container nicht selbst neu — der Healthcheck dient der Sichtbarkeit; Neustart erfolgt
nur, wenn der Node-Prozess sich beendet.

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
scripts/build_cell_notebooks.py (bei jedem dev/build), pack_notebooks.py (zippt jetzt
  _bundle/*.py statt *.ipynb)
public/kurse.json
content/python-checks/config.json, week-{N}.json, index.mjs (Node-Loader für Tests)
.env.example / .env (nie committen)
```

---

## 5. Offene Aufgaben

Stehen in `todo.md` (dort auch Betrieb und bewusst Ungeplantes). Ideen-Backlog: `PROJEKTIDEEN.md`,
Track-Modell und offene Fragen: `VISION.md`.

---

## 6. Entscheidungen / Konventionen (nicht ohne Rückfrage ändern)

Zusätzlich zu den Regeln in `CLAUDE.md` („Nicht ohne Rückfrage ändern“):

- Accounts: Admin legt an; `ageGroup` kinder|jugendliche; ein Mensch = ein Account.
- Sync: per-key Merge nach `updatedAt` beim Seiten-Reload (`restoreSession`/`syncNow`); beim
  expliziten Login (`loadAccountProgress`) ersetzt der Account-Stand den lokalen komplett – auch beim
  ersten Login mit leerem Account (geteilter Rechner, Nutzerwechsel; 3.82).
- Code-Zwischenspeicher (`useSavedCode.js`) und „Meine Seite“ sind bewusst nur lokal, nicht synchronisiert.
- Prod: ein Container `app`, Port 8080, die API liefert auch das Frontend; SQLite, Node ≥ 22 (`node:sqlite`).
- Falsch-Antwort-Erklärungen nur bei `multiple_choice`, nicht bei `multiple_select`.
- Termine nur über das Admin-Panel (`termine`-Tabelle, `/api/termine`), nicht über `public/termine.json`.
- Bewusst nicht geplant: öffentliches Sign-up, Mailversand/Kontaktformular, Supabase als Pflicht.

---

## 7. Schnellstart für Claude in der nächsten Session

1. `git checkout main && git pull`; `CLAUDE.md` ist geladen, alles andere gezielt lesen.
2. Neues Thema → eigener Worktree: `npm run worktree:new -- <branch>` (ohne Präfix).
3. Vor Änderungen an Pyodide, JS-Sandbox, Vue/CSS, Tests, Sync oder Content: den passenden Block in
   „Gelernte Regeln“ lesen. Nicht erwarten: Compose-Service `prod` (heißt `app`), `WeekSection.vue`
   (seit 3.36 `WeekTour.vue`), `.ipynb`-Quellen (seit 3.33 Zellen-Ordner), `KiLaborTour.vue` mit eigener
   Logik (seit 3.116 Wrapper um `WeeklyCourseTour.vue`).
4. Nach jedem Commit `todo.md`/`HANDOFF.md` nachziehen; nach dem Merge Details ins Archiv, hier nur eine
   Tabellenzeile plus ggf. eine Regel (`WORKFLOW.md`).
