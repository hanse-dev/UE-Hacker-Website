# Todo

Erledigtes (frühere Abschnitte "Now" + "Fertige Branches") steht kalt in `docs/archiv/todo-erledigt.md` —
nicht per `@` geladen, nur bei Bedarf lesen. Hier stehen nur **offene** Punkte und die nächsten Themen.

## Laufend: Woche 2 DE/EN angleichen (Branch `python-lektionen-nacharbeiten`)

**Für die nächste Session — hier genau weitermachen:**

Ziel: Wie bei Woche 3/4 wird pro Variante die *größere* Fassung zur Referenz, die andere Sprache wird
1:1 übersetzt (gleiche Lektionsanzahl/-IDs/Aufgabenanzahl, `validation.expected` lokalisiert). Vorgehen
pro Variante: DE/EN-`lessons.json` + alle `.md`-Dateien der Zielsprache neu schreiben (Referenz als
Vorlage), Referenzlösungen von Hand schreiben und mit `python3` prüfen (je Aufgabe: `exec()` gegen
`validation.expected`/`codeContains`/`stdin`), `6_loesungen`-Zellenordner neu erzeugen (Format: siehe
ein beliebiger bestehender `*_6_loesungen`-Ordner — `### <Lektionstitel> – Aufgabe/Task N` + Code,
Abschnittsüberschrift beim ersten Task eines neuen `section`-Werts), `build_cell_notebooks.py` laufen
lassen, dann `python-lektionen-format.spec.js` für die Variante prüfen.

- [x] Abenteuer + Pferde fertig, committet und nach `main` gemergt (`npm run test:checks` grün,
      340 Tests). Details siehe `docs/archiv/todo-erledigt.md`.
- [ ] **Sci-Fi (ausnahmsweise umgekehrt: EN war größer — 7 Lektionen/46 Aufgaben — DE wird an EN
      angeglichen):** **mitten in der Arbeit, nichts committet oder gestaged:**
      - [x] `content/python-woche2-scifi/lessons.json` komplett neu geschrieben (14 Einträge, 46
        Aufgaben, Struktur/IDs = EN)
      - [x] `.md`-Dateien neu geschrieben: `lektion-01` bis `lektion-07`, `debug-01`, `mission-01`
      - [ ] **Fehlen noch:** `mission-02.md`, `mission-03.md`, `boss-01.md`, `boss-02.md`,
        `boss-03.md` (liegen noch mit altem, nicht mehr passendem DE-Text da — Referenztext auf
        Englisch in `content/python-woche2-scifi-en/{mission-02,mission-03,boss-01,boss-02,boss-03}.md`,
        einfach übersetzen, Tabellen/Zahlen 1:1 übernehmen)
      - [ ] Referenzlösungen für alle 39 Nicht-Beispiel-Aufgaben schreiben und mit `python3` gegen
        `validation` prüfen (Beispiel-Prüfskript: für jede Aufgabe den Code `exec()`-en, `stdout`
        gegen `expected` prüfen, bei `stdin` die Werte der Reihe nach als `input()`-Antworten
        durchreichen) — beim Abbruch einer früheren Session lag ein fertiges, geprüftes Lösungs-Dict
        nur im Scratchpad (nicht im Repo, laut Konvention "Generator/Solver nur im Scratchpad" —
        siehe Gelernte Regeln in HANDOFF.md), ist mit der Session weg und muss neu geschrieben werden.
      - [ ] `content/python-12-wochen-grundkurs/woche-2/scifi/woche2_scifi_6_loesungen/` mit den 39
        Lösungen neu erzeugen (Format s.o.), dann `npm run build:cells`
      - [ ] Prüfen: `npx playwright test tests/python-lektionen-format.spec.js -g "scifi"`,
        `python3 scripts/build_lesson_bundle.py`
- [ ] Nach Sci-Fi: `npm run test:checks` voll grün, dann committen, `todo.md`/`HANDOFF.md`
      aktualisieren (Abschnitt 3, neue Nummer nach 3.55), danach **erst weiter mit den
      input()-Wochen (Punkt 4) und den Kleinigkeiten (Punkt 5)** aus dem ursprünglichen
      5-Punkte-Plan des Nutzers.

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

### Offene Nachbesserungen Lektions-Format (nach Woche)

12-Wochen-Kurs Woche 1–12 ist komplett im Lektions-Format (Details/erledigte Punkte siehe
`docs/archiv/todo-erledigt.md`). Hier nur die verbliebenen, bewusst noch offenen Lücken:

- **Woche 1–2:** `output_contains` prüft pro Aufgabe nur einen String — bei mehreren geforderten
  Ausgaben (z.B. Boss 1 Schritt 1, Boss 3 Schritt 2/4 Abenteuer DE) und hart codierten `print`s
  bleibt eine Lücke (Vorschlag: `expectedAll` oder `variables`-Check in `JsLessonView`/`LessonView`).
  Woche 3 Boss 2 (Abenteuer) nutzt Klammern in `or (... and ...)` als leichter Vorgriff auf die
  Rangfolge von and/or (im Boss-Text erklärt). Extra-Herausforderungen Woche 2 sind teils kleiner
  als das Original (z.B. 4 statt 8 Schiffe), weil Listen erst in Woche 6 kommen. Missionen/Boss-
  Quests haben feste Vorgaben statt freier Gestaltung, Bonus-Teile sind ungeprüft — ggf. eine
  ungeprüfte "Freestyle"-Aufgabe pro Woche ergänzen. Vergleiche mit `>` (Boolean-Kapitel Woche 2)
  werden für "Sieger/über Durchschnitt" genutzt, weil `if` erst in Woche 3 kommt — bewusst so.
- **Woche 4:** Debug Bug #1 war im Original eine Endlosschleife (5s-Timeout), jetzt Off-by-one —
  bewusst so. `input()`-Beispiele (Zugangscodes/Passwort/Futter-Abfrage) nicht übernommen — die
  `stdin`-Validierung gibt es jetzt (`validation.stdin`), die Aufgaben selbst sind noch nicht
  (wieder) ergänzt.
- **Woche 5:** Vorgriffe im Original (Listen/Dictionaries/`random`/`try-except`/`help()`) wurden
  ersetzt und größtenteils in späteren Wochen nachgezogen (Listen → Woche 6, Dictionaries →
  Woche 8, `random` → Woche 7). Themenbezeichner zwischen DE/EN nicht gleich (DE
  `berechne_schaden`, EN `calculate_damage`) — bewusst, wie in Woche 4. Debug-Bugs sind die drei
  typischen Funktionsfehler (Einrückung, fehlende Klammern, fehlendes `return`) — bewusst so.
- **Woche 6:** wurde aus einem gemeinsamen Skelett + Themen-Vokabular erzeugt (Generator nur im
  Scratchpad, nicht im Repo) — Texte sind daher zwischen den Themen strukturell gleich, nur
  Vokabular/Geschichte unterscheiden sich. Gilt genauso für Woche 7–12 (s.u.).
- **Woche 7:** Zufalls-Aufgaben prüfen nur Eigenschaften (Bereich, Anzahl), nie feste Werte; dass
  `random` wirklich benutzt wird, bleibt ungeprüft. Aus dem Original weggelassen:
  `time.sleep()`-Rituale, `random.uniform`-Ausgaben mit `:.3f`, `tan`/Logarithmen, `math.tau`/`inf`,
  `input()` im Namens-Orakel/Dungeon-Bonus.
- **Woche 8:** Aus dem Original weggelassen: verschachteltes Questsystem mit Tupel-Belohnungen/
  Tupel als Dictionary-Schlüssel als Aufgabe (nur als Erklärung in Lektion 7), Tupel-Methoden
  `index()`/`count()`, Bonus-Teile ungeprüft (Grund: `output_contains` prüft nur feste Ausgaben).
- **Woche 9:** `input()`-Aufgaben aus dem Original (Boss 1 Tagebuch) durch vorgegebene Einträge
  ersetzt, `input()` nur als Bonus — als Aufgabe mit `validation.stdin` nachziehen. Dateien liegen
  im Pyodide-Dateisystem und bleiben zwischen Aufgaben bestehen; jede Aufgabe schreibt ihre Dateien
  deshalb selbst (ob das Dateisystem beim Kernel-Neustart geleert wird, nicht separat geprüft). Aus
  dem Original weggelassen: `f.writelines()`, `json.dumps(indent=2)`-Ausgabe als Prüfung,
  `csv.DictWriter` mit `extrasaction`, `with open(..., "x")`.
- **Woche 10–12:** Woche 2 DE/EN-Angleichung läuft bereits, siehe "Laufend" oben. Woche 12 ist in
  7 Etappen mit kleinen, einzeln geprüften Aufgaben statt einem durchlaufenden Spiel-Notebook;
  Kampf-Aufgaben nutzen 1-HP-Gegner für deterministische Prüfung. Aus den Originalen weggelassen:
  Operator-Polymorphismus mit `__add__`, `__getitem__`, `input()`-Befehlsschleife in Woche 12
  (Befehle stehen als Liste, bräuchte `stdin`-Validierung), Bonus-Teile ungeprüft.

---

## Nächste Themen (je eigener Branch von `main`)

Reihenfolge empfohlen: 1 → 2. Nicht mischen. (Branch-Namen ohne `cursor/`-Präfix.)
Gesamt-Roadmap/Track-Modell (welche Sprache/welches Thema baut auf was auf) siehe `VISION.md`.
JavaScript-Spielewerkstatt (früher Punkt 1) ist bereits gemergt (Details in
`docs/archiv/todo-erledigt.md`).

### 1. Python-Projekt-Sprints — Branch `kurs-python-projekte`
Die Infrastruktur dafür existiert bereits: generalisiertes `ProjectCourse.vue`, Projekte-Übersicht
mit Filtern unter `/projekte`. Ein weiteres Projekt braucht nur noch einen Content-Ordner +
`kurse.json`-Eintrag (siehe `INHALTE.md` §6), keine neue Komponente.
- [ ] 2–3 weitere Projekt-Ideen ausarbeiten (Sprints im Cäsar-Chiffre-Stil, ~5 Lektionen) —
      Ideen-Backlog mit ~40 Vorschlägen (Spiele, Web, KI, Logik, Krypto, Kreativ, Daten) samt
      Reihenfolge-Empfehlung in `PROJEKTIDEEN.md`; beim Umsetzen dort abhaken
- [ ] Projektideen aus Einstufung ggf. hier ausbauen
- [ ] DE (+ EN nach Bedarf)
- [ ] Smoke-Test → PR nach `main`

### 2. KI-Labor — Branch `kurs-ki-labor`
Baut auf dem Python-Track auf (12-Wochen-Grundkurs), siehe `VISION.md`/`KURSPLAN.md` Kurs 4
"KI-Grundlagen". Breitere Zielgruppe, Fokus auf Prompts/Grenzen/Schul-Nutzen.
- [ ] Kursmetadaten + Content
- [ ] Smoke-Test → PR nach `main`

**Hinweis:** Zweites Thema erst starten, wenn das erste gemerged ist (oder bewusst parallel nur
wenn Kapazität klar ist).
