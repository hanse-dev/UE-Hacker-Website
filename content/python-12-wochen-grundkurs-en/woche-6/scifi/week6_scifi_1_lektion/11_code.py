# Example 1: Searching in lists
systems = ["Weapon System", "Shield System", "Propulsion System", "Life Support", "Weapon System", "Propulsion System"]

print("=== Searching in Lists ===")
print(f"System list: {systems}")

# Find position with index()
shield_position = systems.index("Shield System")
print(f"Shield System at position: {shield_position}")

# Check if present with in
has_propulsion = "Propulsion System" in systems
has_teleporter = "Teleporter" in systems
print(f"Propulsion System present: {has_propulsion}")
print(f"Teleporter present: {has_teleporter}")

# Count with count()
weapon_count = systems.count("Weapon System")
print(f"Number of Weapon Systems: {weapon_count}")