# 🔢 Data Log 2: Accessing entries

Every entry has a number, the **index**. Important: counting starts at **0**!

```python
modules = ["Drive", "Sensor", "Shield", "Radar", "Radio"]
print(modules[0])    # first entry
print(modules[1])    # second entry
print(modules[-1])   # last entry
modules[0] = "Core"   # replace an entry
```

**Remember:**
- `list[0]` is the **first**, `list[-1]` the **last** entry, `list[-2]` the second to last
- An index that does not exist (e.g. `list[5]` with 5 entries) gives an **IndexError**
- With `list[1] = "new"` you **replace** an entry

**Lists in lists:** An entry may itself be a list. With two indices you reach inside: `party[1][0]` is the first entry of the second sub-list.
