# ⚖️ Magic Formula 2: if-else

Sometimes something should happen when the condition is true – **and something else** when it is not. That is what `else` is for:

```python
roll = 18
if roll >= 15:
    print("Critical hit!")
else:
    print("Normal strike")
```

- `else` stands at the **same level** as its `if`
- `else` needs **no condition**, but it also needs a colon
- Exactly **one** of the two paths is run – never both, never none
