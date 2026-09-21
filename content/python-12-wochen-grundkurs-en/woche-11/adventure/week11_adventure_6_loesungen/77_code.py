class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

    def power(self):
        return 10

class Warrior(Hero):
    def __init__(self, name, strength=30):
        super().__init__(name)
        self.strength = strength

    def fight(self):
        print(f"{self.name} swings the sword.")

    def power(self):
        return self.strength

class Mage(Hero):
    def __init__(self, name, mana=50):
        super().__init__(name)
        self.mana = mana

    def fight(self):
        print(f"{self.name} casts a fireball.")

    def power(self):
        return self.mana

team = [Warrior("Aria", 40), Mage("Thorin", 25), Hero("Luna")]
anzahl = 0
for f in team:
    if f.power() >= 30:
        anzahl += 1
print(f"Count: {anzahl}")
