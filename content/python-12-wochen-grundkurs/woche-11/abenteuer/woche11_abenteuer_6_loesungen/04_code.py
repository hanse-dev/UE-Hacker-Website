# Problem: Klassennamen müssen mit Großbuchstaben beginnen
class Drache:
    def fliegen(self):
        print("Der Drache fliegt!")

class Feuerspucker(Drache):
    def feuerspeien(self):
        print("Feuer! 🔥")

drache = Feuerspucker()
drache.fliegen()