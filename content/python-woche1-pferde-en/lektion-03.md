# 🔗 Lesson 3: Joining Texts

With `+` you can glue texts together – like laying building blocks side by side.

```python
print("Horse: " + horse_name)
```

## Why do I need `str()`?

Python treats text and numbers as different *types*. It's like apples and oranges – you can't simply add them together. `str()` is a function too: you put a number inside the parentheses and it hands you back the matching text:

```python
age = 5
print("Age: " + age)       # ❌ Error – number and text don't match
print("Age: " + str(age))  # ✅ works – str() turns 5 into the text "5"
```
