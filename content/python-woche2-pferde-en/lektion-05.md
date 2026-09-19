# 🐴 Lesson 5: Working with Text

Texts (`str`) can be calculated with, too – but in their own way:

- `+` **joins** two texts into one: `"Star" + "light"` gives `"Starlight"`
- `*` **repeats** a text: `"Ha" * 3` gives `"HaHaHa"`

```python
name = "Star"
suffix = "light"
full_name = name + suffix
print(f"Full name: {full_name}")
print(f"Whinny: {name * 3}")
```

> 🐴 **Careful:** `+` only works between two texts – or between two numbers. A text and a number can't be joined directly. You will see how to fix that in the next lesson!
