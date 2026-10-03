import json
quests = [
    {"name": "Locate the signal", "difficulty": 1, "status": "open"},
    {"name": "Launch the probe", "difficulty": 2, "status": "open"},
    {"name": "Repair the hull", "difficulty": 3, "status": "open"},
]
with open("questlog.json", "w") as f:
    json.dump(quests, f)
with open("questlog.json", "r") as f:
    loaded = json.load(f)
print(f"Mission count: {len(loaded)}")
print(f"Status: {loaded[0]['status']}")
