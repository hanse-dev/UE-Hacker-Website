class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}.")

hero = Hero("Aria", 2)
hero.introduce()
