# 🎁 Lesson 4: Returning values with return

So far your routines have **printed** something. Often you want a **result** you can keep working with. That is what **`return`** is for:

```python
def calculate_distance(laps, length):
    return laps * length

distance = calculate_distance(3, 200)
print(f"Distance: {distance} m")
print(f"Long lap: {calculate_distance(5, 400)} m")
```

**What `return` does:**
- It **ends** the function immediately
- It **sends a value back** to the place where you called the function
- You can **store** that value in a variable (`distance = ...`) or use it right away (e.g. in `print` or in a calculation)

> 💡 Think of `calculate_distance(3, 200)` as a placeholder: after the call, the result `600` simply stands there.
