# Listen

Listen sind geordnete, veränderliche Sammlungen. Index beginnt bei 0.

```python
todos = ["Code schreiben", "Testen", "Deployen"]
todos.append("Dokumentieren")
print(len(todos))   # 4
print(todos[0])     # "Code schreiben"
print(todos[-1])    # "Dokumentieren"
```

"Geordnet" bedeutet, die Reihenfolge der Elemente bleibt erhalten, so wie du sie eingefügt hast. "Veränderlich" (mutable) heißt: du kannst eine Liste nach dem Erstellen noch verändern – Elemente hinzufügen, entfernen oder überschreiben – ohne eine neue Liste anzulegen. Das unterscheidet Listen z.B. von Strings, die unveränderlich (immutable) sind.

Der negative Index `-1` zeigt immer auf das letzte Element, `-2` auf das vorletzte usw. – praktisch, wenn du die Länge der Liste nicht kennst oder sie sich noch ändern kann.

Nützliche Methoden: `.append(x)` fügt am Ende hinzu, `.remove(x)` entfernt das erste Vorkommen von `x`, `.sort()` sortiert die Liste **an Ort und Stelle** (verändert sie direkt, statt eine neue zurückzugeben), `len()` liefert die Anzahl der Elemente. Auch Slicing funktioniert wie bei Strings: `todos[0:2]` liefert die ersten beiden Einträge als neue Liste.
