# Solution suggestion Boss Quest 1 – The Riding School Hierarchy

# Step 1: Base class
class Rider:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def lesson(self):
        print(f"{self.name} (Level {self.level}): General riding lesson.")

    def __str__(self):
        return f"Rider {self.name} | Level: {self.level}"

# Step 2: Levels
class Beginner(Rider):
    def __init__(self, name):
        super().__init__(name, 1)

    def lesson(self):
        print(f"{self.name} (Beginner): Learning sitting posture, walk and trot. Helmet on!")

class Intermediate(Rider):
    def __init__(self, name):
        super().__init__(name, 2)

    def lesson(self):
        print(f"{self.name} (Intermediate): Practicing canter, lateral movements and first jumps.")

class Pro(Rider):
    def __init__(self, name):
        super().__init__(name, 3)

    def lesson(self):
        print(f"{self.name} (Pro): Grand Prix dressage, show jumping and tournament preparation.")

# Step 3: Riding school with polymorphism
riding_school = [
    Beginner("Mia"),
    Intermediate("Jonas"),
    Pro("Sarah")
]

print("=== SONNENTAL RIDING SCHOOL ===")
for rider in riding_school:
    print(rider)          # __str__
    rider.lesson()
    print()
