guild = [["Anna", "Jumping", 15], ["Ben", "Dressage", 12], ["Clara", "Vaulting", 8]]
guild.append(["David", "Western", 10])
total = 0
for member in guild:
    total += member[2]
print(f"Members: {len(guild)}")
print(f"Total level: {total}")
