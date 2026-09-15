class Alien:
    def __init__(self, name, planet, gefaehrlichkeit, intelligenz):
        self.name = name
        self.planet = planet
        self.gefaehrlichkeit = gefaehrlichkeit
        self.intelligenz = intelligenz

    def analysieren(self):
        stufe = "HOCH" if self.gefaehrlichkeit >= 8 else ("MITTEL" if self.gefaehrlichkeit >= 5 else "GERING")
        print(f"🔬 {self.name} (Planet: {self.planet}) | Gefahr: {stufe} | IQ: {self.intelligenz}")

    def kontakt(self):
        if self.intelligenz >= 7:
            print(f"{self.name} kann kommunizieren!")
        else:
            print(f"{self.name} reagiert instinktiv.")

bestiarium = [
    Alien("Zorgon", "Kepler-22b", 9, 4),
    Alien("Luminar", "Gliese-667c", 3, 10),
    Alien("Krakon", "HD 40307g", 7, 6),
]

print("=== Alien-Bestiarium ===")
for alien in bestiarium:
    alien.analysieren()
    alien.kontakt()
    print()

print("🎉 Mission abgeschlossen!")
print("🏆 Du hast den Konstrukteur-Meister besiegt!")
print("⭐ Titel erhalten: System-Architekt")