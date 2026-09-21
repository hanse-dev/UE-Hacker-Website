finds = [
    {"name": "Crystal core", "value": 800, "place": "Hangar"},
    {"name": "Sensor chip", "value": 300, "place": "Lab"},
    {"name": "Antimatter", "value": 650, "place": "Bridge"},
]
values = [t["value"] for t in finds]
values = sorted(values, reverse=True)
print(f"Values: {values}")
