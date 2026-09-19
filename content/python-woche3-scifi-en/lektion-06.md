# 📟 System Protocol 6: Nested Conditions

An `if` condition may **contain** another `if` condition – this is called **nesting**. That way you first make a rough decision, then a fine one.

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

**Every extra level needs another level of indentation.** The indentation shows you and Python which `else` belongs to which `if`: the inner `else` is level with the inner `if`, the outer `else` is level with the outer `if`.

> 📡 **Remember:** First the outer condition, then the inner one. If the outer one is false, the inner one is not even checked.

🎉 You have learned all the protocols of this week – now you are ready for debug, missions and the extra challenges!
