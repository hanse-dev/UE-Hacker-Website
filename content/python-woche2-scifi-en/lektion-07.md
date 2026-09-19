# 📟 System Protocol 7: Type Conversion

Sensor data often arrives as **text**. To calculate with it you have to convert it. Four functions do this job:

| Function | Converts to | Example |
|---|---|---|
| `int()` | whole number | `int("273")` → `273` |
| `float()` | decimal number | `float("42.5")` → `42.5` |
| `str()` | text | `str(5)` → `"5"` |
| `bool()` | truth value | `bool(1)` → `True`, `bool(0)` → `False` |

```python
temperature_str = "273"                  # text!
temperature_int = int(temperature_str)   # now a number
print(temperature_int + 10)              # 283
```

And the other way round: to put a number into a text with `+` you need `str()`:

```python
crew = 12
print("Crew: " + str(crew))
```

> 💡 With f-strings you don't need `str()` – they convert automatically.
