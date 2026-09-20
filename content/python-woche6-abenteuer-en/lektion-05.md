# 🔍 Collection Spell 5: Searching and counting

```python
treasures = ["Gold", "Crystal", "Gold", "Amulet", "Gold", "Crown"]
print("Crystal" in treasures)          # True – is the entry in there?
print("Ruby" in treasures)          # False
print(treasures.index("Crystal"))      # position of the first match
print(treasures.count("Gold"))      # how often does it occur?
```

- **`x in list`** gives `True` or `False` – ideal for `if`
- **`list.index(x)`** returns the **position** of the first match (if `x` is not there, you get an error – check with `in` first)
- **`list.count(x)`** counts **how often** `x` occurs
- The word **`in`** works with text too: `"Gold" in "Goldcoin"` is `True`
- **`set(list)`** removes **duplicates** but has no fixed order – `sorted(set(list))` gives the entries without duplicates in alphabetical order
