# Example 2: Sorting lists
numbers = [5, 2, 8, 1, 9, 3]
names = ["Zara", "Anna", "Max", "Berta", "Klaus"]

print("=== Sorting Lists ===")
print(f"Original numbers: {numbers}")
print(f"Original names: {names}")

# Sort directly with sort()
numbers.sort()
print(f"Numbers after sort(): {numbers}")

# Sort a copy with sorted()
sorted_names = sorted(names)
print(f"Names original: {names}")
print(f"Names sorted: {sorted_names}")

# Sort in reverse order
numbers.sort(reverse=True)
print(f"Numbers descending: {numbers}")

# Reverse the order with reverse()
names.reverse()
print(f"Names reversed: {names}")