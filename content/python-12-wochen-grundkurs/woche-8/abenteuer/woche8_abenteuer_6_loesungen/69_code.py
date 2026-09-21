zonen = {
    "Keller": {"monster": "Ratte", "schatz": "Silber", "schwierigkeit": 3},
    "Höhle": {"monster": "Troll", "schatz": "Gold", "schwierigkeit": 5},
    "Turm": {"monster": "Drache", "schatz": "Krone", "schwierigkeit": 8},
}
gefaehrlichste = None
for name, zone in zonen.items():
    if gefaehrlichste is None or zone["schwierigkeit"] > zonen[gefaehrlichste]["schwierigkeit"]:
        gefaehrlichste = name
print(f"Gefährlichste: {gefaehrlichste} ({zonen[gefaehrlichste]['schwierigkeit']})")
