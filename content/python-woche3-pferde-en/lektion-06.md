# 🐴 Lesson 6: Nested Conditions

An `if` can contain **another `if`** – this is called **nesting**. The inner decision is only reached when the outer condition is true.

```python
stable_door_locked = True
right_key = True

if stable_door_locked:
    print("The stable door is locked.")
    if right_key:
        print("The key fits - the stable door opens!")
    else:
        print("This key does not fit.")
else:
    print("The stable door is already open.")
```

> 🐴 **Important:** every new nesting level needs **one more level of indentation** (four more spaces). The indentation shows Python which `else` belongs to which `if`.
