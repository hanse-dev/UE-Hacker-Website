# ⚖️ System Log 5: return or print?

`print` and `return` look similar but do different things:

| | `print(...)` | `return ...` |
|---|---|---|
| Shows something on the screen | ✅ | ❌ |
| Delivers a value to the caller | ❌ | ✅ |
| Function ends immediately | ❌ | ✅ |

**Without `return`** a function automatically returns **`None`** – "nothing":

```python
def show_status():
    print("All systems running.")

result = show_status()
print(f"Return value: {result}")
```

The status is shown, but `result` is `None`. If you want to calculate with the result, you need `return`!

> ⚠️ The most common beginner mistake: you calculate something in the function but forget `return` – and get `None` back.
