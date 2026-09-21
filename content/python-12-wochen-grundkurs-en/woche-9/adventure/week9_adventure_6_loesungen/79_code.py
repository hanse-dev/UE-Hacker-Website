import json
quests = [
    {"name": "Defeat the dragon", "difficulty": 1, "status": "open"},
    {"name": "Find the treasure", "difficulty": 2, "status": "open"},
    {"name": "Save the village", "difficulty": 3, "status": "open"},
]
with open("questlog.json", "w") as f:
    json.dump(quests, f)
with open("questlog.json", "r") as f:
    loaded = json.load(f)
print(f"Quest count: {len(loaded)}")
print(f"Status: {loaded[0]['status']}")
