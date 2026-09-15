class preis:
    def __init__(wert):
        self.wert = wert
    
    def __add__(other):
        return self.wert + other.wert

preis1 = preis(1000)
preis2 = preis(2000)
gesamt = preis1 + preis2
print(f"Gesamtpreis: {gesamt} Euro")