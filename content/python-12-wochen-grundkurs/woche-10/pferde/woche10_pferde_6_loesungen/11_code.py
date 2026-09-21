class Pferd:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

pferd = Pferd("Blitz", 2)
pferd.stelle_vor()
