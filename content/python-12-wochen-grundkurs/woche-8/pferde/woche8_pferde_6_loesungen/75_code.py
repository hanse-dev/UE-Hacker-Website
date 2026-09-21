pferde = [
    {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120},
    {"name": "Sturm", "rasse": "Haflinger", "alter": 12, "punkte": 150},
    {"name": "Luna", "rasse": "Isländer", "alter": 6, "punkte": 90},
    {"name": "Wind", "rasse": "Hannoveraner", "alter": 7, "punkte": 110},
]
def finde_pferde(liste, art):
    namen = []
    for h in liste:
        if h["rasse"] == art:
            namen.append(h["name"])
    return namen

print(f"Hannoveraner: {len(finde_pferde(pferde, 'Hannoveraner'))}")
print(f"Haflinger: {len(finde_pferde(pferde, 'Haflinger'))}")
