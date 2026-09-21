class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

x = Gegenstand("Zugangskarte", "Sie öffnet gesicherte Türen.")
print(x.name)
