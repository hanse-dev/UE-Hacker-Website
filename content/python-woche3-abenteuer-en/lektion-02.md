# ⚖️ Comparison Operators

Conditions are built from **comparisons**. A comparison gives an Air element: `True` or `False`.

## Assignment vs comparison: `=` vs `==`

This is a crucial difference:

- **`=` (one equals sign)** *assigns* a value to a variable:
  ```python
  level = 10      # level now holds 10
  ```
- **`==` (two equals signs)** *compares* two values:
  ```python
  if level == 10:   # is level equal to 10?
      print("Level 10 reached!")
  ```

> ⚠️ In a condition always use `==`, never `=`!

## The comparison runes

| Rune | Meaning | Example | Result (level = 10) |
|------|---------|---------|---------------------|
| `==` | equal | `level == 10` | `True` |
| `!=` | not equal | `level != 10` | `False` |
| `<` | less than | `level < 15` | `True` |
| `<=` | less than or equal | `level <= 10` | `True` |
| `>` | greater than | `level > 5` | `True` |
| `>=` | greater than or equal | `level >= 10` | `True` |

You can print a comparison directly to see its result:

```python
value = 10
print(f"{value} < 15: {value < 15}")
```

And you can use it in a condition, of course:

```python
gold = 100
cost = 80
if gold > cost:
    print(f"Purchase possible! Remaining: {gold - cost}")
```
