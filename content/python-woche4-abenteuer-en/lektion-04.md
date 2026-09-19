# 🔤 Looping Through Letters

A `for` loop can go through not only numbers but also the **letters of a text**, one by one:

```python
name = "Aria"
for letter in name:
    print(f"  - {letter}")
```

This prints `A`, `r`, `i`, `a` one after another. Python treats the text like a chain of characters, and `letter` is the next character on every run.

With this you can, for example, **count letters** – without `len()`:

```python
count = 0
for letter in "Dragon":
    count += 1
```
