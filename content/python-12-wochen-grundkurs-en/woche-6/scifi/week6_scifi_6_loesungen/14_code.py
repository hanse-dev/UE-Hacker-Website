# Step 1: Crew list (nested: [Name, Rank, Position])
crew = [
    ["Captain Alex", "Commander", "Alpha"],
    ["Dr. Vega", "Medical Officer", "Beta"],
    ["Tech Orion", "Engineer", "Gamma"],
]
print("=== Crew Database ===")
for member in crew:
    print(f"  {member[0]} | {member[1]} | Sector: {member[2]}")

# Step 2: New member
crew.append(["Nav Zara", "Pilot", "Delta"])
print(f"Crew strength: {len(crew)}")

# Step 3: Sort by name
crew.sort(key=lambda m: m[0])
print("\n=== Alphabetical ===")
for m in crew:
    print(f"  {m[0]}")