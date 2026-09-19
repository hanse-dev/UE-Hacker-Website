# ⚖️ The Comparison Runes

Besides `==`, Python knows more **comparison operators**. Each one gives `True` or `False`:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal | `level == 10` |
| `!=` | **not** equal | `level != 10` |
| `<` | less than | `level < 10` |
| `<=` | less than or equal | `level <= 10` |
| `>` | greater than | `level > 10` |
| `>=` | greater than or equal | `level >= 10` |

```python
value = 10
print(value < 15)    # True
print(value <= 10)   # True
print(value > 5)     # True
print(value >= 11)   # False
print(value != 10)   # False
```

The difference between `>` and `>=` matters: with `gold > cost`, having *exactly* as much gold is not enough, with `gold >= cost` it is!
