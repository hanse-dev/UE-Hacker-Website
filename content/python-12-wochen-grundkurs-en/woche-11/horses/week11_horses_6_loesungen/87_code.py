class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

    def power(self):
        return 10

class Racehorse(Horse):
    def __init__(self, name, speed=30):
        super().__init__(name)
        self.speed = speed

    def run(self):
        print(f"{self.name} sprints down the track.")

    def power(self):
        return self.speed

class Jumper(Horse):
    def __init__(self, name, height=50):
        super().__init__(name)
        self.height = height

    def run(self):
        print(f"{self.name} jumps the fence.")

    def power(self):
        return self.height

klassen = {"Racehorse": Racehorse, "Jumper": Jumper}
f = klassen["Racehorse"]("Blitz")
f.run()
