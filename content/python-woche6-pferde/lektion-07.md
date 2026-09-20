# 🔁 Übung 7: Listen und Schleifen

Eine `for`-Schleife läuft direkt durch die **Einträge** einer Liste (ohne `range`):

```python
pferde = ["Sturmwind", "Blitz", "Luna"]
for eintrag in pferde:
    print(eintrag)

for nr, eintrag in enumerate(pferde):
    print(nr, eintrag)      # 0 Sturmwind, 1 Blitz, ...
```

- **`for eintrag in liste:`** – `eintrag` ist bei jedem Durchlauf der nächste Eintrag
- **`enumerate(liste)`** liefert zusätzlich die **Position** (`nr` beginnt bei 0)
- Mit einer Schleife kannst du **rechnen**: Summe bilden, zählen, das Größte suchen

**Listen in Funktionen:** Übergibst du eine Liste an eine Funktion, arbeitet die Funktion mit **derselben** Liste. Ein `append` in der Funktion verändert also auch die Liste **außerhalb** – ein `return` ist dafür nicht nötig.
