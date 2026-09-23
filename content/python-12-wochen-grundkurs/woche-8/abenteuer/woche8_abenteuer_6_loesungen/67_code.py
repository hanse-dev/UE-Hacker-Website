zonen = {
    "Keller": {"monster": "Ratte", "schatz": "Silber", "schwierigkeit": 3},
    "Höhle": {"monster": "Troll", "schatz": "Gold", "schwierigkeit": 5},
    "Turm": {"monster": "Drache", "schatz": "Krone", "schwierigkeit": 8},
}
for name, zone in zonen.items():
    print(f"{name}: {zone['monster']} / {zone['schatz']}")
