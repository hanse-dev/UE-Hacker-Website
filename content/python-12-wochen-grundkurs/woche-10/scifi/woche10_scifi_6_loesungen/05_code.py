# Problem: __init__ braucht self als ersten Parameter – sonst weiß Python nicht,
# auf welchem Objekt die Attribute (name, power_level) gespeichert werden sollen.
class Cyborg:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

terminator = Cyborg("T-800", 9000)
print(terminator.name)