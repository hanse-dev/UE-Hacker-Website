guild = [["Aria", "Mage", 15], ["Thorin", "Warrior", 12], ["Luna", "Rogue", 8]]
guild.append(["Finn", "Archer", 10])
total = 0
for member in guild:
    total += member[2]
print(f"Members: {len(guild)}")
print(f"Total level: {total}")
