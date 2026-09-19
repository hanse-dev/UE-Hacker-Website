# Example 1: Loop or list comprehension – same result
energy = [40, 75, 20, 90]

# With a loop and append (Weeks 4 + 6):
doubled_loop = []
for value in energy:
    doubled_loop.append(value * 2)

# With a list comprehension – just one line:
doubled = [value * 2 for value in energy]
print(f"Loop: {doubled_loop}")
print(f"Comprehension: {doubled}")

# Example 2: Transform every element
systems = ["Weapon system", "Shield", "Propulsion", "Sensor"]
capitals = [w.upper() for w in systems]
print(f"\nIn capitals: {capitals}")

# Example 3: Filter with if
long_names = [w for w in systems if len(w) > 6]
print(f"Long names: {long_names}")

# Example 4: Transform AND filter
big_values = [value * 2 for value in energy if value > 50]
print(f"Doubled values above 50: {big_values}")

# The original list stays unchanged
print(f"\nOriginal (Energy): {energy}")