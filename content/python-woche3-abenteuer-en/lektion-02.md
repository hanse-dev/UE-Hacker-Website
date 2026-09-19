# ⚖️ Important Operators: `=` or `==`?

This is a **crucial difference** that trips up many adventurers:

- **`=` (one equals sign)** *assigns*: it stores a value in a variable.
- **`==` (two equals signs)** *compares*: it asks "Are both sides equal?" – and gives back `True` or `False`.

```python
level = 10        # assignment: level gets the value 10
if level == 10:   # comparison: is level equal to 10?
    print("Level 10 reached!")
```

A comparison is a value in itself, and you can even print it:

```python
level = 10
print(level == 10)   # True
print(level == 99)   # False
```

> **Remember:** In a condition always use `==` to compare, never `=`! A single `=` in an `if` is a syntax error.
