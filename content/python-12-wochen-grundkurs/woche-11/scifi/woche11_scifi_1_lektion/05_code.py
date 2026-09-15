# Beispiel 1: Methoden-Polymorphismus
class Laserwaffe:
    def feuern(self):
        print("Laserstrahl abgefeuert! ⚡")

class Plasmawaffe:
    def feuern(self):
        print("Plasmaburst abgefeuert! 🔥")

class Ionenwaffe:
    def feuern(self):
        print("Ionenkanone abgefeuert! 💫")

# Beispiel 2: Polymorphe Funktion
def waffe_testen(waffe):
    print("Waffentest gestartet:")
    waffe.feuern()

# Beispiel 3: Operator-Polymorphismus
class Energiezelle:
    def __init__(self, kapazität):
        self.kapazität = kapazität

    def __add__(self, other):
        return Energiezelle(self.kapazität + other.kapazität)

    def __str__(self):
        return f"{self.kapazität} kWh"
