class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

horse = Horse("Blitz")
horse.introduce()
