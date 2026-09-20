# 🗂️ Datenprotokoll 6: Sortieren

```python
zahlen = [5, 2, 8, 1]
zahlen.sort()                       # verändert die Liste: [1, 2, 5, 8]
absteigend = sorted(zahlen, reverse=True)   # neue Kopie: [8, 5, 2, 1]
zahlen.reverse()                    # Reihenfolge umdrehen
```

- **`liste.sort()`** sortiert die Liste **selbst** (Zahlen aufsteigend, Text nach dem Alphabet)
- **`sorted(liste)`** liefert eine **sortierte Kopie** – das Original bleibt, wie es ist
- **`reverse=True`** sortiert **absteigend**: `sort(reverse=True)`
- **`liste.reverse()`** dreht nur die aktuelle Reihenfolge um (ohne zu sortieren)
- **`sorted(liste, key=len)`** sortiert nach der **Länge** der Einträge (kürzeste zuerst) statt nach dem Alphabet

> ⚠️ Es heißt **`reverse=True`** – schreibe nicht nur `reverse` in die Klammer.
