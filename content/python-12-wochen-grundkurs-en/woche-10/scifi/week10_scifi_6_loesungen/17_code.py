class Spaceship:
    def __init__(self, name, ship_type, crew_strength, shield=100):
        self.name = name
        self.ship_type = ship_type
        self.crew_strength = crew_strength
        self.shield = shield

    def introduce(self):
        print(f"🛸 {self.name} | {self.ship_type} | Crew: {self.crew_strength} | Shield: {self.shield}%")

    def attack(self, target):
        damage = self.crew_strength * 2
        target.shield = max(0, target.shield - damage)
        print(f"{self.name} attacks {target.name}! Damage: {damage}. Shield: {target.shield}%")

    def repair(self):
        self.shield = min(100, self.shield + 25)
        print(f"{self.name} repaired. Shield: {self.shield}%")

nova = Spaceship("Nova-Hawk", "Warship", 30)
defender = Spaceship("Defender", "Cruiser", 20, 80)
scout = Spaceship("Scout-1", "Fighter", 5)

fleet = [nova, defender, scout]
for ship in fleet:
    ship.introduce()

largest_crew = max(fleet, key=lambda s: s.crew_strength)
print(f"\nLargest crew: {largest_crew.name} ({largest_crew.crew_strength})")

nova.attack(defender)
defender.repair()