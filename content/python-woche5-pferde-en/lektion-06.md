# 🧠 Lesson 6: Decisions and loops in functions

You may put everything you already know into a function: **`if`/`else`** and **loops**. With `return` you can deliver a different result depending on the situation:

```python
def check_speed(speed):
    if speed >= 20:
        return "Gallop!"
    else:
        return f"{20 - speed} km/h to go until gallop"

print(check_speed(12))
print(check_speed(25))
```

As soon as a `return` runs, the function ends – the rest is skipped.

A loop fits inside too. It calculates, and at the end `return` hands back the result:

```python
def count_jumps(laps):
    jumps = 0
    for lap in range(1, laps + 1):
        jumps += lap
    return jumps
```

> 💡 The `return` stands **after** the loop (not indented) – otherwise the function would already end after the first pass.
