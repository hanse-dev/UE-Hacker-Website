# 🔍 Exercises with append() and insert()

# Example 1: Adding elements
magic_bag = []
print(f"Empty magic bag: {magic_bag}")

# Add to end with append()
magic_bag.append("Gold Ring")
print(f"After append: {magic_bag}")

magic_bag.append("Magic Wand")
magic_bag.append("Healing Potion")
print(f"Fully filled: {magic_bag}")

# Insert at a specific position with insert()
magic_bag.insert(0, "Key")  # At the beginning
print(f"After insert(0): {magic_bag}")

magic_bag.insert(2, "Amulet")  # At position 2
print(f"After insert(2): {magic_bag}")