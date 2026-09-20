# 🐴 Übung 7: CSV mit DictReader und Formate wechseln

Mit **`DictWriter`** und **`DictReader`** arbeitest du mit **Spaltennamen** statt mit Positionen – jede Zeile ist ein Dictionary aus Woche 8:

```python
import csv

felder = ["name", "rasse", "alter", "punkte"]
with open("pferde.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=felder)
    w.writeheader()               # schreibt die Kopfzeile
    w.writerows(pferde)           # Liste von Dictionaries

with open("pferde.csv", "r") as f:
    for zeile in csv.DictReader(f):
        print(zeile["name"])       # Zugriff über den Spaltennamen
```

**Formate wechseln:** JSON und CSV enthalten dieselben Daten in unterschiedlicher Form. Du liest in einem Format ein (Liste von Dictionaries im Speicher) und schreibst im anderen wieder aus. Denke daran: aus CSV kommen alle Werte als Text – Zahlen wandelst du mit `int()` um.
