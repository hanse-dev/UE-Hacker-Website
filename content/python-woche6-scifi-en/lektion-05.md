# 🔍 Data Log 5: Searching and counting

```python
modules = ["Drive", "Sensor", "Drive", "Shield", "Drive", "Radar"]
print("Sensor" in modules)          # True – is the entry in there?
print("Laser" in modules)          # False
print(modules.index("Sensor"))      # position of the first match
print(modules.count("Drive"))      # how often does it occur?
```

- **`x in list`** gives `True` or `False` – ideal for `if`
- **`list.index(x)`** returns the **position** of the first match (if `x` is not there, you get an error – check with `in` first)
- **`list.count(x)`** counts **how often** `x` occurs
- The word **`in`** works with text too: `"Gold" in "Goldcoin"` is `True`
