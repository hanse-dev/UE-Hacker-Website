class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Jumper(Horse):
    def run(self):
        print(f"{self.name} jumps the fence.")

Horse("Sturm").run()
Jumper("Stella").run()
