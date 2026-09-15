# Problem: __add__ sollte neues Objekt zurückgeben
class Goldstück:
    def __init__(self, wert):
        self.wert = wert
    
    def __add__(self, other):
        return Goldstück(self.wert + other.wert)
    
    def __str__(self):
        return f"{self.wert} Goldstücke"

gold1 = Goldstück(10)
gold2 = Goldstück(20)
gesamt = gold1 + gold2
print(gesamt)