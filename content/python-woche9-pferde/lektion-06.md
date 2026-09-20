# 🐴 Übung 6: CSV-Tabellen: writer und reader

**CSV** speichert eine Tabelle als Text: eine Zeile pro Tabellenzeile, die Spalten durch Kommas getrennt. Das Modul **`csv`** erledigt das Zerlegen für dich:

```python
import csv

with open("pferde.csv", "w", newline="") as f:     # newline="" verhindert leere Zeilen
    schreiber = csv.writer(f)
    schreiber.writerow(["name", "alter"])       # Kopfzeile
    schreiber.writerow(["Blitz", 8])

with open("pferde.csv", "r") as f:
    leser = csv.reader(f)
    kopf = next(leser)                     # erste Zeile überspringen
    for zeile in leser:
        print(zeile[0], zeile[1])           # jede Zeile ist eine Liste
```

> ⚠️ Beim Lesen sind **alle Werte Text**, auch Zahlen! `"8"` ist ein String – für Rechnungen brauchst du `int(zeile[1])`.
