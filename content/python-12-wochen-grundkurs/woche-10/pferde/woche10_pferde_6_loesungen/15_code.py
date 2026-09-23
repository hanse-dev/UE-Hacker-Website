class Pferd:
    def __init__(self, name):
        self.name = name
        self.level = 1

    def trainiere(self):
        self.level += 1
        print(f"{self.name} trainiert: Level {self.level}")

pferd = Pferd("Blitz")
pferd.trainiere()
pferd.trainiere()
