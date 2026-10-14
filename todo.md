# Todo

Erledigtes steht in `docs/archiv/todo-erledigt.md`. Hier stehen nur **offene** Punkte und die
nächsten Themen. Diese Datei wird nicht automatisch geladen.

## Offen

- [ ] **micro:bit-Kurs „Das Roboterauto“ (`content/microbit-auto/`, HANDOFF 3.101) — vor dem ersten
      Termin am echten Auto durchspielen.** Der Kurs ist ohne Hardware entstanden (nur aus der
      Keyestudio-Doku, der MakeCode-Erweiterung und der Bibliothek abgeleitet). Zu prüfen:
      - Stufe 3/4: Ist Motor A wirklich links und `Forward` vorwärts? Passen Tempo 70 und die
        Wartezeiten (1000 ms geradeaus, 400 ms Vierteldrehung) als Startwerte?
      - Stufe 8/9: Welche Zahl meldet `Line Tracking` (angenommen: 2 = nur links Schwarz, 1 = nur
        rechts Schwarz, 3 = beide)? Reicht eine 2 cm breite Linie für beide Sensoren?
      - Stufe 6/7: Liefert `get_distance()` plausible Zentimeter, und passt die Grenze 15 cm?
      - Lektion 1: Menünamen in MakeCode und im Python-Editor (deutsche Oberfläche) stimmen mit dem
        Text überein; `keyes_MiniCar.py` lässt sich über „Projekt → Öffnen“ hinzufügen.
      - Deutsche Namen der MakeCode-Blöcke in den ```` ```bloecke ````-Listings mit dem Editor abgleichen.
- [ ] micro:bit-Kurs: `public/microbit/keyes_MiniCar.py` stammt aus dem Keyestudio-Download, eine
      Lizenz ist dort nicht angegeben. Vorschlag: bei Keyestudio nachfragen oder die Datei durch
      einen Link auf deren Download ersetzen (dann fehlt die Korrektur für `get_distance()`).
- [ ] micro:bit-Kurs: nur DE, EN fehlt. Der Kurs ist ein Projekt-Kurs (`/projekte`); sobald
      weitere micro:bit-Module dazukommen, eigenen Kurs-Typ/Übersicht erwägen (`VISION.md`).
- [ ] micro:bit-Kurs: einzelne Haken gehen beim Neuladen verloren, solange die Stufe nicht
      abgeschlossen ist (bewusst, kein neuer Storage-Key). Bei Bedarf nachrüsten, dann mit
      `contract:update`.
- [ ] Offen aus der Inhaltsprüfung (HANDOFF 3.98, Details im Archiv):
      - **EN nachziehen:** Die englischen Themen Pferde/Sci-Fi (Woche 6–10) enthalten weiter die
        Abenteuer-Reste, die in DE ersetzt wurden (`gilde`, `monster`, `questlog`, "Duell"); EN
        Woche 12 und die EN-Lösungen sind unverändert; der Interaktiv-Kurs EN ist deutlich kürzer
        als DE (3 statt 6 Aufgaben je Lektion). EN wurde sprachlich gar nicht geprüft.
      - **Woche 2 Boss 3 (Abenteuer, Pferde)** rechnet mit Erfolgswahrscheinlichkeit und
        Erwartungswert — für 10/11-Jährige schwer; nur in Sci-Fi ist das jetzt erklärt.
      - **Woche 12 Pferde:** Das Text-Adventure hat auch im Pferde-Thema "Gegner" und "Kampf"
        (Spielmechanik aus dem gemeinsamen Skelett) — bewusst so gelassen, ggf. umthematisieren.
      - **Pferde/Sci-Fi Woche 6–12:** Aufgabentexte nicht Zeile für Zeile gelesen (nur
        Geschichten-Texte + LanguageTool), Glossar nur im Abenteuer-Thema gelesen.
      - **`lint:spelling:de -- --grammatik`** meldet ~300 Hinweise, fast alles Fehlalarme durch
        Code-Bezeichner im Fließtext; die echten Treffer sind behoben. Wer es schärfer will: im
        Extraktor Inline-Code durch ein Platzhalterwort ersetzen statt löschen.
- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken) —
      **zurückgestellt** (Nutzer will erst später deployen). Backup-Cron auf dem Server einrichten
      (Befehl siehe HANDOFF.md Abschnitt 4); externe Sicherung der Backups bewusst nicht mitgebaut.
- [ ] Projekt-Kurse (Cäsar, Vigenère, Häufigkeitsanalyse, Morsecode, Zahlen-Detektiv, JS-Spielewerkstatt, Snake,
      Text-Adventure, Memory, Quiz-Generator): nur DE-Content, EN fehlt noch (`kurse.json` hat bereits
      `title_en` für alle 10, `lessons.json`/`lektion-*.md` sind nur deutsch).
- [ ] Quiz-Generator (`content/js-quiz/`): Der Kurs entstand, als `dom_click_text` nur **einen** Knopf
      mehrfach klicken konnte. Deshalb prüft Lektion 7 „Nochmal spielen“ nur den Punktestand nach dem
      Neustart, und das eigene Quiz nur, dass es mit 3–10 Fragen bis zur Auswertung durchläuft (nicht,
      ob die Fragen wirklich eigene sind). Vorschlag, falls das stört: Die Klick-Liste
      aus dem Memory-Projekt (HANDOFF 3.103, `click` als Liste von IDs) nutzen und die Aufgaben schärfen.
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
- **Themen-Vergleich (Abenteuer/Pferde/Sci-Fi, DE+EN):** Lektionen und Konzepte sind seit 3.100 in
  allen Wochen gleich. Geblieben sind nur unterschiedliche Aufgabenmengen in Debug/Missionen/
  Extra-Herausforderungen der Wochen 2–4 (Woche 3: 55/52/50 Aufgaben, Geschichten sind je Thema
  eigene) und Kleinigkeiten: `>=` in Woche 2 nur Abenteuer (Bool-Lektion), `int(input())` in
  Woche 4 Boss 3 nur Pferde, einzelne Vergleichsoperatoren in Woche 5 Mission 2/Boss 1. In Pferde/
  Sci-Fi stehen neue Lektionen mit neuer ID nicht in ID-Reihenfolge (Woche 3 `lektion-07` nach
  `lektion-01`, Woche 2 Sci-Fi `lektion-08` vor `lektion-07`) — bewusst, IDs sind der
  Fortschritts-Schlüssel.
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
