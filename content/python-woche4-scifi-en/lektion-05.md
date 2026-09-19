# 📟 System Log 5: The while Loop – The Continuous Scanner

A **while loop** repeats code **as long as a condition is true**:

```python
scan = 0
while scan <= 10:
    print(f"Scan {scan}: Data received")
    scan += 1
```

1. `scan` starts at 0
2. As long as `scan <= 10`, the indented code runs
3. `scan += 1` increases the value on every pass
4. At `scan = 11` the condition is false and the loop ends

> ⚠️ **Caution – infinite loops!** If the condition never becomes false (for example because you forgot `scan += 1`), the loop never ends. Always make sure something inside the loop changes the condition.
