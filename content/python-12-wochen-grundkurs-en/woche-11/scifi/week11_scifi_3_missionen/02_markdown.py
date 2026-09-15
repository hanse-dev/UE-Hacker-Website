"""### ⭐⭐☆☆☆ Mission 1: The Robot Hierarchy

The robotics department needs a clean hierarchy for all robot types!

**Step 1 – Create base class Robot:**
Create `class Robot:` with `__init__(self, id, name, energy_status)`; assign the attributes and add a method `activate()` that prints a status message

**Step 2 – Create child classes:**
Create `class Android(Robot):`, `class Drone(Robot):`, `class Cyborg(Robot):` and use `super().__init__(id, name, energy_status)` in each constructor *(= special method that runs automatically when an object is created)* and add a special attribute

**Step 3 – Create an object from each class:**
Create one Android, Drone and Cyborg object each and call `activate()` and the special method for each object

**Bonus:** Add a fourth class that inherits from a child class (e.g. CombatAndroid from Android)."""
