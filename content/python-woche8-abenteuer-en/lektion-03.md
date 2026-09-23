# ⚔️ Archive Spell 3: Safe access with get() and in

If a key is missing, `dict[key]` raises a **KeyError**. Two safe ways:

```python
print(hero.get("name"))         # Aria
print(hero.get("mana"))       # None – no error
print(hero.get("mana", 0))    # 0 – your own default value

print("name" in hero)           # True – checks the KEYS
print("mana" in hero)         # False
```

**`in`** always checks the **keys** of a dictionary, never the values.
