# Beispiel 1: Methoden-Polymorphismus
class Dressurpferd:
    def spezialfähigkeit(self):
        print("Elegante Piaffe! 💃")

class Springpferd:
    def spezialfähigkeit(self):
        print("Hoher Sprung! 🦘")

class Westernpferd:
    def spezialfähigkeit(self):
        print("Sliding Stop! 🤠")

# Beispiel 2: Polymorphe Funktion
def training_absolvieren(pferd):
    print(f"Training für {pferd.name}:")
    pferd.spezialfähigkeit()

# Beispiel 3: Operator-Polymorphismus
class Pferdestärke:
    def __init__(self, wert):
        self.wert = wert
    
    def __add__(self, other):
        return Pferdestärke(self.wert + other.wert)
    
    def __str__(self):
        return f"{self.wert} Pferdestärken"