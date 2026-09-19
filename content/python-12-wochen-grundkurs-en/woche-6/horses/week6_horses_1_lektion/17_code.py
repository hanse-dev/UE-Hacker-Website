# Example 1: Loop or list comprehension – same result
scores = [6, 9, 7, 10]

# With a loop and append (Weeks 4 + 6):
doubled_loop = []
for value in scores:
    doubled_loop.append(value * 2)

# With a list comprehension – just one line:
doubled = [value * 2 for value in scores]
print(f"Loop: {doubled_loop}")
print(f"Comprehension: {doubled}")

# Example 2: Transform every element
disciplines = ["Dressage", "Jumping", "Eventing", "Vaulting"]
capitals = [w.upper() for w in disciplines]
print(f"\nIn capitals: {capitals}")

# Example 3: Filter with if
long_names = [w for w in disciplines if len(w) > 7]
print(f"Long names: {long_names}")

# Example 4: Transform AND filter
big_values = [value * 2 for value in scores if value > 7]
print(f"Doubled values above 7: {big_values}")

# The original list stays unchanged
print(f"\nOriginal (Scores): {scores}")