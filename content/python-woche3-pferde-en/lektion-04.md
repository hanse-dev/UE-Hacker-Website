# 🌿 Lesson 4: if-elif-else

Sometimes two paths are not enough. With **`elif`** (short for "else if") you check further conditions one after another:

```python
experience = 750
if experience >= 1000:
    print("Master Rider!")
elif experience >= 500:
    print("Advanced Rider!")
elif experience >= 100:
    print("Beginner!")
else:
    print("Still a lot to practise...")
```

> 🐴 **Important:** `elif` **always needs a condition**. Python checks from top to bottom and runs only the **first true** path – all others are skipped. `else` at the end catches everything that is left.

That is why the **strictest condition comes first**: with `experience = 750`, `>= 100` would also be true, but `>= 500` comes earlier.
