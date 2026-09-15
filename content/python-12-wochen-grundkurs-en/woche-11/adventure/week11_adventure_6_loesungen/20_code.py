# Solution suggestion Boss Quest 2 – The Mage Family

# Step 1: Base class
class Mage:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name} casts a general spell! (Mana: {self.mana})")

    def __str__(self):
        return f"Mage {self.name} | Mana: {self.mana}"

    def __eq__(self, other):
        return self.mana == other.mana

# Step 2: Schools
class FireMage(Mage):
    def cast_spell(self):
        print(f"{self.name} summons a fireball! 🔥 WUUUSH! (Mana -{10})")
        self.mana -= 10

class IceMage(Mage):
    def cast_spell(self):
        print(f"{self.name} freezes everything! ❄️ KRRRRK! (Mana -{8})")
        self.mana -= 8

class LightningMage(Mage):
    def cast_spell(self):
        print(f"{self.name} hurls a lightning bolt! ⚡ KRAKABOOM! (Mana -{12})")
        self.mana -= 12

# Step 3: Duel
ignis = FireMage("Ignis", 100)
glacius = IceMage("Glacius", 100)
fulmen = LightningMage("Fulmen", 100)

print("=== MAGE DUEL ===")
for mage in [ignis, glacius, fulmen]:
    print(mage)           # __str__
    mage.cast_spell()
    print(f"  Remaining Mana: {mage.mana}")
    print()

print(f"Equal mana after duel? {ignis == glacius}")
