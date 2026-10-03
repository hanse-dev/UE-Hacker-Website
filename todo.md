# Todo

Erledigtes (frühere Abschnitte "Now" + "Fertige Branches") steht kalt in `docs/archiv/todo-erledigt.md` —
nicht per `@` geladen, nur bei Bedarf lesen. Hier stehen nur **offene** Punkte und die nächsten Themen.

## Offen

- [ ] Rechtschreib- und Verständnisprüfung aller deutschen Inhalte (Branch `inhalts-pruefung`,
      HANDOFF 3.98). Mechanischer Pass erledigt (`lint:spelling` + `lint:spelling:de` beide bei 0).
      Lese-Pass (Grammatik, Kommas, Verständlichkeit ab 10/11 Jahren, Aufgabe passt zum `expected`)
      Paket für Paket: ~~Interaktiv-Kurs~~, ~~Woche 1–5 (alle Themen)~~, ~~Woche 6–12~~ (erledigt:
      Abenteuer voll, Pferde/Sci-Fi Geschichten-Texte + LanguageTool) → Wochen-Checks → JS-Grundkurs → Projekt-Kurse → KI-Labor →
      UI-Texte/`kurse.json`/Glossar. EN nur für inhaltliche Korrekturen nachziehen.
      Offene Urteilsfragen aus Paket 3 (Woche 6–12; berühren Code/`expected`/Lösung/EN):
      - Themen-Reste aus dem Abenteuer-Skelett in Pferde und Sci-Fi: Woche 6 Mission 3 Variable
        `gilde` (Reitgruppe/Crew); Woche 7 Boss 3 `monster`/"Dungeon"/"Held" beim
        "Zufalls-Ausritt"/"Zufalls-Sektor"; Woche 9 Boss 3 `questlog`/"Quests"; Woche 10 Boss 2
        "Das Duell" mit `greife_an` (bei Pferden greifen sich Pferde an). Vorschlag: je Thema
        eigene Bezeichner/Geschichte, bei den Pferden statt Duell ein Wettrennen.
      - Woche 12 mischt deutsche und englische Bezeichner (`room_name`, `action`, `target`,
        `foe`, `data`, `amount`, `commands`, `goal_item`, `parse`) — sonst ist der Kurs deutsch.
      - Woche 7 Lektion 7 erwähnt Winkelfunktionen/Bogenmaß und nutzt Fakultät — für 10/11-Jährige
        Stoff aus höheren Klassen; Vorschlag: Satz zu `sin`/`cos`/`tan` streichen.
      Offene Urteilsfragen aus Paket 2 (Nutzer entscheidet, ändern Ausgaben/`expected`/Lösung/EN):
      - Woche 2 Boss 3, alle Themen: rechnet mit "Erfolgswahrscheinlichkeit (0–1)" und
        Erwartungswert — für 10/11-Jährige schwer. Sci-Fi rechnet zudem "Kosten ×
        Wahrscheinlichkeit = erwarteter Erfolg" und nennt die teurere Mission "rentabler"
        (inhaltlich falsch). Vorschlag: Sci-Fi auf "Forschungsertrag" statt "Kosten" umstellen.
      - Woche 2 Sci-Fi hat keine `input()`-Lektion (Abenteuer/Pferde: Lektion 9) und Boss 2 nutzt
        neuronale Netze/Parameter/Genauigkeit als Thema.
      - Woche 3 Pferde Boss 2 "Level 5 – Abmeldung": unklarer Begriff, steckt im `expected`.
      - Woche 1 Abenteuer Boss 1: Geschichte ("Gedicht entschlüsseln") passt nicht zur Aufgabe
        (eigene Sätze schreiben).
      - Für spätere Pakete vorgemerkt: Ausgabetexte ohne Umlaute `Koeln` (`js-grundkurs-woche5`)
        und `Saeugetier` (KI-Labor Woche 2–4, Label in den Daten).
      Offen aus Paket 1:
      - Interaktiv-Kurs EN (`-kinder-en`/`-jugendliche-en`) ist deutlich kürzer als DE (3 statt 6
        Aufgaben, kurze Texte, seit 3.79/3.85 nur DE erweitert) — gehört zum offenen EN-Thema.
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
  bewusst so. `input()`-Aufgabe (Zugangscode/Futter-Abfrage/Docking-Code) mit `validation.stdin`
  je Thema als letzter Boss-3-Schritt nachgezogen (DE+EN, mit `python3` geprüft) — erledigt.
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
- **Woche 9:** `input()`-Aufgabe (Boss 1 Tagebuch, "Eigener Eintrag") mit `validation.stdin` als
  vierter Schritt je Thema nachgezogen (DE+EN, mit `python3` geprüft) — erledigt. Dateien liegen
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
KI-Labor (8 Wochen) und die Python-Projekt-Sprints (Vigenère-Chiffre, Snake, Text-Adventure) sind
bereits gemergt (Details in `docs/archiv/todo-erledigt.md`). Nächstes Thema noch nicht entschieden
(siehe `VISION.md` "Offene Fragen"); Ideen-Backlog in `PROJEKTIDEEN.md`, DE-first (EN-Versionen
siehe "Offen" oben).
