# 📟 System Log 3: Counting Backwards

With a **negative step** `range()` counts backwards – perfect for a countdown to the hyperspace jump:

```python
for i in range(5, 0, -1):
    print(f"{i}...")
print("🚀 HYPERSPACE JUMP!")
```

- `range(5, 0, -1)` gives 5, 4, 3, 2, 1 (the 0 is *not* included)
- The line after the loop is **not indented** – it runs only once, after the loop has finished
