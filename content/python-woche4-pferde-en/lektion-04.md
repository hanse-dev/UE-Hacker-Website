## 🔤 Lesson 4: Walking through letters

A for loop can also go through **text** – letter by letter:

```python
name = "Thunder"
for letter in name:
    print(f"  - {letter}")
```

On every pass `letter` holds the next letter of the horse's name. The loop ends when no letters are left.

> 🐴 This works because text is a **sequence of characters** – just as `range()` produces a sequence of numbers.
