# Beispiel 1: Dictionary in Dictionary
raumstation = {
    "name": "Nebula-7",
    "position": {
        "sektor": "Alpha",
        "koordinaten": (100, 200, 300),
        "system": "Sol"
    },
    "systeme": {
        "antrieb": "Online",
        "lebenserhaltung": "Stabil",
        "kommunikation": "Aktiv"
    }
}

print("=== Verschachteltes Dictionary ===")
print(f"Station: {raumstation['name']}")
print(f"Sektor: {raumstation['position']['sektor']}")
print(f"Koordinaten: {raumstation['position']['koordinaten']}")
print(f"Antrieb: {raumstation['systeme']['antrieb']}")