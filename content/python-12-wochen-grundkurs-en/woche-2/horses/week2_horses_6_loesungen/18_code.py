# Step 1 – Record feed (8 sacks)
sack1_type = "Oats"
sack1_weight = 25.0
sack2_type = "Hay"
sack2_weight = 40.5
sack3_type = "Barley"
sack3_weight = 18.0
sack4_type = "Maize Meal"
sack4_weight = 32.0
sack5_type = "Bran"
sack5_weight = 15.5
sack6_type = "Alfalfa"
sack6_weight = 28.0
sack7_type = "Sugar Beet Pulp"
sack7_weight = 22.0
sack8_type = "Concentrate"
sack8_weight = 12.5

# Step 2 – Feed protocol
print("=== FEED ROOM PROTOCOL ===")
print(f"Sack 1 – {sack1_type}: {sack1_weight} kg")
print(f"Sack 2 – {sack2_type}: {sack2_weight} kg")
print(f"Sack 3 – {sack3_type}: {sack3_weight} kg")
print(f"Sack 4 – {sack4_type}: {sack4_weight} kg")
print(f"Sack 5 – {sack5_type}: {sack5_weight} kg")
print(f"Sack 6 – {sack6_type}: {sack6_weight} kg")
print(f"Sack 7 – {sack7_type}: {sack7_weight} kg")
print(f"Sack 8 – {sack8_type}: {sack8_weight} kg")
print()

# Step 3 – Average
total_weight = sack1_weight + sack2_weight + sack3_weight + sack4_weight + sack5_weight + sack6_weight + sack7_weight + sack8_weight
average = total_weight / 8
print(f"Average weight: {average} kg")

# Step 4 – Heaviest sack
print(f"Heaviest sack: {sack2_type} with {sack2_weight} kg")

# Step 5 – Total weight
print(f"Total weight: {total_weight} kg")

# Bonus
below_average = 0
if sack1_weight < average: below_average += 1
if sack2_weight < average: below_average += 1
if sack3_weight < average: below_average += 1
if sack4_weight < average: below_average += 1
if sack5_weight < average: below_average += 1
if sack6_weight < average: below_average += 1
if sack7_weight < average: below_average += 1
if sack8_weight < average: below_average += 1
print(f"Sacks below average: {below_average}")