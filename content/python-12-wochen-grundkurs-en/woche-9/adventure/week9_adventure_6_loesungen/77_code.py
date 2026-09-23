import json
map_data = {
    "Gold crown": {"coordinates": (10, 20), "value": 800},
    "Silver cup": {"coordinates": (30, 40), "value": 300},
    "Ruby": {"coordinates": (50, 60), "value": 650},
}
map_data["Emerald"] = {"coordinates": [70, 80], "value": 400}
with open("map.json", "w") as f:
    json.dump(map_data, f)
with open("map.json", "r") as f:
    loaded = json.load(f)
best = None
for place in loaded:
    if best is None or loaded[place]["value"] > loaded[best]["value"]:
        best = place
print(f"Most valuable: {best} ({loaded[best]['value']})")
