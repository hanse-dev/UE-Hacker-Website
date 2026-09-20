# 🔍 Datenprotokoll 5: Suchen und zählen

```python
module = ["Antrieb", "Sensor", "Antrieb", "Schild", "Antrieb", "Radar"]
print("Sensor" in module)          # True – ist der Eintrag drin?
print("Laser" in module)          # False
print(module.index("Sensor"))      # Position des ersten Treffers
print(module.count("Antrieb"))      # wie oft kommt er vor?
```

- **`x in liste`** ergibt `True` oder `False` – ideal für `if`
- **`liste.index(x)`** liefert die **Position** des ersten Treffers (gibt es `x` nicht, kommt ein Fehler – prüfe vorher mit `in`)
- **`liste.count(x)`** zählt, **wie oft** `x` vorkommt
- Das Wort **`in`** funktioniert auch bei Text: `"Gold" in "Goldmünze"` ist `True`
