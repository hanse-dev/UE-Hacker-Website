# Problem: Klassennamen müssen mit Großbuchstaben beginnen
# und Methoden brauchen self als ersten Parameter
class Roboter:
    def bewegen(self):
        print("Roboter bewegt sich")

class Drohne(Roboter):
    def fliegen(self):
        print("Drohne fliegt")

meine_drohne = Drohne()
meine_drohne.bewegen()