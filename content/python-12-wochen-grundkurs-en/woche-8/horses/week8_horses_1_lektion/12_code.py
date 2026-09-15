# Example 1: Dictionary inside a dictionary
stable = {
    "name": "Sunny Valley",
    "location": {
        "region": "Southern Germany",
        "coordinates": (100, 200),
        "state": "Bavaria"
    },
    "facilities": {
        "indoor_arena": "20x40m",
        "outdoor_arena": "30x60m",
        "paddocks": "5 units"
    }
}

print("=== Nested Stable Card ===")
print(f"Stable: {stable['name']}")
print(f"Region: {stable['location']['region']}")
print(f"Coordinates: {stable['location']['coordinates']}")
print(f"Indoor arena: {stable['facilities']['indoor_arena']}")