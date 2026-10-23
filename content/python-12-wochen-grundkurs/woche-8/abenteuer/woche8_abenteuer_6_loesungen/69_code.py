zonen = {
    "Keller": {"monster": "Ratte", "schatz": "Silber", "schwierigkeit": 3},
    "Höhle": {"monster": "Troll", "schatz": "Gold", "schwierigkeit": 5},
    "Turm": {"monster": "Drache", "schatz": "Krone", "schwierigkeit": 8},
}
gefaehrlichste = ""
hoechste = 0
for name, zone in zonen.items():
    if zone["schwierigkeit"] > hoechste:
        hoechste = zone["schwierigkeit"]
        gefaehrlichste = name
print(f"Gefährlichste: {gefaehrlichste} ({hoechste})")
