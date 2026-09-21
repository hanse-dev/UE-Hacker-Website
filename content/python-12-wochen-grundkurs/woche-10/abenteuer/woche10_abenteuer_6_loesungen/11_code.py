class Held:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

held = Held("Aria", 2)
held.stelle_vor()
