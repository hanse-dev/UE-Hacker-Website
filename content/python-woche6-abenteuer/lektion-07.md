# 🔁 Sammlungs-Zauber 7: Listen und Schleifen

Eine `for`-Schleife läuft direkt durch die **Einträge** einer Liste (ohne `range`):

```python
schaetze = ["Gold", "Kristall", "Amulett"]
for eintrag in schaetze:
    print(eintrag)

for nr, eintrag in enumerate(schaetze):
    print(nr, eintrag)      # 0 Gold, 1 Kristall, ...
```

- **`for eintrag in liste:`** – `eintrag` ist bei jedem Durchlauf der nächste Eintrag
- **`enumerate(liste)`** liefert zusätzlich die **Position** (`nr` beginnt bei 0)
- Mit einer Schleife kannst du **rechnen**: Summe bilden, zählen, das Größte suchen

**Listen in Funktionen:** Übergibst du eine Liste an eine Funktion, arbeitet die Funktion mit **derselben** Liste. Ein `append` in der Funktion verändert also auch die Liste **außerhalb** – ein `return` ist dafür nicht nötig.
