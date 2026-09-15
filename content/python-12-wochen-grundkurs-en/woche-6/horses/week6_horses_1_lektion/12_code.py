# Example 2: Sorting lists
level = [5, 2, 8, 1, 9, 3]
names = ["Zara", "Anna", "Max", "Berta", "Klaus"]

print("=== Sorting Lists ===")
print(f"Original level: {level}")
print(f"Original names: {names}")

# Sort directly with sort()
level.sort()
print(f"Level after sort(): {level}")

# Sort a copy with sorted()
sorted_names = sorted(names)
print(f"Names original: {names}")
print(f"Names sorted: {sorted_names}")

# Sort in reverse
level.sort(reverse=True)
print(f"Level descending: {level}")

# Reverse order with reverse()
names.reverse()
print(f"Names reversed: {names}")