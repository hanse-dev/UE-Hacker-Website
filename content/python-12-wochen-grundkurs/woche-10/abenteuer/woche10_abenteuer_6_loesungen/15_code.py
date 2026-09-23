class Held:
    def __init__(self, name):
        self.name = name
        self.level = 1

    def trainiere(self):
        self.level += 1
        print(f"{self.name} trainiert: Level {self.level}")

held = Held("Aria")
held.trainiere()
held.trainiere()
