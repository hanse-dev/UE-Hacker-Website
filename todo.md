# Todo

Erledigtes (frühere Abschnitte "Now" + "Fertige Branches") steht kalt in `docs/archiv/todo-erledigt.md` —
nicht per `@` geladen, nur bei Bedarf lesen. Hier stehen nur **offene** Punkte und die nächsten Themen.

## Offen

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
- [ ] Nutzer-Feedback abwarten, dann entscheiden: Wochen 7–12
- [ ] Lösungen/Glossar für das neue Format anpassen (Lösungen passen noch zu den freien Original-Aufgaben)

#### Nachbesserungen Lektions-Format Woche 4
- [ ] Vorgriffe im Original (`break`/`continue`, `random`, Listen, `%`, `input()`) wurden in Missionen/Boss durch feste Werte, `if`/`or` und `while`-Bedingungen ersetzt, Mengen teils kleiner (z.B. Pferde Mission 1 bis 10 statt 20, Boss 1 5 statt 10 Sprünge). In Woche 6 als Wiederholung mit den vollen Original-Aufgaben nachziehen.
- [ ] Debug Bug #1 war im Original eine Endlosschleife (5s-Timeout), jetzt Off-by-one — bewusst so.
- [ ] Glossar (`0_glossar`) und Lernziele-Checkliste der Original-Missionen erwähnen Listen/`append` (Vorgriff auf Woche 6) — bereinigen. Lösungs-Notebooks passen weiter zu den freien Original-Aufgaben.
- [x] `end=""` ist jetzt in Pferde DE/EN und Sci-Fi EN Lektion 7 erklärt; mehrzeilige `expected` mit `\n` (82 Aufgaben) in der App per Wegwerf-Test bestätigt.
- [ ] Pferde DE Boss 3: "Noch 1 Runden" (Plural bei 1) — kosmetisch, DE+`expected` müssten gemeinsam geändert werden.
- [ ] `input()`-Beispiele (Zugangscodes/Passwort/Futter-Abfrage) nicht übernommen — braucht `stdin`-Validierung.

#### Nachbesserungen Lektions-Format Woche 3 (Angleichung DE/EN)
- [ ] Pferde DE `boss-03`: Anweisung nennt "Kein Turniersieg", `expected` ist "Kein Turniersieg." (mit Punkt) — DE + EN vereinheitlichen.
- [ ] Sci-Fi DE/EN `boss-03`: "Gesamtpunkte: 320 und Erfolgsquote: 80.0%" — unklar, ob eine oder zwei Zeilen, geprüft wird nur `Erfolgsquote: 80.0%`; "in zwei Zeilen" ergänzen (oder `expectedAll`).
- [ ] Pferde `boss-01` (Note/Zertifikat) hat keinen `else`-Zweig; Sci-Fi `boss-01.md` hat keine Antworttabelle mehr (DE + EN) — bei Bedarf ergänzen.
- [ ] DE/EN wurden pro Thema aus der größeren Fassung angeglichen; die alten Lösungs-/Glossar-Notebooks von Woche 3 passen nicht mehr zu den Aufgaben (siehe Lösungen/Glossar-Punkt oben).

#### Nachbesserungen Lektions-Format Woche 5 (Funktionen)
- [ ] Vorgriffe im Original (Listen, Dictionaries, `random`, `try/except`, `help()`, Quest-/Kampf-Listen) wurden ersetzt: Missionen/Boss nutzen nur Zahlen, Text, `if`/`elif`/`for`. **Listen-Anteil ist in Woche 6 nachgezogen** (Zauberbuch/Katalog als Liste, Statistik, Funktionen mit Listen). Noch offen: Dictionaries (`erstelle_charakter`, Quest-Dictionary) → Woche 8, Zufallszauber/`random` → Woche 7.
- [ ] `LessonView` prüft nur die Ausgabe (`output_contains`): dass eine Funktion wirklich mit `def` definiert wurde, wird nicht geprüft (hart codiertes `print` besteht). Vorschlag: `functionCalls` (gibt es schon im Check-Schritt/`CodeChallenge`) auch in `LessonView` auswerten.
- [ ] Lösungs-/Glossar-Notebooks Woche 5 (`content/python-12-wochen-grundkurs*/woche-5/*`) passen nicht zu den konkretisierten Aufgaben (Original mit Dictionaries/Listen/`random`), Glossar erwähnt Docstring-Stile (`Args:`/`Returns:`) und `help()` — bereinigen.
- [ ] Woche-5-Themenbezeichner sind zwischen DE und EN nicht gleich (DE `berechne_schaden`, EN `calculate_damage`) — bewusst, wie in Woche 4.
- [ ] Debug Bug #1 (fehlende Einrückung nach `def`) erzeugt einen `IndentationError`; Bug #2 ruft die Funktion ohne Klammern auf (Ausgabe `<function ...>`), Bug #3 hat kein `return` (`None`) — bewusst die drei typischen Funktionsfehler.

#### Nachbesserungen Lektions-Format Woche 6 (Listen)
- [ ] Aus dem Original bewusst weggelassen: `set()`/`list(set(...))` (Duplikate entfernen), `.upper()`/String-Methoden in der List Comprehension, `sorted(..., key=...)`, Slicing (`liste[0:3]`), `extend()` nur im Text; Dictionaries in Boss-Quest 3 (dort Liste `[name, ziel, schwierigkeit]`) → Dictionaries in Woche 8 als Wiederholung nachziehen.
- [ ] Woche-4-Vorgriffe (Pferde Mission 1 bis 20 statt 10 Hürden, Boss 5 statt 10 Sprünge, Abenteuer/Sci-Fi mit `random`/`%`/`input()`) sind in Woche 6 noch NICHT mit den vollen Original-Mengen wiederholt — nur `break`/`continue` und Listen mit Schleifen sind drin. Woche-2-Extras (8 Schiffe, 5 KI-Modelle als Liste) ebenfalls offen.
- [ ] Code-Bezeichner in Pferde/Sci-Fi Boss 3 heißen `quest` (`erstelle_quest`, `suche_quests`) obwohl es Turniere/Missionen sind — bewusst generisch gehalten (ein Skelett für alle Themen), bei Bedarf themenspezifisch umbenennen.
- [ ] Woche 6 wurde aus einem gemeinsamen Skelett + Themen-Vokabular erzeugt (Generator liegt nur im Scratchpad, nicht im Repo) — Texte sind daher zwischen den Themen strukturell gleich, nur Vokabular/Geschichte unterscheiden sich.
- [ ] Lösungs-/Glossar-Notebooks Woche 6 passen nicht zu den konkretisierten Aufgaben (Original mit `set`, Dictionaries, `random`).

#### Nachbesserungen Lektions-Format (Woche 1–2)
Beim Umbau aufgefallen; entweder bewusst so gelassen oder noch offen:
- [x] `max()` (kam in Woche 2 Abenteuer DE/EN Boss 1 und Pferde EN Boss 1 als Vorgriff vor) durch Vergleich mit `>` ersetzt (Lektions-JSON, Boss-Text, Lösungs-Notebook)
- [x] `//`, `%`, `**` (nur Sci-Fi EN Woche 2 Lektion 6, im Original und in allen anderen Themen nicht) entfernt
- [x] Woche 3: DE/EN je Thema angeglichen (Abenteuer 7 Lektionen + 4 Bugs, Pferde/Sci-Fi 6 Lektionen; IDs/Aufgaben DE = EN, Sci-Fi 4 Bugs, Pferde 3), Struktur per Skript + `python-lektionen-format.spec.js` geprüft
- [ ] Woche 3: `output_contains` prüft pro Aufgabe nur einen String (auch Abenteuer Lektion 7 Aufgabe 2 ohne Verschachtelung besteht, Boss 1/2/3 aller Themen prüfen nur die letzte Zeile); bei mehreren geforderten Ausgaben (z.B. Boss 1 Schritt 1, Boss 3 Schritt 2/4 Abenteuer DE) und hart codierten `print`s bleibt eine Lücke — Vorschlag: Mehrfach-Erwartung (`expectedAll`) oder `variables`-Check in `JsLessonView`/`LessonView` einführen
- [ ] Woche 3 Boss 2 (Abenteuer, Level 5: `a or b and c` ohne Klammern besteht ebenfalls) nutzt Klammern in `or (... and ...)` (leichter Vorgriff auf die Rangfolge von and/or), im Boss-Text erklärt
- [ ] Alte Notebooks (Lektion/Debug/Missionen/Boss) der umgestellten Wochen sind noch im Repo (`_bundle` für den ZIP-Download) — entfernen bzw. ausblenden, sobald alle Wochen umgestellt sind
- [ ] Extra-Herausforderungen Woche 2 sind teils kleiner als das Original (z.B. 4 statt 8 Schiffe, 3 statt 5 KI-Modelle), weil Listen erst in Woche 6 kommen und `output_contains` nur feste Ausgaben prüft — bei Bedarf in Woche 6 als Wiederholung mit den vollen Mengen nachziehen
- [ ] `input()`-Aufgaben prüfen nur feste Textteile (Eingabe ist frei), z.B. Woche 2 Lektion "Eingaben" und Mission 3 — eine Prüfung mit vorgegebener Eingabe bräuchte eine neue `validation`-Variante (`stdin`)
- [ ] Missionen/Boss-Quests haben feste Vorgaben statt freier Gestaltung; Bonus-Teile sind ungeprüft — ggf. kreative "Freestyle"-Aufgabe pro Woche ohne Prüfung ergänzen
- [ ] Vergleiche mit `>` (Boolean-Kapitel Woche 2) werden für "Sieger/über Durchschnitt" genutzt, weil `if` erst in Woche 3 kommt — bewusst, im Original gehört `>` zum Boolean-Kapitel

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
