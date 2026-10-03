# ⚖️ Important Operators: `=` or `==`?

This is a **crucial difference** that trips up many cadets:

- **`=` (one equals sign)** *assigns*: it stores a value in a variable.
- **`==` (two equals signs)** *compares*: it asks "Are both sides equal?" – and gives back `True` or `False`.

```python
energy = 100        # assignment: energy gets the value 100
if energy == 100:   # comparison: is energy equal to 100?
    print("Full energy!")
```

A comparison is a value in itself, and you can even print it:

```python
energy = 100
print(energy == 100)   # True
print(energy == 50)   # False
```

> 📡 **Remember:** In a condition always use `==` to compare, never `=`! A single `=` in an `if` is a syntax error.
