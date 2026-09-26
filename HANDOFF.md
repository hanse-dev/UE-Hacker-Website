# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-26
> **Aktueller Stand:** `main` enthält KI-Labor Woche 1–8 (kompletter Kursplan, siehe Abschnitt 5) —
> offen ist nur noch ein abschließender Smoke-Test aller Wochen. Profil zeigt Wochen-Zertifikate aus allen Kursen mit
> Wochen-Check (Python + KI-Labor) inkl. direktem PDF-Download (3.69/3.70); ein "Kurs starten"-Gate
> blendet bei den 3 Wochen-Tour-Kursen Beschreibung/Struktur-Erklärung vor der eigentlichen
> Kurs-Tour aus (3.69). `output_contains`-Aufgabenprüfung toleriert jetzt Groß-/Kleinschreibung,
> Leerzeichen und Satzzeichen am Ende (3.78). Normale Lektionsaufgaben (LessonView/JsLessonView)
> prüfen jetzt nur noch die Ausgabe, nicht mehr Code-Struktur/Variablen/Funktionsaufrufe; der
> zertifikatsrelevante Wochen-Check behält diese Prüfung (3.80). Server-Deploy steht weiter aus
> (Nutzer deployt selbst, siehe Abschnitt 4 "Betrieb").
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
| 3.72 | KI-Labor: Woche 3 "Nächste Nachbarn (k-NN)" | 5 Lektionen (Abstand, euklidische Distanz, 1-NN, Dictionary-Zählen + k nächste, kompletter k-NN-Klassifikator) + Debug + Mission + 3 Extra-Herausforderungen (gewichteter k-NN, Genauigkeit/bestes k, Unentschieden bei >2 Klassen) + eigener Wochen-Check |
| 3.73 | KI-Labor: Woche 4 "Training & Test" | 5 Lektionen (Trainings-/Testdaten trennen, Genauigkeit, Vorhersagen sammeln, alles zusammenfügen, Overfitting an zu kleinem Datensatz) + Debug + Mission + 3 Extra-Herausforderungen (Ausreißer bei k=1 vs. k=3, Trainingsgröße, Overfitting-Erkennung) + eigener Wochen-Check |
| 3.74 | KI-Labor: Woche 5 "Entscheidungsbäume" | 5 Lektionen (Schwellenwert-Entscheidung, Aufteilen+Reinheit messen, besten Trennwert automatisch finden, Baum bauen+klassifizieren, bestes Merkmal wählen) + Debug + Mission + 3 Extra-Herausforderungen (irrelevantes Merkmal ignorieren, Baum auf Testdaten prüfen, unvollkommener Baum vs. Baseline) + eigener Wochen-Check; alle Beispiele/Lösungen mit `python3` geprüft |
| 3.75 | KI-Labor: Woche 6 "Neuronale Netze I" | 5 Lektionen (gewichtete Summe, Sprungfunktion, komplettes Neuron, logische Gatter UND/ODER/NAND/NOR per Gewichte/Schwellenwert, XOR-Grenze eines einzelnen Neurons) + Debug + Mission + 3 Extra-Herausforderungen (gewichtete Sensoren, Schwellenwert-Vergleich per Genauigkeit, systematischer XOR-Beweis) + eigener Wochen-Check; kein Gewichte-Lernen (Perzeptron-Lernregel folgt in Woche 7), alle Beispiele/Lösungen mit `python3` geprüft |
| 3.76 | KI-Labor: Woche 7 "Neuronale Netze II" | 5 Lektionen (Wiederholung Einzelneuron, warum ein Neuron XOR nicht löst, versteckte Schicht + Vorwärtslauf, Gewichte per Zufalls-Suche selbst lernen lassen, trainiertes Netz vs. Einzelneuron-Baseline) + Debug + Mission (Lichtschalter-Rätsel) + 3 Extra-Herausforderungen (XNOR nachbauen, XNOR selbst trainieren, 3×3-Pixel-Mustererkennung) + eigener Wochen-Check; alle Beispiele/Lösungen mit `python3` geprüft |
| 3.77 | KI-Labor: Woche 8 "Grenzen & Ethik" (letzte Woche des Kurses) | 5 Lektionen (schiefe Trainingsdaten, Accuracy-Paradox, Baum übernimmt den Bias, Ausgleich per Undersampling, Chatbots/Datenschutz-Analogie) + Debug + Mission (eigener Bias-Datensatz ausgleichen) + 3 Extra-Herausforderungen (3-Klassen-Bias, Oversampling, Grenzen von Anonymisierung) + eigener Wochen-Check; kein "nächste Woche"-Button mehr nach dem Zertifikat, alle Beispiele/Lösungen mit `python3` geprüft |
| 3.78 | `output_contains` toleriert Groß-/Kleinschreibung, Leerzeichen, Satzzeichen am Ende | `output_equals` bleibt bewusst exakt (prüft teils auf ungewollte Extra-Ausgabe); Test in `week-checks-logic.spec.js` |
| 3.79 | Interaktiv-Kurs: Lektionstexte ausführlicher (Kinder + Jugendliche, DE) | reine Textüberarbeitung, keine Logikänderung |
| 3.80 | Lektionsaufgaben prüfen nur noch die Ausgabe, nicht mehr Code-Struktur/Variablen | `validation.codeContains`/`variables`/`functionCalls` sind in `LessonView.vue`/`JsLessonView.vue` nicht mehr blockierend; `useTaskValidation.js` trennt `validateOutput()` (nur Ausgabe) von `structuralChecksOk()` (nur noch für `CodeChallenge.vue`/Wochen-Check) |

### Gelernte Regeln (wiederverwendbare Fallstricke)

**Content / Notebooks**
- Bulk-Edits an JSON/Notebooks nie per volle Reserialisierung, sondern gezielte Text-Ersetzung + `json.loads()` danach (3.12, 3.16). Seit 3.33 sind 12-Wochen-Notebooks Zellen-Ordner (`NN_*.py`) — keine `.ipynb` als Quelle wieder einführen.
- Debug-Bugs müssen vom Kernel-Zustand unabhängig sein und dürfen die Lösung nicht verraten (3.4). Nach Notebook-Änderung Code-Zellen mit gemeinsamem Namespace per `python3` ausführen.
- Ein "Fund" aus einer Variante gilt nicht automatisch für alle: vor Massenänderungen alle 3 Varianten × DE/EN per grep prüfen (3.26–3.30).
- Neue Aufgabe zu einer bestehenden Lektion im Lektions-Format hinzufügen: in `lessons.json` einfach ans Ende von `tasks` anhängen (egal an welche Lektion sie inhaltlich gehört), UND im passenden `_N_loesungen`-Notebook-Ordner ein neues Markdown+Code-Zell-Paar mit der **höchsten** Nummer ans Ende anhängen — nie mittendrin einfügen, sonst müssen alle nachfolgenden Zellen umnummeriert werden. Der Test `tests/python-lektionen-format.spec.js` prüft nur Textvorkommen + Zellenzahl, nicht die Reihenfolge (3.71).
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
- Seit 3.80 prüft `validateOutput()` (in `LessonView.vue`/`JsLessonView.vue`, also allen normalen
  Lektionsaufgaben) **nur noch die Ausgabe** — `validation.codeContains`/`variables`/`functionCalls`
  in `lessons.json` werden dort ignoriert (bewusst: kein Blockieren mehr durch Code-Struktur). Eine
  Aufgabe **ohne** eigenes `expected`, die sich bisher allein auf `variables`/`functionCalls` verließ
  (z.B. reine "lege diese Variable an"-Aufgaben), besteht dadurch schon, wenn der Code fehlerfrei
  läuft — bei neuen solchen Aufgaben immer ein `expected` (`output_contains`) ergänzen, sonst prüft
  nichts mehr. Nur der zertifikatsrelevante Wochen-Check (`CodeChallenge.vue`) nutzt weiterhin
  `structuralChecksOk()` und braucht echte `variables`/`functionCalls`.

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
- Ein Bildschirm hinter einen Klick-Button setzen (z.B. "Kurs starten") heißt: **jeder** Test, der
  bisher direkt auf diesen Bildschirm navigiert ist, braucht den Klick jetzt davor — repo-weit nach
  der bisherigen bloßen `page.goto(...)`-Zeile grep-suchen (nicht nur die offensichtlichen
  Test-Dateien), Deep-Links mit Query-Parametern, die den neuen Gate-Zustand ohnehin auf "schon
  offen" setzen, brauchen dagegen keine Änderung (3.69).
- CSS-Kind-Selektoren wie `.course-detail > h1` in Tests sind ein stilles Kopplungsrisiko: ein neu
  eingefügter Wrapper-`<div>` um ein Element bricht sie, ohne dass der Test einen offensichtlichen
  Grund nennt. Vor dem Verschachteln eines Elements, das anderswo per direktem Kind-Selektor
  angesprochen wird, repo-weit nach genau diesem Selektor suchen (3.69).

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

**Laufendes Kurs-Thema (siehe todo.md):** KI-Labor komplett (Woche 1–8), nur noch ein
abschließender Smoke-Test aller Wochen offen. Weitere Projekt-Kurs-Ideen in `PROJEKTIDEEN.md`.
Roadmap: `VISION.md`.

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
- `validation.type: "output_contains"` prüft seit 3.78 tolerant (Groß-/Kleinschreibung, mehrfache
  Leerzeichen, Satzzeichen am Ende egal) — `output_equals` bleibt exakt. Beim Schreiben neuer
  Aufgaben mit `output_equals` bewusst bleiben, wenn genau das der Lernpunkt ist (z.B. "keine
  Extra-Ausgabe").

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
