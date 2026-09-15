# Problem: Klassennamen müssen mit Großbuchstaben beginnen
# und Methoden brauchen self als ersten Parameter
class Pferd:
    def wiehern(self):
        print("Wieher! 🐴")

class Araber(Pferd):
    def rennen(self):
        print("Schnell wie der Wind!")

mein_pferd = Araber()
mein_pferd.wiehern()