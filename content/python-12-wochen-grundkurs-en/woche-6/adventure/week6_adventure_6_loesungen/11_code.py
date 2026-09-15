# Step 1 – Create the treasure list
treasures = ["Gold Ducats", "Ruby Ring", "Emerald Necklace", "Silver Cup", "Fairy Dust"]
print("Treasure list:", treasures)

# Step 2 – Add treasures
treasures.append("Dragon Scale")
treasures.append("Fairy Wing")
treasures.append("Moon Stone")
treasures.insert(0, "Legendary Sword")
print("After adding:", treasures)

# Step 3 – Remove a treasure and find a position
treasures.remove("Fairy Dust")
position = treasures.index("Ruby Ring")
print("After removal:", treasures)
print(f"Position of Ruby Ring: {position}")

# Step 4 – Sort and output
treasures.sort()
print("Sorted:", treasures)
print(f"Number of treasures: {len(treasures)}")

# Bonus – nested list
treasure_details = [
    ["Gold Ducats", 500, "rare"],
    ["Ruby Ring", 300, "very rare"],
    ["Moon Stone", 150, "common"]
]
print("\nTreasure Details:")
for treasure in treasure_details:
    print(f"  {treasure[0]}: {treasure[1]} Gold ({treasure[2]})")