# Problem: Klassennamen müssen mit Großbuchstaben beginnen
# und __add__ sollte neues Objekt zurückgeben
class Preis:
    def __init__(self, wert):
        self.wert = wert
    
    def __add__(self, other):
        return Preis(self.wert + other.wert)
    
    def __str__(self):
        return f"{self.wert} Euro"

preis1 = Preis(1000)
preis2 = Preis(2000)
gesamt = preis1 + preis2
print(f"Gesamtpreis: {gesamt}")