# 🛡️ Spell Formula 2: The while Loop

At the second gate stands the **Guardian of the Condition**. He keeps you running in circles *as long as* his condition is true. A `while` loop repeats code **as long as** a condition is `True`:

```python
counter = 0
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1
```

**Step by step:**
1. `counter` starts at 0
2. As long as `counter <= 5` holds, the indented code runs
3. `counter += 1` increases the value on every run
4. At `counter = 6` the condition is false – the loop ends

> ⚠️ **Careful:** If you forget `counter += 1`, the condition never becomes false – the loop runs **forever**! The condition has to change at some point.

| Loop | When? |
|------|-------|
| `for` | You know **how often** |
| `while` | You repeat **as long as** something holds |
