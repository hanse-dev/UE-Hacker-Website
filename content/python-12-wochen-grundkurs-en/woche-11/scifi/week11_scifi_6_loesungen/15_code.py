# Solution Suggestion Mission 3 – The Spaceship Registry

# Step 1: Class Spaceship
class Spaceship:
    def __init__(self, name, ship_class, crew):
        self.name = name
        self.ship_class = ship_class
        self.crew = crew

    # Step 2: Magic Methods
    def __str__(self):
        return f"🚀 {self.name} ({self.ship_class}), Crew: {self.crew}"

    def __add__(self, other):
        return self.crew + other.crew

    def __len__(self):
        return self.crew

    # Bonus
    def __eq__(self, other):
        return self.crew == other.crew

    def __lt__(self, other):
        return self.crew < other.crew

# Step 3: Testing
nebula7 = Spaceship("Nebula-7", "Space Station", 450)
phoenix = Spaceship("Phoenix", "Cruiser", 180)

print(nebula7)
print(phoenix)

total_crew = nebula7 + phoenix
print(f"Total crew: {total_crew} people")

print(f"Crew Nebula-7 (len): {len(nebula7)}")

print(f"Same crew size? {nebula7 == phoenix}")
print(f"Phoenix has fewer crew than Nebula-7? {phoenix < nebula7}")

# Fleet registry output
fleet = [nebula7, phoenix, Spaceship("Spearhead", "Frigate", 40)]
print()
print("=== FLEET REGISTRY ===")
for rank, ship in enumerate(sorted(fleet, key=len, reverse=True), 1):
    print(f"Rank {rank}: {ship}")