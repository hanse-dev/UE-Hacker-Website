# Example 2: Removing elements
inventory = ["Sword", "Shield", "Potion", "Bow", "Arrows", "Potion"]
print(f"Original inventory: {inventory}")

# Remove first occurrence with remove()
inventory.remove("Potion")
print(f"After remove('Potion'): {inventory}")

# Remove and return last element with pop()
last_item = inventory.pop()
print(f"After pop(): {inventory}")
print(f"Removed item: {last_item}")

# Remove a specific element with pop(index)
second_item = inventory.pop(1)
print(f"After pop(1): {inventory}")
print(f"Removed item: {second_item}")

# Clear everything with clear()
inventory.clear()
print(f"After clear(): {inventory}")