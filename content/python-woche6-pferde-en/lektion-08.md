# 🚦 Lesson 8: break and continue

Sometimes you want to **end a loop early** or **skip one pass**:

```python
horses = ["Stormwind", "Lightning", "Luna", "Fox", "Balu"]
for entry in horses:
    if entry == "Luna":
        print("Found!")
        break                # end the loop immediately
    print(entry)

for entry in horses:
    if entry == "Lightning":
        continue             # skip this pass
    print(entry)
```

- **`break`** ends the loop immediately – e.g. as soon as you have found what you were looking for
- **`continue`** skips the rest of the current pass and carries on with the **next** entry

> 💡 Both almost always sit inside an `if` within the loop.
