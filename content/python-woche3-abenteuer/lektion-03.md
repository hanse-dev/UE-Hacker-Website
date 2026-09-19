# ⚖️ Die Vergleichsrunen

Neben `==` kennt Python weitere **Vergleichsoperatoren**. Jeder liefert `True` oder `False`:

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `==` | gleich | `level == 10` |
| `!=` | **nicht** gleich | `level != 10` |
| `<` | kleiner als | `level < 10` |
| `<=` | kleiner oder gleich | `level <= 10` |
| `>` | größer als | `level > 10` |
| `>=` | größer oder gleich | `level >= 10` |

```python
wert = 10
print(wert < 15)    # True
print(wert <= 10)   # True
print(wert > 5)     # True
print(wert >= 11)   # False
print(wert != 10)   # False
```

Der Unterschied zwischen `>` und `>=` ist wichtig: Bei `gold > kosten` reicht *genau* gleich viel Gold nicht aus, bei `gold >= kosten` schon!
