# Example 2: Accessing dictionary elements
ship = {
    "name": "Nebula-Explorer",
    "type": "Research",
    "crew": 150,
    "speed": 0.8
}

print("=== Ship Access ===")
print(f"Ship name: {ship['name']}")
print(f"Ship type: {ship['type']}")
print(f"Crew size: {ship['crew']}")
print(f"Speed: {ship['speed']}c")

# Using the get() method (safer)
print(f"\nWith get(): {ship.get('name')}")
print(f"Non-existent key: {ship.get('spaceship', 'Unknown')}")