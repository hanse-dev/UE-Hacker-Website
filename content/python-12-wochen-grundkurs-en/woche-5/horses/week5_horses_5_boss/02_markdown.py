"""### ⭐⭐⭐⭐☆ Boss Quest 1: The Training Generator

Build a system that automatically generates, rates and stores training sessions for horses.

**Step 1 – Generate training names:**
Write a function `generate_training_name(horse_type, difficulty)` that forms a name from type and difficulty (e.g. `\"JUMPING-L3\"`) and return the name as a string

**Step 2 – Calculate intensity:**
Create a function `calculate_intensity(duration, horse_type)` that returns a value between 0 and 100 and use different factors per `horse_type` (e.g. `\"Sport Horse\"`, `\"Leisure Horse\"`)

**Step 3 – Create training data:**
Write a function `create_training(horse_type, difficulty, duration)` that returns a dictionary with name, type, difficulty and intensity and use your two previous functions

**Step 4 – Manage training plan:**
Create a list `training_plan` and write a function `save_training(plan, training)` that appends the training

**Step 5 – Use the generator:**
Generate at least 5 trainings with different parameters and save them in the plan and print a small statistic (count, average intensity)

**Bonus:** Add a function that prints all trainings sorted by intensity."""
