# Beispiel 1: Einfacher Konstruktor
class Pferd:
    def __init__(self, name):
        self.name = name

# Beispiel 2: Konstruktor mit mehreren Werten
class Fohlen:
    def __init__(self, name, alter, geschlecht):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht

# Beispiel 3: Konstruktor mit Standardwerten
class Pferd:
    def __init__(self, name="Stormy", rasse="Pony"):
        self.name = name
        self.rasse = rasse