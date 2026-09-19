# 🪜 Step Size and Counting Backwards

Sometimes you don't want every number, only **every second** or **every fifth** one. For that there is a **third number** in `range()` – the step size:

```python
for even in range(0, 11, 2):
    print(f"Even number: {even}")
```

This prints `0, 2, 4, 6, 8, 10`.

You count **backwards** with a **negative** step size:

```python
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 Launch!")
```

| Form | Meaning |
|------|---------|
| `range(n)` | 0 to n-1 |
| `range(start, end)` | start to end-1 |
| `range(start, end, step)` | with distance `step` |

Here too: the **end is exclusive**. When counting backwards, `range(5, 0, -1)` stops at 1.
