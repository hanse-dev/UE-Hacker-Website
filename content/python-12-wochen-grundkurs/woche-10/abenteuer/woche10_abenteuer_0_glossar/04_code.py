class Held:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def vorstellen(self):
        print(f"Ich bin {self.name}, Level {self.level}!")

    def aufsteigen(self):
        self.level += 1
        print(f"{self.name} ist jetzt Level {self.level}!")

# Objekte erstellen
held1 = Held("Aria")
held2 = Held("Borin", level=3)

held1.vorstellen()   # Ich bin Aria, Level 1!
held1.aufsteigen()   # Aria ist jetzt Level 2!
print(held2.level)   # 3
