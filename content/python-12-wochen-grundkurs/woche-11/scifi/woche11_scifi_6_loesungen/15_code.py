# Lösungsvorschlag Mission 3 – Das Raumschiff-Register

# Schritt 1: Klasse Raumschiff
class Raumschiff:
    def __init__(self, name, klasse, besatzung):
        self.name = name
        self.klasse = klasse
        self.besatzung = besatzung

    # Schritt 2: Magic Methods
    def __str__(self):
        return f"🚀 {self.name} ({self.klasse}), Besatzung: {self.besatzung}"

    def __add__(self, other):
        return self.besatzung + other.besatzung

    def __len__(self):
        return self.besatzung

    # Bonus
    def __eq__(self, other):
        return self.besatzung == other.besatzung

    def __lt__(self, other):
        return self.besatzung < other.besatzung

# Schritt 3: Testen
nebula7 = Raumschiff("Nebula-7", "Raumstation", 450)
phoenix = Raumschiff("Phoenix", "Kreuzer", 180)

print(nebula7)
print(phoenix)

gesamt_besatzung = nebula7 + phoenix
print(f"Gesamtbesatzung: {gesamt_besatzung} Personen")

print(f"Besatzung Nebula-7 (len): {len(nebula7)}")

print(f"Gleich viele Besatzung? {nebula7 == phoenix}")
print(f"Phoenix hat weniger Besatzung als Nebula-7? {phoenix < nebula7}")

# Flotten-Register ausgeben
flotte = [nebula7, phoenix, Raumschiff("Speerspitze", "Fregatte", 40)]
print()
print("=== FLOTTENREGISTER ===")
for rang, schiff in enumerate(sorted(flotte, key=len, reverse=True), 1):
    print(f"Rang {rang}: {schiff}")