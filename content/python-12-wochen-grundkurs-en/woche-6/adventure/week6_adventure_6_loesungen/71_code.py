guild = [["Aria", "Mage", 15], ["Thorin", "Warrior", 12], ["Luna", "Rogue", 8]]
guild.append(["Finn", "Archer", 10])
strongest = guild[0]
for member in guild:
    if member[2] > strongest[2]:
        strongest = member
print(f"Strongest: {strongest[0]}")
