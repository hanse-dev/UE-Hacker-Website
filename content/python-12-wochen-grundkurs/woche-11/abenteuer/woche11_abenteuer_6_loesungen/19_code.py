class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

class Krieger(Held):
    def __init__(self, name, staerke=30):
        super().__init__(name)
        self.staerke = staerke

    def kaempfe(self):
        print(f"{self.name} schwingt das Schwert.")

class Meister(Krieger):
    def kaempfe(self):
        super().kaempfe()
        print(f"{self.name} ist ein Meister!")

Meister("Aria").kaempfe()
