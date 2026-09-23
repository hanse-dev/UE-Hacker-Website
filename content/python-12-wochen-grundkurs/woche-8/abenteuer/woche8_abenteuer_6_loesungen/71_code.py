zonen = {
    "Keller": {"monster": "Ratte", "schatz": "Silber", "schwierigkeit": 3},
    "Höhle": {"monster": "Troll", "schatz": "Gold", "schwierigkeit": 5},
    "Turm": {"monster": "Drache", "schatz": "Krone", "schwierigkeit": 8},
}
stark = 5
betretbar = []
for name, zone in zonen.items():
    if zone["schwierigkeit"] <= stark:
        betretbar.append(name)
print(f"Betretbar: {betretbar}")
