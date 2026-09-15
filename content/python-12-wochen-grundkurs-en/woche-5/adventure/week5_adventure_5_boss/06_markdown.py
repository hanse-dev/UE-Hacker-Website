"""### ⭐⭐⭐⭐☆ Boss Quest 3: The Battle Simulation

Simulate a battle between two groups (heroes and monsters) with multiple rounds.

**Step 1 – Initialise battle:**
Create a function `initialise_battle(group1, group2)` that returns a starting state with both groups (name, armour, health)

**Step 2 – Calculate damage:**
Write a function `calculate_damage(base_damage, armour_strength)` that returns the actual damage (e.g. `base_damage - armour_strength/10`)

**Step 3 – Execute battle round:**
Create a function `execute_round(status)` that randomly selects an attacking group and applies damage

**Step 4 – Control battle:**
Write a function `start_battle(group_a, group_b, max_rounds)` that runs several rounds until one group is defeated or `max_rounds` is reached and print the winner, loser and remaining health at the end

**Bonus:** Add special spells that cause double damage with a small probability."""
