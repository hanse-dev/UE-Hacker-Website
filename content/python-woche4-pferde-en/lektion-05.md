## ⏳ Lesson 5: Loop – The Endurance Test

A **while loop** repeats code **as long as** a condition is true:

```python
counter = 1
while counter <= 5:
    print(f"Hoofbeat {counter}")
    counter += 1
```

1. `counter` starts at 1.
2. As long as `counter <= 5` is true, the indented code runs.
3. `counter += 1` raises the value by 1 on every pass.
4. At `counter = 6` the condition is false – the loop ends.

> ⚠️ **Careful:** If you forget `counter += 1`, the condition never becomes false – and the loop runs **forever**!
