# 🚀 Data Log 5: Tuples

A **tuple** is like a list, but **immutable**. You write it with round brackets:

```python
part = ("Shield module", 15, "Energy")
print(part[0])          # Shield module – access by position like with lists
print(len(part))        # 3

name, value, kind = part   # unpacking: three variables at once
single = (42,)                 # a one-element tuple needs the comma!
```

**Step by step:**
1. **`(a, b, c)`** – round brackets, commas in between
2. **`tuple[0]`** – access by position
3. **`x, y = tuple`** – unpacking distributes the values to variables (the count must match)

Tuples suit things that belong together and stay fixed – for example coordinates `(x, y)`.
