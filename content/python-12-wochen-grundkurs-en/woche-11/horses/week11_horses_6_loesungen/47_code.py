class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Racehorse(Horse):
    def start(self):
        print("leaves the starting box.")

k = Racehorse("Blitz")
k.introduce()
