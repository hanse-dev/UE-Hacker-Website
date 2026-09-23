class Hero:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

hero = Hero("Aria", 4)
print(f"{hero.name} {hero.level} {hero.energy}")
