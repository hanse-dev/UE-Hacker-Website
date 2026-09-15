# Example 2: List of dictionaries
horses = [
    {
        "name": "Thunder",
        "breed": "Hanoverian",
        "age": 8,
        "training_level": "M"
    },
    {
        "name": "Luna",
        "breed": "Icelandic",
        "age": 6,
        "training_level": "A"
    },
    {
        "name": "Stormy",
        "breed": "Quarter Horse",
        "age": 10,
        "training_level": "L"
    }
]

print("=== Horse List ===")
for horse in horses:
    print(f"{horse['name']} - {horse['breed']} ({horse['age']} years)")

# Filter by age
young = [h for h in horses if h['age'] < 8]
print(f"\nYoung horses: {[h['name'] for h in young]}")