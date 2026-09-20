# 🔢 Lesson 2: Accessing entries

Every entry has a number, the **index**. Important: counting starts at **0**!

```python
horses = ["Stormwind", "Lightning", "Luna", "Fox", "Balu"]
print(horses[0])    # first entry
print(horses[1])    # second entry
print(horses[-1])   # last entry
horses[0] = "Stella"   # replace an entry
```

**Remember:**
- `list[0]` is the **first**, `list[-1]` the **last** entry, `list[-2]` the second to last
- An index that does not exist (e.g. `list[5]` with 5 entries) gives an **IndexError**
- With `list[1] = "new"` you **replace** an entry

**Lists in lists:** An entry may itself be a list. With two indices you reach inside: `party[1][0]` is the first entry of the second sub-list.

**Slices:** With `list[start:stop]` you take a **part** of the list – the end index is **not** included any more:

```python
print(horses[0:3])    # index 0, 1, 2
print(horses[-2:])    # the last two
print(horses[1::2])   # every second entry, from index 1
```
