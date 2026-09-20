# ⚖️ Lesson 5: return or print?

`print` and `return` look similar but do different things:

| | `print(...)` | `return ...` |
|---|---|---|
| Shows something on the screen | ✅ | ❌ |
| Delivers a value to the caller | ❌ | ✅ |
| Function ends immediately | ❌ | ✅ |

**Without `return`** a function automatically returns **`None`** – "nothing":

```python
def show_stable_plan():
    print("Box 1: Stormwind, Box 2: Luna")

result = show_stable_plan()
print(f"Return value: {result}")
```

The stable plan is shown, but `result` is `None`. If you want to calculate with the result, you need `return`!

> ⚠️ The most common beginner mistake: you calculate something in the function but forget `return` – and get `None` back.
