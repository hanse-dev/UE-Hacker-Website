# 🔄 Conversion Spells

Conversions are also **spell formulas (functions)** – you call them with parentheses and give them the value to convert. They hand back the converted value.

| Spell formula | Converts into ... | Example |
|----------------|--------------------|---------|
| `int()` | 🪨 whole number | `int("25")` → `25` |
| `float()` | 💧 decimal number | `float("3.5")` → `3.5` |
| `str()` | 🔥 text | `str(50)` → `"50"` |
| `bool()` | 💨 truth value | `bool(0)` → `False` |

```python
age_text = "25"                  # Fire
age = int(age_text)              # Fire -> Earth
print(age + 5)                   # 30

gold = 50
print("Gold: " + str(gold))      # Earth -> Fire, now it fits with text
```

**Good to know:**
- `int(3.9)` cuts off the decimal places and gives `3` (it does **not** round).
- `int("abc")` doesn't work – only text that really looks like a number can be converted.
- `bool()` gives `False` for `0` and the empty text `""`, otherwise `True`.
