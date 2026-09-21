class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

class Magier(Held):
    def ziehe_waffe(self):
        print(f"{self.name} zieht das Schwert.")

k = Magier("Thorin")
k.stelle_vor()
k.ziehe_waffe()
