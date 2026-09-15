# Beispiel 1: Einfache Vererbung
class Lebewesen:
    def __init__(self, name):
        self.name = name
    
    def atmen(self):
        print(f"{self.name} atmet")

class Mensch(Lebewesen):
    def sprechen(self):
        print(f"{self.name} spricht")

# Beispiel 2: Methoden überschreiben
class Krieger(Lebewesen):
    def atmen(self):
        print(f"{self.name} atmet kämpferisch!")
    
    def kämpfen(self):
        print(f"{self.name} zieht sein Schwert!")

# Beispiel 3: super() verwenden
class Magier(Lebewesen):
    def __init__(self, name, mana):
        super().__init__(name)
        self.mana = mana
    
    def zaubern(self):
        print(f"{self.name} zaubert mit {self.mana} Mana!")