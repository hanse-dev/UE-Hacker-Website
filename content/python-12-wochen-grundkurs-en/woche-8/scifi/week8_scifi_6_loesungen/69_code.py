zones = {
    "Hangar": {"danger": "Meteorite", "find": "Crystal", "difficulty": 3},
    "Lab": {"danger": "Radiation", "find": "Sensor", "difficulty": 5},
    "Bridge": {"danger": "Storm", "find": "Star chart", "difficulty": 8},
}
most_dangerous = None
for name, zone in zones.items():
    if most_dangerous is None or zone["difficulty"] > zones[most_dangerous]["difficulty"]:
        most_dangerous = name
print(f"Most dangerous: {most_dangerous} ({zones[most_dangerous]['difficulty']})")
