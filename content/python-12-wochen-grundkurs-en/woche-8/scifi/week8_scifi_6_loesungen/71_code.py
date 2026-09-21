zones = {
    "Hangar": {"danger": "Meteorite", "find": "Crystal", "difficulty": 3},
    "Lab": {"danger": "Radiation", "find": "Sensor", "difficulty": 5},
    "Bridge": {"danger": "Storm", "find": "Star chart", "difficulty": 8},
}
strong = 5
enterable = []
for name, zone in zones.items():
    if zone["difficulty"] <= strong:
        enterable.append(name)
print(f"Enterable: {enterable}")
