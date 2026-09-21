class Hero:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def fight(self, kosten):
        self.energy -= kosten
        if self.energy < 0:
            self.energy = 0

hero = Hero("Aria")
hero.fight(40)
hero.fight(40)
hero.fight(40)
print(f"Energy: {hero.energy}")
