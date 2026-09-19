# 🔗 System Protocol 3: Joining Texts

With `+` you can glue texts together – like connecting building blocks.

```python
print("Ship: " + ship_name)
```

## Why do I need `str()`?

Python treats text and numbers as different *types*. It's like apples and oranges – you can't simply add them together. `str()` is a function too: you put a number in the parentheses and it hands you back the matching text:

```python
mission = 5
print("Mission: " + mission)       # ❌ Error – number and text don't match
print("Mission: " + str(mission))  # ✅ works – str() turns 5 into the text "5"
```
