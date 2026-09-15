# Beispiel 1: Steckbrief in Steckbrief
dungeon = {
    "name": "Verdammnis-Festung",
    "location": {
        "region": "Schattenlande",
        "koordinaten": (100, 200),
        "reich": "Pyralia"
    },
    "gefaehrten": {
        "boss": "Lich-König",
        "monster": "Skelette",
        "fallen": "Magisch"
    }
}

print("=== Verschachtelter Steckbrief ===")
print(f"Dungeon: {dungeon['name']}")
print(f"Region: {dungeon['location']['region']}")
print(f"Koordinaten: {dungeon['location']['koordinaten']}")
print(f"Boss: {dungeon['gefaehrten']['boss']}")