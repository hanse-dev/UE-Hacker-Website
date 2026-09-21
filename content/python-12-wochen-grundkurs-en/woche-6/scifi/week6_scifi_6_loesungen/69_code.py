guild = [["Nova", "Pilot", 15], ["Kira", "Technician", 12], ["Juno", "Doctor", 8]]
guild.append(["Rex", "Engineer", 10])
total = 0
for member in guild:
    total += member[2]
print(f"Members: {len(guild)}")
print(f"Total level: {total}")
