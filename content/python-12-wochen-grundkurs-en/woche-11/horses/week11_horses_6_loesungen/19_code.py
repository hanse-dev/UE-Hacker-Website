class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Racehorse(Horse):
    def __init__(self, name, speed=30):
        super().__init__(name)
        self.speed = speed

    def run(self):
        print(f"{self.name} sprints down the track.")

class Champion(Racehorse):
    def run(self):
        super().run()
        print(f"{self.name} is a master!")

Champion("Blitz").run()
