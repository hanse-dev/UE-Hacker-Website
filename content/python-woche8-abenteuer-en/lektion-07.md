# ⚔️ Archive Spell 7: Nested structures

Values in a dictionary may themselves be dictionaries or lists – and lists may contain dictionaries:

```python
hero["equipment"] = {"weapon": "Staff", "armor": "Robe"}
print(hero["equipment"]["weapon"])   # two keys in a row: Staff

heroes = [{"name": "Aria", "level": 15}, {"name": "Thorin", "level": 18}]
for e in heroes:
    print(e["name"])

strong = [e["name"] for e in heroes if e["level"] > 14]   # list comprehension with a condition
```

You read from the outside in: first the outer key, then the inner one. A tuple can be a key, too: `{(2, 3): "Point A"}`.
