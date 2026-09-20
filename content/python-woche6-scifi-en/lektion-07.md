# 🔁 Data Log 7: Lists and loops

A `for` loop runs straight through the **entries** of a list (no `range` needed):

```python
modules = ["Drive", "Sensor", "Shield"]
for entry in modules:
    print(entry)

for nr, entry in enumerate(modules):
    print(nr, entry)        # 0 Drive, 1 Sensor, ...
```

- **`for entry in list:`** – `entry` is the next entry on every pass
- **`enumerate(list)`** also gives the **position** (`nr` starts at 0)
- With a loop you can **calculate**: form a sum, count, search for the largest

**Lists in functions:** If you pass a list to a function, the function works with the **same** list. An `append` inside the function therefore also changes the list **outside** – no `return` is needed for that.
