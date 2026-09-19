# 📟 System Protocol 5: Nested Conditions

An `if` can contain **another `if`** inside it – this is called **nesting**. The inner decision is only reached if the outer condition was true.

```python
airlock_locked = True
right_code = True

if airlock_locked:
    print("The airlock is locked.")
    if right_code:
        print("The code is correct – the airlock opens!")
    else:
        print("Wrong code! Access denied.")
else:
    print("The airlock is already open.")
```

> ⚠️ **Important:** Every extra nesting level needs **one more level of indentation** (four more spaces). Indentation decides which `else` belongs to which `if`!
