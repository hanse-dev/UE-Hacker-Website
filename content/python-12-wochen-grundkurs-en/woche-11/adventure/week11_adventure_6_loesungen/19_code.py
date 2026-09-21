class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Warrior(Hero):
    def __init__(self, name, strength=30):
        super().__init__(name)
        self.strength = strength

    def fight(self):
        print(f"{self.name} swings the sword.")

class Master(Warrior):
    def fight(self):
        super().fight()
        print(f"{self.name} is a master!")

Master("Aria").fight()
