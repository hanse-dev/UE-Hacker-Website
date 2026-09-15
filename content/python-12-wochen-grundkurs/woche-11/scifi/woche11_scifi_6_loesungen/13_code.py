# Lösungsvorschlag Mission 2 – Das polymorphe Waffensystem

# Schritt 1: Drei Waffen-Klassen
class Laser:
    def __init__(self, name):
        self.name = name

    def abfeuern(self):
        print(f"Pew! {self.name} feuert einen Laserstrahl! ⚡")

class Plasma:
    def __init__(self, name):
        self.name = name

    def abfeuern(self):
        print(f"Zisch! {self.name} entlädt Plasmaenergie! 🔵")

class Ionen:
    def __init__(self, name):
        self.name = name

    def abfeuern(self):
        print(f"Bzz! {self.name} schleudert einen Ionenstrahl! ⚪")

# Schritt 2: Polymorphe Funktion
def waffe_testen(waffe):
    print(f"Teste Waffe '{waffe.name}':")
    waffe.abfeuern()

# Schritt 3: Alle Waffen testen
laser_mk2 = Laser("Laser-MK2")
plasmawerfer = Plasma("Plasmawerfer-X")
ionenkanone = Ionen("Ionenkanone-3000")

waffe_testen(laser_mk2)
waffe_testen(plasmawerfer)
waffe_testen(ionenkanone)

# Bonus: Waffenfabrik
def waffenfabrik(typ, name):
    if typ == "laser":
        return Laser(name)
    elif typ == "plasma":
        return Plasma(name)
    elif typ == "ionen":
        return Ionen(name)
    else:
        print(f"Unbekannter Waffentyp: {typ}")
        return None

print()
neue_waffe = waffenfabrik("plasma", "Plasma-Prototyp")
waffe_testen(neue_waffe)