horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
    {"name": "Wind", "breed": "Hanoverian", "age": 7, "points": 110},
]
def find_horses(items, kind):
    names = []
    for h in items:
        if h["breed"] == kind:
            names.append(h["name"])
    return names

print(f"Hanoverian: {len(find_horses(horses, 'Hanoverian'))}")
print(f"Haflinger: {len(find_horses(horses, 'Haflinger'))}")
