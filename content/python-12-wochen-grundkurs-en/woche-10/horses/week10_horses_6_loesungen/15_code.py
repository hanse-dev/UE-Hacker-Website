class Horse:
    def __init__(self, name):
        self.name = name
        self.level = 1

    def train(self):
        self.level += 1
        print(f"{self.name} trains: Level {self.level}")

horse = Horse("Blitz")
horse.train()
horse.train()
