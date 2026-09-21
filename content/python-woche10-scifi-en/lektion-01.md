# 🚀 System Protocol 1: Classes and Objects

Welcome to **Space Station Nebula-7**! Every machine is built from a **blueprint**: from one blueprint you get as many robots and tools as you like.

With **`class`** you create a blueprint, with **`Robot()`** you build an **object** from it. You attach properties (**attributes**) with a dot:

```python
class Robot:
    pass

robot = Robot()
robot.name = "Nova"
robot.level = 1
print(robot.name, robot.level)
```

1. **`class Robot:`** – a class name starts with a **capital letter**
2. **`pass`** means "nothing inside yet"
3. **`robot.name = ...`** sets an attribute, **`robot.name`** reads it

> 💡 Every object stands on its own: changing one leaves the other unchanged.
