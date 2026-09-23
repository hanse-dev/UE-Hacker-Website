class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Warrior(Hero):
    pass

class Mage(Hero):
    pass

k = Warrior("Aria")
print(isinstance(k, Hero))
print(isinstance(k, Mage))
