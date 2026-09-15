class Goldstück:
    def __init__(wert):
        self.wert = wert
    
    def __add__(other):
        return self.wert + other.wert

gold1 = Goldstück(10)
gold2 = Goldstück(20)
gesamt = gold1 + gold2
print(gesamt)