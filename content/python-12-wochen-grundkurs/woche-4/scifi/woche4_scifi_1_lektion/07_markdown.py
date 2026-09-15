"""## 🔍 Das Geheimnis von range() - Der Zeit-Generator

**range() ist dein mächtigstes Werkzeug für Zeit-Sequenzen!**

### Die drei Formen von range():

1. **`range(n)`** - Zahlen von 0 bis n-1
   ```python
   range(5) → 0, 1, 2, 3, 4
   ```

2. **`range(start, ende)`** - Zahlen von start bis ende-1
   ```python
   range(2, 7) → 2, 3, 4, 5, 6
   ```

3. **`range(start, ende, schritt)`** - Zahlen mit Abständen
   ```python
   range(1, 10, 2) → 1, 3, 5, 7, 9
   ```

**Wichtige Regeln:**
- Die **obere Grenze ist immer exklusiv** (wird nicht mitgezählt)
- **Negative Schritte** sind möglich für rückwärts zählen
- range() ist **sehr speichereffizient** (erzeugt Zahlen erst bei Bedarf)"""
