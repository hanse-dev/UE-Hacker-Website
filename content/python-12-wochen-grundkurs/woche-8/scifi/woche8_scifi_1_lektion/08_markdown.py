"""### 🛡️ Fehler abfangen mit try/except

Wenn du versuchst, ein unveränderliches Tupel zu verändern, wirft Python einen `TypeError`. Mit `try`/`except` fängst du solche Fehler ab, statt dass dein Programm abstürzt:

```python
try:
    tupel[0] = \"Neu\"        # Code, der einen Fehler auslösen könnte
except TypeError as e:
    print(f\"Fehler: {e}\")   # Was passiert, wenn der Fehler auftritt
```"""
