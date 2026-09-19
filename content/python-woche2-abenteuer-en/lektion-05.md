# 💨 Element 4: Air – Truth Values (`bool`)

**Air** is invisible: it is either there or not. A truth value has only **two possible values**: `True` and `False` – written with a capital first letter and **without** quotation marks.

```python
magic_active = True
poisoned = False
print(f"Magic active: {magic_active}")
print(type(magic_active))   # <class 'bool'>
```

Air often comes from **comparisons**. The result of a comparison is always `True` or `False`:

| Comparison | Meaning |
|------------|---------|
| `a > b` | is a greater than b? |
| `a < b` | is a smaller than b? |
| `a == b` | are a and b equal? (two equals signs!) |

```python
hit_points = 150
print(hit_points > 100)   # True
```

> ⚠️ `"True"` in quotation marks is only text (Fire), not Air.
