# Beispiel 1: __str__ und __repr__
class Zaubertrank:
    def __init__(self, name, farbe):
        self.name = name
        self.farbe = farbe
    
    def __str__(self):
        return f"🧪 {self.name} ({self.farbe})"
    
    def __repr__(self):
        return f"Zaubertrank('{self.name}', '{self.farbe}')"

# Beispiel 2: __len__ und __getitem__
class Inventar:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def hinzufügen(self, item):
        self.items.append(item)

# Beispiel 3: __eq__ und __lt__
class Held:
    def __init__(self, name, stärke):
        self.name = name
        self.stärke = stärke
    
    def __eq__(self, other):
        return self.stärke == other.stärke
    
    def __lt__(self, other):
        return self.stärke < other.stärke
    
    def __str__(self):
        return f"{self.name} (Stärke: {self.stärke})"