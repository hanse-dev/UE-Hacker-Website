# Problem: Methoden brauchen immer self als ersten Parameter – ohne self kann
# die Methode nicht auf self.name zugreifen (sie weiß nicht, welches Pferd gemeint ist).
class Pferd:
    def __init__(self, name):
        self.name = name
    
    def galoppieren(self):
        print(f"{self.name} galoppiert! 🐎")

pferd = Pferd("Spirit")
pferd.galoppieren()