# Problem: __init__ braucht self als ersten Parameter – sonst weiß Python nicht,
# auf welchem Objekt die Attribute (name, level) gespeichert werden sollen.
class Reiter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

maria = Reiter("Maria", 3)
print(maria.name)