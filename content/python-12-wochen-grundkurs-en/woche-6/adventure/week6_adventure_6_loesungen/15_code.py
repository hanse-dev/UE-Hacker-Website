# Step 1 – Create the guild list
guild = [
    ["Aldric", "Warrior", 8],
    ["Lyra", "Mage", 6],
    ["Toryn", "Rogue", 10],
]
print("Guild members:")
for hero in guild:
    print(f"  {hero[0]} ({hero[1]}) – Level {hero[2]}")

# Step 2 – Expand the heroes
guild.append(["Sera", "Healer", 5])
print(f"\nAfter joining: {len(guild)} members")

# Step 3 – Search and sort heroes
search_name = "Lyra"
position = next((i for i, h in enumerate(guild) if h[0] == search_name), -1)
print(f"Position of {search_name}: {position}")

sorted_guild = sorted(guild, key=lambda h: h[2], reverse=True)
print("Sorted by level (descending):")
for h in sorted_guild:
    print(f"  {h[0]} – Level {h[2]}")

# Step 4 – Statistics
print(f"\nTotal members: {len(guild)}")
classes = [h[1] for h in guild]
print(f"Classes: {', '.join(classes)}")
average_level = sum(h[2] for h in guild) / len(guild)
print(f"Average level: {average_level:.1f}")

# Bonus – missions column and sorting
for hero in guild:
    hero.append(hero[2] * 3)  # Missions = Level * 3 as an example
print("\nSorted by missions:")
for h in sorted(guild, key=lambda x: x[3], reverse=True):
    print(f"  {h[0]}: {h[3]} missions")