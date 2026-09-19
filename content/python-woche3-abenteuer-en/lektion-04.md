# ⚖️ Magic Formula 3: `if-elif-else`

With `if-elif-else` you check **several conditions one after another**. `elif` is short for *else if*.

```python
xp = 750
if xp >= 1000:
    print("Master!")
elif xp >= 500:
    print("Advanced!")
elif xp >= 100:
    print("Beginner!")
else:
    print("Still much to learn...")
```

> ⚠️ `elif` **always needs a condition**. Only the **first** true path runs – all others are skipped, even if they would also be true. So put the strictest condition first!

You can use as many `elif` paths as you need. `else` at the end is optional and catches everything else.

It works with text, too:

```python
element = "Water"
if element == "Fire":
    print("Fire Strike!")
elif element == "Water":
    print("Water Torrent!")
else:
    print("Unknown element!")
```
