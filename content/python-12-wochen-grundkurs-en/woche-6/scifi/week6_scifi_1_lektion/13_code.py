# Example 3: Advanced list operations
mission_types = ["Research", "Defense", "Exploration", "Research", "Defense"]

print("=== Advanced Operations ===")
print(f"Mission types list: {mission_types}")

# Unique elements (with set)
unique_types = list(set(mission_types))
print(f"Unique mission types: {unique_types}")

# Loop through a list with for
print("\nAll mission types:")
for i, m in enumerate(mission_types):
    print(f"  Position {i}: {m}")

# List comprehension (advanced)
long_names = [m for m in mission_types if len(m) > 8]
print(f"\nMission types with long names: {long_names}")