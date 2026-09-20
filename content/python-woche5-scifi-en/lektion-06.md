# 🧠 System Log 6: Decisions and loops in functions

You may put everything you already know into a function: **`if`/`else`** and **loops**. With `return` you can deliver a different result depending on the situation:

```python
def check_shield(shield):
    if shield >= 50:
        return "Shield stable!"
    else:
        return f"{50 - shield} % to go until stable"

print(check_shield(20))
print(check_shield(75))
```

As soon as a `return` runs, the function ends – the rest is skipped.

A loop fits inside too. It calculates, and at the end `return` hands back the result:

```python
def count_signals(sectors):
    signals = 0
    for sector in range(1, sectors + 1):
        signals += sector
    return signals
```

> 💡 The `return` stands **after** the loop (not indented) – otherwise the function would already end after the first pass.
