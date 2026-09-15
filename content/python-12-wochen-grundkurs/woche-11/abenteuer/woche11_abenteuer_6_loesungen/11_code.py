# Lösungsvorschlag Mission 1 – Die Charakter-Hierarchie

# Schritt 1: Basisklasse
class Charakter:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def vorstellen(self):
        print(f"Ich bin {self.name}, Level {self.level}, HP: {self.hp}")

# Schritt 2: Kind-Klassen
class Krieger(Charakter):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.ruestung = "Kettenhemd"

    def schlachtruf(self):
        print(f"{self.name} brüllt: Für die Gilde! Rüstung: {self.ruestung}")

class Magier(Charakter):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.mana = 100

    def zaubern(self):
        print(f"{self.name} zaubert! Mana: {self.mana}")

class Schurke(Charakter):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.versteckt = True

    def schleichen(self):
        status = "versteckt" if self.versteckt else "sichtbar"
        print(f"{self.name} schleicht durch die Schatten – aktuell {status}")

# Schritt 3: Objekte erstellen und Methoden aufrufen
thorin = Krieger("Thorin", 10, 200)
thorin.vorstellen()
thorin.schlachtruf()

print()
merlin = Magier("Merlin", 12, 80)
merlin.vorstellen()
merlin.zaubern()

print()
lyra = Schurke("Lyra", 8, 120)
lyra.vorstellen()
lyra.schleichen()

# Bonus: Paladin erbt von Krieger
print()
class Paladin(Krieger):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.heilkraft = 50

    def heilen(self):
        print(f"{self.name} heilt einen Verbündeten um {self.heilkraft} HP!")

arthas = Paladin("Arthas", 15, 250)
arthas.vorstellen()
arthas.schlachtruf()   # von Krieger geerbt
arthas.heilen()