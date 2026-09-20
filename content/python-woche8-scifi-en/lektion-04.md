# 🚀 Data Log 4: Looping through dictionaries

A `for` loop goes through all entries. Three methods give you what you need:

| Method | Returns | Example |
|---|---|---|
| `.keys()` | all keys | `for k in d.keys()` |
| `.values()` | all values | `for v in d.values()` |
| `.items()` | key **and** value | `for k, v in d.items()` |

```python
stock = {"Battery": 3, "Cable": 5, "Sensor": 2}
for name, amount in stock.items():
    print(name, amount)

total = 0
for amount in stock.values():
    total += amount
```

`for name in dict` loops over the **keys** without any addition. `.items()` is the most useful: you get both at once.
