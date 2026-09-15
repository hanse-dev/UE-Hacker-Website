# Step 1: Ship dictionary
ship = {
    "name": "Nebula-7",
    "type": "Research Ship",
    "crew": 150,
    "speed": 9.5
}
print(ship)

# Step 2: Change values
ship["crew"] = 165
ship["status"] = "active"
print(f"Crew: {ship['crew']}")
print(f"Status: {ship['status']}")

# Step 3: Output
print("\n=== Ship Data ===")
for key, value in ship.items():
    print(f"  {key}: {value}")