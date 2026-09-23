# 🔤 Lesson 7: Calculating with Text

Strings have operators too:

- **`+`** glues texts together: `"Star" + "light"` gives `"Starlight"`
- **`*`** repeats a text: `"Neigh! " * 3` gives `"Neigh! Neigh! Neigh! "`

```python
name = "Star"
suffix = "light"
full_name = name + suffix
print(f"Full name: {full_name}")
print(f"Neigh: {name * 3}")
```

> ⚠️ Text and numbers **cannot** be mixed with `+` (`"Age: " + 5` gives an error). For that you need `str()` or an f-string – more on that in the next lesson.
