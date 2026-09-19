## 🏇 Lesson 3: range(start, end, step)

The third number is the **step size**. It lets you skip numbers:

```python
for hurdle in range(0, 11, 2):
    print(f"Hurdle {hurdle}: Cleared!")
```

This prints 0, 2, 4, 6, 8, 10 – every second hurdle.

With a **negative** step size you count **backwards**:

```python
for i in range(5, 0, -1):
    print(f"{i}...")
print("🏇 GO!")
```

> 💡 The `print("🏇 GO!")` is **not indented** – it no longer belongs to the loop and only runs **after** all the passes.
