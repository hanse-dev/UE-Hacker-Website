# 🚦 Collection Spell 8: break and continue

Sometimes you want to **end a loop early** or **skip one pass**:

```python
treasures = ["Gold", "Crystal", "Amulet", "Crown", "Ring"]
for entry in treasures:
    if entry == "Amulet":
        print("Found!")
        break                # end the loop immediately
    print(entry)

for entry in treasures:
    if entry == "Crystal":
        continue             # skip this pass
    print(entry)
```

- **`break`** ends the loop immediately – e.g. as soon as you have found what you were looking for
- **`continue`** skips the rest of the current pass and carries on with the **next** entry

> 💡 Both almost always sit inside an `if` within the loop.
