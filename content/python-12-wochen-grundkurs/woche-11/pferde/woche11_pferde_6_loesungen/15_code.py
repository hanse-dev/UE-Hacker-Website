# Lösungsvorschlag Mission 3 – Das Champion-Register

# Schritt 1: Klasse Champion
class Champion:
    def __init__(self, name, rasse, punkte):
        self.name = name
        self.rasse = rasse
        self.punkte = punkte

    # Schritt 2: Magic Methods
    def __str__(self):
        return f"🏆 {self.name} ({self.rasse}), Punkte: {self.punkte}"

    def __add__(self, other):
        return self.punkte + other.punkte

    def __len__(self):
        return self.punkte

    # Bonus
    def __eq__(self, other):
        return self.punkte == other.punkte

    def __lt__(self, other):
        return self.punkte < other.punkte

# Schritt 3: Testen
champ1 = Champion("Valencia", "Andalusier", 2850)
champ2 = Champion("Pegasus", "Vollblüter", 3100)

print(champ1)
print(champ2)

gesamtpunkte = champ1 + champ2
print(f"Kombinierte Punktzahl: {gesamtpunkte}")

print(f"Punkte Valencia (len): {len(champ1)}")

print(f"Gleich viele Punkte? {champ1 == champ2}")
print(f"Valencia hat weniger Punkte als Pegasus? {champ1 < champ2}")

# Champion-Register ausgeben
register = [champ1, champ2, Champion("Sterntaler", "Haflinger", 2600)]
print()
print("=== CHAMPION-REGISTER ===")
for rang, champ in enumerate(sorted(register, key=len, reverse=True), 1):
    print(f"Platz {rang}: {champ}")