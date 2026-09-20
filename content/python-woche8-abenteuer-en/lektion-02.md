# ⚔️ Archive Spell 2: Changing, adding and removing

A dictionary is **mutable**: you can overwrite values, add new entries and delete entries.

```python
hero["level"] = 20          # existing key: the value is overwritten
hero["level"] += 1          # calculating works too
hero["mana"] = 80       # new key: an entry is added

old = hero.pop("hp")       # removes the entry and returns the value
del hero["class"]             # removes the entry without returning anything
```

The same notation `dict[key] = value` therefore changes **or** adds – depending on whether the key already exists.
