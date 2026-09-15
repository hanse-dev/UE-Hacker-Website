# Lösungsvorschlag Mission 2 – Das polymorphe Arsenal

# Schritt 1: Drei Waffen-Klassen
class Schwert:
    def __init__(self, name):
        self.name = name

    def anwenden(self):
        print(f"Schwert '{self.name}' trifft! CLANG!")

class Bogen:
    def __init__(self, name):
        self.name = name

    def anwenden(self):
        print(f"Bogen '{self.name}': Pfeil fliegt! WHOOSH!")

class Zauberstab:
    def __init__(self, name):
        self.name = name

    def anwenden(self):
        print(f"Zauberstab '{self.name}': Zauber wirkt! ZAP!")

# Schritt 2: Polymorphe Funktion
def nutze_waffe(waffe):
    waffe.anwenden()

# Schritt 3: Alle Waffen testen
klinge = Schwert("Dämonentöter")
langbogen = Bogen("Silberpfeil")
stab = Zauberstab("Mondholz-Stab")

nutze_waffe(klinge)
nutze_waffe(langbogen)
nutze_waffe(stab)

# Bonus: Waffenfabrik
def waffenfabrik(typ, name):
    if typ == "schwert":
        return Schwert(name)
    elif typ == "bogen":
        return Bogen(name)
    elif typ == "zauberstab":
        return Zauberstab(name)
    else:
        print(f"Unbekannter Waffentyp: {typ}")
        return None

print()
neue_waffe = waffenfabrik("schwert", "Drachenklingen")
nutze_waffe(neue_waffe)