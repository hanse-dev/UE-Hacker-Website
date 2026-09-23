class Hero:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def is_tired(self):
        return self.energy < 20

print(Hero("Aria", 10).is_tired())
print(Hero("Thorin", 80).is_tired())
