class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Mage(Hero):
    def __init__(self, name, mana=50):
        super().__init__(name)
        self.mana = mana

k = Mage("Thorin")
print(k.name, k.mana)
