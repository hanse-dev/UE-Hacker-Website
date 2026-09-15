# Step 1: Guild list (nested: [Name, Level, Horse])
guild = [
    ["Lisa", 5, "Thunder"],
    ["Tom", 3, "Luna"],
    ["Sarah", 7, "Midnight"],
]
print("=== Rider's Guild ===")
for rider in guild:
    print(f"  {rider[0]}, Level {rider[1]}, Horse: {rider[2]}")

# Step 2: Add a new rider
guild.append(["Max", 1, "Star"])
print(f"Members: {len(guild)}")

# Step 3: Sort by level
guild.sort(key=lambda r: r[1], reverse=True)
print("\n=== Rankings ===")
for i, r in enumerate(guild, 1):
    print(f"  {i}. {r[0]} (Level {r[1]})")