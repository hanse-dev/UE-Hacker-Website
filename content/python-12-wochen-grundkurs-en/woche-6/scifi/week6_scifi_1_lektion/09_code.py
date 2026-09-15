# Example 3: Combining lists
ships = ["Nebula-Explorer", "Star-Fighter"]
crew = ["Captain Alex", "Dr. Zara"]
missions = ["Research", "Defense", "Exploration"]

print("=== Combining Lists ===")
print(f"Ships: {ships}")
print(f"Crew: {crew}")
print(f"Missions: {missions}")

# Combine with + operator
all_items = ships + crew + missions
print(f"All combined: {all_items}")

# Add one list to another with extend()
ships.extend(crew)
print(f"Ships extended: {ships}")