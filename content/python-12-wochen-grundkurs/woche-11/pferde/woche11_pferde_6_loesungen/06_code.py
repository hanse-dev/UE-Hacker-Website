# Problem: Klassennamen müssen mit Großbuchstaben beginnen
class Tier:
    def __init__(self, name):
        self.name = name

class Pferd(Tier):
    def __init__(self, name, rasse):
        super().__init__(name)
        self.rasse = rasse

stormy = Pferd("Stormy", "Islandpferd")
print(stormy.name)