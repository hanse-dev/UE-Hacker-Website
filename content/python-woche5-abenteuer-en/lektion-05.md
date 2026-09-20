# ⚖️ Spell Formula 2: return or print?

`print` and `return` look similar but do different things:

| | `print(...)` | `return ...` |
|---|---|---|
| Shows something on the screen | ✅ | ❌ |
| Delivers a value to the caller | ❌ | ✅ |
| Function ends immediately | ❌ | ✅ |

**Without `return`** a function automatically returns **`None`** – "nothing":

```python
def show_inventory():
    print("Sword, Shield, Healing Potion")

result = show_inventory()
print(f"Return value: {result}")
```

The inventory is shown, but `result` is `None`. If you want to calculate with the result, you need `return`!

> ⚠️ The most common beginner mistake: you calculate something in the function but forget `return` – and get `None` back.
