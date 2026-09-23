guild = [["Nova", "Pilot", 15], ["Kira", "Technician", 12], ["Juno", "Doctor", 8]]
guild.append(["Rex", "Engineer", 10])
strongest = guild[0]
for member in guild:
    if member[2] > strongest[2]:
        strongest = member
print(f"Strongest: {strongest[0]}")
