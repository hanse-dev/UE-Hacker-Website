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

k = Krieger("Aria")
print(f"{k.name}: {k.staerke}")
