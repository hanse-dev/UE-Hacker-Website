# Todo

Erledigtes, Zurückgestelltes und bewusste Entscheidungen stehen in `docs/archiv/todo-erledigt.md`.
Hier stehen nur **offene, aktuelle** Punkte. Diese Datei wird nicht automatisch geladen.

**Sprache:** Alles bleibt vorerst auf Deutsch (Entscheidung Eike, 14.10.2026). Englische Inhalte
werden nicht neu gebaut und nicht nachgezogen, bis Eike es anders entscheidet; die geparkten
EN-Punkte stehen im Archiv unter „Zurückgestellt: Englisch“.

## Offen

- [ ] **Verständlichkeit (Branch `verstaendlichkeit`, HANDOFF 3.123).** Bericht per
      `npm run check:verstaendlichkeit`. Die Funde „nie gezeigt“ sind behoben (0). Offen:
      lange Sätze/LIX/Fachwörter aus dem Bericht durchgehen (braucht Urteil). Stolperstellen-Zähler
      ist gebaut (HANDOFF 3.124): nach dem Deploy und ein paar Kurstagen den Admin-Reiter ansehen und
      die obersten Aufgaben überarbeiten, danach dort „Zurücksetzen“. KI-Test-Kind ist gebaut (HANDOFF 3.125). Woche 1–3 (Abenteuer) überarbeitet: 54 → 24
      lohnende Stellen, 0 wichtige. Offen: die 24 Rest-Stellen (v. a. sehr lange Aufgabensätze, z. B.
      W1 Mission 2 / W3 Lektion 7 als Liste schreiben; Bonus-Texte mit unklarem Auftrag wie W3 Mission 2/3,
      Boss 3 „Score“; W3 Boss 1: antwort_2 fehlt; Tippen von { } und ⭐), dann Woche 4–12 und die
      Themen Pferde/Sci-Fi mit `npm run testkind` prüfen.
      micro:bit (Blöcke) überarbeitet: 73 → 57 Stellen, 13 → 4 wichtige (danach noch Kreuzung und Taster
      verbessert). Offen: Rest-Stellen v. a. in den Werkstätten (Funktion mit Parametern in Ampel Stufe 2,
      Einsatzfahrzeug im Auto). `--variante python`/`javascript` (Branch `microbit-varianten`):
      Einführung und Stern überarbeitet (Tipps/Ortsangaben je Variante statt Blöcke-Sprache,
      Würfel-Lösung, Gerüste für Funk/Nachtmodus/Taster in der Ampel); Auto folgt. Neu im Editor nachklicken: Python-Editor **Öffnen** neben
      **Speichern**, .hex-Datei auf MakeCode ziehen öffnet sie, Schütteln-Knopf im Simulator. Neu eingefügte
      MakeCode-Angaben (Fortgeschritten → Erweiterungen, Pins → … mehr → Digital-Pin, Plus am wenn-Block,
      Speichern-Symbol neben dem Projektnamen) beim nächsten Termin einmal im echten Editor nachklicken.
      Test-Kind für weitere Kursarten (Projekt-Kurse Python, JS-Grundkurs, Web, KI-Labor) erweitern;
      bis dahin meldet `--geaendert` sie als „nicht geprüft“.

- [ ] Einmaliger Ausfall im vollen Lauf unter Last (15.10., parallel liefen Tests anderer Sessions,
      Suite 4,5 statt ~2,3 Min.): `tests/ki-labor.spec.js` Woche 3 (Python-Lauf > 10 s, Timeout pro
      Lauf seitdem 30 s), allein 3× grün. Der zweite Ausfall (Turtle-Test) ist mit 3.113 weggefallen.
      Vorschlag: Beim nächsten Auftreten prüfen, ob gleichzeitig andere Playwright-Läufe aktiv waren
      (`ps aux | grep "playwright test"`); wenn ja, Pre-push-Läufe mehrerer Sessions nicht parallel
      starten statt die Tests zu ändern.
      **21.10.:** wieder aufgetreten, diesmal ohne parallele Playwright-Läufe: Pre-push 21 statt 3 Min.,
      9 Ausfälle (u. a. `web-grundkurs.spec.js`, einzeln grün). Ursache war allgemeine Last auf dem
      Rechner (Load 20–33 bei 8 Kernen, ~10 GB Swap); der LanguageTool-Container belegte 1,4 GB.
      Nach `npm run lint:spelling:de -- --stopp` lief der Push sofort grün durch. Vorschlag: den
      Container nach jeder Rechtschreibprüfung stoppen; bei hoher Last (`uptime`) erst danach pushen.
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
      Termin einmal mit echten Teilen durchstecken.** Text von Eike gelesen (20.10., kein Beta mehr)
      und seit 21.10. in `/projekte` verlinkt, aber ohne Hardware entstanden. Zu prüfen:
      - Startklar: Steckt der micro:bit mit den Lampen nach oben in der Platine? Sind links wirklich
        nur die 2 Löcher an der Lücke frei, und reichen Widerstandsbeine über die Lücke?
      - Startklar mit 3.3V: Leuchtet die LED am 3.3V-Stift der Platine, sobald der micro:bit am USB
        hängt? Bleibt sie an P13 bei einem frisch ausgepackten micro:bit (Demo-Programm) wirklich dunkel?
      - Leuchten alle 5 LEDs mit 150 Ω hell genug, und stimmen die Farbringe (braun-grün-schwarz-schwarz-braun)?
      - GND-Reihen (HANDOFF 3.119): Reichen die Brückenkabel (Stecker auf Stecker) von Reihe 3 bis
        Reihe 8? Passen GND-Kabel und drei Brücken in eine Reihe mit fünf Löchern?
      - Werkstatt 1: Passt der Taster mit Beinchen in Reihe 15 und 17? Liest P20 mit `ziehe den Pin
        P20 auf nach oben` ohne Druck sicher 1 und mit Druck 0 (P19/P20 sind die I²C-Pins)? Welche
        Lichtstärke-Grenze passt im Raum?
      - Deutsche Namen der MakeCode-Blöcke im Editor abgleichen (aus den offiziellen Übersetzungen
        übernommen, `ändere zeit um -1` und `Erstelle eine Funktion` nicht dort nachgeschlagen).
        Neu: Wie heißt der Block, der einer Variable einen Pin zuweist (im Kurs `setze fuss_rot auf
        P13`), und wo findet man den Pin-Wert? Heißt der Umschalter oben im Editor „JavaScript“?
- [ ] **micro:bit-Kurs „Fang den Stern“ (`content/microbit-sterne/`, HANDOFF 3.120, Beta) — vor dem
      ersten Termin einmal am echten micro:bit durchspielen.** Python-Lösungen gegen ein nachgebautes
      `microbit`-Modul simuliert, JavaScript mit `tsc` gegen eine nachgebaute MakeCode-API geprüft,
      aber nichts lief auf dem Gerät. Zu prüfen:
      - Fühlt sich das Tempo an (Blöcke/JS 400 ms je Schritt, Python 8 × 50 ms)? Ist Fangen machbar?
      - Python: Laufen die Gerüste von Stufe 1/2 wirklich mit `index out of bounds` ab, wie im Text
        angekündigt (MicroPython `display.set_pixel` außerhalb 0–4)?
      - Startklar: Heißen Fenster und Knöpfe beim Verbinden so wie im Text („Gerät verbinden“,
        „BBC micro:bit“, „An micro:bit senden“, „Speichern“)? Block-Namen `Zeichne x … y …`/`lösche x … y …`
        (aus den offiziellen Übersetzungen) und die Kategorie „LED“ im Editor abgleichen.
      - Werkstatt: Heißt die Gesten-Auswahl im Block wirklich „nach links neigen“?
      - Einführung (`content/microbit-einfuehrung/`, gleicher Stand): Stimmt die Beschreibung der
        Rückseite (Lampe neben der USB-Buchse)? Zeigt der Simulator rechts im Editor das Programm wie
        beschrieben (Python: „Ausführen“)?
      - Nach dem Durchspielen: `beta` in `kurse.json` entfernen und die ID in `tests/kurse-beta.spec.js`
        (`NICHT_BETA`) eintragen.
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

- [ ] Aus dem früheren HANDOFF-Abschnitt 5 übernommen (16.10.2026), Stand unklar – beim nächsten Deploy prüfen:
      einmalig `docker compose exec app node api/src/scripts/import-termine-json.js`, falls die
      `termine`-Tabelle auf dem Server noch leer ist.
- [ ] Ohne Termin, braucht Entscheidung oder Rückmeldung: Interaktiv-Kurs „Ausführen vs. Prüfen“/Weiter-Flow
      (Nutzer-Feedback abwarten); EN-Versionen der Projekt-Kurse (DE-first, siehe Memory „vorerst nur
      Deutsch“); Zertifikat per E-Mail (hängt an einer Kontakt-Adresse); dritte Sprache (UI ist schon auf `t()`).

## Nächste Themen (je eigener Branch von `main`)

Gesamt-Roadmap/Track-Modell siehe `VISION.md`, Ideen-Backlog in `PROJEKTIDEEN.md`. Alles Gemergte steht im Archiv.

**Web-Track** (Plan in `KURSPLAN.md`): `web-sandbox` ✅ (3.114) → `kurs-erste-website` ✅ (3.115) → `web-grundkurs` ✅ (3.116, Kurs B als Stufe „Intensiv“ in `web-erste-website`).

Offen bei „Meine erste Website“:
- **Sticker-Bilder** (`public/web-bilder/*.svg`) zeigen System-Emojis; auf Geräten ohne Farb-Emoji-Schrift
  (manche Linux-Rechner) erscheinen leere Kästchen. Im Unterricht prüfen; sonst gezeichnete SVGs.
