"""### ⭐⭐⭐⭐☆ Boss Quest 3: The Battle Simulation

Build a simplified battle simulation system for two fleets with clearly separated functions.

**Step 1 – Initialise battle:**
Create a function `initialise_battle(fleet1, fleet2)` that returns a starting state and store names, shields and hull of both fleets

**Step 2 – Calculate damage:**
Write a function `calculate_damage(base_damage, shield_strength)` that returns the actual damage (e.g. `base_damage - shield_strength/10`) and use this function in the battle rounds

**Step 3 – Execute battle round:**
Create a function `execute_round(status)` that randomly selects an attacking fleet and applies damage

**Step 4 – Control simulation:**
Write a function `start_simulation(fleet1, fleet2, max_rounds)` that runs several rounds until one fleet is defeated or `max_rounds` is reached and print a summary with winner, loser and remaining hull at the end

**Bonus:** Add special weapons that cause double damage with a small probability."""
