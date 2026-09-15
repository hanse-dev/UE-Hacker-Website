# Step 1 – Create the inventory list
inventory = ["Long Sword", "Wooden Shield", "Healing Potion", "Leather Boots", "Iron Helmet"]
print("Inventory:", inventory)
print(f"Number of items: {len(inventory)}")

# Step 2 – Add items
inventory.append("Fire Bow")
inventory.insert(0, "Mage Staff")
print("After adding:", inventory)

# Step 3 – Remove and search items
inventory.remove("Wooden Shield")
last = inventory.pop()
print(f"Removed item (pop): {last}")
position = inventory.index("Healing Potion")
print(f"Position of Healing Potion: {position}")
print(f"Contains Mage Staff: {'Mage Staff' in inventory}")
print("Current inventory:", inventory)

# Step 4 – Statistics
print(f"\nNumber of items: {len(inventory)}")
print(f"Current inventory: {inventory}")
print("Status: Inventory ready for the adventure!")

# Bonus – items with values
values = [200, 150, 50, 90]
item_value_pairs = list(zip(inventory, values))
item_value_pairs.sort(key=lambda x: x[1], reverse=True)
print("\nInventory sorted by value:")
for item, value in item_value_pairs:
    print(f"  {item}: {value} Gold")