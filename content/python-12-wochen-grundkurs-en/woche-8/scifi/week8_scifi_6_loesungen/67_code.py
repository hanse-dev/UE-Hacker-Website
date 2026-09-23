zones = {
    "Hangar": {"danger": "Meteorite", "find": "Crystal", "difficulty": 3},
    "Lab": {"danger": "Radiation", "find": "Sensor", "difficulty": 5},
    "Bridge": {"danger": "Storm", "find": "Star chart", "difficulty": 8},
}
for name, zone in zones.items():
    print(f"{name}: {zone['danger']} / {zone['find']}")
