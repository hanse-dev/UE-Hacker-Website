# Step 1: List of dictionaries
crew = [
    {"name": "Captain Zara", "rank": "Commander", "age": 38, "experience": 15},
    {"name": "Dr. Orion", "rank": "Doctor", "age": 42, "experience": 18},
    {"name": "Tech Maya", "rank": "Engineer", "age": 29, "experience": 6},
]

print("=== Crew Database ===")
for m in crew:
    print(f"  {m['name']} | {m['rank']} | {m['experience']} years")

# Step 2: Search
veteran = next(m for m in crew if m["experience"] == max(c["experience"] for c in crew))
print(f"\nMost experienced: {veteran['name']} ({veteran['experience']} years)")

# Step 3: Sort
crew.sort(key=lambda m: m["age"])
print("\nBy age:")
for m in crew:
    print(f"  {m['name']}: {m['age']} years")