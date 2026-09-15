class Spaceship:
    def __init__(self, name, ship_class, crew):
        self.name = name
        self.ship_class = ship_class
        self.crew = crew

    def hyperjump(self):
        print(f"{self.name}: Hyperjump initiated! 🚀")

    def introduce(self):
        print(f"🛸 {self.name} | {self.ship_class} | Crew: {self.crew}")

nebula = Spaceship("Nebula-7", "Research Ship", 150)
titan = Spaceship("Titan", "Battle Cruiser", 500)
scout = Spaceship("Scout-1", "Reconnaissance Ship", 25)

fleet = [nebula, titan, scout]
print("=== Fleet ===")
for ship in fleet:
    ship.introduce()

nebula.hyperjump()