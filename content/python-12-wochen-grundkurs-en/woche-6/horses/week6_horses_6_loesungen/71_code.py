guild = [["Anna", "Jumping", 15], ["Ben", "Dressage", 12], ["Clara", "Vaulting", 8]]
guild.append(["David", "Western", 10])
strongest = guild[0]
for member in guild:
    if member[2] > strongest[2]:
        strongest = member
print(f"Strongest: {strongest[0]}")
