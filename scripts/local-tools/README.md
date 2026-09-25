# Lokales Tool: Account anlegen + Thermodrucker-Ausdruck

Legt einen neuen Account auf der UE Hacker Website (Produktion) über die Admin-API an —
Benutzername frei wählbar, Passwort wird zufällig generiert — und druckt Benutzername +
Passwort direkt auf einem MXW01-Thermodrucker aus.

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
`create-account-printout.py` startet sich beim Aufruf automatisch im `venv/` neu, falls es
vorhanden ist — egal ob man es mit `python3` oder `venv/bin/python3` aufruft.

`setup-printer-tool.sh` patcht das geklonte MXW01-Tool außerdem automatisch (`patch-mxw01.py`):
Ohne Pause zwischen den kleinen Daten-Häppchen beim Senden verwirft macOS (CoreBluetooth) Bluetooth-
Writes stillschweigend — der Drucker verbindet sich zwar, druckt/fördert aber nichts und sendet auch
keine Fehlermeldung, nur ein stilles Timeout ("Warning: AA notification not received"). Falls
`vendor/` schon vor diesem Fix angelegt wurde: `python3 patch-mxw01.py` einmal manuell nachholen.

Drucker-Adresse finden: `python3 scan-bluetooth.py` (Drucker muss an/wach sein, Gerätename
"MXW01"). **Auf macOS ist das keine echte Bluetooth-MAC**, sondern eine app-spezifische
CoreBluetooth-UUID (z.B. `A652E1F0-...`) — CoreBluetooth gibt aus Datenschutzgründen keine echten
MAC-Adressen heraus. Die "echte" MAC (z.B. von der Verpackung oder einer Handy-App) funktioniert
auf macOS nicht mit `bleak`. Details siehe `vendor/mxw01/README.md` nach dem Setup.

`vendor/` und `venv/` werden von `.gitignore` ausgeschlossen (das MXW01-Tool hat keine
LICENSE-Datei im Original-Repo, daher nicht mit committen; `venv/` ist wie üblich lokal).
`.env` ist ebenfalls gitignored.

## Benutzung

```bash
python3 create-account-printout.py <benutzername> kinder      # oder: jugendliche
```

Fragt nach dem Admin-Passwort (falls nicht in `.env` gesetzt), legt den Account über
`POST /api/admin/users` an und druckt danach einen Beleg mit Benutzername, Passwort, Domain
und Datum. Mit `--no-print` nur anlegen, ohne zu drucken (z.B. zum Testen ohne Drucker in
Reichweite).

Schlägt der Druck fehl (Drucker außer Reichweite, Bluetooth-Fehler, Papier leer), muss **kein**
neuer Account angelegt werden — der zuletzt angelegte Account wird lokal gemerkt
(`.last-account.json`, gitignored, Klartext-Passwort) und lässt sich erneut drucken:

```bash
python3 create-account-printout.py --reprint
```

## Passwort-Format

Zwei zufällige deutsche Wörter + zwei Ziffern, z.B. `Igel-Zug-79` — kurz genug zum Abschreiben,
aber deutlich mehr Kombinationen als ein 4-stelliger PIN.

## Größe des Ausdrucks anpassen

`RECEIPT_FONT_SCALE` in `.env` (Default `1.2`, falls nicht gesetzt) skaliert den ganzen Ausdruck.
Benutzername/Passwort werden automatisch verkleinert, falls sie sonst über den Rahmen hinausragen
würden (z.B. bei sehr langen Benutzernamen).
