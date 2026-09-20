# 🔢 Collection Spell 2: Accessing entries

Every entry has a number, the **index**. Important: counting starts at **0**!

```python
treasures = ["Gold", "Crystal", "Amulet", "Crown", "Ring"]
print(treasures[0])    # first entry
print(treasures[1])    # second entry
print(treasures[-1])   # last entry
treasures[0] = "Key"   # replace an entry
```

**Remember:**
- `list[0]` is the **first**, `list[-1]` the **last** entry, `list[-2]` the second to last
- An index that does not exist (e.g. `list[5]` with 5 entries) gives an **IndexError**
- With `list[1] = "new"` you **replace** an entry

**Lists in lists:** An entry may itself be a list. With two indices you reach inside: `party[1][0]` is the first entry of the second sub-list.
