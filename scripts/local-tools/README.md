# Lokales Tool: Thermodrucker (`drucker.py`)

Ein Skript für alles, was auf dem MXW01-Thermodrucker landet:

- **Account:** legt über die Admin-API einen Account auf der UE Hacker Website (Produktion) an —
  Benutzername frei wählbar, Passwort wird zufällig generiert. Gibt es den Account schon, fragt
  das Skript, ob das Passwort neu gesetzt werden soll (Passwort vergessen). In beiden Fällen
  entsteht ein Zugangsausweis mit Benutzername + Passwort.
- **Gespeicherte Ausdrucke:** Jeder Ausdruck liegt als Bild unter `ausdrucke/` und lässt sich
  aus einer Liste auswählen und erneut drucken.
- **Forscher-Tabelle:** druckt die Tabelle aus Stufe 8 des micro:bit-Kurses („Die Linie sehen“)
  zum Ausfüllen.
- **Bluetooth-Scan:** findet die Adresse des Druckers.

**Läuft nur lokal auf deinem Rechner, ist nicht Teil von Docker/Build/Deploy.**

## Setup (einmalig)

```bash
cd scripts/local-tools
./setup-printer-tool.sh   # klont das MXW01-Tool nach vendor/mxw01, legt venv/ an, installiert Pillow/bleak/matplotlib
cp .env.example .env
# .env ausfüllen: ACCOUNT_SERVER_URL, MXW01_PRINTER_ADDRESS (ADMIN_PASSWORD optional)
```

`setup-printer-tool.sh` legt ein eigenes virtuelles Environment (`venv/`) an, weil macOS/Homebrew-
Python systemweite `pip install`s verweigert (PEP 668, `externally-managed-environment`).
`drucker.py` startet sich beim Aufruf automatisch im `venv/` neu, falls es
vorhanden ist — egal ob man es mit `python3` oder `venv/bin/python3` aufruft.

`setup-printer-tool.sh` patcht das geklonte MXW01-Tool außerdem automatisch (`patch-mxw01.py`):
Ohne Pause zwischen den kleinen Daten-Häppchen beim Senden verwirft macOS (CoreBluetooth) Bluetooth-
Writes stillschweigend — der Drucker verbindet sich zwar, druckt/fördert aber nichts und sendet auch
keine Fehlermeldung, nur ein stilles Timeout ("Warning: AA notification not received"). Falls
`vendor/` schon vor diesem Fix angelegt wurde: `python3 patch-mxw01.py` einmal manuell nachholen.

Drucker-Adresse finden: `python3 drucker.py scan` (Drucker muss an/wach sein, Gerätename
"MXW01"). **Auf macOS ist das keine echte Bluetooth-MAC**, sondern eine app-spezifische
CoreBluetooth-UUID (z.B. `A652E1F0-...`) — CoreBluetooth gibt aus Datenschutzgründen keine echten
MAC-Adressen heraus. Die "echte" MAC (z.B. von der Verpackung oder einer Handy-App) funktioniert
auf macOS nicht mit `bleak`. Details siehe `vendor/mxw01/README.md` nach dem Setup.

`vendor/` und `venv/` werden von `.gitignore` ausgeschlossen (das MXW01-Tool hat keine
LICENSE-Datei im Original-Repo, daher nicht mit committen; `venv/` ist wie üblich lokal).
`.env` ist ebenfalls gitignored.

## Benutzung

Ohne Argumente startet ein Menü, das nach allem Nötigen fragt:

```bash
python3 drucker.py
```

```
UE Hacker – Thermodrucker
  1  Account: anlegen oder Passwort neu setzen
  2  Gespeicherten Ausdruck drucken
  3  Forscher-Tabelle drucken (micro:bit, Stufe 8)
  4  Drucker suchen (Bluetooth-Scan)
  0  Beenden
```

Ein Fehler (Drucker aus, falsches Admin-Passwort) beendet nur die Aktion, das Menü bleibt offen.
Nach dem Admin-Passwort fragt das Menü nur einmal.

Jede Aktion gibt es auch direkt als Unterbefehl (`python3 drucker.py <befehl> --help` zeigt alle
Optionen):

```bash
python3 drucker.py account <benutzername>          # anlegen oder Passwort neu setzen (fragt nach)
python3 drucker.py account <benutzername> kinder   # Altersgruppe für einen neuen Account gleich mitgeben
python3 drucker.py account <benutzername> --reset  # Passwort ohne Rückfrage neu setzen
python3 drucker.py ausdrucke                       # gespeicherten Ausdruck auswählen und drucken
python3 drucker.py tabelle -n 6                    # sechs Tabellen am Stück, mit Schnittlinien
python3 drucker.py scan                            # Drucker-Adresse suchen
```

`account` und `tabelle` kennen `--no-print`: Das Bild wird nur unter `ausdrucke/` gespeichert,
nicht gedruckt — praktisch zum Prüfen ohne Drucker in Reichweite.

### Account anlegen oder Passwort neu setzen

Fragt nach dem Admin-Passwort (falls nicht in `.env` gesetzt) und schaut in der Nutzerliste nach,
ob es den Benutzernamen schon gibt (Groß-/Kleinschreibung egal):

- **Neu:** fragt nach der Altersgruppe, legt den Account über `POST /api/admin/users` an und
  druckt den Zugangsausweis mit Benutzername, Passwort, Domain und Datum.
- **Schon vorhanden:** fragt, ob das Passwort neu gesetzt werden soll (Default: nein). Bei „ja“
  setzt das Skript über `PATCH /api/admin/users/:id` ein neues Zufallspasswort und druckt einen
  neuen Ausweis; das alte Passwort gilt danach nicht mehr. Bei „nein“ passiert nichts — das alte
  Passwort lässt sich nicht auslesen, auf dem Server liegt nur ein Hash.

Fehlt die Drucker-Adresse oder das MXW01-Tool, bricht das Skript ab, **bevor** etwas angelegt oder
geändert wird.

Passwort-Format: zwei zufällige deutsche Wörter + zwei Ziffern, z.B. `Igel-Zug-79` — kurz genug
zum Abschreiben, aber deutlich mehr Kombinationen als ein 4-stelliger PIN.

`RECEIPT_FONT_SCALE` in `.env` (Default `1.2`, falls nicht gesetzt) skaliert den ganzen Ausweis.
Benutzername/Passwort werden automatisch verkleinert, falls sie sonst über den Rahmen hinausragen
würden (z.B. bei sehr langen Benutzernamen).

### Gespeicherte Ausdrucke

Jeder Ausweis und jede Tabelle wird vor dem Drucken als PNG unter `ausdrucke/` gespeichert, z.B.
`2026-10-13_195940_account_lina.png` oder `…_passwort-neu_lina.png`. Schlägt der Druck fehl
(Drucker außer Reichweite, Papier leer), ist also nichts verloren: `python3 drucker.py ausdrucke`
zeigt die 20 neuesten Bilder zur Auswahl, `python3 drucker.py ausdrucke <datei>` druckt eines direkt.

**Die Ausweise enthalten Passwörter im Klartext.** `ausdrucke/` ist gitignored; alte Bilder
einfach im Finder löschen. Nach einem Passwort-Reset gilt nur noch der neueste Ausweis des Accounts.

### Forscher-Tabelle

Auf dem Ausdruck stehen der Stufentitel, eine Zeile für den Teamnamen, die vier Fälle und je ein
leeres Feld für die angezeigte Zahl. Die Zeilen liest das Skript aus
`content/microbit-auto/lektion-09.md`. `--font-scale 1.2` vergrößert Schrift und Zeilenhöhe.

---

# Lokales Tool: Deutsche Rechtschreib- und Grammatikprüfung (`rechtschreibung-de/`)

`npm run lint:spelling:de` — zieht den deutschen Fließtext (ohne Code) aus `content/`,
`public/kurse.json` und `src/locales/de.js` und prüft ihn mit [LanguageTool](https://languagetool.org)
(Open Source). Läuft auf jedem System mit Docker und Python 3: beim ersten Lauf wird der Container
`ue-hacker-languagetool` gestartet (Image `erikvl87/languagetool`, ~1,2 GB, nur an `127.0.0.1`
gebunden — kein Text verlässt den Rechner). Ein Volllauf dauert etwa 6 Minuten. **Nicht Teil von
Hooks/CI/Deploy.** Ergänzt `npm run lint:spelling` (cspell), das bei Deutsch zu viel durchlässt.

- `npm run lint:spelling:de` — nur Rechtschreibung, Exit-Code 1 bei Funden. Legitime Wörter
  (Fachbegriffe, Namen) kommen in `rechtschreibung-de/erlaubt.txt`; Code-Bezeichner aus dem
  Content werden automatisch ignoriert.
- `npm run lint:spelling:de -- --grammatik` — zusätzlich Grammatik-Hinweise (Kongruenz, Kommas).
  Das sind Kandidaten zum Nachlesen, kein Gate: Wegen der Code-Bezeichner im Fließtext sind viele
  Treffer Fehlalarme; laute Regeln stehen in `STILLE_REGELN` in `pruefe.py`.
- `npm run lint:spelling:de -- --stopp` — Container wieder entfernen.
- Ohne Docker: LanguageTool anders starten (z.B. per Java) und `LANGUAGETOOL_URL` setzen.

Verständlichkeit, kaputte Sätze und Aufgaben, die nicht zur Prüfung passen, findet kein Tool
zuverlässig — dafür bleibt nur Lesen.
