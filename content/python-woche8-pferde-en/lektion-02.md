# 🐴 Exercise 2: Changing, adding and removing

A dictionary is **mutable**: you can overwrite values, add new entries and delete entries.

```python
horse["age"] = 20          # existing key: the value is overwritten
horse["age"] += 1          # calculating works too
horse["wins"] = 3       # new key: an entry is added

old = horse.pop("points")       # removes the entry and returns the value
del horse["breed"]             # removes the entry without returning anything
```

The same notation `dict[key] = value` therefore changes **or** adds – depending on whether the key already exists.
