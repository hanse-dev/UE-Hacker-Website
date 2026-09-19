# ⚖️ Magic Formula 5: Nested Conditions

An `if` can **contain** another `if`. This is called **nesting** – like doors behind doors. The inner check only happens if the outer one was true.

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

**The power of indentation:** Every additional level needs **4 more spaces**. The indentation shows Python (and you) which `else` belongs to which `if`.

> Tip: You can often write nested conditions with `and` instead. Nesting pays off when you want to print something between the checks.
