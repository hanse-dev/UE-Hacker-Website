# Todo

Erledigtes (frühere Abschnitte "Now" + "Fertige Branches") steht kalt in `docs/archiv/todo-erledigt.md` —
nicht per `@` geladen, nur bei Bedarf lesen. Hier stehen nur **offene** Punkte und die nächsten Themen.

## Offen

- [ ] `HANDOFF.md` liegt knapp über dem 25-KB-Richtwert (WORKFLOW.md). Grund: Tabellenzeilen 3.53–3.61
      in Abschnitt 3 sind noch volle Absätze statt einzeiliger "Kern in einem Satz"-Zusammenfassungen
      (Detail steht eigentlich schon in `docs/archiv/HANDOFF-historie.md`). Bei Gelegenheit auf eine
      Zeile pro Eintrag kürzen.
- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken) —
      **zurückgestellt** (Nutzer will erst später deployen). Backup-Cron auf dem Server einrichten
      (Befehl siehe HANDOFF.md Abschnitt 4); externe Sicherung der Backups bewusst nicht mitgebaut.
- [ ] Projekt-Kurse (Cäsar, Vigenère, Morsecode, Zahlen-Detektiv, JS-Spielewerkstatt, Snake,
      Text-Adventure): nur DE-Content, EN fehlt noch (`kurse.json` hat bereits `title_en` für alle 7,
      `lessons.json`/`lektion-*.md` sind nur deutsch).
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
- **Woche 10–12:** Woche 12 ist in
  7 Etappen mit kleinen, einzeln geprüften Aufgaben statt einem durchlaufenden Spiel-Notebook;
  Kampf-Aufgaben nutzen 1-HP-Gegner für deterministische Prüfung. Aus den Originalen weggelassen:
  Operator-Polymorphismus mit `__add__`, `__getitem__`, `input()`-Befehlsschleife in Woche 12
  (Befehle stehen als Liste, bräuchte `stdin`-Validierung), Bonus-Teile ungeprüft.

---

## Nächste Themen (je eigener Branch von `main`)

Gesamt-Roadmap/Track-Modell (welche Sprache/welches Thema baut auf was auf) siehe `VISION.md`.
Python-Projekt-Sprints (Vigenère-Chiffre, Snake, Text-Adventure) sind bereits gemergt (Details in
`docs/archiv/todo-erledigt.md`); weitere Ideen im Backlog `PROJEKTIDEEN.md`, DE-first (EN-Versionen
siehe "Offen" oben).

### 1. KI-Labor — Branch `kurs-ki-labor`
Baut auf dem Python-Track auf (12-Wochen-Grundkurs), siehe `VISION.md`/`KURSPLAN.md`
"KI-Track: KI-Grundlagen". 8 Wochen, ohne Themen-Varianten (wie `js-grundkurs`). Bewusst kein
scikit-learn/pandas (Wasm-Download zu schwer) und kein Live-LLM (Kosten/WebGPU) — stattdessen
k-NN, Entscheidungsbaum und ein kleines neuronales Netz komplett selbst in reinem Python gebaut.
- [x] Kursmetadaten + Grundgerüst (Wochenauswahl `KiLaborTour.vue`, `kurse.json`, Routing)
- [x] Woche 1 "Was ist KI?" (5 Lektionen + Debug + Mission + 3 Extra-Herausforderungen), `tests/ki-labor.spec.js`
- [x] Quiz + Wochen-Zertifikat (wie 12-Wochen-Kurs) — `useWeekChecks.js`/`WeekCheckPanel.vue`/
      `CodeChallenge.vue`/`useCertificatePdf.js` um `courseKey` generalisiert, eigener
      Content-Ordner `content/ki-labor-checks/`, bisher nur Woche 1 (7 Fragen + 2 Coding-Aufgaben)
- [ ] Woche 2 "Daten sind alles" (+ Extra-Herausforderungen + eigener Wochen-Check)
- [ ] Woche 3 "Nächste Nachbarn (k-NN)" (+ Extra-Herausforderungen + eigener Wochen-Check)
- [ ] Woche 4 "Training & Test" (+ Extra-Herausforderungen + eigener Wochen-Check)
- [ ] Woche 5 "Entscheidungsbäume" (+ Extra-Herausforderungen + eigener Wochen-Check)
- [ ] Woche 6 "Neuronale Netze I" (+ Extra-Herausforderungen + eigener Wochen-Check)
- [ ] Woche 7 "Neuronale Netze II" (+ Extra-Herausforderungen + eigener Wochen-Check)
- [ ] Woche 8 "Grenzen & Ethik" (+ Extra-Herausforderungen + eigener Wochen-Check)
- [ ] Smoke-Test aller Wochen → PR nach `main`
