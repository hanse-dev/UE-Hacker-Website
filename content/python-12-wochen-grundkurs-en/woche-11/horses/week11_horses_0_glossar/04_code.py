class Horse:
    def __init__(self, name):
        self.name = name

    def ability(self):
        return "Grazes in the meadow"

    def __str__(self):
        return f"Horse: {self.name}"

# Inheritance
class Racehorse(Horse):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def ability(self):   # Polymorphism
        return f"Races at {self.speed} km/h!"

bobby = Horse("Bobby")
lightning = Racehorse("Lightning", speed=60)

print(bobby)                  # Horse: Bobby
print(bobby.ability())        # Grazes in the meadow
print(lightning.ability())    # Races at 60 km/h!
