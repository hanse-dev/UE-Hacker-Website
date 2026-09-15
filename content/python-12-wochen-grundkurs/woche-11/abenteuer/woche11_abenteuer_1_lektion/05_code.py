# Beispiel 1: Methoden-Polymorphismus
class Schwertkämpfer:
    def angreifen(self):
        print("Schlag mit dem Schwert! ⚔️")

class Magier:
    def angreifen(self):
        print("Feuerball geworfen! 🔥")

class Bogenschütze:
    def angreifen(self):
        print("Pfeil abgeschossen! 🏹")

# Beispiel 2: Polymorphe Funktion
def kampf(character):
    character.angreifen()

# Beispiel 3: Operator-Polymorphismus
class Goldstück:
    def __init__(self, wert):
        self.wert = wert
    
    def __add__(self, other):
        return Goldstück(self.wert + other.wert)
    
    def __str__(self):
        return f"{self.wert} Goldstücke"