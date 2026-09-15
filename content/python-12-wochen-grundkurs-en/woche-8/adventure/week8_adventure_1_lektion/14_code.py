# Example 1: Profile within a profile
dungeon = {
    "name": "Damnation Fortress",
    "location": {
        "region": "Shadow Lands",
        "coordinates": (100, 200),
        "realm": "Pyralia"
    },
    "inhabitants": {
        "boss": "Lich King",
        "monsters": "Skeletons",
        "traps": "Magical"
    }
}

print("=== Nested Profile ===")
print(f"Dungeon: {dungeon['name']}")
print(f"Region: {dungeon['location']['region']}")
print(f"Coordinates: {dungeon['location']['coordinates']}")
print(f"Boss: {dungeon['inhabitants']['boss']}")