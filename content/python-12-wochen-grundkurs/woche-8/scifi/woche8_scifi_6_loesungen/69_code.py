zonen = {
    "Hangar": {"gefahr": "Meteorit", "fund": "Kristall", "schwierigkeit": 3},
    "Labor": {"gefahr": "Strahlung", "fund": "Sensor", "schwierigkeit": 5},
    "Brücke": {"gefahr": "Sturm", "fund": "Sternkarte", "schwierigkeit": 8},
}
gefaehrlichste = ""
hoechste = 0
for name, zone in zonen.items():
    if zone["schwierigkeit"] > hoechste:
        hoechste = zone["schwierigkeit"]
        gefaehrlichste = name
print(f"Gefährlichste: {gefaehrlichste} ({hoechste})")
