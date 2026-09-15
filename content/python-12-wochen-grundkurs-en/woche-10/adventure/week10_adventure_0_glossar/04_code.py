class Hero:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}!")

    def level_up(self):
        self.level += 1
        print(f"{self.name} is now Level {self.level}!")

# Create objects
hero1 = Hero("Aria")
hero2 = Hero("Borin", level=3)

hero1.introduce()   # I am Aria, Level 1!
hero1.level_up()    # Aria is now Level 2!
print(hero2.level)  # 3
