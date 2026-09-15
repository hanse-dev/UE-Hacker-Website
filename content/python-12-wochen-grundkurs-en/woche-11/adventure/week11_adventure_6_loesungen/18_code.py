# Solution suggestion Boss Quest 1 – The Guild System

# Step 1: Base class
class Member:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def show_rights(self):
        print(f"{self.name} ({self.rank}): Basic Guild rights")

    def __str__(self):
        return f"[{self.rank}] {self.name}"

# Step 2: Specialisations
class Apprentice(Member):
    def __init__(self, name):
        super().__init__(name, "Apprentice")

    def show_rights(self):
        print(f"{self.name} ({self.rank}): May use the library and join simple missions.")

class Journeyman(Member):
    def __init__(self, name):
        super().__init__(name, "Journeyman")

    def show_rights(self):
        print(f"{self.name} ({self.rank}): May choose missions, train apprentices and use the camp.")

class Master(Member):
    def __init__(self, name):
        super().__init__(name, "Master")

    def show_rights(self):
        print(f"{self.name} ({self.rank}): Full rights – create missions, decide on admissions, manage the treasury.")

# Step 3: Polymorphism in action
guild = [
    Apprentice("Finn"),
    Journeyman("Rowan"),
    Master("Seraphina")
]

print("=== GUILD MEMBERS ===")
for member in guild:
    print(member)           # uses __str__
    member.show_rights()
    print()
