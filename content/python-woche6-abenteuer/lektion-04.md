# ➖ Sammlungs-Zauber 4: Einträge entfernen

```python
schaetze = ["Gold", "Kristall", "Amulett", "Krone", "Ring"]
schaetze.remove("Krone")      # entfernt den ersten Eintrag mit diesem Wert
letzter = schaetze.pop()       # entfernt den LETZTEN und gibt ihn zurück
erster = schaetze.pop(0)       # entfernt den Eintrag an Index 0 und gibt ihn zurück
schaetze.clear()               # leert die ganze Liste
```

- **`remove(x)`** entfernt den ersten Eintrag mit dem **Wert** `x` (gibt es ihn nicht, kommt ein Fehler)
- **`pop()`** entfernt den **letzten** Eintrag, **`pop(index)`** den an dieser **Position** – und liefert ihn als Ergebnis zurück, du kannst ihn also in einer Variable speichern
- **`clear()`** löscht alles

> 💡 `remove` fragt nach dem **Wert**, `pop` nach der **Position**.
