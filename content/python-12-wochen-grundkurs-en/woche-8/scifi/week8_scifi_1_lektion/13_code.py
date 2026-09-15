# Example 2: List of dictionaries
crew = [
    {
        "name": "Captain Alex",
        "role": "Commander",
        "age": 35,
        "experience": 15
    },
    {
        "name": "Dr. Zara",
        "role": "Scientist",
        "age": 28,
        "experience": 8
    },
    {
        "name": "Lt. Nova",
        "role": "Pilot",
        "age": 26,
        "experience": 6
    }
]

print("=== Crew List ===")
for member in crew:
    print(f"{member['name']} - {member['role']} ({member['age']} years)")

# Filter by experience
experienced = [m for m in crew if m['experience'] > 10]
print(f"\nExperienced crew: {[m['name'] for m in experienced]}")