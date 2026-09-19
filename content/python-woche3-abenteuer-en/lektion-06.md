# ⚖️ Magic Formula 5: Nested Conditions

An `if` can contain **another `if`** inside it. This is called **nesting**. The inner decision is only made when the outer condition was true.

```python
door_locked = True
right_key = True

if door_locked:
    print("The door is locked.")
    if right_key:
        print("The key fits - the door opens!")
    else:
        print("This key does not fit.")
else:
    print("The door is already open.")
```

> ⚠️ Every nesting level needs **one more level of indentation** (4 more spaces). The indentation shows Python which code belongs to which path – so be careful!

Read it like a tree: first the outer decision (`door_locked`), then – only inside that branch – the inner decision (`right_key`).
