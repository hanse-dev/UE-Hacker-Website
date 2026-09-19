# 🐴 Week 2 – Lesson 1: String Gallop

Welcome back to the **Sunny Valley Riding Ranch**! This week you will learn how Python organises different kinds of information. You will get to know the four **hoofbeat types** (`str`, `int`, `float`, `bool`), calculate with them and convert them into each other.

## 🐎 First: f-strings

In Week 1 you joined text and variables with `+` and `str()`. There is a much nicer way: the **f-string**.

Put an `f` in front of the opening quotation mark and write your variables in **curly braces** `{}` right inside the text:

```python
horse_name = "Thunder"
age = 8
print(f"Hello {horse_name}! You are {age} years old.")
```

Python fills in the values by itself – no `+`, no `str()` needed. You can even calculate inside the braces:

```python
print(f"Daily feed: {3 + 2} kg")
```

> 🐴 **Important:** Always put the `f` **before** the quotation marks – without it Python prints the braces exactly as they are!
