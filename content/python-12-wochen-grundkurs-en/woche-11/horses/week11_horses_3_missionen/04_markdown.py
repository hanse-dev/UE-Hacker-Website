"""### ⭐⭐⭐☆☆ Mission 2: The Polymorphic Training

The riding school needs a system for different training methods!

**Step 1 – Create three training classes:**
Create `class Dressage:`, `class Jumping:`, `class Western:` each with `__init__(self, name)` and a method `training(self)` and each `training()` outputs a different exercise (e.g. \"Practice Piaffe!\", \"Jump the course!\", \"Ride the slalom!\")

**Step 2 – Polymorphic function:**
Create a function `train_horse(horse, training)` that calls `training.training()` (or outputs the exercise) and the function should work with all three training types

**Step 3 – Test all trainings:**
Create one object each of Dressage, Jumping and Western and call the polymorphic function for each training type

**Bonus:** Create a trainer factory function that creates the matching training based on type."""
