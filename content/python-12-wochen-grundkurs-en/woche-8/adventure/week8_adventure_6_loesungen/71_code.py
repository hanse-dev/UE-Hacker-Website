zones = {
    "Cellar": {"monster": "Rat", "treasure": "Silver", "difficulty": 3},
    "Cave": {"monster": "Troll", "treasure": "Gold", "difficulty": 5},
    "Tower": {"monster": "Dragon", "treasure": "Crown", "difficulty": 8},
}
strong = 5
enterable = []
for name, zone in zones.items():
    if zone["difficulty"] <= strong:
        enterable.append(name)
print(f"Enterable: {enterable}")
