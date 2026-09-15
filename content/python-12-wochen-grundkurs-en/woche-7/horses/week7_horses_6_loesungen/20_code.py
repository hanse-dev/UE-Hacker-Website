import random
import math

horse_names = ["Thunder", "Luna", "Blitz", "Silver"]

# Step 1: Determine weights
print("=== FEED CALCULATOR ===")
print("Horse weights:")
horse_data = []
for name in horse_names:
    weight = random.randint(300, 600)
    horse_data.append((name, weight))
    print(f"  {name}: {weight} kg")

# Step 2: Calculate daily rations (2% body weight)
print("\nDaily rations (2% body weight):")
total_day = 0
rations = []
for name, weight in horse_data:
    ration = math.ceil(weight * 0.02)
    rations.append((name, ration))
    total_day += ration
    print(f"  {name}: {ration} kg/day")

# Step 3: Weekly plan
total_week = total_day * 7
print(f"\nTotal feed per day:  {total_day} kg")
print(f"Total feed per week: {total_week} kg")

# Bonus: Bags (25 kg per bag)
bags = math.ceil(total_week / 25)
print(f"\nBonus: Feed bags needed (25 kg each): {bags} bags")