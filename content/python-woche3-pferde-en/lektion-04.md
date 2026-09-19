# 🐴 Lesson 4: if-elif-else

Sometimes there are more than two paths. With `elif` (short for "else if") you check further conditions one after another:

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

- Python checks from top to bottom and runs **only the first** path whose condition is true. All others are skipped.
- `elif` **always needs a condition**, `else` never does.
- `else` at the end catches everything that is left (it is optional).

> 💡 **Watch the order!** Put the strictest condition first. Otherwise `experience >= 100` would already catch a rider with 750 points.
