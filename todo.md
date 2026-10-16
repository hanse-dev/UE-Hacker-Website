# Todo

Erledigtes, Zurückgestelltes und bewusste Entscheidungen stehen in `docs/archiv/todo-erledigt.md`.
Hier stehen nur **offene, aktuelle** Punkte. Diese Datei wird nicht automatisch geladen.

**Sprache:** Alles bleibt vorerst auf Deutsch (Entscheidung Eike, 14.10.2026). Englische Inhalte
werden nicht neu gebaut und nicht nachgezogen, bis Eike es anders entscheidet; die geparkten
EN-Punkte stehen im Archiv unter „Zurückgestellt: Englisch“.

## Offen

- [ ] Einmaliger Ausfall im vollen Lauf unter Last (15.10., parallel liefen Tests anderer Sessions,
      Suite 4,5 statt ~2,3 Min.): `tests/ki-labor.spec.js` Woche 3 (Python-Lauf > 10 s, Timeout pro
      Lauf seitdem 30 s), allein 3× grün. Der zweite Ausfall (Turtle-Test) ist mit 3.113 weggefallen.
      Vorschlag: Beim nächsten Auftreten prüfen, ob gleichzeitig andere Playwright-Läufe aktiv waren
      (`ps aux | grep "playwright test"`); wenn ja, Pre-push-Läufe mehrerer Sessions nicht parallel
      starten statt die Tests zu ändern.
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
- [ ] **micro:bit-Kurs „Die Ampelanlage“ (`content/microbit-ampel/`, HANDOFF 3.109) — vor dem ersten
      Termin einmal mit echten Teilen durchstecken.** Ohne Hardware entstanden und deshalb noch
      `"unlisted": true` in `kurse.json`; nach dem Test das Feld entfernen und die Kartenzahlen in
      `tests/projekte.spec.js` und `tests/microbit-*.spec.js` anpassen. Zu prüfen:
      - Startklar: Steckt der micro:bit mit den Lampen nach oben in der Platine? Sind links wirklich
        nur die 2 Löcher an der Lücke frei, und reichen Widerstandsbeine über die Lücke?
      - Leuchten alle 5 LEDs mit 150 Ω hell genug, und stimmen die Farbringe (braun-grün-schwarz-schwarz-braun)?
      - Werkstatt 1: Passt der Taster mit Beinchen in Reihe 15 und 17? Funktioniert `ziehe den Pin P15
        auf nach unten` mit 3.3V wie beschrieben? Welche Lichtstärke-Grenze passt im Raum?
      - Deutsche Namen der MakeCode-Blöcke im Editor abgleichen (aus den offiziellen Übersetzungen
        übernommen, `ändere zeit um -1` und `Erstelle eine Funktion` nicht dort nachgeschlagen).
- [ ] micro:bit-Kurs: `public/microbit/keyes_MiniCar.py` stammt aus dem Keyestudio-Download, eine
      Lizenz ist dort nicht angegeben. Vorschlag: bei Keyestudio nachfragen oder die Datei durch
      einen Link auf deren Download ersetzen (dann fehlt die Korrektur für `get_distance()`).
- [ ] Quiz-Generator (`content/js-quiz/`): Der Kurs entstand, als `dom_click_text` nur **einen** Knopf
      mehrfach klicken konnte. Deshalb prüft Lektion 7 „Nochmal spielen“ nur den Punktestand nach dem
      Neustart, und das eigene Quiz nur, dass es mit 3–10 Fragen bis zur Auswertung durchläuft (nicht,
      ob die Fragen wirklich eigene sind). Vorschlag, falls das stört: Die Klick-Liste
      aus dem Memory-Projekt (HANDOFF 3.103, `click` als Liste von IDs) nutzen und die Aufgaben schärfen.
- [ ] Backup-Cron auf dem Server einrichten bzw. prüfen, ob er läuft (Befehl siehe HANDOFF.md
      Abschnitt 4). Die Seite ist live; externe Sicherung der Backups ist bewusst nicht mitgebaut.
- [ ] Prüf-Lücken im 12-Wochen-Kurs (Lektionen prüfen nur die Ausgabe):
      - **Woche 1–2:** `output_contains` prüft pro Aufgabe nur einen String — bei mehreren
        geforderten Ausgaben (z.B. Boss 1 Schritt 1, Boss 3 Schritt 2/4 Abenteuer) und hart
        codierten `print`s bleibt eine Lücke. Vorschlag: `expectedAll` oder `variables`-Check in
        `JsLessonView`/`LessonView`.
      - **Woche 7:** Ob `random` wirklich benutzt wird, bleibt ungeprüft (geprüft werden nur
        Bereich und Anzahl).
      - **Woche 8, 10–12:** Bonus-Teile sind ungeprüft. Woche 12: Die `input()`-Befehlsschleife
        fehlt (Befehle stehen als Liste), sie bräuchte `stdin`-Validierung.
      - Missionen/Boss-Quests haben feste Vorgaben; ggf. eine ungeprüfte „Freestyle“-Aufgabe pro
        Woche ergänzen.
- [ ] Offen aus der Inhaltsprüfung der deutschen Texte (HANDOFF 3.98, Details im Archiv):
      - **Woche 2 Boss 3 (Abenteuer, Pferde)** rechnet mit Erfolgswahrscheinlichkeit und
        Erwartungswert — für 10/11-Jährige schwer; nur in Sci-Fi ist das jetzt erklärt.
      - **Woche 12 Pferde:** Das Text-Adventure hat auch im Pferde-Thema „Gegner“ und „Kampf“
        (Spielmechanik aus dem gemeinsamen Skelett) — ggf. umthematisieren.
      - **Pferde/Sci-Fi Woche 6–12:** Aufgabentexte nicht Zeile für Zeile gelesen (nur
        Geschichten-Texte + LanguageTool), Glossar nur im Abenteuer-Thema gelesen.
      - **`lint:spelling:de -- --grammatik`** meldet ~300 Hinweise, fast alles Fehlalarme durch
        Code-Bezeichner im Fließtext. Wer es schärfer will: im Extraktor Inline-Code durch ein
        Platzhalterwort ersetzen statt löschen.

## Nächste Themen (je eigener Branch von `main`)

Gesamt-Roadmap/Track-Modell siehe `VISION.md`, Ideen-Backlog in `PROJEKTIDEEN.md`. Alles Gemergte steht im Archiv.

**Web-Track** (Plan in `KURSPLAN.md`): `web-sandbox` ✅ (3.114) → `kurs-erste-website` ✅ (3.115) → `web-grundkurs` ✅ (3.116, Kurs B als Stufe „Intensiv“ in `web-erste-website`).

Offen bei „Meine erste Website“ (bewusst nicht in 3.115):
- **Eigene Seite wandert nicht mit:** Jede Aufgabe startet mit ihrer eigenen Vorlage, und Code in
  JS-/Web-Lektionen wird nicht gespeichert (Neuladen = Vorlage). Erst Lektion 8 baut die ganze Seite.
  Vorschlag: pro Web-Kurs eine gespeicherte „Meine Seite“ (`useSavedCode.js`), die Aufgaben mit
  `"startFrom": "meineSeite"` als Vorlage übernehmen — braucht Konzept, wie neue Bausteine dazukommen.
- **Sticker-Bilder** (`public/web-bilder/*.svg`) zeigen System-Emojis; auf Geräten ohne Farb-Emoji-Schrift
  (manche Linux-Rechner) erscheinen leere Kästchen. Im Unterricht prüfen; sonst gezeichnete SVGs.
