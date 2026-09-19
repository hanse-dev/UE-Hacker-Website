# 📟 System Protocol 2: Comparison Operators

Conditions usually come from **comparisons**. A comparison always gives `True` or `False`.

## Assignment vs comparison: `=` and `==`

This is a crucial difference:

- **`=` (one equals sign)** assigns a value to a variable: `level = 10`
- **`==` (two equals signs)** compares two values: `if level == 10:`

> 📡 **Remember:** In conditions always use `==` to compare – never `=`!

## The comparison operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | is equal to | `command == "START"` |
| `!=` | is **not** equal to | `command != "START"` |
| `<` | less than | `energy < 20` |
| `<=` | less than or equal | `temperature <= 100` |
| `>` | greater than | `speed > 1000` |
| `>=` | greater than or equal | `shield_strength >= 50` |

```python
energy = 15
if energy < 20:
    print("Low energy!")
```

You can also simply print a comparison and you will see `True` or `False`:

```python
print(42 <= 42)   # True
```
