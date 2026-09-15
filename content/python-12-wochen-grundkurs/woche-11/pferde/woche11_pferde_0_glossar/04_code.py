class Pferd:
    def __init__(self, name):
        self.name = name

    def fähigkeit(self):
        return "Läuft auf der Weide"

    def __str__(self):
        return f"Pferd: {self.name}"

# Vererbung
class Rennpferd(Pferd):
    def __init__(self, name, tempo):
        super().__init__(name)
        self.tempo = tempo

    def fähigkeit(self):   # Polymorphismus
        return f"Rennt mit {self.tempo} km/h!"

bobby = Pferd("Bobby")
blitz = Rennpferd("Blitz", tempo=60)

print(bobby)                  # Pferd: Bobby
print(bobby.fähigkeit())      # Läuft auf der Weide
print(blitz.fähigkeit())      # Rennt mit 60 km/h!
