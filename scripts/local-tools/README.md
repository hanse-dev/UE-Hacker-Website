# Lokale Tools

Laufen nur auf dem eigenen Rechner, sind nicht Teil von Docker/Build/Deploy.

| Ordner | Wofür | Aufruf |
|---|---|---|
| [`drucker/`](drucker/README.md) | MXW01-Thermodrucker: Accounts anlegen/zurücksetzen mit Zugangsausweis, gespeicherte Ausdrucke, Forscher-Tabelle für den micro:bit-Kurs | `python3 scripts/local-tools/drucker/drucker.py` |
| [`rechtschreibung-de/`](rechtschreibung-de/README.md) | Deutsche Rechtschreib- und Grammatikprüfung mit LanguageTool (Docker) | `npm run lint:spelling:de` |
