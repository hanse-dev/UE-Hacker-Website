# 🚀 Data Log 1: Creating and reading profile cards

Welcome to the **Data Archive of space station Nebula-7**! The ship AI stores every person, part and find as a **record**. It reports: *"Whoever only knows lists searches for seconds – whoever keeps named records finds everything at once."*

A **dictionary** stores values under **names** (keys) instead of numbers like a list. You write it with curly braces:

```python
member = {"name": "Nova", "role": "Pilot", "rank": 4}

print(member["name"])    # access by key: Nova
print(len(member))       # number of entries: 3
empty = {}                # an empty dictionary
```

**Step by step:**
1. **`{}`** – curly braces surround the dictionary
2. **`key: value`** – the colon joins key and value, commas separate the entries
3. **`dict[key]`** – square brackets fetch the value

> ⚠️ A key that does not exist raises a **KeyError**. Watch out for upper and lower case, too!
