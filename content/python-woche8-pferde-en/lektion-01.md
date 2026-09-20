# 🐴 Exercise 1: Creating and reading profile cards

Welcome to the **Stable Archive of the riding farm**! Every horse has a **stable card** with all its details. The stable master says: *"Whoever searches a long list for every detail wastes time. Whoever keeps stable cards finds any horse at once."*

A **dictionary** stores values under **names** (keys) instead of numbers like a list. You write it with curly braces:

```python
horse = {"name": "Blitz", "breed": "Hanoverian", "age": 8}

print(horse["name"])    # access by key: Blitz
print(len(horse))       # number of entries: 3
empty = {}                # an empty dictionary
```

**Step by step:**
1. **`{}`** – curly braces surround the dictionary
2. **`key: value`** – the colon joins key and value, commas separate the entries
3. **`dict[key]`** – square brackets fetch the value

> ⚠️ A key that does not exist raises a **KeyError**. Watch out for upper and lower case, too!
