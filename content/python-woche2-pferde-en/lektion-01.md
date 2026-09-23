# 🐴 Week 2: The Four Gait Types

Welcome back to **Sunny Valley Stables**! Here you master the four fundamental riding techniques. This week you learn the four **gait types** – Python's four data types:

1. Modern messages with **f-strings**
2. 🚶 **Walk** – text (`str`)
3. 🐎 **Trot** – whole numbers (`int`)
4. 🏇 **Canter** – decimal numbers (`float`)
5. 🦘 **Jump** – truth values (`bool`)
6. Calculating with numbers and text
7. **Converting** types
8. Processing input

This week too: every **lesson** is a **function** you call with **parentheses** – just like `print()` from Week 1.

## 📣 Lesson 1: f-strings

In Week 1 you joined text and numbers with `+` and `str()`. There's an easier way: put an **`f`** before the quotation marks and write variables in **curly braces** `{}`.

```python
horse_name = "Thunder"
age = 8
print(f"Hello {horse_name}! You are {age} years old!")
```

You can even calculate inside the braces: `f"Feed: {morning + evening} kg"`.

> 🐴 **Important:** Without the `f` before the quotation marks, `{age}` is printed as plain text!
