# 💨 Air: Truth Values (`bool`)

The Air element only knows **two values**: `True` or `False` – **capitalised** and **without** quotation marks. Like a switch: on or off.

```python
magic_active = True
poisoned = False
print(f"Magic active: {magic_active}")
print(type(magic_active))    # <class 'bool'>
```

Comparisons automatically give you a truth value:

| Comparison | Meaning |
|------------|---------|
| `a > b` / `a < b` | greater than / less than |
| `a >= b` / `a <= b` | greater-or-equal / less-or-equal |
| `a == b` | equal (careful: **two** equals signs!) |
| `a != b` | not equal |

```python
level = 8
print(level >= 10)    # False
```
