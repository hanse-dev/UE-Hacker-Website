# 🔍 Übung 5: Suchen und zählen

```python
pferde = ["Sturmwind", "Blitz", "Sturmwind", "Luna", "Sturmwind", "Fuchs"]
print("Blitz" in pferde)          # True – ist der Eintrag drin?
print("Nova" in pferde)          # False
print(pferde.index("Blitz"))      # Position des ersten Treffers
print(pferde.count("Sturmwind"))      # wie oft kommt er vor?
```

- **`x in liste`** ergibt `True` oder `False` – ideal für `if`
- **`liste.index(x)`** liefert die **Position** des ersten Treffers (gibt es `x` nicht, kommt ein Fehler – prüfe vorher mit `in`)
- **`liste.count(x)`** zählt, **wie oft** `x` vorkommt
- Das Wort **`in`** funktioniert auch bei Text: `"Gold" in "Goldmünze"` ist `True`
- **`set(liste)`** entfernt **Doppelte**, hat aber keine feste Reihenfolge – `sorted(set(liste))` liefert die Einträge ohne Doppelte in alphabetischer Reihenfolge
