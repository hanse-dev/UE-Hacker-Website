class Tier:
    def __init__(name):
        self.name = name

class Hund(Tier):
    def __init__(name, rasse):
        super().__init__(name)
        self.rasse = rasse

hund = Hund("Bello", "Dackel")
print(hund.name)