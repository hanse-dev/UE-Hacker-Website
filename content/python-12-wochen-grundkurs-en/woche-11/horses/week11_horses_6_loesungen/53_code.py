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

k = Racehorse("Blitz")
print(f"{k.name}: {k.speed}")
