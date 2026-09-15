# Step 1 - Fusing two 🔥 Fire Stones
first_name = "Luna"
last_name = "Silvermoon"
name = f"{first_name} {last_name}"
print(f"Fused name: {name}")

# Step 2 - Fusing two 🪨 Earth Stones
gold_a = 150
gold_b = 75
gold_total = gold_a + gold_b
print(f"Fused gold: {gold_total}")

# Step 3 - Fusing two 💧 Water Stones
damage_a = 23.5
damage_b = 31.0
damage_average = (damage_a + damage_b) / 2
print(f"Average damage: {damage_average}")

# Step 4 - Fusing 🔥 Fire and 🪨 Earth
hero = "Thorin"
level = 12
message = hero + " is Level " + str(level)
print(f"Fused message: {message}")

# Bonus: without str() Python would raise a TypeError:
# TypeError: can only concatenate str (not "int") to str
