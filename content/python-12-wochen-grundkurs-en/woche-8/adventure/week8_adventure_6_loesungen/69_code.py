zones = {
    "Cellar": {"monster": "Rat", "treasure": "Silver", "difficulty": 3},
    "Cave": {"monster": "Troll", "treasure": "Gold", "difficulty": 5},
    "Tower": {"monster": "Dragon", "treasure": "Crown", "difficulty": 8},
}
most_dangerous = None
for name, zone in zones.items():
    if most_dangerous is None or zone["difficulty"] > zones[most_dangerous]["difficulty"]:
        most_dangerous = name
print(f"Most dangerous: {most_dangerous} ({zones[most_dangerous]['difficulty']})")
