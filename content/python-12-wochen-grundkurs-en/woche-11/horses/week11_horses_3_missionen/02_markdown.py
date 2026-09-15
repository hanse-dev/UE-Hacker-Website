"""### ⭐⭐☆☆☆ Mission 1: The Horse Hierarchy

The stud farm needs a clean hierarchy for all horse breeds!

**Step 1 – Create base class Horse:**
Create `class Horse:` with `__init__(self, name, age, gender)`; assign the attributes and add a method `neigh()` that prints a message

**Step 2 – Create child classes:**
Create `class RidingHorse(Horse):`, `class Coldblood(Horse):`, `class Pony(Horse):` and use `super().__init__(name, age, gender)` in each constructor *(= special method that runs automatically when an object is created)* and add a special attribute

**Step 3 – Create an object of each class:**
Create one object each of RidingHorse, Coldblood and Pony and call `neigh()` and the special method for each object

**Bonus:** Add a fourth class that inherits from a child class (e.g. DressageHorse from RidingHorse)."""
