# Example 3: Advanced list operations
disciplines = ["Dressage", "Show Jumping", "Western", "Dressage", "Western"]

print("=== Advanced Operations ===")
print(f"Disciplines list: {disciplines}")

# Unique elements (with set)
unique_disciplines = list(set(disciplines))
print(f"Unique disciplines: {unique_disciplines}")

# Iterate through list with for loop
print("\nAll disciplines:")
for i, d in enumerate(disciplines):
    print(f"  Position {i}: {d}")

# List comprehension (advanced)
long_names = [d for d in disciplines if len(d) > 6]
print(f"\nDisciplines with long names: {long_names}")