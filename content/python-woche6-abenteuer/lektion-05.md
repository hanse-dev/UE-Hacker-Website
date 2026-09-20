# 🔍 Sammlungs-Zauber 5: Suchen und zählen

```python
schaetze = ["Gold", "Kristall", "Gold", "Amulett", "Gold", "Krone"]
print("Kristall" in schaetze)          # True – ist der Eintrag drin?
print("Rubin" in schaetze)          # False
print(schaetze.index("Kristall"))      # Position des ersten Treffers
print(schaetze.count("Gold"))      # wie oft kommt er vor?
```

- **`x in liste`** ergibt `True` oder `False` – ideal für `if`
- **`liste.index(x)`** liefert die **Position** des ersten Treffers (gibt es `x` nicht, kommt ein Fehler – prüfe vorher mit `in`)
- **`liste.count(x)`** zählt, **wie oft** `x` vorkommt
- Das Wort **`in`** funktioniert auch bei Text: `"Gold" in "Goldmünze"` ist `True`
- **`set(liste)`** entfernt **Doppelte**, hat aber keine feste Reihenfolge – `sorted(set(liste))` liefert die Einträge ohne Doppelte in alphabetischer Reihenfolge
