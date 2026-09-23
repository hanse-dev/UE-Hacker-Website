zones = {
    "Cellar": {"monster": "Rat", "treasure": "Silver", "difficulty": 3},
    "Cave": {"monster": "Troll", "treasure": "Gold", "difficulty": 5},
    "Tower": {"monster": "Dragon", "treasure": "Crown", "difficulty": 8},
}
for name, zone in zones.items():
    print(f"{name}: {zone['monster']} / {zone['treasure']}")
