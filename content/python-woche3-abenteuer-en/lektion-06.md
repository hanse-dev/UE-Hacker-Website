# ⚖️ Magic Formula 4: Logical Operators (`and`, `or`, `not`)

Often *one* condition is not enough. With **logical operators** you combine several:

| Operator | Meaning | True when ... |
|----------|---------|---------------|
| `and` | and | **both** sides are true |
| `or` | or | **at least one** side is true |
| `not` | not | the condition is **false** (flips it) |

```python
has_key = True
has_torch = True
if has_key and has_torch:
    print("You can safely open the dark chamber!")
```

```python
has_sword = False
has_wand = True
if has_sword or has_wand:
    print("You are armed and ready!")
```

```python
is_cursed = False
if not is_cursed:
    print("You are free of any curse!")
```

You can also mix them with comparisons, for example `if strength > 10 and intelligence > 10:`.
