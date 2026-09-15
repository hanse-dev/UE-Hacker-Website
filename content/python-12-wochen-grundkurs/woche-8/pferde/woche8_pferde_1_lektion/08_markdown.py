"""### 🛡️ Fehler abfangen mit try/except

Wenn du versuchst, eine unveränderliche Daten-Kapsel zu verändern, wirft Python einen `TypeError`. Mit `try`/`except` fängst du solche Fehler ab, statt dass dein Programm abstürzt:

```python
try:
    kapsel[0] = \"Neu\"       # Code, der einen Fehler auslösen könnte
except TypeError as e:
    print(f\"Fehler: {e}\")   # Was passiert, wenn der Fehler auftritt
```"""
