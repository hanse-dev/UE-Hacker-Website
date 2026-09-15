# Problem: Kein Fehler - super() ist korrekt verwendet!
class Tier:
    def __init__(self, name):
        self.name = name

class Hund(Tier):
    def __init__(self, name, rasse):
        super().__init__(name)
        self.rasse = rasse

hund = Hund("Bello", "Dackel")
print(hund.name)