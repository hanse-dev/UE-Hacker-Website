zones = {
    "Meadow": {"obstacle": "Ditch", "prize": "Ribbon", "difficulty": 3},
    "Forest": {"obstacle": "Water jump", "prize": "Cup", "difficulty": 5},
    "Moor": {"obstacle": "Wall", "prize": "Medal", "difficulty": 8},
}
strong = 5
enterable = []
for name, zone in zones.items():
    if zone["difficulty"] <= strong:
        enterable.append(name)
print(f"Enterable: {enterable}")
