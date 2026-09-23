helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
]
starke = [h["name"] for h in helden if h["level"] > 14]
print(f"Starke: {starke}")
