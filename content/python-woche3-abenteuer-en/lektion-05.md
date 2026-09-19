# ⚖️ Magic Formula 4: Logical Operators

With `and`, `or` and `not` you combine several conditions into one.

| Operator | Meaning | True when ... |
|----------|---------|---------------|
| `and` | both | **both** conditions are true |
| `or` | either | **at least one** condition is true |
| `not` | flips | the condition is **false** |

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

Of course you can use them in an `elif`, too:

```python
strength = 8
intelligence = 12
if strength > 10 and intelligence > 10:
    print("Paladin!")
elif strength > 10:
    print("Warrior!")
elif intelligence > 10:
    print("Mage!")
else:
    print("Adventurer!")
```
