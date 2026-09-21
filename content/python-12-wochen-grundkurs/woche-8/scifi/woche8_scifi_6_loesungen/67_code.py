zonen = {
    "Hangar": {"gefahr": "Meteorit", "fund": "Kristall", "schwierigkeit": 3},
    "Labor": {"gefahr": "Strahlung", "fund": "Sensor", "schwierigkeit": 5},
    "Brücke": {"gefahr": "Sturm", "fund": "Sternkarte", "schwierigkeit": 8},
}
for name, zone in zonen.items():
    print(f"{name}: {zone['gefahr']} / {zone['fund']}")
