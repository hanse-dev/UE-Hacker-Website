# ⚖️ Magic Formula 2: `if-else`

`if-else` offers **two paths**: one for a true condition and one for everything else.

```python
roll = 18
if roll >= 15:
    print("Critical hit!")
else:
    print("Normal strike")
```

> ⚠️ `else` needs **no condition** – it runs whenever the `if` was false. It also ends with a colon and its code is indented.

Exactly **one** of the two paths is run – never both, never none.

```python
gold = 45
cost = 50
if gold >= cost:
    print(f"Purchase successful! Remaining: {gold - cost}")
else:
    print(f"Not enough gold! Missing: {cost - gold}")
```
