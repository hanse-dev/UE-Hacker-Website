# ➖ Data Log 4: Removing entries

```python
modules = ["Drive", "Sensor", "Shield", "Radar", "Radio"]
modules.remove("Radar")      # removes the first entry with this value
last = modules.pop()          # removes the LAST one and returns it
first = modules.pop(0)        # removes the entry at index 0 and returns it
modules.clear()               # empties the whole list
```

- **`remove(x)`** removes the first entry with the **value** `x` (if there is none, you get an error)
- **`pop()`** removes the **last** entry, **`pop(index)`** the one at that **position** – and hands it back as a result, so you can store it in a variable
- **`clear()`** deletes everything

> 💡 `remove` asks for the **value**, `pop` asks for the **position**.
