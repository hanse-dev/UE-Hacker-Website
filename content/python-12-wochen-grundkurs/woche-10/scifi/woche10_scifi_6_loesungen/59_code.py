class Roboter:
    def __init__(self, name):
        self.name = name
        self.energie = 100

    def arbeite(self, kosten):
        self.energie -= kosten
        if self.energie < 0:
            self.energie = 0

roboter = Roboter("Nova")
roboter.arbeite(40)
roboter.arbeite(40)
roboter.arbeite(40)
print(f"Energie: {roboter.energie}")
