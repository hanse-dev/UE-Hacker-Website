helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
    {"name": "Mira", "klasse": "Magierin", "level": 13, "leben": 110},
]
def finde_helden(liste, art):
    namen = []
    for h in liste:
        if h["klasse"] == art:
            namen.append(h["name"])
    return namen

print(f"Magierin: {len(finde_helden(helden, 'Magierin'))}")
print(f"Krieger: {len(finde_helden(helden, 'Krieger'))}")
