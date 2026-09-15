# Example 1: Dictionary in dictionary
space_station = {
    "name": "Nebula-7",
    "position": {
        "sector": "Alpha",
        "coordinates": (100, 200, 300),
        "system": "Sol"
    },
    "systems": {
        "drive": "Online",
        "life_support": "Stable",
        "communications": "Active"
    }
}

print("=== Nested Dictionary ===")
print(f"Station: {space_station['name']}")
print(f"Sector: {space_station['position']['sector']}")
print(f"Coordinates: {space_station['position']['coordinates']}")
print(f"Drive: {space_station['systems']['drive']}")