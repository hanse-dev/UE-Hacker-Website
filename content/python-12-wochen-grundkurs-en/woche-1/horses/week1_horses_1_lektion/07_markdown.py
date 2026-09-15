"""## Lesson 3

With `+` you can glue texts together – like connecting building blocks.

```python
print(\"Horse: \" + horse_name)
```

**Why do I need `str()`?**

Python treats text and numbers as different *types*. It's like apples and oranges – you can't simply add them together. `str()` converts a number to text so it can be joined:

```python
age = 5
print(\"Age: \" + age)       # ❌ Error – number and text don't match
print(\"Age: \" + str(age))  # ✅ works – str() turns 5 into the text \"5\"
```"""
