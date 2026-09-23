class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Mage(Hero):
    def draw_weapon(self):
        print(f"{self.name} draws the sword.")

k = Mage("Thorin")
k.introduce()
k.draw_weapon()
