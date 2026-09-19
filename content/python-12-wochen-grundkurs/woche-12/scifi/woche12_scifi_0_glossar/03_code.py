class Waffe:
    def __init__(self, name, schaden):
        self.name = name
        self.schaden = schaden

class Held:
    def __init__(self, name):
        self.name = name
        self.waffe = Waffe("Holzschwert", 2)  # Der Held HAT eine Waffe

held = Held("Mira")
print(f"{held.name} kämpft mit dem {held.waffe.name} (Schaden: {held.waffe.schaden})")