# Example 1: Searching in lists
inventory = ["Sword", "Shield", "Potion", "Bow", "Sword", "Arrows"]

print("=== Searching in Lists ===")
print(f"Inventory: {inventory}")

# Find position with index()
shield_position = inventory.index("Shield")
print(f"Shield at position: {shield_position}")

# Check if present with in
has_bow = "Bow" in inventory
has_staff = "Magic Staff" in inventory
print(f"Bow present: {has_bow}")
print(f"Magic Staff present: {has_staff}")

# Count with count()
sword_count = inventory.count("Sword")
print(f"Number of swords: {sword_count}")