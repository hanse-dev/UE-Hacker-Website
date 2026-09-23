class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Jumper(Horse):
    def __init__(self, name, height=50):
        super().__init__(name)
        self.height = height

k = Jumper("Stella")
print(k.name, k.height)
