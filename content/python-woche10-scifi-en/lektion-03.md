# 🚀 System Protocol 3: Methods and self

A **method** is a function **inside** a class. It can use the object through **`self`**:

```python
class Robot:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}.")

robot = Robot("Nova")
robot.introduce()
```

1. The method is **indented** inside the class and has **`self`** as its first parameter
2. When calling it you write **`robot.introduce()`** – Python fills in `self` itself
3. With **`self.name`** the method reaches the attributes of **this** object

> 💡 Python translates `robot.introduce()` into `Robot.introduce(robot)`.
