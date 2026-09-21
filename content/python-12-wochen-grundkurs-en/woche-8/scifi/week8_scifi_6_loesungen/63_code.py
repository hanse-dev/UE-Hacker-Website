finds = [
    {"name": "Crystal core", "value": 800, "place": "Hangar"},
    {"name": "Sensor chip", "value": 300, "place": "Lab"},
    {"name": "Antimatter", "value": 650, "place": "Bridge"},
]
above = 0
total = 0
for t in finds:
    if t["value"] > 500:
        above += 1
    total += t["value"]
print(f"Above 500: {above}")
print(f"Total value: {total}")
