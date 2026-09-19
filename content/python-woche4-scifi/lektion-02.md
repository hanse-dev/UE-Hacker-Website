# 📟 Systemprotokoll 2: range() – der Zeit-Generator

`range()` ist dein mächtigstes Werkzeug für Zeit-Folgen. Es hat drei Formen:

| Form | Zahlen | Beispiel |
|---|---|---|
| `range(n)` | 0 bis n-1 | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, ende)` | start bis ende-1 | `range(2, 7)` → 2, 3, 4, 5, 6 |
| `range(start, ende, schritt)` | mit Abständen | `range(1, 10, 2)` → 1, 3, 5, 7, 9 |

```python
for sektor in range(3, 8):
    print(f"Sektor {sektor}: Scan abgeschlossen")
```

> ⚠️ Die **obere Grenze ist nie dabei**: `range(3, 8)` hört bei 7 auf – wie Koordinaten von 3 bis *vor* 8.
