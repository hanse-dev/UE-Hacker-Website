"""# 📖 Glossar – 🐴 Woche 9 – JSON-Dateien und I/O: Die Stall-Archive des Reiterhofs
> Dieses Notebook kannst du die ganze Woche offen lassen.

| Begriff | Bedeutung | Beispiel |
|---------|-----------|----------|
| `open()` | Datei öffnen | `open(\"datei.txt\", \"r\")` |
| `with` | Datei sicher öffnen und automatisch schließen | `with open(\"datei.txt\") as f:` |
| `\"r\"` / `\"w\"` / `\"a\"` | Lese- / Schreib- / Anhänge-Modus | `open(\"f.txt\", \"w\")` |
| `.read()` | Gesamten Datei-Inhalt als Text einlesen | `inhalt = f.read()` |
| `.readlines()` | Alle Zeilen als Liste einlesen | `zeilen = f.readlines()` |
| `.write()` | Text in Datei schreiben | `f.write(\"Hallo\")` |
| `json` | Modul für JSON-Daten (strukturierter Text) | `import json` |
| `json.load()` | JSON-Datei einlesen → Python-Dictionary | `daten = json.load(f)` |
| `json.dump()` | Python-Dictionary als JSON speichern | `json.dump(daten, f)` |
| `csv.reader` | CSV-Datei zeilenweise einlesen | `reader = csv.reader(f)` |
| `csv.writer` | Daten als CSV-Datei speichern | `writer = csv.writer(f)` |
| `FileNotFoundError` | Fehler wenn eine Datei nicht gefunden wird | `except FileNotFoundError:` |"""
