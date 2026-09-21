zones = {
    "Meadow": {"obstacle": "Ditch", "prize": "Ribbon", "difficulty": 3},
    "Forest": {"obstacle": "Water jump", "prize": "Cup", "difficulty": 5},
    "Moor": {"obstacle": "Wall", "prize": "Medal", "difficulty": 8},
}
most_dangerous = None
for name, zone in zones.items():
    if most_dangerous is None or zone["difficulty"] > zones[most_dangerous]["difficulty"]:
        most_dangerous = name
print(f"Most dangerous: {most_dangerous} ({zones[most_dangerous]['difficulty']})")
