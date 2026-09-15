"""### ⭐⭐☆☆☆ Mission 1: The Character Hierarchy

The Guild needs a clean hierarchy for all character classes!

**Step 1 – Create the base class Character:**
Create `class Character:` with `__init__(self, name, level, hp)`; assign the attributes and add a method `introduce()` that prints a message

**Step 2 – Create child classes:**
Create `class Warrior(Character):`, `class Mage(Character):`, `class Rogue(Character):` and in each constructor *(= special method that runs automatically when an object is created)* use `super().__init__(name, level, hp)` and add a special attribute

**Step 3 – Create an object of each class:**
Create one Warrior, one Mage, and one Rogue and call `introduce()` and the special method for each object

**Bonus:** Add a fourth class that inherits from a child class (e.g. Paladin from Warrior)."""
