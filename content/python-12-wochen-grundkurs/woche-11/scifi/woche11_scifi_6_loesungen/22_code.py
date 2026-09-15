# Lösungsvorschlag Boss-Quest 3 – Das Alien-Kontakt-System

# Schritt 1: Basis-Klasse
class Alien:
    def __init__(self, name, herkunft):
        self.name = name
        self.herkunft = herkunft

    def kommunizieren(self):
        print(f"{self.name} aus {self.herkunft}: [unbekannte Kommunikation]")

    def __str__(self):
        return f"👽 {self.name} | Herkunft: {self.herkunft}"

    def __len__(self):
        return len(self.herkunft)

# Schritt 2: Alien-Völker
class Zylarianer(Alien):
    def kommunizieren(self):
        print(f"{self.name} (Zylarianer): 'Zyk-zyh-zyh!' – kommuniziert durch Lichtpulse")

class Grolthen(Alien):
    def kommunizieren(self):
        print(f"{self.name} (Grolthen): 'GROMMM!' – tiefes Grollen, Bodenvibrationen spürbar")

class Silicons(Alien):
    def kommunizieren(self):
        print(f"{self.name} (Silicons): '01001000 01101001' – binäre Datenpakete")

class Aethros(Alien):
    def kommunizieren(self):
        print(f"{self.name} (Aethros): [Telepathische Wellen spürbar – kein Ton]")

# Schritt 3: Erstkontakt
kontakte = [
    Zylarianer("Zykla", "Zylaron-5"),
    Grolthen("Grox", "Groltheim"),
    Silicons("Binary-1", "Datacron"),
    Aethros("Ether", "Ätherdimension")
]

print("=== ERSTKONTAKT-PROTOKOLL ===")
for alien in kontakte:
    print(alien)              # __str__
    alien.kommunizieren()     # Polymorphismus!
    print(f"  Herkunftsname Länge: {len(alien)}")   # __len__
    print()

print("🎉 Mission abgeschlossen!")
print("🏆 Du hast den Konstruktions-Meister besiegt!")
print("⭐ Titel erhalten: Architekt der Systeme")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 11 gemeistert!")