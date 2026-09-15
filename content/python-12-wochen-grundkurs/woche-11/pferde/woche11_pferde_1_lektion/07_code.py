# Beispiel 1: __str__ und __repr__
class Pferd:
    def __init__(self, name, rasse):
        self.name = name
        self.rasse = rasse
    
    def __str__(self):
        return f"🐴 {self.name} ({self.rasse})"
    
    def __repr__(self):
        return f"Pferd('{self.name}', '{self.rasse}')"

# Beispiel 2: __len__ und __getitem__
class Herde:
    def __init__(self):
        self.pferde = []
    
    def __len__(self):
        return len(self.pferde)
    
    def __getitem__(self, index):
        return self.pferde[index]
    
    def pferd_hinzufügen(self, pferd):
        self.pferde.append(pferd)

# Beispiel 3: __eq__ und __lt__
class Champion:
    def __init__(self, name, punkte):
        self.name = name
        self.punkte = punkte
    
    def __eq__(self, other):
        return self.punkte == other.punkte
    
    def __lt__(self, other):
        return self.punkte < other.punkte
    
    def __str__(self):
        return f"{self.name} ({self.punkte} Punkte)"