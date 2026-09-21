crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
    {"name": "Kai", "role": "Pilot", "rank": 5, "energy": 110},
]
def find_crew(items, kind):
    names = []
    for h in items:
        if h["role"] == kind:
            names.append(h["name"])
    return names

print(f"Found: {find_crew(crew, 'Pilot')}")
