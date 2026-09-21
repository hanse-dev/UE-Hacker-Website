class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

    def kraft(self):
        return 10

class Krieger(Held):
    def __init__(self, name, staerke=30):
        super().__init__(name)
        self.staerke = staerke

    def kaempfe(self):
        print(f"{self.name} schwingt das Schwert.")

    def kraft(self):
        return self.staerke

class Magier(Held):
    def __init__(self, name, mana=50):
        super().__init__(name)
        self.mana = mana

    def kaempfe(self):
        print(f"{self.name} wirft einen Feuerball.")

    def kraft(self):
        return self.mana

import json
f = Krieger("Aria")
daten = {"typ": type(f).__name__, "name": f.name}
print(json.dumps(daten))
