# 🎁 Spell Formula 2: Returning values with return

So far your formulas have **printed** something. Often you want a **result** you can keep working with. That is what **`return`** is for:

```python
def calculate_damage(base, multiplier):
    return base * multiplier

damage = calculate_damage(10, 2)
print(f"Hit: {damage} damage")
print(f"Critical: {calculate_damage(20, 5)} damage")
```

**What `return` does:**
- It **ends** the function immediately
- It **sends a value back** to the place where you called the function
- You can **store** that value in a variable (`damage = ...`) or use it right away (e.g. in `print` or in a calculation)

> 💡 Think of `calculate_damage(10, 2)` as a placeholder: after the call, the result `20` simply stands there.
