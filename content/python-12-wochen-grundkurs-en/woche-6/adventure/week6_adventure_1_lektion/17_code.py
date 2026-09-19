# Example 1: Loop or list comprehension – same result
damage = [3, 7, 12, 5]

# With a loop and append (Weeks 4 + 6):
doubled_loop = []
for value in damage:
    doubled_loop.append(value * 2)

# With a list comprehension – just one line:
doubled = [value * 2 for value in damage]
print(f"Loop: {doubled_loop}")
print(f"Comprehension: {doubled}")

# Example 2: Transform every element
inventory = ["Potion", "Sword", "Key", "Treasure", "Map"]
capitals = [w.upper() for w in inventory]
print(f"\nShouted: {capitals}")

# Example 3: Filter with if
long_names = [w for w in inventory if len(w) > 5]
print(f"Long names: {long_names}")

# Example 4: Transform AND filter
big_values = [value * 2 for value in damage if value > 4]
print(f"Doubled values above 4: {big_values}")

# The original list stays unchanged
print(f"\nOriginal (Damage): {damage}")