# 📦 System Log 4: Returning values with return

So far your protocols have **printed** something. Often you want a **result** you can keep working with. That is what **`return`** is for:

```python
def calculate_usage(modules, output):
    return modules * output

usage = calculate_usage(3, 20)
print(f"Usage: {usage} kW")
print(f"Full load: {calculate_usage(10, 50)} kW")
```

**What `return` does:**
- It **ends** the function immediately
- It **sends a value back** to the place where you called the function
- You can **store** that value in a variable (`usage = ...`) or use it right away (e.g. in `print` or in a calculation)

> 💡 Think of `calculate_usage(3, 20)` as a placeholder: after the call, the result `60` simply stands there.
