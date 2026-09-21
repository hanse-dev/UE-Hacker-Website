zonen = {
    "Hangar": {"gefahr": "Meteorit", "fund": "Kristall", "schwierigkeit": 3},
    "Labor": {"gefahr": "Strahlung", "fund": "Sensor", "schwierigkeit": 5},
    "Brücke": {"gefahr": "Sturm", "fund": "Sternkarte", "schwierigkeit": 8},
}
gefaehrlichste = None
for name, zone in zonen.items():
    if gefaehrlichste is None or zone["schwierigkeit"] > zonen[gefaehrlichste]["schwierigkeit"]:
        gefaehrlichste = name
print(f"Gefährlichste: {gefaehrlichste} ({zonen[gefaehrlichste]['schwierigkeit']})")
