# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-10-04
> **Aktueller Stand:** `main` enthält alles bis 3.100 (siehe Tabelle in Abschnitt 3).
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

Alles unten ist nach `main` gemergt. Für Details `grep -n "^### 3.NN" docs/archiv/HANDOFF-historie.md`.

| Nr. | Thema | Kern in einem Satz |
|---|---|---|
| 3.1–3.17 | Grundlagen: Einstufung/Checks, Admin+Sync (Express+SQLite), Debug-Notebook-Sicherheit (AST-Loop-Guard), Cäsar-Chiffre, Wochen-Zertifikate statt Punktesystem, Tippfehler-Pass | Details im Archiv |
| 3.18–3.31 | Refactorings + Curriculum-Lücken 12-Wochen-Kurs (Woche 1/3/4/5/6/7/8/11 bereinigt) | `config.json`/`week-N.json` statt `weeks.json` |
| 3.32–3.36 | Turtle-Canvas-Shim, Zellen-Format (`NN_*.py` statt `.ipynb`, CodeMirror 6), Wochen-Check-Validierung, `WeekTour.vue` statt Akkordeon | |
| 3.37–3.44 | `VISION.md`/`PROJEKTIDEEN.md`, Projekte-Übersicht `/projekte`, JS-Spielewerkstatt (iframe-Sandbox), `/profil` mit Abzeichen, JS-Grundkurs (9 Wochen) | |
| 3.46 | Woche 12: Text-Adventure-Abschlussprojekt statt Turtle | Komposition einziger neuer Begriff; List Comprehension neu in Woche 6 |
| 3.47/3.48 | Python Woche 1–4 als Einzel-Lektionen (Woche 3 nachträglich DE/EN angeglichen) (Lektions-Format) | `content/python-woche{N}-*`, Engine `pyodide` in `JsCourseTour`; Woche 3 DE/EN angeglichen; Woche 5–12 fertig; Lösungen aller Wochen aus Referenzlösungen (Glossar noch im alten Stil) |
| 3.49–3.54 | Python Woche 5–12 als Einzel-Lektionen | je Thema 7–9 Lektionen + Debug + 3 Missionen + 3–4 Extra-Herausforderungen; keine Notebook-Woche mehr; `validation.codeContains`/`validation.stdin` eingeführt |
| 3.55–3.57 | Alte Notebooks entfernt, ZIP-Download aus dem Lektions-Format; Woche 2 DE/EN angeglichen | `scripts/build_lesson_bundle.py` |
| 3.58–3.62 | Projekt-Kurse Vigenère, Snake, Text-Adventure/Fluchtraum; alle 7 Projekt-Kurse auf "selbst schreiben + Lösung auf Wunsch" | `codeTemplate` blankt nur neu eingeführte Funktionskörper; `ProjectCompletionBox.vue` |
| 3.63–3.65 | Lokales Tool Account + Thermodrucker; Login-Formulare für Passwort-Manager; Tippfehler-Pass (cspell) | `scripts/local-tools/`, nicht deployed |
| 3.66–3.68, 3.72–3.77, 3.96 | KI-Labor Woche 1–8 mit Quiz, Wochen-Zertifikat und 160 Musterlösungen | `KiLaborTour.vue`; Check-System per `courseKey` generalisiert; `task.referenceSolution` (kein Lösungs-Button), geprüft von `check_kilabor_solutions.py` |
| 3.69/3.70 | Profil zeigt Wochen-Zertifikate mit PDF-Download + "Kurs starten"-Gate | `useCourseCertificates.js`; `CourseDetail.vue` blendet Beschreibung/Struktur hinter einem Start-Button aus; Lernziele fürs PDF aus `loadWeekLernziele()` (Python) bzw. `src/data/kiLaborWeeks.js` |
| 3.71 | Woche 4 + 9: `input()`-Lücken geschlossen | `validation.stdin`-Schritt je Thema (Woche 4 Boss-3, Woche 9 Boss-1), DE+EN, ans Ende der Lektion angehängt |
| 3.78–3.81 | Prüf-Logik der Lektionen | `output_contains` tolerant, `output_equals` exakt; Lektionen prüfen nur die Ausgabe (`validateOutput()`), Struktur-Checks nur im Wochen-Check; Aufgaben nach 2 Fehlversuchen überspringbar (`.btn-skip`); 3.79 Interaktiv-Texte ausführlicher |
| 3.82 | Login ersetzt lokalen Fortschritt durch Account-Stand | `loadAccountProgress()`/`replaceLocalProgress()` (`useProgressSync.js`); Seiten-Reload merged weiter nach `updatedAt` |
| 3.83 | Pre-commit/Pre-push zweistufig statt vollem `test:checks` bei jedem Commit | `scripts/test-changed.mjs` mappt staged Dateien auf betroffene Specs (Pre-commit); voller `test:checks` im Pre-push-Hook |
| 3.84 | Termine im Admin-Panel statt `public/termine.json` | `termine`-Tabelle + `/api/termine` + `/api/admin/termine`, Tab „Termine“ in `AdminView.vue`; einmaliger Umzug per `import-termine-json.js` |
| 3.85 | Interaktiv-Kurs: Editor-Erklärungen, flexible Lektionen + Beispiel-Aufgabe | `lesson.editorHint`, Hinweis für `___`-Lücken; `lesson.minSolved` in `LessonView.vue` macht eine Lektion "flexibel" (5 Aufgaben, mind. 2 nötig, Rest sofort überspringbar) |
| 3.86/3.93 | "Kurs starten"-Gate für Projekt- und Interaktiv-Kurs; Lektionsliste als Leiste | `isFocusableCourse` gilt für alle Kurse außer der Einstufung, `?started=1` hält die Ansicht beim Reload; `course-layout.css` einspaltig; Interaktiv-Kurs: Varianten-Kacheln, "Weiter" scrollt nach oben |
| 3.87 | Git-Worktree-Tooling | `npm run worktree:new`/`worktree:remove`, eigene Ports je Worktree (`worktree.ports.json`), siehe `WORKFLOW.md` |
| 3.89/3.97 | Dev-Modus "Prüfungen überspringen" (zentral, alle Kurse) | `npm run dev:skip-checks` → `devSkipChecks.js` (nur mit `import.meta.env.DEV`): Prüfungen/Quiz immer bestanden, alle Lektionen offen, Banner; Suite `test:devskip` im Pre-push |
| 3.88/3.90 | JS-Spielewerkstatt mit neuem Konzept | 7 Lektionen am laufenden Spiel (ID/URL gleich), Prüfung per `output_equals`, `task.showCanvas: false`, Durchlauf-Test über alle Musterlösungen |
| 3.91 | "Zurücksetzen"-Button für vorgegebenen Code | `.btn-reset` in `LessonView.vue`/`JsLessonView.vue`/`CodeChallenge.vue`, sichtbar sobald der Code vom `codeTemplate` abweicht; setzt nur diese eine Aufgabe zurück |
| 3.92 | JS-Lektionsaufgaben: fehlende `output_contains`-Checks nachgezogen | `js-grundkurs` und `js-snake`: keine JS-Pflichtaufgabe mehr ohne Ausgabe-/Canvas-/DOM-Prüfung (vorher 31, seit 3.80 ungeprüft) |
| 3.94 | Glossar-Tooltip bei verschachtelten Begriffen | `useLessonContent.js`: ein kombinierter Regex-Durchlauf statt sequenziellem Ersetzen |
| 3.95 | Offline-Downloads in 3 Formaten (Notebooks, eine `.py`, Einzeldateien je Lektion) | 12 Wochen, Python-Projekte, KI-Labor; `OfflineDownloads.vue`, `pack_notebooks.py`, Details `INHALTE.md` |
| 3.98 | Rechtschreib- und Verständnisprüfung aller deutschen Inhalte | cspell deckt allen Content ab, neu `lint:spelling:de` (LanguageTool in Docker); alle Kurse gelesen und korrigiert, Themen-Reste in Pferde/Sci-Fi und englische Bezeichner in Woche 12 (DE) bereinigt, Wochen-Check-Fragen zu nicht gelehrtem Stoff ersetzt |
| 3.99 | Fortschritts-Vertrag: Deploy darf gespeicherten Fortschritt nicht brechen | `tests/progress-contract.spec.js` + `tests/fixtures/progress-contract.json` (IDs, Check-Positionen, Storage-Keys/-Versionen, DB-Spalten), `npm run contract:update`, Regeln in `WORKFLOW.md` |
| 3.100 | Themen angeglichen (12-Wochen-Kurs Woche 2–4) + Lösungs-Reihenfolge | gleiche Lektionen/Konzepte in Abenteuer/Pferde/Sci-Fi; neue Lektionen mit neuer ID an passender Stelle; `scripts/sync_loesungen.py` (Woche 9 war im Download verschoben) |
| 3.101 | micro:bit-Kurs „Das Roboterauto“ (`projekt-microbit-auto`) | erster Hardware-Kurs: `engine: "anleitung"` → `GuideLessonView.vue` (Aufgaben zum Abhaken statt Prüfung, Umschalter Blöcke/Python über `:::bloecke`/`:::python`, MakeCode-Blöcke als ```` ```bloecke ````-Text); 11 Stufen in `content/microbit-auto/`; seit 14.10. in `/projekte` verlinkt (das Feld `"unlisted": true` gibt es weiter für künftige Kurse); ein zurückgenommener Pflicht-Haken nimmt den Abschluss der Stufe zurück (`unmarkCompleted`); Details in `INHALTE.md` Abschnitt 6 |
| 3.102 | Eigenes Passwort ändern + Reset per Einmal-Passwort | `POST /api/password` (liefert frisches Token), `POST /api/admin/users/:id/reset-password` (Einmal-Passwort, `must_change_password`), Zwangswechsel im Einstellungs-Modal (`App.vue`), `requireUser` lehnt Tokens mit `iat` vor `password_changed_at` ab; Druck: `drucker.py account <name>` |

### Gelernte Regeln (wiederverwendbare Fallstricke)

**Content / Notebooks**
- Bulk-Edits an JSON/Notebooks nie per volle Reserialisierung, sondern gezielte Text-Ersetzung + `json.loads()` danach (3.12, 3.16). Seit 3.33 sind 12-Wochen-Notebooks Zellen-Ordner (`NN_*.py`) — keine `.ipynb` als Quelle wieder einführen.
- Debug-Bugs müssen vom Kernel-Zustand unabhängig sein und dürfen die Lösung nicht verraten. Nach Notebook-Änderung Code-Zellen mit gemeinsamem Namespace per `python3` ausführen.
- Ein "Fund" aus einer Variante gilt nicht automatisch für alle: vor Massenänderungen alle 3 Varianten × DE/EN grep-prüfen.
- Lektions-IDs (`lektion-NN`) sind der Fortschritts-Schlüssel — neue Lektionen nur mit neuer ID anhängen, bestehende nie umnummerieren; Reihenfolge = Position in `lessons.json`, nicht die ID (3.100).
- Neue Prüf-Logik immer über `useTaskValidation.js` (bzw. `isLessonUnlocked`) laufen lassen — nur dann
  greift der Dev-Modus `dev:skip-checks` automatisch auch im neuen Kurs (3.97).
- `codeTemplate` einer echten Debug-Aufgabe ist absichtlich kaputt — Generatoren kompilieren nur
  Beispiel-Code und Lösungen, nie rohe Aufgaben-Vorlagen (3.95).
- Neue Aufgabe im Lektions-Format: Lösung als Markdown+Code-Zell-Paar mit der **höchsten** Nummer
  im `_6_loesungen`-Ordner anlegen (Markdown enthält den Aufgabentext), danach
  `python3 scripts/sync_loesungen.py` — das sortiert die Paare in Aufgaben-Reihenfolge. Nötig, weil
  der Offline-Download Lösungen nur über die Reihenfolge zuordnet (Woche 9 war deshalb verschoben).
- Standard-PDF-Fonts (pdf-lib/Helvetica) können kein Emoji — Content-Texte vorher per `sanitizeForPdfFont` filtern (3.13).
- Punkte-/Item-System und lokales Fortschritt-Skript **nicht** wieder einführen; Zertifikat = nur Wochen-Check, ein Zertifikat pro Woche, PDF login-gated (3.12/3.13).
- Quizfragen `multiple_choice`: `optionExplanations` mitpflegen, `explanation_en` echt übersetzen; `shuffleQuestionOptions()` muss Text+Erklärung als Paar mischen (3.17). Schwelle nie als exakten Bruch (2/3 → `0.66`, 3.6).
- Projekt-Kurse: der Erklärtext einer Lektion darf die direkt folgende Aufgabe nicht vorwegnehmen — weder als lauffähiger Code (Pseudocode nutzen, siehe 3.61), noch als "Beispiel"-Aufgabe, die exakt dieselbe Funktion wie die nächste "Pflicht"-Aufgabe zeigt (Beispiel muss eine *andere* Instanz desselben Prinzips sein, wie `verdopple` vor `bewegeSchlaeger` in js-spielewerkstatt).

**Pyodide / Ausführung**
- Kein Web Worker: `input()` läuft synchron über `window.prompt()` (65 Notebooks, 3.5). Loop-Guard ist AST-basiert.
- `turtle` gibt es in Pyodide nicht — eigener Canvas-Shim in `usePyodide.js` (3.32).
- Kernel in Tests immer über `startKernel()` starten, nie `if (await btn.isEnabled()) click()` — der
  Button kann dazwischen deaktiviert werden, `click()` hängt dann bis zum Timeout (flaky Tests).
- **Kernel-Button nach Lektionswechsel:** `click({ force: true })` scheitert sporadisch mit „Element is
  outside of the viewport“, weil die Scroll-Animation den Button verschiebt → `dispatchEvent('click')`
  nehmen (so in `tests/helpers/kernel.js` und allen lokalen `initKernel`/`startKernel`).
- **Nach „Weiter“ erst auf die neue Lektion warten** (`waitForFreshLesson()` aus
  `tests/helpers/kernel.js`): Die Seite zeigt kurz noch die alte Lektion, sofortiges Tippen landet in
  deren Editor und ist nach dem Wechsel weg.
- **Zwei Playwright-Läufe im selben Checkout vertragen sich nicht** (z.B. Pre-push-Hook parallel zu
  einem manuellen Lauf): beide wollen Vite auf dem Test-Port. Seit `reuseExistingServer: false` bricht
  der zweite sofort mit „already used“ ab; vorher lieh er sich den Server und lief in
  `ERR_CONNECTION_REFUSED`, sobald der erste fertig war. Parallel testen nur in einem Worktree.
- **Flaky-Suche:** `npm run test:checks -- --repeat-each=3` (bzw. `test:auth`), mit `caffeinate -i`
  davor, damit der Mac nicht einschläft. Schläft er mitten im Lauf, fallen Tests mit Laufzeiten von
  mehreren Minuten aus.
- **Änderungen an `public/kurse.json` auch mit `npm run test:auth` prüfen:** Die Profil-Tests
  (`tests/auth-ui.spec.js`) hängen an der Kursliste, laufen aber weder im Pre-commit- noch im
  Pre-push-Hook.
- Profil-Abzeichen (`useProjectBadges`) rechnen live aus dem Fortschritt. Nichts beim Laden einfrieren,
  was der Sync später ändert: Der Account-Stand kommt nach Login/Neuladen erst nach dem ersten Rendern.
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
- cspell taugt für Deutsch nur als grobes Netz (lässt beliebige Wortzusammensetzungen und
  `strasse`/`wiederspiegeln` durch). Für deutschen Content zusätzlich `npm run lint:spelling:de`
  (LanguageTool; Docker-VM mit 2 GB verträgt nur einen Request gleichzeitig und max. ~1,1 GB Heap).
  Kleingeschriebene Bezeichner gehören nicht in `cspell.json`, Code-Felder ignoriert es per
  `ignoreRegExpList` (3.98).
- Aufgabentext im Lektions-Format ändern heißt: `lessons.json` **und** die Lösungs-Markdown-Zelle
  (`…_6_loesungen`, Test vergleicht den Text exakt); geänderter Ausgabetext zusätzlich in `expected`,
  Vorlage und Lösungs-Code. Danach jede Lösung per `python3` gegen `expected` laufen lassen (3.98).
- Wochen-Check-Fragen und Lernziele (`woche{N}.md`, gehen aufs Zertifikat-PDF) nur zu Stoff, der in
  genau dieser Woche gelehrt wird — beim Verschieben von Stoff zwischen Wochen mitprüfen (3.98).
- Fortschritt hängt an Ordnernamen, Lektions-/Fragen-IDs und der Position der Coding-Aufgaben, nicht an
  Texten: Aufgaben inhaltlich ersetzen ist ok, umbenennen/umsortieren/löschen nicht (`WORKFLOW.md`,
  Test `progress-contract.spec.js`, 3.99). Neue DB-Spalten brauchen `ALTER TABLE` in `db.js`.
- Dateien in Skripten nie als `open(f, 'w').write(...open(f).read()...)` umschreiben — das `'w'`
  leert die Datei, bevor gelesen wird. Erst lesen, dann schreiben (3.98).
- Komponente wird beim Umschalten eines `v-if`-Zweigs neu gemountet → lokaler State geht verloren,
  wenn er nicht vom Parent gehalten wird; beim Neu-Mount auf sinnvollen Zustand zurückfallen (3.55).
- Login-Felder für Passwort-Manager-Autofill brauchen ein echtes `<form>` + `name`-Attribute; bei
  reinem Passwort-Login (kein Benutzername im Modell, z.B. Admin) ein verstecktes `username`-Feld
  mit festem Wert ergänzen (3.64).
- Passwörter liegen nur als Hash vor — „nochmal anzeigen/drucken“ heißt immer: neues Einmal-Passwort
  über `reset-password` erzeugen. Jede Stelle, die `password_hash` schreibt, muss auch
  `password_changed_at` setzen, sonst bleiben alte Sitzungen gültig (3.102).
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
- Thermodrucker-Tool liegt in `scripts/local-tools/drucker/`: Nur `drucker.py` (Einstieg) fragt und
  gibt aus; `druck.py`/`ausweis.py`/`tabelle.py`/`bluetooth.py` liefern Werte und werfen
  `DruckerError`. Neue Aktion = Funktion im passenden Modul + Menüpunkt/Unterbefehl in `drucker.py`.
- `drucker.py` kennt ein Menü (ohne Argumente) und Unterbefehle
  `account`/`ausdrucke`/`tabelle`/`scan`); `drucker_gui.py` ist dasselbe als Fenster (tkinter, auf
  macOS `brew install python-tk@<version>`). Im Fenster läuft alles Langsame über `run_async()` in
  einem Thread — nie Tk-Widgets aus dem Thread anfassen, Ergebnisse kommen über die Queue zurück.
- `drucker.py account <name>` legt an oder setzt bei vorhandenem Account auf Rückfrage das Passwort
  zurück (`POST /api/admin/users/:id/reset-password`, Einmal-Passwort mit Zwangswechsel). Jeder Ausdruck landet als PNG in `ausdrucke/` (gitignored,
  Klartext-Passwörter) und lässt sich daraus erneut drucken.
- `drucker.py tabelle` liest die Forscher-Tabelle aus micro:bit-Stufe 8 aus `lektion-09.md`: Wer
  die Tabelle dort ändert, prüft den Ausdruck mit `--no-print` (Bild in `ausdrucke/`).
- Ohne Drucker testen: `--no-print` statt Druck; Account-Anlage gegen `node scripts/run-test-api.js`
  mit `--server-url http://localhost:<port>` (Admin-Passwort `test-admin-password`), nie gegen Produktion.

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
2. `CLAUDE.md` ist automatisch geladen; bei Content-Arbeit `INHALTE.md`/`todo.md`, sonst nur den passenden Abschnitt hier
3. Neues Thema → **neuen** Branch (ohne Präfix), immer im eigenen Worktree: `npm run worktree:new -- <branch>`
4. Vor Änderungen an Pyodide, JS-Sandbox, Vue-CSS, Sync oder Notebooks: Abschnitt 3 "Gelernte Regeln" lesen.
   Nicht erwarten: Compose-Service `prod` (heißt `app`), `WeekSection.vue`-Akkordeon (seit 3.36 `WeekTour.vue`),
   `.ipynb`-Quellen im 12-Wochen-Kurs (seit 3.33 Zellen-Ordner).
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`. Nach dem Merge den Feature-Abschnitt
   ins Archiv (`docs/archiv/HANDOFF-historie.md`) verschieben und hier nur eine Zeile in der Tabelle in Abschnitt 3
   plus ggf. eine "Gelernte Regel" behalten (siehe `WORKFLOW.md`).
