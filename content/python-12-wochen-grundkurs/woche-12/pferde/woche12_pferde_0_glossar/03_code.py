class Sattel:
    def __init__(self, name, polster):
        self.name = name
        self.polster = polster

class Reiter:
    def __init__(self, name):
        self.name = name
        self.sattel = Sattel("Übungssattel", 2)  # Der Reiter HAT einen Sattel

reiter = Reiter("Mira")
print(f"{reiter.name} reitet mit dem {reiter.sattel.name} (Polster: {reiter.sattel.polster})")