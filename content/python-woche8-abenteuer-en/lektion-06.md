# ⚔️ Archive Spell 6: Immutable and catching errors

If you try to change a tuple, Python raises a **TypeError**. With **`try`/`except`** you catch such errors:

```python
try:
    artifact[1] = 99                # may cause an error
except TypeError:
    print("Tuples are immutable")    # runs only if the error occurs

print("Carry on")                  # always runs
```

**Typical kinds of errors:**
- **`TypeError`** – e.g. changing a tuple
- **`KeyError`** – a key is missing in the dictionary
- **`ValueError`** – e.g. `int("ten")`

Catch only the error you expect – that way you still find real bugs.
