# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-25
> **Aktueller Stand:** Branch `kurs-ki-labor` (noch nicht gemergt): Kursplan für das neue KI-Labor
> auf selbstgebaute Algorithmen statt scikit-learn umgestellt, Grundgerüst (Wochenauswahl,
> `kurse.json`, Routing) + Woche 1 "Was ist KI?" fertig und getestet (3.66); Quiz+Zertifikat +
> Extra-Herausforderung (3 Boss-Lektionen) auf Nutzerwunsch nachgezogen (3.67) — das bislang
> python-only Check-System dafür kurs-fähig gemacht (`useWeekChecks.js`/`WeekCheckPanel.vue`/
> `CodeChallenge.vue`/`useCertificatePdf.js` um `courseKey` erweitert). Wochen 2–8 offen, nächste
> Session macht hier weiter. Vorheriger Stand:
> Backup-Cron-Pfad in HANDOFF korrigiert + Docker-Prod-Build lokal verifiziert, Tippfehler-Pass
> (cspell) auf Lektions-Format/JS-Grundkurs/Interaktiv-/Projekt-Kurse ausgeweitet (3.65).
> Server-Deploy steht weiter aus (Nutzer deployt selbst, siehe Abschnitt 4 "Betrieb").
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
| 3.47/3.48 | Python Woche 1–4 als Einzel-Lektionen (Woche 3 nachträglich DE/EN angeglichen) (Lektions-Format) | `content/python-woche{N}-*`, Engine `pyodide` in `JsCourseTour`; Woche 3 DE/EN angeglichen; Woche 5–12 fertig; Lösungen aller Wochen aus Referenzlösungen (Glossar noch im alten Stil) |
| 3.49 | Python Woche 5 (Funktionen) als Einzel-Lektionen | 7 Lektionen + Debug (3 Bugs) + 3 Missionen + 3 Extra-Herausforderungen je Thema, DE = EN; Generator im Scratchpad (nicht im Repo), jede Aufgabe mit `python3` geprüft; Vorgriffe (Listen/Dict/`random`) ersetzt, siehe `todo.md` |
| 3.50 | Python Woche 6 (Listen) als Einzel-Lektionen | 9 Lektionen + Debug (3 Bugs) + 3 Missionen + 4 Extra-Herausforderungen (4 = Wiederholung mit den vollen Mengen aus Woche 2/4) je Thema, DE = EN; aus einem Skelett + Themen-Vokabular erzeugt (Scratchpad), jede Aufgabe mit `python3` geprüft; nimmt die Woche-4/5-Vorgriffe (Listen, `break`/`continue`) auf, Dictionaries/`random` bleiben für Woche 7/8 |
| 3.51 | Python Woche 7 (Module) als Einzel-Lektionen | 7 Lektionen + Debug + 3 Missionen + 4 Extra-Herausforderungen je Thema, DE = EN; Zufall wird über Eigenschaften geprüft (30 Testläufe im Generator), `%`/`//`/`random`/Feld-Vorgriffe aus Woche 4/5 in Extra-Herausforderung 4 nachgezogen |
| 3.52 | Python Woche 8 (Dictionaries/Tupel) als Einzel-Lektionen | 7 Lektionen (Dictionary, ändern, `get`/`in`, Durchlaufen, Tupel, `try/except`, verschachtelt) + Debug (3 Bugs) + 3 Missionen + 4 Extra-Herausforderungen je Thema, DE = EN; Extra 4 zieht die Vorgriffe aus Woche 5–7 nach (`erstelle_*`-Funktion, Quest-Dictionary, Zählen mit `get`, `random.choice` auf Schlüsseln, `try/except KeyError`); Generator im Scratchpad, jede Referenzlösung mit `python3` ausgeführt |
| 3.53 | Python Woche 9 (JSON und Dateien) als Einzel-Lektionen | 7 Lektionen (`open`/`with`, zeilenweise + `"a"`, `FileNotFoundError`/`os`, `json.dumps`/`loads`, `json.dump`/`load`, `csv.writer`/`reader`, `DictReader`/`DictWriter` + JSON↔CSV) + Debug (3 Bugs) + 3 Missionen + 4 Extra-Herausforderungen je Thema, DE = EN; jede Aufgabe legt ihre Dateien selbst an (Pyodide-Dateisystem bleibt zwischen Aufgaben bestehen); Extra 4 nimmt Funktionen/Listen/`random`/Dictionaries aus Woche 5–8 auf; alle 630 Referenzlösungen von Woche 8+9 zusätzlich in Pyodide (node_modules) ausgeführt |
| 3.54 | Python Woche 10–12 (OOP Grundlagen, OOP Fortgeschritten, Text-Adventure) als Einzel-Lektionen | je Woche 7 Lektionen/Etappen + Debug + 3 Missionen + 4 Extra-Herausforderungen, DE = EN; damit gibt es keine Notebook-Woche mehr in der Tour; `validation.codeContains`/`validation.stdin` eingeführt (3.54b); alle Lösungen Woche 1–12 (2.972 Aufgaben) aus Referenzlösungen neu erzeugt |
| 3.55 | Alte Notebooks entfernt, ZIP-Download neu aus dem Lektions-Format | `scripts/build_lesson_bundle.py` baut Download direkt aus dem Lektions-Format, DE+EN |
| 3.56 | Woche 2: Abenteuer + Pferde DE/EN angeglichen | größere Fassung als Referenz (wie Woche 3/4) |
| 3.57 | Woche 2: Sci-Fi DE/EN angeglichen | ausnahmsweise umgekehrt: EN war größer (7 Lektionen/46 Aufgaben), DE an EN angeglichen; 39 Referenzlösungen einzeln mit `python3` geprüft, `woche2_scifi_6_loesungen` neu erzeugt |
| 3.58 | Projekt-Kurs Vigenère-Chiffre (Nachfolger Cäsar-Chiffre) | `content/vigenere-chiffre` (5 Lektionen, DE-first), `kurse.json`-Eintrag `projekt-vigenere-chiffre` (Level `fortgeschritten`, Tags `kryptografie`/`knobelaufgabe`); alle Referenzlösungen mit `python3` geprüft; `tests/projekte.spec.js` um eigenen Funktions-Test erweitert, bestehende Karten-/Filter-Tests auf 5 Projekte angepasst (Fortgeschritten/Kryptografie treffen jetzt je 2 statt 1 Projekt) |
| 3.59 | Projekt-Kurs Snake (Nachfolger JS-Spielewerkstatt, JS-Sandbox/Canvas) | `content/js-snake` (6 Lektionen, DE-first): Raster→Segment-Array→Steuerung/Bewegung→Animationsloop→Selbst-/Randkollision→eigenes Spiel; `kurse.json`-Eintrag `projekt-js-snake` (`engine: js-sandbox`, Level `fortgeschritten`, Tags `spiele`/`logikraetsel`); alle Pure-Funktionen (inkl. Objekt-Rückgabewerte wie `naechsterKopf`) mit `node` geprüft, `functionCalls`-Validierung nie mit Array als `expected` (nur `===`-Vergleich, siehe HANDOFF-Fallstricke); `tests/projekte.spec.js` um eigenen Funktions-Test erweitert, Karten-/Filter-Tests auf 6 Projekte angepasst (Fortgeschritten trifft jetzt 3, JavaScript-Filter 2 Projekte) |
| 3.60 | Projekt-Kurs Text-Adventure/Fluchtraum | `content/text-adventure-fluchtraum` (6 Lektionen, DE-first, Pyodide): Raum als Dictionary → mehrere Räume verknüpft → Inventar als Liste → verschlossene Tür (Dictionary-Lookup + `in`-Prüfung kombiniert) → Befehle per `input()`/`split()` → Kapitel 6 verbindet alles in einer `while`-Schleife (Sieg = Flur erreicht, ohne Schlüssel läuft die Schleife endlos = zweites Ende); `kurse.json`-Eintrag `projekt-text-adventure` (Level `fortgeschritten`, Tags `spiele`/`logikraetsel`); alle 11 Referenzlösungen (inkl. `stdin`-Befehlsfolgen) mit `python3` geprüft, `validation.variables`/`functionCalls` bewusst **nicht** genutzt (in `LessonView.vue` wird `validateOutput` ohne den `variables`/`functionResults`-Parameter aufgerufen — diese Felder würden dort niemals bestehen, siehe HANDOFF-Fallstricke); `tests/projekte.spec.js` um eigenen Lektions-Test erweitert, Karten-/Filter-Tests auf 7 Projekte angepasst (Fortgeschritten trifft jetzt 4) |
| 3.61 | Alle 7 Projekt-Kurse auf "selbst schreiben + Lösung auf Wunsch" umgestellt | `codeTemplate` blankt nur neu eingeführte Funktionskörper, neuer "Lösung anzeigen"-Button; Snake-Beispielaufgabe/JS-Spielewerkstatt-Erklärtext entschärft (nahmen die folgende Aufgabe vorweg); jede Aufgabe hat jetzt ein `solution`-Feld; Regel dazu unten unter "Gelernte Regeln" |
| 3.62 | Projekt-Abschluss zeigt Abzeichen-Hinweis + Link zu /projekte | Neue Komponente `ProjectCompletionBox.vue`, ersetzt bei der letzten Projekt-Lektion den generischen "Weiter"-Button |
| 3.63 | Lokales Tool: Account anlegen + Thermodrucker-Ausdruck | `scripts/local-tools/create-account-printout.py`, nicht deployed, legt Account über Admin-API an und druckt Ausweis-Beleg auf MXW01-Drucker; macOS braucht CoreBluetooth-UUID statt MAC + Write-Pacing-Patch (`patch-mxw01.py`), mit echtem Drucker getestet |
| 3.64 | Login-Formulare für Passwort-Manager + Admin-Nav-Link nur bei Login | Admin-/Account-Login jetzt echte `<form>`s mit `name`-Attributen (1Password-Autofill); "Admin"-Nav-Link nur sichtbar bei aktivem Admin-Token |
| 3.65 | Tippfehler-Pass (cspell) auf Lektions-Format/JS-Grundkurs/Interaktiv-/Projekt-Kurse | `lint:spelling`-Scope um `content/python-woche*`, `content/js-grundkurs*`, `content/python-grundlagen-interaktiv*` und alle 7 Projekt-Kurse erweitert; 0 echte Tippfehler in 1306 Dateien (verdächtige Kandidaten wie `cilck` waren ein absichtlicher Debug-Bug, `mcvbg`/`rejvs` Chiffretext-Beispiele, `gibtsnicht.json` ein Test-Dateiname, `n`-präfigierte Wörter JSON-`\n`-Escape-Artefakte); 280 legitime Wörter (deutsche Kleinschreibungs-Substantive, Figuren-/Ortsnamen) in `cspell.json` ergänzt |
| 3.66 🚧 | KI-Labor gestartet (Branch `kurs-ki-labor`, noch nicht gemergt) — Kursplan + Woche 1 | Kursplan (`KURSPLAN.md`/`VISION.md`/`todo.md`/`PROJEKTIDEEN.md`) auf selbstgebaute Algorithmen statt scikit-learn umgestellt (Wasm-Download zu schwer, kein Live-LLM wegen API-Kosten/WebGPU), 8 Wochen ohne Themen-Varianten; Aufbau wie `js-grundkurs`, aber im Lektions-Format des 12-Wochen-Kurses (Lektion→Debug→Mission, `output_contains`/`codeContains`, keine `variables`/`functionCalls` — LessonView.vue unterstützt die nicht) statt JS-Sandbox-Format; neue Komponente `KiLaborTour.vue` (Kopie von `JsGrundkursTour.vue`, `engine="pyodide"` in `JsCourseTour`), `isKiLabor`-Sonderfall in `CourseDetail.vue`, `kurse.json`-Eintrag, `content/ki-labor` (Beschreibung) + `content/ki-labor-woche1` (5 Lektionen "Was ist KI?" + Debug + Mission, alle Referenzlösungen mit `python3` geprüft); `jsGrundkurs.*`-t()-Keys zu `weekPicker.*` umbenannt (jetzt von beiden Kursen geteilt); `tests/ki-labor.spec.js` neu, `tests/site.spec.js` Kurskarten-Zahl 3→4; Wochen 2–8 offen, siehe `todo.md` |
| 3.67 🚧 | KI-Labor: Quiz + Wochen-Zertifikat nachgezogen (Branch `kurs-ki-labor`) | Nutzerwunsch nach 3.66: Wochen-Check+Zertifikat wie im 12-Wochen-Kurs, nicht nur Lektion/Debug/Mission. Das bis dahin fest auf den Python-Kurs verdrahtete System (`content/python-checks/`, Storage-Key `ue-hacker-week-checks` ohne Kurs-Bezug) um einen `courseKey`-Parameter generalisiert (Default `'python'` = unverändertes Verhalten, keine Migration): `useWeekChecks.js` (Content-Glob `content/*-checks/`, Storage-Key `ue-hacker-week-checks-<courseKey>`, Fortschritts-Refs jetzt eine `Map` pro `courseKey` statt ein Singleton-Ref), `WeekCheckPanel.vue`/`CodeChallenge.vue` (neue `courseKey`-Prop durchgereicht), `useCertificatePdf.js` (neuer `courseTitle`-Parameter statt hart codiertem "Python 12-Wochen-Grundkurs"); `useProgressSync.js` von fixem `'ue-hacker-week-checks'`-Key auf Präfix-Match umgestellt, damit der neue Kurs-Key mitsynct. `KiLaborTour.vue` bekam einen dritten Zustand (`phase: 'check'`) mit eigenem Zertifikat-Reveal (Kopie der Logik aus `WeekTourStepper.vue`, aber ohne dessen Themen-Varianten-/Notebook-Komplexität) statt Wiederverwendung von `WeekTourStepper.vue` selbst (das zeigt immer einen Themen-Breadcrumb, den es hier nicht geben soll). Neuer Content-Ordner `content/ki-labor-checks/` (`config.json`, `week-1.json` mit 7 Quizfragen + 2 Coding-Aufgaben, `index.mjs`-Node-Loader wie bei `python-checks`), alle Coding-Referenzlösungen mit `python3` geprüft. Zusätzlich (auf Nachfrage "hat Woche 1 auch Hausaufgaben?") 3 Extra-Herausforderungen (`boss-01..03`, Abschnitt `boss`) nach der Mission ergänzt — löst zusammen mit `hasCheck` automatisch die Wahl-Seite aus `JsCourseTour.vue` aus (Extra-Herausforderung optional vs. direkt zum Check). `tests/ki-labor.spec.js` um Check-Flow und Boss-Wahl-Seite erweitert (36 bestehende Python-Check-Tests liefen unverändert grün); `lint:spelling`-Scope um `content/ki-labor*` erweitert. |

### Gelernte Regeln (wiederverwendbare Fallstricke)

**Content / Notebooks**
- Bulk-Edits an JSON/Notebooks nie per volle Reserialisierung, sondern gezielte Text-Ersetzung + `json.loads()` danach (3.12, 3.16). Seit 3.33 sind 12-Wochen-Notebooks Zellen-Ordner (`NN_*.py`) — keine `.ipynb` als Quelle wieder einführen.
- Debug-Bugs müssen vom Kernel-Zustand unabhängig sein und dürfen die Lösung nicht verraten (3.4). Nach Notebook-Änderung Code-Zellen mit gemeinsamem Namespace per `python3` ausführen.
- Ein "Fund" aus einer Variante gilt nicht automatisch für alle: vor Massenänderungen alle 3 Varianten × DE/EN per grep prüfen (3.26–3.30).
- Standard-PDF-Fonts (pdf-lib/Helvetica) können kein Emoji — Content-Texte vorher per `sanitizeForPdfFont` filtern (3.13).
- Punkte-/Item-System und lokales Fortschritt-Skript **nicht** wieder einführen; Zertifikat = nur Wochen-Check, ein Zertifikat pro Woche, PDF login-gated (3.12/3.13).
- Quizfragen `multiple_choice`: `optionExplanations` mitpflegen, `explanation_en` echt übersetzen; `shuffleQuestionOptions()` muss Text+Erklärung als Paar mischen (3.17). Schwelle nie als exakten Bruch (2/3 → `0.66`, 3.6).
- Projekt-Kurse: der Erklärtext einer Lektion darf die direkt folgende Aufgabe nicht vorwegnehmen — weder als lauffähiger Code (Pseudocode nutzen, siehe 3.61), noch als "Beispiel"-Aufgabe, die exakt dieselbe Funktion wie die nächste "Pflicht"-Aufgabe zeigt (Beispiel muss eine *andere* Instanz desselben Prinzips sein, wie `verdopple` vor `bewegeSchlaeger` in js-spielewerkstatt).

**Pyodide / Ausführung**
- Kein Web Worker: `input()` läuft synchron über `window.prompt()` (65 Notebooks, 3.5). Loop-Guard ist AST-basiert.
- `turtle` gibt es in Pyodide nicht — eigener Canvas-Shim in `usePyodide.js` (3.32).
- Kernel in Tests immer über `startKernel()` (`tests/helpers/kernel.js`) starten, nie `if (await btn.isEnabled()) click()` — der Kernel kann dazwischen bereit werden, der Button ist dann deaktiviert und `click()` hängt bis zum Test-Timeout (flaky `zertifikate`/`woche12`).
- `CodeChallenge` startet den Kernel nicht selbst; Tests klicken `.btn-kernel` explizit (3.47-Lektion, `ensureKernel` in `zertifikate.spec.js`).
- Namespace-Variablen vor jedem Check-Lauf löschen; `pyodide.globals.delete()` wirft bei unbekanntem Namen → try/catch (3.34). Vor `functionCalls`-Re-Aufruf `__cell_deadline__` neu setzen (3.34).
- `validation.variables`/`validation.functionCalls` in `lessons.json` **nie** für Python-Inhalte nutzen, die über `LessonView.vue` laufen (12-Wochen-Kurs, Python-Projekt-Kurse): `LessonView.vue` ruft `validateOutput()` ohne die Parameter `variables`/`functionResults` auf (nur `CodeChallenge.vue`/`JsLessonView.vue` für den JS-Grundkurs tun das) — ein `validation.variables`-Feld würde dort jede Aufgabe permanent durchfallen lassen. Für Python-Projekt-Kurse stattdessen `output_contains` (mehrzeilig über `\n`) + `codeContains` nutzen (3.60).

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
- Seit Woche 12 im Lektions-Format ist kein Kurs-Schritt mehr ein Notebook: Tests, die `.cell`/`.btn-run-cell`/`.btn-run-all` brauchen, öffnen das Nachschlagewerk „Lösungen“ über `openSolutionsNotebook()` (`tests/helpers/notebook.js`); 15 s reichen dort unter Last nicht (30 s).
- CodeMirror ist keine `<textarea>`: Tests nutzen `tests/helpers/codemirror.js` (`setCodeMirrorContent`, `hoverOverCodeMirrorText`).
- Beim Umbenennen von Testdateien `package.json`-Skripte mitprüfen — Playwright ignoriert fehlende Dateien stillschweigend, nur der Test-Zähler sinkt (3.43).
- `test:auth` nutzt Port 5174 mit Proxy-Header; läuft dort schon ein "nackter" Vite, kommen 502er → `lsof -nP -iTCP:5174 -sTCP:LISTEN` (3.36).
- Neue `LessonView.vue`-Kurse: Glob-Listen sind seit 3.38 Wildcards — nur Content-Ordner + `kurse.json` nötig.
- Deep-Links `?week=&tab=` (Einstufung, Cäsar-Chiffre) bewusst unverändert lassen, `WeekTour.vue` übersetzt intern (3.36).
- cspell: Wörterbücher brauchen `"import"`, nicht nur `"dictionaries"`; Ausgabe muss im Repo liegen (3.8/3.9).
- Komponente wird beim Umschalten eines `v-if`-Zweigs neu gemountet → lokaler State (z.B. aktuelle Lektion) geht verloren, wenn er nicht vom Parent gehalten wird; beim Neu-Mount auf den zuletzt sinnvollen Zustand zurückfallen, nicht immer auf den Anfang (3.55).
- Login-Felder für Passwort-Manager-Autofill (1Password u.ä.) brauchen ein echtes `<form>` +
  `name`-Attribute auf den Inputs, sonst werden sie oft nicht erkannt/gespeichert; bei reinem
  Passwort-Login (kein Benutzername im Datenmodell, z.B. Admin) ein verstecktes `username`-Feld mit
  festem Wert ergänzen, damit ein vollständiges Login-Paar entsteht (3.64).
- Reaktiver Zustand, der über mehrere Komponenten synchron bleiben muss (z.B. Admin-Token für
  Nav + AdminView), gehört als ein geteilter `ref` in die Composable — nicht als lokaler Ref pro
  Komponente, der bei jeder Aktion manuell nachgezogen wird (3.64).
- Ein Composable/System, das nur für **einen** Kurs gebaut wurde (Content-Pfad + Storage-Key ohne
  Kurs-Bezug fest verdrahtet, z.B. `useWeekChecks.js` vor 3.67), lässt sich nicht einfach an eine
  zweite Stelle durchreichen — der Fortschritt beider Kurse würde sich sonst denselben
  `localStorage`-Key und Content-Ordner teilen. Beim Verallgemeinern: ein `courseKey`-Parameter mit
  Default = bisherigem Verhalten (keine Migration bestehender Nutzerdaten nötig), Storage-Key/
  Content-Glob-Pfad davon ableiten, und **immer** die komplette bestehende Test-Suite des
  Erstnutzers (hier: alle `zertifikate.spec.js`/`week-checks*.spec.js`-Tests) gegenlaufen lassen,
  nicht nur den neuen Kurs testen (3.67).

**Lokale Tools (`scripts/local-tools/`, laufen nie im Deploy)**
- IDN-Domains (Umlaute, z.B. `übergangshacker.de`) vor jedem `urllib`-Request per `.encode('idna')`
  in Punycode wandeln — sonst schickt Python den Host-Header unkodiert, der Server/Reverse-Proxy
  kappt die Verbindung ohne jede Fehlermeldung (`RemoteDisconnected`) (3.63).
- macOS/Homebrew-Python verweigert systemweite `pip install`s (PEP 668) → lokale Tools brauchen ein
  eigenes `venv/`. Um automatisch dorthin zu wechseln (egal mit welchem `python3` aufgerufen): über
  `sys.prefix` prüfen, **nicht** `Path(sys.executable).resolve()` — `venv/bin/python3` ist nur ein
  Symlink auf den System-Interpreter, `.resolve()` hält beide fälschlich für identisch (3.63).
- `bleak`/BLE auf macOS: CoreBluetooth liefert keine echte Bluetooth-MAC, sondern eine app-spezifische
  UUID (aus Datenschutzgründen) — die "echte" MAC von Verpackung/Handy-App funktioniert dort nicht,
  per Scan ermitteln. Und: "write without response"-Pakete ganz ohne Pause zwischen den Häppchen
  verwirft macOS oft stillschweigend (kein Fehler, nur ein stilles Timeout beim Warten auf die
  Geräte-Bestätigung) — kleine Pause (~10ms) zwischen den Writes einbauen (3.63).

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
docker compose exec app node api/src/scripts/backup-db.js   # im laufenden Prod-Container
```

**Empfehlung für den Server:** ein Cron-Job, z.B. täglich um 3 Uhr:
```
0 3 * * * cd /pfad/zum/repo && docker compose exec -T app node api/src/scripts/backup-db.js >> /var/log/ue-hacker-backup.log 2>&1
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
- [ ] Server-Deploy (Nutzer deployt selbst: `git pull` + `docker compose up -d --build app`).
      `npm run build` triggert `build:cells`/`pack:notebooks` automatisch über `prebuild` (lokal per
      Docker-Build+Health-Check verifiziert, 3.65). Danach `/kurs/python-12-wochen-grundkurs` prüfen
      (Wochen-Tour, nicht Akkordeon).
- [ ] Backup-Cron auf dem Server einrichten (Befehl siehe Abschnitt 4, Pfad korrigiert 3.65);
      externe Sicherung der Backups bewusst nicht mitgebaut.

**Inhalte**
- Interaktiv-Kurs: "Ausführen vs. Prüfen"/Weiter-Flow — braucht konkretes Nutzer-Feedback.
- Alle 7 Projekt-Kurse: EN-Version offen (DE-first, `kurse.json` hat schon `title_en`).
- Zertifikat-PDF: E-Mail-Versand später (hängt an der Kontakt-Adresse, nicht selbst erfinden).
- Überlegung (nicht entschieden): dritte Sprache; UI-Ternarys sind schon auf `t()`, offen nur Content-Suffixe.

**Laufendes Kurs-Thema (Branch `kurs-ki-labor`, siehe todo.md):** Woche 1 fertig, Wochen 2–8 offen
(Nächste Nachbarn/k-NN, Training & Test, Entscheidungsbäume, Neuronale Netze I+II, Grenzen &
Ethik — Wochenplan siehe `KURSPLAN.md`). Weitere Projekt-Kurs-Ideen in `PROJEKTIDEEN.md`. Roadmap:
`VISION.md`.

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
