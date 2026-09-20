# 🐴 Übung 4: Dictionaries durchlaufen

Mit einer `for`-Schleife gehst du alle Einträge durch. Drei Methoden liefern, was du brauchst:

| Methode | Liefert | Beispiel |
|---|---|---|
| `.keys()` | alle Schlüssel | `for k in d.keys()` |
| `.values()` | alle Werte | `for v in d.values()` |
| `.items()` | Schlüssel **und** Wert | `for k, v in d.items()` |

```python
futter = {"Hafer": 3, "Heu": 5, "Möhren": 2}
for name, anzahl in futter.items():
    print(name, anzahl)

gesamt = 0
for anzahl in futter.values():
    gesamt += anzahl
```

`for name in dict` läuft ohne Zusatz über die **Schlüssel**. `.items()` ist am nützlichsten: du bekommst beides auf einmal.
