# Step 1: Create a profile
thunder = {"name": "Thunder", "breed": "Hanoverian", "age": 8, "discipline": "Dressage"}
print("=== STABLE ARCHIVE ===")
for key, val in thunder.items():
    print(f"  {key}: {val}")

# Step 2: Fill the stable
stable = [
    {"name": "Thunder", "breed": "Hanoverian", "age": 8, "discipline": "Dressage"},
    {"name": "Luna", "breed": "Icelandic", "age": 4, "discipline": "Cross-Country"},
    {"name": "Flash", "breed": "Arabian", "age": 6, "discipline": "Jumping"}
]

# Step 3: Horses older than 5 years
print("\nHorses older than 5 years:")
total_age = 0
for h in stable:
    total_age += h["age"]
    if h["age"] > 5:
        print(f"  {h['name']}: {h['age']} years ({h['breed']})")
average = total_age / len(stable)
print(f"Average age: {average:.1f} years")

# Bonus: Sort by age (youngest first)
sorted_horses = sorted(stable, key=lambda h: h["age"])
print("\nSorted by age (youngest first):")
for h in sorted_horses:
    print(f"  {h['name']}: {h['age']} years")