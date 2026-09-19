## 🎯 Übung 2: range(start, ende)

Mit zwei Zahlen sagst du `range()`, wo es **anfängt** und wo es **aufhört**:

```python
for hurde in range(3, 8):
    print(f"Hürde {hurde}: Sprung!")
```

Das gibt die Hürden 3, 4, 5, 6 und 7 aus.

> 🐴 **Wichtig:** Der Start ist dabei, das Ende **nicht**! `range(3, 8)` geht von 3 bis **vor** 8 – wie ein Reitplatz, der bei Hürde 7 aufhört.

Die drei Formen von `range()` bisher:
- `range(n)` → 0 bis n-1
- `range(start, ende)` → start bis ende-1
