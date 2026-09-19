# 🪆 Lesson 6: Nested conditions

A condition may **contain another condition** – this is called **nesting**. Each additional level is **indented one step further**:

```python
stable_door_locked = True
right_key = True

if stable_door_locked:
    print("The stable door is locked.")
    if right_key:
        print("The key fits – the stable door opens!")
    else:
        print("This key does not fit.")
else:
    print("The stable door is already open.")
```

The inner question is only asked if the outer one was answered with `True`. Each `else` belongs to the `if` that is **indented equally far**.

> ⚠️ Watch the indentation closely – it decides which code belongs to which condition!
