# Step 1 - Record the treasures
chest1_name = "Ruby Chest"
chest1_gold = 320
chest2_name = "Emerald Chest"
chest2_gold = 480
chest3_name = "Sapphire Chest"
chest3_gold = 210
chest4_name = "Diamond Chest"
chest4_gold = 750
chest5_name = "Gold Chest"
chest5_gold = 390
chest6_name = "Silver Chest"
chest6_gold = 160
chest7_name = "Amethyst Chest"
chest7_gold = 290
chest8_name = "Topaz Chest"
chest8_gold = 440

# Step 2 - Create a treasure log
print("=== TREASURE ROOM LOG ===")
print(f"{chest1_name}: {chest1_gold} gold")
print(f"{chest2_name}: {chest2_gold} gold")
print(f"{chest3_name}: {chest3_gold} gold")
print(f"{chest4_name}: {chest4_gold} gold")
print(f"{chest5_name}: {chest5_gold} gold")
print(f"{chest6_name}: {chest6_gold} gold")
print(f"{chest7_name}: {chest7_gold} gold")
print(f"{chest8_name}: {chest8_gold} gold")
print()

# Step 3 - Calculate the average
total_value = chest1_gold + chest2_gold + chest3_gold + chest4_gold + chest5_gold + chest6_gold + chest7_gold + chest8_gold
average = total_value / 8
print(f"Average value: {average} gold")

# Step 4 - Find the richest chest
highest_value = chest4_gold
richest_chest = chest4_name
print(f"Richest chest: {richest_chest} with {highest_value} gold")

# Step 5 - Total value
print(f"Total value of all chests: {total_value} gold")

# Bonus: chests below the average
below_average = 0
if chest1_gold < average:
    below_average += 1
if chest2_gold < average:
    below_average += 1
if chest3_gold < average:
    below_average += 1
if chest4_gold < average:
    below_average += 1
if chest5_gold < average:
    below_average += 1
if chest6_gold < average:
    below_average += 1
if chest7_gold < average:
    below_average += 1
if chest8_gold < average:
    below_average += 1
print(f"Chests below the average: {below_average}")
