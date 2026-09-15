# Beispiel 1: Einfacher Konstruktor
class Android:
    def __init__(self, name):
        self.name = name

# Beispiel 2: Konstruktor mit mehreren Werten
class Planet:
    def __init__(self, name, typ, durchmesser):
        self.name = name
        self.typ = typ
        self.durchmesser = durchmesser

# Beispiel 3: Konstruktor mit Standardwerten
class Alien:
    def __init__(self, species="Greys", hp=50):
        self.species = species
        self.hp = hp