# Lokales Tool: Thermodrucker (`drucker.py`)

Ein Skript für alles, was auf dem MXW01-Thermodrucker landet:

- **Account:** legt über die Admin-API einen Account auf der UE Hacker Website (Produktion) an —
  Benutzername frei wählbar, Passwort wird zufällig generiert. Gibt es den Account schon, fragt
  das Skript, ob das Passwort zurückgesetzt werden soll (Passwort vergessen). In beiden Fällen
  entsteht ein Zugangsausweis mit Benutzername + Passwort.
- **Gespeicherte Ausdrucke:** Jeder Ausdruck liegt als Bild unter `ausdrucke/` und lässt sich
  aus einer Liste auswählen und erneut drucken.
- **Forscher-Tabelle:** druckt die Tabelle aus Stufe 8 des micro:bit-Kurses („Die Linie sehen“)
  zum Ausfüllen.
- **Bluetooth-Scan:** findet die Adresse des Druckers.

**Läuft nur lokal auf deinem Rechner, ist nicht Teil von Docker/Build/Deploy.**

## Dateien

| Datei | Aufgabe |
|---|---|
| `drucker_gui.py` | Einstieg mit Fenster (tkinter): dieselben Aktionen zum Anklicken, mit Vorschau der Ausdrucke |
| `drucker.py` | Einstieg im Terminal: Menü und Kommandozeile |
| `druck.py` | Pfade, `.env`, Schriften, Ausdrucke speichern/auflisten, Bild an den Drucker schicken |
| `ausweis.py` | Admin-API (anmelden, Account suchen/anlegen/zurücksetzen) und das Ausweis-Bild |
| `tabelle.py` | Tabelle aus dem Lektionstext lesen und als Bild bauen |
| `bluetooth.py` | Bluetooth-Scan nach dem Drucker |
| `setup-printer-tool.sh`, `patch-mxw01.py` | einmaliges Setup (MXW01-Tool klonen und patchen, `venv/` anlegen) |

Nur die beiden Einstiege fragen etwas ab und zeigen etwas an. Die anderen Module liefern Werte
zurück und melden Fehler als `DruckerError`, deshalb teilen sich Fenster und Terminal dieselbe Logik.

## Setup (einmalig)

```bash
cd scripts/local-tools/drucker
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

**Lokale Dateien in diesem Ordner bleiben liegen:** `.env`, `.last-account.json`, `ausdrucke/`,
`vendor/` und `venv/` gehören hierher und sind in Ordnung so, auch wenn das Tool einzelne davon
nicht mehr liest. Nichts davon löschen, verschieben oder „aufräumen“, außer Eike sagt es ausdrücklich.

`vendor/` und `venv/` werden von `.gitignore` ausgeschlossen (das MXW01-Tool hat keine
LICENSE-Datei im Original-Repo, daher nicht mit committen; `venv/` ist wie üblich lokal).
`.env` ist ebenfalls gitignored.

## Benutzung: Fenster

```bash
python3 drucker_gui.py
```

Braucht `tkinter`; auf macOS mit Homebrew-Python einmalig `brew install python-tk@3.14` (Version
passend zum Python). Vier Reiter:

- **Account:** Benutzernamen eingeben und „Prüfen“. Gibt es ihn nicht, Altersgruppe wählen und
  anlegen; gibt es ihn schon, lässt sich das Passwort zurücksetzen (mit Rückfrage).
- **Gespeicherte Ausdrucke:** Liste (neueste zuerst) mit Vorschau; Doppelklick oder Button druckt.
- **Forscher-Tabelle:** Anzahl wählen und drucken.
- **Drucker:** eingestellte Adresse und Bluetooth-Suche.

„Nur speichern, nicht drucken“ unten links gilt für Account und Tabelle. Das Fenster bleibt während
Netz-, Bluetooth- und Druckvorgängen bedienbar; Fehler erscheinen als Meldung.

## Benutzung: Terminal

Ohne Argumente startet ein Menü, das nach allem Nötigen fragt:

```bash
python3 drucker.py
```

```
UE Hacker – Thermodrucker
  1  Account: anlegen oder Passwort zurücksetzen
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
python3 drucker.py account <benutzername>          # anlegen oder Passwort zurücksetzen (fragt nach)
python3 drucker.py account <benutzername> kinder   # Altersgruppe für einen neuen Account gleich mitgeben
python3 drucker.py account <benutzername> --reset  # Passwort ohne Rückfrage zurücksetzen
python3 drucker.py ausdrucke                       # gespeicherten Ausdruck auswählen und drucken
python3 drucker.py tabelle -n 6                    # sechs Tabellen am Stück, mit Schnittlinien
python3 drucker.py scan                            # Drucker-Adresse suchen
```

`account` und `tabelle` kennen `--no-print`: Das Bild wird nur unter `ausdrucke/` gespeichert,
nicht gedruckt — praktisch zum Prüfen ohne Drucker in Reichweite.

### Account anlegen oder Passwort zurücksetzen

Fragt nach dem Admin-Passwort (falls nicht in `.env` gesetzt) und schaut in der Nutzerliste nach,
ob es den Benutzernamen schon gibt (Groß-/Kleinschreibung egal):

- **Neu:** fragt nach der Altersgruppe, legt den Account über `POST /api/admin/users` an und
  druckt den Zugangsausweis mit Benutzername, Passwort, Domain und Datum.
- **Schon vorhanden:** fragt, ob das Passwort zurückgesetzt werden soll (Default: nein). Bei „ja“
  lässt das Skript den Server ein neues **Einmal-Passwort** erzeugen (`POST
  /api/admin/users/:id/reset-password`) und druckt einen Ausweis damit. Das bisherige Passwort gilt
  danach nicht mehr, der Account wird auf allen Geräten abgemeldet, und beim nächsten Login muss
  ein eigenes Passwort gewählt werden. Bei „nein“ passiert nichts — das alte Passwort lässt sich
  nicht auslesen, auf dem Server liegt nur ein Hash. Dasselbe geht ohne Drucker im Admin-Panel
  (Button „Passwort zurücksetzen“).

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
einfach im Finder löschen. Nach einem Passwort-Reset gilt nur noch der neueste Ausweis des Accounts, und auch der nur bis zum
ersten Login.

### Forscher-Tabelle

Auf dem Ausdruck stehen der Stufentitel, eine Zeile für den Teamnamen, die vier Fälle und je ein
leeres Feld für die angezeigte Zahl. Die Zeilen liest das Skript aus
`content/microbit-auto/lektion-09.md`. `--font-scale 1.2` vergrößert Schrift und Zeilenhöhe.

## Fallstricke für Änderungen (aus HANDOFF.md übernommen)
- IDN-Domains (Umlaute) vor jedem `urllib`-Request per `.encode('idna')` in Punycode wandeln, sonst
  kappt der Server die Verbindung ohne Fehlermeldung (3.63).
- macOS/Homebrew-Python verweigert systemweite `pip install`s (PEP 668) → eigenes `venv/`; zum
  Erkennen `sys.prefix` prüfen, nicht `Path(sys.executable).resolve()` (venv-Symlink täuscht sonst
  Identität mit System-Interpreter vor) (3.63).
- `bleak`/BLE auf macOS: CoreBluetooth liefert eine app-spezifische UUID statt der echten MAC (per
  Scan ermitteln); Writes ohne kleine Pause (~10ms) zwischen den Häppchen verwirft macOS still (3.63).
- Thermodrucker-Tool liegt in `scripts/local-tools/drucker/`: Nur `drucker.py` (Einstieg) fragt und
  gibt aus; `druck.py`/`ausweis.py`/`tabelle.py`/`bluetooth.py` liefern Werte und werfen
  `DruckerError`. Neue Aktion = Funktion im passenden Modul + Menüpunkt/Unterbefehl in `drucker.py`.
- `drucker.py` kennt ein Menü (ohne Argumente) und Unterbefehle
  `account`/`ausdrucke`/`tabelle`/`scan`); `drucker_gui.py` ist dasselbe als Fenster (tkinter, auf
  macOS `brew install python-tk@<version>`). Im Fenster läuft alles Langsame über `run_async()` in
  einem Thread — nie Tk-Widgets aus dem Thread anfassen, Ergebnisse kommen über die Queue zurück.
- `drucker.py account <name>` legt an oder setzt bei vorhandenem Account auf Rückfrage das Passwort
  zurück (`POST /api/admin/users/:id/reset-password`, Einmal-Passwort mit Zwangswechsel). Jeder Ausdruck landet als PNG in `ausdrucke/` (gitignored,
  Klartext-Passwörter) und lässt sich daraus erneut drucken.
- `drucker.py tabelle` liest die Forscher-Tabelle aus micro:bit-Stufe 8 aus `lektion-09.md`: Wer
  die Tabelle dort ändert, prüft den Ausdruck mit `--no-print` (Bild in `ausdrucke/`).
- Ohne Drucker testen: `--no-print` statt Druck; Account-Anlage gegen `node scripts/run-test-api.js`
  mit `--server-url http://localhost:<port>` (Admin-Passwort `test-admin-password`), nie gegen Produktion.
