# Problem: Klassennamen müssen mit Großbuchstaben beginnen
# und __add__ sollte neues Objekt zurückgeben
class Datenpaket:
    def __init__(self, größe):
        self.größe = größe
    
    def __add__(self, other):
        return Datenpaket(self.größe + other.größe)
    
    def __str__(self):
        return f"{self.größe} MB"

paket1 = Datenpaket(1024)
paket2 = Datenpaket(2048)
gesamt = paket1 + paket2
print(f"Gesamtgröße: {gesamt}")