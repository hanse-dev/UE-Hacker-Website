zones = {
    "Meadow": {"obstacle": "Ditch", "prize": "Ribbon", "difficulty": 3},
    "Forest": {"obstacle": "Water jump", "prize": "Cup", "difficulty": 5},
    "Moor": {"obstacle": "Wall", "prize": "Medal", "difficulty": 8},
}
for name, zone in zones.items():
    print(f"{name}: {zone['obstacle']} / {zone['prize']}")
