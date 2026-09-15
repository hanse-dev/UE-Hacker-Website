# Example 3: Complex archive structures
# Tuple as dictionary key
box_map = {
    (1, 1): "Thunder",
    (1, 2): "Luna",
    (2, 1): "Stormy"
}

print("=== Box Map ===")
for position, horse in box_map.items():
    print(f"Box {position}: {horse}")

# Complex training system
training = {
    "active": [
        {
            "horse": "Thunder",
            "discipline": "Dressage",
            "schedule": ("Mon", "Wed", "Fri"),
            "status": "In Progress"
        }
    ],
    "completed": [
        {
            "horse": "Luna",
            "discipline": "Western",
            "schedule": ("Tue", "Thu"),
            "status": "Success"
        }
    ]
}

print(f"\nActive trainings: {len(training['active'])}")
print(f"Completed trainings: {len(training['completed'])}")