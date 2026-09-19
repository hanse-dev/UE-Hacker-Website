# ⭐ Patterns of Stars

Nested loops are ideal for **patterns**: the outer loop stands for the **rows**, the inner one for the **columns**.

Normally `print()` jumps to a new line after every output. With `end=""` (or `end=" "`) the cursor stays in the same line instead. An empty `print()` ends the line:

```python
for row in range(3):
    for column in range(4):
        print("⭐", end=" ")
    print()
```

This draws a rectangle of 3 rows with 4 stars each.

**Tip:** If the number of inner runs depends on the row (`range(row)`), you get a **triangle**!
