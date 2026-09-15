# Beispiel 1: Einfacher Konstruktor
class Held:
    def __init__(self, name):
        self.name = name

# Beispiel 2: Konstruktor mit mehreren Werten
class Zaubertrank:
    def __init__(self, name, farbe, staerke):
        self.name = name
        self.farbe = farbe
        self.staerke = staerke

# Beispiel 3: Konstruktor mit Standardwerten
class Goblin:
    def __init__(self, name="Grog", hp=10):
        self.name = name
        self.hp = hp