# Example 3: Complex structures
# Artifact (Tuple) as dictionary key
treasure_map = {
    (100, 200): "Gold Chest",
    (300, 400): "Magic Chest",
    (500, 600): "Artifact Chest"
}

print("=== Treasure Map (Tuple as Key) ===")
for position, treasure in treasure_map.items():
    print(f"{position}: {treasure}")

# Complex quest system
quests = {
    "active": [
        {
            "id": 1,
            "goal": "Defeat dragon",
            "reward": ("Gold", 1000, "XP", 500),
            "status": "In Progress"
        }
    ],
    "completed": [
        {
            "id": 2,
            "goal": "Find treasure",
            "reward": ("Silver", 500, "XP", 250),
            "status": "Success"
        }
    ]
}

print(f"\nActive quests: {len(quests['active'])}")
print(f"Completed quests: {len(quests['completed'])}")