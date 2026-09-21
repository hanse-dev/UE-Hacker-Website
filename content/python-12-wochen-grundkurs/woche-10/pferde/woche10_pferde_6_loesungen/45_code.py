class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}")

pferd = Pferd("Blitz")
pferd.stelle_vor()
