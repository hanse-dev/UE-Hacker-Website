class Raumschiff:
    def __init__(self, name, typ="Standard"):
        self.name = name
        self.typ = typ

    def vorstellen(self):
        print(f"Ich bin {self.name}, Typ: {self.typ}!")

    def starten(self):
        print(f"{self.name} hebt ab!")

# Objekte erstellen
schiff1 = Raumschiff("Enterprise")
schiff2 = Raumschiff("Voyager", typ="Intrepid")

schiff1.vorstellen()  # Ich bin Enterprise, Typ: Standard!
schiff1.starten()     # Enterprise hebt ab!
print(schiff2.typ)    # Intrepid
