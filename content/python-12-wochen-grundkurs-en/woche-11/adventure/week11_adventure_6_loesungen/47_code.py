class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Warrior(Hero):
    def draw_weapon(self):
        print("draws the sword.")

k = Warrior("Aria")
k.introduce()
