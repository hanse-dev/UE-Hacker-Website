# Step 1: Create rider list
riders = [
    {"name": "Lena", "level": 3, "age": 16, "experience": 4},
    {"name": "Tom", "level": 2, "age": 14, "experience": 2},
    {"name": "Sophie", "level": 3, "age": 18, "experience": 5}
]
print("=== RIDER'S GUILD ===")
for r in riders:
    print(f"  {r['name']} | Level {r['level']} | {r['experience']} years experience")

# Step 2: Add a member
riders.append({"name": "Max", "level": 1, "age": 12, "experience": 1})
print(f"\nMembers after joining: {len(riders)}")

# Step 3: Search function by level
def search_by_level(riders_list, level):
    return [r for r in riders_list if r["level"] == level]

level3_riders = search_by_level(riders, 3)
print("\nAll riders at Level 3:")
for r in level3_riders:
    print(f"  {r['name']} (Age {r['age']})")

level2_riders = search_by_level(riders, 2)
print("\nAll riders at Level 2:")
for r in level2_riders:
    print(f"  {r['name']} (Age {r['age']})")

# Step 4: Average age
average_age = sum(r["age"] for r in riders) / len(riders)
print(f"\nAverage age: {average_age:.1f} years")

# Assign horse
horse_names = ["Thunder", "Luna", "Flash", "Silver"]
for i, r in enumerate(riders):
    r["horse"] = horse_names[i]

print("\nHorse assignments:")
for r in riders:
    print(f"  {r['name']} rides {r['horse']}")

# Bonus: Tournaments
riders[0]["tournaments"] = ["Spring Tournament 2024", "Autumn Cup", "County Championship"]
print(f"\nBonus – Tournaments of {riders[0]['name']}: {riders[0]['tournaments']}")