# Todo

Erledigtes (frühere Abschnitte "Now" + "Fertige Branches") steht kalt in `docs/archiv/todo-erledigt.md` —
nicht per `@` geladen, nur bei Bedarf lesen. Hier stehen nur **offene** Punkte und die nächsten Themen.

## Offen

- [x] Glossar-Notebooks (`0_glossar`) Woche 3–12 an die Lektionen angeglichen: Vorgriffe entfernt (Woche 4 Listen/`append`/Index, Woche 5 `try`/`except` in Pferde+Sci-Fi, Woche 8 `.update()`), Wiederholungs-Verweise korrigiert (Woche 5–7, 9), Woche-6-Tabelle repariert und um Listen ergänzt, Woche 10 Doppelzeile; Test `Glossare: keine Vorgriffe` in `tests/storytelling-content.spec.js`. Bewusst gelassen: `snake_case`/Algorithmus/Instanz (Konzepte ohne eigene Aufgabe), Woche 7 Pferde/Sci-Fi mit kleinerer Begriffsliste als Abenteuer.
- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken) —
      **zurückgestellt** (Nutzer will erst später deployen). Backup-Cron auf dem Server einrichten
      (Befehl siehe HANDOFF.md Abschnitt 4); externe Sicherung der Backups bewusst nicht mitgebaut.
- [ ] Tippfehler-Pass (`cspell`): `.vue`-Prosa (Ternary-/`t()`-Texte) und Interaktiv-/Projekt-Kurse noch
      nicht geprüft.
- [ ] Weitere Sprache neben DE/EN? Noch keine Entscheidung, kein Ziel. UI-Texte laufen bereits über
      `t()` (`locales/de.js`/`en.js`); offen bliebe nur der Content: `_en`-Feld-Suffix in
      `content/python-checks/week-{N}.json`, `-en`-Ordner-Suffix in `useCourseData.js`. Größter
      Aufwand wäre der Content selbst (444 Notebooks × Sprache). Keine neue i18n-Library nötig.
- [ ] `kurs-python-spiele` — Idee verworfen zugunsten von `kurs-js-spielewerkstatt`: Pyodides
      synchrones Ausführungsmodell ist mit einer echten Spiele-Loop unvereinbar (Archiv HANDOFF 3.32).

### 12-Wochen-Kurs: Lektions-Format (Branch `python-woche1-lektionen-format`)
- [x] Woche 1 + 2 (Abenteuer, Pferde, Sci-Fi; DE + EN) als Einzel-Lektionen im JS-Kurs-Format (siehe HANDOFF.md 3.47)
- [x] Woche 4 (Schleifen; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.48).
- [x] Woche 4: DE/EN-Struktur angeglichen (Abenteuer 8, Pferde 7, Sci-Fi 7 Lektionen; IDs/Aufgaben identisch, EN/DE jeweils als Übersetzung der größeren Fassung)
- [x] Woche 5 (Funktionen; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.49), ohne Sub-Agenten aus einer Datenquelle pro Thema erzeugt
- [x] Woche 6 (Listen; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.50): 9 Lektionen, Debug, 3 Missionen, 3 Extra-Herausforderungen je Thema, DE = EN; enthält die nachgezogenen Vorgriffe (Listen, `append`, `break`/`continue`, Funktionen mit Listen)
- [x] Woche 7 (Module; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.51): 7 Lektionen, Debug, 3 Missionen, 4 Extra-Herausforderungen je Thema, DE = EN; Zufalls-Aufgaben prüfen Eigenschaften statt fester Werte; nimmt die Woche-4/5-Vorgriffe mit `random`, `%` und Feld auf (Extra-Herausforderung 4)
- [x] Woche 8 (Dictionaries/Tupel; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.52): 7 Lektionen, Debug, 3 Missionen, 4 Extra-Herausforderungen je Thema, DE = EN; enthält die nachgezogenen Dictionary-/`try/except`-Vorgriffe aus Woche 5/6
- [x] Woche 9 (JSON und Dateien; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.53): 7 Lektionen, Debug, 3 Missionen, 4 Extra-Herausforderungen je Thema, DE = EN
- [x] Woche 10 (OOP Grundlagen), Woche 11 (OOP Fortgeschritten), Woche 12 (Text-Adventure-Abschlussprojekt; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.54): je 7 Lektionen/Etappen, Debug, 3 Missionen, 4 Extra-Herausforderungen, DE = EN
- [x] Lösungs-Notebooks passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.

#### Nachbesserungen Lektions-Format Woche 4
- [ ] Vorgriffe im Original (`break`/`continue`, `random`, Listen, `%`, `input()`) wurden in Missionen/Boss durch feste Werte, `if`/`or` und `while`-Bedingungen ersetzt, Mengen teils kleiner (z.B. Pferde Mission 1 bis 10 statt 20, Boss 1 5 statt 10 Sprünge). In Woche 6 als Wiederholung mit den vollen Original-Aufgaben nachziehen.
- [ ] Debug Bug #1 war im Original eine Endlosschleife (5s-Timeout), jetzt Off-by-one — bewusst so.
- [x] Glossar (Woche 4) bereinigt. [x] Lernziele-Checklisten der Original-Missionen (Woche 4: Listen/`append`/Index/`break`/`continue`; Woche 5: `try/except`) bereinigt. Offen bleibt: die Original-Missionen/-Boss-Notebooks selbst enthalten Listen-Aufgaben (Bonus/Boss), sie liegen nur noch im ZIP (siehe „Alte Notebooks“). Lösungs-Notebooks passen weiter zu den freien Original-Aufgaben.
- [x] `end=""` ist jetzt in Pferde DE/EN und Sci-Fi EN Lektion 7 erklärt; mehrzeilige `expected` mit `\n` (82 Aufgaben) in der App per Wegwerf-Test bestätigt.
- [x] Pferde DE Boss 3: "Noch 1 Runden" (Plural bei 1) — kosmetisch, DE+`expected` müssten gemeinsam geändert werden.
- [ ] `input()`-Beispiele (Zugangscodes/Passwort/Futter-Abfrage) nicht übernommen — die `stdin`-Validierung gibt es jetzt (`validation.stdin`, siehe INHALTE.md); die Aufgaben selbst sind noch nicht (wieder) ergänzt.

#### Nachbesserungen Lektions-Format Woche 3 (Angleichung DE/EN)
- [x] Pferde DE `boss-03`: Anweisung nennt "Kein Turniersieg", `expected` ist "Kein Turniersieg." (mit Punkt) — DE + EN vereinheitlichen.
- [x] Sci-Fi DE/EN `boss-03`: "Gesamtpunkte: 320 und Erfolgsquote: 80.0%" — unklar, ob eine oder zwei Zeilen, geprüft wird nur `Erfolgsquote: 80.0%`; "in zwei Zeilen" ergänzen (oder `expectedAll`).
- [ ] Pferde `boss-01` (Note/Zertifikat) hat keinen `else`-Zweig; Sci-Fi `boss-01.md` hat keine Antworttabelle mehr (DE + EN) — bei Bedarf ergänzen.
- [x] Lösungs-Notebooks passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.

#### Nachbesserungen Lektions-Format Woche 5 (Funktionen)
- [ ] Vorgriffe im Original (Listen, Dictionaries, `random`, `try/except`, `help()`, Quest-/Kampf-Listen) wurden ersetzt: Missionen/Boss nutzen nur Zahlen, Text, `if`/`elif`/`for`. **Listen-Anteil ist in Woche 6 nachgezogen** (Zauberbuch/Katalog als Liste, Statistik, Funktionen mit Listen). Dictionaries (`erstelle_*`, Quest-Dictionary) sind in Woche 8 (Extra-Herausforderung 4) nachgezogen, `random` in Woche 7.
- [x] `LessonView` prüfte nur die Ausgabe: **erledigt** über `validation.codeContains` (Woche 3–12 automatisch aus der Aufgabenstellung abgeleitet, siehe INHALTE.md); hart codiertes `print` besteht dort nicht mehr. Vorschlag: `functionCalls` (gibt es schon im Check-Schritt/`CodeChallenge`) auch in `LessonView` auswerten.
- [x] Lösungs-Notebooks Woche 5 passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.
- [ ] Woche-5-Themenbezeichner sind zwischen DE und EN nicht gleich (DE `berechne_schaden`, EN `calculate_damage`) — bewusst, wie in Woche 4.
- [ ] Debug Bug #1 (fehlende Einrückung nach `def`) erzeugt einen `IndentationError`; Bug #2 ruft die Funktion ohne Klammern auf (Ausgabe `<function ...>`), Bug #3 hat kein `return` (`None`) — bewusst die drei typischen Funktionsfehler.

#### Nachbesserungen Lektions-Format Woche 6 (Listen)
- [x] Aus dem Original wieder aufgenommen: Slicing (`[0:3]`, `[-2:]`, `[1::2]`), `extend()`, `sorted(set(...))`, `sorted(..., key=len)`, `.upper()` in der List Comprehension (je eine Zusatzaufgabe in Lektion 2/3/5/6/9).
- [x] Woche-2-Extras (8 Truhen/Säcke/Module, 5 Zauber/Übungen/KI-Modelle) und Woche-4-Mengen (Zahlen 1–20 gerade/rückwärts, sortierte Ereignis-Liste) mit den vollen Original-Mengen als Extra-Herausforderung 4 "Wiederholung" nachgezogen.
- [x] Boss 3 themenspezifisch benannt (Pferde `erstelle_turnier`/`turniere`, Sci-Fi `erstelle_mission`/`missionen`).
- [x] Woche-4-Vorgriffe mit `random`, `%` und dem 8×8-Feld sind in Woche 7 (Extra-Herausforderung 4) nachgezogen (Zufallswerte/-ereignisse/-weg, Primzahlen bis 100, Schachbrett, Figur über das Feld). Offen nur: `input()`-Aufgaben (braucht `stdin`-Validierung, siehe Woche 1–2/4-Nachbesserungen).
- [x] Dictionaries aus den Originalen sind in Woche 8 (Extra-Herausforderung 4) als Wiederholung nachgezogen.
- [ ] Woche 6 wurde aus einem gemeinsamen Skelett + Themen-Vokabular erzeugt (Generator liegt nur im Scratchpad, nicht im Repo) — Texte sind daher zwischen den Themen strukturell gleich, nur Vokabular/Geschichte unterscheiden sich.
- [x] Lösungs-Notebooks Woche 6 passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.

#### Nachbesserungen Lektions-Format Woche 7 (Module)
- [ ] Zufalls-Aufgaben prüfen nur Eigenschaften (Bereich, "in der Liste", Anzahl), nie feste Zufallswerte; ein `import random` ist über `codeContains` (`import`) nur teilweise erzwungen — dass `random` wirklich benutzt wird, bleibt ungeprüft.
- [ ] Aus dem Original weggelassen: `time.sleep(1)`-Rituale mit Sekunden (hier < 0,3 s, damit Tests/Aufgaben schnell laufen), `random.random()`/`uniform`-Ausgaben mit `:.3f`, Winkelfunktionen `tan`/Logarithmen (nur `sin`+`radians`, `factorial`/`gcd`/`lcm`), `math.tau`/`inf`, `input()` im Namens-Orakel (dort fester Name), `input()` im Dungeon-Bonus (nur Bonus-Text).
- [x] Lösungs-Notebooks Woche 7 passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.
- [ ] Woche 7 wurde wie Woche 6 aus einem Skelett + Themen-Vokabular erzeugt (Generator nur im Scratchpad); alle Referenzlösungen von Woche 5–7 wurden zusätzlich in Pyodide (node_modules, Python 3.13) ausgeführt — die App nutzt Pyodide 0.24.1 (Python 3.11), dort nicht separat geprüft.

#### Nachbesserungen Lektions-Format (Woche 1–2)
Beim Umbau aufgefallen; entweder bewusst so gelassen oder noch offen:
- [x] `max()` (kam in Woche 2 Abenteuer DE/EN Boss 1 und Pferde EN Boss 1 als Vorgriff vor) durch Vergleich mit `>` ersetzt (Lektions-JSON, Boss-Text, Lösungs-Notebook)
- [x] `//`, `%`, `**` (nur Sci-Fi EN Woche 2 Lektion 6, im Original und in allen anderen Themen nicht) entfernt
- [x] Woche 3: DE/EN je Thema angeglichen (Abenteuer 7 Lektionen + 4 Bugs, Pferde/Sci-Fi 6 Lektionen; IDs/Aufgaben DE = EN, Sci-Fi 4 Bugs, Pferde 3), Struktur per Skript + `python-lektionen-format.spec.js` geprüft
- [ ] Woche 3: `output_contains` prüft pro Aufgabe nur einen String (auch Abenteuer Lektion 7 Aufgabe 2 ohne Verschachtelung besteht, Boss 1/2/3 aller Themen prüfen nur die letzte Zeile); bei mehreren geforderten Ausgaben (z.B. Boss 1 Schritt 1, Boss 3 Schritt 2/4 Abenteuer DE) und hart codierten `print`s bleibt eine Lücke — Vorschlag: Mehrfach-Erwartung (`expectedAll`) oder `variables`-Check in `JsLessonView`/`LessonView` einführen
- [ ] Woche 3 Boss 2 (Abenteuer, Level 5: `a or b and c` ohne Klammern besteht ebenfalls) nutzt Klammern in `or (... and ...)` (leichter Vorgriff auf die Rangfolge von and/or), im Boss-Text erklärt
- [ ] Alte Notebooks (Lektion/Debug/Missionen/Boss) der umgestellten Wochen sind noch im Repo: sie speisen den Wochen-ZIP-Download (`_bundle`, Offline-Nutzung ohne Jupyter) und stehen nicht mehr in der Tour. Entscheidung offen: als "Original-Aufgaben" im ZIP behalten oder entfernen (dann ZIP aus den Lektionen neu bauen).
- [ ] Extra-Herausforderungen Woche 2 sind teils kleiner als das Original (z.B. 4 statt 8 Schiffe, 3 statt 5 KI-Modelle), weil Listen erst in Woche 6 kommen und `output_contains` nur feste Ausgaben prüft — bei Bedarf in Woche 6 als Wiederholung mit den vollen Mengen nachziehen
- [x] `input()`-Aufgaben (Woche 1, 2) prüfen jetzt mit `validation.stdin` und der daraus berechneten Ausgabe statt nur festen Textteilen.
- [ ] Missionen/Boss-Quests haben feste Vorgaben statt freier Gestaltung; Bonus-Teile sind ungeprüft — ggf. kreative "Freestyle"-Aufgabe pro Woche ohne Prüfung ergänzen
- [ ] Vergleiche mit `>` (Boolean-Kapitel Woche 2) werden für "Sieger/über Durchschnitt" genutzt, weil `if` erst in Woche 3 kommt — bewusst, im Original gehört `>` zum Boolean-Kapitel

#### Nachbesserungen Lektions-Format Woche 8 (Dictionaries/Tupel)
- [ ] Aus dem Original weggelassen: verschachteltes Questsystem mit Tupel-Belohnungen und Tupel als Dictionary-Schlüssel als Aufgabe (nur als Erklärung in Lektion 7), Tupel-Methoden `index()`/`count()`, Bonus-Teile ungeprüft. Grund: `output_contains` prüft nur feste Ausgaben.
- [x] `dict`/`try`-Struktur: `try`/`except`, `def`, `json.*`, `csv.*` werden jetzt über `validation.codeContains` geprüft (siehe Woche 5); `dict` selbst nicht (kein eindeutiger Baustein).
- [x] Lösungs-Notebooks Woche 8 passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.
- [ ] Woche 8 wurde wie Woche 6/7 aus einem Skelett + Themen-Vokabular erzeugt (Generator nur im Scratchpad); Aufgaben teils identisch zwischen den Themen, nur Vokabular unterscheidet sich.

#### Nachbesserungen Lektions-Format Woche 10–12 (OOP, Text-Adventure)
- [ ] Woche 2: DE und EN sind strukturell nicht angeglichen (Aufgaben-/Lektionsanzahl weicht in Abenteuer, Pferde und Sci-Fi ab, IDs unterschiedlich) — wie bei Woche 3/4 aus der größeren Fassung angleichen (`python-woche2-*`, 17 Abweichungen).
- [x] Struktur (`class`, `super()`, Magic Methods, `isinstance`) wird über `validation.codeContains` geprüft; Rest-Lücke: Bausteine in Texten/Kommentaren zählen nicht als Umgehung, aber `print("class")` zählt als Vorkommen (bewusst einfach).
- [ ] Woche 12: Lektion ist in 7 Etappen mit kleinen, einzeln geprüften Aufgaben statt einem durchlaufenden Spiel-Notebook; das Original (Startpaket-Zellen, `spiele()` mit Zufalls-Kampf) liegt nur noch als Nachschlagewerk „Lösungen“ (und `woche12_*_1_lektion`) im Repo. Kampf-Aufgaben nutzen 1-HP-Gegner, damit die Prüfung deterministisch ist.
- [ ] Aus den Originalen weggelassen: Operator-Polymorphismus mit `__add__` auf Goldstücken als Beispiel (jetzt `Supply`/`Vorrat`), `__getitem__`, `input()`-Befehlsschleife in Woche 12 (Befehle stehen als Liste, braucht `stdin`-Validierung), Bonus-Teile ungeprüft.
- [x] Lösungs-Notebooks Woche 10–12 sind aus den Referenzlösungen der Aufgaben neu erzeugt (eine Zelle je Aufgabe, Debug mit Erklärung). Offen bleibt nur das Glossar von Woche 10–12 (erwähnt teils Themen der Original-Aufgaben).
- [ ] Woche 10–12 wurden wie Woche 6–9 aus einem Skelett + Themen-Vokabular erzeugt (Generator nur im Scratchpad); Aufgaben teils identisch zwischen den Themen, nur Vokabular unterscheidet sich. EN nutzt englische Bezeichner (`Player`, `world`, `go north`).
- [ ] (siehe oben: alte Notebooks) — `tests/storytelling-content.spec.js` liest noch aus den Quelldateien von Woche 5/8/9/11/12.

#### Nachbesserungen Lektions-Format Woche 9 (JSON und Dateien)
- [ ] `input()`-Aufgaben aus dem Original (Boss 1 Tagebuch, Eintrag per `input()`) durch vorgegebene Einträge ersetzt, `input()` nur als Bonus — `validation.stdin` gibt es jetzt; als Aufgabe nachziehen.
- [ ] Dateien liegen im Pyodide-Dateisystem und bleiben zwischen Aufgaben (und Läufen) bestehen; jede Aufgabe schreibt ihre Dateien deshalb selbst. Ob das Dateisystem beim Kernel-Neustart geleert wird, in der App nicht separat geprüft.
- [ ] Aus dem Original weggelassen: `f.writelines()`, `json.dumps(indent=2)`-Ausgabe als Prüfung, `csv.DictWriter` mit `extrasaction`, `with open(..., "x")`; nur `indent`/Umlaut-Escapes (`\\u00e4`) sind als Hinweis erwähnt.
- [x] Lösungs-Notebooks Woche 9 passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.
- [ ] Woche 9 wurde wie Woche 6–8 aus einem Skelett + Themen-Vokabular erzeugt (Generator nur im Scratchpad).

---

## Nächste Themen (je eigener Branch von `main`)

Reihenfolge empfohlen: 1 → 2 → 3. Nicht mischen. (Branch-Namen ohne `cursor/`-Präfix.)
Gesamt-Roadmap/Track-Modell (welche Sprache/welches Thema baut auf was auf) siehe `VISION.md`.

### 1. JavaScript-Spielewerkstatt — Branch `kurs-js-spielewerkstatt` ✅ gemergt
Ersetzt die frühere Idee einer Python-Spiele-Werkstatt: Pyodides synchrones "einmal ausführen"-
Modell ist mit einer echten Spiele-Loop (requestAnimationFrame, laufende Tasten-/Maus-Events)
unvereinbar (siehe HANDOFF.md 3.32) — daher JavaScript statt Python, mit einer neuen
iframe-Sandbox-Ausführungsumgebung. Kompaktes Projekt (6 Lektionen, wie Cäsar-Chiffre), erstes
Spiel "Fang den Ball". Details siehe HANDOFF.md 3.39.
- [x] Neue JS-Sandbox-Ausführungsumgebung (`useJsSandbox.js`, iframe-basiert, kein Worker)
- [x] `engine`-Prop an `ProjectCourse.vue`/`CourseDetail.vue` ergänzt (Default `'pyodide'`)
- [x] Kursmetadaten in `kurse.json` (`engine: "js-sandbox"`, `language: "javascript"`, `level`,
      neuer Tag `spiele` im Projekte-Filter-Vokabular, inkl. neuer `projectTag.spiele`-Locale-Keys)
- [x] Content: 6 Lektionen "Fang den Ball" (DE-first, kein `-en`-Ordner wie Cäsar-Chiffre)
- [x] Playwright-Tests (`tests/js-spielewerkstatt.spec.js`, 12 Tests) + `tests/projekte.spec.js`
      angepasst → volle `test:checks`-Suite grün.
- [ ] `KURSPLAN.md`/`VISION.md` bei Bedarf nachziehen — bisher keine Abweichung vom dortigen
      Track-Modell nötig (JS-Projekt-Kurs passt unverändert ins bestehende Schema)

### 2. Was kommt danach? Python-Projekt-Sprints — Branch `kurs-python-projekte`
Die Infrastruktur dafür existiert bereits (Branch `kurs-projekte-uebersicht`, s.u.): generalisiertes
`ProjectCourse.vue`, Projekte-Übersicht mit Filtern unter `/projekte`. Ein weiteres Projekt braucht
nur noch einen Content-Ordner + `kurse.json`-Eintrag (siehe `INHALTE.md` §6), keine neue Komponente.
- [ ] 2–3 weitere Projekt-Ideen ausarbeiten (Sprints im Cäsar-Chiffre-Stil, ~5 Lektionen) —
      Ideen-Backlog mit ~40 Vorschlägen (Spiele, Web, KI, Logik, Krypto, Kreativ, Daten) samt
      Reihenfolge-Empfehlung in `PROJEKTIDEEN.md`; beim Umsetzen dort abhaken
- [ ] Projektideen aus Einstufung ggf. hier ausbauen
- [ ] DE (+ EN nach Bedarf)
- [ ] Smoke-Test → PR nach `main`

### 3. KI-Labor — Branch `kurs-ki-labor`
Baut auf dem Python-Track auf (12-Wochen-Grundkurs), siehe `VISION.md`/`KURSPLAN.md` Kurs 4
"KI-Grundlagen". Breitere Zielgruppe, Fokus auf Prompts/Grenzen/Schul-Nutzen.
- [ ] Kursmetadaten + Content
- [ ] Smoke-Test → PR nach `main`

**Hinweis:** Drittes Thema erst starten, wenn 1 und 2 gemerged sind (oder bewusst parallel nur
wenn Kapazität klar ist).
