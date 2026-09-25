# Lokales Tool: Account anlegen + Thermodrucker-Ausdruck

Legt einen neuen Account auf der UE Hacker Website (Produktion) über die Admin-API an —
Benutzername frei wählbar, Passwort wird zufällig generiert — und druckt Benutzername +
Passwort direkt auf einem MXW01-Thermodrucker aus.

**Läuft nur lokal auf deinem Rechner, ist nicht Teil von Docker/Build/Deploy.**

## Setup (einmalig)

```bash
cd scripts/local-tools
./setup-printer-tool.sh                       # klont das MXW01-Tool nach vendor/mxw01
pip install -r vendor/mxw01/requirements.txt   # Pillow, bleak, matplotlib
cp .env.example .env
# .env ausfüllen: ACCOUNT_SERVER_URL, MXW01_PRINTER_ADDRESS (ADMIN_PASSWORD optional)
```

Bluetooth-MAC-Adresse des Druckers finden: Systemeinstellungen/Bluetooth-Scanner oder eine
BLE-Scanner-App, Gerät heißt "MX01W". Details siehe `vendor/mxw01/README.md` nach dem Setup.

`vendor/` wird von `.gitignore` ausgeschlossen (das MXW01-Tool hat keine LICENSE-Datei im
Original-Repo, daher nicht mit committen). `.env` ist ebenfalls gitignored.

## Benutzung

```bash
python3 create-account-printout.py <benutzername> kinder      # oder: jugendliche
```

Fragt nach dem Admin-Passwort (falls nicht in `.env` gesetzt), legt den Account über
`POST /api/admin/users` an und druckt danach einen Beleg mit Benutzername, Passwort, Domain
und Datum. Mit `--no-print` nur anlegen, ohne zu drucken (z.B. zum Testen ohne Drucker in
Reichweite).

## Passwort-Format

Zwei zufällige deutsche Wörter + zwei Ziffern, z.B. `Igel-Zug-79` — kurz genug zum Abschreiben,
aber deutlich mehr Kombinationen als ein 4-stelliger PIN.
