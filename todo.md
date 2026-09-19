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
- [x] Woche 4 (Schleifen; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.48). Woche 3 fehlt noch.
- [x] Woche 4: DE/EN-Struktur angeglichen (Abenteuer 8, Pferde 7, Sci-Fi 7 Lektionen; IDs/Aufgaben identisch, EN/DE jeweils als Übersetzung der größeren Fassung)
- [ ] Nutzer-Feedback abwarten, dann entscheiden: Wochen 3, 5–12
- [ ] Lösungen/Glossar für das neue Format anpassen (Lösungen passen noch zu den freien Original-Aufgaben)

#### Nachbesserungen Lektions-Format Woche 4
- [ ] Vorgriffe im Original (`break`/`continue`, `random`, Listen, `%`, `input()`) wurden in Missionen/Boss durch feste Werte, `if`/`or` und `while`-Bedingungen ersetzt, Mengen teils kleiner (z.B. Pferde Mission 1 bis 10 statt 20, Boss 1 5 statt 10 Sprünge). In Woche 6 als Wiederholung mit den vollen Original-Aufgaben nachziehen.
- [ ] Debug Bug #1 war im Original eine Endlosschleife (5s-Timeout), jetzt Off-by-one — bewusst so.
- [ ] Glossar (`0_glossar`) und Lernziele-Checkliste der Original-Missionen erwähnen Listen/`append` (Vorgriff auf Woche 6) — bereinigen. Lösungs-Notebooks passen weiter zu den freien Original-Aufgaben.
- [x] `end=""` ist jetzt in Pferde DE/EN und Sci-Fi EN Lektion 7 erklärt; mehrzeilige `expected` mit `\n` (82 Aufgaben) in der App per Wegwerf-Test bestätigt.
- [ ] Pferde DE Boss 3: "Noch 1 Runden" (Plural bei 1) — kosmetisch, DE+`expected` müssten gemeinsam geändert werden.
- [ ] `input()`-Beispiele (Zugangscodes/Passwort/Futter-Abfrage) nicht übernommen — braucht `stdin`-Validierung.

#### Nachbesserungen Lektions-Format (Woche 1–2)
Beim Umbau aufgefallen; entweder bewusst so gelassen oder noch offen:
- [x] `max()` (kam in Woche 2 Abenteuer DE/EN Boss 1 und Pferde EN Boss 1 als Vorgriff vor) durch Vergleich mit `>` ersetzt (Lektions-JSON, Boss-Text, Lösungs-Notebook)
- [x] `//`, `%`, `**` (nur Sci-Fi EN Woche 2 Lektion 6, im Original und in allen anderen Themen nicht) entfernt
- [ ] Woche 3: Debug-Bugs uneinheitlich (Abenteuer DE + Sci-Fi DE haben 4 Bugs, die übrigen Themen/Sprachen 3), ebenso Aufgabenzahl bei Missionen/Boss — angleichen (Konzept "identisch zwischen Varianten", siehe INHALTE.md)
- [ ] Woche 3: `output_contains` prüft pro Aufgabe nur einen String; bei mehreren geforderten Ausgaben (z.B. Boss 1 Schritt 1, Boss 3 Schritt 2/4 Abenteuer DE) und hart codierten `print`s bleibt eine Lücke — Vorschlag: Mehrfach-Erwartung (`expectedAll`) oder `variables`-Check in `JsLessonView`/`LessonView` einführen
- [ ] Woche 3 Boss 2 (Abenteuer) nutzt Klammern in `or (... and ...)` (leichter Vorgriff auf die Rangfolge von and/or), im Boss-Text erklärt
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
