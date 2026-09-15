# Step 1: Treasure profile
treasure1 = {"name": "Ruby Ring", "value": 800, "location": "Dragon Cave", "rarity": "Legendary"}
print("=== TREASURE ARCHIVE ===")
for key, value in treasure1.items():
    print(f"  {key}: {value}")

# Step 2: Collect 3 treasures
treasures = [
    {"name": "Ruby Ring", "value": 800, "location": "Dragon Cave", "rarity": "Legendary"},
    {"name": "Silver Sword", "value": 350, "location": "Tower of Light", "rarity": "Rare"},
    {"name": "Golden Crown", "value": 1200, "location": "Elven Forest", "rarity": "Unique"}
]

# Step 3: Search the archive
print("\nValuable treasures (> 500 Gold):")
total_value = 0
for t in treasures:
    total_value += t["value"]
    if t["value"] > 500:
        print(f"  {t['name']}: {t['value']} Gold ({t['rarity']})")
print(f"Total value of all treasures: {total_value} Gold")

# Bonus: Sort by value
sorted_treasures = sorted(treasures, key=lambda t: t["value"], reverse=True)
print("\nSorted by value (highest first):")
for t in sorted_treasures:
    print(f"  {t['name']}: {t['value']} Gold")