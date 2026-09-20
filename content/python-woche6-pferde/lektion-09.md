# ✨ Übung 9: List Comprehension

Aus einer Liste eine **neue** Liste machen – mit Schleife und `append` sind das mehrere Zeilen. Eine **List Comprehension** schafft es in einer:

```python
schaden = [3, 7, 12, 5]
verdoppelt = [wert * 2 for wert in schaden]          # [6, 14, 24, 10]
grosse = [wert for wert in schaden if wert > 4]      # [7, 12, 5]
```

Lies sie von links nach rechts: *„Nimm `wert * 2` für jeden `wert` in `schaden`."* Ein `if` am Ende **filtert**: nur passende Einträge kommen in die neue Liste.

**Mit Text arbeiten:** `wort.upper()` macht aus einem Text **GROSSBUCHSTABEN** – das geht auch in einer Comprehension: `[w.upper() for w in liste]`.

> 💡 Die ursprüngliche Liste bleibt unverändert – du bekommst immer eine **neue** Liste.
