# 🪜 Schrittweite und rückwärts zählen

Manchmal willst du nicht jede Zahl, sondern nur **jede zweite** oder **jede fünfte**. Dafür gibt es die **dritte Zahl** in `range()` – die Schrittweite:

```python
for gerade in range(0, 11, 2):
    print(f"Gerade Zahl: {gerade}")
```

Das gibt `0, 2, 4, 6, 8, 10` aus.

**Rückwärts** zählst du mit einer **negativen** Schrittweite:

```python
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 Start!")
```

| Form | Bedeutung |
|------|-----------|
| `range(n)` | 0 bis n-1 |
| `range(start, ende)` | start bis ende-1 |
| `range(start, ende, schritt)` | mit Abstand `schritt` |

Auch hier gilt: Das **Ende ist exklusiv**. Beim Rückwärtszählen hört `range(5, 0, -1)` bei 1 auf.
