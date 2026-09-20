# ➖ Lesson 4: Removing entries

```python
horses = ["Stormwind", "Lightning", "Luna", "Fox", "Balu"]
horses.remove("Fox")      # removes the first entry with this value
last = horses.pop()          # removes the LAST one and returns it
first = horses.pop(0)        # removes the entry at index 0 and returns it
horses.clear()               # empties the whole list
```

- **`remove(x)`** removes the first entry with the **value** `x` (if there is none, you get an error)
- **`pop()`** removes the **last** entry, **`pop(index)`** the one at that **position** – and hands it back as a result, so you can store it in a variable
- **`clear()`** deletes everything

> 💡 `remove` asks for the **value**, `pop` asks for the **position**.
