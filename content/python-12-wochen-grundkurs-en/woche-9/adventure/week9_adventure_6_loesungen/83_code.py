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
loaded[0]["status"] = "done"
with open("questlog.json", "w") as f:
    json.dump(loaded, f)
with open("questlog.json", "r") as f:
    fresh = json.load(f)
print(f"First: {fresh[0]['status']}")
