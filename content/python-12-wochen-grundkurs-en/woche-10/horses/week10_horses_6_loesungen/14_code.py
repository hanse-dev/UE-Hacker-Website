class Horse:
    def __init__(self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender

    def feed(self):
        print(f"{self.name} is eating. Munch! 🐴")

    def introduce(self):
        print(f"{self.name} – {self.breed} ({self.gender})")

bella = Horse("Bella", "Warmblood", "Mare")
max_horse = Horse("Max", "Pony", "Stallion")

bella.introduce()
max_horse.introduce()
bella.feed()
max_horse.feed()