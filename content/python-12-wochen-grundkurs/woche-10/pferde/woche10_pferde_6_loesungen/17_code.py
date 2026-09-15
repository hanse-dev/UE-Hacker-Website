class Pferd:
    def __init__(self, name, rasse, alter, energie=100):
        self.name = name
        self.rasse = rasse
        self.alter = alter
        self.energie = energie

    def vorstellen(self):
        print(f"🐴 {self.name} | {self.rasse} | {self.alter} Jahre | Energie: {self.energie}%")

    def trainieren(self, stunden):
        verbrauch = stunden * 10
        self.energie = max(0, self.energie - verbrauch)
        print(f"{self.name} trainierte {stunden}h. Energie jetzt: {self.energie}%")

    def ausruhen(self):
        self.energie = min(100, self.energie + 30)
        print(f"{self.name} ruht sich aus. Energie: {self.energie}%")

thunder = Pferd("Thunder", "Hannoveraner", 6)
luna = Pferd("Luna", "Haflinger", 4)
thunder.vorstellen()
thunder.trainieren(3)
thunder.ausruhen()
luna.vorstellen()