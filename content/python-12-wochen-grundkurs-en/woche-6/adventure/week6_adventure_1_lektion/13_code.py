# Example 3: Useful list operations
monsters = ["Goblin", "Orc", "Troll", "Dragon", "Goblin", "Orc"]

print("=== List Operations ===")
print(f"Monster list: {monsters}")
print(f"Number of monsters: {len(monsters)}")

# Unique elements: set() removes duplicates
# set is a collection without order and without duplicates
unique_monsters = list(set(monsters))
print(f"Unique monsters: {unique_monsters}")

# Index and value at the same time with enumerate()
print("\nAll monsters with position:")
for index, m in enumerate(monsters):
    print(f"  Position {index}: {m}")
