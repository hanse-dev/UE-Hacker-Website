# ⚖️ Lesson 2: Comparison operators

Conditions usually come from **comparisons**. A comparison always gives `True` or `False`.

## `=` or `==`?

This is a crucial difference!

- **`=`** **assigns** a value to a variable: `age = 10`
- **`==`** **compares** two values for equality: `age == 10`

```python
age = 10          # assignment
if age == 10:     # comparison
    print("The horse is 10 years old!")
```

> 🐴 **Remember:** In a condition always use `==` for comparisons, never `=`!

## The six comparison operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal to | `age == 10` |
| `!=` | not equal to | `gait != "Gallop"` |
| `<` | less than | `age < 5` |
| `<=` | less than or equal | `age <= 5` |
| `>` | greater than | `age > 15` |
| `>=` | greater than or equal | `age >= 3` |

You can also print a comparison directly: `print(160 < 165)` shows `True`.
