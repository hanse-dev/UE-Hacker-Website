zonen = {
    "Hangar": {"gefahr": "Meteorit", "fund": "Kristall", "schwierigkeit": 3},
    "Labor": {"gefahr": "Strahlung", "fund": "Sensor", "schwierigkeit": 5},
    "Brücke": {"gefahr": "Sturm", "fund": "Sternkarte", "schwierigkeit": 8},
}
stark = 5
betretbar = []
for name, zone in zonen.items():
    if zone["schwierigkeit"] <= stark:
        betretbar.append(name)
print(f"Betretbar: {betretbar}")
