class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Jumper(Horse):
    def start(self):
        print(f"{self.name} leaves the starting box.")

k = Jumper("Stella")
k.introduce()
k.start()
