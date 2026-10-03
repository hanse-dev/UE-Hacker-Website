import json
map_data = {
    "Gold cup": {"coordinates": (10, 20), "value": 800},
    "Silver ribbon": {"coordinates": (30, 40), "value": 300},
    "Honor prize": {"coordinates": (50, 60), "value": 650},
}
with open("map.json", "w") as f:
    json.dump(map_data, f)
with open("map.json", "r") as f:
    loaded = json.load(f)
print(f"Places: {len(loaded)}")
print(f"Coordinates: {loaded['Gold cup']['coordinates']}")
