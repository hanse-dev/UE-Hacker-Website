# 📟 Systemprotokoll 3: Rückwärts zählen

Mit einer **negativen Schrittweite** zählt `range()` rückwärts – perfekt für einen Countdown zum Hypersprung:

```python
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 HYPERSPRUNG!")
```

- `range(5, 0, -1)` liefert 5, 4, 3, 2, 1 (die 0 ist *nicht* dabei)
- Die Zeile nach der Schleife ist **nicht eingerückt** – sie läuft nur einmal, nachdem die Schleife fertig ist
