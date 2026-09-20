# 🚀 Data Log 7: Nested structures

Values in a dictionary may themselves be dictionaries or lists – and lists may contain dictionaries:

```python
member["equipment"] = {"tool": "Laser", "suit": "Spacesuit"}
print(member["equipment"]["tool"])   # two keys in a row: Laser

crew = [{"name": "Nova", "rank": 4}, {"name": "Rex", "rank": 6}]
for e in crew:
    print(e["name"])

strong = [e["name"] for e in crew if e["rank"] > 3]   # list comprehension with a condition
```

You read from the outside in: first the outer key, then the inner one. A tuple can be a key, too: `{(2, 3): "Point A"}`.
