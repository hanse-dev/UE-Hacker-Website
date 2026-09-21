class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

hero = Hero("Aria")
hero.introduce()
