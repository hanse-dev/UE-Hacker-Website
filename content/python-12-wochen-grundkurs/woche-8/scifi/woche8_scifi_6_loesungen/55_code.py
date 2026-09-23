crew = [
    {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120},
    {"name": "Rex", "rolle": "Ingenieur", "rang": 6, "energie": 150},
    {"name": "Zara", "rolle": "Botanikerin", "rang": 3, "energie": 90},
    {"name": "Kai", "rolle": "Pilotin", "rang": 5, "energie": 110},
]
def finde_crew(liste, art):
    namen = []
    for h in liste:
        if h["rolle"] == art:
            namen.append(h["name"])
    return namen

print(f"Gefunden: {finde_crew(crew, 'Pilotin')}")
