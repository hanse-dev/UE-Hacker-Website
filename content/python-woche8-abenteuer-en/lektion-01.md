# ⚔️ Archive Spell 1: Creating and reading profile cards

Welcome to the **Guild Archive of Pyralia**! For every hero, monster and treasure the archivist keeps a **profile card**. He says: *"Whoever only knows lists searches forever – whoever keeps profile cards finds any hero with a single word."*

A **dictionary** stores values under **names** (keys) instead of numbers like a list. You write it with curly braces:

```python
hero = {"name": "Aria", "class": "Mage", "level": 15}

print(hero["name"])    # access by key: Aria
print(len(hero))       # number of entries: 3
empty = {}                # an empty dictionary
```

**Step by step:**
1. **`{}`** – curly braces surround the dictionary
2. **`key: value`** – the colon joins key and value, commas separate the entries
3. **`dict[key]`** – square brackets fetch the value

> ⚠️ A key that does not exist raises a **KeyError**. Watch out for upper and lower case, too!
