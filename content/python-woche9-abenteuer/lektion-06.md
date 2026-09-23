# ⚔️ Archiv-Zauber 6: CSV-Tabellen: writer und reader

**CSV** speichert eine Tabelle als Text: eine Zeile pro Tabellenzeile, die Spalten durch Kommas getrennt. Das Modul **`csv`** erledigt das Zerlegen für dich:

```python
import csv

with open("helden.csv", "w", newline="") as f:     # newline="" verhindert leere Zeilen
    schreiber = csv.writer(f)
    schreiber.writerow(["name", "level"])       # Kopfzeile
    schreiber.writerow(["Aria", 15])

with open("helden.csv", "r") as f:
    leser = csv.reader(f)
    kopf = next(leser)                     # erste Zeile überspringen
    for zeile in leser:
        print(zeile[0], zeile[1])           # jede Zeile ist eine Liste
```

> ⚠️ Beim Lesen sind **alle Werte Text**, auch Zahlen! `"15"` ist ein String – für Rechnungen brauchst du `int(zeile[1])`.
