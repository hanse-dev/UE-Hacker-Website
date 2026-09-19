# 🔄 Conversion Spells

To change an element from one nature into another you cast a **conversion spell** – and these are all **functions** too, just like `print()` and `type()`. They are named after the element they create:

| Spell formula | Creates | Example | Result |
|---------------|---------|---------|--------|
| `int(x)` | 🪨 Earth (whole number) | `int("25")` | `25` |
| `float(x)` | 💧 Water (decimal number) | `float("7.5")` | `7.5` |
| `str(x)` | 🔥 Fire (text) | `str(20)` | `"20"` |
| `bool(x)` | 💨 Air (truth value) | `bool(0)` | `False` |

```python
age_str = "25"              # Fire – only text
age_int = int(age_str)      # Earth – now a real number
print(age_int + 5)          # 30
```

**`str()` makes fusion possible:**

```python
level = 7
print("Level: " + str(level))   # Level: 7
```

**`bool()`:** `0`, `0.0` and empty text `""` become `False`; everything else becomes `True`.

```python
print(bool(0))       # False
print(bool("Aria"))  # True
```

> ⚠️ `int("hello")` does not work – only text that really looks like a number can be converted.
