# ✨ Collection Spell 9: List comprehension

Turning a list into a **new** list takes several lines with a loop and `append`. A **list comprehension** does it in one:

```python
damage = [3, 7, 12, 5]
doubled = [value * 2 for value in damage]            # [6, 14, 24, 10]
big = [value for value in damage if value > 4]       # [7, 12, 5]
```

Read it from left to right: *"Take `value * 2` for every `value` in `damage`."* An `if` at the end **filters**: only matching entries go into the new list.

**Working with text:** `word.upper()` turns a text into **CAPITAL LETTERS** – that works inside a comprehension too: `[w.upper() for w in list]`.

> 💡 The original list stays unchanged – you always get a **new** list.
