# 🔁 Datenprotokoll 7: Listen und Schleifen

Eine `for`-Schleife läuft direkt durch die **Einträge** einer Liste (ohne `range`):

```python
module = ["Antrieb", "Sensor", "Schild"]
for eintrag in module:
    print(eintrag)

for nr, eintrag in enumerate(module):
    print(nr, eintrag)      # 0 Antrieb, 1 Sensor, ...
```

- **`for eintrag in liste:`** – `eintrag` ist bei jedem Durchlauf der nächste Eintrag
- **`enumerate(liste)`** liefert zusätzlich die **Position** (`nr` beginnt bei 0)
- Mit einer Schleife kannst du **rechnen**: Summe bilden, zählen, das Größte suchen

**Listen in Funktionen:** Übergibst du eine Liste an eine Funktion, arbeitet die Funktion mit **derselben** Liste. Ein `append` in der Funktion verändert also auch die Liste **außerhalb** – ein `return` ist dafür nicht nötig.
