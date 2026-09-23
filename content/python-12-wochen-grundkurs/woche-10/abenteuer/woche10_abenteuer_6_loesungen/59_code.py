class Held:
    def __init__(self, name):
        self.name = name
        self.energie = 100

    def kaempfe(self, kosten):
        self.energie -= kosten
        if self.energie < 0:
            self.energie = 0

held = Held("Aria")
held.kaempfe(40)
held.kaempfe(40)
held.kaempfe(40)
print(f"Energie: {held.energie}")
