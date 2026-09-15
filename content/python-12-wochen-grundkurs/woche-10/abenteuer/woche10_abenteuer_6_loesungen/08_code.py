# Problem: Methoden brauchen immer self als ersten Parameter – ohne self kann
# die Methode nicht auf self.name zugreifen (sie weiß nicht, welcher Drache gemeint ist).
class Drache:
    def __init__(self, name):
        self.name = name
    
    def vorstellen(self):
        print(f"Ich bin {self.name}!")

drache = Drache("Smaug")
drache.vorstellen()