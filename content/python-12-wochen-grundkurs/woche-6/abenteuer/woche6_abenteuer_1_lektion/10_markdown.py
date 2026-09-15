"""## Sammlungs-Zauber 3: Listen durchsuchen und sortieren

**Suchen und prüfen:**
- `index(element)` – gibt die Position des Elements zurück
- `element in liste` – prüft ob Element vorhanden (`True`/`False`)
- `count(element)` – zählt wie oft ein Element vorkommt
- `len(liste)` – gibt die Anzahl der Elemente zurück

**Sortieren:**
- `sort()` – sortiert die Liste (verändert sie direkt)
- `sorted(liste)` – gibt eine sortierte Kopie zurück
- `reverse()` – dreht die Reihenfolge um

**Mit Index und Wert gleichzeitig:**
- `enumerate(liste)` – liefert in einer `for`-Schleife immer **Index und Wert** als Paar:

```python
for index, element in enumerate(liste):
    print(f\"Position {index}: {element}\")
```"""
