# 🚀 Daten-Log 6: Unveränderlich und Fehler abfangen

Wenn du ein Tupel ändern willst, wirft Python einen **TypeError**. Mit **`try`/`except`** fängst du solche Fehler ab:

```python
try:
    bauteil[1] = 99                # kann einen Fehler auslösen
except TypeError:
    print("Tupel sind unveränderlich")   # läuft nur, wenn der Fehler auftritt

print("Weiter geht es")            # läuft immer
```

**Typische Fehlerarten:**
- **`TypeError`** – z. B. ein Tupel ändern
- **`KeyError`** – ein Schlüssel fehlt im Dictionary
- **`ValueError`** – z. B. `int("zehn")`

Fange nur den Fehler ab, den du erwartest – so findest du echte Bugs weiterhin.
