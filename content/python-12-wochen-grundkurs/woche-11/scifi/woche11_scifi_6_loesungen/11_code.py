# Lösungsvorschlag Mission 1 – Die Roboter-Hierarchie

# Schritt 1: Basisklasse
class Roboter:
    def __init__(self, id, name, energiestatus):
        self.id = id
        self.name = name
        self.energiestatus = energiestatus

    def aktivieren(self):
        print(f"[{self.id}] {self.name} – Energie: {self.energiestatus}% – SYSTEM ONLINE")

# Schritt 2: Kind-Klassen
class Android(Roboter):
    def __init__(self, id, name, energiestatus):
        super().__init__(id, name, energiestatus)
        self.sprachen = ["Galaktisch", "Terranisch"]

    def kommunizieren(self):
        print(f"{self.name} spricht: {', '.join(self.sprachen)}")

class Drohne(Roboter):
    def __init__(self, id, name, energiestatus):
        super().__init__(id, name, energiestatus)
        self.max_hoehe_m = 500

    def fliegen(self):
        print(f"{self.name} steigt auf bis zu {self.max_hoehe_m} Meter!")

class Cyborg(Roboter):
    def __init__(self, id, name, energiestatus):
        super().__init__(id, name, energiestatus)
        self.menschlich = True

    def status(self):
        bio = "biologisch" if self.menschlich else "vollmechanisch"
        print(f"{self.name}: Hybrideinheit – teils {bio}")

# Schritt 3: Objekte erstellen
seven = Android("AND-007", "Seven", 98)
seven.aktivieren()
seven.kommunizieren()

print()
scout = Drohne("DRN-42", "Scout", 85)
scout.aktivieren()
scout.fliegen()

print()
nexus = Cyborg("CYB-01", "Nexus", 72)
nexus.aktivieren()
nexus.status()

# Bonus: Kampfandroid erbt von Android
print()
class Kampfandroid(Android):
    def __init__(self, id, name, energiestatus):
        super().__init__(id, name, energiestatus)
        self.waffe = "Plasmablaster"

    def angriff(self):
        print(f"{self.name} feuert den {self.waffe}! PEWPEW!")

rex = Kampfandroid("KAD-99", "Rex", 100)
rex.aktivieren()       # von Roboter geerbt
rex.kommunizieren()    # von Android geerbt
rex.angriff()