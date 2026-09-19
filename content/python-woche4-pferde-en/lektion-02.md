## 🎯 Lesson 2: range(start, end)

With two numbers you tell `range()` where to **begin** and where to **stop**:

```python
for hurdle in range(3, 8):
    print(f"Hurdle {hurdle}: Jump!")
```

This prints hurdles 3, 4, 5, 6 and 7.

> 🐴 **Important:** The start is included, the end is **not**! `range(3, 8)` goes from 3 up to **just before** 8 – like an arena that ends at hurdle 7.

The three forms of `range()` so far:
- `range(n)` → 0 to n-1
- `range(start, end)` → start to end-1
