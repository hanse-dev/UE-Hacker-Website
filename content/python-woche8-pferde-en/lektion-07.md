# 🐴 Exercise 7: Nested structures

Values in a dictionary may themselves be dictionaries or lists – and lists may contain dictionaries:

```python
horse["equipment"] = {"saddle": "Leather", "blanket": "Wool"}
print(horse["equipment"]["saddle"])   # two keys in a row: Leather

horses = [{"name": "Blitz", "age": 8}, {"name": "Storm", "age": 12}]
for e in horses:
    print(e["name"])

strong = [e["name"] for e in horses if e["age"] > 7]   # list comprehension with a condition
```

You read from the outside in: first the outer key, then the inner one. A tuple can be a key, too: `{(2, 3): "Point A"}`.
