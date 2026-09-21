class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

class Krieger(Held):
    def ziehe_waffe(self):
        print("zieht das Schwert.")

k = Krieger("Aria")
k.stelle_vor()
