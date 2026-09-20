# 🚀 Data Log 2: Changing, adding and removing

A dictionary is **mutable**: you can overwrite values, add new entries and delete entries.

```python
member["rank"] = 20          # existing key: the value is overwritten
member["rank"] += 1          # calculating works too
member["shield"] = 80       # new key: an entry is added

old = member.pop("energy")       # removes the entry and returns the value
del member["role"]             # removes the entry without returning anything
```

The same notation `dict[key] = value` therefore changes **or** adds – depending on whether the key already exists.
