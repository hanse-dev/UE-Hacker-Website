class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}")

roboter = Roboter("Nova")
roboter.stelle_vor()
