# 🔍 range() mit Start und Ende

Die Turmwächterin zeigt dir eine Steintafel: *"Nicht jede Zählung beginnt bei null."* Mit **zwei Zahlen** in `range()` bestimmst du Anfang **und** Ende:

```python
for zahl in range(3, 8):
    print(f"Zahl: {zahl}")
```

Das gibt `3, 4, 5, 6, 7` aus.

| Schreibweise | Ergebnis |
|--------------|----------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(3, 8)` | 3, 4, 5, 6, 7 |
| `range(1, 4)` | 1, 2, 3 |

**Wichtige Regel:** Die **obere Grenze ist immer exklusiv** – sie wird nicht mehr mitgezählt. Willst du bis 10 zählen, schreibst du `range(1, 11)`.
