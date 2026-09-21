crew = [
    {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120},
    {"name": "Rex", "rolle": "Ingenieur", "rang": 6, "energie": 150},
    {"name": "Zara", "rolle": "Botanikerin", "rang": 3, "energie": 90},
    {"name": "Kai", "rolle": "Pilotin", "rang": 5, "energie": 110},
]
rang_werte = [h["rang"] for h in crew]
rangliste = sorted(rang_werte, reverse=True)
bester = crew[0]
for h in crew:
    if h["rang"] > bester["rang"]:
        bester = h
print(f"Bester: {bester['name']}")
print(f"Rangliste: {rangliste}")
