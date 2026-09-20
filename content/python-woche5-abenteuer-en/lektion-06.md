# 🧠 Spell Formula 2: Decisions and loops in functions

You may put everything you already know into a function: **`if`/`else`** and **loops**. With `return` you can deliver a different result depending on the situation:

```python
def check_level(level):
    if level >= 10:
        return "Ready for the quest!"
    else:
        return f"{10 - level} more levels needed"

print(check_level(5))
print(check_level(12))
```

As soon as a `return` runs, the function ends – the rest is skipped.

A loop fits inside too. It calculates, and at the end `return` hands back the result:

```python
def sum_to(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total
```

> 💡 The `return` stands **after** the loop (not indented) – otherwise the function would already end after the first pass.
