# Step 1: System list
systems = ["Propulsion", "Shield", "Weapons", "Sensors", "Life Support"]
print(systems)
print(f"Number of systems: {len(systems)}")

# Step 2: Add & remove systems
systems.append("Communications")
systems.insert(0, "Emergency Reactor")
failed = systems.pop(2)
print(f"System failed: {failed}")
print(systems)

# Step 3: Search & sort
systems.sort()
print(f"Sorted: {systems}")
print(f"'Shield' at index: {systems.index('Shield')}")