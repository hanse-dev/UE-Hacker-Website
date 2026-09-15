# Problem: Methoden brauchen immer self als ersten Parameter – ohne self kann
# die Methode nicht auf self.bezeichnung zugreifen (sie weiß nicht, welcher Roboter gemeint ist).
class Roboter:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
    
    def bewegen(self):
        print(f"{self.bezeichnung} bewegt sich! 🤖")

roboter = Roboter("R2-D2")
roboter.bewegen()