# 🐴 Lesson 7: Processing Input

Remember `input()` from Week 1? Here comes the catch: **`input()` always returns a `str`** – even if the rider types a number!

```python
entry = input("How many kg of hay? ")   # rider types 15
print(type(entry))                      # <class 'str'>
```

To calculate with the entry, convert it first:

```python
number = int(entry)
print(f"{number} kg of hay lasts for {number * 2} days.")
```

For decimal numbers use `float(entry)` instead.

In the exercises below the input is **simulated** – the text is already in a variable, as if the rider had just typed it. In your own programs you can replace it with a real `input()` any time.
