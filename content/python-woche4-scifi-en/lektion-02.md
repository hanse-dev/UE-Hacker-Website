# 📟 System Log 2: range() – The Time Generator

`range()` is your most powerful tool for time sequences. It has three forms:

| Form | Numbers | Example |
|---|---|---|
| `range(n)` | 0 up to n-1 | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, end)` | start up to end-1 | `range(2, 7)` → 2, 3, 4, 5, 6 |
| `range(start, end, step)` | with intervals | `range(1, 10, 2)` → 1, 3, 5, 7, 9 |

```python
for sector in range(3, 8):
    print(f"Sector {sector}: Scan complete")
```

> ⚠️ The **upper bound is never included**: `range(3, 8)` stops at 7 – like coordinates from 3 up to *before* 8.
