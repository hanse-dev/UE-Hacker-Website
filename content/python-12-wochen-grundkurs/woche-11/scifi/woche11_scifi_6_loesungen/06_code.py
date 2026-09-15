# Problem: Klassennamen müssen mit Großbuchstaben beginnen
class Maschine:
    def __init__(self, id):
        self.id = id

class Android(Maschine):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

unit7 = Android("007", "Seven")
print(unit7.id)