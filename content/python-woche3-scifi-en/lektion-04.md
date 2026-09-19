# 📟 System Protocol 4: if-elif-else

Sometimes there are **more than two** possibilities. That is what `elif` (short for "else if") is for:

```python
points = 750
if points >= 1000:
    print("Fleet Commander!")
elif points >= 500:
    print("Captain!")
elif points >= 100:
    print("Lieutenant!")
else:
    print("Cadet!")
```

- Python checks the conditions **from top to bottom**.
- **Only the first true path** is executed, the rest is skipped.
- `elif` **always needs a condition** (unlike `else`).
- You may use as many `elif` as you like; the final `else` is optional and catches everything else.

Text can be selected this way too:

```python
weapon = "Laser"
if weapon == "Laser":
    print("Laser activated!")
elif weapon == "Plasma":
    print("Plasma cannon loaded!")
else:
    print("Unknown weapon!")
```

> 📡 **Remember:** Order matters! Check the strictest condition first.
