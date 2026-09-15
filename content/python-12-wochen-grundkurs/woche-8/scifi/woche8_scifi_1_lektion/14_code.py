# Beispiel 3: Komplexe Datenstrukturen
# Tupel als Dictionary-Schlüssel
galaxie_karte = {
    (100, 200): "Sonne A",
    (300, 400): "Sonne B",
    (500, 600): "Sonne C"
}

print("=== Galaxie-Karte ===")
for koordinate, stern in galaxie_karte.items():
    print(f"{koordinate}: {stern}")

# Komplexes Missionssystem
missionen = {
    "aktive": [
        {
            "id": 1,
            "ziel": (100, 200, 300),
            "crew": ["Alex", "Zara"],
            "status": "In Bearbeitung"
        }
    ],
    "abgeschlossen": [
        {
            "id": 2,
            "ziel": (400, 500, 600),
            "crew": ["Nova"],
            "status": "Erfolg"
        }
    ]
}

print(f"\nAktive Missionen: {len(missionen['aktive'])}")
print(f"Abgeschlossene Missionen: {len(missionen['abgeschlossen'])}")