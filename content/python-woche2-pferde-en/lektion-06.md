# 🐴 Lesson 6: Converting Types

Not all types can be combined directly. `"5" + 3` causes an error, because a text and a number are different hoofbeat types. The solution: **convert** the type. Python has one function for every type:

| Function | Turns the value into ... | Example | Result |
|----------|--------------------------|---------|--------|
| `int()` | a whole number | `int("5")` | `5` |
| `float()` | a decimal number | `float("4.25")` | `4.25` |
| `str()` | a text | `str(12)` | `"12"` |
| `bool()` | a truth value | `bool(0)` | `False` |

```python
age_text = "5"
age_number = int(age_text)
print(age_number + 3)     # 8
```

**Good to know about `bool()`:** `0` and the empty text `""` become `False`, everything else becomes `True`.

Only convertible things work: `int("Thunder")` causes a `ValueError`, because "Thunder" is not a number.
