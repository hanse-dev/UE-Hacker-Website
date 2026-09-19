# 🔗 Spell Formula 3: Joining Texts

With `+` you can glue texts together – like connecting building blocks.

```python
print("Hero: " + hero_name)
```

## Why do I need `str()`?

Python treats text and numbers as different *types*. It's like apples and oranges – you can't simply add them together. `str()` is a spell formula (function) too: you put a number in the parentheses and it gives you back the matching text. `str()` turns a number into text so it can be joined:

```python
level = 5
print("Level: " + level)       # ❌ Error – number and text don't match
print("Level: " + str(level))  # ✅ works – str() turns 5 into the text "5"
```

This is how you build whole sentences:

```python
print(name + " fights with " + weapon + " and has " + str(arrows) + " arrows.")
```
