# Solution suggestion Mission 1 – The Character Hierarchy

# Step 1: Base class
class Character:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}, HP: {self.hp}")

# Step 2: Child classes
class Warrior(Character):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.armour = "Chainmail"

    def battle_cry(self):
        print(f"{self.name} roars: For the Guild! Armour: {self.armour}")

class Mage(Character):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.mana = 100

    def cast_spell(self):
        print(f"{self.name} casts a spell! Mana: {self.mana}")

class Rogue(Character):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.hidden = True

    def sneak(self):
        status = "hidden" if self.hidden else "visible"
        print(f"{self.name} sneaks through the shadows – currently {status}")

# Step 3: Create objects and call methods
thorin = Warrior("Thorin", 10, 200)
thorin.introduce()
thorin.battle_cry()

print()
merlin = Mage("Merlin", 12, 80)
merlin.introduce()
merlin.cast_spell()

print()
lyra = Rogue("Lyra", 8, 120)
lyra.introduce()
lyra.sneak()

# Bonus: Paladin inherits from Warrior
print()
class Paladin(Warrior):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.healing_power = 50

    def heal(self):
        print(f"{self.name} heals an ally for {self.healing_power} HP!")

arthas = Paladin("Arthas", 15, 250)
arthas.introduce()
arthas.battle_cry()   # inherited from Warrior
arthas.heal()
