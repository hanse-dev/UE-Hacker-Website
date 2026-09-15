# Problem: __init__ needs self as first parameter – otherwise Python doesn't know
# on which object the attributes (name, mana) should be stored.
class Wizard:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

merlin = Wizard("Merlin", 150)
print(merlin.name)