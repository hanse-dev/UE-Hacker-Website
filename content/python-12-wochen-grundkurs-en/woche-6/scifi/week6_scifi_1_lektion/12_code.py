# Example 2: Sorting lists
priorities = [5, 2, 8, 1, 9, 3]
sectors = ["Zeta", "Alpha", "Gamma", "Beta", "Delta"]

print("=== Sorting Lists ===")
print(f"Original priorities: {priorities}")
print(f"Original sectors: {sectors}")

# Sort directly with sort()
priorities.sort()
print(f"Priorities after sort(): {priorities}")

# Sort a copy with sorted()
sorted_sectors = sorted(sectors)
print(f"Sectors original: {sectors}")
print(f"Sectors sorted: {sorted_sectors}")

# Sort in reverse
priorities.sort(reverse=True)
print(f"Priorities descending: {priorities}")

# Reverse order with reverse()
sectors.reverse()
print(f"Sectors reversed: {sectors}")