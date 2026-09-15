class Soldat:
    def __init__(self, name, rang="Rekrut", einheit="Standard"):
        self.name = name
        self.rang = rang
        self.einheit = einheit

    def vorstellen(self):
        print(f"⚔️ {self.name} | {self.rang} | Einheit: {self.einheit}")

    def befoerdern(self, neuer_rang):
        self.rang = neuer_rang
        print(f"{self.name} wurde befördert zu: {self.rang}!")

shepard = Soldat("Shepard", "Kommandant", "N7")
vasquez = Soldat("Vasquez", "Sergeant", "Alpha")
hicks = Soldat("Hicks", einheit="Bravo")

print("=== Space-Marine ===")
for s in [shepard, vasquez, hicks]:
    s.vorstellen()

hicks.befoerdern("Gefreiter")