## ⭐ Lesson 8: Patterns of Stars

Nested loops are ideal for **patterns**: the outer loop stands for the **rows**, the inner one for the **columns**.

If the number of inner runs depends on the row (`range(row)`), you get a **staircase** instead of a rectangle:

```python
for row in range(1, 4):
    for column in range(row):
        print("🐴", end=" ")
    print()
```

Row 1 gets one horse, row 2 two, row 3 three.

> 💡 You can also print the loop variable of the inner loop: `print(column, end="")` writes numbers instead of stars.
