# Boss-Quest 1: Die Waffenschmiede

# Schritt 1: Waffe-Klasse
class Waffe:
    def __init__(self, name, typ, schaden):
        self.name = name
        self.typ = typ
        self.schaden = schaden

    # Schritt 2: Methoden
    def anzeigen(self):
        print(f"[{self.typ}] {self.name} – Schaden: {self.schaden}")

    def benutzen(self):
        print(f"{self.name} wird eingesetzt! +{self.schaden} Schaden!")

    # Bonus: verbessern-Methode
    def verbessern(self):
        self.schaden += 5
        print(f"{self.name} wurde verbessert! Neuer Schaden: {self.schaden}")

# Schritt 3: Waffenlager
waffenlager = [
    Waffe("Excalibur", "Schwert", 60),
    Waffe("Shadowsong", "Dolch", 35),
    Waffe("Donnerbogen", "Bogen", 45),
]

print("=== Waffenlager ===")
for waffe in waffenlager:
    waffe.anzeigen()

# Stärkste Waffe finden
staerkste = max(waffenlager, key=lambda w: w.schaden)
print(f"\nStärkste Waffe: {staerkste.name} ({staerkste.schaden} Schaden)")

# Bonus: Waffe verbessern
staerkste.verbessern()

print("\n=== Einsatz ===")
for waffe in waffenlager:
    waffe.benutzen()