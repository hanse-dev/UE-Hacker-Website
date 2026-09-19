# 🐴 Lesson 5: Logical Operators

With `and`, `or` and `not` you combine several conditions:

| Operator | Meaning |
|----------|---------|
| `and` | **both** conditions must be true |
| `or` | **at least one** condition must be true |
| `not` | flips `True` to `False` and the other way round |

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
    print("The horse is healthy and ready to work!")
```

You can also mix comparisons with `and`/`or`: `if height > 170 and temperament > 7:`
