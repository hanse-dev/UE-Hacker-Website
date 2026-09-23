# 🔄 Lesson 8: Converting Types

Not all types fit together – `"5" * 2` gives `"55"`, but `5 * 2` gives `10`. Luckily there are four **conversion functions**, one per gait type. Give them a value, and they hand it back in the new type:

| Function | turns it into … | Example | Result |
|----------|-------------------|---------|--------|
| `int()` | whole number | `int("5")` | `5` |
| `float()` | decimal number | `float("4.5")` | `4.5` |
| `str()` | text | `str(5)` | `"5"` |
| `bool()` | truth value | `bool(1)` | `True` |

```python
age_text = "5"
age_number = int(age_text)
print(type(age_text))    # <class 'str'>
print(type(age_number))  # <class 'int'>
```

> 🐴 **Remember:** `int("abc")` doesn't work – only text that really looks like a number can be converted.
