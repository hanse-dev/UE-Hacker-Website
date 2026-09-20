# 🔁 Collection Spell 7: Lists and loops

A `for` loop runs straight through the **entries** of a list (no `range` needed):

```python
treasures = ["Gold", "Crystal", "Amulet"]
for entry in treasures:
    print(entry)

for nr, entry in enumerate(treasures):
    print(nr, entry)        # 0 Gold, 1 Crystal, ...
```

- **`for entry in list:`** – `entry` is the next entry on every pass
- **`enumerate(list)`** also gives the **position** (`nr` starts at 0)
- With a loop you can **calculate**: form a sum, count, search for the largest

**Lists in functions:** If you pass a list to a function, the function works with the **same** list. An `append` inside the function therefore also changes the list **outside** – no `return` is needed for that.
