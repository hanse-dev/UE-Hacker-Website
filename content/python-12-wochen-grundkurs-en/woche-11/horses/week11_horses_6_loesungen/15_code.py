# Solution suggestion Mission 3 – The Champion Register

# Step 1: Class Champion
class Champion:
    def __init__(self, name, breed, points):
        self.name = name
        self.breed = breed
        self.points = points

    # Step 2: Magic Methods
    def __str__(self):
        return f"🏆 {self.name} ({self.breed}), Points: {self.points}"

    def __add__(self, other):
        return self.points + other.points

    def __len__(self):
        return self.points

    # Bonus
    def __eq__(self, other):
        return self.points == other.points

    def __lt__(self, other):
        return self.points < other.points

# Step 3: Testing
champ1 = Champion("Valencia", "Andalusian", 2850)
champ2 = Champion("Pegasus", "Thoroughbred", 3100)

print(champ1)
print(champ2)

total_points = champ1 + champ2
print(f"Combined score: {total_points}")

print(f"Valencia's points (len): {len(champ1)}")

print(f"Same points? {champ1 == champ2}")
print(f"Valencia has fewer points than Pegasus? {champ1 < champ2}")

# Output champion register
register = [champ1, champ2, Champion("Stardust", "Haflinger", 2600)]
print()
print("=== CHAMPION REGISTER ===")
for rank, champ in enumerate(sorted(register, key=len, reverse=True), 1):
    print(f"Rank {rank}: {champ}")
