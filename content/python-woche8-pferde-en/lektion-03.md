# 🐴 Exercise 3: Safe access with get() and in

If a key is missing, `dict[key]` raises a **KeyError**. Two safe ways:

```python
print(horse.get("name"))         # Blitz
print(horse.get("wins"))       # None – no error
print(horse.get("wins", 0))    # 0 – your own default value

print("name" in horse)           # True – checks the KEYS
print("wins" in horse)         # False
```

**`in`** always checks the **keys** of a dictionary, never the values.
