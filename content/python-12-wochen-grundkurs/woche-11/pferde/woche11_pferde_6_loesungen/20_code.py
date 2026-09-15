# Lösungsvorschlag Boss-Quest 2 – Die Pferde-Familie

# Schritt 1: Basis-Klasse
class Pferd:
    def __init__(self, name, energie):
        self.name = name
        self.energie = energie

    def laufen(self):
        print(f"{self.name} läuft – gleichmäßiger Galopp. (Energie: {self.energie})")

    def __str__(self):
        return f"🐴 {self.name} | Energie: {self.energie}"

    def __eq__(self, other):
        return self.energie == other.energie

# Schritt 2: Rassen
class Haflinger(Pferd):
    def laufen(self):
        print(f"{self.name} (Haflinger): Ausdauernder Bergritt, sicher und zuverlässig! (Energie -{5})")
        self.energie -= 5

class Araber(Pferd):
    def laufen(self):
        print(f"{self.name} (Araber): Blitzschneller Sprint, federnde Gänge! (Energie -{12})")
        self.energie -= 12

class Andalusier(Pferd):
    def laufen(self):
        print(f"{self.name} (Andalusier): Eleganter Schaukelschwung, majestätische Bewegungen! (Energie -{8})")
        self.energie -= 8

# Schritt 3: Rennen
goldi = Haflinger("Goldi", 100)
rashid = Araber("Rashid", 100)
conquistador = Andalusier("Conquistador", 100)

print("=== PFERDERENNEN ===")
for pferd in [goldi, rashid, conquistador]:
    print(pferd)        # __str__
    pferd.laufen()
    print(f"  Verbleibende Energie: {pferd.energie}")
    print()

print(f"Goldi und Rashid gleich viel Energie? {goldi == rashid}")