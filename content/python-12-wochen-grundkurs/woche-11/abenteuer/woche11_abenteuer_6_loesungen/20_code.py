# Lösungsvorschlag Boss-Quest 2 – Die Zauberer-Familie

# Schritt 1: Basis-Klasse
class Zauberer:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

    def zauber_wirken(self):
        print(f"{self.name} wirkt einen allgemeinen Zauber! (Mana: {self.mana})")

    def __str__(self):
        return f"Zauberer {self.name} | Mana: {self.mana}"

    def __eq__(self, other):
        return self.mana == other.mana

# Schritt 2: Schulen
class Feuermagier(Zauberer):
    def zauber_wirken(self):
        print(f"{self.name} beschwört einen Feuerball! 🔥 WUUUSH! (Mana -{10})")
        self.mana -= 10

class Eismagier(Zauberer):
    def zauber_wirken(self):
        print(f"{self.name} friert alles ein! ❄️ KRRRRK! (Mana -{8})")
        self.mana -= 8

class Blitzmagier(Zauberer):
    def zauber_wirken(self):
        print(f"{self.name} schleudert einen Blitz! ⚡ KRAKABOOM! (Mana -{12})")
        self.mana -= 12

# Schritt 3: Duell
ignis = Feuermagier("Ignis", 100)
glacius = Eismagier("Glacius", 100)
fulmen = Blitzmagier("Fulmen", 100)

print("=== ZAUBERER-DUELL ===")
for zauberer in [ignis, glacius, fulmen]:
    print(zauberer)           # __str__
    zauberer.zauber_wirken()
    print(f"  Verbleibendes Mana: {zauberer.mana}")
    print()

print(f"Gleich viel Mana nach Duell? {ignis == glacius}")