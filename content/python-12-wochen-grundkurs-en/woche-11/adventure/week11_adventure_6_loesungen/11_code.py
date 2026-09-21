class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Mage(Hero):
    def fight(self):
        print(f"{self.name} casts a fireball.")

Hero("Luna").fight()
Mage("Thorin").fight()
