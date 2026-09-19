# 🔍 range() with Start and End

The Tower Guardian shows you a stone tablet: *"Not every count begins at zero."* With **two numbers** in `range()` you set the beginning **and** the end:

```python
for number in range(3, 8):
    print(f"Number: {number}")
```

This prints `3, 4, 5, 6, 7`.

| Notation | Result |
|----------|--------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(3, 8)` | 3, 4, 5, 6, 7 |
| `range(1, 4)` | 1, 2, 3 |

**Important rule:** The **upper limit is always exclusive** – it is not counted any more. If you want to count up to 10, write `range(1, 11)`.
