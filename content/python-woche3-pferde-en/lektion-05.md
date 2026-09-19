# 🔗 Lesson 5: Logical operators (and, or, not)

With **`and`**, **`or`** and **`not`** you combine several conditions:

| Operator | Meaning |
|----------|---------|
| `and` | **both** conditions must be true |
| `or` | **at least one** must be true |
| `not` | flips a truth value (`True` ↔ `False`) |

```python
has_saddle = True
has_helmet = True
if has_saddle and has_helmet:
    print("You are ready to ride!")
```

```python
has_bridle = False
has_halter = True
if has_bridle or has_halter:
    print("You can lead the horse!")
```

```python
is_sick = False
if not is_sick:
    print("The horse is healthy!")
```

> 💡 With several combinations, **parentheses** help, e.g. `a or (b and c)` – then it is clear what belongs together.
