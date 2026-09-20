# 🚀 Daten-Log 4: Dictionaries durchlaufen

Mit einer `for`-Schleife gehst du alle Einträge durch. Drei Methoden liefern, was du brauchst:

| Methode | Liefert | Beispiel |
|---|---|---|
| `.keys()` | alle Schlüssel | `for k in d.keys()` |
| `.values()` | alle Werte | `for v in d.values()` |
| `.items()` | Schlüssel **und** Wert | `for k, v in d.items()` |

```python
lager = {"Batterie": 3, "Kabel": 5, "Sensor": 2}
for name, anzahl in lager.items():
    print(name, anzahl)

gesamt = 0
for anzahl in lager.values():
    gesamt += anzahl
```

`for name in dict` läuft ohne Zusatz über die **Schlüssel**. `.items()` ist am nützlichsten: du bekommst beides auf einmal.
