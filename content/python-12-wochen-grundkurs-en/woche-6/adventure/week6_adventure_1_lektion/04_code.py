# Example 2: Accessing list elements
inventory = ["Sword", "Shield", "Potion", "Bow", "Arrows"]

print("=== Inventory Access ===")
print(f"Full inventory: {inventory}")
print(f"First item: {inventory[0]}")
print(f"Second item: {inventory[1]}")
print(f"Last item: {inventory[-1]}")

# Length of the list
print(f"Number of items: {len(inventory)}")

# Slicing (sections)
print(f"First 3 items: {inventory[0:3]}")
print(f"Last 2 items: {inventory[-2:]}")