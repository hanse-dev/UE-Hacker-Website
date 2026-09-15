class datenpaket:
    def __init__(größe):
        self.größe = größe
    
    def __add__(other):
        return self.größe + other.größe

paket1 = datenpaket(1024)
paket2 = datenpaket(2048)
gesamt = paket1 + paket2
print(f"Gesamtgröße: {gesamt} MB")