class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}")

held = Held("Aria")
held.stelle_vor()
