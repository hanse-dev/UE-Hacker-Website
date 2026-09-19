# ⚖️ Magic Formula 3: if-elif-else

With more than two possibilities, `elif` helps (short for *else if*). Python checks the conditions **from top to bottom** and runs only the **first** true branch:

```python
xp = 750
if xp >= 1000:
    print("Master!")
elif xp >= 500:
    print("Advanced!")
elif xp >= 100:
    print("Beginner!")
else:
    print("Still much to learn...")
```

- `elif` **always needs a condition** (an `elif:` without a condition is an error)
- You can use as many `elif` as you like
- The `else` at the end is optional and catches **everything else**
- **Order matters:** With `xp = 750`, both `xp >= 500` and `xp >= 100` are true – but only the first hit counts. So always check from strict to loose.
