helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
    {"name": "Mira", "klasse": "Magierin", "level": 13, "leben": 110},
]
level_werte = [h["level"] for h in helden]
rangliste = sorted(level_werte, reverse=True)
bester = helden[0]
for h in helden:
    if h["level"] > bester["level"]:
        bester = h
print(f"Bester: {bester['name']}")
print(f"Rangliste: {rangliste}")
