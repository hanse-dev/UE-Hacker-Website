# Lösungsvorschlag Mission 3 – Magische Artefakte

# Schritt 1: Klasse Artefakt
class Artefakt:
    def __init__(self, name, macht, typ):
        self.name = name
        self.macht = macht
        self.typ = typ

    # Schritt 2: Magic Methods
    def __str__(self):
        return f"✨ {self.name} ({self.typ}), Macht: {self.macht}"

    def __add__(self, other):
        return self.macht + other.macht

    def __len__(self):
        return self.macht

    # Bonus
    def __eq__(self, other):
        return self.macht == other.macht

    def __lt__(self, other):
        return self.macht < other.macht

# Schritt 3: Testen
amulett = Artefakt("Amulett der Weisheit", 75, "Schmuck")
stab = Artefakt("Stab der Stürme", 90, "Waffe")

print(amulett)
print(stab)

kombinierte_macht = amulett + stab
print(f"Kombinierte Macht: {kombinierte_macht}")

print(f"Macht von Amulett (len): {len(amulett)}")

print(f"Gleich stark? {amulett == stab}")
print(f"Amulett schwächer als Stab? {amulett < stab}")