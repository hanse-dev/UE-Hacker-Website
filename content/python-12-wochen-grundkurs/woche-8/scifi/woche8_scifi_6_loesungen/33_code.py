crew = [
    {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120},
    {"name": "Rex", "rolle": "Ingenieur", "rang": 6, "energie": 150},
    {"name": "Zara", "rolle": "Botanikerin", "rang": 3, "energie": 90},
]
starke = [h["name"] for h in crew if h["rang"] > 3]
print(f"Starke: {starke}")
