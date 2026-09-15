# Beispiel 1: __str__ und __repr__
class Raumschiff:
    def __init__(self, name, klasse):
        self.name = name
        self.klasse = klasse

    def __str__(self):
        return f"🚀 {self.name} ({self.klasse})"

    def __repr__(self):
        return f"Raumschiff('{self.name}', '{self.klasse}')"

# Beispiel 2: __len__ und __getitem__
class Flotte:
    def __init__(self):
        self.schiffe = []

    def __len__(self):
        return len(self.schiffe)

    def __getitem__(self, index):
        return self.schiffe[index]

    def schiff_hinzufügen(self, schiff):
        self.schiffe.append(schiff)

# Beispiel 3: __eq__ und __lt__
class Planet:
    def __init__(self, name, einwohner):
        self.name = name
        self.einwohner = einwohner

    def __eq__(self, other):
        return self.einwohner == other.einwohner

    def __lt__(self, other):
        return self.einwohner < other.einwohner

    def __str__(self):
        return f"{self.name} ({self.einwohner} Einwohner)"
