# 🚀 Data Log 1: Creating lists

Welcome to the **Data Banks of space station Nebula-7**! Sensors, modules, crew members – the ship's AI stores everything in lists. It reports: *"Whoever collects data without ordering it only collects noise."*

So far every variable has held **one** value. With a **list** you store **many** values in a single variable:

```python
modules = ["Drive", "Sensor", "Shield", "Radar", "Radio"]
print(modules)
print(len(modules))
```

**Step by step:**
1. **`[ ]`** – square brackets create a list
2. **`,`** – commas separate the entries
3. Text goes in quotes, numbers do not: `[1, 5, 10]`
4. **`len(list)`** returns the **number** of entries
5. **`[]`** on its own is an **empty** list

> 💡 A list may mix text and numbers – but usually you collect things of the same kind.
