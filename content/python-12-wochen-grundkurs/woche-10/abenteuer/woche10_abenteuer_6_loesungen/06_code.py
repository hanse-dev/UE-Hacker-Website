# Problem: __init__ braucht self als ersten Parameter – sonst weiß Python nicht,
# auf welchem Objekt die Attribute (name, mana) gespeichert werden sollen.
class Magier:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

merlin = Magier("Merlin", 150)
print(merlin.name)