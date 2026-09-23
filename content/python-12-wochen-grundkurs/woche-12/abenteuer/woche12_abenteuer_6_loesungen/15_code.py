class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

x = Gegenstand("Fackel", "Sie leuchtet in dunklen Ecken.")
print(x.name)
