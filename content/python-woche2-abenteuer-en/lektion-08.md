# 🔮 Consulting the Oracle

You already know `input()` from Week 1 – it is a spell formula that consults the oracle. The answer is **always a 🔥 Fire element (string)** – even if someone types a number! For 🪨 Earth or 💧 Water you have to convert the answer:

```python
name = input("What is your name? ")          # Fire (str)
age = int(input("How old are you? "))        # Fire -> Earth (str -> int)
power = float(input("Magic power? "))        # Fire -> Water (str -> float)
```

You see a **spell inside a spell**: `input()` is cast first, then `int()` converts its result.

```python
level = int(input("Level? "))
print(f"In 5 levels you will be Level {level + 5}.")
```
