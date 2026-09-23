class Roboter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

roboter = Roboter("Nova", 2)
roboter.stelle_vor()
