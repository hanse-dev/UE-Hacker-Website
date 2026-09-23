class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

class Magier(Held):
    def __init__(self, name, mana=50):
        super().__init__(name)
        self.mana = mana

k = Magier("Thorin")
print(k.name, k.mana)
