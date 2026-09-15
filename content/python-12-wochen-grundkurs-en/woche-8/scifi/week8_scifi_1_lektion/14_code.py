# Example 3: Complex data structures
# Tuples as dictionary keys
galaxy_map = {
    (100, 200): "Star A",
    (300, 400): "Star B",
    (500, 600): "Star C"
}

print("=== Galaxy Map ===")
for coordinate, star in galaxy_map.items():
    print(f"{coordinate}: {star}")

# Complex mission system
missions = {
    "active": [
        {
            "id": 1,
            "target": (100, 200, 300),
            "crew": ["Alex", "Zara"],
            "status": "In Progress"
        }
    ],
    "completed": [
        {
            "id": 2,
            "target": (400, 500, 600),
            "crew": ["Nova"],
            "status": "Success"
        }
    ]
}

print(f"\nActive missions: {len(missions['active'])}")
print(f"Completed missions: {len(missions['completed'])}")