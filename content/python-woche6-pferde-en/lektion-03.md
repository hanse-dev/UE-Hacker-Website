# ➕ Lesson 3: Adding entries

A list is **changeable** – you can add entries:

```python
horses = ["Stormwind", "Lightning", "Luna"]
horses.append("Nova")         # at the end
horses.insert(0, "Stella")   # at a position (here: at the very front)
print(horses)
```

- **`append(x)`** adds `x` **at the end**
- **`insert(index, x)`** puts `x` at position `index`, the others move back
- You join two lists with **`+`**: `everything = list1 + list2`
- With **`extend(list2)`** you attach a whole list

> ⚠️ `append` and `insert` **change** the list itself and return nothing – do **not** write `list = list.append(x)`, otherwise `list` is `None` afterwards!
