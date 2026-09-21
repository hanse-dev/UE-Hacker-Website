class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Racehorse(Horse):
    pass

class Jumper(Horse):
    pass

k = Racehorse("Blitz")
print(isinstance(k, Horse))
print(isinstance(k, Jumper))
