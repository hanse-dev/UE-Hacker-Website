# 📟 System Log 6: The Shield Generator

A while loop often needs **several variables**: one for the value that changes, and one that counts the passes.

```python
energy = 100
minute = 1
while energy > 20:
    energy -= 15
    print(f"Minute {minute}: remaining: {energy}%")
    minute += 1
print(f"Shield critical after {minute-1} minutes!")
```

The loop stops as soon as `energy > 20` is false. After the loop `minute-1` tells you how many passes there were.

Values can also change by other rules, e.g. doubling with `signal *= 2`.
