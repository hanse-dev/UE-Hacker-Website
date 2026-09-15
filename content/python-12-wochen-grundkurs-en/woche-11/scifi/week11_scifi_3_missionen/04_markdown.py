"""### ⭐⭐⭐☆☆ Mission 2: The Polymorphic Weapon System

The weapons department needs a system for different weapon types!

**Step 1 – Create three weapon classes:**
Create `class Laser:`, `class Plasma:`, `class Ion:` each with `__init__(self, name)` and a method `fire(self)` and each `fire()` outputs a different message (e.g. \"Pew! Laser fires!\", \"Hiss! Plasma released!\", \"Bzz! Ion beam!\")

**Step 2 – Polymorphic function:**
Create a function `test_weapon(weapon)` that calls `weapon.fire()` and the function should work with all three weapon types

**Step 3 – Test all weapons:**
Create one Laser, Plasma and Ion object each and call `test_weapon()` for each weapon

**Bonus:** Create a weapon factory function that creates the appropriate weapon based on type."""
