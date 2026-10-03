# ⚖️ Important Operators: `=` or `==`?

This is a **crucial difference** that trips up many riders:

- **`=` (one equals sign)** *assigns*: it stores a value in a variable.
- **`==` (two equals signs)** *compares*: it asks "Are both sides equal?" – and gives back `True` or `False`.

```python
age = 10        # assignment: age gets the value 10
if age == 10:   # comparison: is age equal to 10?
    print("The horse is 10 years old!")
```

A comparison is a value in itself, and you can even print it:

```python
age = 10
print(age == 10)   # True
print(age == 12)   # False
```

> 🐴 **Remember:** In a condition always use `==` to compare, never `=`! A single `=` in an `if` is a syntax error.
